#!/usr/bin/env python3
"""Build only the approved Project Management retrofit lessons for local release QA."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COURSE = ROOT / "apps/project-management"
CURRICULUM = COURSE / "curriculum"
SITE = COURSE / "dist/site"

ACADEMY_CSS = (ROOT / "core/components/academy.css").read_text(encoding="utf-8")
ACADEMY_JS = (ROOT / "core/components/academy.js").read_text(encoding="utf-8")
RETROFIT_CSS = (CURRICULUM / "project-retrofit.css").read_text(encoding="utf-8")
RETROFIT_JS = (CURRICULUM / "project-retrofit.js").read_text(encoding="utf-8")

ACADEMY_CSS = re.sub(r"</(style)", r"<\\/\1", ACADEMY_CSS, flags=re.I)
RETROFIT_CSS = re.sub(r"</(style)", r"<\\/\1", RETROFIT_CSS, flags=re.I)
ACADEMY_JS = re.sub(r"</(script)", r"<\\/\1", ACADEMY_JS, flags=re.I)
RETROFIT_JS = re.sub(r"</(script)", r"<\\/\1", RETROFIT_JS, flags=re.I)

TARGETS = {
    "module-10-quality-management.html": "lesson-pm-10-quality-management.html",
    "module-12-teams-stakeholders-communication.html": (
        "lesson-pm-12-teams-stakeholders-communication.html"
    ),
    "module-15-measurement-honest-status.html": "lesson-pm-15-measurement-honest-status.html",
    "module-17-safety-locates-commissioning.html": (
        "lesson-pm-17-safety-locates-commissioning.html"
    ),
}

NAVIGATION = {
    "masterclass-project-management.html": "course-project-management.html",
    **{
        f"module-{number:02d}-{slug}.html": f"lesson-pm-{number:02d}-{output_slug}.html"
        for number, slug, output_slug in (
            (1, "what-is-a-project", "what-is-a-project"),
            (2, "delivery-and-life-cycles", "delivery-life-cycles"),
            (3, "governance-integration-tailoring", "governance-integration-tailoring"),
            (4, "scope-and-requirements", "scope-and-requirements"),
            (5, "scheduling-critical-path", "scheduling-critical-path"),
            (6, "advanced-scheduling", "advanced-scheduling"),
            (7, "estimating-budgeting", "estimating-budgeting"),
            (8, "earned-value", "earned-value"),
            (9, "procurement-contracts-claims", "procurement-contracts-claims"),
            (10, "quality-management", "quality-management"),
            (11, "risk-uncertainty", "risk-uncertainty"),
            (12, "teams-stakeholders-communication", "teams-stakeholders-communication"),
            (13, "leadership-negotiation-ethics", "leadership-negotiation-ethics"),
            (14, "executing-controlling", "executing-controlling"),
            (15, "measurement-honest-status", "measurement-honest-status"),
            (16, "capital-lifecycle-regulatory", "capital-lifecycle-regulatory"),
            (17, "safety-locates-commissioning", "safety-locates-commissioning"),
            (18, "asset-management-digital-resilience", "asset-management-digital-resilience"),
            (19, "program-portfolio", "program-portfolio"),
            (20, "capstone-agentic-pm", "capstone-agentic-pm"),
            (21, "exam-prep", "exam-prep"),
        )
    },
}


def inline_assets(html: str) -> str:
    html = re.sub(
        r'<link rel="stylesheet" href="[^"]*academy\.css">',
        f"<style>\n{ACADEMY_CSS}\n</style>",
        html,
    )
    html = html.replace(
        '<link rel="stylesheet" href="project-retrofit.css">',
        f"<style>\n{RETROFIT_CSS}\n</style>",
    )
    html = re.sub(
        r'<script src="[^"]*academy\.js"></script>',
        f"<script>\n{ACADEMY_JS}\n</script>",
        html,
    )
    html = html.replace(
        '<script src="project-retrofit.js"></script>',
        f"<script>\n{RETROFIT_JS}\n</script>",
    )
    for source, output in NAVIGATION.items():
        html = html.replace(f'href="{source}"', f'href="{output}"')
    return html


def main() -> None:
    for source_name, output_name in TARGETS.items():
        html = inline_assets((CURRICULUM / source_name).read_text(encoding="utf-8"))
        if "—" in html or "–" in html:
            raise AssertionError(f"prohibited dash in {source_name}")
        if "project-retrofit.css" in html or "project-retrofit.js" in html:
            raise AssertionError(f"retrofit assets were not inlined in {source_name}")
        output = SITE / output_name
        output.write_text(html, encoding="utf-8")
        print(f"built {output.relative_to(ROOT)} ({output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
