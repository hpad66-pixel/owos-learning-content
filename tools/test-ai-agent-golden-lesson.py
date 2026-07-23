#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "apps/what-is-an-ai-agent/curriculum/module-04-the-handoff.html"
text = LESSON.read_text(encoding="utf-8")


def require(phrase: str) -> None:
    if phrase not in text:
        raise AssertionError(f"golden lesson is missing: {phrase}")


for phrase in (
    'name="viewport"',
    'name="owos-learning-object" content="aia001:04"',
    'name="owos-release-state" content="golden-candidate"',
    "Handoff orchestration simulator",
    "Handoff repair laboratory",
    "Action authority console",
    "Orchestration and Handoff Contract",
    "Deterministic knowledge checks",
    "Source map and instructional boundary",
    "Module 4 Knowledge Graph",
    "One outfall, four records, one accountable decision",
    'id="nextStep"',
    'id="pauseSteps"',
    'id="resetSteps"',
    'id="reviewContract"',
    'id="contractScore"',
    'id="graphActiveRole"',
    'data-graph-node="provenance"',
    "AG-009",
    "AG-016 and AG-017",
    "AG-018 and AG-019",
    "AG-020 and AG-021",
    "prefers-reduced-motion:reduce",
    'aria-live="polite"',
    'id="completeLesson" disabled',
    "localStorage.setItem",
    "/api/learn/events",
    "/api/learn/enrollments",
):
    require(phrase)

if text.count('class="option"') < 8:
    raise AssertionError("golden lesson needs the governed quiz mix")
if text.count("data-correct") < 8:
    raise AssertionError("golden lesson needs deterministic answer keys")
if text.count('class="panel"') < 4:
    raise AssertionError("golden lesson needs at least four visual or interactive panels")
if text.count("data-instructor-explanation") < 10:
    raise AssertionError("golden lesson must teach every major component with visible instructor explanation")
for phrase in (
    "How to read the simulation",
    "Before you read the funnel",
    "How to use the laboratory",
    "How to set authority",
    "Why this work product matters",
    "What these checks measure",
    "Anatomy of a controlled handoff packet",
    "How one missing locator travels downstream",
    'id="causeChain"',
    'data-packet-mode="complete"',
    'data-packet-mode="missing"',
    "function scoreContract()",
    "function paintGraphStep(step,i)",
    'aria-label="Advance one handoff"',
):
    require(phrase)
if "undefined" in text.lower():
    raise AssertionError("golden lesson contains an undefined sentinel")
if "—" in text or "–" in text:
    raise AssertionError("golden lesson contains a prohibited dash")

print("AI agent golden lesson QA passed: simulation, repair, authority, work product, assessments, graph, persistence, and accessibility contracts are present.")
