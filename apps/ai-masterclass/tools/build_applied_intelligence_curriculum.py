#!/usr/bin/env python3
"""Build the inclusive One Water AI curriculum from the complete 64-module source library."""

from __future__ import annotations

import argparse
import ast
import base64
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from pypdf import PdfReader, PdfWriter


APP_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = APP_ROOT.parents[1]
LEGACY_ROOT = REPO_ROOT / "AI Master CLass"
LEGACY_HTML = LEGACY_ROOT / "HTML"
LEGACY_BOOK = LEGACY_ROOT / "Book"
LEGACY_GLOSSARY_PDF = LEGACY_BOOK / "book_glossary.pdf"
LEGACY_BUILD_BOOK = LEGACY_BOOK / "build_book.py"
SKILLS_ZIP = LEGACY_ROOT / "Prompt-Skills-Pack" / "APAS_Prompt_Skills_Starter_Pack.zip"

OUTPUT_HTML = APP_ROOT / "output" / "html" / "one-water-ai-applied-intelligence-curriculum.html"
OUTPUT_PDF = APP_ROOT / "output" / "pdf" / "one-water-ai-applied-intelligence-curriculum.pdf"
OUTPUT_MANIFEST = APP_ROOT / "output" / "applied-intelligence-curriculum-manifest.json"
GRANULAR_TOC = APP_ROOT / "curriculum" / "one-water-ai-granular-toc.json"
BUILDER = Path(__file__).resolve()

PROGRAM_NAME = "One Water AI"
PROGRAM_SUBTITLE = "The Applied Intelligence Curriculum for the Water Sector"
EXPECTED_MODULES = 64
CURRENT_EDITION = "2.1"

TRACKS = [
    ("Utility Operations and Practice", "Operators, maintainers, supervisors, and utility practitioners"),
    ("Engineering, Planning and Capital Delivery", "Engineers, planners, asset managers, and project teams"),
    ("Executive and Public Leadership", "Utility leaders, elected officials, boards, and government professionals"),
    ("Data, AI and Governance", "Data stewards, technologists, cybersecurity teams, and AI practitioners"),
    ("Consulting and Industry Innovation", "Consultants, vendors, solution providers, and industry partners"),
    ("Research and Academia", "Faculty, researchers, associations, and nonprofit collaborators"),
    ("Emerging Professionals and Students", "Students, interns, and early-career water professionals"),
]

