#!/usr/bin/env python3
"""Mechanical checks for the binding OWOS Course Production Contract."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "core/standards/COURSE-PRODUCTION-CONTRACT.md"
OPERATING = ROOT / "core/standards/COURSE-OPERATING-STANDARD.md"
DESIGN = ROOT / "core/standards/COURSE-DESIGN-SYSTEM.md"
SKILL = ROOT / ".codex/skills/continue-owos-course/SKILL.md"
CREATOR = ROOT / "tools/create-course.py"
BRIEF = ROOT / "core/templates/MODULE-DESIGN-BRIEF.md"
QA = ROOT / "core/templates/MODULE-QA-REPORT.md"


def require(path: Path, phrases: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path} is missing: {phrase}")
    if "—" in text or "–" in text:
        raise AssertionError(f"prohibited dash found in {path}")


require(
    CONTRACT,
    [
        "Syllabus and blueprint gate",
        "Complete lesson experience",
        "Instructor voice and explanation",
        "Graphics, interaction, and pacing",
        "Course navigation and connected learning",
        "compact Graph, Community, and Start actions",
        "white, right-side drawers",
        "complete graph and community section at the bottom",
        "#owos-course-community",
        "module-specific FAQ",
        "dark surface is a release blocker",
        "Deterministic learning and records",
        "Quality assurance and release",
        "Definition of done",
    ],
)
require(OPERATING, ["COURSE-PRODUCTION-CONTRACT.md"])
require(DESIGN, ["COURSE-PRODUCTION-CONTRACT.md"])
require(SKILL, ["COURSE-PRODUCTION-CONTRACT.md", "floating cards or hanging rails", "module-specific FAQ", "contrast guard"])
require(CREATOR, ["Course Production Contract", "#owos-course-community", "Graph, Community, and Start", "Floating cards and hanging rails are prohibited", "module-specific FAQ"])
require(BRIEF, ["Header Graph, Community, and Start actions", "#owos-course-community", "Learner FAQ plan", "Dark-surface contrast plan"])
require(QA, ["Header Graph, Community, and Start actions", "Explicit bottom connected-learning anchor", "Module-specific FAQ coverage", "Dark-surface contrast guard"])

print("OWOS Course Production Contract QA passed.")
