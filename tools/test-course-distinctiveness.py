#!/usr/bin/env python3
"""Regression tests for the course-level anti-repetition gate."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from course_distinctiveness import audit


def lesson(title: str, visual: str, quiz: str, interaction: str, faq: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8"></head><body>
<main><h1>{title}</h1><section class="{title.lower()}">
<div data-visual-type="{visual}"></div>
<div data-quiz-type="{quiz}"></div>
<div data-purposeful-interaction="{interaction}"></div>
<form data-artifact="{title.lower()}"></form>
<section data-module-faq><details><summary>{faq}</summary><p>Answer</p></details></section>
</section></main></body></html>"""


with tempfile.TemporaryDirectory() as directory:
    course = Path(directory)
    curriculum = course / "curriculum"
    controls = course / ".course"
    curriculum.mkdir()
    controls.mkdir()
    specs = {
        "module-01-one.html": {
            "archetype": "incident",
            "signature_mechanism": "trace alarm",
            "opening": "alarm",
            "work_product_mode": "incident card",
        },
        "module-02-two.html": {
            "archetype": "lab",
            "signature_mechanism": "build graph",
            "opening": "blank canvas",
            "work_product_mode": "graph",
        },
        "module-03-three.html": {
            "archetype": "courtroom",
            "signature_mechanism": "admit proof",
            "opening": "disputed claim",
            "work_product_mode": "decision",
        },
        "module-04-four.html": {
            "archetype": "studio",
            "signature_mechanism": "design control",
            "opening": "blank plan",
            "work_product_mode": "plan",
        },
    }
    (controls / "experience-architecture.json").write_text(
        json.dumps({
            "minimum_archetypes": 3,
            "thresholds": {
                "maximum_archetype_share": 0.34,
                "maximum_adjacent_structural_similarity": 0.96,
                "factory_pattern_share": 1.10
            },
            "lessons": specs
        }),
        encoding="utf-8",
    )
    for index, name in enumerate(specs):
        (curriculum / name).write_text(
            lesson(
                f"Lesson {index}",
                ("network", "console", "proof", "plan")[index],
                ("construct", "execute", "defend", "design")[index],
                ("trace", "query", "judge", "shape")[index],
                (
                    "Where is the alarm?",
                    "What path matched?",
                    "What proof is valid?",
                    "Which control belongs?",
                )[index],
            ),
            encoding="utf-8",
        )
    result = audit(course)
    if result["status"] != "passed":
        raise AssertionError(result["errors"])

    (controls / "experience-architecture.json").write_text(
        json.dumps({
            "minimum_archetypes": 3,
            "thresholds": {
                "maximum_archetype_share": 0.34,
                "maximum_adjacent_structural_similarity": 0.96,
                "factory_pattern_share": 0.40
            },
            "lessons": specs
        }),
        encoding="utf-8",
    )
    repeated = lesson("Repeated", "boxes", "multiple-choice", "step-through", "Same question")
    for name in specs:
        (curriculum / name).write_text(repeated, encoding="utf-8")
    blocked = audit(course)
    if blocked["status"] != "blocked":
        raise AssertionError("factory-pattern lessons must fail the distinctiveness gate")
    expected = ("identical quiz sequence", "factory-pattern control counts", "FAQ question")
    if not all(any(phrase in error for error in blocked["errors"]) for phrase in expected):
        raise AssertionError(blocked["errors"])

print("OWOS course distinctiveness QA passed: varied lessons accepted and factory repetition blocked.")
