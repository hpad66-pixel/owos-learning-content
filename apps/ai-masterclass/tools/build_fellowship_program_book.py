#!/usr/bin/env python3
"""Build the synchronized One Water AI Executive Fellowship document package."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import zipfile
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from build_fellowship_pdfs import PROGRAM_TITLE, parse_syllabus, register_fonts


ROOT = Path(__file__).resolve().parents[1]
SYLLABUS = ROOT / "SYLLABUS.md"
COURSE_BRIEF = ROOT / "COURSE-BRIEF.md"
FIELDBOOK_BLUEPRINT = ROOT / "work-products" / "ONE-WATER-AI-FIELDBOOK-BLUEPRINT.md"
RESEARCH_TEMPLATE = ROOT / "research" / "MODULE-RESEARCH-AND-VISUAL-BRIEF-TEMPLATE.md"
CURRICULUM_PDF = ROOT / "output" / "pdf" / "one-water-ai-executive-fellowship-master-curriculum.pdf"
FIELDBOOK_PDF = ROOT / "output" / "pdf" / "one-water-ai-fieldbook-working-edition.pdf"
HTML_DIR = ROOT / "output" / "html"
PDF_DIR = ROOT / "output" / "pdf"
PACKAGE_DIR = ROOT / "output" / "package"
PROGRAM_HTML = HTML_DIR / "one-water-ai-executive-fellowship-program-book.html"
PROGRAM_PDF = PDF_DIR / "one-water-ai-executive-fellowship-program-book.pdf"
PACKAGE_ZIP = PACKAGE_DIR / "one-water-ai-executive-fellowship-document-package.zip"
MANIFEST = ROOT / "output" / "fellowship-program-book-manifest.json"
PACKAGE_README = PACKAGE_DIR / "README.txt"
BUILDER = Path(__file__).resolve()

GRAPHITE = colors.HexColor("#102B3A")
NAVY = colors.HexColor("#0B2231")
WATER = colors.HexColor("#0786C6")
SKY = colors.HexColor("#DFF3FC")
GOLD = colors.HexColor("#E6B84A")
INK = colors.HexColor("#172638")
MUTED = colors.HexColor("#556779")
LINE = colors.HexColor("#D7E3EB")
PAPER = colors.HexColor("#F5F9FC")
WHITE = colors.white


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    return " ".join(text.split())


def extract_section(markdown: str, heading: str, next_heading: str | None = None) -> str:
    start = markdown.index(heading) + len(heading)
    end = markdown.find(next_heading, start) if next_heading else len(markdown)
    if end < 0:
        end = len(markdown)
    return markdown[start:end].strip()


def extract_numbered_items(section: str) -> list[str]:
    return [clean_markdown(match.group(1)) for match in re.finditer(r"^\d+\.\s+(.+?)(?=\n\d+\.|\Z)", section, re.MULTILINE | re.DOTALL)]


def extract_bullets(section: str) -> list[str]:
    return [clean_markdown(line[2:]) for line in section.splitlines() if line.startswith("- ")]


def extract_references(section: str) -> list[dict[str, str]]:
    lines = section.splitlines()
    references: list[dict[str, str]] = []
    for index, line in enumerate(lines):
        if not line.startswith("- "):
            continue
        label = clean_markdown(line[2:]).rstrip(":")
        url = ""
        for candidate in lines[index + 1 :]:
            candidate = candidate.strip()
            if not candidate:
                continue
            if candidate.startswith("http"):
                url = candidate
            break
        references.append({"label": label, "url": url})
    return references


def program_data() -> dict[str, object]:
    markdown = SYLLABUS.read_text(encoding="utf-8")
    courses = parse_syllabus()
    value_text = extract_section(markdown, "## The value proposition", "## Why this program earns a premium position")
    premium_text = extract_section(markdown, "## Why this program earns a premium position", "## Intended participants")
    participants_text = extract_section(markdown, "## Intended participants", "## Program architecture")
    capstone_text = extract_section(markdown, "## Capstone completion standard", "## Learning rhythm")
    rhythm_text = extract_section(markdown, "## Learning rhythm", "## Completion evidence")
    completion_text = extract_section(markdown, "## Completion evidence", "## Program references used for curriculum comparison")
    references_text = extract_section(markdown, "## Program references used for curriculum comparison")
    value_paragraphs = [clean_markdown(item) for item in re.split(r"\n\s*\n", value_text) if item.strip()]
    return {
        "courses": courses,
        "value_paragraphs": value_paragraphs,
        "premium": extract_numbered_items(premium_text),
        "participants": extract_bullets(participants_text),
        "capstone": extract_numbered_items(capstone_text),
        "rhythm": extract_numbered_items(rhythm_text),
        "completion": extract_bullets(completion_text),
        "references": extract_references(references_text),
    }


def html_list(items: list[str], ordered: bool = False) -> str:
    tag = "ol" if ordered else "ul"
    return f"<{tag}>" + "".join(f"<li>{html.escape(item)}</li>" for item in items) + f"</{tag}>"


def build_html(data: dict[str, object]) -> str:
    courses = data["courses"]
    course_cards = []
    for course in courses:
        module_rows = "".join(
            f"""
            <article class="module">
              <div class="module-number">{module.number:02d}</div>
              <div>
                <h4>{html.escape(module.title)}</h4>
                <p>{html.escape(module.learning_job)}</p>
                <p class="result"><strong>Fieldbook result:</strong> {html.escape(module.result)}</p>
              </div>
            </article>"""
            for module in course.modules
        )
        course_cards.append(
            f"""
            <details class="course" id="course-{course.number}" open>
              <summary>
                <span class="course-kicker">Course {course.number} · Weeks {(course.number - 1) * 3 + 1} to {course.number * 3}</span>
                <span class="course-title">{html.escape(course.title)}</span>
                <span class="course-promise">{html.escape(course.promise)}</span>
              </summary>
              <div class="module-grid">{module_rows}</div>
            </details>"""
        )

    workflow = [
        ("1", "Define value", "Name the utility decision, audience, work product, and professional value."),
        ("2", "Discover sources", "Use Perplexity or another research tool to find source leads, then open the originals."),
        ("3", "Preserve evidence", "Register direct URLs, files, dates, permissions, and exact locators."),
        ("4", "Verify claims", "Check every material claim against the original source and record limitations."),
        ("5", "Write the manuscript", "Produce one complete Markdown teaching paper in plain English."),
        ("6", "Design graphics", "Describe visuals that explain a process, relationship, comparison, or decision."),
        ("7", "Assemble learning", "Build the approved lesson in Articulate with interactions, checks, and accessibility."),
        ("8", "Review and release", "Run factual, practitioner, learning, accessibility, and publishing gates."),
    ]
    workflow_html = "".join(
        f'<div class="step"><span>{number}</span><h4>{title}</h4><p>{body}</p></div>'
        for number, title, body in workflow
    )
    value_html = "".join(f"<p>{html.escape(item)}</p>" for item in data["value_paragraphs"])
    reference_links = "".join(
        f'<li><a href="{html.escape(ref["url"])}">{html.escape(ref["label"])}</a></li>'
        for ref in data["references"]
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Complete program book for the One Water AI Executive Fellowship.">
  <title>{PROGRAM_TITLE} | Program Book</title>
  <style>
    :root {{ --navy:#0b2231; --graphite:#102b3a; --water:#0786c6; --sky:#dff3fc; --gold:#e6b84a; --ink:#172638; --muted:#556779; --line:#d7e3eb; --paper:#f5f9fc; --white:#fff; }}
    * {{ box-sizing:border-box; }}
    html {{ scroll-behavior:smooth; }}
    body {{ margin:0; color:var(--ink); background:var(--paper); font-family:Arial, Helvetica, sans-serif; line-height:1.58; }}
    a {{ color:#036fa8; }}
    .topbar {{ position:sticky; top:0; z-index:20; display:flex; gap:20px; align-items:center; justify-content:space-between; padding:14px clamp(18px,4vw,64px); background:rgba(255,255,255,.96); border-bottom:1px solid var(--line); backdrop-filter:blur(12px); }}
    .brand {{ display:flex; align-items:center; gap:12px; font-weight:800; color:var(--navy); }}
    .drop {{ width:34px; height:34px; display:grid; place-items:center; border-radius:11px; color:white; background:linear-gradient(145deg,var(--water),#0a5f91); }}
    .actions {{ display:flex; flex-wrap:wrap; gap:8px; }}
    .button {{ display:inline-flex; align-items:center; justify-content:center; min-height:42px; padding:8px 15px; border-radius:11px; text-decoration:none; font-weight:700; background:var(--water); color:white; border:1px solid var(--water); }}
    .button.secondary {{ color:var(--navy); background:white; border-color:var(--line); }}
    .hero {{ color:white; background:linear-gradient(135deg,var(--navy) 0%,#07507a 58%,#0794d4 100%); overflow:hidden; }}
    .hero-inner {{ max-width:1280px; margin:auto; padding:clamp(64px,10vw,125px) clamp(22px,5vw,70px); position:relative; }}
    .hero-inner:after {{ content:""; position:absolute; width:430px; height:430px; border:1px solid rgba(255,255,255,.22); border-radius:50%; right:-110px; bottom:-280px; box-shadow:0 0 0 70px rgba(255,255,255,.06),0 0 0 140px rgba(255,255,255,.04); }}
    .eyebrow {{ margin:0 0 12px; color:#bdeaff; text-transform:uppercase; letter-spacing:.16em; font-size:.78rem; font-weight:800; }}
    h1 {{ max-width:900px; margin:0; font-size:clamp(2.7rem,7vw,6rem); line-height:.96; letter-spacing:-.055em; }}
    .lede {{ max-width:790px; margin:25px 0 0; font-size:clamp(1.05rem,2vw,1.35rem); color:#eef9ff; }}
    .facts {{ max-width:1280px; margin:-34px auto 0; padding:0 clamp(22px,5vw,70px); position:relative; z-index:2; display:grid; grid-template-columns:repeat(4,1fr); gap:12px; }}
    .fact {{ background:white; border:1px solid var(--line); border-radius:17px; padding:22px; box-shadow:0 12px 35px rgba(7,35,54,.10); }}
    .fact strong {{ display:block; font-size:1.6rem; color:var(--navy); }}
    .fact span {{ color:var(--muted); font-size:.9rem; }}
    main {{ max-width:1280px; margin:auto; padding:54px clamp(22px,5vw,70px) 90px; }}
    section {{ margin:0 0 72px; scroll-margin-top:95px; }}
    .section-label {{ color:var(--water); text-transform:uppercase; letter-spacing:.15em; font-size:.75rem; font-weight:800; }}
    h2 {{ margin:.25rem 0 1rem; color:var(--navy); font-size:clamp(2rem,4vw,3.4rem); line-height:1.04; letter-spacing:-.035em; }}
    h3 {{ color:var(--navy); }}
    .intro {{ max-width:820px; color:var(--muted); font-size:1.12rem; }}
    .two-col {{ display:grid; grid-template-columns:1.05fr .95fr; gap:26px; }}
    .panel {{ background:white; border:1px solid var(--line); border-radius:20px; padding:clamp(22px,3vw,34px); }}
    .panel.dark {{ background:var(--navy); color:white; border:0; }}
    .panel.dark h3 {{ color:white; }}
    .panel.dark p, .panel.dark li {{ color:#dceaf2; }}
    .workflow {{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-top:25px; }}
    .step {{ position:relative; min-height:215px; padding:22px; background:white; border:1px solid var(--line); border-radius:18px; }}
    .step span {{ display:grid; place-items:center; width:34px; height:34px; border-radius:50%; background:var(--sky); color:#075f8e; font-weight:800; }}
    .step h4 {{ margin:18px 0 8px; font-size:1.05rem; color:var(--navy); }}
    .step p {{ margin:0; color:var(--muted); font-size:.93rem; }}
    .course {{ margin:16px 0; background:white; border:1px solid var(--line); border-radius:20px; overflow:hidden; }}
    .course summary {{ cursor:pointer; list-style:none; padding:26px clamp(22px,4vw,42px); background:linear-gradient(120deg,#eef8fd,#fff); }}
    .course summary::-webkit-details-marker {{ display:none; }}
    .course-kicker {{ display:block; color:#0675ad; text-transform:uppercase; letter-spacing:.13em; font-size:.72rem; font-weight:800; }}
    .course-title {{ display:block; margin:6px 0; color:var(--navy); font-size:clamp(1.35rem,3vw,2rem); font-weight:800; line-height:1.12; }}
    .course-promise {{ display:block; max-width:860px; color:var(--muted); }}
    .module-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:1px; background:var(--line); border-top:1px solid var(--line); }}
    .module {{ display:grid; grid-template-columns:48px 1fr; gap:16px; padding:23px; background:white; }}
    .module-number {{ font-size:1.2rem; font-weight:800; color:var(--water); }}
    .module h4 {{ margin:0 0 7px; color:var(--navy); font-size:1rem; }}
    .module p {{ margin:0; color:var(--muted); font-size:.92rem; }}
    .module .result {{ margin-top:8px; color:var(--ink); }}
    .architecture {{ display:grid; grid-template-columns:repeat(5,1fr); gap:10px; align-items:center; margin-top:25px; }}
    .arch-node {{ min-height:138px; display:flex; flex-direction:column; justify-content:center; padding:18px; border-radius:17px; background:white; border:1px solid var(--line); }}
    .arch-node strong {{ color:var(--navy); }}
    .arch-node span {{ margin-top:6px; color:var(--muted); font-size:.88rem; }}
    .status {{ border-left:5px solid var(--gold); }}
    footer {{ padding:35px clamp(22px,5vw,70px); background:var(--navy); color:#dceaf2; }}
    footer strong {{ color:white; }}
    @media (max-width:900px) {{ .facts,.workflow {{ grid-template-columns:1fr 1fr; }} .two-col,.module-grid,.architecture {{ grid-template-columns:1fr; }} .arch-node {{ min-height:auto; }} }}
    @media (max-width:560px) {{ .topbar {{ align-items:flex-start; }} .brand span {{ max-width:155px; }} .actions .secondary {{ display:none; }} .facts,.workflow {{ grid-template-columns:1fr; }} .facts {{ margin-top:0; padding-top:18px; }} h1 {{ font-size:2.65rem; }} .module {{ grid-template-columns:38px 1fr; padding:19px 16px; }} }}
    @media print {{ .topbar {{ display:none; }} .hero-inner {{ padding:55px; }} .facts {{ margin:15px auto 0; }} details > * {{ display:block !important; }} .course,.panel,.step,.module {{ break-inside:avoid; box-shadow:none; }} main {{ padding:35px; }} }}
  </style>
</head>
<body>
  <nav class="topbar" aria-label="Document downloads">
    <div class="brand"><span class="drop">OW</span><span>One Water AI Executive Fellowship</span></div>
    <div class="actions">
      <a class="button secondary" href="../pdf/one-water-ai-executive-fellowship-master-curriculum.pdf">Curriculum PDF</a>
      <a class="button secondary" href="../pdf/one-water-ai-fieldbook-working-edition.pdf">Fieldbook PDF</a>
      <a class="button" href="../pdf/one-water-ai-executive-fellowship-program-book.pdf">Download this PDF</a>
    </div>
  </nav>
  <header class="hero">
    <div class="hero-inner">
      <p class="eyebrow">One Water Operating System · Powered by APAS.AI</p>
      <h1>One Water AI Executive Fellowship</h1>
      <p class="lede">A six-month applied program for professionals responsible for water, wastewater, and stormwater decisions. Learn the technology in plain English, test it against utility work, and leave with a governed implementation portfolio.</p>
    </div>
  </header>
  <div class="facts" aria-label="Program facts">
    <div class="fact"><strong>24 weeks</strong><span>Six-month cohort</span></div>
    <div class="fact"><strong>64 modules</strong><span>Eight connected courses</span></div>
    <div class="fact"><strong>132 hours</strong><span>Guided and applied work</span></div>
    <div class="fact"><strong>$10,000</strong><span>Target tuition per participant</span></div>
  </div>
  <main>
    <section id="purpose">
      <p class="section-label">The position</p>
      <h2>Professional judgment, not content access</h2>
      <div class="two-col">
        <div class="panel">{value_html}</div>
        <div class="panel dark"><h3>What participants leave able to do</h3>{html_list(data["premium"], ordered=True)}</div>
      </div>
    </section>
    <section id="audience">
      <p class="section-label">Who it serves</p>
      <h2>Built for people who influence consequential decisions</h2>
      <div class="two-col">
        <div class="panel"><h3>Intended participants</h3>{html_list(data["participants"])}</div>
        <div class="panel status"><h3>Current release boundary</h3><p>This program book is the current, rebranded program architecture. It contains the complete 8-course, 64-module Fellowship blueprint and its production system. It is not a claim that all 64 learner-facing Articulate modules have been authored or released.</p><p>The older 686-page <em>One Water AI Master Class</em> compilation remains a legacy source library. It must be mapped, reviewed, and rewritten into this Fellowship sequence before any section is treated as current learner content.</p></div>
      </div>
    </section>
    <section id="curriculum">
      <p class="section-label">Complete curriculum</p>
      <h2>Eight courses. Sixty-four modules. One implementation portfolio.</h2>
      <p class="intro">Open any course to see every module, the learning job, and the Fieldbook result. The sequence moves from shared language to trusted context, bounded agents, utility applications, governance, economics, studios, and a defended pilot.</p>
      {''.join(course_cards)}
    </section>
    <section id="capstone">
      <p class="section-label">Modules 57 to 64</p>
      <h2>The capstone turns learning into a governed pilot</h2>
      <div class="two-col">
        <div class="panel"><h3>Required evidence</h3>{html_list(data["capstone"], ordered=True)}</div>
        <div class="panel dark"><h3>Completion evidence</h3>{html_list(data["completion"])}</div>
      </div>
    </section>
    <section id="fieldbook">
      <p class="section-label">The companion system</p>
      <h2>The Fieldbook keeps the 64 modules connected</h2>
      <div class="two-col">
        <div class="panel"><p>The One Water AI Fieldbook is part workbook, part laboratory notebook, part decision record, and part executive playbook. Every module adds one decision, map, test, reflection, or professional record. By Module 64, those records form the participant's implementation portfolio.</p><p>Participants retain their private entries. Confidential organizational material is not shared unless the participant chooses to submit it for review.</p><a class="button" href="../pdf/one-water-ai-fieldbook-working-edition.pdf">Download the 143-page Fieldbook</a></div>
        <div class="panel"><h3>Repeating module rhythm</h3><ol><li><strong>Before:</strong> What do I currently believe, and what decision would I make?</li><li><strong>Learn:</strong> What relationship, mechanism, or distinction matters?</li><li><strong>Apply:</strong> What does this mean for one utility task or organizational situation?</li><li><strong>Keep:</strong> What record enters my implementation portfolio?</li></ol></div>
      </div>
    </section>
    <section id="workflow">
      <p class="section-label">From research to instruction</p>
      <h2>Every module follows the same governed production path</h2>
      <p class="intro">Research tools help find material. They do not become the evidence. The original source, exact locator, reviewer, and limitation stay with the claim.</p>
      <div class="workflow">{workflow_html}</div>
    </section>
    <section id="manuscript">
      <p class="section-label">The controlled Markdown file</p>
      <h2>One module record carries the research, teaching, and visual direction</h2>
      <div class="two-col">
        <div class="panel"><h3>What the manuscript contains</h3><ul><li>the module value proposition and audience;</li><li>research questions, source inventory, and claim ledger;</li><li>a complete instructor explanation in plain English;</li><li>a utility example, limitation, failure, and decision method;</li><li>graphic instructions that state what each visual teaches;</li><li>distributed assessments with explanatory feedback;</li><li>frequently asked questions, citations, and approval state.</li></ul></div>
        <div class="panel"><h3>Graphics must teach</h3><p>A graphic is chosen because a process, relationship, comparison, cause, hierarchy, quantity, place, or change is easier to understand visually. Decorative technology images do not count.</p><p>Each visual states what it must show, how the learner uses it, the conclusion the learner should reach, its accessible description, and its mobile behavior.</p><a class="button secondary" href="../../research/MODULE-RESEARCH-AND-VISUAL-BRIEF-TEMPLATE.md">Open the module template</a></div>
      </div>
    </section>
    <section id="delivery">
      <p class="section-label">Delivery architecture</p>
      <h2>The repository controls truth. Articulate teaches. LearnWorlds delivers.</h2>
      <div class="architecture" aria-label="Content and delivery architecture">
        <div class="arch-node"><strong>Research and annotations</strong><span>Original sources, transcripts, conversations, and practitioner judgment.</span></div>
        <div class="arch-node"><strong>GitHub source of truth</strong><span>Versioned syllabus, manuscript, claims, graphics brief, Fieldbook, and approvals.</span></div>
        <div class="arch-node"><strong>Articulate</strong><span>Learner-facing instruction, interactions, quizzes, accessibility, and SCORM or xAPI package.</span></div>
        <div class="arch-node"><strong>LearnWorlds</strong><span>Enrollment, cohort access, commerce, progress, community, and course delivery.</span></div>
        <div class="arch-node"><strong>OWOS knowledge graph</strong><span>Governed concepts, relationships, sources, and deeper evidence exploration.</span></div>
      </div>
    </section>
    <section id="references">
      <p class="section-label">Reference boundary</p>
      <h2>Curriculum comparison sources</h2>
      <div class="panel"><p>These sources informed the curriculum gap review. They do not authorize copying third-party course content and they do not serve as authority for utility operations.</p><ul>{reference_links}</ul></div>
    </section>
  </main>
  <footer><strong>{PROGRAM_TITLE}</strong><br>One Water Operating System · Powered by APAS.AI<br>Controlled program document. Curriculum and production status remain governed by repository approvals.</footer>
</body>
</html>
"""


