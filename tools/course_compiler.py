#!/usr/bin/env python3
"""Validate and compile structured OWOS module packages.

HTML is a deterministic delivery output. The module package remains the
authoritative source.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import sys
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

import yaml


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_CSS = ROOT / "core/runtime/course-module.css"
RUNTIME_JS = ROOT / "core/runtime/course-module.js"
COMPILER_VERSION = "1.1.0"
REQUIRED_FILES = (
    "design-brief.md",
    "module.yaml",
    "storyboard.yaml",
    "visuals/visual-manifest.yaml",
    "interactions.yaml",
    "assessments.yaml",
    "sources.yaml",
    "glossary.yaml",
    "qa.yaml",
)
SUPPORTED_INTERACTIONS = {
    "triple-builder",
    "path-tracer",
    "artifact-classifier",
    "failure-trace",
    "object-router",
    "triple-repair-bench",
    "identity-adjudication",
    "graph-growth-lab",
    "hierarchy-repair",
    "ontology-canvas",
    "sparql-builder",
    "inference-court",
    "shacl-clinic",
    "evidence-reconciliation",
    "knowledge-spine-router",
    "accountability-handoff",
    "mapping-workbench",
    "mapping-break-repair",
    "access-pattern-stress-test",
    "stale-copy-diagnosis",
    "evidence-promotion",
    "evidence-state-classifier",
    "context-assembly",
    "permission-gate",
    "pipeline-rerun",
    "pipeline-stage-diagnosis",
}
SUPPORTED_ASSESSMENTS = {
    "multiple-choice",
    "flip-cards",
    "matching",
    "multi-select",
    "applied-work-product",
}
BLOCK_TYPES = {
    "prose",
    "callout",
    "visual",
    "interaction",
    "assessment",
    "work_product",
    "faq",
    "evidence",
}


class ModulePackageError(ValueError):
    """Raised when a structured module package is incomplete or unsafe."""


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise ModulePackageError(f"{path}: cannot read YAML: {error}") from error
    if not isinstance(data, dict):
        raise ModulePackageError(f"{path}: expected a YAML object")
    return data


def source_files(module_dir: Path) -> list[Path]:
    files = [module_dir / name for name in REQUIRED_FILES]
    visual_manifest = module_dir / "visuals/visual-manifest.yaml"
    if visual_manifest.is_file():
        for visual in load_yaml(visual_manifest).get("visuals", []):
            if isinstance(visual, dict) and visual.get("locator"):
                files.append(module_dir / str(visual["locator"]))
    return sorted(set(files))


def package_checksum(module_dir: Path) -> str:
    digest = hashlib.sha256()
    for path in source_files(module_dir):
        if not path.is_file():
            continue
        digest.update(path.relative_to(module_dir).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    for runtime_path in (Path(__file__).resolve(), RUNTIME_CSS, RUNTIME_JS):
        digest.update(runtime_path.name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(runtime_path.read_bytes())
        digest.update(b"\0")
    digest.update(COMPILER_VERSION.encode("utf-8"))
    return digest.hexdigest()


def require_fields(record: dict[str, Any], fields: tuple[str, ...], label: str, errors: list[str]) -> None:
    for field in fields:
        if record.get(field) in (None, "", []):
            errors.append(f"{label}: missing {field}")


def unique_records(records: Any, key: str, label: str, errors: list[str]) -> dict[str, dict[str, Any]]:
    if not isinstance(records, list):
        errors.append(f"{label}: expected a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            errors.append(f"{label} item {index}: expected an object")
            continue
        identifier = record.get(key)
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"{label} item {index}: missing {key}")
            continue
        if identifier in result:
            errors.append(f"{label}: duplicate {key} {identifier}")
            continue
        result[identifier] = record
    return result


def text_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(text_values(item))
        return result
    if isinstance(value, dict):
        result = []
        for item in value.values():
            result.extend(text_values(item))
        return result
    return []


def validate_package(module_dir: Path, *, release_ready: bool = False) -> dict[str, Any]:
    module_dir = module_dir.resolve()
    errors: list[str] = []
    for name in REQUIRED_FILES:
        if not (module_dir / name).is_file():
            errors.append(f"missing required package file: {name}")
    if errors:
        raise ModulePackageError("\n".join(errors))

    module_data = load_yaml(module_dir / "module.yaml")
    storyboard = load_yaml(module_dir / "storyboard.yaml")
    visual_data = load_yaml(module_dir / "visuals/visual-manifest.yaml")
    interaction_data = load_yaml(module_dir / "interactions.yaml")
    assessment_data = load_yaml(module_dir / "assessments.yaml")
    source_data = load_yaml(module_dir / "sources.yaml")
    glossary_data = load_yaml(module_dir / "glossary.yaml")
    qa_data = load_yaml(module_dir / "qa.yaml")

    for label, data in (
        ("module", module_data),
        ("storyboard", storyboard),
        ("visual manifest", visual_data),
        ("interaction manifest", interaction_data),
        ("assessment manifest", assessment_data),
        ("source manifest", source_data),
        ("glossary", glossary_data),
        ("QA", qa_data),
    ):
        if data.get("schema_version") != 1:
            errors.append(f"{label}: schema_version must be 1")

    module = module_data.get("module")
    learning = module_data.get("learning")
    sections = module_data.get("sections")
    completion = module_data.get("completion")
    if not isinstance(module, dict):
        errors.append("module.yaml: module must be an object")
        module = {}
    if not isinstance(learning, dict):
        errors.append("module.yaml: learning must be an object")
        learning = {}
    if not isinstance(sections, list) or len(sections) < 3:
        errors.append("module.yaml: sections must contain at least three sections")
        sections = []
    if not isinstance(completion, dict):
        errors.append("module.yaml: completion must be an object")
        completion = {}

    require_fields(
        module,
        (
            "course_id",
            "module_id",
            "slug",
            "title",
            "promise",
            "duration",
            "level",
            "archetype",
            "signature_mechanism",
            "source_version",
        ),
        "module",
        errors,
    )
    require_fields(
        learning,
        ("audience", "outcomes", "prior_knowledge", "misconception", "transfer_task"),
        "learning",
        errors,
    )
    require_fields(completion, ("required_ids", "rule"), "completion", errors)

    module_id = module.get("module_id")
    for label, data in (
        ("storyboard", storyboard),
        ("visual manifest", visual_data),
        ("interaction manifest", interaction_data),
        ("assessment manifest", assessment_data),
        ("source manifest", source_data),
        ("glossary", glossary_data),
        ("QA", qa_data),
    ):
        if module_id and data.get("module_id") != module_id:
            errors.append(f"{label}: module_id does not match {module_id}")

    approvals = storyboard.get("approvals")
    if storyboard.get("status") != "approved":
        errors.append("storyboard: status must be approved before compilation")
    if not isinstance(approvals, dict):
        errors.append("storyboard: approvals must be an object")
    else:
        for gate in ("narrative", "visuals", "interactions", "assessments", "owner"):
            status = str(approvals.get(gate, ""))
            if release_ready and status != "approved":
                errors.append(f"storyboard: {gate} approval must be approved for release")
            elif not status.startswith("approved"):
                errors.append(f"storyboard: {gate} approval is not approved for a reference build")

    beats = storyboard.get("beats")
    if not isinstance(beats, list) or len(beats) < 3:
        errors.append("storyboard: at least three beats are required")
    else:
        for index, beat in enumerate(beats, start=1):
            if not isinstance(beat, dict):
                errors.append(f"storyboard beat {index}: expected an object")
                continue
            require_fields(
                beat,
                (
                    "beat_id",
                    "learner_question",
                    "instructor_purpose",
                    "intended_realization",
                    "transition",
                ),
                f"storyboard beat {index}",
                errors,
            )

    visuals = unique_records(visual_data.get("visuals"), "visual_id", "visual manifest", errors)
    interactions = unique_records(
        interaction_data.get("interactions"), "interaction_id", "interaction manifest", errors
    )
    assessments = unique_records(
        assessment_data.get("assessments"), "assessment_id", "assessment manifest", errors
    )
    sources = unique_records(source_data.get("sources"), "source_id", "source manifest", errors)

    visual_fields = (
        "title",
        "asset_class",
        "teaching_idea",
        "learner_conclusion",
        "reading_guide",
        "alternative_text",
        "mobile_treatment",
        "reduced_motion_treatment",
        "creator",
        "source",
        "license",
        "permission_status",
        "originality_status",
        "storyboard_status",
        "rendered_review_status",
    )
    for visual_id, visual in visuals.items():
        require_fields(visual, visual_fields, f"visual {visual_id}", errors)
        locator = visual.get("locator")
        component_id = visual.get("component_id")
        if not locator and not component_id:
            errors.append(f"visual {visual_id}: locator or component_id is required")
            continue
        if locator:
            asset = (module_dir / str(locator)).resolve()
            if module_dir not in asset.parents:
                errors.append(f"visual {visual_id}: asset must stay inside the module package")
            elif not asset.is_file():
                errors.append(f"visual {visual_id}: asset does not exist: {locator}")
            elif asset.stat().st_size < 1000:
                errors.append(f"visual {visual_id}: asset is too small to count as an explanatory visual")
            elif asset.suffix.lower() == ".svg":
                try:
                    root = ElementTree.parse(asset).getroot()
                except ElementTree.ParseError as error:
                    errors.append(f"visual {visual_id}: invalid SVG: {error}")
                else:
                    if not root.tag.endswith("svg"):
                        errors.append(f"visual {visual_id}: SVG root is missing")
                    if not root.findall("{http://www.w3.org/2000/svg}title"):
                        errors.append(f"visual {visual_id}: SVG needs a title element")
                    if not root.findall("{http://www.w3.org/2000/svg}desc"):
                        errors.append(f"visual {visual_id}: SVG needs a description element")
        if release_ready:
            for gate in ("permission_status", "originality_status", "storyboard_status", "rendered_review_status"):
                if visual.get(gate) not in {"approved", "original"}:
                    errors.append(f"visual {visual_id}: {gate} is not release approved")

    for interaction_id, interaction in interactions.items():
        require_fields(
            interaction,
            ("component", "title", "teaching_purpose", "instructions", "completion_id", "config"),
            f"interaction {interaction_id}",
            errors,
        )
        if interaction.get("component") not in SUPPORTED_INTERACTIONS:
            errors.append(
                f"interaction {interaction_id}: unsupported component {interaction.get('component')}"
            )

    for assessment_id, assessment in assessments.items():
        require_fields(
            assessment,
            ("type", "cognitive_job", "prompt", "feedback", "completion_id"),
            f"assessment {assessment_id}",
            errors,
        )
        if assessment.get("type") not in SUPPORTED_ASSESSMENTS:
            errors.append(
                f"assessment {assessment_id}: unsupported type {assessment.get('type')}"
            )
        if assessment.get("type") == "multiple-choice":
            options = assessment.get("options")
            if not isinstance(options, list) or len(options) < 2:
                errors.append(f"assessment {assessment_id}: multiple-choice needs options")
            elif sum(bool(option.get("correct")) for option in options if isinstance(option, dict)) != 1:
                errors.append(f"assessment {assessment_id}: exactly one option must be correct")
        if assessment.get("type") == "flip-cards" and len(assessment.get("cards", [])) < 3:
            errors.append(f"assessment {assessment_id}: flip-cards needs at least three cards")
        if assessment.get("type") == "matching":
            pairs = assessment.get("pairs")
            if not isinstance(pairs, list) or len(pairs) < 3:
                errors.append(f"assessment {assessment_id}: matching needs at least three pairs")
        if assessment.get("type") == "multi-select":
            options = assessment.get("options")
            if not isinstance(options, list) or len(options) < 3:
                errors.append(f"assessment {assessment_id}: multi-select needs at least three options")
            elif not any(bool(option.get("correct")) for option in options if isinstance(option, dict)):
                errors.append(f"assessment {assessment_id}: multi-select needs at least one correct option")

    used_visuals: set[str] = set()
    used_interactions: set[str] = set()
    used_assessments: set[str] = set()
    section_ids: set[str] = set()
    for section_index, section in enumerate(sections, start=1):
        if not isinstance(section, dict):
            errors.append(f"section {section_index}: expected an object")
            continue
        require_fields(section, ("section_id", "title", "blocks"), f"section {section_index}", errors)
        section_id = section.get("section_id")
        if section_id in section_ids:
            errors.append(f"section {section_index}: duplicate section_id {section_id}")
        section_ids.add(str(section_id))
        blocks = section.get("blocks")
        if not isinstance(blocks, list) or not blocks:
            errors.append(f"section {section_index}: blocks must be a non-empty list")
            continue
        for block_index, block in enumerate(blocks, start=1):
            if not isinstance(block, dict):
                errors.append(f"section {section_index} block {block_index}: expected an object")
                continue
            block_type = block.get("type")
            if block_type not in BLOCK_TYPES:
                errors.append(f"section {section_index} block {block_index}: invalid type {block_type}")
                continue
            if block_type == "visual":
                visual_id = block.get("visual_id")
                if visual_id not in visuals:
                    errors.append(f"section {section_index}: unknown visual_id {visual_id}")
                else:
                    used_visuals.add(str(visual_id))
            if block_type == "interaction":
                interaction_id = block.get("interaction_id")
                if interaction_id not in interactions:
                    errors.append(f"section {section_index}: unknown interaction_id {interaction_id}")
                else:
                    used_interactions.add(str(interaction_id))
            if block_type == "assessment":
                assessment_id = block.get("assessment_id")
                if assessment_id not in assessments:
                    errors.append(f"section {section_index}: unknown assessment_id {assessment_id}")
                else:
                    used_assessments.add(str(assessment_id))
            if block_type == "work_product":
                work_product_id = block.get("work_product_id")
                if work_product_id not in assessments:
                    errors.append(f"section {section_index}: work product has no assessment contract")
                elif assessments[work_product_id].get("type") != "applied-work-product":
                    errors.append(f"section {section_index}: work product contract has wrong type")
                else:
                    used_assessments.add(str(work_product_id))
            if block_type == "evidence":
                for source_ref in block.get("source_refs", []):
                    if source_ref not in sources:
                        errors.append(f"section {section_index}: unknown source_ref {source_ref}")

    if len(used_visuals) < 2:
        errors.append("module must use at least two resolvable explanatory visuals")
    unused_visuals = sorted(set(visuals) - used_visuals)
    if unused_visuals:
        errors.append("visual manifest contains unused assets: " + ", ".join(unused_visuals))
    unused_interactions = sorted(set(interactions) - used_interactions)
    if unused_interactions:
        errors.append("interaction manifest contains unused components: " + ", ".join(unused_interactions))
    unused_assessments = sorted(set(assessments) - used_assessments)
    if unused_assessments:
        errors.append("assessment manifest contains unused assessments: " + ", ".join(unused_assessments))

    required_ids = completion.get("required_ids", [])
    if not isinstance(required_ids, list) or not all(isinstance(item, str) for item in required_ids):
        errors.append("completion.required_ids must be a list of strings")
        required_ids = []
    produced_ids = {
        str(record.get("completion_id"))
        for record in list(interactions.values()) + list(assessments.values())
        if record.get("completion_id")
    }
    missing_completion = sorted(set(required_ids) - produced_ids)
    if missing_completion:
        errors.append("completion IDs have no producing component: " + ", ".join(missing_completion))

    combined_text = "\n".join(
        text_values(module_data)
        + text_values(storyboard)
        + text_values(visual_data)
        + text_values(interaction_data)
        + text_values(assessment_data)
        + text_values(glossary_data)
    )
    if "\u2014" in combined_text:
        errors.append("learner source contains a prohibited em dash")
    if "\u2013" in combined_text:
        errors.append("learner source contains a prohibited en dash")

    qa_gates = qa_data.get("gates")
    if not isinstance(qa_gates, dict):
        errors.append("QA gates must be an object")
    elif release_ready:
        for gate, status in qa_gates.items():
            if status != "approved":
                errors.append(f"QA gate {gate} must be approved for release")

    if errors:
        raise ModulePackageError("\n".join(f"- {error}" for error in errors))

    return {
        "module_dir": module_dir,
        "module_data": module_data,
        "storyboard": storyboard,
        "visuals": visuals,
        "interactions": interactions,
        "assessments": assessments,
        "sources": sources,
        "glossary": glossary_data.get("terms", []),
        "qa": qa_data,
        "checksum": package_checksum(module_dir),
        "compiler_version": COMPILER_VERSION,
        "release_ready": release_ready,
    }


def render_visual(visual: dict[str, Any], asset_prefix: str) -> str:
    locator = asset_prefix + str(visual["locator"])
    return f"""
