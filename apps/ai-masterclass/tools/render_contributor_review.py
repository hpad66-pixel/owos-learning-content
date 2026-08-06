#!/usr/bin/env python3
"""Render a contributor curriculum review JSON as an auditable Markdown crosswalk."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "curriculum" / "shreya-technical-foundations-review.json"
EXTRACTION = ROOT / "research" / "extractions" / "INT-002-one-water-ai-technical-foundations.md"
MATRIX = ROOT / "research" / "INT-002-TECHNICAL-FOUNDATIONS-INTEGRATION-MATRIX.md"


def display_status(value: str) -> str:
    return {
        "already-done-exactly": "Already done exactly",
        "already-planned-exactly": "Already planned exactly",
        "partial-expand": "Partially covered, expand",
        "new-addition": "New addition",
    }[value]


def main() -> None:
    review = json.loads(SOURCE.read_text(encoding="utf-8"))
    contributor = review["contributor"]
    items = review["items"]
    EXTRACTION.parent.mkdir(parents=True, exist_ok=True)

    extraction = [
        "# INT-002: One Water AI Technical Foundations",
        "",
        f"- Contributor: {contributor['name']}",
        f"- Contributor role: {contributor['role']}",
        f"- Received: {review['received']}",
        f"- Preserved source: `{review['source_file']}`",
        f"- SHA-256: `{review['source_sha256']}`",
        "- Source length: 5 rendered pages",
        f"- Extracted topic count: {len(items)}",
        "- Source condition: visually inspected; clean, readable, and complete; no comments, footnotes, endnotes, or tables detected",
        "",
        "## Extraction boundary",
        "",
        "This inventory preserves Shreya's topic sequence and page locators. The original DOCX remains the authority for her complete wording and rationale. Curriculum placement and coverage decisions are maintained separately so source content is never silently overwritten.",
        "",
        "## Topic inventory",
        "",
        "| ID | Page | Topic |",
        "| --- | ---: | --- |",
    ]
    extraction.extend(f"| {item['id']} | {item['source_page']} | {item['title']} |" for item in items)
    extraction.extend([
        "",
        "## Evidence boundary",
        "",
        "This is expert curriculum input, not a factual authority for learner-facing technical claims. Named products and providers are examples that require current verification, licensing review, and non-endorsement framing before publication.",
        "",
    ])
    EXTRACTION.write_text("\n".join(extraction), encoding="utf-8")

    counts = review["summary"]
    matrix = [
        "# INT-002 Technical Foundations Integration Matrix",
        "",
        "## Decision summary",
        "",
        f"All {len(items)} topics supplied by {contributor['name']} have a stable ID, source page, primary curriculum home, coverage decision, matched curriculum IDs, and governed next action.",
        "",
        f"- Already done exactly in the current curriculum: {counts['already_done_exactly']}",
        f"- Already planned exactly in an existing proposal: {counts['already_planned_exactly']}",
        f"- Partially covered and marked for expansion: {counts['partial_expand']}",
        f"- New governed additions: {counts['new_addition']}",
        "",
        "Already planned does not mean already taught. New and expanded items remain proposals until evidence review and blueprint approval.",
        "",
        "## Item-by-item placement",
        "",
        "| ID | Shreya's topic | Decision | Primary home | Existing match | Integration action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        matches = ", ".join(item["matches"]) if item["matches"] else "None"
        action = item["action"].replace("|", "\\|")
        matrix.append(
            f"| {item['id']} | {item['title']} | {display_status(item['classification'])} | "
            f"{item['primary_module']} | {matches} | {action} |"
        )
    matrix.extend([
        "",
        "## Attribution and change control",
        "",
        "Shreya remains the source contributor on all 56 records. Where her topic duplicates existing curriculum, the original curriculum authorship is not reassigned; her contribution is recorded as independent reinforcement. Any later change must retain the stable STF ID, editor identity, timestamp, revision number, decision note, and source link.",
        "",
        "## Release boundary",
        "",
        review["authority"],
        "",
    ])
    MATRIX.write_text("\n".join(matrix), encoding="utf-8")
    print(f"Rendered {len(items)} contributor review items")


if __name__ == "__main__":
    main()
