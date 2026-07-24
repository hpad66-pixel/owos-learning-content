#!/usr/bin/env python3
"""Regression tests for the full-module gate in the generic release builder."""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
import tempfile
from pathlib import Path

import yaml


REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "apps/meaning-before-models"
STEM = "module-09-reasoning-and-inference-with-owl"
SPEC = importlib.util.spec_from_file_location(
    "build_course_release", REPO / "tools/build-course-release.py"
)
if SPEC is None or SPEC.loader is None:
    raise AssertionError("could not load generic release builder")
release_builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release_builder)


def approve_fixture_qa(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"^release_status:\s*\S+\s*$",
        "release_status: approved",
        text,
        flags=re.M,
    )
    for gate in (
        "Accuracy and evidence",
        "Learning design",
        "Course distinctiveness",
        "Utility-practitioner review",
        "Technical and accessibility review",
        "Release control",
    ):
        text = re.sub(
            rf"^(\|\s*{re.escape(gate)}\s*\|)\s*[^|]+(\|.*)$",
            rf"\1 passed \2",
            text,
            flags=re.M,
        )
    text = text.replace("- [ ]", "- [x]")
    text = re.sub(
        r"^\|\s*Release\s*\|.*$",
        "| Release | Fixture Human Reviewer | 2026-07-23 | Approved for fixture release test |",
        text,
        flags=re.M,
    )
    path.write_text(text, encoding="utf-8")


def fixture(root: Path, contract_version: int = 3) -> Path:
    course = root / "apps/fixture-course"
    for relative in (
        ".course",
        "curriculum/design-briefs",
        "curriculum/scripts",
        "qa",
        "dist/site",
    ):
        (course / relative).mkdir(parents=True, exist_ok=True)

    source_lesson = SOURCE / "curriculum" / f"{STEM}.html"
    shutil.copy(source_lesson, course / "curriculum" / f"{STEM}.html")
    shutil.copy(
        SOURCE / "curriculum/meaning-fieldbook.css",
        course / "curriculum/meaning-fieldbook.css",
    )
    shutil.copy(
        source_lesson,
        course / "dist/site/lesson-fixture-09-inference.html",
    )
    shutil.copy(
        SOURCE / "curriculum/meaning-fieldbook.css",
        course / "dist/site/meaning-fieldbook.css",
    )
    shutil.copy(
        SOURCE / "curriculum/design-briefs" / f"{STEM}.md",
        course / "curriculum/design-briefs" / f"{STEM}.md",
    )
    shutil.copy(
        SOURCE / "qa" / f"{STEM}-quality-control-report.md",
        course / "qa" / f"{STEM}-quality-control-report.md",
    )
    approve_fixture_qa(course / "qa" / f"{STEM}-quality-control-report.md")
    shutil.copy(
        SOURCE / "curriculum/scripts" / f"{STEM}-video-script.md",
        course / "curriculum/scripts" / f"{STEM}-video-script.md",
    )
    shutil.copy(
        SOURCE / ".course/full-module-contract.json",
        course / ".course/full-module-contract.json",
    )
    architecture = {
        "minimum_archetypes": 1,
        "full_module_conformance": {
            "script_policy": "if-present",
        },
        "thresholds": {
            "maximum_archetype_share": 1.0,
            "maximum_identical_quiz_sequence_count": 2,
            "maximum_identical_interaction_signature_count": 2,
            "maximum_adjacent_structural_similarity": 1.0,
            "maximum_repeated_faq_question_count": 2,
            "maximum_repeated_instructor_paragraph_count": 3,
            "factory_pattern_share": 1.0,
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
    (course / "curriculum/SYLLABUS.md").write_text(
        "# Fixture syllabus\n", encoding="utf-8"
    )
    (course / "dist/site/course-fixture.html").write_text(
        "<!doctype html><html><body><main><h1>Fixture</h1></main></body></html>\n",
        encoding="utf-8",
    )
    quality_contract = {
        "version": contract_version,
        "enforce_on_release": True,
        "minimum_purposeful_interactions": 1,
        "course_distinctiveness_required": True,
    }
    if contract_version >= 3:
        quality_contract["full_module_conformance_required"] = True
    record = {
        "schema_version": 1,
        "course_id": "owos-course-fixture-001",
        "slug": "fixture-course",
        "title": "Fixture Course",
        "status": "working-review",
        "course_version": "0.1.0",
        "release_date": "2026-07-23",
        "quality_contract": quality_contract,
        "provenance": {
            "repository": "example/fixture",
            "ref": "main",
            "content_baseline_commit": "fixture",
        },
        "structure": {"chapters": 1},
        "source_files": {"syllabus": "curriculum/SYLLABUS.md"},
        "delivery": {
            "landing_output": "dist/site/course-fixture.html",
            "available_chapters": 1,
            "released_chapters": ["09"],
            "runtime_store_key": "fixture",
            "runtime_canonical": "/course-fixture",
            "runtime_repository": "example/runtime",
            "runtime_path": "site",
            "learner_records": "test",
            "semantic_alignment": "test",
            "edge_delivery": "test",
        },
    }
    (course / "course.yaml").write_text(
        yaml.safe_dump(record, sort_keys=False),
        encoding="utf-8",
    )
    return course


with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    release_builder.ROOT = root
    course = fixture(root)
    result = release_builder.build(course)
    quality = result["course"]["quality_contract"]
    if quality.get("full_module_conformance") != "passed":
        raise AssertionError("version 3 release did not record full-module conformance")
    if quality.get("full_modules_validated") != 1:
        raise AssertionError("version 3 release did not record the validated lesson count")
    evidence = quality.get("full_module_evidence", [])
    if len(evidence) != 1 or not evidence[0]["evidence"]["qa"].get("sha256"):
        raise AssertionError("version 3 release did not checksum per-lesson evidence")

    record_path = course / "course.yaml"
    record = yaml.safe_load(record_path.read_text(encoding="utf-8"))
    record["quality_contract"].pop("full_module_conformance_required")
    record_path.write_text(
        yaml.safe_dump(record, sort_keys=False),
        encoding="utf-8",
    )
    try:
        release_builder.build(course)
    except SystemExit as error:
        if "version 3 or later requires" not in str(error):
            raise AssertionError(f"unexpected version 3 contract failure: {error}") from error
    else:
        raise AssertionError("version 3 release accepted an omitted full-module gate")
    record["quality_contract"]["full_module_conformance_required"] = True
    record_path.write_text(
        yaml.safe_dump(record, sort_keys=False),
        encoding="utf-8",
    )

    (course / "qa" / f"{STEM}-quality-control-report.md").unlink()
    try:
        release_builder.build(course)
    except SystemExit as error:
        if "whole-course full-module conformance gate failed" not in str(error):
            raise AssertionError(f"unexpected release failure: {error}") from error
    else:
        raise AssertionError("version 3 release accepted a missing module QA report")

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    release_builder.ROOT = root
    course = fixture(root, contract_version=2)
    (course / "qa" / f"{STEM}-quality-control-report.md").unlink()
    result = release_builder.build(course)
    if "full_module_conformance" in result["course"]["quality_contract"]:
        raise AssertionError("legacy contract incorrectly claimed the new conformance gate")

print(
    "Course release full-conformance QA passed: version 3 requires and records the "
    "whole-course gate; version 2 remains backward-compatible without claiming it."
)
