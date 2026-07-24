#!/usr/bin/env python3
"""Machine-enforced learner-experience checks for released OWOS lessons."""

from __future__ import annotations

import json
import re
from pathlib import Path


COMPONENT = re.compile(
    r'<div\s+(?P<attrs>[^>]*\bdata-ac="(?P<kind>[^"]+)"[^>]*)>\s*'
    r'<script\s+type="application/json">(?P<config>[\s\S]*?)</script>',
    re.I,
)


class CourseQualityError(ValueError):
    """Raised when a released lesson fails the OWOS quality contract."""


def fail(path: Path, message: str) -> None:
    raise CourseQualityError(f"{path.as_posix()}: {message}")


def validate_table(path: Path, config: dict) -> None:
    headers = config.get("headers", config.get("cols"))
    rows = config.get("rows")
    if not isinstance(headers, list) or not headers:
        fail(path, "table component needs a non-empty headers or cols list")
    if not isinstance(rows, list) or not rows:
        fail(path, "table component needs a non-empty rows list")
    for index, row in enumerate(rows, start=1):
        if isinstance(row, list):
            if len(row) < 2 or not row[0]:
                fail(path, f"table row {index} needs a label and at least one cell")
            continue
        if not isinstance(row, dict) or not row.get("name") or not isinstance(row.get("cells"), list):
            fail(path, f"table row {index} needs name and cells")


def validate_multi(path: Path, config: dict) -> None:
    options = config.get("options")
    if not isinstance(options, list) or len(options) < 2:
        fail(path, "multi-select component needs at least two options")
    for index, option in enumerate(options, start=1):
        if not isinstance(option, list) or len(option) < 2 or not isinstance(option[1], bool):
            fail(path, f"multi-select option {index} needs text and a deterministic boolean answer")


def validate_lesson(path: Path, contract: dict) -> dict:
    """Validate one built lesson and return auditable quality metrics."""

    text = path.read_text(encoding="utf-8")
    effective = text
    for href in re.findall(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"', text, re.I):
        if href.startswith(("http://", "https://", "/")):
            continue
        stylesheet = (path.parent / href).resolve()
        if stylesheet.is_file():
            effective += "\n" + stylesheet.read_text(encoding="utf-8")
    lowered = effective.lower()
    minimum = int(contract.get("minimum_purposeful_interactions", 2))

    if re.search(r"\bundefined\b", text, re.I):
        fail(path, "contains the undefined sentinel")
    if '<meta name="viewport"' not in lowered:
        fail(path, "needs a mobile viewport declaration")
    if "@media" not in lowered:
        fail(path, "needs responsive layout rules")
    if "prefers-reduced-motion" not in lowered:
        fail(path, "needs reduced-motion behavior")
    if "aria-live" not in lowered:
        fail(path, "needs an accessible live-feedback region")
    if not re.search(r"<(button|input|select|textarea)\b", lowered):
        fail(path, "needs keyboard-operable learner controls")

    components = []
    for match in COMPONENT.finditer(text):
        kind = match.group("kind").strip().lower()
        if kind == "type":
            continue
        attrs = match.group("attrs")
        try:
            config = json.loads(match.group("config"))
        except json.JSONDecodeError as error:
            fail(path, f"{kind} component has invalid JSON: {error.msg}")
        if not isinstance(config, dict):
            fail(path, f"{kind} component configuration must be an object")
        if kind != "reflect" and ('data-title="' not in attrs or 'data-kind="' not in attrs):
            fail(path, f"{kind} component needs a visible title and interaction kind")
        if kind == "table":
            validate_table(path, config)
        if kind == "multi":
            validate_multi(path, config)
        components.append(kind)

    legacy_component_count = len(components)

    # The current OWOS master-class runtime uses semantic HTML data contracts instead of the
    # legacy JSON component wrapper. Count only controls with deterministic answer, completion,
    # or artifact contracts so visual decoration cannot satisfy the quality gate.
    native_components = []
    native_rules = {
        "quiz": r"\bdata-quiz=",
        "matching": r"\bdata-match=",
        "simulation": r"\bdata-stepper=",
        "lab": r"\bdata-lab=",
        "work_product": r"\bdata-artifact=",
        "custom_quiz": r'class="[^"]*\bquiz\b[^"]*"',
        "custom_simulation": r'id="playSteps"',
        "custom_lab": r'id="runRepair"',
        "custom_work_product": r'id="contractForm"',
        "structured_triple_builder": r"\bdata-triple-builder\b",
        "structured_path_tracer": r"\bdata-path-tracer\b",
        "structured_choice": r"\bdata-choice-group\b",
        "structured_flip_cards": r"\bdata-flip-group\b",
        "structured_work_product": r"\bdata-work-product\b",
    }
    for kind, pattern in native_rules.items():
        if re.search(pattern, text, re.I):
            native_components.append(kind)
    for interaction in re.findall(
        r'\bdata-purposeful-interaction="([^"]+)"',
        text,
        re.I,
    ):
        native_components.append(f"purposeful:{interaction.strip().lower()}")
    if native_components:
        modern_contract = any(
            marker in text
            for marker in ("data-quiz=", "data-match=", "data-stepper=", "data-lab=", "data-artifact=")
        )
        has_completion_contract = (
            "data-required=" in text
            or (
                "data-required-ids=" in text
                and "data-completion=" in text
            )
        )
        if legacy_component_count == 0 and modern_contract and not has_completion_contract:
            fail(
                path,
                "native interactions need completion evidence through "
                "data-required or structured data-completion contracts",
            )
        if "data-quiz=" in text and "data-correct=" not in text:
            fail(path, "native quizzes need deterministic data-correct answers")
        if "data-match=" in text and "data-answer=" not in text:
            fail(path, "native matching needs deterministic data-answer values")
        components.extend(native_components)

    purposeful = [kind for kind in components if kind != "reflect"]
    if len(purposeful) < minimum:
        fail(path, f"needs at least {minimum} purposeful interactions; found {len(purposeful)}")

    return {
        "lesson": path.name,
        "purposeful_interactions": len(purposeful),
        "component_types": sorted(set(purposeful)),
        "responsive": True,
        "reduced_motion": True,
        "live_feedback": True,
        "keyboard_controls": True,
        "undefined_sentinel": False,
    }