<figure class="learning-visual" id="{esc(visual['visual_id'])}"
  data-visual-type="{esc(visual['asset_class'])}"
  data-component-source="structured-module-package">
  <h3>{esc(visual['title'])}</h3>
  <div class="reading-guide" data-reading-guide><strong>How to read it:</strong> {esc(visual['reading_guide'])}</div>
  <div class="visual-frame">
    <img src="{esc(locator)}" alt="{esc(visual['alternative_text'])}">
  </div>
  <figcaption class="conclusion" data-learner-conclusion><strong>What this shows:</strong> {esc(visual['learner_conclusion'])}</figcaption>
</figure>"""


def render_choice(assessment: dict[str, Any]) -> str:
    options = "\n".join(
        f'<button class="choice" type="button" data-choice data-correct="{str(bool(option["correct"])).lower()}">{esc(option["text"])}</button>'
        for option in assessment["options"]
    )
    feedback = assessment["feedback"]
    return f"""
<section class="component" id="{esc(assessment['assessment_id'])}" data-choice-group
  data-purposeful-interaction="multiple-choice" data-quiz-type="multiple-choice"
  data-quiz-source="structured-module-package"
  data-completion="{esc(assessment['completion_id'])}"
  data-correct-feedback="{esc(feedback['correct'])}"
  data-incorrect-feedback="{esc(feedback['incorrect'])}">
  <header class="component-header"><h3>{esc(assessment['prompt'])}</h3><span class="kind">Decision check</span></header>
  <div class="component-body">
    <p class="component-intro">Choose the strongest answer, then check it. The feedback explains the boundary.</p>
    <div class="choice-grid">{options}</div>
    <button class="button primary" type="button" data-check-choice>Check my answer</button>
    <div class="feedback" data-feedback aria-live="polite"></div>
  </div>
