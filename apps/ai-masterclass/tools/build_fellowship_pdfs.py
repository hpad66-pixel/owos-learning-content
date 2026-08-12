#!/usr/bin/env python3
"""Build the One Water AI Executive Fellowship curriculum and Fieldbook PDFs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
SYLLABUS = ROOT / "SYLLABUS.md"
COURSE_METADATA = ROOT / "course.yaml"
FIELDBOOK_BLUEPRINT = ROOT / "work-products" / "ONE-WATER-AI-FIELDBOOK-BLUEPRINT.md"
OUTPUT = ROOT / "output" / "pdf"
CURRICULUM_PDF = OUTPUT / "one-water-ai-executive-fellowship-master-curriculum.pdf"
FIELDBOOK_PDF = OUTPUT / "one-water-ai-fieldbook-working-edition.pdf"
SYNC_MANIFEST = OUTPUT / "fellowship-sync-manifest.json"
BUILDER = Path(__file__).resolve()

PROGRAM_TITLE = "One Water AI Executive Fellowship"
EXPECTED_COURSES = 8
EXPECTED_MODULES = 64

PAGE_W, PAGE_H = letter
MARGIN = 54

GRAPHITE = HexColor("#1C1B19")
CHARCOAL = HexColor("#292826")
PROCESS = HexColor("#10232E")
WHITE = HexColor("#F2F1EC")
BODY = HexColor("#D9D6CF")
MUTED = HexColor("#756F66")
WATER = HexColor("#1687B8")
WATER_LIGHT = HexColor("#7DC6E8")
AMBER = HexColor("#E0A64A")
GREEN = HexColor("#2D9B68")
RED = HexColor("#C95D50")
PAPER = HexColor("#F7F5F0")
INK = HexColor("#20201E")
LINE = HexColor("#D8D3C9")
PALE_BLUE = HexColor("#E7F4FA")
PALE_AMBER = HexColor("#FBF2DF")


@dataclass
class Module:
    number: int
    title: str
    learning_job: str
    result: str


@dataclass
class Course:
    number: int
    title: str
    promise: str
    modules: list[Module]


def register_fonts() -> None:
    font_dir = Path("/System/Library/Fonts/Supplemental")
    pdfmetrics.registerFont(TTFont("OWOS", str(font_dir / "Arial.ttf")))
    pdfmetrics.registerFont(TTFont("OWOS-Bold", str(font_dir / "Arial Bold.ttf")))
    pdfmetrics.registerFont(TTFont("OWOS-Italic", str(font_dir / "Arial Italic.ttf")))
    pdfmetrics.registerFont(TTFont("OWOS-Black", str(font_dir / "Arial Black.ttf")))


def parse_syllabus() -> list[Course]:
    text = SYLLABUS.read_text(encoding="utf-8")
    title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    if not title_match or title_match.group(1).strip() != PROGRAM_TITLE:
        raise ValueError(f"The syllabus title must be '{PROGRAM_TITLE}'")
    matches = list(re.finditer(r"^## Course (\d+): (.+)$", text, re.MULTILINE))
    courses: list[Course] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[start:end]
        promise_match = re.search(
            r"### Course promise\s+\n\s*(.+?)(?=\n\n\| Module)", section, re.DOTALL
        )
        promise = " ".join(promise_match.group(1).split()) if promise_match else ""
        modules = []
        for line in section.splitlines():
            module_match = re.match(
                r"\|\s*(\d+)\.\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", line
            )
            if module_match:
                modules.append(
                    Module(
                        number=int(module_match.group(1)),
                        title=module_match.group(2).strip(),
                        learning_job=module_match.group(3).strip(),
                        result=module_match.group(4).strip(),
                    )
                )
        courses.append(
            Course(
                number=int(match.group(1)),
                title=match.group(2).strip(),
                promise=promise,
                modules=modules,
            )
        )
    module_numbers = [module.number for course in courses for module in course.modules]
    if len(courses) != EXPECTED_COURSES or len(module_numbers) != EXPECTED_MODULES:
        raise ValueError(
            f"Expected {EXPECTED_COURSES} courses and {EXPECTED_MODULES} modules in the master syllabus"
        )
    if module_numbers != list(range(1, EXPECTED_MODULES + 1)):
        raise ValueError("Module numbers must be consecutive from 1 through 64")
    return courses


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_control_records(courses: list[Course]) -> None:
    metadata = COURSE_METADATA.read_text(encoding="utf-8")
    blueprint = FIELDBOOK_BLUEPRINT.read_text(encoding="utf-8")
    required_metadata = [
        f"premium_cohort: {PROGRAM_TITLE}",
        f"courses: {EXPECTED_COURSES}",
        f"modules: {EXPECTED_MODULES}",
    ]
    missing_metadata = [item for item in required_metadata if item not in metadata]
    if missing_metadata:
        raise ValueError(f"Course metadata is out of sync: {', '.join(missing_metadata)}")
    if "Each of the 64 modules" not in blueprint:
        raise ValueError("The Fieldbook blueprint must declare the 64-module working rhythm")
    missing_courses = [
        str(course.number)
        for course in courses
        if f"## Course {course.number} Fieldbook records" not in blueprint
    ]
    if missing_courses:
        raise ValueError(
            "The Fieldbook blueprint is missing course record sections: " + ", ".join(missing_courses)
        )


def build_sync_manifest(courses: list[Course]) -> dict[str, object]:
    return {
        "schema": "owos-fellowship-sync/v1",
        "program_title": PROGRAM_TITLE,
        "course_count": len(courses),
        "module_count": sum(len(course.modules) for course in courses),
        "module_range": [1, EXPECTED_MODULES],
        "sources": {
            str(SYLLABUS.relative_to(ROOT)): sha256(SYLLABUS),
            str(COURSE_METADATA.relative_to(ROOT)): sha256(COURSE_METADATA),
            str(FIELDBOOK_BLUEPRINT.relative_to(ROOT)): sha256(FIELDBOOK_BLUEPRINT),
            str(BUILDER.relative_to(ROOT)): sha256(BUILDER),
        },
        "outputs": {
            str(CURRICULUM_PDF.relative_to(ROOT)): {
                "pages": 17,
                "sha256": sha256(CURRICULUM_PDF),
            },
            str(FIELDBOOK_PDF.relative_to(ROOT)): {
                "pages": 143,
                "sha256": sha256(FIELDBOOK_PDF),
            },
        },
    }


def check_sync(courses: list[Course]) -> None:
    if not SYNC_MANIFEST.exists():
        raise ValueError("Synchronization manifest is missing. Rebuild both PDFs together.")
    manifest = json.loads(SYNC_MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("program_title") != PROGRAM_TITLE:
        raise ValueError("The synchronization manifest has the wrong program title")
    if manifest.get("course_count") != len(courses):
        raise ValueError("The synchronization manifest has the wrong course count")
    if manifest.get("module_count") != EXPECTED_MODULES:
        raise ValueError("The synchronization manifest has the wrong module count")
    for relative_path, expected_hash in manifest.get("sources", {}).items():
        path = ROOT / relative_path
        if not path.exists() or sha256(path) != expected_hash:
            raise ValueError(f"Source changed after the last synchronized build: {relative_path}")
    for relative_path, record in manifest.get("outputs", {}).items():
        path = ROOT / relative_path
        if not path.exists() or sha256(path) != record.get("sha256"):
            raise ValueError(f"Output is missing or stale: {relative_path}")


def words(text: str) -> list[str]:
    return text.replace("\n", " ").split()


def wrap(text: str, font: str, size: float, width: float) -> list[str]:
    output: list[str] = []
    current = ""
    for word in words(text):
        candidate = word if not current else f"{current} {word}"
        if pdfmetrics.stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                output.append(current)
            current = word
    if current:
        output.append(current)
    return output or [""]


def draw_wrapped(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str = "OWOS",
    size: float = 10,
    leading: float | None = None,
    color=INK,
    max_lines: int | None = None,
) -> float:
    leading = leading or size * 1.35
    lines = wrap(text, font, size, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    pdf.setFillColor(color)
    pdf.setFont(font, size)
    for line in lines:
        pdf.drawString(x, y, line)
        y -= leading
    return y


def draw_label(pdf: canvas.Canvas, text: str, x: float, y: float, color=WATER) -> None:
    pdf.setFillColor(color)
    pdf.setFont("Courier-Bold", 7.5)
    pdf.drawString(x, y, text.upper())


def draw_drop(pdf: canvas.Canvas, x: float, y: float, scale: float = 1.0, color=WATER) -> None:
    path = pdf.beginPath()
    path.moveTo(x, y + 24 * scale)
    path.curveTo(x - 15 * scale, y + 7 * scale, x - 12 * scale, y - 10 * scale, x, y - 13 * scale)
    path.curveTo(x + 12 * scale, y - 10 * scale, x + 15 * scale, y + 7 * scale, x, y + 24 * scale)
    pdf.setFillColor(color)
    pdf.drawPath(path, fill=1, stroke=0)
    pdf.setFillColor(WHITE)
    pdf.circle(x - 4 * scale, y + 1 * scale, 1.5 * scale, fill=1, stroke=0)
    pdf.circle(x + 4 * scale, y + 1 * scale, 1.5 * scale, fill=1, stroke=0)


def footer(pdf: canvas.Canvas, page_no: int, label: str, dark: bool = False) -> None:
    color = BODY if dark else MUTED
    pdf.setStrokeColor(Color(color.red, color.green, color.blue, alpha=0.4))
    pdf.line(MARGIN, 38, PAGE_W - MARGIN, 38)
    pdf.setFont("Courier", 7)
    pdf.setFillColor(color)
    pdf.drawString(MARGIN, 26, label.upper())
    pdf.drawRightString(PAGE_W - MARGIN, 26, f"{page_no:03d}")


def cover(pdf: canvas.Canvas, title: str, subtitle: str, edition: str) -> None:
    pdf.setFillColor(GRAPHITE)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.setFillColor(PROCESS)
    pdf.circle(PAGE_W + 20, PAGE_H - 55, 220, fill=1, stroke=0)
    pdf.setStrokeColor(Color(WATER_LIGHT.red, WATER_LIGHT.green, WATER_LIGHT.blue, alpha=0.28))
    for radius in (90, 130, 170):
        pdf.circle(PAGE_W - 45, PAGE_H - 75, radius, fill=0, stroke=1)
    draw_drop(pdf, 74, PAGE_H - 86, 1.05, WATER)
    draw_label(pdf, "One Water Operating System", 104, PAGE_H - 77, WATER_LIGHT)
    pdf.setFillColor(WHITE)
    pdf.setFont("OWOS-Black", 34)
    y = PAGE_H - 205
    for line in wrap(title, "OWOS-Black", 34, PAGE_W - 108):
        pdf.drawString(MARGIN, y, line)
        y -= 42
    y -= 8
    y = draw_wrapped(pdf, subtitle, MARGIN, y, PAGE_W - 140, "OWOS", 16, 23, BODY)
    pdf.setFillColor(AMBER)
    pdf.rect(MARGIN, y - 35, 58, 5, fill=1, stroke=0)
    draw_label(pdf, edition, MARGIN, 78, AMBER)
    pdf.setFillColor(BODY)
    pdf.setFont("OWOS", 9)
    pdf.drawString(MARGIN, 57, "Built for water, wastewater, stormwater, and One Water leadership")
    pdf.setFillColor(WATER_LIGHT)
    pdf.drawRightString(PAGE_W - MARGIN, 57, "Powered by APAS.AI")
    pdf.showPage()


def prospectus_header(pdf: canvas.Canvas, page_no: int, section: str) -> None:
    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_drop(pdf, MARGIN + 8, PAGE_H - 42, 0.42, WATER)
    pdf.setFillColor(INK)
    pdf.setFont("OWOS-Bold", 8)
    pdf.drawString(MARGIN + 28, PAGE_H - 39, "ONE WATER AI EXECUTIVE FELLOWSHIP")
    draw_label(pdf, section, PAGE_W - MARGIN - 170, PAGE_H - 39, WATER)
    footer(pdf, page_no, "One Water AI Executive Fellowship")


def section_title(pdf: canvas.Canvas, kicker: str, title: str, y: float = PAGE_H - 100) -> float:
    draw_label(pdf, kicker, MARGIN, y, WATER)
    y -= 28
    pdf.setFillColor(INK)
    pdf.setFont("OWOS-Black", 25)
    for line in wrap(title, "OWOS-Black", 25, PAGE_W - 2 * MARGIN):
        pdf.drawString(MARGIN, y, line)
        y -= 31
    return y - 8


def card(pdf: canvas.Canvas, x: float, y: float, w: float, h: float, title: str, body: str, accent=WATER) -> None:
    pdf.setFillColor(WHITE)
    pdf.roundRect(x, y - h, w, h, 8, fill=1, stroke=0)
    pdf.setStrokeColor(LINE)
    pdf.roundRect(x, y - h, w, h, 8, fill=0, stroke=1)
    pdf.setFillColor(accent)
    pdf.rect(x, y - h, 4, h, fill=1, stroke=0)
    draw_label(pdf, title, x + 15, y - 21, accent)
    draw_wrapped(pdf, body, x + 15, y - 40, w - 30, "OWOS", 9.2, 12.3, INK)


def build_prospectus(courses: list[Course], output_path: Path) -> None:
    pdf = canvas.Canvas(str(output_path), pagesize=letter)
    pdf.setTitle("One Water AI Executive Fellowship: Master Curriculum")
    pdf.setAuthor("APAS.AI and One Water Operating System")
    pdf.setSubject("24-week executive fellowship curriculum for water-sector AI leadership")
    cover(
        pdf,
        "One Water AI Executive Fellowship",
        "Master curriculum, program value, participant experience, and implementation portfolio",
        "Master curriculum candidate | August 2026",
    )
    page = 2

    prospectus_header(pdf, page, "The proposition")
    y = section_title(pdf, "The problem we are solving", "AI fluency is not the finish line.")
    y = draw_wrapped(
        pdf,
        "The water sector needs professionals who can separate a demonstration from a defensible utility application. The work begins with technology, but it has to reach data, knowledge, governance, people, economics, and accountable decisions.",
        MARGIN,
        y,
        PAGE_W - 2 * MARGIN,
        "OWOS",
        13,
        19,
        INK,
    )
    y -= 22
    card(pdf, MARGIN, y, 230, 116, "What the participant learns", "Explain the technology, test the evidence, identify useful applications, design controls, and lead a bounded pilot.", WATER)
    card(pdf, MARGIN + 250, y, 230, 116, "What the organization receives", "A prioritized opportunity portfolio, governance record, investment case, 90-day pilot brief, and one-year roadmap.", GREEN)
    y -= 145
    card(pdf, MARGIN, y, 480, 98, "The promise", "Move one meaningful utility opportunity from enthusiasm to a source-backed, governed, measurable pilot that leadership can understand, challenge, fund, or stop.", AMBER)
    pdf.showPage()
    page += 1

    prospectus_header(pdf, page, "Program at a glance")
    y = section_title(pdf, "Six months of applied learning", "Eight courses. Sixty-four modules. One implementation portfolio.")
    facts = [
        ("24", "weeks"),
        ("132", "guided hours"),
        ("25", "participants per cohort"),
        ("$10K", "target tuition"),
    ]
    x = MARGIN
    for number, label in facts:
        pdf.setFillColor(WHITE)
        pdf.roundRect(x, y - 94, 110, 84, 8, fill=1, stroke=0)
        pdf.setStrokeColor(LINE)
        pdf.roundRect(x, y - 94, 110, 84, 8, fill=0, stroke=1)
        pdf.setFillColor(WATER)
        pdf.setFont("OWOS-Black", 24)
        pdf.drawString(x + 13, y - 42, number)
        draw_label(pdf, label, x + 13, y - 67, MUTED)
        x += 123
    y -= 124
    draw_label(pdf, "Learning system", MARGIN, y, WATER)
    y -= 27
    flow = ["Articulate modules", "Live executive forums", "Applied studios", "OWOS knowledge graph", "Fieldbook", "Capstone defense"]
    for index, item in enumerate(flow, 1):
        pdf.setFillColor(PROCESS if index % 2 else CHARCOAL)
        pdf.roundRect(MARGIN, y - 43, 480, 35, 6, fill=1, stroke=0)
        pdf.setFillColor(WATER_LIGHT)
        pdf.setFont("Courier-Bold", 8)
        pdf.drawString(MARGIN + 14, y - 30, f"{index:02d}")
        pdf.setFillColor(WHITE)
        pdf.setFont("OWOS-Bold", 10)
        pdf.drawString(MARGIN + 50, y - 30, item)
        y -= 43
    pdf.showPage()
    page += 1

    prospectus_header(pdf, page, "Who should attend")
    y = section_title(pdf, "A selected professional cohort", "Built for people who influence consequential decisions.")
    audiences = [
        "General managers, executive directors, and deputy directors",
        "Operations, maintenance, engineering, and water-quality leaders",
        "Capital, asset, customer, finance, and communications leaders",
        "Data, technology, cybersecurity, innovation, and transformation officers",
        "Legal, privacy, procurement, risk, audit, and governance professionals",
        "Senior consultants, solution providers, researchers, regulators, and nonprofit leaders",
        "Selected emerging leaders with sponsor support and a real application context",
    ]
    for item in audiences:
        pdf.setFillColor(PALE_BLUE)
        pdf.circle(MARGIN + 6, y - 4, 6, fill=1, stroke=0)
        pdf.setFillColor(WATER)
        pdf.setFont("OWOS-Bold", 8)
        pdf.drawCentredString(MARGIN + 6, y - 7, "+")
        y = draw_wrapped(pdf, item, MARGIN + 22, y, 455, "OWOS", 11, 15, INK)
        y -= 10
    y -= 5
    card(pdf, MARGIN, y, 480, 92, "Admissions expectation", "Programming is not required. Participants need a real professional context, organizational support, and the authority or influence to complete an applied capstone.", AMBER)
    pdf.showPage()
    page += 1

    prospectus_header(pdf, page, "Program map")
    y = section_title(pdf, "The six-month sequence", "From shared language to a governed pilot.")
    for course in courses:
        weeks_start = 1 + (course.number - 1) * 3
        weeks_end = weeks_start + 2
        pdf.setFillColor(PROCESS if course.number % 2 else CHARCOAL)
        pdf.roundRect(MARGIN, y - 64, 480, 54, 8, fill=1, stroke=0)
        pdf.setFillColor(WATER_LIGHT)
        pdf.setFont("OWOS-Black", 18)
        pdf.drawString(MARGIN + 13, y - 42, f"{course.number:02d}")
        pdf.setFillColor(WHITE)
        pdf.setFont("OWOS-Bold", 11)
        pdf.drawString(MARGIN + 58, y - 30, course.title)
        pdf.setFillColor(BODY)
        pdf.setFont("OWOS", 8)
        pdf.drawString(MARGIN + 58, y - 46, f"Weeks {weeks_start} to {weeks_end} | Modules {course.modules[0].number} to {course.modules[-1].number}")
        y -= 64
    pdf.showPage()
    page += 1

    for course in courses:
        prospectus_header(pdf, page, f"Course {course.number}")
        y = section_title(pdf, f"Weeks {1 + (course.number - 1) * 3} to {3 + (course.number - 1) * 3}", course.title)
        y = draw_wrapped(pdf, course.promise, MARGIN, y, 480, "OWOS", 11.2, 16, INK)
        y -= 18
        draw_label(pdf, "Eight applied modules", MARGIN, y, WATER)
        y -= 20
        for module in course.modules:
            pdf.setFillColor(WHITE)
            pdf.roundRect(MARGIN, y - 52, 480, 46, 6, fill=1, stroke=0)
            pdf.setStrokeColor(LINE)
            pdf.roundRect(MARGIN, y - 52, 480, 46, 6, fill=0, stroke=1)
            pdf.setFillColor(WATER)
            pdf.setFont("OWOS-Black", 12)
            pdf.drawString(MARGIN + 12, y - 27, f"{module.number:02d}")
            pdf.setFillColor(INK)
            pdf.setFont("OWOS-Bold", 9.2)
            pdf.drawString(MARGIN + 47, y - 21, module.title[:70])
            pdf.setFillColor(MUTED)
            pdf.setFont("OWOS", 7.6)
            result = f"Keep: {module.result}"
            pdf.drawString(MARGIN + 47, y - 37, result[:92])
            y -= 52
        pdf.showPage()
        page += 1

    prospectus_header(pdf, page, "The Fieldbook")
    y = section_title(pdf, "The companion product", "Learning that accumulates into professional work.")
    y = draw_wrapped(pdf, "The One Water AI Fieldbook is part workbook, part laboratory notebook, part decision record, and part executive playbook. Each module adds one useful artifact. At graduation, those artifacts form a complete implementation portfolio.", MARGIN, y, 480, "OWOS", 12, 18, INK)
    y -= 18
    fieldbook_items = [
        "AI use-case boundary and terms field card",
        "Data and knowledge readiness map",
        "Claude Skill package and Utility Agent Canvas",
        "Prioritized utility opportunity portfolio",
        "Governance, permissions, evaluation, and procurement records",
        "Investment case, workforce plan, and operating model",
        "Tested prototype evidence package",
        "90-day pilot brief and one-year roadmap",
    ]
    for index, item in enumerate(fieldbook_items, 1):
        card(pdf, MARGIN + ((index - 1) % 2) * 247, y - ((index - 1) // 2) * 90, 233, 76, f"Record {index}", item, WATER if index < 5 else GREEN)
    pdf.showPage()
    page += 1

    prospectus_header(pdf, page, "Capstone")
    y = section_title(pdf, "The proof of learning", "A pilot that can be understood, challenged, measured, and stopped.")
    capstone = [
        "Problem, current process, affected people, and baseline",
        "Accountable sponsor, owner, reviewers, users, and decision rights",
        "Approved sources, data limitations, definitions, and provenance",
        "Architecture decision and reason simpler alternatives were rejected",
        "Permissions, controls, review, incident, and escalation design",
        "Historical test cases, thresholds, cost limits, and human-review effort",
        "Ninety-day pilot sequence and one-year adoption roadmap",
        "Candid statement of what remains unknown",
    ]
    for index, item in enumerate(capstone, 1):
        pdf.setFillColor(PALE_AMBER if index in (4, 8) else PALE_BLUE)
        pdf.roundRect(MARGIN, y - 50, 480, 40, 6, fill=1, stroke=0)
        pdf.setFillColor(AMBER if index in (4, 8) else WATER)
        pdf.setFont("OWOS-Black", 13)
        pdf.drawString(MARGIN + 12, y - 34, f"{index:02d}")
        draw_wrapped(pdf, item, MARGIN + 50, y - 25, 415, "OWOS", 9.4, 12, INK, 2)
        y -= 50
    pdf.showPage()
    page += 1

    prospectus_header(pdf, page, "Release boundary")
    y = section_title(pdf, "What is built, and what remains", "The blueprint is complete. The fellowship still has to earn release.")
    card(pdf, MARGIN, y, 233, 196, "Built now", "A 24-week architecture, 64-module curriculum, premium value proposition, Fieldbook system, applied capstone, free-resource strategy, source controls, and the first module authoring package.", GREEN)
    card(pdf, MARGIN + 247, y, 233, 196, "Required before enrollment", "Faculty and practitioner review, source rights, 64 Articulate lessons, live-studio plans, the completed Fieldbook, assessment and credential controls, design-cohort evidence, accessibility review, and delivery integration.", AMBER)
    y -= 225
    card(pdf, MARGIN, y, 480, 112, "Credential boundary", "Completion does not authorize engineering, operations, regulation, finance, procurement, or security decisions. Any fellowship credential remains disabled until identity, evidence, assessment, review, and issuance gates are independently approved.", RED)
    pdf.showPage()
    page += 1

    prospectus_header(pdf, page, "References")
    y = section_title(pdf, "Curriculum comparison sources", "External programs informed the gap assessment, not the utility content.")
    refs = [
        ("MIT Sloan AI Executive Academy", "https://executive.mit.edu/ai-executive-academy.html"),
        ("MIT Sloan AI Essentials", "https://executive.mit.edu/ai-essentials.html"),
        ("Anthropic: The Complete Guide to Building Skills for Claude", "https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf"),
    ]
    for title, url in refs:
        draw_label(pdf, title, MARGIN, y, WATER)
        y = draw_wrapped(pdf, url, MARGIN, y - 18, 480, "Courier", 8, 11, INK)
        y -= 22
    card(pdf, MARGIN, y, 480, 96, "Source boundary", "These public references support curriculum comparison only. They do not provide authority for utility operations, and no third-party course content is reproduced in this document.", AMBER)
    pdf.showPage()
    pdf.save()


def fieldbook_header(pdf: canvas.Canvas, page_no: int, course: Course | None = None) -> None:
    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_drop(pdf, MARGIN + 6, PAGE_H - 35, 0.32, WATER)
    pdf.setFillColor(INK)
    pdf.setFont("OWOS-Bold", 7.5)
    pdf.drawString(MARGIN + 23, PAGE_H - 33, "THE ONE WATER AI FIELDBOOK")
    if course:
        draw_label(pdf, f"Course {course.number}: {course.title}", PAGE_W - MARGIN - 220, PAGE_H - 33, WATER)


def ruled_box(pdf: canvas.Canvas, x: float, y: float, w: float, h: float, title: str, prompt: str, accent=WATER, lines: int = 5) -> None:
    pdf.setFillColor(WHITE)
    pdf.roundRect(x, y - h, w, h, 8, fill=1, stroke=0)
    pdf.setStrokeColor(LINE)
    pdf.roundRect(x, y - h, w, h, 8, fill=0, stroke=1)
    pdf.setFillColor(accent)
    pdf.rect(x, y - 5, w, 5, fill=1, stroke=0)
    draw_label(pdf, title, x + 14, y - 23, accent)
    prompt_y = draw_wrapped(pdf, prompt, x + 14, y - 42, w - 28, "OWOS", 9.2, 12.5, INK, 4)
    line_top = min(prompt_y - 8, y - 76)
    available = line_top - (y - h + 16)
    line_count = max(1, min(lines, int(available / 20)))
    if line_count:
        gap = available / line_count
        pdf.setStrokeColor(HexColor("#C9C4BA"))
        for index in range(line_count):
            line_y = line_top - gap * index
            pdf.line(x + 14, line_y, x + w - 14, line_y)


def course_divider(pdf: canvas.Canvas, course: Course, page_no: int) -> None:
    pdf.setFillColor(GRAPHITE)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.setFillColor(PROCESS)
    pdf.circle(PAGE_W - 50, PAGE_H - 180, 170, fill=1, stroke=0)
    pdf.setStrokeColor(Color(WATER_LIGHT.red, WATER_LIGHT.green, WATER_LIGHT.blue, alpha=0.28))
    for radius in (65, 100, 135):
        pdf.circle(PAGE_W - 70, PAGE_H - 190, radius, fill=0, stroke=1)
    draw_label(pdf, f"Course {course.number} | Modules {course.modules[0].number} to {course.modules[-1].number}", MARGIN, PAGE_H - 92, WATER_LIGHT)
    pdf.setFillColor(WHITE)
    pdf.setFont("OWOS-Black", 29)
    y = PAGE_H - 145
    for line in wrap(course.title, "OWOS-Black", 29, 440):
        pdf.drawString(MARGIN, y, line)
        y -= 36
    y -= 14
    y = draw_wrapped(pdf, course.promise, MARGIN, y, 430, "OWOS", 14, 21, BODY)
    y -= 32
    draw_label(pdf, "This course adds", MARGIN, y, AMBER)
    y -= 23
    for module in course.modules:
        pdf.setFillColor(WHITE)
        pdf.setFont("OWOS-Bold", 9)
        pdf.drawString(MARGIN, y, f"{module.number:02d}  {module.result}")
        y -= 20
    footer(pdf, page_no, "The One Water AI Fieldbook", dark=True)
    pdf.showPage()


def module_spread(pdf: canvas.Canvas, course: Course, module: Module, page_no: int) -> int:
    fieldbook_header(pdf, page_no, course)
    draw_label(pdf, f"Module {module.number:02d}", MARGIN, PAGE_H - 77, WATER)
    pdf.setFillColor(INK)
    pdf.setFont("OWOS-Black", 21)
    y = PAGE_H - 105
    for line in wrap(module.title, "OWOS-Black", 21, 480):
        pdf.drawString(MARGIN, y, line)
        y -= 26
    y -= 5
    draw_wrapped(pdf, module.learning_job, MARGIN, y, 480, "OWOS", 10.5, 15, MUTED, 3)
    ruled_box(pdf, MARGIN, y - 66, 480, 150, "Before", "What do I believe now? What decision would I make before the lesson, and what evidence would I use?", WATER, 5)
    ruled_box(pdf, MARGIN, y - 232, 232, 210, "Learn", "What relationship, mechanism, distinction, or consequence changed my understanding?", WATER, 7)
    ruled_box(pdf, MARGIN + 248, y - 232, 232, 210, "Questions", "What remains unclear? Which claim, source, example, or assumption do I need to test?", AMBER, 7)
    footer(pdf, page_no, f"Module {module.number:02d} | Before and learn")
    pdf.showPage()
    page_no += 1

    fieldbook_header(pdf, page_no, course)
    draw_label(pdf, f"Module {module.number:02d} | Apply and keep", MARGIN, PAGE_H - 77, GREEN)
    pdf.setFillColor(INK)
    pdf.setFont("OWOS-Black", 19)
    pdf.drawString(MARGIN, PAGE_H - 107, "Turn the idea into a professional record.")
    ruled_box(pdf, MARGIN, PAGE_H - 139, 480, 154, "Apply", f"Where does this appear in my organization? Use one real task, decision, record, role, asset, or consequence. Learning job: {module.learning_job}", GREEN, 5)
    ruled_box(pdf, MARGIN, PAGE_H - 309, 480, 180, "Keep", f"Add this record to the implementation portfolio: {module.result}.", WATER, 7)
    y = PAGE_H - 510
    mini_w = 150
    prompts = [
        ("Evidence", "What source or observation supports this?"),
        ("Owner", "Who remains accountable?"),
        ("Next action", "What will I test, ask, change, or stop?"),
    ]
    for index, (title, prompt) in enumerate(prompts):
        ruled_box(pdf, MARGIN + index * 165, y, mini_w, 112, title, prompt, AMBER if index == 2 else WATER, 2)
    pdf.setFillColor(PALE_BLUE)
    pdf.roundRect(MARGIN, 65, 480, 42, 6, fill=1, stroke=0)
    draw_label(pdf, "Completion check", MARGIN + 12, 91, WATER)
    pdf.setFont("OWOS", 8.5)
    pdf.setFillColor(INK)
    pdf.drawString(MARGIN + 138, 88, "[ ] lesson  [ ] activity  [ ] record  [ ] reflection  [ ] ready for review")
    footer(pdf, page_no, f"Module {module.number:02d} | Apply and keep")
    pdf.showPage()
    return page_no + 1


def build_fieldbook(courses: list[Course], output_path: Path) -> None:
    pdf = canvas.Canvas(str(output_path), pagesize=letter)
    pdf.setTitle("The One Water AI Fieldbook")
    pdf.setAuthor("APAS.AI and One Water Operating System")
    pdf.setSubject("Participant working edition for the One Water AI Executive Fellowship")
    cover(
        pdf,
        "The One Water AI Fieldbook",
        "From first question to a governed utility pilot",
        "Participant working edition 0.1 | 64-module portfolio",
    )
    page = 2

    fieldbook_header(pdf, page)
    y = section_title(pdf, "This Fieldbook belongs to", "Your work. Your evidence. Your implementation record.")
    ruled_box(pdf, MARGIN, y, 480, 118, "Participant", "Name, role, organization, and preferred contact information.", WATER, 4)
    ruled_box(pdf, MARGIN, y - 134, 480, 150, "My professional objective", "What do I need to understand, decide, build, improve, or prevent during the next six months?", GREEN, 5)
    ruled_box(pdf, MARGIN, y - 300, 480, 130, "My sponsor and peer", "Who supports this work, and who will challenge my assumptions honestly?", AMBER, 4)
    footer(pdf, page, "Participant identity and purpose")
    pdf.showPage()
    page += 1

    fieldbook_header(pdf, page)
    y = section_title(pdf, "Private by design", "Do not put protected utility information into a course workbook.")
    y = draw_wrapped(pdf, "Use generalized examples when a real record contains security-sensitive, personal, confidential, privileged, client, procurement, personnel, or operational information. The Fieldbook helps you reason about the work. It is not an approved repository for protected records.", MARGIN, y, 480, "OWOS", 11.5, 17, INK)
    y -= 22
    ruled_box(pdf, MARGIN, y, 480, 158, "My confidentiality boundary", "What information, systems, facilities, people, clients, security details, or records must I never enter or upload?", RED, 6)
    ruled_box(pdf, MARGIN, y - 174, 480, 145, "My safe working substitute", "How will I generalize, redact, synthesize, or obtain approval for examples used in learning?", GREEN, 5)
    footer(pdf, page, "Confidentiality boundary")
    pdf.showPage()
    page += 1

    fieldbook_header(pdf, page)
    y = section_title(pdf, "How to use the Fieldbook", "Every module leaves something useful behind.")
    rhythm = [
        ("Before", "State what you believe and what you would decide before the lesson."),
        ("Learn", "Record the relationship, mechanism, distinction, or consequence that matters."),
        ("Apply", "Connect the idea to one real utility task, role, asset, record, or decision."),
        ("Keep", "Add one durable record to your implementation portfolio."),
    ]
    for index, (title, body) in enumerate(rhythm):
        card(pdf, MARGIN, y - index * 105, 480, 88, f"{index + 1:02d} | {title}", body, [WATER, WATER_LIGHT, GREEN, AMBER][index])
    footer(pdf, page, "The four-part working rhythm")
    pdf.showPage()
    page += 1

    fieldbook_header(pdf, page)
    y = section_title(pdf, "Starting point", "Record the baseline before the curriculum changes your answers.")
    ruled_box(pdf, MARGIN, y, 232, 188, "Current fluency", "What can I explain today about models, prompts, retrieval, knowledge graphs, skills, agents, and governance?", WATER, 7)
    ruled_box(pdf, MARGIN + 248, y, 232, 188, "Current practice", "Where is my organization already using, testing, buying, or discussing AI?", GREEN, 7)
    ruled_box(pdf, MARGIN, y - 205, 232, 188, "Current concern", "What could go wrong technically, professionally, organizationally, or publicly?", RED, 7)
    ruled_box(pdf, MARGIN + 248, y - 205, 232, 188, "Current opportunity", "What work is slow, fragmented, repetitive, difficult to retrieve, or hard to defend?", AMBER, 7)
    footer(pdf, page, "Baseline reflection")
    pdf.showPage()
    page += 1

    for course in courses:
        course_divider(pdf, course, page)
        page += 1
        for module in course.modules:
            page = module_spread(pdf, course, module, page)

    fieldbook_header(pdf, page)
    y = section_title(pdf, "Capstone portfolio", "Assemble the record. Do not hide the unknowns.")
    items = [
        "Executive summary and utility problem",
        "Current process and baseline",
        "Opportunity portfolio and selected use case",
        "Data, knowledge, sources, and limitations",
        "Architecture decision and alternatives",
        "Governance, security, permissions, and human authority",
        "Evaluation, economics, and success measures",
        "Workforce and operating-model implications",
        "Ninety-day pilot brief",
        "One-year roadmap",
        "Unresolved questions and next accountable decision",
    ]
    for index, item in enumerate(items, 1):
        pdf.setFillColor(WHITE)
        pdf.roundRect(MARGIN, y - 39, 480, 31, 5, fill=1, stroke=0)
        pdf.setStrokeColor(LINE)
        pdf.roundRect(MARGIN, y - 39, 480, 31, 5, fill=0, stroke=1)
        pdf.setFont("OWOS-Bold", 9)
        pdf.setFillColor(WATER)
        pdf.drawString(MARGIN + 11, y - 28, f"[ ] {index:02d}")
        pdf.setFillColor(INK)
        pdf.drawString(MARGIN + 62, y - 28, item)
        y -= 39
    footer(pdf, page, "Capstone portfolio checklist")
    pdf.showPage()
    page += 1

    fieldbook_header(pdf, page)
    y = section_title(pdf, "Six months later", "What can I now explain, decide, build, and stop?")
    ruled_box(pdf, MARGIN, y, 480, 148, "Recognition", "What do I see now that I did not see at the beginning?", WATER, 5)
    ruled_box(pdf, MARGIN, y - 164, 480, 148, "Professional judgment", "Which decision can I make more clearly, and what evidence will I require?", GREEN, 5)
    ruled_box(pdf, MARGIN, y - 328, 480, 148, "Next accountable action", "What happens in the next three hours, the next 30 days, and the next 90 days?", AMBER, 5)
    footer(pdf, page, "Final reflection")
    pdf.showPage()
    pdf.save()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the curriculum, Fieldbook, metadata, builder, or PDFs are out of sync.",
    )
    args = parser.parse_args()
    courses = parse_syllabus()
    validate_control_records(courses)
    if args.check:
        check_sync(courses)
        print(f"Synchronized: {PROGRAM_TITLE}, {len(courses)} courses, {EXPECTED_MODULES} modules")
        return

    register_fonts()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    build_prospectus(courses, CURRICULUM_PDF)
    build_fieldbook(courses, FIELDBOOK_PDF)
    manifest = build_sync_manifest(courses)
    SYNC_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(courses)} courses and {sum(len(c.modules) for c in courses)} modules")
    print(CURRICULUM_PDF)
    print(FIELDBOOK_PDF)
    print(SYNC_MANIFEST)


if __name__ == "__main__":
    main()
