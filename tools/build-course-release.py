#!/usr/bin/env python3
"""Build and verify an OWOS course release manifest.

The manifest contains metadata and checksums only. The receiving repository checks out the exact
source commit and verifies every file before copying it into the OWOS runtime.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def required(value, label: str):
    if value in (None, "", []):
        raise SystemExit(f"course.yaml is missing {label}")
    return value


def relative_file(path: Path) -> dict:
    rel = path.relative_to(ROOT).as_posix()
    return {
        "source_path": rel,
        "runtime_path": f"site/{path.name}",
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "role": "course_landing" if path.name.startswith("course-") else "lesson",
    }


def build(course_dir: Path) -> dict:
    record_path = course_dir / "course.yaml"
    record = yaml.safe_load(record_path.read_text(encoding="utf-8")) or {}
    delivery = required(record.get("delivery"), "delivery")
    structure = required(record.get("structure"), "structure")
    source_files = required(record.get("source_files"), "source_files")
    version = str(required(record.get("course_version"), "course_version"))

    landing_value = Path(required(delivery.get("landing_output"), "delivery.landing_output"))
    landing = landing_value if landing_value.is_absolute() else course_dir / landing_value
    site_dir = landing.parent
    lessons = sorted(site_dir.glob("lesson-*.html"))
    available = int(required(delivery.get("available_chapters"), "delivery.available_chapters"))
    chapters = int(required(structure.get("chapters"), "structure.chapters"))
    released = [str(value).zfill(2) for value in required(delivery.get("released_chapters"), "delivery.released_chapters")]

    if not landing.is_file():
        raise SystemExit(f"landing output does not exist: {landing.relative_to(ROOT)}")
    if available != len(released):
        raise SystemExit(f"available_chapters is {available}, but released_chapters contains {len(released)} values")
    if available > chapters:
        raise SystemExit("available_chapters cannot exceed structure.chapters")
    if len(lessons) != chapters:
        raise SystemExit(f"expected {chapters} built lessons, found {len(lessons)}")

    files = [relative_file(landing), *(relative_file(path) for path in lessons)]
    for entry in files:
        text = (ROOT / entry["source_path"]).read_text(encoding="utf-8")
        if "—" in text or "–" in text:
            raise SystemExit(f"prohibited dash character in {entry['source_path']}")

    syllabus_value = Path(required(source_files.get("syllabus"), "source_files.syllabus"))
    syllabus = syllabus_value if syllabus_value.is_absolute() else course_dir / syllabus_value
    provenance = required(record.get("provenance"), "provenance")
    repository = required(provenance.get("repository"), "provenance.repository")
    content_commit = required(provenance.get("content_baseline_commit"), "provenance.content_baseline_commit")
    slug = required(record.get("slug"), "slug")
    course_id = required(record.get("course_id"), "course_id")
    release_id = f"{course_id}-v{version}"

    return {
        "schema_version": 1,
        "contract": "owos-course-release/1.0",
        "release_id": release_id,
        "release_date": str(required(record.get("release_date"), "release_date")),
        "generated_by": "tools/build-course-release.py",
        "course": {
            "course_id": course_id,
            "slug": slug,
            "title": required(record.get("title"), "title"),
            "version": version,
            "status": required(record.get("status"), "status"),
            "chapters": chapters,
            "available_chapters": available,
            "released_chapters": released,
            "runtime_store_key": required(delivery.get("runtime_store_key"), "delivery.runtime_store_key"),
            "runtime_canonical": required(delivery.get("runtime_canonical"), "delivery.runtime_canonical"),
        },
        "source": {
            "repository": repository,
            "ref": required(provenance.get("ref"), "provenance.ref"),
            "content_baseline_commit": content_commit,
            "course_path": course_dir.relative_to(ROOT).as_posix(),
            "course_record": record_path.relative_to(ROOT).as_posix(),
            "course_record_sha256": sha256(record_path),
            "syllabus_path": syllabus.relative_to(ROOT).as_posix(),
            "syllabus_sha256": sha256(syllabus),
        },
        "runtime": {
            "repository": required(delivery.get("runtime_repository"), "delivery.runtime_repository"),
            "path": required(delivery.get("runtime_path"), "delivery.runtime_path"),
            "learner_records": required(delivery.get("learner_records"), "delivery.learner_records"),
            "semantic_alignment": required(delivery.get("semantic_alignment"), "delivery.semantic_alignment"),
            "edge_delivery": required(delivery.get("edge_delivery"), "delivery.edge_delivery"),
        },
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("course", help="course slug under apps, for example project-management")
    parser.add_argument("--check", action="store_true", help="verify the existing manifest without rewriting it")
    args = parser.parse_args()
    course_dir = ROOT / "apps" / args.course
    manifest_path = course_dir / "dist" / "release-manifest.json"
    manifest = build(course_dir)

    if args.check:
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        if existing != manifest:
            raise SystemExit(f"stale course manifest: {manifest_path.relative_to(ROOT)}")
        print(f"verified {manifest['release_id']} with {len(manifest['files'])} files")
        return

    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"built {manifest_path.relative_to(ROOT)} with {len(manifest['files'])} files")


if __name__ == "__main__":
    main()
