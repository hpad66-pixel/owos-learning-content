#!/usr/bin/env python3
"""Validate every included lesson in a governed OWOS course.

The course experience architecture is the lesson inventory. Evidence paths may be
declared per lesson, while stable repository conventions cover the common case.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from course_conformance import ConformanceError, validate_module


DEFAULT_SETTINGS = {
    "lesson_directory": "curriculum",
    "brief_directory": "curriculum/design-briefs",
    "qa_directory": "qa",
    "script_directory": "curriculum/scripts",
    "contract": ".course/full-module-contract.json",
    "lesson_glob": "module-[0-9][0-9]-*.html",
    "script_policy": "if-present",
}


class CourseFullConformanceError(ValueError):
    """Raised when any included course lesson lacks full-module conformance."""


def _safe_course_path(course: Path, value: str, label: str) -> Path:
    candidate = (course / value).resolve()
    course_root = course.resolve()
    if candidate != course_root and course_root not in candidate.parents:
        raise CourseFullConformanceError(
            f"{label} must stay inside the course directory: {value}"
        )
    return candidate


def _existing_candidate(
    candidates: list[Path],
    label: str,
    errors: list[str],
    *,
    required: bool,
) -> Path | None:
    existing = [path for path in candidates if path.is_file()]
    if len(existing) > 1:
        errors.append(
            f"{label} is ambiguous; declare its path in the lesson manifest: "
            + ", ".join(str(path) for path in existing)
        )
        return None
    if existing:
        return existing[0]
    if required:
        errors.append(
            f"missing {label}; checked: " + ", ".join(str(path) for path in candidates)
        )
    return None


def _declared_path(
    course: Path,
    lesson_config: dict,
    key: str,
    label: str,
    errors: list[str],
) -> Path | None:
    evidence = lesson_config.get("evidence", {})
    if not isinstance(evidence, dict):
        errors.append("lesson evidence must be an object")
        return None
    value = evidence.get(key, lesson_config.get(key))
    if value in (None, ""):
        return None
    if not isinstance(value, str):
        errors.append(f"{label} path must be a string")
        return None
    try:
        return _safe_course_path(course, value, label)
    except CourseFullConformanceError as error:
        errors.append(str(error))
        return None


def _module_prefix(stem: str) -> str:
    match = re.match(r"^(module-\d+)", stem)
    return match.group(1) if match else stem


def _relative(course: Path, path: Path | None) -> str | None:
    return path.relative_to(course.resolve()).as_posix() if path else None


def _validate_release_ready_qa(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^release_status:\s*approved\s*$", text, flags=re.M):
        errors.append(
            "release-ready conformance requires release_status: approved in the QA report"
        )
    for gate in (
        "Accuracy and evidence",
        "Learning design",
        "Course distinctiveness",
        "Utility-practitioner review",
        "Technical and accessibility review",
        "Release control",
    ):
        match = re.search(
            rf"^\|\s*{re.escape(gate)}\s*\|\s*([^|]+)\|",
            text,
            flags=re.M,
        )
        if not match or match.group(1).strip().lower() != "passed":
            errors.append(f"release-ready QA hard gate is not passed: {gate}")

    manual_match = re.search(
        r"## Manual review still required\s*(.*?)(?=\n## |\Z)",
        text,
        flags=re.S,
    )
    checkboxes = (
        re.findall(r"^\s*-\s*\[([ xX])\]", manual_match.group(1), flags=re.M)
        if manual_match
        else []
    )
    if not checkboxes:
        errors.append("release-ready QA report needs explicit manual review checkboxes")
    elif any(value == " " for value in checkboxes):
        errors.append("release-ready QA report still has unchecked manual reviews")

    release_row = re.search(
        r"^\|\s*Release\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|",
        text,
        flags=re.M,
    )
    if not release_row or not all(value.strip() for value in release_row.groups()):
        errors.append(
            "release-ready QA report needs a completed Release approval record"
        )
    elif any(
        blocked in release_row.group(3).strip().lower()
        for blocked in ("blocked", "pending", "not approved")
    ):
        errors.append("Release approval record does not record an approval")


def audit(course: Path, *, require_release_ready: bool = False) -> dict:
    course = course.resolve()
    architecture_path = course / ".course/experience-architecture.json"
    if not architecture_path.is_file():
        raise CourseFullConformanceError(
            f"missing course experience architecture: {architecture_path}"
        )
    try:
        architecture = json.loads(architecture_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise CourseFullConformanceError(
            f"invalid course experience architecture JSON: {error}"
        ) from error

    lesson_inventory = architecture.get("lessons")
    if not isinstance(lesson_inventory, dict) or not lesson_inventory:
        raise CourseFullConformanceError(
            "experience architecture must declare a non-empty lessons object"
        )
    configured_settings = architecture.get("full_module_conformance", {})
    if not isinstance(configured_settings, dict):
        raise CourseFullConformanceError(
            "full_module_conformance must be an object when configured"
        )
    settings = {**DEFAULT_SETTINGS, **configured_settings}
    if settings["script_policy"] not in {"if-present", "required", "none"}:
        raise CourseFullConformanceError(
            "full_module_conformance.script_policy must be if-present, required, or none"
        )

    lesson_dir = _safe_course_path(
        course, str(settings["lesson_directory"]), "lesson directory"
    )
    brief_dir = _safe_course_path(
        course, str(settings["brief_directory"]), "brief directory"
    )
    qa_dir = _safe_course_path(course, str(settings["qa_directory"]), "QA directory")
    script_dir = _safe_course_path(
        course, str(settings["script_directory"]), "script directory"
    )
    default_contract = _safe_course_path(
        course, str(settings["contract"]), "full-module contract"
    )

    errors: list[str] = []
    discovered = {
        path.name
        for path in lesson_dir.glob(str(settings["lesson_glob"]))
        if ".artifact." not in path.name
    }
    declared = set(lesson_inventory)
    undeclared = sorted(discovered - declared)
    if undeclared:
        errors.append(
            "lesson files are missing from experience architecture: "
            + ", ".join(undeclared)
        )
    declared_missing = []
    for name, config in lesson_inventory.items():
        if Path(name).name != name:
            errors.append(
                f"lesson inventory keys must be filenames inside the lesson directory: {name}"
            )
            continue
        included = config.get("include", True) if isinstance(config, dict) else True
        if included and not (lesson_dir / name).is_file():
            declared_missing.append(name)
    declared_missing.sort()
    if declared_missing:
        errors.append(
            "included lesson files do not exist: " + ", ".join(declared_missing)
        )

    results: list[dict] = []
    for lesson_name, raw_config in lesson_inventory.items():
        config = raw_config or {}
        if not isinstance(config, dict):
            errors.append(f"{lesson_name}: lesson manifest entry must be an object")
            continue
        if not config.get("include", True):
            continue

        lesson_errors: list[str] = []
        lesson = lesson_dir / lesson_name
        stem = lesson.stem
        prefix = _module_prefix(stem)

        brief = _declared_path(
            course, config, "brief", f"{lesson_name} design brief", lesson_errors
        )
        if brief is None:
            brief = _existing_candidate(
                [brief_dir / f"{stem}.md"],
                f"{lesson_name} module design brief",
                lesson_errors,
                required=True,
            )

        qa = _declared_path(
            course, config, "qa", f"{lesson_name} scored QA report", lesson_errors
        )
        if qa is None:
            qa_candidates = [qa_dir / f"{stem}-quality-control-report.md"]
            fallback = qa_dir / f"{prefix}-quality-control-report.md"
            if fallback not in qa_candidates:
                qa_candidates.append(fallback)
            qa = _existing_candidate(
                qa_candidates,
                f"{lesson_name} scored QA report",
                lesson_errors,
                required=True,
            )

        contract = _declared_path(
            course, config, "contract", f"{lesson_name} full-module contract", lesson_errors
        ) or default_contract
        if not contract.is_file():
            lesson_errors.append(f"missing full-module contract: {contract}")

        script: Path | None = None
        explicit_script = _declared_path(
            course, config, "script", f"{lesson_name} recording script", lesson_errors
        )
        script_policy = config.get("script_policy", settings["script_policy"])
        if script_policy not in {"if-present", "required", "none"}:
            lesson_errors.append(
                f"{lesson_name} script_policy must be if-present, required, or none"
            )
        elif script_policy != "none":
            if explicit_script is not None:
                script = explicit_script
                if not script.is_file():
                    lesson_errors.append(
                        f"configured module recording script is missing: {script}"
                    )
            else:
                script = _existing_candidate(
                    [
                        script_dir / f"{stem}-video-script.md",
                        script_dir / f"{stem}-recording-script.md",
                        script_dir / f"{stem}.md",
                    ],
                    f"{lesson_name} recording script",
                    lesson_errors,
                    required=script_policy == "required",
                )

        if not lesson_errors and brief and qa:
            try:
                module_result = validate_module(
                    lesson, qa, brief, script, contract
                )
            except (ConformanceError, FileNotFoundError, json.JSONDecodeError) as error:
                lesson_errors.extend(str(error).splitlines())
            else:
                if require_release_ready:
                    _validate_release_ready_qa(qa, lesson_errors)
                if lesson_errors:
                    errors.extend(
                        f"{lesson_name}: {error}" for error in lesson_errors
                    )
                    continue
                results.append(
                    {
                        **module_result,
                        "evidence": {
                            "brief": _relative(course, brief),
                            "qa": _relative(course, qa),
                            "script": _relative(course, script),
                            "contract": _relative(course, contract),
                        },
                    }
                )
        if lesson_errors:
            errors.extend(f"{lesson_name}: {error}" for error in lesson_errors)

    if errors:
        raise CourseFullConformanceError(
            "\n".join(f"- {error}" for error in errors)
        )
    if not results:
        raise CourseFullConformanceError("no included lessons were validated")

    return {
        "course": course.name,
        "included_lessons": len(results),
        "status": (
            "whole-course release-ready full-module conformance passed"
            if require_release_ready
            else "whole-course full-module working conformance passed"
        ),
        "lessons": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", type=Path, required=True)
    parser.add_argument(
        "--release-ready",
        action="store_true",
        help="also require completed manual gates and an explicit QA release approval",
    )
    args = parser.parse_args()
    try:
        result = audit(args.course, require_release_ready=args.release_ready)
    except CourseFullConformanceError as error:
        print(f"OWOS whole-course full-module conformance failed:\n{error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