class CoverBand(Flowable):
    def __init__(self, height: float = 8.1 * inch):
        super().__init__()
        self.width = 7.5 * inch
        self.height = height

    def draw(self) -> None:
        c = self.canv
        c.setFillColor(GRAPHITE)
        c.roundRect(0, 0, self.width, self.height, 20, fill=1, stroke=0)
        c.setFillColor(WATER)
        c.circle(self.width - 40, 50, 150, fill=1, stroke=0)
        c.setFillColor(colors.Color(1, 1, 1, alpha=.10))
        c.circle(self.width - 40, 50, 105, fill=1, stroke=0)
        c.setFillColor(GOLD)
        c.setFont("OWOS-Bold", 9)
        c.drawString(38, self.height - 55, "ONE WATER OPERATING SYSTEM  |  POWERED BY APAS.AI")
        c.setFillColor(WHITE)
        c.setFont("OWOS-Black", 38)
        y = self.height - 150
        for line in ["One Water AI", "Executive", "Fellowship"]:
            c.drawString(38, y, line)
            y -= 48
        c.setFillColor(colors.HexColor("#D8F2FF"))
        c.setFont("OWOS", 15)
        c.drawString(40, y - 5, "Complete program book")
        c.setFont("OWOS", 11)
        c.drawString(40, y - 42, "24 weeks  |  8 courses  |  64 modules  |  Capstone defense")
        c.drawString(40, y - 62, "Fieldbook  |  Research workflow  |  Articulate and LearnWorlds delivery")
        c.setFillColor(WHITE)
        c.setFont("OWOS-Bold", 12)
        c.drawString(40, 48, "Rebranded controlled document set  |  August 2026")


