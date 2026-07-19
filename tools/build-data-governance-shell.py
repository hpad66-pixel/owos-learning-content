#!/usr/bin/env python3
"""Build the governed Data Governance course shell from its canonical syllabus.

The shell makes the complete curriculum structure reviewable without claiming
that placeholder chapters are finished lessons. Source pages keep shared core
links for authoring. Distribution pages inline the core for OWOS.ai delivery.

Usage:
  python3 tools/build-data-governance-shell.py
  python3 tools/build-data-governance-shell.py --check
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import pathlib
import re
import sys
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parents[1]
APP = ROOT / "apps/data-ai-governance"
CURRICULUM = APP / "curriculum"
DIST = APP / "dist/site"
SYLLABUS = CURRICULUM / "SYLLABUS.md"
COURSE_ID = "owos-master-data-governance-001"
STORE_KEY = "dga001"
COURSE_TITLE = "Data Before AI: Data and Artificial Intelligence Governance for Utilities"
COURSE_SOURCE = "masterclass-data-governance.html"
COURSE_OUTPUT = "course-data-governance.html"
RELEASED_CHAPTERS = {"00", "01", "02", "03", "04", "05"}
SHELL_VERSION = "0.21.0"

CORE_CSS = (ROOT / "core/components/academy.css").read_text(encoding="utf-8")
CORE_JS = (ROOT / "core/components/academy.js").read_text(encoding="utf-8")
DROOBI_SVG = (ROOT / "core/brand/droobi.svg").read_bytes()


@dataclass(frozen=True)
class Section:
    title: str
    body: str


@dataclass(frozen=True)
class Chapter:
    number: str
    title: str
    part_code: str
    part_title: str
    chapter_type: str
    sections: tuple[Section, ...]
    learner_can: str
    riverbend: str
    studio: str
    output: str

    @property
    def slug(self) -> str:
        value = self.title.lower().replace("artificial intelligence", "ai")
        value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
        return value

    @property
    def source_name(self) -> str:
        return f"module-{self.number}-{self.slug}.html"

    @property
    def output_name(self) -> str:
        return f"lesson-dg-{self.number}-{self.slug}.html"


def clean(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value.replace("—", "-").replace("–", "-")


def inline(value: str) -> str:
    safe = html.escape(clean(value), quote=True)
    safe = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"`(.+?)`", r"<code>\1</code>", safe)
    return safe


def parse_syllabus() -> list[Chapter]:
    text = SYLLABUS.read_text(encoding="utf-8")
    part_matches = list(
        re.finditer(r"^# (ORIENTATION|PART [A-Z]) \| (.+)$", text, flags=re.MULTILINE)
    )
    chapter_matches = list(
        re.finditer(
            r"^## Chapter (\d{2}) \| (.+?)\n(.*?)(?=\n## Chapter|\n---(?:\n|$)|\n# (?:PART|APPLIED)|\Z)",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
    )
    chapters: list[Chapter] = []
    for match in chapter_matches:
        number, title, body = match.groups()
        part = max((p for p in part_matches if p.start() < match.start()), key=lambda p: p.start())
        section_block = re.search(
            r"\*\*Sections:\*\*\s*(.*?)(?=\n\*\*Learner can:\*\*)",
            body,
            flags=re.DOTALL,
        )
        if not section_block:
            raise ValueError(f"Chapter {number} has no Sections block")
        section_matches = re.findall(
            r"\d+\. \*\*(.+?)\*\*\s*(.*?)(?=\n\d+\. \*\*|\Z)",
            section_block.group(1),
            flags=re.DOTALL,
        )
        if len(section_matches) != 3:
            raise ValueError(f"Chapter {number} has {len(section_matches)} sections; expected 3")

        def field(label: str) -> str:
            field_match = re.search(
                rf"\*\*{re.escape(label)}:\*\*\s*(.*?)(?=\n\*\*[^\n]+:\*\*|\Z)",
                body,
                flags=re.DOTALL,
            )
            if not field_match:
                raise ValueError(f"Chapter {number} is missing {label}")
            return clean(field_match.group(1))

        type_match = re.search(r"\*\*Type:\*\*\s*(.+)", body)
        chapters.append(
            Chapter(
                number=number,
                title=clean(title),
                part_code=part.group(1),
                part_title=clean(part.group(2)),
                chapter_type=clean(type_match.group(1)) if type_match else "Core",
                sections=tuple(Section(clean(a), clean(b)) for a, b in section_matches),
                learner_can=field("Learner can"),
                riverbend=field("Riverbend case"),
                studio=field("Deployment Studio"),
                output=field("Output"),
            )
        )
    if len(chapters) != 25 or [c.number for c in chapters] != [f"{n:02d}" for n in range(25)]:
        raise ValueError("The governed syllabus must contain Chapters 00 through 24")
    return chapters


def logo() -> str:
    return """<span class="owos-logo"><svg width="20" height="20" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 6C32 6 13 30 13 43a19 19 0 0 0 38 0C51 30 32 6 32 6Z" fill="#fff"/></svg></span>"""


