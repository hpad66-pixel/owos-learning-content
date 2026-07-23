#!/usr/bin/env python3
"""Validate a full OWOS module against the binding production contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup


DEFAULT_CONTRACT = {
    "minimum_visual_types": 4,
    "minimum_purposeful_interactions": 2,
    "minimum_quiz_types": 3,
    "minimum_faq_questions": 5,
    "minimum_defined_terms": 5,
    "require_experience_fingerprint": False,
    "require_structured_flip_cards": False,
    "minimum_flip_answer_chars": 0,
    "approved_component_sources": ["component-gallery", "shared-component-library"],
    "approved_quiz_sources": ["quiz-gallery", "applied-assessment-contract"],
    "visual_catalog_terms": {},
    "required_community_features": [
        "search",
        "filters",
        "bookmarks",
        "threaded-replies",
        "presence",
        "instructor-treatment",
    ],
}

BANNED = (
    "\u2014",
    "\u2013",
    "delve",
    "dive into",
    "tapestry",
    "testament to",
    "game-changer",
    "revolutionary",
)


class ConformanceError(ValueError):
    """Raised when a full module fails the production contract."""


def load_contract(path: Path | None) -> dict:
    contract = dict(DEFAULT_CONTRACT)
    if path:
        contract.update(json.loads(path.read_text(encoding="utf-8")))
    return contract


def linked_styles(path: Path, soup: BeautifulSoup) -> str:
    styles = "\n".join(tag.get_text(" ", strip=False) for tag in soup.find_all("style"))
    for link in soup.find_all("link", rel=lambda value: value and "stylesheet" in value):
        href = link.get("href", "")
        if not href or href.startswith(("http://", "https://", "/")):
            continue
        candidate = (path.parent / href).resolve()
        if candidate.is_file():
            styles += "\n" + candidate.read_text(encoding="utf-8")
    return styles


def require_sections(text: str, headings: list[str], label: str, errors: list[str]) -> None:
    for heading in headings:
        if heading not in text:
            errors.append(f"{label} is missing required section: {heading}")


def validate_qa_report(path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"missing scored QA report: {path}")
        return
    text = path.read_text(encoding="utf-8")
    require_sections(
        text,
        [
            "score:",
            "score_out_of: 100",
            "working_status:",
            "release_status:",
            "## Scored quality review",
            "## Hard gates",
            "## Automated checks",
            "## Manual review still required",
            "## Required revisions",
            "## Approval record",
        ],
        "QA report",
        errors,
    )
    if not re.search(r"score:\s*[1-9][0-9]?\b", text):
        errors.append("QA report needs a numeric score from 1 to 99")
    for gate in (
        "Accuracy and evidence",
        "Learning design",
        "Utility-practitioner review",
        "Technical and accessibility review",
        "Release control",
    ):
        if gate not in text:
            errors.append(f"QA report is missing hard gate: {gate}")


def validate_module(
    lesson: Path,
    qa: Path,
    brief: Path,
    script: Path,
    contract_path: Path | None = None,
) -> dict:
    contract = load_contract(contract_path)
    text = lesson.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, "html.parser")
    errors: list[str] = []

    for phrase in BANNED:
        if phrase.lower() in text.lower():
            errors.append(f"learner-facing lesson contains prohibited language or punctuation: {phrase}")

    if not soup.find("meta", attrs={"name": "viewport"}):
        errors.append("lesson needs a mobile viewport declaration")
    for name in ("owos-course-id", "owos-learning-object", "owos-release-state"):
        if not soup.find("meta", attrs={"name": name, "content": True}):
            errors.append(f"lesson needs stable metadata: {name}")
    if len(soup.find_all("main")) != 1 or len(soup.find_all("h1")) != 1:
        errors.append("lesson needs exactly one main landmark and one h1")
    if contract.get("require_experience_fingerprint"):
        body = soup.find("body")
        if not body or not body.get("data-experience"):
            errors.append("lesson needs a named data-experience narrative architecture")
        if not soup.select_one(".question-flips[data-card-layout]"):
            errors.append("lesson needs a named question-card composition")

    header = soup.find("header") or soup.find("nav")
    if not header:
        errors.append("lesson needs a header")
    else:
        for selector, label in (
            ("[data-open-graph]", "Graph"),
            ("[data-open-community]", "Community"),
            ('a[href="#lesson-start"]', "Start"),
        ):
            if not header.select_one(selector):
                errors.append(f"lesson header is missing {label}")

    if not soup.select_one("#lesson-start"):
        errors.append("Start action needs a #lesson-start target")
    if not soup.select_one("[data-opening-decision][data-required]"):
        errors.append("lesson needs a consequential opening decision with completion evidence")

    for lens in ("foundation", "practitioner", "leader"):
        if not soup.select_one(f'[data-lens="{lens}"]'):
            errors.append(f"lesson is missing the {lens} instructional lens")

    visuals = soup.select("[data-visual-type]")
    visual_types = [item.get("data-visual-type", "").strip() for item in visuals]
    unique_visuals = sorted({item for item in visual_types if item})
    if len(unique_visuals) < int(contract["minimum_visual_types"]):
        errors.append(
            f"lesson needs {contract['minimum_visual_types']} visual types; found {unique_visuals}"
        )
    governed_visuals = [item for item in visuals if item.get("id", "").startswith("visual-")]
    governed_shapes = {
        item.get("data-visual-shape", "").strip()
        for item in governed_visuals
        if item.get("data-visual-shape", "").strip()
    }
    minimum_shapes = int(contract.get("minimum_distinct_visual_shapes", 0))
    if minimum_shapes and len(governed_shapes) < minimum_shapes:
        errors.append(
            f"lesson needs {minimum_shapes} structurally distinct visual shapes; "
            f"found {sorted(governed_shapes)}"
        )
    approved_sources = set(contract["approved_component_sources"])
    for visual in visuals:
        visual_id = visual.get("id")
        if not visual_id:
            errors.append("every governed visual needs a stable id")
            continue
        if visual.get("data-component-source") not in approved_sources:
            errors.append(f"{visual_id} does not identify an approved component source")
        if visual_id.startswith("visual-"):
            if not visual.get("data-visual-family"):
                errors.append(f"{visual_id} needs a governed visual family")
            if not visual.get("data-visual-shape"):
                errors.append(f"{visual_id} needs a structural visual-shape fingerprint")
        if not visual.select_one("[data-reading-guide]"):
            errors.append(f"{visual_id} needs a visible reading guide")
        if not visual.select_one("[data-learner-conclusion]"):
            errors.append(f"{visual_id} needs a learner conclusion")
        explanation = soup.select_one(
            f'[data-instructor-explanation][data-teaches~="{visual_id}"]'
        )
        if not explanation:
            errors.append(f"{visual_id} needs a preceding instructor explanation")
        elif explanation.sourceline and visual.sourceline and explanation.sourceline > visual.sourceline:
            errors.append(f"{visual_id} instructor explanation must appear before the visual")

    catalog_path = Path(__file__).resolve().parents[1] / "core/components/COMPONENTS.md"
    gallery_path = Path(__file__).resolve().parents[1] / "core/components/component-gallery.html"
    catalog_text = catalog_path.read_text(encoding="utf-8").lower()
    gallery_text = gallery_path.read_text(encoding="utf-8").lower()
    visual_catalog_terms = contract.get("visual_catalog_terms", {})
    for visual_type in unique_visuals:
        catalog_term = visual_catalog_terms.get(visual_type)
        if not catalog_term and contract.get("allow_lesson_specific_visual_types"):
            catalog_term = contract.get("lesson_specific_visual_catalog_term")
        if not catalog_term:
            errors.append(f"visual type has no shared catalog trace: {visual_type}")
        elif (
            catalog_term.lower() not in catalog_text
            or catalog_term.lower() not in gallery_text
        ):
            errors.append(
                f"visual type does not exist in both shared component references: {visual_type}"
            )

    interactions = soup.select("[data-purposeful-interaction][data-required]")
    if len(interactions) < int(contract["minimum_purposeful_interactions"]):
        errors.append(
            "lesson needs at least "
            f"{contract['minimum_purposeful_interactions']} purposeful required interactions"
        )
    approved_quiz_sources = set(contract["approved_quiz_sources"])
    for interaction in interactions:
        source = interaction.get("data-component-source") or interaction.get("data-quiz-source")
        if source not in approved_sources | approved_quiz_sources:
            errors.append(
                f"purposeful interaction lacks governed component or quiz provenance: "
                f"{interaction.get('id', interaction.get('data-purposeful-interaction'))}"
            )

    quizzes = soup.select("[data-quiz-type][data-required]")
    quiz_types = [item.get("data-quiz-type", "").strip() for item in quizzes]
    unique_quizzes = sorted({item for item in quiz_types if item})
    if len(unique_quizzes) < int(contract["minimum_quiz_types"]):
        errors.append(
            f"lesson needs {contract['minimum_quiz_types']} quiz types; found {unique_quizzes}"
        )
    flip_cards = soup.select('[data-quiz-type="flip-cards"] .flip-question')
    minimum_flip_cards = int(contract.get("minimum_question_flip_cards", 0))
    if len(flip_cards) < minimum_flip_cards:
        errors.append(
            f"lesson needs {minimum_flip_cards} question flip cards; found {len(flip_cards)}"
        )
    if contract.get("require_structured_flip_cards"):
        answers = []
        minimum_answer_chars = int(contract.get("minimum_flip_answer_chars", 0))
        for index, card in enumerate(flip_cards, start=1):
            front = card.select_one(".flip-inner .flip-front")
            back = card.select_one(".flip-inner .flip-back")
            if not front or not back:
                errors.append(
                    f"flip card {index} needs governed inner, question-face, and answer-face structure"
                )
                continue
            if card.get("aria-pressed") not in {"false", "true"}:
                errors.append(f"flip card {index} needs an aria-pressed state")
            if len(front.get_text(" ", strip=True)) < 20:
                errors.append(f"flip card {index} question is too short to teach")
            answer = back.get_text(" ", strip=True)
            if len(answer) < minimum_answer_chars:
                errors.append(
                    f"flip card {index} answer needs at least {minimum_answer_chars} characters"
                )
            answers.append(answer)
        if len(answers) != len(set(answers)):
            errors.append("flip-card answers must be module-specific, not repeated filler")
    for left, right in zip(quiz_types, quiz_types[1:]):
        if left and left == right:
            errors.append(f"quiz type repeats consecutively: {left}")
    for quiz in quizzes:
        quiz_id = quiz.get("id", "unnamed quiz")
        if quiz.get("data-quiz-source") not in approved_quiz_sources:
            errors.append(f"{quiz_id} does not identify an approved quiz source")
        if not quiz.get("data-retry"):
            errors.append(f"{quiz_id} needs an explanatory retry message")
        if not quiz.select_one("[aria-live]"):
            errors.append(f"{quiz_id} needs an accessible live-feedback region")
        explanation = soup.select_one(
            f'[data-instructor-explanation][data-teaches~="{quiz_id}"]'
        )
        if not explanation:
            errors.append(f"{quiz_id} needs a preceding instructor explanation")

    artifacts = {
        item.get("data-artifact")
        for item in soup.select("[data-artifact][data-required]")
        if item.get("data-artifact")
    }
    final_checks = soup.select("[data-final-applied-check][data-required][data-artifact-ref]")
    if not final_checks:
        errors.append("lesson needs a deterministic final applied check tied to the work product")
    for check in final_checks:
        if check.get("data-artifact-ref") not in artifacts:
            errors.append("final applied check references an unknown work product")

    faq = soup.select_one("[data-module-faq]")
    if not faq:
        errors.append("lesson needs a module-specific FAQ")
    elif len(faq.find_all("details")) < int(contract["minimum_faq_questions"]):
        errors.append(
            f"FAQ needs {contract['minimum_faq_questions']} questions"
        )
    evidence = soup.select_one("[data-evidence-boundary]")
    if not evidence:
        errors.append("lesson needs an explicit evidence boundary")
    if faq and evidence and faq.sourceline and evidence.sourceline and faq.sourceline > evidence.sourceline:
        errors.append("module FAQ must appear before the evidence boundary")
    if evidence and len(evidence.find_all("a", href=True)) < 3:
        errors.append("evidence boundary needs at least three linked sources")

    graph = soup.select_one('[data-drawer="graph"]')
    if not graph:
        errors.append("lesson needs a same-page Graph drawer")
    else:
        if graph.get("data-component-source") not in approved_sources:
            errors.append("Graph drawer lacks governed component provenance")
        for kind in ("concept", "source", "role", "competency", "relationship"):
            if not graph.select_one(f'[data-graph-kind="{kind}"]'):
                errors.append(f"Graph drawer is missing {kind} context")

    community = soup.select_one('[data-drawer="community"]')
    if not community:
        errors.append("lesson needs a same-page Community drawer")
    else:
        if community.get("data-component-source") not in approved_sources:
            errors.append("Community drawer lacks governed component provenance")
        present = {
            node.get("data-community-feature")
            for node in community.select("[data-community-feature]")
        }
        for feature in contract["required_community_features"]:
            if feature not in present:
                errors.append(f"Community drawer is missing feature: {feature}")

    anchor = soup.select_one("#owos-course-community")
    navigation = soup.select_one(".footnav")
    if not anchor or not navigation:
        errors.append("lesson needs bottom connected learning followed by lesson navigation")
    elif (
        anchor.sourceline
        and navigation.sourceline
        and anchor.sourceline > navigation.sourceline
    ):
        errors.append("#owos-course-community must appear before bottom navigation")

    tooltips = soup.select("#tt")
    terms = soup.select(".term[data-def]")
    if len(tooltips) != 1:
        errors.append("lesson needs exactly one tooltip element with id tt")
    if len(terms) < int(contract["minimum_defined_terms"]):
        errors.append(
            f"lesson needs at least {contract['minimum_defined_terms']} defined terms; found {len(terms)}"
        )
    if soup.select("[title]"):
        errors.append("title attributes create duplicate tooltips and are prohibited")

    styles = linked_styles(lesson, soup)
    if "@media" not in styles:
        errors.append("lesson needs responsive style rules")
    if "prefers-reduced-motion" not in styles:
        errors.append("lesson needs reduced-motion style rules")
    if not re.search(r"\.(?:dark|hero|drawer-head)[^{]*\{[^}]*color:\s*(?:#fff|white|var\(--light)", styles, re.I | re.S):
        errors.append("dark teaching surfaces need an explicit light-text rule")

    requirements = {
        item.get("data-requirement")
        for item in soup.select("[data-requirement]")
        if item.get("data-requirement")
    }
    declared = {
        item.get("data-required")
        for item in soup.select("[data-required]")
        if item.get("data-required")
    }
    if not declared.issubset(requirements):
        errors.append(
            "every data-required value must appear in the visible completion requirements"
        )
    if not soup.select_one("[data-complete][disabled]"):
        errors.append("lesson needs a completion control that begins disabled")

    brief_text = brief.read_text(encoding="utf-8") if brief.is_file() else ""
    if not brief_text:
        errors.append(f"missing module design brief: {brief}")
    else:
        require_sections(
            brief_text,
            [
                "## Concept-to-experience plan",
                "## Module design fingerprint",
                "## Instructor explanation plan",
                "## Visual pacing review",
                "## Explanatory graphic plan",
                "## Learner FAQ plan",
                "## Recording script",
                "## Diversity check",
                "## Approval",
            ],
            "module design brief",
            errors,
        )
        for visual_type in unique_visuals:
            if visual_type not in brief_text:
                errors.append(
                    f"design brief does not trace implemented visual type: {visual_type}"
                )
        for quiz_type in unique_quizzes:
            if quiz_type not in brief_text:
                errors.append(
                    f"design brief does not trace implemented quiz type: {quiz_type}"
                )

    if not script.is_file():
        errors.append(f"missing module recording script: {script}")
    else:
        script_text = script.read_text(encoding="utf-8")
        for marker in ("Spoken words", "Visual direction"):
            if marker not in script_text:
                errors.append(f"recording script is missing marker: {marker}")

    validate_qa_report(qa, errors)
    if errors:
        raise ConformanceError("\n".join(f"- {error}" for error in errors))

    return {
        "lesson": lesson.name,
        "visual_types": unique_visuals,
        "purposeful_interactions": len(interactions),
        "quiz_types": unique_quizzes,
        "required_evidence": len(declared),
        "defined_terms": len(terms),
        "community_features": contract["required_community_features"],
        "status": "full-module working conformance passed",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lesson", type=Path, required=True)
    parser.add_argument("--qa", type=Path, required=True)
    parser.add_argument("--brief", type=Path, required=True)
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--contract", type=Path)
    args = parser.parse_args()
    try:
        result = validate_module(
            args.lesson,
            args.qa,
            args.brief,
            args.script,
            args.contract,
        )
    except (ConformanceError, FileNotFoundError, json.JSONDecodeError) as error:
        print(f"OWOS full-module conformance failed:\n{error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
