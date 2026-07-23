#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "apps/what-is-an-ai-agent/curriculum/module-04-the-handoff.html"
text = LESSON.read_text(encoding="utf-8")


def require(phrase: str) -> None:
    if phrase not in text:
        raise AssertionError(f"Module 4 application control is missing: {phrase}")


for phrase in (
    'id="contractScore"',
    'id="contractCriteria"',
    'id="contractReviewFeedback"',
    'state.work=score===5',
    '"source","evidence"',
    '"conflict","limit"',
    '"status","decision"',
    '"locator","link","record"',
    '"asset","identity"',
    '"date","time","version"',
    '"retry","escalat","stop"',
    '"certif","record","execute","external"',
    'id="nextStep"',
    'id="pauseSteps"',
    'id="resetSteps"',
    'function paintGraphStep(step,i)',
    'data-graph-node="human-authority"',
):
    require(phrase)

if text.count('class="criterion"') < 5:
    raise AssertionError("Module 4 must display all five deterministic contract criteria")

print("Module 4 application QA passed: simulation controls, responsive graph, and five-part contract scoring are present.")
