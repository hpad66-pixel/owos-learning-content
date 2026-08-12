#!/usr/bin/env python3

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
sources = yaml.safe_load((ROOT / "sources.yaml").read_text())
results = json.loads(
    (ROOT / "generated" / "sample-basin-results.json").read_text()
)
paper = (ROOT / "white-paper.md").read_text()

formula_ids = {item["id"] for item in registry["formulae"]}
source_ids = {item["id"] for item in sources["sources"]}
problems: list[str] = []

for formula in registry["formulae"]:
    for basis in formula.get("source_basis", []):
        if isinstance(basis, dict):
            source_id = basis.get("source_id")
            if source_id and source_id not in source_ids:
                problems.append(
                    f"{formula['id']} references unknown source {source_id}"
                )

wired = {
    formula_id
    for group in results["calculation_lineage"].values()
    for formula_id in group
}
unknown_wired = wired - formula_ids
if unknown_wired:
    problems.append(f"results reference unknown formula IDs: {unknown_wired}")

paper_ids = set(re.findall(r"\bF-(?:[A-Z]+-)+[0-9]{3}\b", paper))
unknown_paper = paper_ids - formula_ids
if unknown_paper:
    problems.append(f"paper references unknown formula IDs: {unknown_paper}")

missing_from_paper = wired - paper_ids
if missing_from_paper:
    problems.append(
        f"sample-basin formula IDs absent from paper: {missing_from_paper}"
    )

if problems:
    raise SystemExit("\n".join(problems))

print(
    f"PASS: {len(formula_ids)} registered formulae, "
    f"{len(source_ids)} registered sources, "
    f"{len(wired)} wired sample formulae, and "
    f"{len(paper_ids)} paper formula references resolve."
)
