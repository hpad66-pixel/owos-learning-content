#!/usr/bin/env python3
"""Acceptance checks for the foundational utility AI-agent curriculum."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps/what-is-an-ai-agent"
BRIEFS = COURSE / "curriculum/design-briefs"
SCRIPTS = COURSE / "curriculum/scripts"


def require(path: Path, phrases: list[str]) -> None:
    if not path.exists():
        raise AssertionError(f"missing curriculum artifact: {path}")
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path} is missing: {phrase}")
    if "—" in text or "–" in text:
        raise AssertionError(f"prohibited dash found in {path}")


expected_briefs = {
    "module-01-before-the-agent.md": ["Progressive comparison", "AI Terms Field Card"],
    "module-02-inside-the-agent-loop.md": ["Event-stream inspector", "Agent Loop Trace"],
    "module-03-agent-anatomy.md": ["Interactive anatomy experience", "Tooltip behavior"],
    "module-04-the-handoff.md": ["approved for golden-lesson production", "Broken-handoff diagnosis"],
    "module-05-agent-agentic-or-automated.md": ["autonomy spectrum", "Simplest-solution recommender"],
    "module-06-guardrails.md": ["excessive agency", "Operational-technology boundary"],
    "module-07-utility-applications.md": ["Utility opportunity portfolio review", "one idea rejected"],
    "module-08-design-your-agent.md": ["Utility Agent Canvas", "Adversarial review"],
}

for filename, phrases in expected_briefs.items():
    require(BRIEFS / filename, phrases)

expected_scripts = {
    "module-01-before-the-agent-video-script.md": ["AI terms field card", "Spoken words"],
    "module-02-inside-the-agent-loop-video-script.md": ["agent-loop trace", "Spoken words"],
    "module-03-agent-anatomy-video-script.md": ["dependency and readiness map", "Spoken words"],
    "module-04-the-handoff-video-script.md": ["orchestration and handoff contract", "Spoken words"],
    "module-05-agent-agentic-or-automated-video-script.md": ["autonomy and consequence decision record", "Spoken words"],
    "module-06-guardrails-video-script.md": ["guardrail and human-authority plan", "Spoken words"],
    "module-07-utility-applications-video-script.md": ["utility opportunity portfolio", "Spoken words"],
    "module-08-design-your-agent-video-script.md": ["90-Day Pilot Brief", "Spoken words"],
}

for filename, phrases in expected_scripts.items():
    require(SCRIPTS / filename, phrases)

require(
    SCRIPTS / "COURSE-OVERVIEW-VIDEO-SCRIPT.md",
    ["Lesson 1: Before the Agent", "Lesson 8: Design Your First Utility Agent", "Spoken words"],
)

require(
    COURSE / "SYLLABUS.md",
    [
        "The twelve learning dimensions",
        "Agent anatomy, explained simply",
        "Thirty-day application challenge",
        "Capstone completion standard",
    ],
)
require(COURSE / "curriculum/GLOSSARY.md", ["Agentic system", "Prompt injection", "Streaming"])
require(COURSE / "curriculum/ASSESSMENT-BLUEPRINT.md", ["Deterministic scoring", "Credential boundary"])
require(COURSE / "curriculum/INSTRUCTOR-GUIDE.md", ["Common misconceptions", "Role lenses"])
require(COURSE / "curriculum/TOOLTIP-AND-PLAIN-LANGUAGE-STANDARD.md", ["one tooltip element", "Reading test"])
require(COURSE / "work-products/UTILITY-AGENT-CANVAS.md", ["Simplest suitable architecture", "Operational-technology boundary"])
require(COURSE / "work-products/90-DAY-PILOT-BRIEF.md", ["Days 1 through 30", "Stop conditions"])
require(COURSE / "research/EVIDENCE-BOUNDARIES.md", ["Utility safety boundary", "operational technology"])

record = yaml.safe_load((COURSE / "course.yaml").read_text(encoding="utf-8"))
if record["status"] != "golden_candidate_built":
    raise AssertionError("course must disclose that the golden lesson is built but not approved as the production benchmark")
if record["structure"]["chapters"] != 8:
    raise AssertionError("course record must declare eight modules")
if record["delivery"]["release_state"] != "golden_lesson_built_pending_review":
    raise AssertionError("release state must disclose that the built golden lesson is pending review")

print("AI agent curriculum QA passed: eight module briefs, assessments, capstone, glossary, instruction, and safety boundaries are connected.")
