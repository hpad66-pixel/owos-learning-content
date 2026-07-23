#!/usr/bin/env python3
"""Mechanical acceptance checks for the OWOS Course Design System."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / "core/standards/COURSE-DESIGN-SYSTEM.md"
MODULE_BRIEF = ROOT / "core/templates/MODULE-DESIGN-BRIEF.md"
COURSE_MATRIX = ROOT / "core/templates/COURSE-DESIGN-MATRIX.md"
SKILL = ROOT / ".codex/skills/continue-owos-course/SKILL.md"
REPO_AGENTS = ROOT / "AGENTS.md"
CREATOR = ROOT / "tools/create-course.py"


def require(path: Path, phrases: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path} is missing: {phrase}")
    if "—" in text or "–" in text:
        raise AssertionError(f"prohibited dash found in {path}")


require(
    DESIGN,
    [
        "Project Delivery Master Class",
        "Data Before AI",
        "Chapter 09 capability benchmark",
        "capability benchmark. It is not a visual mold",
        "module design fingerprint",
        "four different visual types",
        "two purposeful interactions",
        "three different quiz types",
        "Check diversity across the course",
        "Make animation instructional",
        "same-page Knowledge Graph experience",
        "Failure conditions",
    ],
)
require(MODULE_BRIEF, ["Concept-to-experience plan", "Module design fingerprint", "Diversity check"])
require(COURSE_MATRIX, ["Opening pattern", "Purposeful interactions", "Repetition risk"])
require(
    SKILL,
    [
        "COURSE-DESIGN-SYSTEM.md",
        "VISUAL-ARSENAL.md",
        "COMPONENTS.md",
        "QUIZ-TYPES.md",
        "Design every module as its own learning experience",
        "MODULE-DESIGN-BRIEF.md",
        "COURSE-DESIGN-MATRIX.md",
    ],
)
require(REPO_AGENTS, ["Course Design System", "Chapter 09 is a capability benchmark"])
require(CREATOR, ["Course Design System", "COURSE-DESIGN-MATRIX.md"])

print("OWOS Course Design System QA passed: hybrid model, design fingerprints, diversity matrix, and skill wiring are enforced.")
