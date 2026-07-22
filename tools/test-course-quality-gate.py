#!/usr/bin/env python3
"""Regression tests for the machine-enforced OWOS course quality gate."""

from __future__ import annotations

import tempfile
from pathlib import Path

from course_quality import CourseQualityError, validate_lesson


ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "apps/data-ai-governance/dist/site/lesson-dg-09-d02-accountability-and-stewardship.html"
CONTRACT = {"minimum_purposeful_interactions": 2}


def must_fail(text: str, expected: str) -> None:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "lesson.html"
        path.write_text(text, encoding="utf-8")
        try:
            validate_lesson(path, CONTRACT)
        except CourseQualityError as error:
            if expected not in str(error):
                raise AssertionError(f"expected {expected!r}, received {error!r}") from error
        else:
            raise AssertionError(f"quality gate accepted a lesson missing {expected}")


lesson = LESSON.read_text(encoding="utf-8")
result = validate_lesson(LESSON, CONTRACT)
if result["purposeful_interactions"] < 2:
    raise AssertionError("golden lesson needs at least two purposeful interactions")

must_fail(lesson.replace("Maya Torres", "undefined", 1), "undefined sentinel")
must_fail(lesson.replace("prefers-reduced-motion", "motion-preference-removed"), "reduced-motion")
must_fail(
    lesson.replace(
        '"headers":["Responsibility","Utility","Supplier","Minimum proof"]',
        '"headers":[]',
        1,
    ),
    "non-empty headers",
)

print("OWOS course quality gate QA passed: valid release accepted and three regressions blocked.")
