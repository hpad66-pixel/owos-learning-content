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

from course_quality import CourseQualityError, validate_lesson
from course_distinctiveness import audit as audit_distinctiveness
from course_full_conformance import (
    CourseFullConformanceError,
    audit as audit_full_conformance,
)
from course_compiler import ModulePackageError, validate_package

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def required(value, label: str):
    if value in (None, "", []):
        raise SystemExit(f"course.yaml is missing {label}")
    return value


def relative_file(path: Path, site_dir: Path) -> dict:
    rel = path.relative_to(ROOT).as_posix()
    runtime_rel = path.relative_to(site_dir).as_posix()
    return {
        "source_path": rel,
        "runtime_path": f"site/{runtime_rel}",
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "role": (
            "course_landing"
            if path.name.startswith("course-")
            else "lesson"
            if path.name.startswith("lesson-")
            else "runtime_asset"
        ),
    }


def audit_structured_authoring(
    course_dir: Path,
    *,
    chapters: int,
    require_release_ready: bool,
) -> dict | None:
    authoring_path = course_dir / ".course/authoring.json"
    if not authoring_path.is_file():
        return None
    authoring = json.loads(authoring_path.read_text(encoding="utf-8"))
    if authoring.get("authoritative_source") != "structured_modules":
        return None
    migration = authoring.get("migration_state") or {}
    legacy_remaining = int(migration.get("legacy_html_modules_remaining", 0))
    if legacy_remaining:
        return None
    module_value = Path(str(authoring.get("module_directory", "modules")))
    module_root = module_value if module_value.is_absolute() else course_dir / module_value
    module_dirs = sorted(
        path for path in module_root.iterdir()
        if path.is_dir() and (path / "module.yaml").is_file()
    )
    if len(module_dirs) != chapters:
        raise SystemExit(
            "structured authoring gate expected "
            f"{chapters} module packages, found {len(module_dirs)}"
        )
    results = []
    for module_dir in module_dirs:
        try:
            package = validate_package(
                module_dir, release_ready=require_release_ready
            )
        except ModulePackageError as error:
            raise SystemExit(
                "structured authoring gate failed before release:\n"
                f"{module_dir.name}:\n{error}"
            ) from error
        results.append(
            {
                "module_id": package["module_data"]["module"]["module_id"],
                "module_path": module_dir.relative_to(ROOT).as_posix(),
                "source_version": package["module_data"]["module"]["source_version"],
                "package_checksum": package["checksum"],
                "compiler_version": package["compiler_version"],
            }
        )
    return {
        "status": "passed",
        "modules_validated": len(results),
        "modules": results,
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
    quality_contract = required(record.get("quality_contract"), "quality_contract")

    if not landing.is_file():
        raise SystemExit(f"landing output does not exist: {landing.relative_to(ROOT)}")
    if available != len(released):
        raise SystemExit(f"available_chapters is {available}, but released_chapters contains {len(released)} values")
    if available > chapters:
        raise SystemExit("available_chapters cannot exceed structure.chapters")
    if len(lessons) != chapters:
        raise SystemExit(f"expected {chapters} built lessons, found {len(lessons)}")

    released_lessons = [path for path in lessons if any(f"-{chapter}-" in path.name for chapter in released)]
    if len(released_lessons) != len(released):
        raise SystemExit(
            f"expected {len(released)} released lesson files, found {len(released_lessons)}"
        )
    quality_results = []
    full_conformance = None
    if quality_contract.get("enforce_on_release") is not True:
        raise SystemExit("quality_contract.enforce_on_release must be true")
    if quality_contract.get("course_distinctiveness_required") is not True:
        raise SystemExit("quality_contract.course_distinctiveness_required must be true")
    quality_contract_version = int(
        required(quality_contract.get("version"), "quality_contract.version")
    )
    full_conformance_required = quality_contract.get(
        "full_module_conformance_required"
    )
    if quality_contract_version >= 3 and full_conformance_required is not True:
        raise SystemExit(
            "quality contract version 3 or later requires "
            "quality_contract.full_module_conformance_required: true"
        )
    distinctiveness = audit_distinctiveness(course_dir)
    if distinctiveness["status"] != "passed":
        summary = "\n".join(
            f"- {error}" for error in distinctiveness["errors"][:20]
        )
        raise SystemExit(
            "course distinctiveness gate failed before release:\n" + summary
        )
    release_state = str(
        delivery.get("release_state")
        or delivery.get("shell_status")
        or ""
    ).strip()
    require_release_ready = release_state == "released"
    structured_authoring = audit_structured_authoring(
        course_dir,
        chapters=chapters,
        require_release_ready=require_release_ready,
    )
    if full_conformance_required is True:
        try:
            full_conformance = audit_full_conformance(
                course_dir, require_release_ready=require_release_ready
            )
        except CourseFullConformanceError as error:
            raise SystemExit(
                "whole-course full-module conformance gate failed before release:\n"
                f"{error}"
            ) from error
        if full_conformance["included_lessons"] != chapters:
            raise SystemExit(
                "whole-course full-module conformance validated "
                f"{full_conformance['included_lessons']} included lessons, "
                f"but structure.chapters declares {chapters}"
            )
    try:
        quality_results = [validate_lesson(path, quality_contract) for path in released_lessons]
    except CourseQualityError as error:
        raise SystemExit(f"course quality gate failed: {error}") from error

    runtime_assets = sorted(
        path for path in site_dir.rglob("*")
        if path.is_file() and path != landing and path not in lessons
    )
    files = [
        relative_file(landing, site_dir),
        *(relative_file(path, site_dir) for path in lessons),
        *(relative_file(path, site_dir) for path in runtime_assets),
    ]
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
    release_quality_contract = {
        "version": quality_contract_version,
        "released_lessons_validated": len(quality_results),
        "minimum_purposeful_interactions": int(
            required(
                quality_contract.get("minimum_purposeful_interactions"),
                "quality_contract.minimum_purposeful_interactions",
            )
        ),
        "course_distinctiveness": "passed",
        "lesson_archetypes": len(distinctiveness["archetypes"]),
        "release_assurance": (
            "release-ready" if require_release_ready else "public-live-review"
        ),
    }
    if full_conformance is not None:
        evidence_inventory = []
        for lesson_result in full_conformance["lessons"]:
            evidence = {}
            for kind, course_relative in lesson_result["evidence"].items():
                if course_relative is None:
                    evidence[kind] = None
                    continue
                evidence_path = course_dir / course_relative
                evidence[kind] = {
                    "source_path": evidence_path.relative_to(ROOT).as_posix(),
                    "sha256": sha256(evidence_path),
                }
            lesson_path = course_dir / "curriculum" / lesson_result["lesson"]
            evidence_inventory.append(
                {
                    "lesson": lesson_path.relative_to(ROOT).as_posix(),
                    "lesson_sha256": sha256(lesson_path),
                    "evidence": evidence,
                }
            )
        release_quality_contract.update(
            {
                "full_module_conformance": "passed",
                "full_modules_validated": full_conformance["included_lessons"],
                "full_module_evidence": evidence_inventory,
            }
        )
    if structured_authoring is not None:
        release_quality_contract.update(
            {
                "structured_authoring": structured_authoring["status"],
                "structured_modules_validated": structured_authoring["modules_validated"],
                "structured_module_sources": structured_authoring["modules"],
            }
        )

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
            "quality_contract": release_quality_contract,
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
