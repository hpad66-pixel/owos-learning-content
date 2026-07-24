#!/usr/bin/env python3
"""Regression checks for the approved Modules 10, 12, 15, and 17 retrofit."""

from __future__ import annotations

import json
from pathlib import Path

from bs4 import BeautifulSoup


COURSE = Path(__file__).resolve().parents[1]
CURRICULUM = COURSE / "curriculum"

SPECS = {
    "module-10-quality-management.html": {
        "quiz_types": ("diagnostic-repair", "quality-record-gate"),
        "visual_types": ("phase-gate", "line-s-curve"),
        "artifact": "quality-repair-record",
        "preserved_components": ("coq", "process", "examsim", "artifactbuilder"),
    },
    "module-12-teams-stakeholders-communication.html": {
        "quiz_types": ("role-conversation", "stakeholder-brief-gate"),
        "visual_types": ("two-by-two", "network-diagram"),
        "artifact": "stakeholder-engagement-brief",
        "preserved_components": ("decide", "grid", "channels", "examsim", "artifactbuilder"),
    },
    "module-15-measurement-honest-status.html": {
        "quiz_types": ("dashboard-forensics", "status-brief-gate"),
        "visual_types": ("comparison-table", "heat-grid"),
        "artifact": "executive-status-brief",
        "preserved_components": ("dashboard", "beforeafter", "examsim", "artifactbuilder"),
    },
    "module-17-safety-locates-commissioning.html": {
        "quiz_types": ("readiness-gate", "readiness-pack-gate"),
        "visual_types": ("phase-gate", "applicability-gate"),
        "artifact": "readiness-and-clearance-pack",
        "preserved_components": ("process", "clearance", "applicability", "artifacttracker"),
    },
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    quiz_sequences: list[tuple[str, ...]] = []
    checked_scripts = 0

    for filename, expected in SPECS.items():
        path = CURRICULUM / filename
        require(path.is_file(), f"missing lesson: {filename}")
        text = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")

        require(len(soup.find_all("main")) == 1, f"{filename}: expected one main")
        require(len(soup.find_all("h1")) == 1, f"{filename}: expected one h1")
        require(
            len(soup.select("[data-module-faq] details")) == 5,
            f"{filename}: expected five FAQs",
        )
        require(soup.select_one('script[src="project-retrofit.js"]'), f"{filename}: retrofit JS missing")
        require(soup.select_one('link[href="project-retrofit.css"]'), f"{filename}: retrofit CSS missing")

        quiz_types = tuple(
            item.get("data-quiz-type", "")
            for item in soup.select("[data-quiz-type][data-required]")
        )
        require(quiz_types == expected["quiz_types"], f"{filename}: quiz sequence {quiz_types}")
        quiz_sequences.append(quiz_types)

        visual_types = {
            item.get("data-visual-type", "") for item in soup.select("[data-visual-type]")
        }
        require(
            set(expected["visual_types"]).issubset(visual_types),
            f"{filename}: visual types {sorted(visual_types)}",
        )

        artifact = soup.select_one(f'[data-artifact="{expected["artifact"]}"]')
        require(artifact is not None, f"{filename}: module-specific artifact missing")
        final = soup.select_one(
            f'[data-final-applied-check][data-artifact-ref="{expected["artifact"]}"]'
        )
        require(final is not None, f"{filename}: artifact-linked final check missing")

        components = {item.get("data-ac", "") for item in soup.select("[data-ac]")}
        missing_components = set(expected["preserved_components"]) - components
        require(
            not missing_components,
            f"{filename}: preserved components missing {sorted(missing_components)}",
        )

        declared = {
            item.get("data-requirement", "")
            for item in soup.select("[data-requirement]")
        }
        required = {
            item.get("data-required", "")
            for item in soup.select("[data-required]")
            if item.get("data-required")
        }
        require(required.issubset(declared), f"{filename}: undeclared evidence {required - declared}")
        require(soup.select_one("#owos-course-community"), f"{filename}: bottom anchor missing")
        require(soup.select_one("[data-open-graph]"), f"{filename}: Graph action missing")
        require(soup.select_one("[data-open-community]"), f"{filename}: Community action missing")

        for script in soup.select('script[type="application/json"]'):
            json.loads(script.string or script.get_text())
            checked_scripts += 1

    require(
        len(set(quiz_sequences)) == len(SPECS),
        "targeted modules must have four different quiz sequences",
    )
    print(
        "PASS: 4 targeted lessons; 4 unique quiz sequences; "
        f"{checked_scripts} component configurations parsed; preserved simulations verified."
    )


if __name__ == "__main__":
    main()
