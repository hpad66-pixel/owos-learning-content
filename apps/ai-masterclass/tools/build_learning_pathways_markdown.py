#!/usr/bin/env python3
"""Render the governed learning-pathway blueprint as readable Markdown."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "curriculum" / "learning-pathways.json"
OUTPUT = ROOT / "curriculum" / "LEARNING-PATHWAYS.md"


def main() -> None:
    record = json.loads(SOURCE.read_text(encoding="utf-8"))
    lines = [
        "# One Water AI Learning Pathways",
        "",
        record["model"]["headline"],
        "",
        record["model"]["description"],
        "",
        f"**Authority boundary:** {record['authority']}",
        "",
    ]
    for pathway in record["pathways"]:
        lines.extend([
            f"## {pathway['title']}",
            "",
            f"**{pathway['headline']}**",
            "",
            pathway["promise"],
            "",
            f"**Audience:** {pathway['audience']}",
            "",
            f"**Problem:** {pathway['problem']}",
            "",
            "### Demonstrated objectives",
            "",
        ])
        lines.extend(f"- {item}" for item in pathway["objectives"])
        lines.extend(["", "### Outcomes", ""])
        lines.extend(f"- {item}" for item in pathway["outcomes"])
        lines.extend(["", "### Portfolio evidence", ""])
        lines.extend(f"- {item}" for item in pathway["portfolioEvidence"])
        lines.extend(["", "### Water-sector examples", ""])
        lines.extend(f"- {item}" for item in pathway["examples"])
        lines.extend([
            "",
            f"**Analogy:** {pathway['analogy']}",
            "",
            f"**Call to action:** {pathway['primaryCta']}",
            "",
            f"**Source audience profiles:** {', '.join(pathway['sourceTrackIds'])}",
            "",
            f"**Module view:** {len(pathway['moduleIds'])} governed Fellowship modules",
            "",
        ])
    lines.extend(["## Common questions", ""])
    for item in record["commonQuestions"]:
        lines.extend([f"### {item['question']}", "", item["answer"], ""])
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)} with {len(record['pathways'])} pathways")


if __name__ == "__main__":
    main()
