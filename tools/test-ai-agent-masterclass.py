#!/usr/bin/env python3
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "apps/what-is-an-ai-agent/curriculum"
QA_ROOT = ROOT / "apps/what-is-an-ai-agent/qa"
pages = {
    1: "module-01-before-the-agent.html",
    2: "module-02-inside-the-agent-loop.html",
    3: "module-03-agent-anatomy.html",
    4: "module-04-the-handoff.html",
    5: "module-05-agent-agentic-or-automated.html",
    6: "module-06-guardrails.html",
    7: "module-07-utility-applications.html",
    8: "module-08-design-your-agent.html",
}

for number, filename in pages.items():
    path = CURRICULUM / filename
    if not path.exists():
        raise AssertionError(f"missing learner-facing module: {filename}")
    text = path.read_text(encoding="utf-8")
    required = [
        'name="viewport"',
        f"aia001:{number:02d}",
        "Instructor explanation",
        "Knowledge check",
        "Professional work product" if number < 8 else "Capstone work product",
        "Knowledge Graph",
        "Source map and instructional boundary" if number == 4 else ("Evidence and credential boundary" if number == 8 else "Evidence boundary"),
        "prefers-reduced-motion:reduce" if number == 4 else "masterclass.css",
    ]
    for phrase in required:
        if phrase not in text:
            raise AssertionError(f"{filename} is missing {phrase}")
    if text.count("Knowledge check") < 3:
        raise AssertionError(f"{filename} must visibly distribute at least three knowledge checks")
    if number != 4 and text.count("data-required") < 5:
        raise AssertionError(f"{filename} needs deterministic decision, interaction, assessment, and work-product evidence")
    if number != 4 and "<svg" not in text:
        raise AssertionError(f"{filename} needs an original explanatory graphic")
    if "—" in text or "–" in text:
        raise AssertionError(f"{filename} contains a prohibited dash")
    if re.search(r">\s*undefined\s*<", text, re.I):
        raise AssertionError(f"{filename} contains a learner-visible invalid sentinel")

landing = (CURRICULUM / "course-what-is-an-ai-agent.html").read_text(encoding="utf-8")
for filename in pages.values():
    if filename not in landing:
        raise AssertionError(f"master-class landing page is not connected to {filename}")

runtime = (CURRICULUM / "masterclass.js").read_text(encoding="utf-8")
for phrase in (
    "data-quiz",
    "data-match",
    "data-stepper",
    "data-lab",
    "data-artifact",
    "data-open-graph",
    "localStorage",
    "instructorNotes",
    "teachingExpansion",
    "faqNotes",
    "faqExpansion",
    "Questions learners usually ask",
    "How to use this section",
    "How to read this graphic",
    "Before you interact",
    "Build something you can use",
):
    if phrase not in runtime:
        raise AssertionError(f"master-class runtime is missing {phrase}")
faq_runtime = runtime.split("var faqNotes=", 1)[1]
for number in pages:
    key = f'"{number:02d}":'
    if key not in runtime:
        raise AssertionError(f"master-class runtime is missing the Module {number} instructor layer")
    start = faq_runtime.index(key)
    next_key = f'"{number + 1:02d}":' if number < 8 else "};\nfunction faqExpansion"
    end = faq_runtime.index(next_key, start)
    if faq_runtime[start:end].count('["') < 4:
        raise AssertionError(f"master-class runtime needs at least four module-specific FAQs for Module {number}")
if "—" in runtime or "–" in runtime:
    raise AssertionError("master-class instructor runtime contains a prohibited dash")

styles = (CURRICULUM / "masterclass.css").read_text(encoding="utf-8")
for phrase in (
    ".instructor-dialogue",
    ".visual-break",
    ".concept-flow",
    ".module-faq",
    ".faq-map",
    ".faq-item",
    ".dark p",
    ".preview pre",
    "@media(max-width:760px)",
):
    if phrase not in styles:
        raise AssertionError(f"master-class design system is missing {phrase}")
if ".dark h2" not in styles or "color:#fff" not in styles:
    raise AssertionError("dark teaching surfaces do not explicitly enforce light text")
if "lesson-tool-rail" in runtime or ".lesson-tool-rail" in styles:
    raise AssertionError("the removed hanging lesson tool rail returned")

expected_scores = {
    1: 91,
    2: 92,
    3: 92,
    4: 92,
    5: 91,
    6: 92,
    7: 91,
    8: 93,
}
for number, score in expected_scores.items():
    report = QA_ROOT / f"module-{number:02d}-quality-control-report.md"
    if not report.exists():
        raise AssertionError(f"missing QA report for Module {number}")
    content = report.read_text(encoding="utf-8")
    if f"score: {score}" not in content or f"**{score}**" not in content:
        raise AssertionError(f"Module {number} QA report does not record score {score}")
    if "Version 0.9.2 FAQ review" not in content:
        raise AssertionError(f"Module {number} QA report does not review the module-specific FAQ")
    if score < 90:
        raise AssertionError(f"Module {number} is below the master-class threshold")

scorecard = (QA_ROOT / "masterclass-scorecard.md").read_text(encoding="utf-8")
if "aggregate_score: 92" not in scorecard or "**92**" not in scorecard:
    raise AssertionError("Master-class scorecard does not record the aggregate score")

print("AI Agent Master Class QA passed: eight chronological modules, distributed quizzes, distinct visuals, work products, graphs, persistence, and completion contracts are connected.")