</section>"""


def render_flip_cards(assessment: dict[str, Any]) -> str:
    cards = "\n".join(
        f"""
<button class="flip-card" type="button" data-flip-card aria-pressed="false">
  <span class="flip-card-inner">
    <span class="flip-face flip-front">{esc(card['front'])}</span>
    <span class="flip-face flip-back">{esc(card['back'])}</span>
  </span>
</button>"""
        for card in assessment["cards"]
    )
    return f"""
<section class="component" id="{esc(assessment['assessment_id'])}" data-flip-group
  data-purposeful-interaction="flip-cards" data-quiz-type="flip-cards"
  data-quiz-source="structured-module-package"
  data-completion="{esc(assessment['completion_id'])}"
  data-correct-feedback="{esc(assessment['feedback']['correct'])}">
  <header class="component-header"><h3>{esc(assessment['prompt'])}</h3><span class="kind">Flip-card retrieval</span></header>
  <div class="component-body">
    <p class="component-intro">Say the answer before selecting each card. Select all four cards to complete this retrieval check.</p>
    <div class="flip-grid">{cards}</div>
    <div class="feedback" data-feedback aria-live="polite"></div>
  </div>
</section>"""


def render_matching(assessment: dict[str, Any]) -> str:
    targets = assessment["targets"]
    rows = []
    for pair in assessment["pairs"]:
        options = '<option value="">Choose a meaning job</option>' + "".join(
            f'<option value="{esc(target)}">{esc(target)}</option>' for target in targets
        )
        rows.append(
            f"""
<label class="match-row">
  <span>{esc(pair['prompt'])}</span>
  <select data-match-answer="{esc(pair['answer'])}">{options}</select>
</label>"""
        )
    return f"""
<section class="component" id="{esc(assessment['assessment_id'])}" data-matching
  data-purposeful-interaction="matching" data-quiz-type="matching"
  data-quiz-source="structured-module-package"
  data-completion="{esc(assessment['completion_id'])}"
  data-correct-feedback="{esc(assessment['feedback']['correct'])}"
  data-incorrect-feedback="{esc(assessment['feedback']['incorrect'])}">
  <header class="component-header"><h3>{esc(assessment['prompt'])}</h3><span class="kind">Relationship matching</span></header>
  <div class="component-body">
    <p class="component-intro">Match each ordinary-language question to the job that answers it. Check all rows together, then revise any row that needs another look.</p>
    <div class="match-grid">{''.join(rows)}</div>
    <button class="button primary" type="button" data-check-matching>Check the matches</button>
    <div class="feedback" data-feedback aria-live="polite"></div>
  </div>
</section>"""


def render_multi_select(assessment: dict[str, Any]) -> str:
    options = "\n".join(
        f"""
<label class="select-option">
  <input type="checkbox" data-multi-option data-correct="{str(bool(option['correct'])).lower()}">
  <span>{esc(option['text'])}</span>
</label>"""
        for option in assessment["options"]
    )
    return f"""
