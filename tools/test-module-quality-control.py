#!/usr/bin/env python3
"""Verify the reusable module QA contract and the current AI-agent golden-lesson report."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "core/templates/MODULE-QA-REPORT.md"
REPORT = ROOT / "apps/what-is-an-ai-agent/qa/module-04-quality-control-report.md"
SKILL = ROOT / ".codex/skills/continue-owos-course/SKILL.md"
STANDARD = ROOT / "core/standards/COURSE-OPERATING-STANDARD.md"


def require(path: Path, phrases: list[str]) -> str:
    if not path.exists():
        raise AssertionError(f"missing QA artifact: {path}")
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path} is missing: {phrase}")
    if "—" in text or "–" in text:
        raise AssertionError(f"prohibited dash found in {path}")
    return text


require(
    TEMPLATE,
    [
        "Scored quality review",
        "Hard gates",
        "Automated checks",
        "Manual review still required",
        "The numeric score summarizes quality. It never overrides a failed hard gate.",
    ],
)
report = require(
    REPORT,
    [
        "score: 86",
        "working_status: conditional_pass",
        "release_status: blocked",
        "86 out of 100",
        "Utility-practitioner review",
        "Technical and accessibility review",
        "Required revisions",
    ],
)
require(SKILL, ["MODULE-QA-REPORT.md", "hard gates", "show it to Hardeep after each module"])
require(STANDARD, ["Module quality-control report", "numeric score never overrides"])

if report.count("| **Total** | **100** | **86**") != 1:
    raise AssertionError("Module 4 QA report must disclose exactly one 86 out of 100 total")

print("Module quality-control QA passed: scored report, hard gates, evidence, and unresolved work are visible.")
