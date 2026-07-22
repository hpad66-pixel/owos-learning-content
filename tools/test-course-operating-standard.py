#!/usr/bin/env python3
"""Mechanical acceptance checks for OWOS Course Operating Standard 2.0."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STANDARD = ROOT / "core/standards/COURSE-OPERATING-STANDARD.md"
COURSE = ROOT / "apps/data-ai-governance/course.yaml"
SOURCE = ROOT / "apps/data-ai-governance/curriculum/module-09-d02-accountability-and-stewardship.html"
DIST = ROOT / "apps/data-ai-governance/dist/site/lesson-dg-09-d02-accountability-and-stewardship.html"
RELEASE = ROOT / "apps/data-ai-governance/dist/release-manifest.json"


def require(text: str, phrases: list[str], label: str) -> None:
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{label} is missing: {phrase}")


standard = STANDARD.read_text(encoding="utf-8")
course = COURSE.read_text(encoding="utf-8")
source = SOURCE.read_text(encoding="utf-8")
dist = DIST.read_text(encoding="utf-8")
release = json.loads(RELEASE.read_text(encoding="utf-8"))

require(
    standard,
    [
        "Project Delivery supplies the learner-experience benchmark",
        "Data Before AI supplies the production benchmark",
        "Required lesson journey",
        "Course production gates",
        "Data Before AI Chapter 09",
    ],
    "course operating standard",
)
require(
    course,
    [
        "course_version: 0.24.0",
        "golden_lesson: \"09\"",
        "lesson_contract_elements: 11",
        "- \"09\"",
    ],
    "Data Before AI course record",
)
require(
    source,
    [
        'content="released"',
        "Everyone contributed. Nobody owned the joined truth.",
        'id="openingDecision"',
        'id="authoritySimulation"',
        'id="lessonGraph"',
        'id="packForm"',
        'id="masteryCheck"',
        'id="completeChapter" disabled',
        "criteria D02.1 through D02.5",
        "v0.24.0",
    ],
    "golden lesson source",
)
require(
    dist,
    [
        "Golden hybrid lesson 01",
        "Accountability that survives the handoff.",
        "academy: bad config",
        "Chapter 09 complete",
    ],
    "golden lesson distribution build",
)

for path, text in ((STANDARD, standard), (SOURCE, source)):
    if "—" in text or "–" in text:
        raise AssertionError(f"prohibited dash found in {path}")

if release.get("contract") != "owos-course-release/1.0":
    raise AssertionError("release manifest contract is not governed")
if release.get("course", {}).get("version") != "0.24.0":
    raise AssertionError("release manifest does not identify course version 0.24.0")
if len(release.get("files", [])) != 26:
    raise AssertionError("release manifest must contain the landing page and 25 lessons")

print("OWOS Course Operating Standard QA passed: standard 2.0.0, golden lesson 09, release 0.24.0.")
