#!/usr/bin/env python3
"""Validate the Version 4 implementation bundle and its cross-file contracts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml


HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent


REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "COPY-PASTE-AGENT-HANDOFF.md",
    "implementation-edition.md",
    "work-packages.yaml",
    "acceptance-matrix.yaml",
    "openapi.yaml",
    "agent-tools.yaml",
    "formula-contract-template.yaml",
    "intake.yaml",
    "sources.yaml",
    "claims.yaml",
    "decisions.yaml",
    "qa.yaml",
    "approvals.yaml",
    "golden-cases/golden-case-register.yaml",
]


EXAMPLE_SCHEMA_MAP = {
    "examples/analysis-request.example.json": "schemas/analysis-request.schema.json",
    "examples/input-snapshot.example.json": "schemas/input-snapshot.schema.json",
    "examples/result-envelope.example.json": "schemas/result-envelope.schema.json",
    "examples/model-run-not-run.example.json": "schemas/model-run.schema.json",
}


def walk_yaml_and_json() -> tuple[list[Path], list[Path], list[str]]:
    yaml_files = sorted(BUNDLE.rglob("*.yaml"))
    json_files = sorted(BUNDLE.rglob("*.json"))
    errors: list[str] = []
    for path in yaml_files:
        try:
            yaml.safe_load(path.read_text())
        except Exception as exc:
            errors.append(f"YAML parse failed for {path.relative_to(BUNDLE)}: {exc}")
    for path in json_files:
        try:
            json.loads(path.read_text())
        except Exception as exc:
            errors.append(f"JSON parse failed for {path.relative_to(BUNDLE)}: {exc}")
    return yaml_files, json_files, errors


def has_type(instance: Any, expected: Any) -> bool:
    if isinstance(expected, list):
        return any(has_type(instance, item) for item in expected)
    mapping = {
        "object": dict,
        "array": list,
        "string": str,
        "number": (int, float),
        "integer": int,
        "boolean": bool,
        "null": type(None),
    }
    expected_type = mapping.get(expected)
    if expected_type is None:
        return True
    if expected == "number" and isinstance(instance, bool):
        return False
    if expected == "integer" and isinstance(instance, bool):
        return False
    return isinstance(instance, expected_type)


def validate_instance(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    if "type" in schema and not has_type(instance, schema["type"]):
        return [f"{path}: expected type {schema['type']}, got {type(instance).__name__}"]
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} is not in enum")
    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: string is shorter than minLength")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            errors.append(f"{path}: string does not match pattern {schema['pattern']}")
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if schema.get("minimum") is not None and instance < schema["minimum"]:
            errors.append(f"{path}: number is below minimum")
        if schema.get("maximum") is not None and instance > schema["maximum"]:
            errors.append(f"{path}: number is above maximum")
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: missing required property {key}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(instance) - set(properties)
            for key in sorted(extra):
                errors.append(f"{path}: unexpected property {key}")
        for key, value in instance.items():
            child_schema = properties.get(key)
            if isinstance(child_schema, dict):
                errors.extend(validate_instance(value, child_schema, f"{path}.{key}"))
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: fewer items than minItems")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, sort_keys=True) for item in instance]
            if len(serialized) != len(set(serialized)):
                errors.append(f"{path}: array items are not unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, value in enumerate(instance):
                errors.extend(validate_instance(value, item_schema, f"{path}[{index}]"))
    return errors


def validate_dependency_graph(work_packages: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids = [item["id"] for item in work_packages]
    if len(ids) != len(set(ids)):
        errors.append("work package identifiers are not unique")
    id_set = set(ids)
    graph: dict[str, list[str]] = {}
    for item in work_packages:
        dependencies = item.get("dependencies", [])
        graph[item["id"]] = dependencies
        for dependency in dependencies:
            if dependency not in id_set:
                errors.append(f"{item['id']} has unknown dependency {dependency}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"work package dependency cycle includes {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph.get(node, []):
            visit(dependency)
        visiting.remove(node)
        visited.add(node)

    for node in ids:
        visit(node)
    return errors


def main() -> None:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (BUNDLE / relative).is_file():
            errors.append(f"missing required file: {relative}")

    yaml_files, json_files, parse_errors = walk_yaml_and_json()
    errors.extend(parse_errors)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    work = yaml.safe_load((BUNDLE / "work-packages.yaml").read_text())
    acceptance = yaml.safe_load((BUNDLE / "acceptance-matrix.yaml").read_text())
    tools = yaml.safe_load((BUNDLE / "agent-tools.yaml").read_text())
    openapi = yaml.safe_load((BUNDLE / "openapi.yaml").read_text())
    sources = yaml.safe_load((BUNDLE / "sources.yaml").read_text())
    claims = yaml.safe_load((BUNDLE / "claims.yaml").read_text())

    work_packages = work["work_packages"]
    errors.extend(validate_dependency_graph(work_packages))

    acceptance_ids = [item["id"] for item in acceptance["acceptance_criteria"]]
    if len(acceptance_ids) != len(set(acceptance_ids)):
        errors.append("acceptance identifiers are not unique")
    acceptance_set = set(acceptance_ids)
    used_acceptance: list[str] = []
    for package in work_packages:
        used_acceptance.extend(package.get("acceptance_criteria", []))
        for criterion in package.get("acceptance_criteria", []):
            if criterion not in acceptance_set:
                errors.append(f"{package['id']} references unknown acceptance criterion {criterion}")
    unused_acceptance = acceptance_set - set(used_acceptance)
    if unused_acceptance:
        errors.append(f"unused acceptance criteria: {sorted(unused_acceptance)}")

    schema_ids: list[str] = []
    for path in sorted((BUNDLE / "schemas").glob("*.schema.json")):
        schema = json.loads(path.read_text())
        schema_id = schema.get("$id")
        if not schema_id:
            errors.append(f"{path.name} has no $id")
        else:
            schema_ids.append(schema_id)
    if len(schema_ids) != len(set(schema_ids)):
        errors.append("JSON Schema identifiers are not unique")

    for example_relative, schema_relative in EXAMPLE_SCHEMA_MAP.items():
        instance = json.loads((BUNDLE / example_relative).read_text())
        schema = json.loads((BUNDLE / schema_relative).read_text())
        for error in validate_instance(instance, schema):
            errors.append(f"{example_relative} against {schema_relative}: {error}")

    operation_ids: list[str] = []
    local_refs: list[str] = []

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "operationId":
                    operation_ids.append(child)
                if key == "$ref" and isinstance(child, str) and not child.startswith("#"):
                    local_refs.append(child)
                collect(child)
        elif isinstance(value, list):
            for child in value:
                collect(child)

    collect(openapi)
    if len(operation_ids) != len(set(operation_ids)):
        errors.append("OpenAPI operationId values are not unique")
    for ref in local_refs:
        ref_path = (BUNDLE / ref).resolve()
        if not ref_path.is_file():
            errors.append(f"OpenAPI local reference does not resolve: {ref}")

    tool_names = [item["name"] for item in tools["tools"]]
    if len(tool_names) != len(set(tool_names)):
        errors.append("agent tool names are not unique")
    prohibited = set(tools["globally_prohibited_tools"])
    overlap = prohibited.intersection(tool_names)
    if overlap:
        errors.append(f"permitted and prohibited tool lists overlap: {sorted(overlap)}")

    source_ids = {item["id"] for item in sources["sources"]}
    for claim in claims["claims"]:
        for source_id in claim.get("sources", []):
            if source_id not in source_ids:
                errors.append(f"{claim['id']} references unknown source {source_id}")
    for source in sources["sources"]:
        locator = source["locator"]
        if locator.startswith("current_") or locator.startswith("http"):
            continue
        path = (BUNDLE / locator).resolve()
        if not path.is_file():
            errors.append(f"source locator does not resolve: {locator}")

    handoff = (BUNDLE / "COPY-PASTE-AGENT-HANDOFF.md").read_text()
    required_handoff_markers = [
        "One sanitary-sewer basin",
        "The deterministic calculation engine computes registered formulas.",
        "Humans approve consequential findings",
        "Stop conditions",
        "WP-01",
    ]
    for marker in required_handoff_markers:
        if marker not in handoff:
            errors.append(f"agent handoff is missing marker: {marker}")

    for path in sorted(BUNDLE.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".json", ".py"}:
            continue
        text = path.read_text()
        if "\u2014" in text or "\u2013" in text:
            errors.append(f"prohibited Unicode dash found in {path.relative_to(BUNDLE)}")
        trailing = [line for line in text.splitlines() if line.rstrip() != line]
        if trailing:
            errors.append(f"trailing whitespace found in {path.relative_to(BUNDLE)}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    print(f"PASS: {len(REQUIRED_FILES)} required bundle files are present")
    print(f"PASS: {len(yaml_files)} YAML files and {len(json_files)} JSON files parse")
    print(f"PASS: {len(work_packages)} work packages have a valid acyclic dependency graph")
    print(f"PASS: {len(acceptance_ids)} acceptance criteria resolve exactly once")
    print(f"PASS: {len(schema_ids)} JSON Schema identifiers are unique")
    print(f"PASS: {len(EXAMPLE_SCHEMA_MAP)} examples satisfy the implemented structural schema checks")
    print(f"PASS: {len(operation_ids)} OpenAPI operation identifiers are unique")
    print(f"PASS: {len(local_refs)} OpenAPI local schema references resolve")
    print(f"PASS: {len(tool_names)} bounded agent tools and {len(prohibited)} globally prohibited tools are disjoint")
    print("PASS: claim source identifiers and local source locators resolve")
    print("PASS: agent handoff authority, stop, and first-assignment markers are present")

    qa_path = BUNDLE / "qa.yaml"
    qa = yaml.safe_load(qa_path.read_text())
    for key in [
        "bundle_validator",
        "yaml_parse",
        "json_parse",
        "schema_identifier_uniqueness",
        "work_package_dependency_graph",
        "acceptance_identifier_resolution",
        "openapi_operation_identifier_uniqueness",
        "example_structure",
        "source_path_resolution",
        "prohibited_punctuation",
    ]:
        qa["automated_checks"][key]["status"] = "passed"
    qa_path.write_text(yaml.safe_dump(qa, sort_keys=False, allow_unicode=False))

    manifest_path = BUNDLE / "build-manifest.yaml"
    if manifest_path.is_file():
        manifest = yaml.safe_load(manifest_path.read_text())
        manifest["validation"]["status"] = "passed"
        manifest_path.write_text(
            yaml.safe_dump(manifest, sort_keys=False, allow_unicode=False)
        )


if __name__ == "__main__":
    main()