<section class="component" id="{esc(assessment['assessment_id'])}" data-multi-select
  data-purposeful-interaction="multi-select" data-quiz-type="multi-select"
  data-quiz-source="structured-module-package"
  data-completion="{esc(assessment['completion_id'])}"
  data-correct-feedback="{esc(assessment['feedback']['correct'])}"
  data-incorrect-feedback="{esc(assessment['feedback']['incorrect'])}">
  <header class="component-header"><h3>{esc(assessment['prompt'])}</h3><span class="kind">Context boundary check</span></header>
  <div class="component-body">
    <p class="component-intro">Select every item the bounded task needs. Leave irrelevant or unauthorized material outside the packet.</p>
    <div class="multi-grid">{options}</div>
    <button class="button primary" type="button" data-check-multi>Check the packet</button>
    <div class="feedback" data-feedback aria-live="polite"></div>
  </div>
</section>"""


def render_triple_builder(interaction: dict[str, Any]) -> str:
    config = interaction["config"]

    def options(values: list[str]) -> str:
        return '<option value="">Choose</option>' + "".join(
            f'<option value="{esc(value)}">{esc(value)}</option>' for value in values
        )

    return f"""
<section class="component" id="{esc(interaction['interaction_id'])}" data-triple-builder
  data-purposeful-interaction="triple-builder"
  data-component-source="structured-module-package"
  data-completion="{esc(interaction['completion_id'])}"
  data-correct="{esc(json.dumps(config['correct'], separators=(',', ':')))}"
  data-minimum-explanation="{esc(config['minimum_explanation_characters'])}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Triple construction</span></header>
  <div class="component-body">
    <p class="component-intro">{esc(interaction['instructions'])}</p>
    <div class="triple-builder">
      <label>Subject<select>{options(config['subjects'])}</select></label>
      <span class="triple-arrow" aria-hidden="true">→</span>
      <label>Predicate<select>{options(config['predicates'])}</select></label>
      <span class="triple-arrow" aria-hidden="true">→</span>
      <label>Object<select>{options(config['objects'])}</select></label>
    </div>
    <div class="triple-output" data-triple-output aria-live="polite">Choose all three positions.</div>
    <div class="button-row">
      <button class="button primary" type="button" data-check-triple>Check triple</button>
      <button class="button" type="button" data-reverse disabled>Reverse the ends</button>
    </div>
    <label class="work-product">Why does the reversed statement change the meaning?
      <textarea rows="3" placeholder="Explain the direction change"></textarea>
    </label>
    <button class="button good" type="button" data-finish-triple>Finish construction</button>
    <div class="feedback" data-feedback aria-live="polite"></div>
  </div>
</section>"""


def render_path_tracer(interaction: dict[str, Any]) -> str:
    config = interaction["config"]
    edges = []
    for index, edge in enumerate(config["edges"]):
        start = config["nodes"][index]
        end = config["nodes"][index + 1]
        edges.append(
            f"""
<button class="edge-button" type="button" data-edge-index="{index}" data-explanation="{esc(edge['explanation'])}">
  <strong>{index + 1}. {esc(start)} → {esc(edge['predicate'])} → {esc(end)}</strong>
  <span>{esc(edge['explanation'])}</span>
</button>"""
        )
    return f"""
<section class="component" id="{esc(interaction['interaction_id'])}" data-path-tracer
  data-purposeful-interaction="path-tracer"
  data-component-source="structured-module-package"
  data-completion="{esc(interaction['completion_id'])}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Evidence path</span></header>
  <div class="component-body">
    <p class="component-intro">{esc(interaction['instructions'])}</p>
    <div class="path-strip">{''.join(edges)}</div>
    <div class="button-row"><button class="button" type="button" data-reset-path>Reset path</button></div>
    <div class="feedback" data-feedback aria-live="polite">Begin with edge 1.</div>
  </div>
</section>"""


def render_artifact_classifier(interaction: dict[str, Any]) -> str:
    config = interaction["config"]
    jobs = config["jobs"]
    cards = []
    for index, item in enumerate(config["items"]):
        options = '<option value="">Choose the primary job</option>' + "".join(
            f'<option value="{esc(job)}">{esc(job)}</option>' for job in jobs
        )
        cards.append(
            f"""
<article class="triage-card" data-triage-item data-answer="{esc(item['answer'])}"
  data-explanation="{esc(item['explanation'])}">
  <span class="triage-number">{index + 1:02d}</span>
  <h4>{esc(item['title'])}</h4>
  <p>{esc(item['description'])}</p>
  <label>Primary job<select>{options}</select></label>
  <div class="item-feedback" data-item-feedback aria-live="polite"></div>
</article>"""
        )
    return f"""
<section class="component signature-component" id="{esc(interaction['interaction_id'])}" data-artifact-classifier
  data-purposeful-interaction="artifact-classifier"
  data-component-source="structured-module-package"
  data-completion="{esc(interaction['completion_id'])}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Meaning Triage Desk</span></header>
  <div class="component-body">
    <p class="component-intro">{esc(interaction['instructions'])}</p>
    <div class="triage-grid">{''.join(cards)}</div>
    <div class="button-row">
      <button class="button primary" type="button" data-check-triage>Check the desk</button>
      <button class="button" type="button" data-reset-triage>Reset</button>
    </div>
    <div class="feedback" data-feedback aria-live="polite"></div>
  </div>
</section>"""


def render_failure_trace(interaction: dict[str, Any]) -> str:
    paths = []
    for path in interaction["config"]["paths"]:
        steps = "".join(f"<li>{esc(step)}</li>" for step in path["steps"])
        paths.append(
            f"""
<button class="failure-trigger" type="button" data-failure-trigger="{esc(path['job'])}">
  <strong>{esc(path['job'])}</strong><span>{esc(path['missing'])}</span>
</button>
<article class="failure-result" data-failure-result="{esc(path['job'])}" hidden>
  <p class="failure-label">Follow the consequence</p>
  <ol>{steps}</ol>
  <p><strong>First repair:</strong> {esc(path['repair'])}</p>
  <p><strong>Accountable role:</strong> {esc(path['owner'])}</p>
</article>"""
        )
    return f"""
<section class="component signature-component" id="{esc(interaction['interaction_id'])}" data-failure-trace
  data-purposeful-interaction="failure-trace"
  data-component-source="structured-module-package"
  data-completion="{esc(interaction['completion_id'])}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Failure propagation laboratory</span></header>
  <div class="component-body">
    <p class="component-intro">{esc(interaction['instructions'])}</p>
    <div class="failure-lab">{''.join(paths)}</div>
    <div class="feedback" data-feedback aria-live="polite">Inspect all five failure paths.</div>
  </div>
</section>"""


def render_identity_adjudication(interaction: dict[str, Any]) -> str:
    config = interaction["config"]
    cards = []
    for item in config["records"]:
        options = '<option value="">Record a finding</option>' + "".join(
            f'<option value="{esc(finding)}">{esc(finding)}</option>' for finding in config["findings"]
        )
        cards.append(
            f"""<article class="docket-card" data-docket-record data-answer="{esc(item['answer'])}"
  data-explanation="{esc(item['explanation'])}">
  <span class="docket-source">{esc(item['source'])}</span><h4>{esc(item['identifier'])}</h4>
  <dl><div><dt>Location</dt><dd>{esc(item['location'])}</dd></div>
  <div><dt>Equipment</dt><dd>{esc(item['equipment'])}</dd></div>
  <div><dt>Evidence date</dt><dd>{esc(item['date'])}</dd></div></dl>
  <label>Finding<select>{options}</select></label>
  <div class="item-feedback" data-item-feedback aria-live="polite"></div></article>"""
        )
    return f"""
