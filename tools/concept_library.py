#!/usr/bin/env python3
"""Build the OWOS Concept Brief library from its governed registry."""

from __future__ import annotations

import argparse
import html
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def build(registry_path: Path, output: Path) -> None:
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    items = data.get("items") or []
    cards = []
    for item in items:
        topics = "".join(f"<li>{esc(topic)}</li>" for topic in item.get("topics") or [])
        cards.append(
            '<article class="brief-card">'
            f'<div class="brief-number">{esc(item["number"])}</div>'
            f'<p class="eyebrow">{esc(item["eyebrow"])}</p>'
            f'<h2>{esc(item["title"])}</h2>'
            f'<p>{esc(item["description"])}</p>'
            f'<ul>{topics}</ul>'
            f'<div class="card-meta"><span>{esc(item["edition"])}</span>'
            f'<a href="{esc(item["href"])}">Open brief</a></div>'
            "</article>"
        )
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(data["title"])} | One Water Foundation</title>
<style>
:root{{--bg:#171614;--panel:#252422;--paper:#f3efe8;--ink:#211f1b;--blue:#7dc6e8;--gold:#ebca62;--line:#49463f}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:#f8f5ef;font:16px/1.6 Arial,sans-serif}}
.wrap{{width:min(1120px,calc(100% - 32px));margin:auto}}header{{padding:clamp(72px,10vw,140px) 0 70px;border-bottom:1px solid var(--line)}}
.kicker,.eyebrow{{color:var(--blue);font:700 11px/1.3 ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase}}
h1{{max-width:900px;margin:.18em 0;font-size:clamp(54px,9vw,112px);line-height:.88;letter-spacing:-.055em}}
header p{{max-width:700px;color:#c8c1b6;font-size:19px}}main{{padding:70px 0 120px}}.brief-grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}}
.brief-card{{position:relative;padding:clamp(28px,5vw,52px);background:var(--panel);min-height:480px}}.brief-number{{position:absolute;top:22px;right:24px;color:#666159;font-size:60px;font-weight:800}}
.brief-card h2{{max-width:520px;margin:18px 0;font-size:clamp(36px,5vw,64px);line-height:.95;letter-spacing:-.04em}}.brief-card>p:not(.eyebrow){{max-width:570px;color:#c8c1b6}}
.brief-card ul{{display:flex;flex-wrap:wrap;gap:8px;padding:0;list-style:none}}.brief-card li{{padding:6px 9px;border:1px solid #55514b;color:#ddd6cb;font-size:12px}}
.card-meta{{position:absolute;right:clamp(28px,5vw,52px);bottom:clamp(28px,5vw,52px);left:clamp(28px,5vw,52px);display:flex;align-items:center;justify-content:space-between;gap:18px;border-top:1px solid var(--line);padding-top:22px}}
.card-meta span{{color:var(--gold);font:700 11px ui-monospace,monospace;text-transform:uppercase}}a{{display:inline-flex;min-height:44px;align-items:center;padding:9px 15px;background:var(--blue);color:var(--ink);font-weight:800;text-decoration:none}}
a:focus-visible{{outline:3px solid var(--gold);outline-offset:3px}}footer{{padding:32px 0;border-top:1px solid var(--line);color:#8f8a81;font-size:13px}}
@media(max-width:720px){{.brief-grid{{grid-template-columns:1fr}}.brief-card{{min-height:520px}}}}
</style></head><body><header><div class="wrap"><p class="kicker">ONE WATER FOUNDATION · KNOWLEDGE LIBRARY</p>
<h1>{esc(data["title"])}</h1><p>{esc(data["promise"])}</p></div></header>
<main><div class="wrap"><div class="brief-grid">{''.join(cards)}</div></div></main>
<footer><div class="wrap">Graphite Edition is the standard visual direction. Each brief retains its own learning mechanism and governed evidence record.</div></footer>
</body></html>"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=ROOT / "concept-briefs" / "library.yaml")
    parser.add_argument("--output", type=Path, default=ROOT / "concept-briefs" / "dist" / "index.html")
    args = parser.parse_args()
    build(args.registry.resolve(), args.output.resolve())
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