def head(title: str, description: str, release_state: str = "structure-ready-content-pending") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} &middot; One Water OS Academy</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<meta name="owos-course-id" content="{COURSE_ID}">
<meta name="owos-course-store" content="{STORE_KEY}">
<meta name="owos-release-state" content="{html.escape(release_state, quote=True)}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath d='M32 5C32 5 12 30 12 43a20 20 0 0 0 40 0C52 30 32 5 32 5Z' fill='%230A78BA'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../../core/components/academy.css">
<style>{SHELL_CSS}</style>
</head>"""


SHELL_CSS = """
html,body{max-width:100%;overflow-x:hidden}
.dg-hero{margin:28px 0 24px;padding:32px;border-radius:24px;background:linear-gradient(135deg,#083a5c,#0a78ba 62%,#15937a);color:#fff;box-shadow:0 20px 60px rgba(8,58,92,.2);overflow:hidden;position:relative}
.dg-hero:after{content:"";position:absolute;width:280px;height:280px;border:54px solid rgba(255,255,255,.08);border-radius:50%;right:-105px;top:-110px}
.dg-hero h1{color:#fff;max-width:19ch;margin:.45rem 0 .8rem;font-size:clamp(2.15rem,5vw,4rem)}
.dg-hero p{color:#e8f5fb;max-width:68ch;font-size:1.08rem;margin:0}
.dg-eyebrow{font:700 11px var(--fm);letter-spacing:.13em;text-transform:uppercase;color:#bfeaff}
.dg-status{display:inline-flex;align-items:center;gap:8px;max-width:100%;margin-top:18px;padding:7px 12px;border:1px solid rgba(255,255,255,.28);background:rgba(255,255,255,.1);border-radius:999px;font:700 11px var(--fm);line-height:1.45;letter-spacing:.04em;text-transform:uppercase;color:#fff;white-space:normal}
.dg-status i{width:8px;height:8px;border-radius:50%;background:#f2c94c}
.dg-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:18px 0 28px}.dg-stat{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px;box-shadow:var(--sh)}.dg-stat b{display:block;color:var(--ink);font-size:1.55rem}.dg-stat span{font:600 10px var(--fm);text-transform:uppercase;letter-spacing:.08em;color:var(--ink-3)}
.dg-note{border:1px solid #ead89d;background:#fff9e8;border-radius:16px;padding:18px 20px;margin:20px 0}.dg-note strong{color:#795809}.dg-note p{margin:4px 0 0}
.dg-flow{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:18px 0 30px}.dg-flow div{position:relative;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 12px;font-size:12px;font-weight:700;color:var(--ink);text-align:center}.dg-flow div:not(:last-child):after{content:"→";position:absolute;right:-11px;top:50%;z-index:2;color:var(--brand);transform:translateY(-50%);background:var(--bg);padding:0 3px}
.dg-lenses{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0 28px}.dg-lens{padding:18px;border-radius:14px;background:#fff;border:1px solid var(--line);border-top:4px solid var(--brand)}.dg-lens:nth-child(2){border-top-color:var(--green)}.dg-lens:nth-child(3){border-top-color:var(--gold)}.dg-lens h3{margin:0 0 5px;font-size:1rem}.dg-lens p{margin:0;font-size:.88rem;line-height:1.55}
.dg-part{margin:24px 0}.dg-part-head{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;background:#0b3f63;color:#fff;border-radius:14px 14px 0 0;padding:13px 16px}.dg-part-head b{font:700 11px var(--fm);letter-spacing:.1em;color:#9bddff}.dg-part-head span{font-weight:800}.dg-part-head small{margin-left:auto;color:#cce4f2}.dg-list{border:1px solid var(--line);border-top:0;background:#fff;border-radius:0 0 14px 14px;overflow:hidden}.dg-row{display:grid;grid-template-columns:48px 1fr auto;gap:14px;padding:16px;align-items:start;border-bottom:1px solid var(--line);text-decoration:none}.dg-row:last-child{border-bottom:0}.dg-row:hover{background:var(--brand-50);text-decoration:none}.dg-num{width:42px;height:42px;border-radius:11px;background:var(--brand-50);border:1px solid var(--brand-100);display:grid;place-items:center;color:var(--brand-700);font:800 13px var(--fm)}.dg-row h3{margin:0 0 5px;font-size:1rem}.dg-sections{font-size:.79rem;color:var(--ink-3);line-height:1.5}.dg-pill{font:700 9px var(--fm);text-transform:uppercase;letter-spacing:.06em;color:#7a5c13;background:#fff7df;border:1px solid #ead89d;padding:5px 9px;border-radius:999px;white-space:nowrap}
.dg-row.released{background:linear-gradient(90deg,#eef8f5,#fff)}.dg-row.released .dg-num{background:#dff3ec;border-color:#9fd2bf;color:#086b50}.dg-row.released .dg-pill{color:#086b50;background:#eaf8f3;border-color:#9fd2bf}
.dg-shell{border:1px solid #ead89d;background:linear-gradient(120deg,#fff9e8,#fff);border-radius:16px;padding:20px;margin:18px 0 26px;display:flex;gap:14px}.dg-shell-icon{width:40px;height:40px;flex:none;border-radius:12px;background:#f2c94c;display:grid;place-items:center;color:#493800;font-weight:900}.dg-shell h2{font-size:1.05rem;margin:0 0 4px}.dg-shell p{margin:0;font-size:.91rem}
.dg-plan{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:18px 0 28px}.dg-plan-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px}.dg-plan-card .k{font:700 10px var(--fm);letter-spacing:.08em;color:var(--brand);text-transform:uppercase}.dg-plan-card h2{font-size:1.12rem;margin:7px 0}.dg-plan-card p{font-size:.9rem;margin:0}.dg-plan-card .pending{display:inline-block;margin-top:14px;font:700 9px var(--fm);text-transform:uppercase;color:#7a5c13;background:#fff7df;border:1px solid #ead89d;border-radius:999px;padding:4px 8px}
.dg-artifacts{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}.dg-artifact{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px}.dg-artifact b{display:block;font-size:.75rem;color:var(--brand);text-transform:uppercase;letter-spacing:.05em;margin-bottom:5px}.dg-artifact p{font-size:.88rem;margin:0}
.dg-gates{background:#eef8f5;border:1px solid #bfe0d4;border-radius:16px;padding:18px;margin:24px 0}.dg-gates h2{font-size:1.1rem;margin:0 0 9px}.dg-gates ul{margin:0;padding-left:20px}.dg-gates li{margin:5px 0;font-size:.88rem}
.dg-nav{display:grid;grid-template-columns:1fr auto 1fr;gap:10px;align-items:stretch;margin:30px 0}.dg-nav a{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-weight:700;font-size:.83rem}.dg-nav a:last-child{text-align:right}.dg-nav .home{text-align:center;background:var(--brand);color:#fff;border-color:var(--brand)}
.dg-footer{margin-top:48px;border-top:1px solid var(--line);padding:22px 0 38px;color:var(--ink-3);font:500 11px var(--fm)}
@media(max-width:760px){.dg-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.dg-flow{grid-template-columns:1fr}.dg-flow div:not(:last-child):after{content:"↓";right:auto;left:50%;top:auto;bottom:-14px;transform:translateX(-50%)}.dg-lenses,.dg-plan,.dg-artifacts{grid-template-columns:1fr}.dg-row{grid-template-columns:42px minmax(0,1fr)}.dg-pill{grid-column:2}.dg-nav{grid-template-columns:1fr}.dg-nav a,.dg-nav a:last-child{text-align:center}}
@media(max-width:520px){.owos-nav{padding:0 12px}.owos-brand{gap:6px;min-width:0}.owos-wm{font-size:13px}.owos-pw{display:none}.crumb{font-size:9px;line-height:1.35;text-align:right;max-width:100px}.wrap{padding-left:16px;padding-right:16px}.dg-hero{padding:26px 20px;border-radius:20px}.dg-hero h1{font-size:2.15rem}.dg-hero p{font-size:1rem}.dg-status{border-radius:14px;font-size:9px}.dg-stat{padding:14px 12px}.dg-stat b{font-size:1.35rem}.dg-row{padding:14px 12px;gap:10px}.dg-sections{overflow-wrap:anywhere}.dg-shell{padding:16px;flex-direction:column}.dg-shell-icon{width:36px;height:36px}}
""".replace("—", "-").replace("–", "-")


def nav(home: str, crumb: str) -> str:
    return f"""<nav class="owos-nav">
  <a class="owos-brand" href="{home}">{logo()}<span class="owos-wm">One Water <b>OS</b></span><span class="owos-pw">Academy &middot; <em>Data Governance</em></span></a>
  <span class="crumb"><a href="{home}">Master Class</a> / <b>{html.escape(crumb)}</b></span>
</nav>"""


def landing(chapters: list[Chapter]) -> str:
    groups: list[tuple[str, str, list[Chapter]]] = []
    for chapter in chapters:
        if not groups or groups[-1][0] != chapter.part_code:
            groups.append((chapter.part_code, chapter.part_title, []))
        groups[-1][2].append(chapter)
    curriculum = []
    for code, title, items in groups:
        rows = []
        for chapter in items:
            section_titles = " &middot; ".join(html.escape(s.title) for s in chapter.sections)
            released = chapter.number in RELEASED_CHAPTERS
            release_state = "released" if released else "content-pending"
            release_label = "Available now" if released else "Shell ready"
            release_class = " released" if released else ""
            rows.append(f"""<a class="dg-row{release_class}" href="{chapter.source_name}" data-chapter="{chapter.number}" data-release-state="{release_state}">
  <span class="dg-num">{chapter.number}</span>
  <span><h3>{html.escape(chapter.title)}</h3><span class="dg-sections">{section_titles}</span></span>
  <span class="dg-pill">{release_label}</span>
</a>""")
        curriculum.append(f"""<section class="dg-part">
<div class="dg-part-head"><b>{html.escape(code)}</b><span>{html.escape(title)}</span><small>{len(items)} chapter{'s' if len(items) != 1 else ''}</small></div>
<div class="dg-list">{''.join(rows)}</div>
</section>""")
    description = "The complete 25-chapter utility Data and AI Governance curriculum structure, ready for governed lesson development."
    return f"""{head('Data Before AI', description, 'in-development')}
<body data-course-id="{COURSE_ID}" data-course-store="{STORE_KEY}" data-release-state="in-development">
{nav(COURSE_SOURCE, 'Curriculum')}
<div id="rprog"></div>
<main class="wrap">
  <header class="dg-hero">
    <div class="dg-eyebrow">OWOS Academy &middot; Utility Master Class</div>
    <h1>Data Before AI</h1>
    <p>Build the governance layer that makes utility data trustworthy enough for operations, regulation, capital decisions, analytics, artificial intelligence, and digital twins.</p>
    <span class="dg-status"><i></i>Chapters 00 to 05 available &middot; 19 chapters in development</span>
  </header>

  <div class="dg-stats" aria-label="Course structure">
    <div class="dg-stat"><b>25</b><span>Chapters 00 to 24</span></div>
    <div class="dg-stat"><b>75</b><span>Planned sections</span></div>
    <div class="dg-stat"><b>12</b><span>Governance domains</span></div>
    <div class="dg-stat"><b>{len(RELEASED_CHAPTERS)}</b><span>Lessons released</span></div>
  </div>

  <aside class="dg-note"><strong>The course is releasing chapter by chapter.</strong><p>Chapters 00 to 02 establish the governed Launch Pack, executive case, controlled utility language, provenance, quality-by-use rule, and first data product. Chapter 03 builds the authority register and legal applicability gate. Chapter 04 maps the physical and digital utility data estate around material decisions. Chapter 05 establishes shared identity and minimum reconstructable records. The other 19 destinations preserve the governed syllabus while their lesson bodies remain in development.</p></aside>

  <h2>One source, one delivery path</h2>
  <div class="dg-flow" aria-label="Course delivery path"><div>onewater-os curriculum</div><div>Validated native build</div><div>OWOS.ai Learn</div><div>Supabase learner records</div><div>Knowledge Graph alignment</div></div>

  <h2>Choose the depth that fits your role</h2>
  <div class="dg-lenses">
    <article class="dg-lens"><h3>Foundation</h3><p>Plain language, utility examples, and the essential choices every participant should understand.</p></article>
    <article class="dg-lens"><h3>Practitioner</h3><p>Deployment studios, records, controls, and evidence you can take into a utility implementation.</p></article>
    <article class="dg-lens"><h3>Leader</h3><p>Decision rights, consequences, investment gates, assurance boundaries, and scale choices.</p></article>
  </div>

  <section id="curriculum">
    <h2>The complete curriculum</h2>
    <p>Open any chapter to review its exact three-section plan, learner outcome, Riverbend utility case, deployment studio, and required output.</p>
    {''.join(curriculum)}
  </section>

  <section class="dg-part">
    <div class="dg-part-head"><b>APPLIED CAPSTONE</b><span>Deploy one governed utility decision chain</span><small>20-artifact Launch Pack</small></div>
    <div class="dg-list"><div class="dg-row"><span class="dg-num">CP</span><span><h3>Prove the operating model on one material decision</h3><span class="dg-sections">Decision chain &middot; evidence &middot; 90-day launch &middot; funded roadmap &middot; assurance boundary</span></span><span class="dg-pill">Design ready</span></div></div>
  </section>
</main>
<footer class="dg-footer"><div class="wrap">Course ID: {COURSE_ID} &middot; Store: {STORE_KEY} &middot; Native OWOS HTML &middot; Course build {SHELL_VERSION}</div></footer>
<script src="../../../core/components/academy.js"></script>
</body></html>"""


def lesson(chapter: Chapter, chapters: list[Chapter]) -> str:
    index = int(chapter.number)
    prev_link = chapters[index - 1].source_name if index else COURSE_SOURCE
    prev_label = f"Chapter {index - 1:02d}" if index else "Course landing"
    next_link = chapters[index + 1].source_name if index < 24 else COURSE_SOURCE
    next_label = f"Chapter {index + 1:02d}" if index < 24 else "Course landing"
    cards = []
    for section_index, section in enumerate(chapter.sections, start=1):
        cards.append(f"""<article class="dg-plan-card">
  <span class="k">Section {section_index} of 3</span>
  <h2>{html.escape(section.title)}</h2>
  <p>{inline(section.body)}</p>
  <span class="pending">Content development pending</span>
</article>""")
    description = f"Chapter {chapter.number} shell for {chapter.title} in the OWOS utility Data and AI Governance Master Class."
    return f"""{head(f'Chapter {chapter.number}: {chapter.title}', description)}
<body data-course-id="{COURSE_ID}" data-course-store="{STORE_KEY}" data-module="{chapter.number}" data-release-state="content-pending">
{nav(COURSE_SOURCE, f'Chapter {chapter.number}')}
<div id="rprog"></div>
<main class="wrap">
  <header class="dg-hero">
    <div class="dg-eyebrow">{html.escape(chapter.part_code)} &middot; {html.escape(chapter.part_title)} &middot; {html.escape(chapter.chapter_type)}</div>
    <h1>{html.escape(chapter.title)}</h1>
    <p>{inline(chapter.learner_can)}</p>
    <span class="dg-status"><i></i>Chapter {chapter.number} shell &middot; content pending</span>
  </header>

  <section class="dg-shell" role="status">
    <div class="dg-shell-icon">{chapter.number}</div>
    <div><h2>Structure is wired; the lesson is not released.</h2><p>This page preserves the approved syllabus plan and navigation. It intentionally contains no completion event, scored assessment, or credential claim. Those activate only after the full lesson passes content, interaction, evidence, accessibility, and utility-pilot review.</p></div>
  </section>

  <h2>What the learner will be able to do</h2>
  <p>{inline(chapter.learner_can)}</p>

  <div class="dg-plan">{''.join(cards)}</div>

  <h2>The utility deployment thread</h2>
  <div class="dg-artifacts">
    <article class="dg-artifact"><b>Riverbend utility case</b><p>{inline(chapter.riverbend)}</p></article>
    <article class="dg-artifact"><b>Deployment Studio</b><p>{inline(chapter.studio)}</p></article>
    <article class="dg-artifact"><b>Chapter output</b><p>{inline(chapter.output)}</p></article>
  </div>

  <section class="dg-gates"><h2>What must be added before release</h2><ul><li>Complete utility lesson narrative at Foundation, Practitioner, and Leader depth</li><li>Approved diagrams or simulations selected from the OWOS visual system</li><li>Varied knowledge checks with explanatory feedback and critical-gate handling</li><li>Citations, applicability boundaries, accessible interactions, and mobile visual review</li><li>Supabase completion rule and Knowledge Graph alignments verified against the released version</li></ul></section>

  <nav class="dg-nav" aria-label="Chapter navigation"><a href="{prev_link}">&larr; {html.escape(prev_label)}</a><a class="home" href="{COURSE_SOURCE}">All 25 chapters</a><a href="{next_link}">{html.escape(next_label)} &rarr;</a></nav>
</main>
<footer class="dg-footer"><div class="wrap">{COURSE_ID} &middot; Learning object {STORE_KEY}:{chapter.number} &middot; Content status: pending</div></footer>
<script src="../../../core/components/academy.js"></script>
</body></html>"""


def self_contained(source: str, link_map: dict[str, str]) -> str:
    css = CORE_CSS.replace("</style", "<\\/style")
    js = CORE_JS.replace("</script", "<\\/script")
    result = re.sub(
        r'<link rel="stylesheet" href="[^"]*academy\.css">',
        lambda _: f"<style>\n{css}\n</style>",
        source,
    )
    result = re.sub(
        r'<script src="[^"]*academy\.js"></script>',
        lambda _: f"<script>\n{js}\n</script>",
        result,
    )
    data_uri = "data:image/svg+xml;base64," + base64.b64encode(DROOBI_SVG).decode("ascii")
    result = result.replace("../../../core/brand/droobi.svg", data_uri)
    for source_name, output_name in link_map.items():
        result = result.replace(f'href="{source_name}"', f'href="{output_name}"')
    if "—" in result or "–" in result:
        raise ValueError("Built page contains a prohibited em or en dash")
    if re.search(r'<(?:link[^>]*academy\.css|script src="[^"]*academy\.js)', result):
        raise ValueError("Built page still references the shared core")
    return result


def expected_files(chapters: list[Chapter]) -> dict[pathlib.Path, str]:
    link_map = {COURSE_SOURCE: COURSE_OUTPUT}
    link_map.update({chapter.source_name: chapter.output_name for chapter in chapters})
    source_pages = {CURRICULUM / COURSE_SOURCE: landing(chapters)}
    for chapter in chapters:
        path = CURRICULUM / chapter.source_name
        source_pages[path] = path.read_text(encoding="utf-8") if chapter.number in RELEASED_CHAPTERS else lesson(chapter, chapters)
    files = dict(source_pages)
    for path, page in source_pages.items():
        output_name = link_map[path.name]
        files[DIST / output_name] = self_contained(page, link_map)
    syllabus_bytes = SYLLABUS.read_bytes()
    manifest = {
        "schema_version": 1,
        "course_id": COURSE_ID,
        "store": STORE_KEY,
        "slug": "data-before-ai-governance",
        "title": COURSE_TITLE,
        "source_format": "native_html",
        "release_state": "in_development",
        "available_modules": len(RELEASED_CHAPTERS),
        "module_count": len(chapters),
        "section_count": sum(len(c.sections) for c in chapters),
        "guided_minutes_estimate": 2700,
        "syllabus_sha256": hashlib.sha256(syllabus_bytes).hexdigest(),
        "landing": COURSE_OUTPUT,
        "modules": [
            {
                "number": chapter.number,
                "learning_object_key": f"{STORE_KEY}:{chapter.number}",
                "title": chapter.title,
                "part": chapter.part_code,
                "part_title": chapter.part_title,
                "source": chapter.source_name,
                "output": chapter.output_name,
                "release_state": "released" if chapter.number in RELEASED_CHAPTERS else "content_pending",
                "sections": [section.title for section in chapter.sections],
            }
            for chapter in chapters
        ],
    }
    files[APP / "dist/course-manifest.json"] = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale")
    args = parser.parse_args()
    chapters = parse_syllabus()
    files = expected_files(chapters)
    failures: list[str] = []
    for path, content in files.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                failures.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"built {path.relative_to(ROOT)}")
    if failures:
        print("Generated Data Governance shell is stale:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1
    print(f"validated {len(chapters)} chapters, {sum(len(c.sections) for c in chapters)} sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
