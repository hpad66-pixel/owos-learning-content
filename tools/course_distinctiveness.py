#!/usr/bin/env python3
"""Audit a complete OWOS course for factory-pattern lesson repetition."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

from bs4 import BeautifulSoup


DEFAULTS = {
    "maximum_archetype_share": 0.33,
    "maximum_identical_quiz_sequence_count": 2,
    "maximum_identical_interaction_signature_count": 2,
    "maximum_adjacent_structural_similarity": 0.82,
    "maximum_repeated_faq_question_count": 2,
    "maximum_repeated_instructor_paragraph_count": 3,
    "factory_pattern_share": 0.40,
}

LEGACY_QUIZZES = {
    "classify",
    "estimate",
    "fill",
    "flip",
    "match",
    "matching",
    "mc",
    "multi",
    "order",
    "ordering",
    "reflect",
    "reflection",
    "tf",
    "truefalse",
}


class DistinctivenessError(ValueError):
    """Raised when the rendered course repeats a lesson factory pattern."""


def normalize(value: str) -> str:
    value = re.sub(r"\b(?:module|chapter|lesson)\s+\d+\b", "module", value, flags=re.I)
    value = re.sub(r"\b\d+(?:\.\d+)?\b", "#", value)
    return re.sub(r"\s+", " ", value.strip().lower())


def lesson_files(course: Path, manifest: dict) -> list[Path]:
    configured = manifest.get("lessons", {})
    if configured:
        return [
            course / "curriculum" / name
            for name, config in configured.items()
            if config.get("include", True)
        ]
    return sorted(
        path
        for path in (course / "curriculum").glob("module-[0-9][0-9]-*.html")
        if ".artifact." not in path.name
    )


def metadata(soup: BeautifulSoup, name: str) -> str:
    node = soup.find("meta", attrs={"name": name})
    return node.get("content", "").strip() if node else ""


def ordered_markers(soup: BeautifulSoup) -> list[str]:
    markers = []
    for node in soup.select(
        "section, [data-visual-type], [data-quiz-type], [data-purposeful-interaction], [data-artifact], [data-ac]"
    ):
        if node.has_attr("data-visual-type"):
            markers.append(f"visual:{node['data-visual-type']}")
        elif node.has_attr("data-ac"):
            kind = node.get("data-ac", "").strip()
            prefix = "quiz" if kind in LEGACY_QUIZZES else "component"
            markers.append(f"{prefix}:{kind}")
        elif node.has_attr("data-quiz-type"):
            markers.append(f"quiz:{node['data-quiz-type']}")
        elif node.has_attr("data-purposeful-interaction"):
            markers.append(f"interaction:{node['data-purposeful-interaction']}")
        elif node.has_attr("data-artifact"):
            markers.append(f"artifact:{node.name}")
        else:
            classes = ".".join(node.get("class", [])[:3])
            markers.append(f"section:{classes or 'plain'}")
    return markers


def inspect_lesson(path: Path, config: dict) -> dict:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    archetype = config.get("archetype") or metadata(soup, "owos-lesson-archetype")
    mechanism = config.get("signature_mechanism") or metadata(
        soup, "owos-signature-mechanism"
    )
    opening = config.get("opening") or metadata(soup, "owos-opening-pattern")
    work_product = config.get("work_product_mode") or metadata(
        soup, "owos-work-product-mode"
    )
    quizzes = tuple(
        node.get("data-quiz-type", "").strip()
        for node in soup.select("[data-quiz-type]")
        if node.get("data-quiz-type")
    )
    legacy_components = tuple(
        node.get("data-ac", "").strip()
        for node in soup.select("[data-ac]")
        if node.get("data-ac")
    )
    quizzes = quizzes + tuple(
        kind for kind in legacy_components if kind in LEGACY_QUIZZES
    )
    interactions = tuple(
        node.get("data-purposeful-interaction", "").strip()
        for node in soup.select("[data-purposeful-interaction]")
        if node.get("data-purposeful-interaction")
    )
    interactions = interactions + tuple(
        kind for kind in legacy_components if kind not in LEGACY_QUIZZES
    )
    visuals = tuple(
        node.get("data-visual-type", "").strip()
        for node in soup.select("[data-visual-type]")
        if node.get("data-visual-type")
    )
    visuals = visuals + tuple(
        kind for kind in legacy_components if kind not in LEGACY_QUIZZES
    )
    faqs = tuple(
        normalize(node.get_text(" ", strip=True))
        for node in soup.select("[data-module-faq] summary")
    )
    instructor_paragraphs = tuple(
        normalize(node.get_text(" ", strip=True))
        for node in soup.select("[data-instructor-explanation] p")
        if len(normalize(node.get_text(" ", strip=True))) >= 80
    )
    counts = (
        len(soup.select("main section")),
        len(soup.find_all("button")),
        len(soup.find_all(["input", "select", "textarea"])),
        len(soup.find_all("details")),
        len(visuals),
        len(quizzes),
        len(interactions),
    )
    markers = ordered_markers(soup)
    return {
        "file": path.name,
        "title": soup.h1.get_text(" ", strip=True) if soup.h1 else path.stem,
        "archetype": archetype,
        "signature_mechanism": mechanism,
        "opening": opening,
        "work_product_mode": work_product,
        "quiz_sequence": quizzes,
        "interaction_signature": interactions,
        "visual_sequence": visuals,
        "faqs": faqs,
        "instructor_paragraphs": instructor_paragraphs,
        "counts": counts,
        "structure": "|".join(markers),
    }


def minimum_archetypes(total: int) -> int:
    if total <= 5:
        return 3
    if total <= 10:
        return 4
    if total <= 16:
        return 5
    return 6


def repeated_values(records: list[dict], field: str) -> dict:
    grouped = defaultdict(list)
    for record in records:
        value = record[field]
        if value:
            grouped[value].append(record["file"])
    return grouped


def audit(course: Path) -> dict:
    manifest_path = course / ".course" / "experience-architecture.json"
    manifest = (
        json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest_path.is_file()
        else {}
    )
    thresholds = dict(DEFAULTS)
    thresholds.update(manifest.get("thresholds", {}))
    files = lesson_files(course, manifest)
    if not files:
        raise DistinctivenessError(f"no lesson files found in {course}")
    missing = [path for path in files if not path.is_file()]
    if missing:
        raise DistinctivenessError(
            "configured lesson files do not exist: " + ", ".join(str(path) for path in missing)
        )
    configured = manifest.get("lessons", {})
    records = [
        inspect_lesson(path, configured.get(path.name, {}))
        for path in files
    ]
    errors: list[str] = []
    warnings: list[str] = []

    for field, label in (
        ("archetype", "lesson archetype"),
        ("signature_mechanism", "signature mechanism"),
        ("opening", "opening pattern"),
        ("work_product_mode", "work-product mode"),
    ):
        absent = [record["file"] for record in records if not record[field]]
        if absent:
            errors.append(f"{label} is undeclared for: {', '.join(absent)}")

    archetypes = Counter(record["archetype"] for record in records if record["archetype"])
    required_archetypes = int(
        manifest.get("minimum_archetypes", minimum_archetypes(len(records)))
    )
    if len(archetypes) < required_archetypes:
        errors.append(
            f"course needs at least {required_archetypes} lesson archetypes; found {len(archetypes)}"
        )
    max_share = float(thresholds["maximum_archetype_share"])
    for archetype, count in archetypes.items():
        if count / len(records) > max_share + 1e-9:
            errors.append(
                f"archetype {archetype!r} occupies {count}/{len(records)} lessons, above {max_share:.0%}"
            )

    mechanisms = repeated_values(records, "signature_mechanism")
    for mechanism, names in mechanisms.items():
        if len(names) > 1:
            errors.append(
                f"signature mechanism {mechanism!r} is reused by: {', '.join(names)}"
            )

    for field, limit_key, label in (
        (
            "quiz_sequence",
            "maximum_identical_quiz_sequence_count",
            "quiz sequence",
        ),
        (
            "interaction_signature",
            "maximum_identical_interaction_signature_count",
            "interaction signature",
        ),
    ):
        limit = int(thresholds[limit_key])
        for value, names in repeated_values(records, field).items():
            if len(names) > limit:
                errors.append(
                    f"identical {label} appears in {len(names)} lessons: {', '.join(names)}"
                )

    count_groups = defaultdict(list)
    for record in records:
        count_groups[record["counts"]].append(record["file"])
    factory_share = float(thresholds["factory_pattern_share"])
    for vector, names in count_groups.items():
        if len(names) >= 4 and len(names) / len(records) >= factory_share:
            errors.append(
                "factory-pattern control counts "
                f"{vector} recur in {len(names)}/{len(records)} lessons: {', '.join(names)}"
            )

    adjacent = []
    similarity_limit = float(thresholds["maximum_adjacent_structural_similarity"])
    for left, right in zip(records, records[1:]):
        similarity = SequenceMatcher(None, left["structure"], right["structure"]).ratio()
        adjacent.append(
            {
                "left": left["file"],
                "right": right["file"],
                "similarity": round(similarity, 3),
            }
        )
        if similarity > similarity_limit:
            errors.append(
                f"adjacent structural similarity {similarity:.1%} exceeds {similarity_limit:.0%}: "
                f"{left['file']} and {right['file']}"
            )

    faq_limit = int(thresholds["maximum_repeated_faq_question_count"])
    faq_usage = defaultdict(list)
    paragraph_usage = defaultdict(list)
    for record in records:
        for question in set(record["faqs"]):
            faq_usage[question].append(record["file"])
        for paragraph in set(record["instructor_paragraphs"]):
            paragraph_usage[paragraph].append(record["file"])
    for question, names in faq_usage.items():
        if len(names) > faq_limit:
            errors.append(
                f"FAQ question is repeated in {len(names)} lessons: {question!r}"
            )
    paragraph_limit = int(thresholds["maximum_repeated_instructor_paragraph_count"])
    for paragraph, names in paragraph_usage.items():
        if len(names) > paragraph_limit:
            errors.append(
                f"generic instructor paragraph is repeated in {len(names)} lessons: "
                f"{paragraph[:120]!r}"
            )

    for left, right in zip(records, records[1:]):
        same = [
            label
            for field, label in (
                ("archetype", "archetype"),
                ("opening", "opening"),
                ("quiz_sequence", "quiz sequence"),
                ("interaction_signature", "interaction signature"),
                ("work_product_mode", "work-product mode"),
            )
            if left[field] and left[field] == right[field]
        ]
        if len(same) >= 3:
            errors.append(
                f"adjacent lessons repeat {', '.join(same)}: {left['file']} and {right['file']}"
            )

    if not manifest_path.is_file():
        warnings.append(
            "missing .course/experience-architecture.json; rendered metadata alone was audited"
        )
    return {
        "course": str(course),
        "lessons": len(records),
        "archetypes": dict(archetypes),
        "adjacent_similarity": adjacent,
        "errors": errors,
        "warnings": warnings,
        "status": "passed" if not errors else "blocked",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", type=Path, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = audit(args.course.resolve())
    except (DistinctivenessError, json.JSONDecodeError) as error:
        print(f"OWOS course distinctiveness audit failed:\n{error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(
            f"{result['status'].upper()}: {result['lessons']} lessons, "
            f"{len(result['archetypes'])} archetypes"
        )
        for warning in result["warnings"]:
            print(f"WARNING: {warning}")
        for error in result["errors"]:
            print(f"BLOCKER: {error}")
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
