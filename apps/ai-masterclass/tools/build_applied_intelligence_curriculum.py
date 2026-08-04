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
BUILDER = Path(__file__).resolve()

PROGRAM_NAME = "One Water AI"
PROGRAM_SUBTITLE = "The Applied Intelligence Curriculum for the Water Sector"
EXPECTED_MODULES = 64

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
    <div class="edition">Complete curriculum<br>Edition 2.0 · 2026</div>
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


def toc_document(titles: dict[str, str], module_pages: dict[int, int], toc_pages: int) -> str:
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
            rows.append(f'<div class="row"><span class="number">{key}</span><span class="title">{html.escape(titles[key])}</span><span class="dots"></span><span class="page">{start_pages[number]}</span></div>')
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{PROGRAM_NAME} | Contents</title>
<style>
@page{{size:letter;margin:.48in .62in}}*{{box-sizing:border-box}}body{{margin:0;color:#26221d;background:#f8f5ee;font-family:Georgia,'Times New Roman',serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.header{{margin:0 0 12px;padding-bottom:9px;border-bottom:3px solid #c6922f}}.kicker{{color:#aa771d;font:800 8px/1.2 'Courier New',monospace;letter-spacing:.15em;text-transform:uppercase}}h1{{margin:4px 0 0;font-size:29px;line-height:1;color:#1e1c19}}
.part{{display:flex;align-items:baseline;gap:9px;margin-top:10px;padding-top:6px;border-top:1px solid #d9d1c4;break-after:avoid}}.part span{{color:#aa771d;font:800 8px/1.2 'Courier New',monospace;text-transform:uppercase;letter-spacing:.12em}}.part strong{{font-size:12px;color:#1e1c19}}
.row{{display:flex;align-items:baseline;gap:7px;padding:2.2px 0;font-size:8.8px;line-height:1.2;break-inside:avoid}}.number{{width:23px;color:#aa771d;font-family:'Courier New',monospace;font-weight:700}}.title{{max-width:5.75in}}.dots{{flex:1;border-bottom:1px dotted #b8ad9e;transform:translateY(-2px)}}.page{{color:#6d655b;font-variant-numeric:tabular-nums}}
</style></head><body><header class="header"><div class="kicker">{PROGRAM_NAME}</div><h1>Complete Curriculum Contents</h1></header>{''.join(rows)}</body></html>"""


def interactive_reader(cover: str, module_records: list[dict[str, str]]) -> str:
    cover_payload = json.dumps(cover, ensure_ascii=True).replace("</", "<\\/")
    module_payload = json.dumps(module_records, ensure_ascii=True).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{PROGRAM_NAME} | {PROGRAM_SUBTITLE}</title>
<style>
:root{{--black:#191917;--black2:#25231f;--paper:#f8f5ee;--white:#fffdf7;--ink:#26221d;--muted:#71695e;--line:#d9d1c4;--gold:#d7a43e;--gold2:#f0cf83}}*{{box-sizing:border-box}}html,body{{height:100%;margin:0}}body{{font-family:Arial,Helvetica,sans-serif;background:var(--paper);color:var(--ink);overflow:hidden}}button,input,a{{font:inherit}}
.app{{display:grid;grid-template-rows:auto 1fr;height:100%}}.topbar{{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:16px;padding:11px 16px;background:var(--black);color:var(--white);border-bottom:3px solid var(--gold)}}.brand{{display:flex;gap:10px;align-items:center;min-width:0}}.mark{{display:grid;place-items:center;width:34px;height:34px;border:1px solid var(--gold);border-radius:50%;background:transparent;color:var(--gold);font-size:10px;font-weight:800}}.brand-copy{{min-width:0}}.brand-copy span{{display:block;color:var(--gold);font:800 8px/1.2 'Courier New',monospace;letter-spacing:.13em;text-transform:uppercase}}.brand-copy strong{{display:block;margin-top:2px;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.current{{min-width:0;text-align:center}}.current strong{{display:block;font-family:Georgia,'Times New Roman',serif;font-size:13px;font-weight:400;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.current span{{display:block;margin-top:3px;color:#bdb6aa;font-size:9px;font-family:'Courier New',monospace;letter-spacing:.07em}}.actions{{display:flex;gap:7px}}.button{{border:1px solid rgba(215,164,62,.48);border-radius:5px;background:transparent;color:var(--white);padding:8px 10px;cursor:pointer;text-decoration:none}}.button.primary{{background:var(--gold);border-color:var(--gold);color:var(--black);font-weight:800}}.button:hover,.button:focus-visible{{outline:2px solid var(--gold2);outline-offset:2px}}
.workspace{{display:grid;grid-template-columns:330px minmax(0,1fr);min-height:0}}.sidebar{{display:grid;grid-template-rows:auto 1fr;min-height:0;background:var(--paper);border-right:1px solid var(--line)}}.search-wrap{{padding:14px;border-bottom:1px solid var(--line)}}.search-wrap label{{display:block;margin-bottom:6px;color:#9a6b19;font:800 9px/1.2 'Courier New',monospace;text-transform:uppercase;letter-spacing:.11em}}.search{{width:100%;padding:10px;border:1px solid var(--line);border-radius:5px;background:#fffdf8;color:var(--ink)}}.list{{overflow:auto;padding:8px}}.front-link,.module-link{{display:grid;grid-template-columns:40px 1fr;gap:9px;width:100%;border:0;border-radius:5px;padding:10px;text-align:left;background:transparent;color:var(--ink);cursor:pointer}}.front-link:hover,.module-link:hover{{background:#eee7da}}.front-link[aria-current="page"],.module-link[aria-current="page"]{{background:var(--black);color:var(--white)}}.num{{color:#9a6b19;font:700 11px/1.5 'Courier New',monospace}}[aria-current="page"] .num{{color:var(--gold)}}.label{{font-family:Georgia,'Times New Roman',serif;font-size:12.5px;line-height:1.32}}.reader{{position:relative;min-width:0;min-height:0;background:#ded8ce}}.reader iframe{{display:block;width:100%;height:100%;border:0;background:#fffdf8}}.progress{{position:absolute;bottom:0;left:0;right:0;height:3px;background:rgba(25,25,23,.18)}}.progress span{{display:block;height:100%;width:0;background:var(--gold)}}.menu{{display:none}}
@media(max-width:850px){{.topbar{{grid-template-columns:auto minmax(0,1fr) auto;padding:9px;gap:8px}}.brand-copy span,.current span{{display:none}}.brand-copy strong{{font-size:11px}}.current strong{{font-size:10px}}.workspace{{grid-template-columns:1fr}}.sidebar{{position:fixed;z-index:30;top:55px;bottom:0;left:0;width:min(90vw,360px);transform:translateX(-105%);transition:transform .2s ease;box-shadow:12px 0 34px rgba(0,0,0,.2)}}body.nav-open .sidebar{{transform:translateX(0)}}.menu{{display:inline-block}}.actions .desktop{{display:none}}}}
@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important;transition:none!important}}}}
</style></head><body><div class="app"><header class="topbar"><div class="brand"><span class="mark">OW</span><div class="brand-copy"><span>One Water Operating System</span><strong>{PROGRAM_NAME}</strong></div></div><div class="current"><strong id="current-title">{PROGRAM_SUBTITLE}</strong><span id="current-number">ONE FOUNDATION · SEVEN TRACKS · 64 MODULES</span></div><div class="actions"><button class="button menu" id="menu" type="button" aria-controls="sidebar" aria-expanded="false">Contents</button><button class="button" id="previous" type="button">Previous</button><button class="button" id="next" type="button">Next</button><a class="button primary desktop" href="../pdf/{OUTPUT_PDF.name}">Download PDF</a></div></header><div class="workspace"><aside class="sidebar" id="sidebar"><div class="search-wrap"><label for="search">Find a module</label><input class="search" id="search" type="search" placeholder="Search all 64 modules"></div><nav class="list" id="list"></nav></aside><main class="reader"><iframe id="frame" title="{PROGRAM_NAME} curriculum"></iframe><div class="progress"><span id="progress"></span></div></main></div></div>
<script>
const cover={cover_payload};const modules={module_payload};const list=document.getElementById('list');const frame=document.getElementById('frame');const title=document.getElementById('current-title');const number=document.getElementById('current-number');const progress=document.getElementById('progress');const search=document.getElementById('search');const previous=document.getElementById('previous');const next=document.getElementById('next');const menu=document.getElementById('menu');let current=-1;
function item(buttonClass,num,label,index){{const button=document.createElement('button');button.type='button';button.className=buttonClass;button.dataset.index=String(index);if(index===current)button.setAttribute('aria-current','page');button.innerHTML=`<span class="num">${{num}}</span><span class="label">${{label}}</span>`;button.addEventListener('click',()=>openItem(index,true));return button}}
function renderList(query=''){{const q=query.trim().toLowerCase();list.innerHTML='';if(!q||'cover tracks audience'.includes(q))list.appendChild(item('front-link','START','Cover and learning tracks',-1));modules.forEach((module,index)=>{{const haystack=`${{module.number}} ${{module.title}}`.toLowerCase();if(q&&!haystack.includes(q))return;list.appendChild(item('module-link',module.number,module.title,index));}})}}
function openItem(index,push){{current=Math.max(-1,Math.min(modules.length-1,index));if(current<0){{frame.srcdoc=cover;title.textContent='{PROGRAM_SUBTITLE}';number.textContent='ONE FOUNDATION · SEVEN TRACKS · 64 MODULES';progress.style.width='0%';}}else{{const module=modules[current];frame.srcdoc=module.content;frame.title=`Module ${{module.number}}: ${{module.title}}`;title.textContent=module.title;number.textContent=`MODULE ${{module.number}} · ${{current+1}} OF ${{modules.length}}`;progress.style.width=`${{((current+1)/modules.length)*100}}%`;}}previous.disabled=current<0;next.disabled=current===modules.length-1;renderList(search.value);if(push)history.pushState({{index:current}},'',current<0?'#cover':`#module=${{modules[current].number}}`);document.body.classList.remove('nav-open');menu.setAttribute('aria-expanded','false');}}
function indexFromHash(){{const match=location.hash.match(/module=(\\d{{2}})/);if(!match)return -1;return modules.findIndex(module=>module.number===match[1]);}}search.addEventListener('input',()=>renderList(search.value));previous.addEventListener('click',()=>openItem(current-1,true));next.addEventListener('click',()=>openItem(current+1,true));menu.addEventListener('click',()=>{{const open=document.body.classList.toggle('nav-open');menu.setAttribute('aria-expanded',String(open));}});window.addEventListener('popstate',()=>openItem(indexFromHash(),false));document.addEventListener('keydown',event=>{{if(event.key==='Escape'){{document.body.classList.remove('nav-open');menu.setAttribute('aria-expanded','false');}}}});openItem(indexFromHash(),false);
</script></body></html>"""


def build() -> dict[str, object]:
    paths = source_module_paths()
    titles = canonical_titles()
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

        for index, source_path in enumerate(paths):
            number = int(source_path.name.split("_", 2)[1])
            revised = replace_identity(source_path.read_text(encoding="utf-8"))
            revised_for_reader = embed_skills_download(revised)
            revised_path = html_dir / source_path.name
            revised_path.write_text(revised, encoding="utf-8")
            destination = pdf_dir / source_path.with_suffix(".pdf").name
            render_html(chrome, revised_path, destination)
            module_pdfs[number] = destination
            module_pages[number] = len(PdfReader(destination).pages)
            module_records.append({"number":f"{number:02d}","title":titles[f"{number:02d}"],"content":revised_for_reader})
            print(f"Rendered module {number:02d} of 63", flush=True)

        cover_html = temp / "cover.html"
        cover_pdf = temp / "cover.pdf"
        cover = cover_document()
        cover_html.write_text(cover, encoding="utf-8")
        render_html(chrome, cover_html, cover_pdf)
        if len(PdfReader(cover_pdf).pages) != 1:
            raise RuntimeError("The branded cover must render as exactly one page")

        toc_pages = 3
        toc_html = temp / "toc.html"
        toc_pdf = temp / "toc.pdf"
        for _ in range(3):
            toc_html.write_text(toc_document(titles, module_pages, toc_pages), encoding="utf-8")
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
        for roman, part_title, numbers in PARTS:
            numbers_list = list(numbers)
            parent = writer.add_outline_item(f"Part {roman + ': ' if roman else ''}{part_title}", module_start_pages[numbers_list[0]])
            for number in numbers_list:
                writer.add_outline_item(f"{number:02d}. {titles[f'{number:02d}']}", module_start_pages[number], parent=parent)
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
    module_records = []
    for source_path in paths:
        number = int(source_path.name.split("_", 2)[1])
        revised = replace_identity(source_path.read_text(encoding="utf-8"))
        module_records.append({
            "number": f"{number:02d}",
            "title": titles[f"{number:02d}"],
            "content": embed_skills_download(revised),
        })
    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(interactive_reader(cover_document(), module_records), encoding="utf-8")
    manifest = json.loads(OUTPUT_MANIFEST.read_text(encoding="utf-8"))
    manifest["source"]["builder_sha256"] = sha256(BUILDER)
    manifest["outputs"][str(OUTPUT_HTML.relative_to(APP_ROOT))]["sha256"] = sha256(OUTPUT_HTML)
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def check() -> None:
    if not OUTPUT_MANIFEST.exists():
        raise RuntimeError("The curriculum build manifest is missing")
    manifest = json.loads(OUTPUT_MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("program_name") != PROGRAM_NAME or manifest.get("modules") != EXPECTED_MODULES:
        raise RuntimeError("Program identity or module count is out of sync")
    for relative, record in manifest["outputs"].items():
        path = APP_ROOT / relative
        if not path.exists() or sha256(path) != record["sha256"]:
            raise RuntimeError(f"Output is missing or stale: {relative}")
    html_text = OUTPUT_HTML.read_text(encoding="utf-8")
    if "One Water AI Master Class" in html_text or "The One Water AI Master Class" in html_text:
        raise RuntimeError("Legacy Master Class branding remains in the new HTML")
    if html_text.count('"number": "') != EXPECTED_MODULES:
        raise RuntimeError("The interactive HTML does not contain exactly 64 modules")
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
