#!/usr/bin/env python3
"""Validate Version 3 source preservation and model-integration coverage."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

import build_integrated_system_bible as v1


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
ROOT = PACKAGE.parent


def between(text: str, start: str, end: str) -> str:
    return text.split("\n" + start + "\n", 1)[1].split("\n" + end + "\n", 1)[0]


def normalized_shifted(markdown: str) -> str:
    shifted = v1.shift_headings(markdown, 1).strip()
    return "\n".join(line.rstrip() for line in shifted.splitlines())


def main() -> None:
    bible = (PACKAGE / "ii-intelligence-system-bible-v3.md").read_text()
    registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
    manifest = yaml.safe_load((PACKAGE / "operationalization-manifest.yaml").read_text())
    errors: list[str] = []

    exact_sources = [
        (
            "\n".join(
                line.rstrip()
                for line in (PACKAGE / "model-integration-v3.md").read_text().strip().splitlines()
            ),
            "EPA SWMM and EPANET integration source volume",
        ),
        (normalized_shifted((ROOT / "white-paper.md").read_text()), "engineering source volume"),
        (
            normalized_shifted((PACKAGE / "white-paper.md").read_text()),
            "operational Architecture Bible source volume",
        ),
        (
            normalized_shifted((PACKAGE / "open-source-repository-landscape.md").read_text()),
            "open-source repository landscape",
        ),
    ]
    for source, label in exact_sources:
        if bible.count(source) != 1:
            errors.append(f"complete {label} is not present exactly once")

    formula_book = between(
        bible,
        "# Book III. Every formula explained",
        "# Book IV. Every source and input explained",
    )
    expected_formula_ids = [item["id"] for item in registry["formulae"]]
    formula_headings = re.findall(r"^## Formula \d+\. (F-[^:]+):", formula_book, re.MULTILINE)
    if formula_headings != expected_formula_ids:
        errors.append("formula explanation order or coverage does not match the formula registry")
    for section in [
        "### The question it answers",
        "### What it means and why it is calculated",
        "### Inputs, meaning, and origin",
        "### What the calculation does",
        "### What the result conveys",
        "### How it connects to the larger equation",
        "### How the agent and human reviewer use it",
        "### What must not be inferred",
    ]:
        if formula_book.count(section) != len(expected_formula_ids):
            errors.append(f"formula narrative section count failed for {section}")

    source_book = between(
        bible,
        "# Book IV. Every source and input explained",
        "# Book V. Every dashboard value and decision explained",
    )
    for source in manifest["source_classes"]:
        if f"## {source['id']}. {source['name']}" not in source_book:
            errors.append(f"missing source story for {source['id']}")

    dashboard_book = between(
        bible,
        "# Book V. Every dashboard value and decision explained",
        "# Version 3 source-volume completeness statement",
    )
    for metric in manifest["dashboard_metrics"]:
        marker = f"## {metric['id']} / #{metric['number']}. {metric['label']}"
        if marker not in dashboard_book:
            errors.append(f"missing dashboard metric story for {metric['id']}")
    for decision in manifest["decision_bindings"]:
        if f"## {decision['id']}. {decision['name']}" not in dashboard_book:
            errors.append(f"missing decision story for {decision['id']}")

    required_markers = [
        "## 5A. EPA SWMM routes the response through the represented sewer",
        "## 6A. EPANET independently checks the pressurized pump and force-main problem",
        "# Book II. EPA SWMM, EPANET, and the governed model layer",
        "## 4. EPA SWMM in detailed plain English",
        "## 5. Running EPA SWMM through Python with PySWMM",
        "python -m pip install \"pyswmm[swmm5.2.4]\"",
        "python run_swmm_model.py Example1.inp --node 21 --link 15",
        "## 6. EPANET in detailed plain English",
        "## 7. Running EPANET from Python through WNTR",
        "python -m pip install wntr",
        "## 9. With-model and without-model scenarios",
        "## 10. Model outputs on the dashboards",
        "### 10.2 Model Assurance dashboard mockup",
        "## 11. Model service architecture",
        "## 12. Agent behavior around SWMM and EPANET",
        "https://github.com/USEPA/Stormwater-Management-Model",
        "https://github.com/pyswmm/pyswmm",
        "https://github.com/OpenWaterAnalytics/EPANET",
        "https://github.com/USEPA/WNTR",
    ]
    required_markers.extend(f"`M-{number}`" for number in range(35, 45))
    for marker in required_markers:
        if marker not in bible:
            errors.append(f"missing Version 3 marker: {marker}")

    for index in range(1, 10):
        if f"dashboard-mockups/screenshots/{index:02d}-" not in bible:
            errors.append(f"missing dashboard screenshot reference {index:02d}")

    for token in ["—", "–", "game-changer", "tapestry", "moreover", "furthermore"]:
        if token.lower() in bible.lower():
            errors.append(f"prohibited punctuation or phrase found: {token}")
    trailing = [number for number, line in enumerate(bible.splitlines(), 1) if line.rstrip() != line]
    if trailing:
        errors.append(f"trailing whitespace found on {len(trailing)} lines")
    if bible.count("```") % 2:
        errors.append("code fences are not balanced")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    print("PASS: four governed source volumes are included exactly once")
    print(f"PASS: {len(expected_formula_ids)} formulas receive eight-part explanatory treatment")
    print(f"PASS: {len(manifest['source_classes'])} source classes receive explanatory treatment")
    print(f"PASS: {len(manifest['dashboard_metrics'])} worked dashboard metrics receive explanatory treatment")
    print(f"PASS: {len(manifest['decision_bindings'])} decisions receive explanatory treatment")
    print("PASS: EPA SWMM and EPANET appear in the connected story and detailed model book")
    print("PASS: PySWMM and WNTR installation and execution runbooks are present")
    print("PASS: model-assurance metrics M-35 through M-44 are wired")
    print("PASS: 9 populated dashboard figures remain included")

    manifest_path = PACKAGE / "build-manifest-v3.yaml"
    build_manifest = yaml.safe_load(manifest_path.read_text())
    build_manifest["validation"]["status"] = "passed"
    manifest_path.write_text(
        yaml.safe_dump(build_manifest, sort_keys=False, allow_unicode=False)
    )


if __name__ == "__main__":
    main()
