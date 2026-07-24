#!/usr/bin/env python3
"""Validate all eighteen Meaning Before Models module candidates."""

import importlib.util
import json
from pathlib import Path

from bs4 import BeautifulSoup

from course_conformance import validate_module
from course_distinctiveness import audit as audit_distinctiveness


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps/meaning-before-models"
CONTRACT = COURSE / ".course/full-module-contract.json"
contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
spec = importlib.util.spec_from_file_location(
    "meaning_course_builder", ROOT / "tools/build-meaning-before-models-course.py"
)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
MODULES = builder.MODULES

records = {
    item["number"]: {
        "lesson": COURSE / "curriculum" / f"module-{item['number']:02}-{item['slug']}.html",
        "brief": COURSE / "curriculum/design-briefs" / f"module-{item['number']:02}-{item['slug']}.md",
        "script": COURSE / "curriculum/scripts" / f"module-{item['number']:02}-{item['slug']}-video-script.md",
        "qa": COURSE / "qa" / f"module-{item['number']:02}-{item['slug']}-quality-control-report.md",
    }
    for item in MODULES
}
records[5] = {
    "lesson": COURSE / "curriculum/module-05-five-layers-of-meaning.html",
    "brief": COURSE / "curriculum/design-briefs/module-05-five-layers-of-meaning.md",
    "script": COURSE / "curriculum/scripts/module-05-five-layers-of-meaning-video-script.md",
    "qa": COURSE / "qa/module-05-quality-control-report.md",
}

results = []
for number in range(1, 19):
    record = records[number]
    result = validate_module(
        record["lesson"], record["qa"], record["brief"], record["script"], CONTRACT
    )
    results.append(result)
    soup = BeautifulSoup(record["lesson"].read_text(encoding="utf-8"), "html.parser")
    ids = [node["id"] for node in soup.select("[id]")]
    if len(ids) != len(set(ids)):
        raise AssertionError(f"module {number:02} has duplicate HTML ids")
    for node, attr in [
        *[(node, "href") for node in soup.find_all("link", href=True)],
        *[(node, "src") for node in soup.find_all("script", src=True)],
        *[(node, "href") for node in soup.find_all("a", href=True)],
    ]:
        value = node.get(attr, "")
        if not value or value.startswith(("http:", "https:", "data:", "#", "/")):
            continue
        target = (record["lesson"].parent / value.split("#")[0]).resolve()
        if not target.exists():
            raise AssertionError(f"module {number:02} has missing local target: {value}")

if len(results) != 18:
    raise AssertionError("all eighteen modules must be validated")
minimum_visuals = int(contract["minimum_visual_types"])
minimum_quizzes = int(contract["minimum_quiz_types"])
if any(len(item["visual_types"]) < minimum_visuals for item in results):
    raise AssertionError(f"every module needs at least {minimum_visuals} explanatory visual types")
if any(len(item["quiz_types"]) < minimum_quizzes for item in results):
    raise AssertionError(f"every module needs at least {minimum_quizzes} assessment types")

distinctiveness = audit_distinctiveness(COURSE)
if distinctiveness["status"] != "passed":
    raise AssertionError(
        "Meaning Before Models module contracts pass individually, but the course-level "
        "distinctiveness gate is blocked:\n"
        + "\n".join(f"- {error}" for error in distinctiveness["errors"][:20])
    )

landing = COURSE / "curriculum/course-meaning-before-models.html"
landing_text = landing.read_text(encoding="utf-8")
for number, record in records.items():
    if record["lesson"].name not in landing_text:
        raise AssertionError(f"course landing page does not link module {number:02}")

print("Meaning Before Models QA passed: module conformance and course distinctiveness both pass.")