PARTS = [
    ("", "Orientation", [0]),
    ("I", "Foundations and Mental Models", range(1, 13)),
    ("II", "Retrieval, Generation and the Data Foundation", range(13, 21)),
    ("III", "Governance, Security and Provenance", range(21, 32)),
    ("IV", "Using AI in Professional Work", range(32, 39)),
    ("V", "Building AI Systems", range(39, 45)),
    ("VI", "Role-Based Practice", range(45, 52)),
    ("VII", "Adoption and Applied Work", range(52, 54)),
    ("VIII", "AI Across the Water Lifecycle", range(54, 64)),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def chrome_binary() -> str:
    candidates = [
        os.environ.get("CHROME_BIN"),
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise RuntimeError("Chrome was not found. Set CHROME_BIN to a headless Chrome binary.")


def source_module_paths() -> list[Path]:
    paths = sorted(LEGACY_HTML.glob("Module_[0-9][0-9]_*.html"))
    numbers = [int(path.name.split("_", 2)[1]) for path in paths]
    if numbers != list(range(EXPECTED_MODULES)):
        raise RuntimeError("The source library must contain exactly Modules 00 through 63")
    return paths


def canonical_titles() -> dict[str, str]:
    tree = ast.parse(LEGACY_BUILD_BOOK.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "TITLES" for target in node.targets):
            titles = ast.literal_eval(node.value)
            if len(titles) == EXPECTED_MODULES:
                return titles
    raise RuntimeError("Could not read the canonical 64-module title map")


def granular_curriculum() -> dict[str, object]:
    if not GRANULAR_TOC.exists():
        raise RuntimeError("The granular curriculum tracker is missing")
    data = json.loads(GRANULAR_TOC.read_text(encoding="utf-8"))
    modules = data.get("modules", [])
    if len(modules) != EXPECTED_MODULES:
        raise RuntimeError("The granular curriculum tracker must contain exactly 64 modules")
    numbers = [module.get("number") for module in modules]
    if numbers != [f"{number:02d}" for number in range(EXPECTED_MODULES)]:
        raise RuntimeError("The granular curriculum tracker is not ordered from Module 00 through Module 63")
    return data


def granular_structure_sha256(data: dict[str, object] | None = None) -> str:
    """Hash the curriculum structure without creating a PDF page-span dependency cycle."""
    curriculum = data or granular_curriculum()
    structure = {
        "schema_version": curriculum.get("schema_version"),
        "modules": [
            {
                "number": module["number"],
                "title": module["title"],
                "current_sections": module.get("current_sections", []),
                "proposed_additions": module.get("proposed_additions", []),
                "targeted_enhancements": module.get("targeted_enhancements", []),
            }
            for module in curriculum["modules"]
        ],
    }
    payload = json.dumps(structure, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def anchor_id(section_id: str) -> str:
    return "owai-" + re.sub(r"[^a-z0-9]+", "-", section_id.lower()).strip("-")


def inject_granular_structure(source: str, module: dict[str, object]) -> str:
    """Add stable section numbers and clearly labeled planned additions to one module."""
    sections = module["current_sections"]
    heading_pattern = re.compile(r"<h([23])([^>]*)>(.*?)</h\1>", re.I | re.S)
    index = 0

    def number_heading(match: re.Match[str]) -> str:
        nonlocal index
        if index >= len(sections):
            raise RuntimeError(f"Module {module['number']} has more h2/h3 headings than its tracker")
        section = sections[index]
        expected = "2" if section["level"] == 1 else "3"
        if match.group(1) != expected:
            raise RuntimeError(
                f"Module {module['number']} heading order changed at {section['id']}: "
                f"expected h{expected}, found h{match.group(1)}"
            )
        attrs = match.group(2)
        if not re.search(r"\bid\s*=", attrs, re.I):
            attrs += f' id="{anchor_id(section["id"])}"'
        label = html.escape(section["id"])
        index += 1
        return (
            f'<h{match.group(1)}{attrs}><span class="owai-section-number">{label}</span>'
            f'{match.group(3)}</h{match.group(1)}>'
        )

    script_match = re.search(r"<script\b", source, re.I)
    if script_match:
        document_markup = source[:script_match.start()]
        script_markup = source[script_match.start():]
    else:
        document_markup = source
        script_markup = ""
    source = heading_pattern.sub(number_heading, document_markup) + script_markup
    if index != len(sections):
        raise RuntimeError(
            f"Module {module['number']} tracker has {len(sections)} sections but only {index} headings were found"
        )

    additions = module.get("proposed_additions", [])
    enhancements = module.get("targeted_enhancements", [])
    planned = ""
    if additions or enhancements:
        plan_anchor = anchor_id(f"M{module['number']}.PLAN")
        blocks = []
        for addition in additions:
            subtopics = "".join(
                f'<li id="{anchor_id(item["id"])}"><span class="owai-subtopic-number">{html.escape(item["id"])}</span>{html.escape(item["title"])}</li>'
                for item in addition["subtopics"]
            )
            blocks.append(
                f'<article class="owai-proposal {html.escape(addition["coverage"])}">'
                f'<h3 id="{anchor_id(addition["id"])}"><span class="owai-section-number">{html.escape(addition["id"])}</span>{html.escape(addition["title"])}</h3>'
                f'<div class="owai-proposal-meta"><span>{html.escape(addition["coverage"])}</span><span>{html.escape(addition["decision"])}</span><span>{html.escape(addition["gap_id"])}</span></div>'
                f'<p>{html.escape(addition["recommendation"])}</p>'
                f'{f"<ul>{subtopics}</ul>" if subtopics else ""}'
                '</article>'
            )
        for enhancement in enhancements:
            blocks.append(
                '<article class="owai-proposal partial">'
                f'<h3 id="{anchor_id(enhancement["id"])}"><span class="owai-section-number">{html.escape(enhancement["id"])}</span>{html.escape(enhancement["title"])}</h3>'
                f'<div class="owai-proposal-meta"><span>targeted enhancement</span><span>{html.escape(enhancement["coverage"])}</span></div>'
                f'<p>{html.escape(enhancement["summary"])}</p>'
                '</article>'
            )
        planned = (
            '<section class="owai-planned-expansion">'
            '<div class="owai-planned-kicker">Curriculum expansion register</div>'
            f'<h2 id="{plan_anchor}">Current and proposed additions for Module {html.escape(module["number"])}</h2>'
            '<p class="owai-planned-note">The status badge on each entry governs its curriculum decision. Accepted means an approved curriculum blueprint, not finished instruction. Every entry still requires research, authoring, review, accessibility, packaging, and release approval before learner delivery.</p>'
            + "".join(blocks)
            + '</section>'
        )

    style = """
<style id="owai-granular-structure">
.owai-section-number{display:block;margin:0 0 5px;color:#9a6b19;font:800 10px/1.2 'Courier New',monospace;letter-spacing:.08em;text-transform:uppercase;scroll-margin-top:18px}
.owai-planned-expansion{margin:30px 0 0;padding:24px;border:2px solid #c6922f;border-radius:12px;background:#fff8e8;break-inside:avoid}
.owai-planned-kicker{color:#865a0d;font:800 10px/1.2 'Courier New',monospace;letter-spacing:.12em;text-transform:uppercase}
.owai-planned-expansion>h2{margin-top:7px}.owai-planned-note{padding:12px 14px;border-left:4px solid #c6922f;background:#fffdf7;color:#5d5344}
.owai-proposal{margin-top:15px;padding:15px 17px;border:1px solid #d9c89f;border-left:5px solid #a87416;border-radius:8px;background:#fffdf8;break-inside:avoid}
.owai-proposal.missing{border-left-color:#a93a30}.owai-proposal.duplicate{border-left-color:#66547c}.owai-proposal h3{margin:0 0 8px}.owai-proposal-meta{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.owai-proposal-meta span{padding:3px 7px;border-radius:999px;background:#eee5d2;color:#5f5443;font:700 9px/1.2 Arial,sans-serif;text-transform:uppercase;letter-spacing:.04em}
.owai-proposal ul{margin-bottom:0}.owai-subtopic-number{display:inline-block;min-width:82px;color:#865a0d;font:700 10px/1.4 'Courier New',monospace}
@media(max-width:700px){.owai-planned-expansion{padding:17px}.owai-subtopic-number{display:block;min-width:0;margin-bottom:2px}}
</style>
"""
    source = source.replace("</head>", style + "</head>")
    if planned:
        source = source.replace("</body>", planned + "</body>")
    return source


def module_navigation(module: dict[str, object]) -> list[dict[str, object]]:
    navigation = [
        {
            "id": section["id"],
            "title": section["title"],
            "anchor": anchor_id(section["id"]),
            "kind": "current",
            "level": section["level"],
        }
        for section in module["current_sections"]
    ]
    for addition in module.get("proposed_additions", []):
        navigation.append({
            "id": addition["id"],
            "title": addition["title"],
            "anchor": anchor_id(addition["id"]),
            "kind": "planned",
            "level": 1,
        })
        navigation.extend({
            "id": subtopic["id"],
            "title": subtopic["title"],
            "anchor": anchor_id(subtopic["id"]),
            "kind": "planned subtopic",
            "level": 2,
        } for subtopic in addition["subtopics"])
    navigation.extend({
        "id": enhancement["id"],
        "title": enhancement["title"],
        "anchor": anchor_id(enhancement["id"]),
        "kind": "enhancement",
        "level": 1,
    } for enhancement in module.get("targeted_enhancements", []))
    return navigation


def replace_identity(source: str) -> str:
    replacements = [
        ("The One Water AI Master Class", PROGRAM_NAME),
        ("One Water AI Master Class", PROGRAM_NAME),
        ("One Water AI Executive Fellowship", PROGRAM_NAME),
        ("one-water-ai-master-class", "one-water-ai"),
    ]
    for old, new in replacements:
        source = source.replace(old, new)
    return source


def embed_skills_download(source: str) -> str:
    if not SKILLS_ZIP.exists():
        return source
    payload = base64.b64encode(SKILLS_ZIP.read_bytes()).decode("ascii")
    uri = f"data:application/zip;base64,{payload}"
    return source.replace('../Prompt-Skills-Pack/APAS_Prompt_Skills_Starter_Pack.zip', uri)


def cover_document() -> str:
    track_cards = "".join(
        f'<div class="track"><strong>{html.escape(name)}</strong><span>{html.escape(audience)}</span></div>'
        for name, audience in TRACKS
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{PROGRAM_NAME} | {PROGRAM_SUBTITLE}</title>
<style>
  @page {{ size: letter; margin: 0; }}
  * {{ box-sizing:border-box; }}
  html,body {{ margin:0; width:100%; min-height:100%; font-family:Arial,Helvetica,sans-serif; background:#191917; color:#f7f2e8; }}
  .cover {{ position:relative; width:8.5in; height:11in; margin:0 auto; overflow:hidden; padding:.68in .72in .55in; background:#191917; display:flex; flex-direction:column; }}
  .cover:before {{ content:""; position:absolute; width:5.35in; height:5.35in; border-radius:50%; right:-2.75in; top:-2.45in; border:1px solid rgba(218,167,64,.60); box-shadow:0 0 0 .55in rgba(218,167,64,.08),0 0 0 1.12in rgba(218,167,64,.045); }}
  .cover:after {{ content:""; position:absolute; width:1.5in; height:3px; left:.72in; top:2.05in; background:#d7a43e; }}
  .topline {{ position:relative; z-index:1; display:flex; align-items:center; gap:12px; color:#d7a43e; font:800 9px/1.2 'Courier New',monospace; letter-spacing:.16em; text-transform:uppercase; }}
  .mark {{ width:38px; height:38px; border:1px solid #d7a43e; border-radius:50%; display:grid; place-items:center; color:#d7a43e; background:transparent; letter-spacing:0; font-size:11px; }}
  .title-block {{ position:relative; z-index:1; margin-top:.78in; max-width:6.55in; }}
  .title-block h1 {{ margin:0; color:#fffdf7; font-size:58px; line-height:.90; letter-spacing:-.055em; font-weight:800; }}
  .title-block h2 {{ margin:22px 0 0; max-width:6.2in; color:#d7a43e; font-family:Georgia,'Times New Roman',serif; font-size:24px; line-height:1.22; font-weight:400; font-style:italic; }}
  .descriptor {{ margin:17px 0 0; max-width:6.15in; color:#d2cdc3; font-size:13.4px; line-height:1.48; }}
  .rule {{ width:1.05in; height:4px; margin:22px 0 18px; background:#d7a43e; }}
  .shared {{ color:#f7f2e8; font:800 11px/1.3 'Courier New',monospace; letter-spacing:.08em; text-transform:uppercase; }}
  .tracks {{ display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:10px; }}
  .track {{ min-height:.59in; padding:10px 12px; border:1px solid rgba(215,164,62,.44); border-radius:5px; background:rgba(255,255,255,.035); }}
  .track strong {{ display:block; color:#fffdf7; font-size:10.7px; line-height:1.15; }}
  .track span {{ display:block; margin-top:4px; color:#bdb6aa; font-size:8.2px; line-height:1.25; }}
  .track:last-child {{ grid-column:1 / -1; width:50%; justify-self:center; }}
  .footer {{ margin-top:auto; display:grid; grid-template-columns:1fr auto; align-items:end; gap:20px; border-top:1px solid rgba(215,164,62,.45); padding-top:14px; }}
  .author strong {{ display:block; color:#fffdf7; font-size:14px; }}
  .author span,.edition {{ color:#a9a297; font-size:9.5px; line-height:1.45; }}
  .edition {{ text-align:right; }}
  @media(max-width:700px) {{
    .cover {{ width:100%; height:auto; min-height:100vh; padding:28px 22px; }}
    .title-block {{ margin-top:56px; }}
    .title-block h1 {{ font-size:50px; }}
    .tracks {{ grid-template-columns:1fr; }}
    .track:last-child {{ grid-column:auto; width:auto; }}
    .footer {{ margin-top:32px; }}
  }}
</style>
</head>
<body>
<main class="cover">
  <div class="topline"><span class="mark">OW</span><span>One Water Operating System · Powered by APAS.AI</span></div>
  <section class="title-block">
    <h1>{PROGRAM_NAME}</h1>
    <h2>{PROGRAM_SUBTITLE}</h2>
    <p class="descriptor">Data, knowledge, artificial intelligence, agents, governance, and practical application across water, wastewater, stormwater, and reuse.</p>
    <div class="rule"></div>
    <div class="shared">One shared foundation · Seven role-based tracks · 64 modules</div>
    <div class="tracks">{track_cards}</div>
  </section>
  <footer class="footer">
    <div class="author"><strong>Hardeep Anand, PE</strong><span>Founder and CEO, APAS.AI</span></div>
    <div class="edition">Complete granular curriculum<br>Edition {CURRENT_EDITION} · 2026</div>
  </footer>
</main>
</body>
</html>"""


def render_html(chrome: str, source: Path, destination: Path) -> None:
    destination.unlink(missing_ok=True)
    command = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={destination}",
        source.resolve().as_uri(),
    ]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not destination.exists() or destination.stat().st_size == 0:
        raise RuntimeError(f"Chrome did not create {destination}")


def section_local_pages(module_pdf: Path, module: dict[str, object]) -> dict[str, int]:
    reader = PdfReader(module_pdf)
    page_text = [" ".join((page.extract_text() or "").split()).upper() for page in reader.pages]
    compact_page_text = [re.sub(r"[^A-Z0-9]+", "", text) for text in page_text]
    records = [(section["id"], section["title"]) for section in module["current_sections"]]
    for addition in module.get("proposed_additions", []):
        records.append((addition["id"], addition["title"]))
        records.extend((item["id"], item["title"]) for item in addition["subtopics"])
    records.extend((item["id"], item["title"]) for item in module.get("targeted_enhancements", []))
    pages = {}
    for identifier, title in records:
        needle = identifier.upper()
        compact_needle = re.sub(r"[^A-Z0-9]+", "", needle)
        for page_index, (text, compact_text) in enumerate(zip(page_text, compact_page_text)):
            if needle in text or compact_needle in compact_text:
                pages[identifier] = page_index + 1
                break
        if identifier not in pages:
            title_needle = re.sub(r"[^A-Z0-9]+", "", title.upper())
            for page_index, compact_text in enumerate(compact_page_text):
                if title_needle and title_needle in compact_text:
                    pages[identifier] = page_index + 1
                    break
        if identifier not in pages:
            raise RuntimeError(f"Could not locate {identifier} in the rendered PDF for Module {module['number']}")
    return pages


def toc_document(
    titles: dict[str, str],
    module_pages: dict[int, int],
    toc_pages: int,
    modules: list[dict[str, object]],
    local_pages: dict[int, dict[str, int]],
) -> str:
    current_page = 1 + toc_pages + 1
    start_pages: dict[int, int] = {}
    for number in range(EXPECTED_MODULES):
        start_pages[number] = current_page
        current_page += module_pages[number]
    rows: list[str] = []
    for roman, part_title, numbers in PARTS:
        label = f"Part {roman}" if roman else "Start here"
        rows.append(f'<div class="part"><span>{label}</span><strong>{html.escape(part_title)}</strong></div>')
        for number in numbers:
            key = f"{number:02d}"
            module = modules[number]
            rows.append(
                f'<div class="row module-row"><span class="number">M{key}</span><span class="title">{html.escape(titles[key])}</span><span class="dots"></span><span class="page">{start_pages[number]}</span></div>'
            )
            for section in module["current_sections"]:
                page = start_pages[number] + local_pages[number][section["id"]] - 1
                nested = " nested" if section["level"] == 2 else ""
                rows.append(
                    f'<div class="row section-row{nested}"><span class="number">{html.escape(section["id"])}</span><span class="title">{html.escape(section["title"])}</span><span class="dots"></span><span class="page">{page}</span></div>'
                )
            for addition in module.get("proposed_additions", []):
                page = start_pages[number] + local_pages[number][addition["id"]] - 1
                rows.append(
                    f'<div class="row proposed-row"><span class="number">{html.escape(addition["id"])}</span><span class="title"><b>Planned:</b> {html.escape(addition["title"])}</span><span class="dots"></span><span class="page">{page}</span></div>'
                )
                for subtopic in addition["subtopics"]:
                    sub_page = start_pages[number] + local_pages[number][subtopic["id"]] - 1
                    rows.append(
                        f'<div class="row subtopic-row"><span class="number">{html.escape(subtopic["id"])}</span><span class="title">{html.escape(subtopic["title"])}</span><span class="dots"></span><span class="page">{sub_page}</span></div>'
                    )
            for enhancement in module.get("targeted_enhancements", []):
                page = start_pages[number] + local_pages[number][enhancement["id"]] - 1
                rows.append(
                    f'<div class="row proposed-row"><span class="number">{html.escape(enhancement["id"])}</span><span class="title"><b>Strengthen:</b> {html.escape(enhancement["title"])}</span><span class="dots"></span><span class="page">{page}</span></div>'
                )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{PROGRAM_NAME} | Contents</title>
<style>
@page{{size:letter;margin:.44in .55in}}*{{box-sizing:border-box}}body{{margin:0;color:#26221d;background:#f8f5ee;font-family:Georgia,'Times New Roman',serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.header{{margin:0 0 12px;padding-bottom:9px;border-bottom:3px solid #c6922f}}.kicker{{color:#aa771d;font:800 8px/1.2 'Courier New',monospace;letter-spacing:.15em;text-transform:uppercase}}h1{{margin:4px 0 0;font-size:27px;line-height:1;color:#1e1c19}}.explain{{margin:6px 0 0;color:#6d655b;font:9px/1.35 Arial,sans-serif}}
.part{{display:flex;align-items:baseline;gap:9px;margin-top:11px;padding:7px 0 3px;border-top:2px solid #c6922f;break-after:avoid}}.part span{{color:#aa771d;font:800 8px/1.2 'Courier New',monospace;text-transform:uppercase;letter-spacing:.12em}}.part strong{{font-size:12px;color:#1e1c19}}
.row{{display:flex;align-items:baseline;gap:6px;padding:1.35px 0;font-size:7.6px;line-height:1.15;break-inside:avoid}}.number{{width:58px;flex:0 0 58px;color:#8a6218;font-family:'Courier New',monospace;font-weight:700}}.title{{max-width:5.5in}}.dots{{flex:1;border-bottom:1px dotted #c5baaa;transform:translateY(-2px)}}.page{{color:#6d655b;font-variant-numeric:tabular-nums}}.module-row{{margin-top:4px;padding:4px 0 2px;border-top:1px solid #ded5c7;font-size:9px;font-weight:700}}.module-row .number{{color:#1e1c19}}.section-row{{padding-left:10px}}.section-row.nested{{padding-left:25px;color:#615a50}}.proposed-row{{margin-top:2px;padding:2px 4px 2px 10px;background:#fff1cc;border-left:3px solid #b78020}}.proposed-row b{{color:#865a0d}}.subtopic-row{{padding-left:25px;color:#6b604f;font-size:7px}}.subtopic-row .number{{width:68px;flex-basis:68px}}
</style></head><body><header class="header"><div class="kicker">{PROGRAM_NAME} · Edition {CURRENT_EDITION}</div><h1>Complete Granular Curriculum Contents</h1><p class="explain">Current numbered sections show what each module teaches today. Gold entries show planned additions and targeted strengthening that remain under curriculum review.</p></header>{''.join(rows)}</body></html>"""


def interactive_reader(cover: str, module_records: list[dict[str, str]]) -> str:
    cover_payload = json.dumps(cover, ensure_ascii=True).replace("</", "<\\/")
    module_payload = json.dumps(module_records, ensure_ascii=True).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{PROGRAM_NAME} | {PROGRAM_SUBTITLE}</title>
<style>
:root{{--black:#191917;--black2:#25231f;--paper:#f8f5ee;--white:#fffdf7;--ink:#26221d;--muted:#71695e;--line:#d9d1c4;--gold:#d7a43e;--gold2:#f0cf83}}*{{box-sizing:border-box}}html,body{{height:100%;margin:0}}body{{font-family:Arial,Helvetica,sans-serif;background:var(--paper);color:var(--ink);overflow:hidden}}button,input,a{{font:inherit}}
.app{{display:grid;grid-template-rows:auto 1fr;height:100%}}.topbar{{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:16px;padding:11px 16px;background:var(--black);color:var(--white);border-bottom:3px solid var(--gold)}}.brand{{display:flex;gap:10px;align-items:center;min-width:0}}.mark{{display:grid;place-items:center;width:34px;height:34px;border:1px solid var(--gold);border-radius:50%;background:transparent;color:var(--gold);font-size:10px;font-weight:800}}.brand-copy{{min-width:0}}.brand-copy span{{display:block;color:var(--gold);font:800 8px/1.2 'Courier New',monospace;letter-spacing:.13em;text-transform:uppercase}}.brand-copy strong{{display:block;margin-top:2px;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.current{{min-width:0;text-align:center}}.current strong{{display:block;font-family:Georgia,'Times New Roman',serif;font-size:13px;font-weight:400;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.current span{{display:block;margin-top:3px;color:#bdb6aa;font-size:9px;font-family:'Courier New',monospace;letter-spacing:.07em}}.actions{{display:flex;gap:7px}}.button{{border:1px solid rgba(215,164,62,.48);border-radius:5px;background:transparent;color:var(--white);padding:8px 10px;cursor:pointer;text-decoration:none}}.button.primary{{background:var(--gold);border-color:var(--gold);color:var(--black);font-weight:800}}.button:hover,.button:focus-visible{{outline:2px solid var(--gold2);outline-offset:2px}}
.workspace{{display:grid;grid-template-columns:420px minmax(0,1fr);min-height:0}}.sidebar{{display:grid;grid-template-rows:auto 1fr;min-height:0;background:var(--paper);border-right:1px solid var(--line)}}.search-wrap{{padding:14px;border-bottom:1px solid var(--line)}}.search-wrap label{{display:block;margin-bottom:6px;color:#9a6b19;font:800 9px/1.2 'Courier New',monospace;text-transform:uppercase;letter-spacing:.11em}}.search{{width:100%;padding:10px;border:1px solid var(--line);border-radius:5px;background:#fffdf8;color:var(--ink)}}.list{{overflow:auto;padding:8px}}.front-link,.open-module,.section-link{{display:grid;grid-template-columns:76px 1fr;gap:9px;width:100%;border:0;border-radius:5px;padding:8px 10px;text-align:left;background:transparent;color:var(--ink);cursor:pointer}}.front-link:hover,.open-module:hover,.section-link:hover{{background:#eee7da}}.front-link[aria-current="page"],.open-module[aria-current="page"]{{background:var(--black);color:var(--white)}}.toc-module{{margin:5px 0;border:1px solid var(--line);border-radius:7px;background:#fffdf8;overflow:hidden}}.toc-module>summary{{display:grid;grid-template-columns:48px 1fr auto;gap:8px;align-items:start;padding:10px;cursor:pointer;list-style:none}}.toc-module>summary::-webkit-details-marker{{display:none}}.toc-module>summary:after{{content:'+';display:grid;place-items:center;width:20px;height:20px;border-radius:50%;background:#eee3cc;color:#7d5710;font-weight:800}}.toc-module[open]>summary:after{{content:'-'}}.toc-module[open]>summary{{border-bottom:1px solid var(--line);background:#f3ecdf}}.toc-children{{padding:6px}}.open-module{{font-weight:800;border-bottom:1px solid #eee5d7;margin-bottom:4px}}.section-link{{grid-template-columns:86px 1fr;padding:6px 8px;font-size:11px;line-height:1.28}}.section-link.nested{{padding-left:22px;color:#665e52}}.section-link.proposed{{margin-top:3px;background:#fff3d6;border-left:3px solid #b9821f}}.section-link.subtopic{{padding-left:28px;color:#665d4f}}.num{{color:#9a6b19;font:700 10px/1.45 'Courier New',monospace}}[aria-current="page"] .num{{color:var(--gold)}}.label{{font-family:Georgia,'Times New Roman',serif;font-size:12.5px;line-height:1.32}}.toc-module>summary .label{{font-weight:700}}.toc-kind{{display:block;margin-top:2px;color:#8a8174;font:700 8px/1.2 Arial,sans-serif;text-transform:uppercase;letter-spacing:.05em}}.reader{{position:relative;min-width:0;min-height:0;background:#ded8ce}}.reader iframe{{display:block;width:100%;height:100%;border:0;background:#fffdf8}}.progress{{position:absolute;bottom:0;left:0;right:0;height:3px;background:rgba(25,25,23,.18)}}.progress span{{display:block;height:100%;width:0;background:var(--gold)}}.menu{{display:none}}
@media(max-width:850px){{.topbar{{grid-template-columns:auto minmax(0,1fr) auto;padding:9px;gap:8px}}.brand-copy span,.current span{{display:none}}.brand-copy strong{{font-size:11px}}.current strong{{font-size:10px}}.workspace{{grid-template-columns:1fr}}.sidebar{{position:fixed;z-index:30;top:55px;bottom:0;left:0;width:min(90vw,360px);transform:translateX(-105%);transition:transform .2s ease;box-shadow:12px 0 34px rgba(0,0,0,.2)}}body.nav-open .sidebar{{transform:translateX(0)}}.menu{{display:inline-block}}.actions .desktop{{display:none}}}}
@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important;transition:none!important}}}}
</style></head><body><div class="app"><header class="topbar"><div class="brand"><span class="mark">OW</span><div class="brand-copy"><span>One Water Operating System</span><strong>{PROGRAM_NAME}</strong></div></div><div class="current"><strong id="current-title">{PROGRAM_SUBTITLE}</strong><span id="current-number">ONE FOUNDATION · SEVEN TRACKS · 64 MODULES</span></div><div class="actions"><button class="button menu" id="menu" type="button" aria-controls="sidebar" aria-expanded="false">Contents</button><button class="button" id="previous" type="button">Previous</button><button class="button" id="next" type="button">Next</button><a class="button primary desktop" href="../pdf/{OUTPUT_PDF.name}">Download PDF</a></div></header><div class="workspace"><aside class="sidebar" id="sidebar"><div class="search-wrap"><label for="search">Find any module, section, or planned addition</label><input class="search" id="search" type="search" placeholder="Search the complete granular contents"></div><nav class="list" id="list"></nav></aside><main class="reader"><iframe id="frame" title="{PROGRAM_NAME} curriculum"></iframe><div class="progress"><span id="progress"></span></div></main></div></div>
<script>
const cover={cover_payload};const modules={module_payload};const list=document.getElementById('list');const frame=document.getElementById('frame');const title=document.getElementById('current-title');const number=document.getElementById('current-number');const progress=document.getElementById('progress');const search=document.getElementById('search');const previous=document.getElementById('previous');const next=document.getElementById('next');const menu=document.getElementById('menu');let current=-1;
let pendingAnchor='';
function textSpan(className,value){{const span=document.createElement('span');span.className=className;span.textContent=value;return span}}
function navButton(buttonClass,num,label,index,anchor='',kind=''){{const button=document.createElement('button');button.type='button';button.className=buttonClass;button.dataset.index=String(index);button.dataset.anchor=anchor;if(index===current&&!anchor)button.setAttribute('aria-current','page');button.appendChild(textSpan('num',num));const copy=document.createElement('span');copy.className='label';copy.textContent=label;if(kind)copy.appendChild(textSpan('toc-kind',kind));button.appendChild(copy);button.addEventListener('click',()=>openItem(index,true,anchor));return button}}
function renderList(query=''){{const q=query.trim().toLowerCase();list.innerHTML='';if(!q||'cover tracks audience'.includes(q))list.appendChild(navButton('front-link','START','Cover and learning tracks',-1));modules.forEach((module,index)=>{{const matchingSections=module.navigation.filter(section=>!q||`${{section.id}} ${{section.title}} ${{section.kind}}`.toLowerCase().includes(q));const moduleMatches=!q||`${{module.number}} ${{module.title}}`.toLowerCase().includes(q);if(q&&!moduleMatches&&!matchingSections.length)return;const details=document.createElement('details');details.className='toc-module';details.open=index===current||Boolean(q);const summary=document.createElement('summary');summary.appendChild(textSpan('num',`M${{module.number}}`));summary.appendChild(textSpan('label',module.title));details.appendChild(summary);const children=document.createElement('div');children.className='toc-children';children.appendChild(navButton('open-module',`M${{module.number}}`,'Open complete module',index));const visibleSections=q&&!moduleMatches?matchingSections:module.navigation;visibleSections.forEach(section=>{{let cls='section-link';if(section.level===2)cls+=' nested';if(section.kind==='planned'||section.kind==='enhancement')cls+=' proposed';if(section.kind==='planned subtopic')cls+=' proposed subtopic';children.appendChild(navButton(cls,section.id,section.title,index,section.anchor,section.kind));}});details.appendChild(children);list.appendChild(details);}})}}
function scrollToPending(){{if(!pendingAnchor)return;const target=frame.contentWindow&&frame.contentWindow.document.getElementById(pendingAnchor);if(target)target.scrollIntoView({{behavior:'smooth',block:'start'}});pendingAnchor='';}}
frame.addEventListener('load',scrollToPending);
function openItem(index,push,anchor=''){{const nextIndex=Math.max(-1,Math.min(modules.length-1,index));const changed=nextIndex!==current;current=nextIndex;pendingAnchor=anchor;if(current<0){{frame.srcdoc=cover;title.textContent='{PROGRAM_SUBTITLE}';number.textContent='ONE FOUNDATION · SEVEN TRACKS · 64 MODULES';progress.style.width='0%';}}else{{const module=modules[current];if(changed||!frame.srcdoc)frame.srcdoc=module.content;else scrollToPending();frame.title=`Module ${{module.number}}: ${{module.title}}`;title.textContent=module.title;number.textContent=`MODULE ${{module.number}} · ${{current+1}} OF ${{modules.length}}`;progress.style.width=`${{((current+1)/modules.length)*100}}%`;}}previous.disabled=current<0;next.disabled=current===modules.length-1;renderList(search.value);if(push)history.pushState({{index:current,anchor}},'',current<0?'#cover':`#module=${{modules[current].number}}${{anchor?'&section='+encodeURIComponent(anchor):''}}`);document.body.classList.remove('nav-open');menu.setAttribute('aria-expanded','false');}}
function indexFromHash(){{const match=location.hash.match(/module=(\\d{{2}})/);if(!match)return -1;return modules.findIndex(module=>module.number===match[1]);}}function anchorFromHash(){{const match=location.hash.match(/section=([^&]+)/);return match?decodeURIComponent(match[1]):''}}search.addEventListener('input',()=>renderList(search.value));previous.addEventListener('click',()=>openItem(current-1,true));next.addEventListener('click',()=>openItem(current+1,true));menu.addEventListener('click',()=>{{const open=document.body.classList.toggle('nav-open');menu.setAttribute('aria-expanded',String(open));}});window.addEventListener('popstate',()=>openItem(indexFromHash(),false,anchorFromHash()));document.addEventListener('keydown',event=>{{if(event.key==='Escape'){{document.body.classList.remove('nav-open');menu.setAttribute('aria-expanded','false');}}}});openItem(indexFromHash(),false,anchorFromHash());
</script></body></html>"""


def build() -> dict[str, object]:
    paths = source_module_paths()
    titles = canonical_titles()
    granular = granular_curriculum()
    granular_modules = {module["number"]: module for module in granular["modules"]}
    chrome = chrome_binary()
    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="owos-applied-intelligence-") as temp_name:
        temp = Path(temp_name)
        html_dir = temp / "html"
        pdf_dir = temp / "pdf"
        html_dir.mkdir()
        pdf_dir.mkdir()
        module_records: list[dict[str, str]] = []
        module_pdfs: dict[int, Path] = {}
        module_pages: dict[int, int] = {}
        local_pages: dict[int, dict[str, int]] = {}

        for index, source_path in enumerate(paths):
            number = int(source_path.name.split("_", 2)[1])
            module = granular_modules[f"{number:02d}"]
            revised = replace_identity(source_path.read_text(encoding="utf-8"))
            revised = inject_granular_structure(revised, module)
            revised_for_reader = embed_skills_download(revised)
            revised_path = html_dir / source_path.name
            revised_path.write_text(revised, encoding="utf-8")
            destination = pdf_dir / source_path.with_suffix(".pdf").name
            render_html(chrome, revised_path, destination)
            module_pdfs[number] = destination
            module_pages[number] = len(PdfReader(destination).pages)
            local_pages[number] = section_local_pages(destination, module)
            module_records.append({
                "number": f"{number:02d}",
                "title": titles[f"{number:02d}"],
                "content": revised_for_reader,
                "navigation": module_navigation(module),
            })
            print(f"Rendered module {number:02d} of 63", flush=True)

        cover_html = temp / "cover.html"
        cover_pdf = temp / "cover.pdf"
        cover = cover_document()
        cover_html.write_text(cover, encoding="utf-8")
        render_html(chrome, cover_html, cover_pdf)
        if len(PdfReader(cover_pdf).pages) != 1:
            raise RuntimeError("The branded cover must render as exactly one page")

        toc_pages = 48
        toc_html = temp / "toc.html"
        toc_pdf = temp / "toc.pdf"
        for _ in range(6):
            toc_html.write_text(
                toc_document(titles, module_pages, toc_pages, granular["modules"], local_pages),
                encoding="utf-8",
            )
            render_html(chrome, toc_html, toc_pdf)
            actual = len(PdfReader(toc_pdf).pages)
            if actual == toc_pages:
                break
            toc_pages = actual

        writer = PdfWriter()
        sequence = [cover_pdf, toc_pdf] + [module_pdfs[number] for number in range(EXPECTED_MODULES)] + [LEGACY_GLOSSARY_PDF]
        page_offset = 0
        module_start_pages: dict[int, int] = {}
        for sequence_index, path in enumerate(sequence):
            reader = PdfReader(path)
            if sequence_index >= 2 and sequence_index < 2 + EXPECTED_MODULES:
                module_start_pages[sequence_index - 2] = page_offset
            for page in reader.pages:
                writer.add_page(page)
            page_offset += len(reader.pages)
        writer.add_metadata({
            "/Title": f"{PROGRAM_NAME}: {PROGRAM_SUBTITLE}",
            "/Author": "Hardeep Anand, PE - APAS.AI",
            "/Subject": "Complete 64-module applied intelligence curriculum for the water sector",
            "/Keywords": "One Water, artificial intelligence, water utilities, applied intelligence, curriculum",
        })
        writer.add_outline_item("Cover and Learning Tracks", 0)
        contents_parent = writer.add_outline_item("Complete Granular Curriculum Contents", 1)
        for roman, part_title, numbers in PARTS:
            numbers_list = list(numbers)
            parent = writer.add_outline_item(f"Part {roman + ': ' if roman else ''}{part_title}", module_start_pages[numbers_list[0]])
            for number in numbers_list:
                module = granular["modules"][number]
                module_parent = writer.add_outline_item(f"M{number:02d}. {titles[f'{number:02d}']}", module_start_pages[number], parent=parent)
                for section in module["current_sections"]:
                    target = module_start_pages[number] + local_pages[number][section["id"]] - 1
                    writer.add_outline_item(f"{section['id']} {section['title']}", target, parent=module_parent)
                for addition in module.get("proposed_additions", []):
                    target = module_start_pages[number] + local_pages[number][addition["id"]] - 1
                    addition_parent = writer.add_outline_item(f"{addition['id']} Planned: {addition['title']}", target, parent=module_parent)
                    for subtopic in addition["subtopics"]:
                        sub_target = module_start_pages[number] + local_pages[number][subtopic["id"]] - 1
                        writer.add_outline_item(f"{subtopic['id']} {subtopic['title']}", sub_target, parent=addition_parent)
                for enhancement in module.get("targeted_enhancements", []):
                    target = module_start_pages[number] + local_pages[number][enhancement["id"]] - 1
                    writer.add_outline_item(f"{enhancement['id']} Strengthen: {enhancement['title']}", target, parent=module_parent)
        with OUTPUT_PDF.open("wb") as handle:
            writer.write(handle)

        OUTPUT_HTML.write_text(interactive_reader(cover, module_records), encoding="utf-8")

    return {
        "program_name": PROGRAM_NAME,
        "program_subtitle": PROGRAM_SUBTITLE,
        "tracks": [name for name, _ in TRACKS],
        "modules": EXPECTED_MODULES,
        "source": {
            "legacy_pdf": str((LEGACY_BOOK / "One_Water_AI_Master_Class_Master.pdf").relative_to(REPO_ROOT)),
            "legacy_pdf_sha256": sha256(LEGACY_BOOK / "One_Water_AI_Master_Class_Master.pdf"),
            "module_html_hashes": {path.name: sha256(path) for path in paths},
            "glossary_sha256": sha256(LEGACY_GLOSSARY_PDF),
            "granular_structure_sha256": granular_structure_sha256(granular),
            "builder_sha256": sha256(BUILDER),
        },
        "outputs": {
            str(OUTPUT_HTML.relative_to(APP_ROOT)): {"sha256": sha256(OUTPUT_HTML)},
            str(OUTPUT_PDF.relative_to(APP_ROOT)): {"sha256": sha256(OUTPUT_PDF), "pages": len(PdfReader(OUTPUT_PDF).pages)},
        },
    }


def rebuild_reader() -> None:
    paths = source_module_paths()
    titles = canonical_titles()
    granular = granular_curriculum()
    granular_modules = {module["number"]: module for module in granular["modules"]}
    module_records = []
    for source_path in paths:
        number = int(source_path.name.split("_", 2)[1])
        module = granular_modules[f"{number:02d}"]
        revised = replace_identity(source_path.read_text(encoding="utf-8"))
        revised = inject_granular_structure(revised, module)
        module_records.append({
            "number": f"{number:02d}",
            "title": titles[f"{number:02d}"],
            "content": embed_skills_download(revised),
            "navigation": module_navigation(module),
        })
    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(interactive_reader(cover_document(), module_records), encoding="utf-8")
    manifest = json.loads(OUTPUT_MANIFEST.read_text(encoding="utf-8"))
    manifest["source"]["builder_sha256"] = sha256(BUILDER)
    manifest["source"]["granular_structure_sha256"] = granular_structure_sha256(granular)
    manifest["outputs"][str(OUTPUT_HTML.relative_to(APP_ROOT))]["sha256"] = sha256(OUTPUT_HTML)
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def check() -> None:
    if not OUTPUT_MANIFEST.exists():
        raise RuntimeError("The curriculum build manifest is missing")
    manifest = json.loads(OUTPUT_MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("program_name") != PROGRAM_NAME or manifest.get("modules") != EXPECTED_MODULES:
        raise RuntimeError("Program identity or module count is out of sync")
    if manifest["source"].get("builder_sha256") != sha256(BUILDER):
        raise RuntimeError("The official curriculum builder changed without a rebuild")
    if manifest["source"].get("granular_structure_sha256") != granular_structure_sha256():
        raise RuntimeError("The granular curriculum tracker changed without a rebuild")
    for relative, record in manifest["outputs"].items():
        path = APP_ROOT / relative
        if not path.exists() or sha256(path) != record["sha256"]:
            raise RuntimeError(f"Output is missing or stale: {relative}")
    html_text = OUTPUT_HTML.read_text(encoding="utf-8")
    if "One Water AI Master Class" in html_text or "The One Water AI Master Class" in html_text:
        raise RuntimeError("Legacy Master Class branding remains in the new HTML")
    if html_text.count('"number": "') != EXPECTED_MODULES:
        raise RuntimeError("The interactive HTML does not contain exactly 64 modules")
    if html_text.count('"navigation": [') != EXPECTED_MODULES:
        raise RuntimeError("The interactive HTML does not contain granular navigation for all 64 modules")
    script_text = "const cover=" + html_text.split("\n<script>\nconst cover=", 1)[1].rsplit("\n</script>", 1)[0]
    syntax = subprocess.run(["node", "--check"], input=script_text, text=True, capture_output=True)
    if syntax.returncode:
        raise RuntimeError(f"The interactive HTML JavaScript is invalid: {syntax.stderr.strip()}")
    pdf_reader = PdfReader(OUTPUT_PDF)
    pdf_text = "\n".join(page.extract_text() or "" for page in pdf_reader.pages)
    normalized_pdf_text = " ".join(pdf_text.split())
    if PROGRAM_SUBTITLE not in normalized_pdf_text or "One Water AI Master Class" in normalized_pdf_text:
        raise RuntimeError("The new PDF title is missing or legacy branding remains")
    if "Module 63" not in pdf_text or "Master Glossary" not in pdf_text:
        raise RuntimeError("The new PDF is missing the final module or glossary")
    if "Complete Granular Curriculum Contents" not in normalized_pdf_text:
        raise RuntimeError("The new PDF is missing the detailed curriculum contents")
    if "M40.03" not in pdf_text or "M40.P01" not in pdf_text:
        raise RuntimeError("The new PDF is missing numbered current or planned sections")
    print(f"Verified {PROGRAM_NAME}: {EXPECTED_MODULES} modules, {len(pdf_reader.pages)} PDF pages, complete interactive HTML")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--reader-only", action="store_true")
    args = parser.parse_args()
    if args.check:
        check()
        return
    if args.reader_only:
        rebuild_reader()
        check()
        return
    manifest = build()
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    check()


if __name__ == "__main__":
    main()
