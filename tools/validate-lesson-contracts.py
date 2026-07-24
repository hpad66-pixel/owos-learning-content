#!/usr/bin/env python3
"""Validate planned OWOS lesson contracts before module design begins."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TOP_LEVEL = {
    "schema_version",
    "status",
    "course_id",
    "module",
    "learning_job",
    "depth",
    "experience",
    "evidence",
    "sequence",
}
REQUIRED_MODULE = {"id", "number", "title", "part", "curriculum_role"}
REQUIRED_LEARNING = {
    "learner_question",
    "outcome",
    "prior_knowledge",
    "misconception",
    "transfer_task",
}
REQUIRED_DEPTH = {"common_route", "practitioner", "leader"}
REQUIRED_EXPERIENCE = {
    "archetype",
    "opening",
    "mental_model",
    "signature_mechanism",
    "visual_jobs",
    "assessment_jobs",
    "work_product",
    "capstone_contribution",
}
REQUIRED_EVIDENCE = {"source_refs", "claim_refs", "boundary"}
REQUIRED_SEQUENCE = {"requires", "prepares"}


def missing_fields(record: dict, required: set[str]) -> list[str]:
    return sorted(
        field
        for field in required
        if record.get(field) in (None, "", [])
        and field not in {"requires", "prepares"}
    )


def declared_ids(path: Path, prefix: str) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(rf"\|\s*({re.escape(prefix)}-\d+)\s*\|", text))


def validate(course_dir: Path) -> dict:
    course_record = yaml.safe_load(
        (course_dir / "course.yaml").read_text(encoding="utf-8")
    ) or {}
    planned = course_record.get("planned_structure") or {}
    expected = int(planned.get("chapters", 0))
    contracts = sorted((course_dir / "modules").glob("*/lesson-contract.yaml"))
    errors: list[str] = []
    if expected <= 0:
        errors.append("course.yaml must declare planned_structure.chapters")
    if len(contracts) != expected:
        errors.append(
            f"expected {expected} lesson contracts, found {len(contracts)}"
        )

    source_ids = declared_ids(
        course_dir / "research/SOURCE-REGISTER.md", "SRC"
    ) | declared_ids(course_dir / "research/SOURCE-REGISTER.md", "DIR")
    claim_ids = declared_ids(course_dir / "research/CLAIMS-REGISTER.md", "CLM")
    module_ids: set[str] = set()
    numbers: set[int] = set()
    parsed = []

    for path in contracts:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as error:
            errors.append(f"{path.name}: invalid YAML: {error}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.name}: contract must be an object")
            continue
        if data.get("schema_version") != 1:
            errors.append(f"{path.name}: schema_version must be 1")
        missing = missing_fields(data, REQUIRED_TOP_LEVEL)
        if missing:
            errors.append(f"{path.name}: missing top-level fields {missing}")
            continue
        for label, record, required in (
            ("module", data["module"], REQUIRED_MODULE),
            ("learning_job", data["learning_job"], REQUIRED_LEARNING),
            ("depth", data["depth"], REQUIRED_DEPTH),
            ("experience", data["experience"], REQUIRED_EXPERIENCE),
            ("evidence", data["evidence"], REQUIRED_EVIDENCE),
            ("sequence", data["sequence"], REQUIRED_SEQUENCE),
        ):
            if not isinstance(record, dict):
                errors.append(f"{path.name}: {label} must be an object")
                continue
            fields = missing_fields(record, required)
            if fields:
                errors.append(f"{path.name}: {label} is missing {fields}")

        module_id = str(data["module"].get("id", ""))
        number = data["module"].get("number")
        if module_id in module_ids:
            errors.append(f"{path.name}: duplicate module id {module_id}")
        module_ids.add(module_id)
        if not isinstance(number, int):
            errors.append(f"{path.name}: module number must be an integer")
        elif number in numbers:
            errors.append(f"{path.name}: duplicate module number {number}")
        else:
            numbers.add(number)
        for field in ("visual_jobs", "assessment_jobs"):
            values = data["experience"].get(field)
            if not isinstance(values, list) or len(values) < 2:
                errors.append(
                    f"{path.name}: experience.{field} needs at least two jobs"
                )
        unknown_sources = sorted(
            set(data["evidence"].get("source_refs", [])) - source_ids
        )
        unknown_claims = sorted(
            set(data["evidence"].get("claim_refs", [])) - claim_ids
        )
        if unknown_sources:
            errors.append(f"{path.name}: unknown source refs {unknown_sources}")
        if unknown_claims:
            errors.append(f"{path.name}: unknown claim refs {unknown_claims}")
        text = path.read_text(encoding="utf-8")
        if "—" in text or "–" in text:
            errors.append(f"{path.name}: prohibited dash punctuation")
        parsed.append((path, data))

    expected_numbers = set(range(1, expected + 1))
    if numbers != expected_numbers:
        errors.append(
            f"module numbers must be continuous 1 through {expected}"
        )
    for path, data in parsed:
        references = set(data["sequence"].get("requires", [])) | set(
            data["sequence"].get("prepares", [])
        )
        unknown = sorted(references - module_ids)
        if unknown:
            errors.append(f"{path.name}: unknown sequence module ids {unknown}")
        if data["module"]["id"] in references:
            errors.append(f"{path.name}: module cannot depend on itself")

    if errors:
        raise ValueError("\n".join(f"- {error}" for error in errors))
    return {
        "course": course_dir.name,
        "contracts": len(contracts),
        "module_ids": sorted(module_ids),
        "status": "lesson contract gate passed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", required=True)
    args = parser.parse_args()
    course_dir = ROOT / "apps" / args.course
    try:
        result = validate(course_dir)
    except (FileNotFoundError, ValueError, yaml.YAMLError) as error:
        print(f"OWOS lesson contract gate failed:\n{error}", file=sys.stderr)
        return 1
    print(
        f"{result['course']}: {result['contracts']} contracts, "
        f"{result['status']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
