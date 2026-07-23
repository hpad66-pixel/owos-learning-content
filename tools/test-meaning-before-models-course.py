#!/usr/bin/env python3
"""Validate all eighteen Meaning Before Models module candidates."""

import importlib.util
from pathlib import Path

from bs4 import BeautifulSoup

from course_conformance import validate_module


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps/meaning-before-models"
CONTRACT = COURSE / ".course/full-module-contract.json"
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
experience_fingerprints = []
all_lesson_visual_types = set()
experience_names = []
card_layouts = []
for number in range(1, 19):
    record = records[number]
    result = validate_module(
        record["lesson"], record["qa"], record["brief"], record["script"], CONTRACT
    )
    results.append(result)
    soup = BeautifulSoup(record["lesson"].read_text(encoding="utf-8"), "html.parser")
    lesson_visuals = soup.select('[id^="visual-"][data-visual-type]')
    visual_types = tuple(node["data-visual-type"] for node in lesson_visuals)
    visual_shapes = tuple(node["data-visual-shape"] for node in lesson_visuals)
    inner_signatures = []
    for node in lesson_visuals:
        stage = node.select_one(".visual-stage")
        root = next((child for child in stage.children if getattr(child, "name", None)), None)
        inner_signatures.append((root.name, tuple(root.get("class", []))))
    quiz_sequence = tuple(
        node["data-quiz-type"] for node in soup.select("[data-quiz-type][data-required]")
    )
    experience = soup.body.get("data-experience", "")
    card_layout = soup.select_one(".question-flips[data-card-layout]")
    if not experience:
        raise AssertionError(f"module {number:02} needs a named narrative architecture")
    if not card_layout:
        raise AssertionError(f"module {number:02} needs a named card composition")
    experience_names.append(experience)
    card_layouts.append(card_layout["data-card-layout"])
    if len(set(visual_shapes)) != len(visual_shapes):
        raise AssertionError(f"module {number:02} repeats a structural visual shape: {visual_shapes}")
    if len(set(inner_signatures)) != len(inner_signatures):
        raise AssertionError(
            f"module {number:02} relabels the same inner visual structure: {inner_signatures}"
        )
    if len(soup.select('#question-deck .flip-question, #opening-quiz .flip-question')) < 4:
        raise AssertionError(f"module {number:02} needs four working question flip cards")
    answers = [
        node.get_text(" ", strip=True)
        for node in soup.select("#question-deck .flip-back, #opening-quiz .flip-back")
    ]
    if len(answers) != 4 or len(set(answers)) != 4 or any(len(answer) < 45 for answer in answers):
        raise AssertionError(f"module {number:02} has missing, repeated, or shallow flip-card answers")
    all_lesson_visual_types.update(visual_types)
    experience_fingerprints.append((number, visual_types, visual_shapes, quiz_sequence))
    runtime_name = record["lesson"].name.replace("module-", "lesson-meaning-before-models-")
    runtime_lesson = COURSE / "dist/site" / runtime_name
    if not runtime_lesson.exists():
        raise AssertionError(f"module {number:02} is missing its packaged runtime lesson")
    runtime_soup = BeautifulSoup(runtime_lesson.read_text(encoding="utf-8"), "html.parser")
    runtime_visual_types = tuple(
        node["data-visual-type"]
        for node in runtime_soup.select('[id^="visual-"][data-visual-type]')
    )
    runtime_visual_shapes = tuple(
        node["data-visual-shape"]
        for node in runtime_soup.select('[id^="visual-"][data-visual-shape]')
    )
    runtime_quiz_sequence = tuple(
        node["data-quiz-type"]
        for node in runtime_soup.select("[data-quiz-type][data-required]")
    )
    runtime_experience = runtime_soup.body.get("data-experience", "")
    runtime_card_layout = runtime_soup.select_one(".question-flips[data-card-layout]")
    if (runtime_visual_types, runtime_visual_shapes, runtime_quiz_sequence) != (
        visual_types, visual_shapes, quiz_sequence
    ):
        raise AssertionError(
            f"module {number:02} packaged runtime is stale relative to curriculum source"
        )
    if runtime_experience != experience or not runtime_card_layout or runtime_card_layout["data-card-layout"] != card_layout["data-card-layout"]:
        raise AssertionError(
            f"module {number:02} packaged experience fingerprint is stale"
        )
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
if any(len(item["visual_types"]) < 4 for item in results):
    raise AssertionError("every module needs four visual types")
if any(len(item["quiz_types"]) < 3 for item in results):
    raise AssertionError("every module needs three quiz types")
if len(all_lesson_visual_types) < 55:
    raise AssertionError(
        f"course-wide visual arsenal is too narrow: {len(all_lesson_visual_types)} visual types"
    )
if len(set(experience_names)) != 18:
    raise AssertionError(f"every lesson needs a unique narrative architecture: {experience_names}")
if len(set(card_layouts)) != 18:
    raise AssertionError(f"every lesson needs a unique question-card composition: {card_layouts}")
dominant_visuals = [fingerprint[1][0] for fingerprint in experience_fingerprints]
if len(set(dominant_visuals)) != 18:
    raise AssertionError(f"every lesson needs a distinct dominant visual: {dominant_visuals}")
for left, right in zip(experience_fingerprints, experience_fingerprints[1:]):
    if left[1] == right[1] or left[2] == right[2]:
        raise AssertionError(
            f"adjacent modules {left[0]:02} and {right[0]:02} repeat a visual sequence"
        )
    if left[3] == right[3]:
        raise AssertionError(
            f"adjacent modules {left[0]:02} and {right[0]:02} repeat a quiz sequence"
        )

landing = COURSE / "curriculum/course-meaning-before-models.html"
landing_text = landing.read_text(encoding="utf-8")
for number, record in records.items():
    if record["lesson"].name not in landing_text:
        raise AssertionError(f"course landing page does not link module {number:02}")

if (
    COURSE.joinpath("curriculum/course-module.js").read_bytes()
    != COURSE.joinpath("dist/site/meaning-before-models-course-module.js").read_bytes()
):
    raise AssertionError("packaged course interaction runtime is stale")
if (
    COURSE.joinpath("curriculum/module-05-golden.css").read_bytes()
    != COURSE.joinpath("dist/site/meaning-before-models-module-05.css").read_bytes()
):
    raise AssertionError("packaged course visual system is stale")

print("Meaning Before Models QA passed: all eighteen full-module candidates conform.")
