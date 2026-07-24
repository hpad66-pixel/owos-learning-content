#!/usr/bin/env python3
"""Regression tests for whole-course full-module conformance."""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from course_full_conformance import CourseFullConformanceError, audit


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "apps/meaning-before-models"
STEM = "module-09-reasoning-and-inference-with-owl"


def make_course(root: Path) -> Path:
    course = root / "fixture-course"
    for relative in (
        ".course",
        "curriculum/design-briefs",
        "curriculum/scripts",
        "qa",
    ):
        (course / relative).mkdir(parents=True, exist_ok=True)
    shutil.copy(
        SOURCE / "curriculum" / f"{STEM}.html",
        course / "curriculum" / f"{STEM}.html",
    )
    shutil.copy(
        SOURCE / "curriculum/meaning-fieldbook.css",
        course / "curriculum/meaning-fieldbook.css",
    )
    shutil.copy(
        SOURCE / "curriculum/design-briefs" / f"{STEM}.md",
        course / "curriculum/design-briefs" / f"{STEM}.md",
    )
    shutil.copy(
        SOURCE / "qa" / f"{STEM}-quality-control-report.md",
        course / "qa" / f"{STEM}-quality-control-report.md",
    )
    shutil.copy(
        SOURCE / "curriculum/scripts" / f"{STEM}-video-script.md",
        course / "curriculum/scripts" / f"{STEM}-video-script.md",
    )
    shutil.copy(
        SOURCE / ".course/full-module-contract.json",
        course / ".course/full-module-contract.json",
    )
    architecture = {
        "full_module_conformance": {
            "lesson_directory": "curriculum",
            "brief_directory": "curriculum/design-briefs",
            "qa_directory": "qa",
            "script_directory": "curriculum/scripts",
            "contract": ".course/full-module-contract.json",
            "script_policy": "if-present",
        },
        "lessons": {
            f"{STEM}.html": {
                "archetype": "model-courtroom",
                "signature_mechanism": "test-inference",
                "opening": "unexplained-claim",
                "work_product_mode": "decision-card",
            }
        },
    }
    (course / ".course/experience-architecture.json").write_text(
        json.dumps(architecture, indent=2) + "\n",
        encoding="utf-8",
    )
    return course


def expect_failure(course: Path, phrase: str) -> None:
    try:
        audit(course)
    except CourseFullConformanceError as error:
        if phrase not in str(error):
            raise AssertionError(f"expected {phrase!r}, received {error!r}") from error
    else:
        raise AssertionError(f"whole-course conformance accepted missing {phrase}")


with tempfile.TemporaryDirectory() as directory:
    course = make_course(Path(directory))
    result = audit(course)
    if result["included_lessons"] != 1:
        raise AssertionError("whole-course runner did not validate the included lesson")
    evidence = result["lessons"][0]["evidence"]
    if not all(evidence[key] for key in ("brief", "qa", "script", "contract")):
        raise AssertionError("whole-course result does not trace every resolved evidence file")
    try:
        audit(course, require_release_ready=True)
    except CourseFullConformanceError as error:
        if "release_status: approved" not in str(error):
            raise AssertionError(f"unexpected release-ready failure: {error}") from error
    else:
        raise AssertionError("release-ready conformance accepted blocked manual approvals")

    script = course / "curriculum/scripts" / f"{STEM}-video-script.md"
    valid_script = script.read_text(encoding="utf-8")
    script.write_text("# Invalid script\n", encoding="utf-8")
    expect_failure(course, "recording script is missing marker")
    script.write_text(valid_script, encoding="utf-8")

    qa = course / "qa" / f"{STEM}-quality-control-report.md"
    qa.unlink()
    expect_failure(course, "missing")

with tempfile.TemporaryDirectory() as directory:
    course = make_course(Path(directory))
    shutil.copy(
        SOURCE / "curriculum/module-08-ask-the-graph-with-sparql.html",
        course / "curriculum/module-08-ask-the-graph-with-sparql.html",
    )
    expect_failure(course, "missing from experience architecture")

with tempfile.TemporaryDirectory() as directory:
    course = make_course(Path(directory))
    (course / "curriculum/design-briefs" / f"{STEM}.md").unlink()
    expect_failure(course, "module design brief")

with tempfile.TemporaryDirectory() as directory:
    course = make_course(Path(directory))
    (course / ".course/full-module-contract.json").unlink()
    expect_failure(course, "full-module contract")

print(
    "Whole-course full-module conformance QA passed: complete evidence accepted, "
    "invalid scripts, missing briefs, missing QA, missing contracts, and "
    "undeclared lessons blocked."
)
