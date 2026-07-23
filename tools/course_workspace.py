#!/usr/bin/env python3
"""Track new and changed source material in an OWOS course workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "apps"
WATCHED_DIRECTORIES = (
    "inbox",
    "research/originals",
    "research/annotations",
    "conversations",
    "author-input",
)
SUPPORTED_EXTENSIONS = {
    ".csv",
    ".doc",
    ".docx",
    ".html",
    ".jpeg",
    ".jpg",
    ".m4a",
    ".md",
    ".mp3",
    ".mp4",
    ".pdf",
    ".png",
    ".ppt",
    ".pptx",
    ".txt",
    ".wav",
    ".webp",
    ".xls",
    ".xlsx",
}
IGNORED_NAMES = {".DS_Store", "README.md"}
SCHEMA = "owos-course-workspace/1.0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inventory(course_dir: Path) -> dict[str, dict[str, Any]]:
    files: dict[str, dict[str, Any]] = {}
    for relative_dir in WATCHED_DIRECTORIES:
        folder = course_dir / relative_dir
        if not folder.exists():
            continue
        for path in sorted(folder.rglob("*")):
            if (
                not path.is_file()
                or path.name in IGNORED_NAMES
                or path.suffix.lower() not in SUPPORTED_EXTENSIONS
            ):
                continue
            stat = path.stat()
            relative = path.relative_to(course_dir).as_posix()
            files[relative] = {
                "sha256": sha256(path),
                "bytes": stat.st_size,
                "modified_ns": stat.st_mtime_ns,
            }
    return files


def compare(
    previous: dict[str, dict[str, Any]], current: dict[str, dict[str, Any]]
) -> dict[str, list[str]]:
    old_paths = set(previous)
    new_paths = set(current)
    return {
        "new": sorted(new_paths - old_paths),
        "changed": sorted(
            path
            for path in old_paths & new_paths
            if previous[path].get("sha256") != current[path].get("sha256")
        ),
        "unchanged": sorted(
            path
            for path in old_paths & new_paths
            if previous[path].get("sha256") == current[path].get("sha256")
        ),
        "removed": sorted(old_paths - new_paths),
    }


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return data if isinstance(data, dict) else {}


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(temporary, path)


def scan_course(course_dir: Path, persist: bool = True) -> dict[str, Any]:
    state_path = course_dir / ".course" / "workspace-state.json"
    previous_manifest = load_manifest(state_path)
    previous_files = previous_manifest.get("files", {})
    if not isinstance(previous_files, dict):
        previous_files = {}

    current_files = inventory(course_dir)
    changes = compare(previous_files, current_files)
    scanned_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    result = {
        "schema": SCHEMA,
        "course": course_dir.name,
        "scanned_at": scanned_at,
        "changes": changes,
        "files": current_files,
        "totals": {
            "tracked": len(current_files),
            "new": len(changes["new"]),
            "changed": len(changes["changed"]),
            "unchanged": len(changes["unchanged"]),
            "removed": len(changes["removed"]),
        },
    }
    if persist:
        atomic_write_json(state_path, result)
    return result


def resolve_course(slug: str) -> Path:
    if not slug or any(character not in "abcdefghijklmnopqrstuvwxyz0123456789-" for character in slug):
        raise ValueError("Course slug must contain only lowercase letters, numbers, and hyphens.")
    course_dir = APPS / slug
    if not course_dir.is_dir():
        raise FileNotFoundError(f"Course workspace not found: {course_dir}")
    return course_dir


def plain_summary(result: dict[str, Any]) -> str:
    totals = result["totals"]
    lines = [
        f"Course: {result['course']}",
        f"Tracked: {totals['tracked']}",
        f"New: {totals['new']} | Changed: {totals['changed']} | Removed: {totals['removed']}",
    ]
    for label in ("new", "changed", "removed"):
        for path in result["changes"][label]:
            lines.append(f"{label.upper()}: {path}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    scan = subparsers.add_parser("scan", help="Record source changes for one course.")
    scan.add_argument("--course", required=True, help="Course folder slug under apps/.")
    scan.add_argument("--json", action="store_true", help="Print the complete result as JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "scan":
        result = scan_course(resolve_course(args.course))
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print(plain_summary(result))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
