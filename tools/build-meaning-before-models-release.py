#!/usr/bin/env python3
"""Build the self-contained Meaning Before Models live-review release."""

from __future__ import annotations

import re
import shutil
import json
from pathlib import Path

import yaml

from course_distinctiveness import audit as audit_distinctiveness


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps/meaning-before-models"
SOURCE = COURSE / "curriculum"
DIST = COURSE / "dist/site"

ASSETS = {
    "masterclass.css": "meaning-before-models-masterclass.css",
    "masterclass.js": "meaning-before-models-masterclass.js",
    "course-module.js": "meaning-before-models-course-module.js",
    "module-05-golden.css": "meaning-before-models-module-05.css",
    "module-05-golden.js": "meaning-before-models-module-05.js",
    "meaning-fieldbook.css": "meaning-before-models-fieldbook.css",
    "meaning-fieldbook.js": "meaning-before-models-fieldbook.js",
}


def structured_assets() -> dict[str, tuple[Path, str]]:
    """Map structured curriculum references to flat release assets."""

    authoring_path = COURSE / ".course/authoring.json"
    if not authoring_path.is_file():
        return {}
    authoring = json.loads(authoring_path.read_text(encoding="utf-8"))
    migration = authoring.get("migration_state") or {}
    result: dict[str, tuple[Path, str]] = {}
    for module_name in migration.get("structured_modules", []):
        module_dir = COURSE / "modules" / str(module_name)
        manifest_path = module_dir / "visuals/visual-manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        for visual in manifest.get("visuals", []):
            locator = str(visual.get("locator", ""))
            if not locator:
                continue
            source = module_dir / locator
            output = f"meaning-before-models-{module_name}-{source.name}"
            curriculum_reference = f"../modules/{module_name}/{locator}"
            result[curriculum_reference] = (source, output)
    return result


STRUCTURED_ASSETS = structured_assets()


def lesson_output(source: Path) -> str:
    match = re.fullmatch(r"module-(\d{2})-(.+)\.html", source.name)
    if not match:
        raise SystemExit(f"unexpected lesson filename: {source.name}")
    return f"lesson-meaning-before-models-{match.group(1)}-{match.group(2)}.html"


LESSONS = sorted(SOURCE.glob("module-*.html"))
LINKS = {
    "course-meaning-before-models.html": "course-meaning-before-models.html",
    **{path.name: lesson_output(path) for path in LESSONS},
}


def transform(text: str, *, landing: bool) -> str:
    for source, output in LINKS.items():
        text = text.replace(f'href="{source}', f'href="{output}')
    for source, output in ASSETS.items():
        text = text.replace(f'href="{source}"', f'href="{output}"')
        text = text.replace(f'src="{source}"', f'src="{output}"')
    for source, (_, output) in STRUCTURED_ASSETS.items():
        text = text.replace(f'href="{source}"', f'href="{output}"')
        text = text.replace(f'src="{source}"', f'src="{output}"')

    text = re.sub(
        r'(<meta name="owos-release-state" content=")[^"]+(">)',
        r"\1live-review\2",
        text,
    )
    if landing:
        text = text.replace("MASTER CLASS / WORKING REVIEW", "MASTER CLASS / LIVE REVIEW")
        text = text.replace(
            "The complete lesson set passes repository conformance. Human review and release remain blocked.",
            "The complete lesson set passes repository conformance and is available for live review. "
            "Credentials and authoritative completion remain disabled while human review continues.",
        )
        text = text.replace("<span>Release blocked</span>", "<span>Live review published</span>")
        text = text.replace(
            "Working master-class candidate. No release or credential claim.",
            "Live-review course. No credential, certification, or operational authority claim.",
        )
    else:
        text = text.replace(
            "Production candidate. No release, credential, graph publication, or operational authority claim.",
            "Live-review lesson. No credential, certification, graph-publication, or operational authority claim.",
        )

    if "—" in text or "–" in text:
        raise SystemExit("prohibited dash character reached release output")
    return text


def clean_dist() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    for path in DIST.iterdir():
        if path.is_dir():
            raise SystemExit(f"unexpected directory in generated output: {path}")
        path.unlink()


def main() -> None:
    distinctiveness = audit_distinctiveness(COURSE)
    if distinctiveness["status"] != "passed":
        raise SystemExit(
            "Meaning Before Models release blocked by course distinctiveness gate:\n"
            + "\n".join(f"- {error}" for error in distinctiveness["errors"][:20])
        )
    if len(LESSONS) != 18:
        raise SystemExit(f"expected 18 source lessons, found {len(LESSONS)}")
    clean_dist()

    landing_source = SOURCE / "course-meaning-before-models.html"
    landing_target = DIST / "course-meaning-before-models.html"
    landing_target.write_text(
        transform(landing_source.read_text(encoding="utf-8"), landing=True),
        encoding="utf-8",
    )

    for source in LESSONS:
        target = DIST / lesson_output(source)
        target.write_text(
            transform(source.read_text(encoding="utf-8"), landing=False),
            encoding="utf-8",
        )

    for source_name, output_name in ASSETS.items():
        shutil.copyfile(SOURCE / source_name, DIST / output_name)
    for source, output_name in STRUCTURED_ASSETS.values():
        shutil.copyfile(source, DIST / output_name)

    for page in sorted(DIST.glob("*.html")):
        text = page.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http:", "https:", "data:", "#", "/", "mailto:")):
                continue
            target = DIST / href.split("#", 1)[0]
            if not target.exists():
                raise SystemExit(f"{page.name} has missing release target: {href}")
        for src in re.findall(r'src="([^"]+)"', text):
            if src.startswith(("http:", "https:", "data:", "/")):
                continue
            if not (DIST / src).exists():
                raise SystemExit(f"{page.name} has missing release asset: {src}")

    print(
        "Built Meaning Before Models live review: "
        f"{len(LESSONS)} lessons and {len(ASSETS) + len(STRUCTURED_ASSETS)} assets."
    )


if __name__ == "__main__":
    main()
