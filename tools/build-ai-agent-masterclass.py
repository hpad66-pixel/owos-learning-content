#!/usr/bin/env python3
"""Build the AI Agent Master Class into its governed OWOS runtime package."""

from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps" / "what-is-an-ai-agent"
SOURCE = COURSE / "curriculum"
OUTPUT = COURSE / "dist" / "site"

MODULES = {
    "module-01-before-the-agent.html": "lesson-ai-agent-01-before-the-agent.html",
    "module-02-inside-the-agent-loop.html": "lesson-ai-agent-02-inside-the-agent-loop.html",
    "module-03-agent-anatomy.html": "lesson-ai-agent-03-agent-anatomy.html",
    "module-04-the-handoff.html": "lesson-ai-agent-04-the-handoff.html",
    "module-05-agent-agentic-or-automated.html": "lesson-ai-agent-05-agent-agentic-or-automated.html",
    "module-06-guardrails.html": "lesson-ai-agent-06-guardrails.html",
    "module-07-utility-applications.html": "lesson-ai-agent-07-utility-applications.html",
    "module-08-design-your-agent.html": "lesson-ai-agent-08-design-your-agent.html",
}


def runtime_html(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    for old, new in MODULES.items():
        text = text.replace(old, new)
    text = text.replace('content="masterclass-candidate"', 'content="live-review"')
    text = text.replace('content="golden-candidate"', 'content="live-review"')
    text = text.replace("MASTER CLASS / PRIVATE REVIEW", "MASTER CLASS / LIVE REVIEW")
    if 'name="owos-course-store"' not in text:
        text = text.replace(
            "</head>",
            '<link rel="stylesheet" href="/owos-brand.css">'
            '<meta name="owos-course-store" content="aia001"></head>',
            1,
        )
    else:
        text = text.replace(
            "</head>",
            '<link rel="stylesheet" href="/owos-brand.css"></head>',
            1,
        )
    text = text.replace('role="status" aria-live="polite"', 'role="status"')
    text = text.replace('role="status"', 'role="status" aria-live="polite"')
    text = re.sub(
        r'<div class="feedback"(?![^>]*\brole=)([^>]*)>',
        r'<div class="feedback"\1 role="status" aria-live="polite">',
        text,
    )
    text = text.replace(
        "</body>",
        '<script src="/owos-shell.js" defer></script></body>',
        1,
    )
    return text


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for path in OUTPUT.glob("*"):
        if path.is_file():
            path.unlink()

    landing = SOURCE / "course-what-is-an-ai-agent.html"
    (OUTPUT / landing.name).write_text(runtime_html(landing), encoding="utf-8")
    for source_name, runtime_name in MODULES.items():
        (OUTPUT / runtime_name).write_text(runtime_html(SOURCE / source_name), encoding="utf-8")
    for asset in ("masterclass.css", "masterclass.js"):
        shutil.copyfile(SOURCE / asset, OUTPUT / asset)
    print(f"Built AI Agent Master Class: 1 landing, {len(MODULES)} lessons, 2 shared assets")


if __name__ == "__main__":
    main()