<section class="component signature-component identity-docket" id="{esc(interaction['interaction_id'])}"
  data-identity-adjudication data-purposeful-interaction="identity-adjudication"
  data-component-source="structured-module-package" data-completion="{esc(interaction['completion_id'])}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Identity evidence docket</span></header>
  <div class="component-body"><p class="component-intro">{esc(interaction['instructions'])}</p>
  <div class="docket-grid">{''.join(cards)}</div>
  <div class="button-row"><button class="button primary" type="button" data-check-docket>Submit findings</button>
  <button class="button" type="button" data-reset-docket>Clear docket</button></div>
  <div class="feedback" data-feedback aria-live="polite">Review all five records.</div></div>
</section>"""


def render_graph_growth_lab(interaction: dict[str, Any]) -> str:
    sources = interaction["config"]["sources"]
    packets = "".join(
        f'<button class="source-packet" type="button" data-source-packet="{esc(source["source"])}">'
        f'<strong>{esc(source["source"])}</strong><span>{esc(source["summary"])}</span>'
        f'<small>{len(source["statements"])} reviewed statements</small></button>'
        for source in sources
    )
    questions = "".join(
        f'<button class="graph-question" type="button" data-graph-question="{esc(item["question"])}" '
        f'data-requires="{esc(json.dumps(item["requires"], separators=(",", ":")))}" '
        f'data-answer="{esc(item["answer"])}" data-path="{esc(" → ".join(item["path"]))}">'
        f'<strong>{esc(item["label"])}</strong><span>{esc(item["question"])}</span></button>'
        for item in interaction["config"]["questions"]
    )
    return f"""
<section class="component signature-component graph-growth-lab" id="{esc(interaction['interaction_id'])}"
  data-graph-growth-lab data-purposeful-interaction="graph-growth-lab"
  data-component-source="structured-module-package" data-completion="{esc(interaction['completion_id'])}"
  data-source-statements="{esc(json.dumps(sources, separators=(',', ':')))}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Relationship discovery laboratory</span></header>
  <div class="component-body"><p class="component-intro">{esc(interaction['instructions'])}</p>
    <div class="graph-lab-layout">
      <aside class="source-shelf"><h4>Reviewed source packets</h4>{packets}</aside>
      <div class="graph-stage"><div class="graph-stage-header"><strong>Machine-readable statement ledger</strong>
        <span data-graph-count>0 statements loaded</span></div>
        <div class="statement-ledger" data-statement-ledger><p class="empty-state">Choose a source packet. Every statement remains attributable to its source.</p></div>
      </div>
    </div>
    <div class="question-console"><h4>Competency questions</h4>
      <p>Try each question as the graph grows. It unlocks only when every required source packet is present.</p>
      <div class="question-grid">{questions}</div>
      <article class="query-result" data-query-result aria-live="polite">No question tested yet.</article>
    </div>
    <div class="button-row"><button class="button" type="button" data-reset-graph>Reset graph</button></div>
    <div class="feedback" data-feedback aria-live="polite">Load source packets, then test all three questions.</div>
  </div>
</section>"""


def render_hierarchy_repair(interaction: dict[str, Any]) -> str:
    cases = "".join(
        f'<article class="repair-card" data-hierarchy-case data-answer="{esc(item["answer"])}" data-explanation="{esc(item["explanation"])}">'
        f'<h4>{esc(item["statement"])}</h4><p>{esc(item["consequence"])}</p><div class="button-row">'
        + "".join(f'<button class="button" type="button" data-hierarchy-choice="{esc(choice)}">{esc(choice)}</button>' for choice in interaction["config"]["choices"])
        + '</div><div class="item-feedback" data-item-feedback aria-live="polite"></div></article>'
        for item in interaction["config"]["cases"]
    )
    return f"""<section class="component signature-component" id="{esc(interaction['interaction_id'])}" data-hierarchy-repair
 data-purposeful-interaction="hierarchy-repair" data-component-source="structured-module-package" data-completion="{esc(interaction['completion_id'])}">
 <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Hierarchy consequence laboratory</span></header>
 <div class="component-body"><p class="component-intro">{esc(interaction['instructions'])}</p><div class="repair-grid">{cases}</div>
 <div class="feedback" data-feedback aria-live="polite">Review every classification statement.</div></div></section>"""


def render_ontology_canvas(interaction: dict[str, Any]) -> str:
    questions = "".join(
        f'<article class="canvas-card"><h4>{esc(item["question"])}</h4><p>{esc(item["purpose"])}</p>'
        f'<label>Decision<select data-canvas-answer="{esc(item["answer"])}"><option value="">Choose</option>'
        + "".join(f'<option value="{esc(choice)}">{esc(choice)}</option>' for choice in interaction["config"]["choices"])
        + f'</select></label><div class="item-feedback" data-item-feedback data-explanation="{esc(item["explanation"])}"></div></article>'
        for item in interaction["config"]["decisions"]
    )
    return f"""<section class="component signature-component" id="{esc(interaction['interaction_id'])}" data-ontology-canvas
 data-purposeful-interaction="ontology-canvas" data-component-source="structured-module-package" data-completion="{esc(interaction['completion_id'])}">
 <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Bounded modeling workshop</span></header>
 <div class="component-body"><p class="component-intro">{esc(interaction['instructions'])}</p><div class="canvas-grid">{questions}</div>
 <button class="button primary" type="button" data-check-canvas>Review ontology slice</button>
 <div class="feedback" data-feedback aria-live="polite"></div></div></section>"""


def render_sparql_builder(interaction: dict[str, Any]) -> str:
    clauses = "".join(
        f'<button class="query-clause" type="button" data-query-clause="{index}" data-code="{esc(item["code"])}" '
        f'data-effect="{esc(item["effect"])}"><strong>{index + 1}. {esc(item["label"])}</strong><code>{esc(item["code"])}</code></button>'
        for index, item in enumerate(interaction["config"]["clauses"])
    )
    return f"""<section class="component signature-component" id="{esc(interaction['interaction_id'])}" data-sparql-builder
 data-purposeful-interaction="sparql-builder" data-component-source="structured-module-package" data-completion="{esc(interaction['completion_id'])}">
 <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">SPARQL query laboratory</span></header>
 <div class="component-body"><p class="component-intro">{esc(interaction['instructions'])}</p>
 <div class="query-lab"><div class="query-clause-shelf">{clauses}</div><div class="query-console"><pre data-query-code># Select clause 1 to begin</pre>
 <div class="query-effect" data-query-effect aria-live="polite">The graph pattern will illuminate here.</div></div></div>
 <button class="button" type="button" data-reset-query>Reset query</button><div class="feedback" data-feedback aria-live="polite">Assemble every clause in order.</div></div></section>"""


def render_decision_lab(interaction: dict[str, Any], component: str, kind: str, card_attr: str, choice_attr: str) -> str:
    choices = interaction["config"]["choices"]
    cards = "".join(
        f'<article class="decision-case" {card_attr} data-answer="{esc(item["answer"])}" data-explanation="{esc(item["explanation"])}">'
        f'<span class="case-label">{esc(item.get("label", f"Case {index + 1}"))}</span><h4>{esc(item["claim"])}</h4>'
        f'<div class="case-evidence">{esc(item["evidence"])}</div><div class="case-rule"><strong>Declared control</strong><br>{esc(item["rule"])}</div>'
        f'<div class="button-row">{"".join(f"""<button class="button" type="button" {choice_attr}="{esc(choice)}">{esc(choice)}</button>""" for choice in choices)}</div>'
        f'<div class="item-feedback" data-item-feedback aria-live="polite"></div></article>'
        for index, item in enumerate(interaction["config"]["cases"])
    )
    return f"""<section class="component signature-component decision-lab" id="{esc(interaction['interaction_id'])}" data-{component}
 data-purposeful-interaction="{component}" data-component-source="structured-module-package" data-completion="{esc(interaction['completion_id'])}">
 <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">{esc(kind)}</span></header>
 <div class="component-body"><p class="component-intro">{esc(interaction['instructions'])}</p>
 <div class="decision-case-grid">{cards}</div><div class="feedback" data-feedback aria-live="polite">Resolve every case and read its evidence explanation.</div></div></section>"""


def render_inference_court(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "inference-court", "OWL model court", "data-inference-case", "data-inference-choice")


def render_shacl_clinic(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "shacl-clinic", "SHACL validation clinic", "data-shacl-case", "data-shacl-choice")


def render_evidence_reconciliation(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "evidence-reconciliation", "Evidence reconciliation hearing", "data-evidence-case", "data-evidence-choice")


def render_knowledge_spine_router(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "knowledge-spine-router", "Knowledge Spine routing studio", "data-spine-case", "data-spine-choice")


def render_accountability_handoff(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "accountability-handoff", "Accountability handoff", "data-handoff-case", "data-handoff-choice")


def render_mapping_workbench(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "mapping-workbench", "Source-to-concept wiring bench", "data-mapping-case", "data-mapping-choice")


def render_mapping_break_repair(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "mapping-break-repair", "Mapping break and repair laboratory", "data-map-repair-case", "data-map-repair-choice")


def render_access_pattern_stress_test(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "access-pattern-stress-test", "Access-pattern stress board", "data-access-case", "data-access-choice")


def render_stale_copy_diagnosis(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "stale-copy-diagnosis", "Stale-copy failure rehearsal", "data-stale-case", "data-stale-choice")


def render_evidence_promotion(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "evidence-promotion", "Document-to-claim promotion rail", "data-promotion-case", "data-promotion-choice")


def render_evidence_state_classifier(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "evidence-state-classifier", "Evidence-state investigation", "data-evidence-state-case", "data-evidence-state-choice")


def render_context_assembly(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "context-assembly", "Runtime context assembly console", "data-context-case", "data-context-choice")


def render_permission_gate(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "permission-gate", "Fail-closed permission gate", "data-permission-case", "data-permission-choice")


def render_pipeline_rerun(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "pipeline-rerun", "Synchronized answer-pipeline laboratory", "data-pipeline-case", "data-pipeline-choice")


def render_pipeline_stage_diagnosis(interaction: dict[str, Any]) -> str:
    return render_decision_lab(interaction, "pipeline-stage-diagnosis", "Repeatability microscope", "data-stage-case", "data-stage-choice")


def render_object_router(interaction: dict[str, Any]) -> str:
    cards = []
    for index, item in enumerate(interaction["config"]["items"]):
        cards.append(
            f"""