def page_footer(canvas, doc) -> None:
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.line(0.72 * inch, 0.55 * inch, 7.78 * inch, 0.55 * inch)
        canvas.setFillColor(MUTED)
        canvas.setFont("OWOS", 7.5)
        canvas.drawString(0.72 * inch, 0.35 * inch, PROGRAM_TITLE)
        canvas.drawRightString(7.78 * inch, 0.35 * inch, str(doc.page))
    canvas.restoreState()


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "h1": ParagraphStyle("H1", parent=base["Heading1"], fontName="OWOS-Black", fontSize=27, leading=30, textColor=GRAPHITE, spaceAfter=15),
        "h2": ParagraphStyle("H2", parent=base["Heading2"], fontName="OWOS-Bold", fontSize=18, leading=22, textColor=GRAPHITE, spaceBefore=8, spaceAfter=10),
        "h3": ParagraphStyle("H3", parent=base["Heading3"], fontName="OWOS-Bold", fontSize=12, leading=15, textColor=WATER, spaceBefore=6, spaceAfter=6),
        "body": ParagraphStyle("Body", parent=base["BodyText"], fontName="OWOS", fontSize=9.4, leading=14, textColor=INK, spaceAfter=8),
        "small": ParagraphStyle("Small", parent=base["BodyText"], fontName="OWOS", fontSize=8, leading=11, textColor=MUTED),
        "module": ParagraphStyle("Module", parent=base["BodyText"], fontName="OWOS", fontSize=8.3, leading=11, textColor=INK),
        "label": ParagraphStyle("Label", parent=base["BodyText"], fontName="OWOS-Bold", fontSize=7.2, leading=9, textColor=WATER, uppercase=True, spaceAfter=5),
        "center": ParagraphStyle("Center", parent=base["BodyText"], fontName="OWOS", fontSize=9, leading=13, textColor=INK, alignment=TA_CENTER),
        "toc": ParagraphStyle("Toc", parent=base["BodyText"], fontName="OWOS-Bold", fontSize=10, leading=14, textColor=GRAPHITE),
    }


