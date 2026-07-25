#!/usr/bin/env python3
"""Run the local OWOS Course Author Studio.

The studio edits structured module files, preserves snapshots before each save,
validates packages, and compiles deterministic previews.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import shutil
import sys
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import yaml

from course_compiler import ModulePackageError, build_module, inspect_package, validate_package


ROOT = Path(__file__).resolve().parents[1]
STUDIO = ROOT / "tools/course-author-studio"
EDITABLE_FILES = (
    "design-brief.md",
    "module.yaml",
    "storyboard.yaml",
    "visuals/visual-manifest.yaml",
    "interactions.yaml",
    "assessments.yaml",
    "sources.yaml",
    "glossary.yaml",
    "qa.yaml",
)


def safe_module(course_slug: str, module_slug: str) -> Path:
    if Path(course_slug).name != course_slug or Path(module_slug).name != module_slug:
        raise ValueError("Course and module slugs must be simple directory names.")
    module_dir = (ROOT / "apps" / course_slug / "modules" / module_slug).resolve()
    modules_root = (ROOT / "apps" / course_slug / "modules").resolve()
    if modules_root not in module_dir.parents or not module_dir.is_dir():
        raise ValueError("Structured module not found.")
    return module_dir


def course_inventory() -> list[dict]:
    courses = []
    for modules_dir in sorted((ROOT / "apps").glob("*/modules")):
        if not modules_dir.is_dir():
            continue
        modules = []
        for module_dir in sorted(modules_dir.iterdir()):
            module_file = module_dir / "module.yaml"
            if not module_dir.is_dir() or not module_file.is_file():
                continue
            try:
                data = yaml.safe_load(module_file.read_text(encoding="utf-8"))
                module = data.get("module", {})
            except (OSError, yaml.YAMLError, AttributeError):
                module = {}
            modules.append(
                {
                    "slug": module_dir.name,
                    "module_id": module.get("module_id", module_dir.name),
                    "title": module.get("title", module_dir.name),
                    "source_version": module.get("source_version", "unknown"),
                    "preview_exists": (module_dir / "build/index.html").is_file(),
                }
            )
        if modules:
            courses.append(
                {
                    "slug": modules_dir.parent.name,
                    "title": modules_dir.parent.name.replace("-", " ").title(),
                    "modules": modules,
                }
            )
    return courses


class StudioHandler(SimpleHTTPRequestHandler):
    server_version = "OWOSCourseAuthorStudio/1.0"

    def log_message(self, format_string: str, *args: object) -> None:
        sys.stdout.write(f"{self.address_string()} {format_string % args}\n")

    def json_response(self, data: object, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(data, indent=2, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length > 2_000_000:
            raise ValueError("Request is too large.")
        data = json.loads(self.rfile.read(length).decode("utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object.")
        return data

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/courses":
            self.json_response({"courses": course_inventory()})
            return
        if parsed.path == "/api/module":
            try:
                query = parse_qs(parsed.query)
                module_dir = safe_module(query["course"][0], query["module"][0])
                package = inspect_package(module_dir)
                files = {
                    name: (module_dir / name).read_text(encoding="utf-8")
                    for name in EDITABLE_FILES
                }
                self.json_response(
                    {
                        "package": package,
                        "files": files,
                        "preview_url": f"/repo/{module_dir.relative_to(ROOT).as_posix()}/build/index.html",
                    }
                )
            except (KeyError, IndexError, ValueError, OSError, ModulePackageError) as error:
                self.json_response({"error": str(error)}, HTTPStatus.BAD_REQUEST)
            return
        if parsed.path.startswith("/repo/"):
            relative = unquote(parsed.path.removeprefix("/repo/"))
            candidate = (ROOT / relative).resolve()
            if ROOT not in candidate.parents or not candidate.is_file():
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            body = candidate.read_bytes()
            content_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        if parsed.path in {"/", "/index.html"} or parsed.path.startswith("/review/"):
            self.path = "/index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        try:
            payload = self.read_json()
            module_dir = safe_module(str(payload["course"]), str(payload["module"]))
            if parsed.path == "/api/save":
                filename = str(payload["file"])
                if filename not in EDITABLE_FILES:
                    raise ValueError("This file is not editable in Author Studio.")
                content = str(payload["content"])
                if filename.endswith(".yaml"):
                    parsed_yaml = yaml.safe_load(content)
                    if not isinstance(parsed_yaml, dict):
                        raise ValueError("The saved YAML must contain one top-level object.")
                target = module_dir / filename
                if target.is_file():
                    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
                    snapshot = module_dir / ".history" / stamp / filename
                    snapshot.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(target, snapshot)
                target.write_text(content.rstrip() + "\n", encoding="utf-8")
                self.json_response({"status": "saved", "file": filename})
                return
            if parsed.path == "/api/validate":
                package = validate_package(module_dir)
                self.json_response(
                    {
                        "status": "valid",
                        "checksum": package["checksum"],
                        "compiler_version": package["compiler_version"],
                    }
                )
                return
            if parsed.path == "/api/build":
                result = build_module(module_dir, None)
                self.json_response(
                    {
                        **result,
                        "preview_url": f"/repo/{module_dir.relative_to(ROOT).as_posix()}/build/index.html",
                    }
                )
                return
            self.json_response({"error": "Unknown endpoint."}, HTTPStatus.NOT_FOUND)
        except (KeyError, ValueError, OSError, json.JSONDecodeError, yaml.YAMLError, ModulePackageError) as error:
            self.json_response({"error": str(error)}, HTTPStatus.BAD_REQUEST)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    if not STUDIO.is_dir():
        print(f"Missing Author Studio assets: {STUDIO}", file=sys.stderr)
        return 1
    handler = lambda *handler_args, **kwargs: StudioHandler(
        *handler_args, directory=str(STUDIO), **kwargs
    )
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"OWOS Course Author Studio: http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