<article class="route-card" data-route-item data-answer="{esc(item['answer'])}"
  data-explanation="{esc(item['explanation'])}">
  <span class="triage-number">{index + 1:02d}</span>
  <h4>{esc(item['statement'])}</h4>
  <p>{esc(item['question'])}</p>
  <div class="button-row">
    <button class="button" type="button" data-route-choice="Resource">Another resource</button>
    <button class="button" type="button" data-route-choice="Literal">Literal value</button>
  </div>
  <div class="item-feedback" data-item-feedback aria-live="polite"></div>
</article>"""
        )
    return f"""
<section class="component signature-component" id="{esc(interaction['interaction_id'])}" data-object-router
  data-purposeful-interaction="object-router" data-component-source="structured-module-package"
  data-completion="{esc(interaction['completion_id'])}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Object fork</span></header>
  <div class="component-body">
    <p class="component-intro">{esc(interaction['instructions'])}</p>
    <div class="route-grid">{''.join(cards)}</div>
    <div class="feedback" data-feedback aria-live="polite">Route every object.</div>
  </div>
</section>"""


def render_triple_repair_bench(interaction: dict[str, Any]) -> str:
    cards = []
    for index, item in enumerate(interaction["config"]["repairs"]):
        defect_options = '<option value="">Choose the defect</option>' + "".join(
            f'<option value="{esc(value)}">{esc(value)}</option>'
            for value in interaction["config"]["defect_types"]
        )
        repair_options = '<option value="">Choose the repair</option>' + "".join(
            f'<option value="{esc(value)}">{esc(value)}</option>'
            for value in item["repair_options"]
        )
        cards.append(
            f"""
<article class="repair-card" data-repair-card data-defect="{esc(item['defect'])}"
  data-repair="{esc(item['repair'])}" data-explanation="{esc(item['explanation'])}">
  <span class="triage-number">BENCH {index + 1:02d}</span>
  <p class="broken-statement">{esc(item['broken'])}</p>
  <div class="repair-fields">
    <label>What failed?<select data-defect-field>{defect_options}</select></label>
    <label>Smallest defensible repair<select data-repair-field>{repair_options}</select></label>
  </div>
  <div class="item-feedback" data-item-feedback aria-live="polite"></div>
</article>"""
        )
    return f"""
<section class="component signature-component" id="{esc(interaction['interaction_id'])}" data-triple-repair-bench
  data-purposeful-interaction="triple-repair-bench" data-component-source="structured-module-package"
  data-completion="{esc(interaction['completion_id'])}">
  <header class="component-header"><h3>{esc(interaction['title'])}</h3><span class="kind">Triple Evidence Bench</span></header>
  <div class="component-body">
    <p class="component-intro">{esc(interaction['instructions'])}</p>
    <div class="repair-grid">{''.join(cards)}</div>
    <button class="button primary" type="button" data-check-repairs>Review all repairs</button>
    <div class="feedback" data-feedback aria-live="polite"></div>
  </div>
</section>"""


def render_work_product(assessment: dict[str, Any]) -> str:
    labels = {
        "subject": "Subject",
        "predicate": "Predicate",
        "object": "Object",
        "source": "Authoritative source",
        "question": "Utility question this relationship helps answer",
    }
    fields = []
    labels.update(assessment.get("field_labels", {}))
    long_fields = set(assessment.get("textarea_fields", ["question"]))
    for field in assessment["required_fields"]:
        if field in long_fields:
            fields.append(
                f'<label>{esc(labels[field])}<textarea name="{esc(field)}" rows="3" required></textarea></label>'
            )
        else:
            fields.append(
                f'<label>{esc(labels.get(field, field.title()))}<input name="{esc(field)}" required></label>'
            )
    return f"""
