#!/usr/bin/env python3
"""Audit structured-authoring adoption across the OWOS course portfolio."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from course_compiler import (
    COMPILER_VERSION,
    ModulePackageError,
    validate_package,
)
from course_distinctiveness import audit as audit_distinctiveness


ROOT = Path(__file__).resolve().parents[1]
COMPILER_CONTRACT = "owos-course-compiler/1"


def audit_course(course_dir: Path) -> dict:
    record = yaml.safe_load(
        (course_dir / "course.yaml").read_text(encoding="utf-8")
    ) or {}
    chapters = int((record.get("structure") or {}).get("chapters", 0))
    authoring_path = course_dir / ".course/authoring.json"
    errors: list[str] = []
    if not authoring_path.is_file():
        return {
            "course": course_dir.name,
            "title": record.get("title", course_dir.name),
            "chapters": chapters,
            "status": "unmanifested",
            "structured_modules": 0,
            "legacy_modules": chapters,
            "compiler_contract": None,
            "compiler_version": None,
            "distinctiveness_gate": "unknown",
            "errors": ["missing .course/authoring.json"],
        }

    authoring = json.loads(authoring_path.read_text(encoding="utf-8"))
    migration = authoring.get("migration_state") or {}
    structured_names = migration.get("structured_modules") or []
    legacy = int(migration.get("legacy_html_modules_remaining", 0))
    if not isinstance(structured_names, list):
        errors.append("migration_state.structured_modules must be a list")
        structured_names = []
    if authoring.get("compiler_contract") != COMPILER_CONTRACT:
        errors.append(f"compiler_contract must be {COMPILER_CONTRACT}")
    if authoring.get("compiler_version") != COMPILER_VERSION:
        errors.append(
            f"compiler_version must be {COMPILER_VERSION}"
        )
    if len(structured_names) + legacy != chapters:
        errors.append(
            "structured plus legacy module count does not equal course chapters"
        )

    architecture_path = course_dir / ".course/experience-architecture.json"
    architecture = {}
    if architecture_path.is_file():
        architecture = json.loads(architecture_path.read_text(encoding="utf-8"))
    lesson_inventory = architecture.get("lessons") or {}
    package_results = []
    for module_name in structured_names:
        package_dir = course_dir / str(
            authoring.get("module_directory", "modules")
        ) / str(module_name)
        try:
            package = validate_package(package_dir)
        except ModulePackageError as error:
            errors.append(f"{module_name}: {error}")
            continue

        matches = [
            lesson_name
            for lesson_name, config in lesson_inventory.items()
            if isinstance(config, dict)
            and config.get("structured_package")
            == package_dir.relative_to(course_dir).as_posix()
        ]
        if len(matches) != 1:
            errors.append(
                f"{module_name}: expected one compiled lesson mapping, found {len(matches)}"
            )
            continue
        lesson = course_dir / "curriculum" / matches[0]
        if not lesson.is_file():
            errors.append(f"{module_name}: compiled curriculum lesson is missing")
            continue
        soup = BeautifulSoup(lesson.read_text(encoding="utf-8"), "html.parser")
        checksum = soup.find("meta", attrs={"name": "owos-package-checksum"})
        compiler = soup.find("meta", attrs={"name": "owos-compiler-version"})
        if not checksum or checksum.get("content") != package["checksum"]:
            errors.append(
                f"{module_name}: compiled checksum does not match source package"
            )
        if not compiler or compiler.get("content") != COMPILER_VERSION:
            errors.append(
                f"{module_name}: compiled compiler version is stale"
            )
        package_results.append(
            {
                "module": module_name,
                "lesson": matches[0],
                "checksum": package["checksum"],
                "compiler_version": package["compiler_version"],
            }
        )

    try:
        distinctiveness = audit_distinctiveness(course_dir)
        distinctiveness_status = distinctiveness["status"]
    except (FileNotFoundError, KeyError, ValueError, SystemExit):
        distinctiveness_status = "not_configured"

    if errors:
        status = "invalid"
    elif legacy == 0 and len(structured_names) == chapters:
        status = "fully_structured"
    elif structured_names:
        status = "hybrid_migration"
    else:
        status = "legacy_pending_migration"
    return {
        "course": course_dir.name,
        "title": record.get("title", course_dir.name),
        "chapters": chapters,
        "status": status,
        "structured_modules": len(structured_names),
        "legacy_modules": legacy,
        "compiler_contract": authoring.get("compiler_contract"),
        "compiler_version": authoring.get("compiler_version"),
        "distinctiveness_gate": distinctiveness_status,
        "verified_packages": package_results,
        "errors": errors,
    }


def markdown_report(result: dict) -> str:
    rows = []
    for course in result["courses"]:
        rows.append(
            "| {title} | {chapters} | {structured_modules} | {legacy_modules} | "
            "{status} | {distinctiveness_gate} |".format(**course)
        )
    return f"""# Structured Authoring Migration Status

Generated by `tools/audit-structured-authoring.py`.

Compiler contract: `{COMPILER_CONTRACT}`
Compiler implementation: `{COMPILER_VERSION}`

| Course | Modules | Structured | Legacy | Migration truth | Distinctiveness gate |
| --- | ---: | ---: | ---: | --- | --- |
{chr(10).join(rows)}

## Portfolio truth

- Total governed modules: {result["totals"]["modules"]}
- Verified structured modules: {result["totals"]["structured_modules"]}
- Legacy modules still requiring conversion: {result["totals"]["legacy_modules"]}
- Portfolio audit status: {result["status"]}

The compiler standard governs all courses listed here. It does not retroactively turn legacy HTML
into structured source. A module counts as structured only when its package validates and its
compiled curriculum lesson carries the matching source checksum and compiler version.

Distinctiveness is a separate gate. The compiler guarantees source separation, deterministic
rendering, real-asset resolution, component contracts, completion evidence, and reproducibility.
Unique learning design comes from the approved course identity, module fingerprint, storyboard,
visual manifest, signature mechanism, adjacent-module comparison, rendered review, and
course-level distinctiveness audit.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", type=Path)
    args = parser.parse_args()

    courses = [
        audit_course(path)
        for path in sorted((ROOT / "apps").iterdir())
        if path.is_dir()
        and not path.name.startswith("_")
        and (path / "course.yaml").is_file()
    ]
    totals = {
        "modules": sum(course["chapters"] for course in courses),
        "structured_modules": sum(
            course["structured_modules"] for course in courses
        ),
        "legacy_modules": sum(course["legacy_modules"] for course in courses),
    }
    result = {
        "compiler_contract": COMPILER_CONTRACT,
        "compiler_version": COMPILER_VERSION,
        "status": (
            "passed" if all(not course["errors"] for course in courses) else "failed"
        ),
        "totals": totals,
        "courses": courses,
    }
    if args.write_report:
        output = args.write_report
        if not output.is_absolute():
            output = ROOT / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
