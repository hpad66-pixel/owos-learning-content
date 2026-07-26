#!/usr/bin/env python3
"""Fail-closed checks for a clean public Concept Brief HTML candidate."""

from __future__ import annotations

import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class PublicBriefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_depth = 0
        self.ids: list[str] = []
        self.links: list[str] = []
        self.images: list[dict[str, str]] = []
        self.buttons: list[dict[str, str]] = []
        self.summaries = 0
        self.headings: Counter[str] = Counter()
        self.visible_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}
        if tag in {"script", "style"}:
            self.hidden_depth += 1
        if attributes.get("id"):
            self.ids.append(attributes["id"])
        if tag == "a":
            self.links.append(attributes.get("href", ""))
        if tag == "img":
            self.images.append(attributes)
        if tag == "button":
            self.buttons.append(attributes)
        if tag == "summary":
            self.summaries += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings[tag] += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth and data.strip():
            self.visible_parts.append(data.strip())


def fail(message: str) -> None:
    raise AssertionError(message)


if len(sys.argv) != 2:
    raise SystemExit("usage: test-concept-public-output.py <html>")

html_path = Path(sys.argv[1]).resolve()
html_text = html_path.read_text(encoding="utf-8")
parser = PublicBriefParser()
parser.feed(html_text)
visible_text = " ".join(parser.visible_parts)

required = (
    "OWOS CONCEPT BRIEF",
    "Chemistry changes the particle before physics can remove it",
    "The live jar",
    "Key terms explained",
    "Jar test protocol",
    "Sources and scope",
    "Where can I check the source material?",
    "From understanding to action",
    "What should I do next?",
    "Should I change dose or mixing based on this brief?",
    "IN 30 SECONDS",
    "What changed",
    "What to observe",
    "What not to assume",
    "COMMENT ON THIS BRIEF",
    "This brief explains the concept. Facility decisions still require your approved procedures and qualified judgment.",
)
for phrase in required:
    if phrase not in visible_text:
        fail(f"missing required public content: {phrase}")
if (
    "PUBLIC EDITION" not in visible_text
    and "GRAPHITE EDITION" not in visible_text
    and "FINAL FEDERAL EDITION" not in visible_text
    and "EDITION 1.0" not in visible_text
):
    fail("public page is missing its edition label")

for forbidden in (
    "Connected in the graph",
    "Connected in OWOS",
    "Perplexity",
    "What the research changed",
    "Evidence and research decisions",
    "Verification coverage:",
    "Pending material claims:",
    "source checked",
    "claim review pending",
    "Concept Brief Compiler",
    "Republic of Korea",
    "Japan",
    "How much of this working brief is actually verified?",
    "THE CONCEPT ENGINE PRINCIPLE",
    "Vendor placeholder",
    "Paid vendor placement",
):
    if forbidden in visible_text:
        fail(f"internal or out-of-scope language is visible: {forbidden}")

for unsafe_value in ("G 900", "G 546", "G 390", "0.26", "-15 mV", "-30 mV"):
    if unsafe_value in visible_text:
        fail(f"withheld numeric claim is visible: {unsafe_value}")

if "—" in visible_text or "–" in visible_text:
    fail("public copy contains an em dash or en dash")
if "undefined" in visible_text.lower() or "null" in visible_text.lower():
    fail("public copy contains an undefined or null placeholder")

duplicate_ids = [item for item, count in Counter(parser.ids).items() if count > 1]
if duplicate_ids:
    fail(f"duplicate HTML ids: {', '.join(duplicate_ids)}")
if parser.headings["h1"] != 1:
    fail("public page must contain exactly one h1")
if parser.headings["h2"] < 8:
    fail("public page is missing expected section headings")
if not parser.summaries:
    fail("public FAQ disclosure is missing")

for image in parser.images:
    if not image.get("src"):
        fail("image has no source")
    if not image.get("alt"):
        fail(f"image has no alternative text: {image.get('src')}")
    source = image["src"]
    if not source.startswith(("http://", "https://", "data:")):
        asset_path = (html_path.parent / source).resolve()
        if not asset_path.is_file():
            fail(f"local image asset does not resolve: {source}")

for button in parser.buttons:
    if button.get("type") not in {"button", "reset", "submit"}:
        fail("interactive button has an unsafe or missing type")
    if button.get("data-jar-control") and not button.get("aria-pressed"):
        fail("jar control is missing aria-pressed state")

if not parser.links or any(not href for href in parser.links):
    fail("public page contains an empty link")

allowed_source_hosts = {
    "www.ecfr.gov",
    "www.epa.gov",
    "nepis.epa.gov",
    "www.pnws-awwa.org",
    "apas.ai",
}
for href in parser.links:
    if href.startswith("#"):
        continue
    if href.startswith(("../", "./")):
        continue
    if href.startswith("/course-community.html"):
        continue
    if href.startswith("/directory"):
        continue
    host = urlparse(href).hostname
    if host not in allowed_source_hosts:
        fail(f"public source link is outside the approved United States list: {href}")

for required_markup in (
    'name="viewport"',
    'data-owos-theme="graphite"',
    "prefers-reduced-motion:reduce",
    ".table-wrap",
    'aria-live="polite"',
    "<noscript>",
    'class="jar-canvas"',
    'role="img"',
    'id="owos-concept-community"',
    'id="owos-concept-sop"',
    'id="copy-sop-outline"',
    'id="owos-commercial-placements"',
    "data-concept-testimonials",
    "data-testimonial-consent",
    "What worked for me",
    "Built and powered by APAS",
    "Vendors and sponsors do not select, approve, rank, suppress, or modify",
):
    if required_markup not in html_text:
        fail(f"missing accessibility or responsive markup: {required_markup}")

print(
    "Public Concept Brief QA passed: clean public language, unique ids, semantic structure, "
    "United States source links, safe qualitative controls, responsive metadata, reduced motion, "
    "live feedback, alternative text, and no-JavaScript meaning are present."
)