<section class="component" id="{esc(assessment['assessment_id'])}"
  data-purposeful-interaction="applied-work-product"
  data-component-source="structured-module-package">
  <header class="component-header"><h3>{esc(assessment.get('title', 'Professional Work Product'))}</h3><span class="kind">Professional work product</span></header>
  <div class="component-body">
    <p class="component-intro">{esc(assessment['prompt'])}</p>
    <form class="work-product" data-work-product="{esc(assessment['assessment_id'])}"
      data-artifact="{esc(assessment['assessment_id'])}"
      data-completion="{esc(assessment['completion_id'])}"
      data-correct-feedback="{esc(assessment['feedback']['correct'])}"
      data-incorrect-feedback="{esc(assessment['feedback']['incorrect'])}">
      <div class="field-grid">{''.join(fields[:-1])}</div>
      {fields[-1]}
      <button class="button primary" type="submit">Save {esc(assessment.get('title', 'Work Product'))}</button>
      <div class="feedback" data-feedback aria-live="polite"></div>
      <pre class="artifact-preview" data-artifact-preview>Your local preview will appear here.</pre>
    </form>
  </div>
</section>"""


def render_faq(items: list[dict[str, Any]]) -> str:
    details = "\n".join(
        f"<details><summary>{esc(item['question'])}</summary><p>{esc(item['answer'])}</p></details>"
        for item in items
    )
    return f"""
<section class="faq-list" aria-labelledby="faq-heading" data-module-faq>
  <h3 id="faq-heading">Questions people actually ask</h3>
  {details}
</section>"""


def render_evidence(block: dict[str, Any], sources: dict[str, dict[str, Any]]) -> str:
    links = "".join(
        f'<li><a href="{esc(sources[source_id]["url"])}">{esc(sources[source_id]["title"])}</a>, {esc(sources[source_id]["authority"])}</li>'
        for source_id in block.get("source_refs", [])
    )
    return f"""
<section class="evidence" data-evidence-boundary>
  <h3>Evidence boundary</h3>
  <p>{esc(block['statement'])}</p>
  <ul>{links}</ul>
</section>"""


def render_block(
    block: dict[str, Any],
    package: dict[str, Any],
    asset_prefix: str,
) -> str:
    block_type = block["type"]
    if block_type == "prose":
        paragraphs = "".join(f"<p>{esc(paragraph)}</p>" for paragraph in block["paragraphs"])
        return f'<div class="prose">{paragraphs}</div>'
    if block_type == "callout":
        return f'<aside class="callout"><h3>{esc(block["title"])}</h3><p>{esc(block["text"])}</p></aside>'
    if block_type == "visual":
        return render_visual(package["visuals"][block["visual_id"]], asset_prefix)
    if block_type == "interaction":
        interaction = package["interactions"][block["interaction_id"]]
        if interaction["component"] == "triple-builder":
            return render_triple_builder(interaction)
        if interaction["component"] == "path-tracer":
            return render_path_tracer(interaction)
        if interaction["component"] == "artifact-classifier":
            return render_artifact_classifier(interaction)
        if interaction["component"] == "failure-trace":
            return render_failure_trace(interaction)
        if interaction["component"] == "identity-adjudication":
            return render_identity_adjudication(interaction)
        if interaction["component"] == "graph-growth-lab":
            return render_graph_growth_lab(interaction)
        if interaction["component"] == "hierarchy-repair":
            return render_hierarchy_repair(interaction)
        if interaction["component"] == "ontology-canvas":
            return render_ontology_canvas(interaction)
        if interaction["component"] == "sparql-builder":
            return render_sparql_builder(interaction)
        if interaction["component"] == "inference-court":
            return render_inference_court(interaction)
        if interaction["component"] == "shacl-clinic":
            return render_shacl_clinic(interaction)
        if interaction["component"] == "evidence-reconciliation":
            return render_evidence_reconciliation(interaction)
        if interaction["component"] == "knowledge-spine-router":
            return render_knowledge_spine_router(interaction)
        if interaction["component"] == "accountability-handoff":
            return render_accountability_handoff(interaction)
        if interaction["component"] == "mapping-workbench":
            return render_mapping_workbench(interaction)
        if interaction["component"] == "mapping-break-repair":
            return render_mapping_break_repair(interaction)
        if interaction["component"] == "access-pattern-stress-test":
            return render_access_pattern_stress_test(interaction)
        if interaction["component"] == "stale-copy-diagnosis":
            return render_stale_copy_diagnosis(interaction)
        if interaction["component"] == "evidence-promotion":
            return render_evidence_promotion(interaction)
        if interaction["component"] == "evidence-state-classifier":
            return render_evidence_state_classifier(interaction)
        if interaction["component"] == "context-assembly":
            return render_context_assembly(interaction)
        if interaction["component"] == "permission-gate":
            return render_permission_gate(interaction)
        if interaction["component"] == "pipeline-rerun":
            return render_pipeline_rerun(interaction)
        if interaction["component"] == "pipeline-stage-diagnosis":
            return render_pipeline_stage_diagnosis(interaction)
        if interaction["component"] == "object-router":
            return render_object_router(interaction)
        return render_triple_repair_bench(interaction)
    if block_type == "assessment":
        assessment = package["assessments"][block["assessment_id"]]
        if assessment["type"] == "multiple-choice":
            return render_choice(assessment)
        if assessment["type"] == "flip-cards":
            return render_flip_cards(assessment)
        if assessment["type"] == "matching":
            return render_matching(assessment)
        if assessment["type"] == "multi-select":
            return render_multi_select(assessment)
    if block_type == "work_product":
        return render_work_product(package["assessments"][block["work_product_id"]])
    if block_type == "faq":
        return render_faq(block["items"])
    if block_type == "evidence":
        return render_evidence(block, package["sources"])
    raise ModulePackageError(f"cannot render block type {block_type}")


def render_module(
    package: dict[str, Any],
    *,
    asset_prefix: str = "../",
    course_href: str = "../../curriculum/course-meaning-before-models.html",
) -> str:
    module_data = package["module_data"]
    module = module_data["module"]
    learning = module_data["learning"]
    completion = module_data["completion"]
    required_ids = completion["required_ids"]
    sections = []
    for index, section in enumerate(module_data["sections"], start=1):
        blocks = "\n".join(
            render_block(block, package, asset_prefix) for block in section["blocks"]
        )
        sections.append(
            f"""
<section class="lesson-section" id="{esc(section['section_id'])}">
  <header class="section-heading">
    <span class="section-number">{index:02d}</span>
    <div><span class="kind">{esc(section.get('kind', 'Teaching section'))}</span><h2>{esc(section['title'])}</h2></div>
  </header>
  {blocks}
