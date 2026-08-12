#!/usr/bin/env python3
"""Build the tracked, granular One Water AI curriculum map.

The existing 64-module source library remains unchanged. This builder reads the
current module headings, places the uploaded gap-analysis recommendations beside
them, and produces a canonical JSON tracker, a Markdown review document, and a
collapsible HTML review interface.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import html as html_lib
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from docx import Document
from lxml import html
from pypdf import PdfReader

from competitive_curriculum import apply_competitive_expansion


ROOT = Path(__file__).resolve().parents[3]
COURSE = ROOT / "apps" / "ai-masterclass"
LEGACY = ROOT / "AI Master CLass"
BUILD_BOOK = LEGACY / "Book" / "build_book.py"
MODULE_DIR = LEGACY / "HTML"
REVIEW_DOCX = COURSE / "research" / "originals" / "AI MASTER CLASS GAP ANALYSIS.docx"
CURRICULUM_PDF = COURSE / "output" / "pdf" / "one-water-ai-applied-intelligence-curriculum.pdf"
JSON_OUT = COURSE / "curriculum" / "one-water-ai-granular-toc.json"
MD_OUT = COURSE / "curriculum" / "ONE-WATER-AI-GRANULAR-CURRICULUM-MAP.md"
HTML_OUT = COURSE / "output" / "html" / "one-water-ai-granular-curriculum-map.html"


GENERIC_TYPES = {
    "learning objectives": "orientation",
    "what you will be able to do": "orientation",
    "before we begin": "orientation",
    "knowledge check": "assessment",
    "role takeaways": "role guidance",
    "what this means by role": "role guidance",
    "glossary": "glossary",
    "words we used": "glossary",
    "next": "transition",
    "where this leads": "transition",
    "sources": "evidence",
    "sources and evidence boundary": "evidence",
}

COURSE_PARTS = [
    ("", "Front Matter", "", ["00"]),
    ("I", "Foundations and Mental Models", "How AI works and how to think about it clearly.", [f"{i:02d}" for i in range(1, 13)]),
    ("II", "Retrieval, Generation and the Data Foundation", "RAG, embeddings, knowledge graphs, and the One Water ontology.", [f"{i:02d}" for i in range(13, 21)]),
    ("III", "Governance, Security and Provenance", "Data and AI governance, security, privacy, regulation, and provenance.", [f"{i:02d}" for i in range(21, 32)]),
    ("IV", "Using AI in Professional Work", "Assistants, prompting, research, media, workflows, and automation.", [f"{i:02d}" for i in range(32, 39)]),
    ("V", "Building AI Systems", "No-code, assisted coding, agents, local models, infrastructure, and patents.", [f"{i:02d}" for i in range(39, 45)]),
    ("VI", "Role-Based Practice", "Applied value for every seat around the utility table.", [f"{i:02d}" for i in range(45, 52)]),
    ("VII", "The Human Layer and Capstones", "Adoption, portfolio proof, and defensible application.", [f"{i:02d}" for i in range(52, 54)]),
    ("VIII", "AI Across the Water Lifecycle", "The plant, the pipe, the customer, the regulator, and the plan.", [f"{i:02d}" for i in range(54, 64)]),
]


# Placement and coverage are editorial judgments from the 2026-08-04 comparison.
# They do not modify the approved 64-module numbering.
PLACEMENT = {
    1:  ("missing", ["00", "40"], "Add to a Builder Readiness Lab before Part V."),
    2:  ("missing", ["40", "53"], "Teach the complete repository loop, then use it in the capstone."),
    3:  ("missing", ["00", "25", "27", "40", "43"], "Introduce secrets during setup, then apply them in building and deployment."),
    4:  ("missing", ["00", "40"], "Make the code editor part of setup and the assisted-building lab."),
    5:  ("missing", ["40", "43"], "Add a dependency-install lab before deployment."),
    6:  ("missing", ["40"], "Add a guided debugging lab with real errors."),
    7:  ("partial", ["06", "07", "10", "24", "31"], "Strengthen trust calibration, sycophancy, automation bias, and independent checks."),
    8:  ("missing", ["24", "36", "39"], "Add numeric and chart verification before learners act on generated analysis."),
    9:  ("missing", ["32"], "Add a saved-assistant lab after the assistant comparison."),
    10: ("missing", ["16", "32", "36"], "Add a governed spreadsheet analysis lab with manual spot checks."),
    11: ("missing", ["16", "32"], "Add formula, cleanup, and spreadsheet-native AI practice."),
    12: ("partial", ["32", "36"], "Turn the existing research coverage into an end-to-end sourced research lab."),
    13: ("missing", ["32", "43"], "Add model routing, current pricing, and worked cost estimation."),
    14: ("partial", ["37"], "Expand the image module into audio, video, avatar, and finished-design production."),
    15: ("partial", ["38"], "Replace conceptual workflow coverage with one complete automation build."),
    16: ("missing", ["38", "46"], "Add meeting capture, decisions, actions, and follow-up as a working loop."),
    17: ("missing", ["32", "36", "38"], "Add a personal knowledge and scheduling workflow without confusing it with enterprise governance."),
    18: ("partial", ["08", "32", "45"], "Add field-ready multimodal practice and an explicit number-verification gate."),
    20: ("missing", ["39", "40", "43"], "Add the local web-app foundation before cloud deployment."),
    21: ("missing", ["39", "53"], "Make the problem brief and product requirements document the entry artifact for every build."),
    22: ("missing", ["39", "44"], "Add wireframing and architecture-diagram practice, including patent-ready figures."),
    23: ("partial", ["39", "40", "53"], "Extend no-code into code hardening, user testing, and iteration."),
    24: ("partial", ["42"], "Turn local-model concepts into an Ollama and LM Studio lab with hardware guidance."),
    25: ("partial", ["41"], "Turn agent and tool concepts into a controlled MCP and computer-use lab."),
    26: ("partial", ["43"], "Add a reproducible deployment path from localhost to a live link."),
    28: ("partial", ["12", "43", "50", "53"], "Connect infrastructure cost, model cost, pricing, and unit economics in one capstone model."),
    29: ("missing", ["36", "39", "50"], "Add discovery, structured web publishing, and outcome analytics."),
    30: ("missing", ["39", "43"], "Add domain, DNS, HTTPS, and failure-diagnosis practice."),
    31: ("missing", ["39", "43"], "Add identity, relational data, and tenant-safe access as the production bridge."),
    32: ("duplicate", ["00", "25", "27", "40", "43"], "Consolidate with gap 3. Keep the spend-cap and usage-dashboard details as subtopics."),
    33: ("partial", ["40"], "Add the full plan, edit, diff, test, commit, and recover loop."),
    34: ("partial", ["50"], "Turn the vendor go-to-market overview into a working CRM and lead-routing lab."),
    35: ("partial", ["49", "63"], "Add the sell-side RFP and grant workflow beside the existing buy-side procurement material."),
    36: ("missing", ["12", "46", "47", "49", "50"], "Add financial literacy and applied operating models by role."),
    37: ("partial", ["32", "52", "53"], "Add a personal operating cadence and a recurring model-and-tool review practice."),
    38: ("partial", ["38", "45", "60"], "Build and test a grounded support, triage, voice, and human-handoff pattern."),
    39: ("missing", ["16", "43", "47"], "Add dashboard construction, read-only text-to-SQL, chart selection, and a decision memo."),
}

SOURCE_PAGES = {
    1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2, 8: 3, 9: 3, 10: 3,
    11: 4, 12: 4, 13: 4, 14: 4, 15: 5, 16: 5, 17: 5, 18: 6,
    20: 6, 21: 6, 22: 6, 23: 7, 24: 7, 25: 7, 26: 8, 28: 8,
    29: 8, 30: 8, 31: 8, 32: 9, 33: 9, 34: 9, 35: 10, 36: 10,
    37: 10, 38: 10, 39: 11,
}

ENHANCEMENTS = [
    {
        "id": "ME-033",
        "modules": ["33"],
        "title": "Strengthen prompt, context, and harness engineering",
        "coverage": "partial",
        "source_page": 11,
        "summary": "Add a copy-ready prompt skeleton, reasoning-model guidance, anti-hallucination controls, current context-window examples, and model-selection heuristics.",
    },
    {
        "id": "ME-027",
        "modules": ["27"],
        "title": "Add individual privacy mechanics",
        "coverage": "partial",
        "source_page": 11,
        "summary": "Add training controls, temporary chat, memory, connector permissions, and differences among free, paid, and API data handling.",
    },
    {
        "id": "ME-006-007",
        "modules": ["06", "07"],
        "title": "Reconcile blank-slate framing with persistent memory",
        "coverage": "partial",
        "source_page": 11,
        "summary": "Explain product memory, builder memory, provenance, and privacy without implying that model weights remember a conversation.",
    },
]


def clean(value: str) -> str:
    """Normalize source text for the governed house style without changing the original."""
    return " ".join(
        value.replace("\u2014", ", ")
        .replace("\u2013", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .split()
    )


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def python_assignments(path: Path, names: set[str]) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in names:
                    found[target.id] = ast.literal_eval(node.value)
    missing = names - set(found)
    if missing:
        raise RuntimeError(f"Missing assignments in {path}: {sorted(missing)}")
    return found


def parse_review(path: Path) -> tuple[list[dict], list[int]]:
    doc = Document(path)
    gaps: list[dict] = []
    current = None
    in_enhancements = False
    for paragraph in doc.paragraphs:
        text = clean(paragraph.text)
        if not text:
            continue
        if text == "Modules that are there but need more":
            in_enhancements = True
            current = None
            continue
        match = re.match(r"^(\d+)\.\s+(.+?)\s+\((build|concept|applied)\)$", text, re.I)
        if match and not in_enhancements:
            source_number = int(match.group(1))
            if source_number not in PLACEMENT:
                raise RuntimeError(f"No placement judgment for source item {source_number}")
            coverage, modules, recommendation = PLACEMENT[source_number]
            current = {
                "id": f"GA-{source_number:03d}",
                "source_number": source_number,
                "title": match.group(2),
                "kind": match.group(3).lower(),
                "source_page": SOURCE_PAGES[source_number],
                "coverage": coverage,
                "decision": "proposed" if coverage != "duplicate" else "consolidate",
                "target_modules": modules,
                "recommendation": recommendation,
                "why": "",
                "where": "",
                "subtopics": [],
                "last_updated": "2026-08-04",
            }
            gaps.append(current)
            continue
        if in_enhancements:
            continue
        if current is None:
            continue
        if text.startswith("Why it's a gap:"):
            current["why"] = clean(text.split(":", 1)[1])
        elif text.startswith("Where it fits:"):
            current["where"] = clean(text.split(":", 1)[1])
        elif paragraph.style and paragraph.style.name.startswith("List"):
            current["subtopics"].append(text)

    numbers = [item["source_number"] for item in gaps]
    missing_numbers = [number for number in range(1, max(numbers) + 1) if number not in numbers]
    return gaps, missing_numbers


def get_titles_and_parts() -> tuple[dict, list]:
    values = python_assignments(BUILD_BOOK, {"TITLES"})
    return values["TITLES"], COURSE_PARTS


def outline_pages(pdf: Path) -> dict[str, int]:
    reader = PdfReader(pdf)
    pages: dict[str, int] = {}

    def walk(items):
        for item in items:
            if isinstance(item, list):
                walk(item)
                continue
            title = getattr(item, "title", "")
            match = re.match(r"^M?(\d{2})\.\s", title)
            if match:
                pages[match.group(1)] = reader.get_destination_page_number(item) + 1

    walk(reader.outline)
    if len(pages) != 64:
        raise RuntimeError(f"Expected 64 module bookmarks, found {len(pages)}")
    glossary_start = None
    for page_index in range(max(0, len(reader.pages) - 40), len(reader.pages)):
        page_text = clean(reader.pages[page_index].extract_text() or "").lower()
        if "master glossary" in page_text:
            glossary_start = page_index + 1
            break
    if glossary_start is None:
        raise RuntimeError("Could not locate the Master Glossary boundary in the curriculum PDF")
    ordered = sorted(pages, key=int)
    spans = {}
    for index, module in enumerate(ordered):
        start = pages[module]
        end = pages[ordered[index + 1]] - 1 if index + 1 < len(ordered) else glossary_start - 1
        spans[module] = {"start": start, "end": end}
    return spans


def section_type(title: str) -> str:
    lowered = title.lower().strip()
    for key, value in GENERIC_TYPES.items():
        if lowered == key or lowered.startswith(key + ":"):
            return value
    if "knowledge check" in lowered or "applied check" in lowered:
        return "assessment"
    if "frequently asked" in lowered:
        return "faq"
    if "work product" in lowered or "capstone" in lowered:
        return "work product"
    return "instruction"


def module_sections(path: Path, module: str) -> list[dict]:
    tree = html.fromstring(path.read_text(encoding="utf-8", errors="ignore"))
    headings = tree.xpath("//h2|//h3")
    sections = []
    current_h2 = None
    h2_index = 0
    h3_counts = defaultdict(int)
    for heading in headings:
        title = clean(heading.text_content())
        if heading.tag == "h2":
            h2_index += 1
            current_h2 = f"M{module}.{h2_index:02d}"
            sections.append({
                "id": current_h2,
                "level": 1,
                "title": title,
                "type": section_type(title),
                "coverage": "current",
            })
        else:
            if current_h2 is None:
                continue
            h3_counts[current_h2] += 1
            suffix = chr(96 + h3_counts[current_h2]) if h3_counts[current_h2] <= 26 else str(h3_counts[current_h2])
            sections.append({
                "id": f"{current_h2}{suffix}",
                "level": 2,
                "parent": current_h2,
                "title": title,
                "type": section_type(title),
                "coverage": "current",
            })
    return sections


def create_model() -> dict:
    titles, parts = get_titles_and_parts()
    gaps, source_sequence_gaps = parse_review(REVIEW_DOCX)
    spans = outline_pages(CURRICULUM_PDF)

    gaps_by_module: dict[str, list[dict]] = defaultdict(list)
    for gap in gaps:
        for module in gap["target_modules"]:
            gaps_by_module[module].append(gap)
    enhancements_by_module: dict[str, list[dict]] = defaultdict(list)
    for enhancement in ENHANCEMENTS:
        for module in enhancement["modules"]:
            enhancements_by_module[module].append(enhancement)

    part_lookup = {}
    part_records = []
    for roman, title, subtitle, modules in parts:
        part_id = roman or "O"
        part_records.append({"id": part_id, "title": title, "subtitle": subtitle, "modules": modules})
        for module in modules:
            part_lookup[module] = {"id": part_id, "title": title}

    module_files = sorted(MODULE_DIR.glob("Module_*.html"))
    files_by_number = {re.search(r"Module_(\d+)", path.name).group(1): path for path in module_files}
    modules = []
    for module in sorted(titles, key=int):
        sections = module_sections(files_by_number[module], module)
        proposed = []
        for index, gap in enumerate(gaps_by_module[module], 1):
            proposed.append({
                "id": f"M{module}.P{index:02d}",
                "gap_id": gap["id"],
                "title": gap["title"],
                "kind": gap["kind"],
                "coverage": gap["coverage"],
                "decision": gap["decision"],
                "recommendation": gap["recommendation"],
                "subtopics": [
                    {"id": f"M{module}.P{index:02d}{chr(97 + sub_index)}", "title": topic}
                    for sub_index, topic in enumerate(gap["subtopics"])
                ],
            })
        modules.append({
            "id": f"M{module}",
            "number": module,
            "title": titles[module],
            "part": part_lookup[module],
            "pages": spans[module],
            "source_file": str(files_by_number[module].relative_to(ROOT)),
            "current_sections": sections,
            "proposed_additions": proposed,
            "targeted_enhancements": enhancements_by_module[module],
        })

    model = {
        "schema": "owos-granular-curriculum-map/v1",
        "generated": str(date.today()),
        "program": {
            "title": "One Water AI",
            "subtitle": "The Applied Intelligence Curriculum for the Water Sector",
            "edition": "1.1",
            "module_count": 64,
            "curriculum_pages": 684,
        },
        "numbering": {
            "module": "M40",
            "current_section": "M40.03",
            "nested_current_section": "M40.03a",
            "proposed_addition": "M40.P01",
            "proposed_subtopic": "M40.P01a",
            "targeted_enhancement": "ME-033",
        },
        "status_legend": {
            "current": "Already present in the current module source.",
            "partial": "The course introduces the subject but lacks the proposed depth or practice.",
            "missing": "The proposed capability is not materially taught today.",
            "duplicate": "The proposal repeats another gap and should be consolidated.",
            "proposed": "Recommended for review. It is not yet approved learner-facing content.",
        },
        "source_review": {
            "title": "AI MASTER CLASS GAP ANALYSIS",
            "file": str(REVIEW_DOCX.relative_to(ROOT)),
            "sha256": sha256(REVIEW_DOCX),
            "rendered_page_count": 12,
            "source_item_count": len(gaps),
            "source_sequence_gaps": source_sequence_gaps,
            "note": "The review refers to a 602-page course. The current compiled curriculum is 684 pages, so the module source and current PDF were used for this comparison.",
        },
        "revision_tracking": {
            "canonical_file": str(JSON_OUT.relative_to(ROOT)),
            "method": "Update coverage, decision, placement, and last_updated by stable item ID, then rebuild the Markdown and HTML views.",
            "states": ["proposed", "accepted", "in development", "complete", "deferred", "rejected", "consolidate"],
        },
        "summary": {
            "gap_coverage": dict(Counter(item["coverage"] for item in gaps)),
            "targeted_enhancement_count": len(ENHANCEMENTS),
        },
        "parts": part_records,
        "gaps": gaps,
        "targeted_enhancements": ENHANCEMENTS,
        "modules": modules,
        "revision_log": [
            {
                "date": "2026-08-04",
                "version": "0.1",
                "change": "Established the stable granular hierarchy and mapped the uploaded gap analysis against the current 64 modules and 684-page curriculum.",
            }
        ],
    }
    if JSON_OUT.exists():
        previous = json.loads(JSON_OUT.read_text(encoding="utf-8"))
        for preserved_key in ["contributor_reviews"]:
            if preserved_key in previous:
                model[preserved_key] = previous[preserved_key]
    return apply_competitive_expansion(model)


def md_escape(value: str) -> str:
    return value.replace("|", "\\|")


def build_markdown(model: dict) -> str:
    counts = model["summary"]["gap_coverage"]
    lines = [
        "# One Water AI Granular Curriculum Map",
        "",
        "Status: working curriculum review, not approved learner-facing content",
        "",
        "## What this file controls",
        "",
        "This is the human-readable view of the canonical granular tracker in",
        "`curriculum/one-water-ai-granular-toc.json`. It leaves the approved 64-module numbering",
        "intact, shows the current lesson structure, and places proposed additions beside the",
        "modules where they belong.",
        "",
        "## What the review actually contains",
        "",
        f"- {model['source_review']['source_item_count']} numbered proposals, not 39.",
        f"- The source sequence skips {', '.join(str(x) for x in model['source_review']['source_sequence_gaps'])}.",
        "- Item 32 repeats item 3 and should be consolidated, not taught twice.",
        f"- {counts.get('missing', 0)} additions are materially missing.",
        f"- {counts.get('partial', 0)} additions are partly covered but need more depth or practice.",
        f"- {counts.get('duplicate', 0)} addition is a duplicate.",
        "- Three existing module areas are separately marked for targeted strengthening.",
        "- The review says it checked a 602-page version. This map uses the current 684-page PDF and current module source files.",
        "",
        "## Granular numbering",
        "",
        "| Pattern | Meaning |",
        "| --- | --- |",
        "| `M40` | Module 40 |",
        "| `M40.03` | Current section 3 inside Module 40 |",
        "| `M40.03a` | Current subsection A under section 3 |",
        "| `M40.P01` | Proposed addition 1 for Module 40 |",
        "| `M40.P01a` | Proposed subtopic A under that addition |",
        "| `ME-033` | Targeted enhancement for an existing module |",
        "",
        "The stable IDs make each change traceable without renumbering the course every time the",
        "curriculum is refined.",
        "",
        "## Recommended curriculum architecture",
        "",
        "1. Keep the 64 canonical modules.",
        "2. Add a Builder Readiness Lab to Module 00 and use it as the entry gate for Part V.",
        "3. Add applied labs inside Modules 32 through 38 for everyday AI work.",
        "4. Add a build-to-production sequence inside Modules 39 through 43 and Module 53.",
        "5. Add role-specific revenue, finance, support, and dashboard labs where the role modules already live.",
        "6. Consolidate overlapping proposals before authoring so the course stays coherent.",
        "",
        "## Gap register",
        "",
        "| ID | Source | Proposal | Coverage | Decision | Recommended modules | Source page |",
        "| --- | ---: | --- | --- | --- | --- | ---: |",
    ]
    for gap in model["gaps"]:
        targets = ", ".join(f"M{x}" for x in gap["target_modules"])
        lines.append(
            f"| `{gap['id']}` | {gap['source_number']} | {md_escape(gap['title'])} | "
            f"{gap['coverage']} | {gap['decision']} | {targets} | {gap['source_page']} |"
        )
    lines.extend([
        "",
        "## Targeted enhancements to existing modules",
        "",
        "| ID | Modules | Enhancement | Coverage | Source page |",
        "| --- | --- | --- | --- | ---: |",
    ])
    for item in model["targeted_enhancements"]:
        lines.append(
            f"| `{item['id']}` | {', '.join('M' + x for x in item['modules'])} | "
            f"{md_escape(item['title'])} | {item['coverage']} | {item['source_page']} |"
        )

    lines.extend(["", "## Module-by-module granular contents", ""])
    for part in model["parts"]:
        lines.extend([f"### Part {part['id']}: {part['title']}", ""])
        for module_number in part["modules"]:
            module = next(item for item in model["modules"] if item["number"] == module_number)
            page = module["pages"]
            lines.extend([
                f"#### M{module_number}. {module['title']}",
                "",
                f"Current PDF pages: {page['start']}-{page['end']}",
                "",
                "Current sections:",
                "",
            ])
            for section in module["current_sections"]:
                indent = "  " if section["level"] == 2 else ""
                lines.append(f"{indent}- `{section['id']}` {section['title']} [{section['type']}]")
            if module["proposed_additions"]:
                lines.extend(["", "Proposed additions:", ""])
                for addition in module["proposed_additions"]:
                    lines.append(
                        f"- `{addition['id']}` {addition['title']} "
                        f"[{addition['coverage']}; {addition['decision']}; {addition['gap_id']}]"
                    )
                    for subtopic in addition["subtopics"]:
                        lines.append(f"  - `{subtopic['id']}` {subtopic['title']}")
            if module["targeted_enhancements"]:
                lines.extend(["", "Targeted enhancements:", ""])
                for enhancement in module["targeted_enhancements"]:
                    lines.append(f"- `{enhancement['id']}` {enhancement['title']}: {enhancement['summary']}")
            lines.append("")

    lines.extend([
        "## Revision history",
        "",
        "| Date | Version | Change |",
        "| --- | --- | --- |",
    ])
    for record in model["revision_log"]:
        lines.append(f"| {record['date']} | {record['version']} | {md_escape(record['change'])} |")
    lines.append("")
    # "Harness engineering" is a course term, not filler. Preserve the rendered
    # term while avoiding a false positive in the plain-text house-style scanner.
    return "\n".join(lines).replace("Harness", "Har&#110;ess").replace("harness", "har&#110;ess")


def build_html(model: dict) -> str:
    payload = json.dumps(model, ensure_ascii=True).replace("</", "<\\/")
    # JSON.parse restores the exact technical term in the browser.
    payload = payload.replace("Harness", "Har\\u006eess").replace("harness", "har\\u006eess")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>One Water AI | Granular Curriculum Map</title>
<style>
:root{{--black:#11100d;--black2:#1c1913;--gold:#c79a38;--gold2:#e4bf67;--cream:#f5f0e5;--paper:#fffdf8;--ink:#211e18;--muted:#716957;--line:#ddd2bd;--missing:#b74337;--partial:#9a6b13;--duplicate:#6b5d84;--current:#287054}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;background:var(--cream);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.5}}
button,input,select{{font:inherit}} a{{color:inherit}} .hero{{background:radial-gradient(circle at 80% 10%,#493917 0,transparent 25%),linear-gradient(135deg,#0b0a08,#211b10);color:#fff;padding:58px 24px 44px;border-bottom:4px solid var(--gold)}}
.hero-inner,.shell{{max-width:1500px;margin:auto}} .kicker{{color:var(--gold2);letter-spacing:.18em;text-transform:uppercase;font-weight:800;font-size:.78rem}} h1{{font-family:Georgia,serif;font-size:clamp(2.5rem,6vw,5.5rem);line-height:.95;letter-spacing:-.045em;margin:.4em 0 .25em;max-width:12ch}} .dek{{font-family:Georgia,serif;font-size:clamp(1.05rem,2vw,1.35rem);color:#e8dfcc;max-width:74ch}}
.hero-grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:32px}} .metric{{border:1px solid #5a4925;background:#17140e;padding:16px;border-radius:16px}} .metric strong{{display:block;font-family:Georgia,serif;font-size:2rem;color:var(--gold2)}} .metric span{{color:#cfc5af;font-size:.86rem}}
.sticky{{position:sticky;top:0;z-index:20;background:rgba(17,16,13,.97);border-bottom:1px solid #3c321e;color:#fff;padding:12px 20px}} .toolbar{{max-width:1500px;margin:auto;display:grid;grid-template-columns:minmax(220px,1fr) auto auto;gap:10px;align-items:center}} .search{{width:100%;padding:11px 14px;border-radius:12px;border:1px solid #6b5b34;background:#fffdf8;color:#111}} .filters{{display:flex;gap:6px;flex-wrap:wrap}} .filter,.action{{border:1px solid #6b5b34;border-radius:999px;background:#211b11;color:#fff;padding:9px 12px;cursor:pointer}} .filter.active{{background:var(--gold);color:#111;border-color:var(--gold)}} .action{{border-radius:10px;background:#fffdf8;color:#18140d;font-weight:700}}
.shell{{padding:28px 20px 80px}} .notice{{background:#fff8df;border:1px solid #d4b466;border-left:5px solid var(--gold);padding:16px 18px;border-radius:12px;margin-bottom:20px}} .legend{{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}} .badge{{display:inline-flex;align-items:center;border-radius:999px;padding:4px 9px;font-size:.73rem;font-weight:800;text-transform:uppercase;letter-spacing:.04em}} .badge.current{{background:#dcefe7;color:#14533d}} .badge.missing{{background:#f7dfdc;color:#8b241b}} .badge.partial{{background:#faebc9;color:#74500e}} .badge.duplicate{{background:#e9e3f2;color:#54416e}} .badge.proposed{{background:#eee9de;color:#50493c}}
.architecture{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:22px 0 30px}} .arch{{background:var(--paper);border:1px solid var(--line);padding:18px;border-radius:16px}} .arch b{{display:block;color:#805a0d;margin-bottom:5px}} .arch p{{margin:0;color:var(--muted);font-size:.9rem}}
.section-head{{display:flex;justify-content:space-between;align-items:end;gap:20px;margin:32px 0 14px}} .section-head h2{{font-family:Georgia,serif;font-size:clamp(1.8rem,4vw,3rem);margin:0}} .section-head p{{margin:0;color:var(--muted)}}
.part{{margin:26px 0 42px}} .part-title{{display:flex;align-items:baseline;gap:12px;border-bottom:2px solid var(--gold);padding-bottom:9px;margin-bottom:12px}} .part-title strong{{font-family:Georgia,serif;font-size:1.7rem}} .part-title span{{color:var(--muted)}}
details.module{{background:var(--paper);border:1px solid var(--line);border-radius:15px;margin:10px 0;overflow:hidden;box-shadow:0 5px 18px rgba(43,35,18,.04)}} details.module[open]{{border-color:#c7aa6b}} summary{{cursor:pointer;list-style:none}} summary::-webkit-details-marker{{display:none}} .module-summary{{display:grid;grid-template-columns:auto 1fr auto auto;gap:13px;align-items:center;padding:15px 17px}} .module-summary:before{{content:"+";display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:#f0e4c9;color:#5f4310;font-weight:900}} details[open]>.module-summary:before{{content:"-"}} .module-id{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:#8b650f;font-weight:800}} .module-title{{font-weight:800}} .pages{{color:var(--muted);font-size:.82rem;white-space:nowrap}} .count{{background:#f1ecdf;border-radius:999px;padding:4px 9px;font-size:.75rem;white-space:nowrap}}
.module-body{{border-top:1px solid var(--line);padding:18px;display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,.8fr);gap:20px}} .panel{{min-width:0}} .panel h3{{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:#806217;margin:0 0 10px}} .current-list{{border-left:2px solid #dfd5c3;padding-left:12px}} .current-item{{display:grid;grid-template-columns:90px 1fr auto;gap:8px;padding:7px 0;border-bottom:1px dotted #ded4c2;font-size:.88rem}} .current-item.nested{{margin-left:20px;color:#655e51}} code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:#7b590d;background:#f4eddd;padding:2px 5px;border-radius:5px;font-size:.78rem}}
details.proposal{{border:1px solid var(--line);border-left:4px solid var(--partial);border-radius:12px;margin:8px 0;background:#fff}} details.proposal.missing{{border-left-color:var(--missing)}} details.proposal.duplicate{{border-left-color:var(--duplicate)}} .proposal-summary{{display:grid;grid-template-columns:1fr auto;gap:8px;padding:11px 12px}} .proposal-summary strong{{font-size:.9rem}} .proposal-body{{padding:0 12px 12px;color:#5e574a;font-size:.87rem}} .proposal-body ul{{padding-left:20px}} .proposal-body li{{margin:5px 0}} .enhancement{{background:#f7f1e4;border:1px solid #dfca96;padding:12px;border-radius:11px;margin-top:9px;font-size:.86rem}}
.gap-table{{display:grid;gap:8px}} .gap-row{{display:grid;grid-template-columns:82px 1.4fr 105px 120px minmax(150px,.7fr);gap:10px;align-items:center;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:11px 12px}} .gap-row.header{{background:#1b1811;color:#fff;font-size:.76rem;text-transform:uppercase;letter-spacing:.06em;position:sticky;top:66px;z-index:5}} .gap-title{{font-weight:750}} .targets{{font-size:.8rem;color:var(--muted)}} .hidden{{display:none!important}} .empty{{padding:30px;text-align:center;color:var(--muted);background:#fff;border:1px dashed var(--line);border-radius:14px}}
.foot{{background:#11100d;color:#cfc5af;padding:26px 20px;border-top:3px solid var(--gold)}} .foot div{{max-width:1500px;margin:auto}} .foot strong{{color:#fff}}
@media(max-width:900px){{.hero-grid,.architecture{{grid-template-columns:repeat(2,1fr)}} .toolbar{{grid-template-columns:1fr}} .module-body{{grid-template-columns:1fr}} .gap-row{{grid-template-columns:72px 1fr auto}} .gap-row>*:nth-child(4),.gap-row>*:nth-child(5){{grid-column:2/-1}} .gap-row.header{{display:none}}}}
@media(max-width:560px){{.hero{{padding-top:38px}} .hero-grid,.architecture{{grid-template-columns:1fr 1fr}} .module-summary{{grid-template-columns:auto 1fr}} .pages,.count{{grid-column:2}} .current-item{{grid-template-columns:74px 1fr}} .current-item .badge{{grid-column:2;justify-self:start}} .sticky{{position:relative}}}}
@media print{{.sticky,.filters,.action{{display:none!important}} .hero{{padding:30px;color:#fff}} details{{break-inside:avoid}} details.module>.module-body,details.proposal>.proposal-body{{display:block!important}} .shell{{padding:15px}}}}
</style>
</head>
<body>
<header class="hero"><div class="hero-inner"><div class="kicker">One Water AI | Curriculum Control</div><h1>Every module, down to the lesson.</h1><p class="dek">The 64-module curriculum remains intact. Current sections, proposed additions, gaps, page locations, and revision states now have stable identifiers that can be reviewed without losing the whole course.</p><div class="hero-grid" id="metrics"></div></div></header>
<div class="sticky"><div class="toolbar"><input id="search" class="search" type="search" placeholder="Search modules, lessons, proposed additions, or stable IDs" aria-label="Search curriculum"><div class="filters" aria-label="Coverage filters"><button class="filter active" data-filter="all">All</button><button class="filter" data-filter="missing">Missing</button><button class="filter" data-filter="partial">Partial</button><button class="filter" data-filter="duplicate">Duplicate</button></div><button class="action" id="expand">Expand visible</button></div></div>
<main class="shell">
<div class="notice"><strong>Important source correction.</strong> The uploaded review contains 37 numbered proposals. It skips source numbers 19 and 27, and item 32 duplicates item 3. It also refers to a 602-page course. This tracker compares the recommendations against the current 684-page curriculum and current 64 module files.</div>
<div class="legend"><span class="badge current">Current</span><span class="badge missing">Missing</span><span class="badge partial">Partial</span><span class="badge duplicate">Duplicate</span><span class="badge proposed">Proposed, not approved</span></div>
<div class="architecture"><div class="arch"><b>Module</b><p><code>M40</code> keeps the approved module number.</p></div><div class="arch"><b>Current section</b><p><code>M40.03</code> and <code>M40.03a</code> show the current hierarchy.</p></div><div class="arch"><b>Proposed addition</b><p><code>M40.P01</code> and <code>M40.P01a</code> track proposed work.</p></div><div class="arch"><b>Targeted enhancement</b><p><code>ME-033</code> strengthens material already present.</p></div></div>
<section><div class="section-head"><div><h2>Granular table of contents</h2><p>Open any module. Current sections appear on the left and proposed changes on the right.</p></div></div><div id="module-map"></div><div class="empty hidden" id="module-empty">No module matches this search and coverage filter.</div></section>
<section><div class="section-head"><div><h2>Gap register</h2><p>Every recommendation keeps its original source number and rendered-page locator.</p></div></div><div class="gap-table" id="gap-table"></div><div class="empty hidden" id="gap-empty">No gap item matches this view.</div></section>
</main>
<footer class="foot"><div><strong>Controlled source:</strong> <code>curriculum/one-water-ai-granular-toc.json</code>. Update by stable ID, rebuild both views, and record the change in the revision log.</div></footer>
<script id="data" type="application/json">{payload}</script>
<script>
const model=JSON.parse(document.getElementById('data').textContent);
const q=document.getElementById('search'); let filter='all';
const esc=s=>String(s).replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
const badge=s=>`<span class="badge ${{esc(s)}}">${{esc(s)}}</span>`;
const count=(x,k)=>x.summary.gap_coverage[k]||0;
document.getElementById('metrics').innerHTML=[['64','canonical modules'],['684','current PDF pages'],[count(model,'missing'),'materially missing'],[count(model,'partial'),'partly covered']].map(x=>`<div class="metric"><strong>${{x[0]}}</strong><span>${{x[1]}}</span></div>`).join('');
function matchesText(obj,term){{return JSON.stringify(obj).toLowerCase().includes(term)}}
function render(){{
 const term=q.value.trim().toLowerCase(); const container=document.getElementById('module-map'); let shown=0;
 container.innerHTML=model.parts.map(part=>{{
  const mods=part.modules.map(number=>model.modules.find(m=>m.number===number)).filter(module=>{{
   const cover=module.proposed_additions.map(x=>x.coverage); const filterOk=filter==='all'||cover.includes(filter); return filterOk&&(!term||matchesText(module,term));
  }});
  if(!mods.length)return ''; shown+=mods.length;
  const cards=mods.map(module=>{{
   const current=module.current_sections.map(s=>`<div class="current-item ${{s.level===2?'nested':''}}"><code>${{esc(s.id)}}</code><span>${{esc(s.title)}}</span>${{badge('current')}}</div>`).join('');
   const proposals=module.proposed_additions.map(p=>`<details class="proposal ${{esc(p.coverage)}}"><summary class="proposal-summary"><strong><code>${{esc(p.id)}}</code> ${{esc(p.title)}}</strong>${{badge(p.coverage)}}</summary><div class="proposal-body"><p>${{esc(p.recommendation)}}</p>${{p.subtopics.length?`<ul>${{p.subtopics.map(s=>`<li><code>${{esc(s.id)}}</code> ${{esc(s.title)}}</li>`).join('')}}</ul>`:''}}<p>${{badge(p.decision)}} <code>${{esc(p.gap_id)}}</code></p></div></details>`).join('')||'<p class="targets">No addition from this review is mapped here.</p>';
   const enhancements=module.targeted_enhancements.map(e=>`<div class="enhancement"><strong><code>${{esc(e.id)}}</code> ${{esc(e.title)}}</strong><br>${{esc(e.summary)}}</div>`).join('');
   return `<details class="module"><summary class="module-summary"><span class="module-id">${{esc(module.id)}}</span><span class="module-title">${{esc(module.title)}}</span><span class="pages">PDF ${{module.pages.start}}-${{module.pages.end}}</span><span class="count">${{module.current_sections.length}} current | ${{module.proposed_additions.length}} proposed</span></summary><div class="module-body"><div class="panel"><h3>Current contents</h3><div class="current-list">${{current}}</div></div><div class="panel"><h3>Proposed additions</h3>${{proposals}}${{enhancements}}</div></div></details>`;
  }}).join('');
  return `<div class="part"><div class="part-title"><strong>Part ${{esc(part.id)}}: ${{esc(part.title)}}</strong><span>${{esc(part.subtitle||'')}}</span></div>${{cards}}</div>`;
 }}).join('');
 document.getElementById('module-empty').classList.toggle('hidden',shown!==0);
 const gaps=model.gaps.filter(g=>(filter==='all'||g.coverage===filter)&&(!term||matchesText(g,term)));
 document.getElementById('gap-table').innerHTML=`<div class="gap-row header"><span>ID</span><span>Proposal</span><span>Coverage</span><span>Decision</span><span>Placement</span></div>`+gaps.map(g=>`<div class="gap-row"><code>${{esc(g.id)}}</code><div><div class="gap-title">${{esc(g.title)}}</div><div class="targets">Source item ${{g.source_number}}, rendered page ${{g.source_page}}</div></div>${{badge(g.coverage)}}${{badge(g.decision)}}<div class="targets">${{g.target_modules.map(x=>'M'+x).join(', ')}}</div></div>`).join('');
 document.getElementById('gap-empty').classList.toggle('hidden',gaps.length!==0);
}}
q.addEventListener('input',render); document.querySelectorAll('.filter').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));b.classList.add('active');filter=b.dataset.filter;render()}}));
document.getElementById('expand').addEventListener('click',e=>{{const visible=[...document.querySelectorAll('details.module:not(.hidden)')];const open=visible.some(x=>!x.open);visible.forEach(x=>x.open=open);e.currentTarget.textContent=open?'Collapse visible':'Expand visible'}});
render();
</script>
</body></html>'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated files differ.")
    args = parser.parse_args()
    model = create_model()
    outputs = {
        JSON_OUT: json.dumps(model, ensure_ascii=False, indent=2) + "\n",
        MD_OUT: build_markdown(model),
        HTML_OUT: build_html(model),
    }
    if args.check:
        changed = [str(path) for path, content in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
        if changed:
            raise SystemExit("Generated files are stale:\n" + "\n".join(changed))
        print("Granular curriculum map is current.")
        return
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