def bullet_flowables(items: list[str], style: ParagraphStyle, ordered: bool = False) -> list[Paragraph]:
    return [Paragraph(f"{index}. {html.escape(item)}" if ordered else f"• {html.escape(item)}", style) for index, item in enumerate(items, 1)]


def section_header(kicker: str, title: str, s: dict[str, ParagraphStyle]) -> list[Flowable]:
    return [Paragraph(kicker.upper(), s["label"]), Paragraph(title, s["h1"]), Spacer(1, 5)]


def build_pdf(data: dict[str, object]) -> None:
    register_fonts()
    PROGRAM_PDF.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(PROGRAM_PDF),
        pagesize=letter,
        rightMargin=.72 * inch,
        leftMargin=.72 * inch,
        topMargin=.68 * inch,
        bottomMargin=.68 * inch,
        title=f"{PROGRAM_TITLE} | Complete Program Book",
        author="One Water Operating System, powered by APAS.AI",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="content", frames=[frame], onPage=page_footer)])
    s = styles()
    story: list[Flowable] = [CoverBand(), PageBreak()]

    story += section_header("Document map", "What is inside", s)
    toc = [
        ("01", "Program position and value"), ("02", "Audience and program facts"),
        ("03", "Complete 8-course, 64-module curriculum"), ("04", "Capstone and completion standard"),
        ("05", "Fieldbook and participant portfolio"), ("06", "Research, evidence, manuscript, and graphics workflow"),
        ("07", "Articulate, LearnWorlds, and OWOS delivery architecture"), ("08", "Release boundary and reference sources"),
    ]
    table = Table([[Paragraph(number, s["h3"]), Paragraph(label, s["toc"])] for number, label in toc], colWidths=[.55 * inch, 5.9 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LINEBELOW", (0,0), (-1,-1), .4, LINE), ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8)]))
    story += [table, Spacer(1, 20), Paragraph("Naming correction", s["h2"]), Paragraph("The current program is the One Water AI Executive Fellowship. The older 686-page One Water AI Master Class compilation remains a legacy source library. It is not relabeled as completed Fellowship instruction.", s["body"]), PageBreak()]

    story += section_header("01 · The position", "Professional judgment, not content access", s)
    for paragraph in data["value_paragraphs"]:
        story.append(Paragraph(html.escape(paragraph), s["body"]))
    story += [Paragraph("What participants leave able to do", s["h2"])]
    story += bullet_flowables(data["premium"], s["body"], ordered=True)
    story += [PageBreak()]

    story += section_header("02 · Program facts", "Designed for consequential utility decisions", s)
    facts = [["24 weeks", "64 modules", "132 hours", "$10,000 target"], ["Six-month cohort", "Eight courses", "Guided effort", "Per participant"]]
    fact_table = Table(facts, colWidths=[1.62 * inch] * 4, rowHeights=[.45 * inch, .3 * inch])
    fact_table.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), SKY), ("TEXTCOLOR", (0,0), (-1,0), GRAPHITE), ("FONTNAME", (0,0), (-1,0), "OWOS-Bold"), ("FONTSIZE", (0,0), (-1,0), 12), ("FONTNAME", (0,1), (-1,1), "OWOS"), ("FONTSIZE", (0,1), (-1,1), 7.5), ("ALIGN", (0,0), (-1,-1), "CENTER"), ("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("BOX", (0,0), (-1,-1), .6, LINE), ("INNERGRID", (0,0), (-1,-1), .4, LINE)]))
    story += [fact_table, Spacer(1, 16), Paragraph("Intended participants", s["h2"])]
    story += bullet_flowables(data["participants"], s["body"])
    story += [Spacer(1, 10), Paragraph("Current release boundary", s["h2"]), Paragraph("This program book contains the complete rebranded curriculum and the production system that keeps it controlled. It does not claim that all 64 learner-facing Articulate modules are complete. Each module still passes research, factual, practitioner, learning, accessibility, and release gates.", s["body"]), PageBreak()]

    story += section_header("03 · Complete curriculum", "Eight connected courses", s)
    story.append(Paragraph("The sequence moves from shared language to trusted context, bounded agents, utility applications, governance, economics, applied studios, and a defended pilot. Every module produces a Fieldbook record.", s["body"]))
    for course in data["courses"]:
        course_header = [Spacer(1, 8), Paragraph(f"Course {course.number}: {html.escape(course.title)}", s["h2"]), Paragraph(html.escape(course.promise), s["body"])]
        module_table_data = [[Paragraph("Module", s["label"]), Paragraph("Learning job", s["label"]), Paragraph("Fieldbook result", s["label"])]]
        for module in course.modules:
            module_table_data.append([
                Paragraph(f"<b>{module.number}. {html.escape(module.title)}</b>", s["module"]),
                Paragraph(html.escape(module.learning_job), s["module"]),
                Paragraph(html.escape(module.result), s["module"]),
            ])
        module_table = Table(module_table_data, colWidths=[2.0 * inch, 2.8 * inch, 1.65 * inch], repeatRows=1, hAlign="LEFT")
        module_table.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), GRAPHITE), ("TEXTCOLOR", (0,0), (-1,0), WHITE), ("VALIGN", (0,0), (-1,-1), "TOP"), ("BOX", (0,0), (-1,-1), .5, LINE), ("INNERGRID", (0,0), (-1,-1), .35, LINE), ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, PAPER]), ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
        story += [KeepTogether(course_header + [module_table]), PageBreak()]

    story += section_header("04 · Modules 57 to 64", "The capstone turns learning into a governed pilot", s)
    story.append(Paragraph("The capstone must identify and defend the following evidence.", s["body"]))
    story += bullet_flowables(data["capstone"], s["body"], ordered=True)
    story += [Spacer(1, 12), Paragraph("Program completion evidence", s["h2"])]
    story += bullet_flowables(data["completion"], s["body"])
    story += [Paragraph("Completion does not authorize engineering, operational, regulatory, financial, procurement, or security decisions. Any credential remains disabled until independent evidence, assessment, identity, and issuance gates are approved.", s["small"]), PageBreak()]

    story += section_header("05 · The companion system", "The Fieldbook keeps 64 modules connected", s)
    story += [Paragraph("The One Water AI Fieldbook is part workbook, part laboratory notebook, part decision record, and part executive playbook. Every module adds one decision, map, test, reflection, or professional record. By Module 64, those records form the participant's implementation portfolio.", s["body"]), Paragraph("The repeating four-part rhythm", s["h2"])]
    rhythm = [
        ["Before", "What do I currently believe, and what decision would I make?"],
        ["Learn", "What relationship, mechanism, or distinction matters?"],
        ["Apply", "What does this mean for one utility task or organizational situation?"],
        ["Keep", "What record enters my implementation portfolio?"],
    ]
    rhythm_table = Table([[Paragraph(f"<b>{a}</b>", s["body"]), Paragraph(b, s["body"])] for a,b in rhythm], colWidths=[1.0 * inch, 5.45 * inch])
    rhythm_table.setStyle(TableStyle([("BACKGROUND", (0,0), (0,-1), SKY), ("BOX", (0,0), (-1,-1), .5, LINE), ("INNERGRID", (0,0), (-1,-1), .35, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 9), ("RIGHTPADDING", (0,0), (-1,-1), 9), ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8)]))
    story += [rhythm_table, Spacer(1, 16), Paragraph("Participant control", s["h2"]), Paragraph("Participants own their entries. Confidential organizational material remains private unless the participant explicitly shares it for review. Learning records can preserve completion events without ingesting confidential text.", s["body"]), PageBreak()]

    story += section_header("06 · Production system", "From research question to governed lesson", s)
    workflow = [
        ("1. Define value", "Name the utility decision, audience, work product, and professional value."),
        ("2. Discover sources", "Use Perplexity or another research tool to find source leads. Open the original sources."),
        ("3. Preserve evidence", "Register direct URLs, files, dates, permissions, and exact locators."),
        ("4. Verify claims", "Check every material claim against the original and record limits and conflicts."),
        ("5. Write the manuscript", "Produce one complete Markdown teaching paper in plain English."),
        ("6. Design graphics", "Describe visuals that explain processes, relationships, comparisons, and decisions."),
        ("7. Assemble learning", "Build in Articulate with interactions, explanatory feedback, and accessibility."),
        ("8. Review and release", "Pass factual, practitioner, learning, accessibility, and publishing gates."),
    ]
    for index in range(0, len(workflow), 2):
        cells = []
        for title, body in workflow[index:index+2]:
            cells.append(Paragraph(f"<b>{title}</b><br/>{body}", s["body"]))
        box = Table([cells], colWidths=[3.15 * inch, 3.15 * inch])
        box.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), PAPER), ("BOX", (0,0), (-1,-1), .5, LINE), ("INNERGRID", (0,0), (-1,-1), .5, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 11), ("RIGHTPADDING", (0,0), (-1,-1), 11), ("TOPPADDING", (0,0), (-1,-1), 11), ("BOTTOMPADDING", (0,0), (-1,-1), 11)]))
        story += [box, Spacer(1, 8)]
    story += [Paragraph("Citation rule", s["h2"]), Paragraph("Perplexity supports discovery. The original source supports the claim. Every material claim records the source title, issuer, date, direct URL or file, exact locator, support, limitation, currency, applicability, conflict, reviewer, and approval state.", s["body"]), Paragraph("Graphic rule", s["h2"]), Paragraph("A graphic must make a relationship easier to understand. Each visual states what it shows, how the learner uses it, the conclusion the learner should reach, its accessible description, its mobile behavior, and the source IDs behind it. Decorative technology images do not count.", s["body"]), PageBreak()]

    story += section_header("07 · Delivery architecture", "One source of truth, three delivery layers", s)
    architecture = [
        ["Research and annotations", "Original sources, transcripts, conversations, and practitioner judgment."],
        ["GitHub source of truth", "Versioned syllabus, manuscript, claims, graphics brief, Fieldbook, and approvals."],
        ["Articulate", "Learner instruction, interactions, quizzes, accessibility, and SCORM or xAPI package."],
        ["LearnWorlds", "Enrollment, cohort access, commerce, progress, community, and delivery."],
        ["OWOS knowledge graph", "Governed concepts, relationships, sources, and deeper evidence exploration."],
    ]
    arch_table = Table([[Paragraph(f"<b>{a}</b>", s["body"]), Paragraph(b, s["body"])] for a,b in architecture], colWidths=[1.75 * inch, 4.7 * inch])
    arch_table.setStyle(TableStyle([("BACKGROUND", (0,0), (0,-1), GRAPHITE), ("TEXTCOLOR", (0,0), (0,-1), WHITE), ("BOX", (0,0), (-1,-1), .5, LINE), ("INNERGRID", (0,0), (-1,-1), .35, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10), ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10)]))
    story += [arch_table, Spacer(1, 18), Paragraph("What changes together", s["h2"]), Paragraph("When the curriculum changes, the syllabus, program book, curriculum prospectus, Fieldbook, metadata, and synchronization record are rebuilt together. Articulate and LearnWorlds receive only approved versions.", s["body"]), PageBreak()]

    story += section_header("08 · Governance", "Release boundary and reference sources", s)
    story += [Paragraph("The legacy boundary", s["h2"]), Paragraph("The 686-page One Water AI Master Class compilation is valuable source material. Its old title, sequence, and module numbering do not match this Fellowship. Migration requires a module-by-module source map, claim review, voice review, visual review, and an explicit decision to retain, rewrite, combine, or retire each section.", s["body"]), Paragraph("Curriculum comparison sources", s["h2"])]
    for reference in data["references"]:
        story.append(Paragraph(f"• <b>{html.escape(reference['label'])}</b><br/><link href=\"{html.escape(reference['url'])}\" color=\"#036FA8\">{html.escape(reference['url'])}</link>", s["body"]))
    story += [Spacer(1, 12), Paragraph("Document set", s["h2"]), Paragraph("This package includes the self-contained HTML program book, this PDF program book, the 17-page curriculum prospectus, the 143-page Fieldbook working edition, the reusable module research and visual brief, and a package README.", s["body"]), Spacer(1, 25), Paragraph("One Water Operating System", s["h2"]), Paragraph("Powered by APAS.AI", s["body"])]
    doc.build(story)