</section>"""
        )

    progress = "\n".join(
        f'<div class="progress-item" data-completion-id="{esc(item)}">{esc(item.replace("-", " ").title())}</div>'
        for item in required_ids
    )
    outcomes = "".join(f"<li>{esc(outcome)}</li>" for outcome in learning["outcomes"])
    glossary_items = []
    for term in package["glossary"]:
        short = f" ({esc(term['short'])})" if term.get("short") else ""
        glossary_items.append(
            f'<article><h3>{esc(term["term"])}{short}</h3><p>{esc(term["definition"])}</p></article>'
        )
    glossary = "".join(glossary_items)
    source_cards = "".join(
        f'<article><h3>{esc(source["title"])}</h3><p>{esc(source["use"])}</p><a href="{esc(source["url"])}">Open source</a></article>'
        for source in package["sources"].values()
    )
    css = RUNTIME_CSS.read_text(encoding="utf-8")
    script = RUNTIME_JS.read_text(encoding="utf-8")
    release_label = "release-ready" if package["release_ready"] else "structured working candidate"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(module['title'])} | One Water OS Academy</title>
  <meta name="description" content="{esc(module['promise'])}">
  <meta name="owos-course-id" content="{esc(module['course_id'])}">
  <meta name="owos-learning-object" content="{esc(module['module_id'])}">
  <meta name="owos-release-state" content="{esc(release_label)}">
  <meta name="owos-source-version" content="{esc(module['source_version'])}">
  <meta name="owos-compiler-version" content="{COMPILER_VERSION}">
  <meta name="owos-package-checksum" content="{package['checksum']}">
  <style>{css}</style>
</head>
<body data-module-id="{esc(module['module_id'])}" data-source-version="{esc(module['source_version'])}"
  data-required-ids="{esc(json.dumps(required_ids, separators=(',', ':')))}">
  <a class="skip-link" href="#lesson-start">Skip to lesson</a>
  <header class="topbar">
    <div class="shell topbar-inner">
      <a class="brand" href="{esc(course_href)}">OW <span>One Water OS Academy</span></a>
      <nav class="top-actions" aria-label="Lesson tools">
        <button class="button" type="button" data-open-drawer="graph">Graph</button>
        <button class="button" type="button" data-open-drawer="glossary">Glossary</button>
        <a class="button primary" href="#lesson-start">Start</a>
      </nav>
    </div>
  </header>
  <main id="lesson-start">
    <section class="hero">
      <div class="shell">
        <span class="eyebrow">{esc(module.get('eyebrow', module['archetype']))}</span>
        <h1>{esc(module['title'])}</h1>
        <p>{esc(module['promise'])}</p>
        <div class="hero-meta"><span>{esc(module['duration'])}</span><span>{esc(module['level'])}</span><span>{esc(module['archetype'].replace('-', ' '))}</span></div>
      </div>
    </section>
    <section class="shell progress-panel" aria-label="Completion evidence">{progress}</section>
    <div class="shell">
      <section class="lesson-section">
        <header class="section-heading"><span class="section-number">✓</span><div><span class="kind">Learner promise</span><h2>What you will be able to do</h2></div></header>
        <div class="prose"><ul>{outcomes}</ul><p><strong>Misconception we will change:</strong> {esc(learning['misconception'])}</p></div>
      </section>
{''.join(sections)}
      <section id="owos-course-community" class="connected">
        <article><span class="kind">Knowledge Graph</span><h3>Inspect the lesson relationships</h3><p>See the concepts, sources, competency, and evidence boundary behind this module.</p><button class="button" type="button" data-open-drawer="graph">Open Graph</button></article>
        <article><span class="kind">Community</span><h3>Compare one real relationship</h3><p>Discuss which relationship your utility repeatedly rebuilds by hand. Community discussion is not governed evidence.</p><button class="button" type="button" disabled>Community in platform runtime</button></article>
      </section>
      <section class="completion">
        <h2>Complete the working candidate</h2>
        <p>{esc(completion['rule'])}</p>
        <button class="button good" type="button" data-complete-module disabled>Complete module</button>
        <p data-completion-status aria-live="polite"></p>
      </section>
    </div>
  </main>
  <div class="drawer-scrim" data-drawer-scrim></div>
  <aside class="drawer" data-drawer="graph" aria-hidden="true">
    <header class="drawer-head"><h2>Lesson Graph</h2><button class="button" type="button" data-close-drawer>Close</button></header>
    <p>This module connects an RDF triple, a utility relationship, a graph path, a source boundary, and the competency to construct one source-bounded relationship.</p>
    <div class="glossary-list">{source_cards}</div>
  </aside>
  <aside class="drawer" data-drawer="glossary" aria-hidden="true">
    <header class="drawer-head"><h2>Module Glossary</h2><button class="button" type="button" data-close-drawer>Close</button></header>
    <div class="glossary-list">{glossary}</div>
  </aside>
  <footer><div class="shell">{esc(release_label)}. Compiler {COMPILER_VERSION}. Source {esc(module['source_version'])}. No credential or operational authority.</div></footer>
  <script>{script}</script>
</body>
</html>
"""


def build_module(
    module_dir: Path,
    output: Path | None,
    *,
    release_ready: bool = False,
    asset_prefix: str = "../",
    course_href: str = "../../curriculum/course-meaning-before-models.html",
) -> dict[str, Any]:
    package = validate_package(module_dir, release_ready=release_ready)
    output_path = output.resolve() if output else package["module_dir"] / "build/index.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rendered = render_module(
        package,
        asset_prefix=asset_prefix,
        course_href=course_href,
    )
    output_path.write_text(rendered, encoding="utf-8")
    return {
        "status": "built",
        "module_id": package["module_data"]["module"]["module_id"],
        "output": str(output_path),
        "checksum": package["checksum"],
        "compiler_version": COMPILER_VERSION,
        "release_ready": release_ready,
    }


def inspect_package(module_dir: Path) -> dict[str, Any]:
    package = validate_package(module_dir)
    return {
        "module": package["module_data"]["module"],
        "learning": package["module_data"]["learning"],
        "sections": [
            {
                "section_id": section["section_id"],
                "title": section["title"],
                "block_types": [block["type"] for block in section["blocks"]],
            }
            for section in package["module_data"]["sections"]
        ],
        "storyboard": package["storyboard"],
        "visuals": list(package["visuals"].values()),
        "interactions": list(package["interactions"].values()),
        "assessments": list(package["assessments"].values()),
        "qa": package["qa"],
        "checksum": package["checksum"],
        "compiler_version": COMPILER_VERSION,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "inspect"):
        sub = subparsers.add_parser(command)
        sub.add_argument("module_dir", type=Path)
        if command == "validate":
            sub.add_argument("--release-ready", action="store_true")
    build = subparsers.add_parser("build")
    build.add_argument("module_dir", type=Path)
    build.add_argument("--output", type=Path)
    build.add_argument("--release-ready", action="store_true")
    build.add_argument(
        "--asset-prefix",
        default="../",
        help="prefix placed before module-relative visual locators",
    )
    build.add_argument(
        "--course-href",
        default="../../curriculum/course-meaning-before-models.html",
        help="course landing link for the selected delivery target",
    )
    args = parser.parse_args()

    try:
        if args.command == "validate":
            result = validate_package(args.module_dir, release_ready=args.release_ready)
            output = {
                "status": "valid",
                "module_id": result["module_data"]["module"]["module_id"],
                "checksum": result["checksum"],
                "compiler_version": COMPILER_VERSION,
                "release_ready": args.release_ready,
            }
        elif args.command == "inspect":
            output = inspect_package(args.module_dir)
        else:
            output = build_module(
                args.module_dir,
                args.output,
                release_ready=args.release_ready,
                asset_prefix=args.asset_prefix,
                course_href=args.course_href,
            )
    except ModulePackageError as error:
        print(f"OWOS Course Compiler failed:\n{error}", file=sys.stderr)
        return 1
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
