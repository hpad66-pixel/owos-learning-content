#!/usr/bin/env python3
"""Validate formula, source, result, dashboard, and decision traceability."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
ROOT = PACKAGE.parent


def resolve_path(value, path: str):
    current = value
    for part in path.split("."):
        current = current[part]
    return current


def main() -> None:
    registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
    manifest = yaml.safe_load((PACKAGE / "operationalization-manifest.yaml").read_text())
    results = json.loads((ROOT / "generated/sample-basin-results.json").read_text())
    bible = (PACKAGE / "ii-intelligence-system-bible.md").read_text()
    mockup_html = (PACKAGE / "dashboard-mockups" / "index.html").read_text()
    mockup_markdown = (PACKAGE / "dashboard-mockups.md").read_text()
    screenshot_dir = PACKAGE / "dashboard-mockups" / "screenshots"

    errors: list[str] = []
    formula_ids = [item["id"] for item in registry["formulae"]]
    formula_set = set(formula_ids)
    source_set = {item["id"] for item in manifest["source_classes"]}
    metrics = manifest["dashboard_metrics"]
    metric_set = {item["id"] for item in metrics}

    if len(formula_ids) != len(formula_set):
        errors.append("formula registry contains duplicate identifiers")

    formula_headings = re.findall(r"^## Formula \d+: (F-[^,]+),", bible, re.MULTILINE)
    if formula_headings != formula_ids:
        errors.append("generated formula catalog does not match registry order and coverage")

    metric_numbers = [item["number"] for item in metrics]
    if metric_numbers != list(range(1, len(metrics) + 1)):
        errors.append("dashboard metric numbers are not contiguous from 1")

    for metric in metrics:
        unknown_formulae = set(metric.get("formula_ids", [])) - formula_set
        if unknown_formulae:
            errors.append(f"{metric['id']} references unknown formulae {sorted(unknown_formulae)}")
        unknown_sources = set(metric.get("source_classes", [])) - source_set
        if unknown_sources:
            errors.append(f"{metric['id']} references unknown sources {sorted(unknown_sources)}")
        try:
            resolve_path(results, metric["result_path"])
        except Exception:
            errors.append(f"{metric['id']} result path does not resolve: {metric['result_path']}")
        marker = f"| {metric['number']} | `{metric['id']}`"
        if marker not in bible:
            errors.append(f"{metric['id']} is absent from generated traceability table")
        if metric["id"] not in mockup_html:
            errors.append(f"{metric['id']} is absent from populated dashboard prototype")

    for number in range(1, 10):
        dash_id = f"DASH-{number:02d}"
        if dash_id not in mockup_markdown:
            errors.append(f"{dash_id} is absent from dashboard mockup appendix")
        expected = list(screenshot_dir.glob(f"{number:02d}-*.png"))
        if len(expected) != 1 or expected[0].stat().st_size == 0:
            errors.append(f"{dash_id} does not resolve to one nonempty screenshot")

    if "# Part VII. Fully populated dashboard mockups" not in bible:
        errors.append("integrated Bible does not contain the populated dashboard appendix")

    for decision in manifest["decision_bindings"]:
        unknown_metrics = set(decision["metric_ids"]) - metric_set
        if unknown_metrics:
            errors.append(f"{decision['id']} references unknown metrics {sorted(unknown_metrics)}")

    for gap in manifest.get("lineage_gaps", []):
        unknown_metrics = set(gap["metric_ids"]) - metric_set
        if unknown_metrics:
            errors.append(f"{gap['id']} references unknown metrics {sorted(unknown_metrics)}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    print(f"PASS: {len(formula_ids)} formulae cataloged")
    print(f"PASS: {len(manifest['source_classes'])} source classes resolved")
    print(f"PASS: {len(metrics)} numbered dashboard metrics resolve to sample results")
    print(f"PASS: {len(manifest['decision_bindings'])} decision bindings resolve")
    print(f"PASS: {len(manifest.get('lineage_gaps', []))} visible lineage gaps retained")
    print("PASS: 9 populated dashboard mockups and screenshots resolve")


if __name__ == "__main__":
    main()