def package_readme() -> str:
    return f"""{PROGRAM_TITLE}
Complete document package

START HERE
1. Open html/one-water-ai-executive-fellowship-program-book.html in a web browser.
2. Open pdf/one-water-ai-executive-fellowship-program-book.pdf for the printable program book.

INCLUDED
- pdf/one-water-ai-executive-fellowship-program-book.pdf
- pdf/one-water-ai-executive-fellowship-master-curriculum.pdf
- pdf/one-water-ai-fieldbook-working-edition.pdf
- html/one-water-ai-executive-fellowship-program-book.html
- templates/MODULE-RESEARCH-AND-VISUAL-BRIEF-TEMPLATE.md

IMPORTANT BOUNDARY
The program architecture is complete and rebranded. The learner-facing Articulate modules are not all
complete. The older 686-page One Water AI Master Class is a legacy source library, not the current
Fellowship course book.
"""


def build_package() -> None:
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    PACKAGE_README.write_text(package_readme(), encoding="utf-8")
    with zipfile.ZipFile(PACKAGE_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(PACKAGE_README, "README.txt")
        archive.write(PROGRAM_HTML, f"html/{PROGRAM_HTML.name}")
        archive.write(PROGRAM_PDF, f"pdf/{PROGRAM_PDF.name}")
        archive.write(CURRICULUM_PDF, f"pdf/{CURRICULUM_PDF.name}")
        archive.write(FIELDBOOK_PDF, f"pdf/{FIELDBOOK_PDF.name}")
        archive.write(RESEARCH_TEMPLATE, f"templates/{RESEARCH_TEMPLATE.name}")


def build_manifest(data: dict[str, object]) -> dict[str, object]:
    outputs = [PROGRAM_HTML, PROGRAM_PDF, CURRICULUM_PDF, FIELDBOOK_PDF, PACKAGE_ZIP]
    return {
        "schema": "owos-fellowship-program-book/v1",
        "program_title": PROGRAM_TITLE,
        "course_count": len(data["courses"]),
        "module_count": sum(len(course.modules) for course in data["courses"]),
        "sources": {str(path.relative_to(ROOT)): sha256(path) for path in [SYLLABUS, COURSE_BRIEF, FIELDBOOK_BLUEPRINT, RESEARCH_TEMPLATE, BUILDER]},
        "outputs": {
            str(path.relative_to(ROOT)): {
                "sha256": sha256(path),
                **({"pages": len(PdfReader(str(path)).pages)} if path.suffix == ".pdf" else {}),
            }
            for path in outputs
        },
    }


def check(data: dict[str, object]) -> None:
    if not MANIFEST.exists():
        raise ValueError("Program book manifest is missing. Run the builder first.")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("program_title") != PROGRAM_TITLE or manifest.get("course_count") != 8 or manifest.get("module_count") != 64:
        raise ValueError("Program identity or curriculum count is out of sync")
    for relative, expected in manifest["sources"].items():
        path = ROOT / relative
        if not path.exists() or sha256(path) != expected:
            raise ValueError(f"Controlled source changed after build: {relative}")
    for relative, record in manifest["outputs"].items():
        path = ROOT / relative
        if not path.exists() or sha256(path) != record["sha256"]:
            raise ValueError(f"Output is missing or stale: {relative}")
    html_text = PROGRAM_HTML.read_text(encoding="utf-8")
    if html_text.count('class="module"') != 64:
        raise ValueError("HTML program book does not contain exactly 64 modules")
    pdf_text = " ".join("\n".join(page.extract_text() or "" for page in PdfReader(str(PROGRAM_PDF)).pages).split())
    if PROGRAM_TITLE not in pdf_text or not re.search(r"64\.\s+Capstone defense and\s+professional commitment", pdf_text):
        raise ValueError("PDF program book is missing the program title or final module")
    print(f"Synchronized: {PROGRAM_TITLE}, 8 courses, 64 modules, {len(PdfReader(str(PROGRAM_PDF)).pages)}-page program book")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = program_data()
    if args.check:
        check(data)
        return
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    PROGRAM_HTML.write_text(build_html(data), encoding="utf-8")
    build_pdf(data)
    build_package()
    MANIFEST.write_text(json.dumps(build_manifest(data), indent=2) + "\n", encoding="utf-8")
    check(data)


if __name__ == "__main__":
    main()
