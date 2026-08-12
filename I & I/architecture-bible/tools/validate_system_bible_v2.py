#!/usr/bin/env python3
"""Validate Version 2 source preservation and explanatory coverage."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

import build_integrated_system_bible as v1


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
ROOT = PACKAGE.parent


def between(text: str, start: str, end: str) -> str:
    anchored_start = "\n" + start + "\n"
    anchored_end = "\n" + end + "\n"
    return text.split(anchored_start, 1)[1].split(anchored_end, 1)[0]


def build_normalized_source(markdown: str) -> str:
    shifted = v1.shift_headings(markdown, 1).strip()
    return "\n".join(line.rstrip() for line in shifted.splitlines())


def main() -> None:
    bible = (PACKAGE / "ii-intelligence-system-bible-v2.md").read_text()
    engineering = (ROOT / "white-paper.md").read_text()
    architecture = (PACKAGE / "white-paper.md").read_text()
    registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
    manifest = yaml.safe_load((PACKAGE / "operationalization-manifest.yaml").read_text())
    errors: list[str] = []

    shifted_engineering = build_normalized_source(engineering)
    shifted_architecture = build_normalized_source(architecture)
    if bible.count(shifted_engineering) != 1:
        errors.append("complete shifted engineering source volume is not present exactly once")
    if bible.count(shifted_architecture) != 1:
        errors.append("complete shifted architecture source volume is not present exactly once")

    formula_book = between(bible, "# Book II. Every formula explained", "# Book III. Every source and input explained")
    formula_headings = re.findall(r"^## Formula \d+\. (F-[^:]+):", formula_book, re.MULTILINE)
    expected_formula_ids = [item["id"] for item in registry["formulae"]]
    if formula_headings != expected_formula_ids:
        errors.append("formula explanation order or coverage does not match the 39-formula registry")
    required_formula_sections = [
        "### The question it answers",
        "### What it means and why it is calculated",
        "### Inputs, meaning, and origin",
        "### What the calculation does",
        "### What the result conveys",
        "### How it connects to the larger equation",
        "### How the agent and human reviewer use it",
        "### What must not be inferred",
    ]
    for section in required_formula_sections:
        if formula_book.count(section) != len(expected_formula_ids):
            errors.append(f"formula narrative section count failed for {section}")

    source_book = between(
        bible,
        "# Book III. Every source and input explained",
        "# Book IV. Every dashboard value and decision explained",
    )
    for source in manifest["source_classes"]:
        if f"## {source['id']}. {source['name']}" not in source_book:
            errors.append(f"missing explanatory source story for {source['id']}")

    dashboard_book = between(
        bible,
        "# Book IV. Every dashboard value and decision explained",
        "# Source-volume completeness statement",
    )
    for metric in manifest["dashboard_metrics"]:
        if f"## {metric['id']} / #{metric['number']}. {metric['label']}" not in dashboard_book:
            errors.append(f"missing explanatory metric story for {metric['id']}")
    for decision in manifest["decision_bindings"]:
        if f"## {decision['id']}. {decision['name']}" not in dashboard_book:
            errors.append(f"missing explanatory decision story for {decision['id']}")

    rtk_markers = [
        "RTK explained: R, T, K",
        "F-RTK-001`, component volume and duration",
        "F-RTK-002`, triangular component peak and ordinate",
        "F-RTK-003`, event superposition",
        "## Formula 9. F-RTK-001",
        "## Formula 10. F-RTK-002",
        "## Formula 11. F-RTK-003",
        "## 5. RTK explains the shape of rainfall response",
    ]
    for marker in rtk_markers:
        if marker not in bible:
            errors.append(f"missing RTK discoverability marker: {marker}")

    for index in range(1, 10):
        screenshot_pattern = f"dashboard-mockups/screenshots/{index:02d}-"
        if screenshot_pattern not in bible:
            errors.append(f"missing dashboard screenshot reference {index:02d}")

    prohibited = ["—", "–", "game-changer", "tapestry", "moreover", "furthermore"]
    for token in prohibited:
        if token.lower() in bible.lower():
            errors.append(f"prohibited punctuation or phrase found: {token}")

    trailing = [index for index, line in enumerate(bible.splitlines(), start=1) if line.rstrip() != line]
    if trailing:
        errors.append(f"trailing whitespace found on {len(trailing)} lines")
    if bible.count("```") % 2:
        errors.append("code fences are not balanced")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    print("PASS: complete engineering source volume included exactly once")
    print("PASS: complete architecture source volume included exactly once")
    print(f"PASS: {len(expected_formula_ids)} formulas receive eight-part explanatory treatment")
    print(f"PASS: {len(manifest['source_classes'])} source classes receive explanatory treatment")
    print(f"PASS: {len(manifest['dashboard_metrics'])} dashboard metrics receive explanatory treatment")
    print(f"PASS: {len(manifest['decision_bindings'])} decisions receive explanatory treatment")
    print("PASS: RTK is explicit in the master contents, system story, formula book, and preserved source")
    print("PASS: 9 populated dashboard figures remain included")


if __name__ == "__main__":
    main()
