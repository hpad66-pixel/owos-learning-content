#!/usr/bin/env python3
"""Mechanical acceptance checks for the OWOS Course Design System."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / "core/standards/COURSE-DESIGN-SYSTEM.md"
EXPERIENCE = ROOT / "core/standards/COURSE-EXPERIENCE-ARCHITECTURE.md"
EXPERIENCE_BRIEF = ROOT / "core/templates/COURSE-EXPERIENCE-BRIEF.md"
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
        "two to five explanatory visuals",
        "signature mechanism",
        "Course Experience Brief",
        "Check diversity across the course",
        "Make animation instructional",
        "same-page Knowledge Graph experience",
        "Teach the interface in the interface",
        "Prepare media only when the course modality calls for it",
        "Use graphics to explain, not decorate",
        "Failure conditions",
    ],
)
require(MODULE_BRIEF, ["Concept-to-experience plan", "Module design fingerprint", "Instructor explanation plan", "Explanatory graphic plan", "Recording script", "Diversity check"])
require(COURSE_MATRIX, ["Lesson archetype", "Signature mechanism", "Repetition risk"])
require(EXPERIENCE, ["The lesson must stand without video", "Course-level anti-repetition gate", "Whole-course full-module evidence", "Failure conditions"])
require(EXPERIENCE_BRIEF, ["Course identity", "Written-first teaching contract", "Course rhythm", "Full-module evidence inventory"])
require(
    SKILL,
    [
        "COURSE-DESIGN-SYSTEM.md",
        "COURSE-EXPERIENCE-ARCHITECTURE.md",
        "VISUAL-ARSENAL.md",
        "COMPONENTS.md",
        "QUIZ-TYPES.md",
        "Design every module as its own learning experience",
        "MODULE-DESIGN-BRIEF.md",
        "COURSE-DESIGN-MATRIX.md",
        "Teach every major visual",
        "Recording scripts are optional",
        "Use explanatory graphics",
        "course_distinctiveness.py",
    ],
)
require(REPO_AGENTS, ["Course Design System", "Chapter 09 is a capability benchmark"])
require(CREATOR, ["Course Experience Architecture", "COURSE-EXPERIENCE-BRIEF.md", "course_distinctiveness.py", "course_full_conformance.py"])

print("OWOS Course Design System QA passed: written-first teaching, course identities, experience briefs, and distinctiveness gates are enforced.")
