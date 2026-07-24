#!/usr/bin/env python3
"""Run the course-level experience gate for every governed OWOS course."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

from course_distinctiveness import audit


ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "apps"


def governed_courses() -> list[Path]:
    courses = []
    for record_path in sorted(APPS.glob("*/course.yaml")):
        if record_path.parent.name.startswith("_"):
            continue
        record = yaml.safe_load(record_path.read_text(encoding="utf-8")) or {}
        quality = record.get("quality_contract") or {}
        if quality.get("course_distinctiveness_required") is True:
            courses.append(record_path.parent)
    return courses


failures = []
courses = governed_courses()
if not courses:
    raise AssertionError("no courses require the course-level experience gate")

for course in courses:
    result = audit(course)
    print(
        f"{course.name}: {result['status']}, {result['lessons']} lessons, "
        f"{len(result['archetypes'])} archetypes"
    )
    if result["status"] != "passed":
        failures.append((course.name, result["errors"]))

if failures:
    for course_name, errors in failures:
        print(f"\n{course_name} blockers:", file=sys.stderr)
        for error in errors[:20]:
            print(f"- {error}", file=sys.stderr)
    raise SystemExit(
        f"\n{len(failures)} governed course experience audit(s) are blocked."
    )

print(f"All {len(courses)} governed OWOS course experience audits passed.")
