#!/usr/bin/env python3
"""Regression test for version 3 full-conformance course scaffolding."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from argparse import Namespace
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "create_course", ROOT / "tools/create-course.py"
)
if SPEC is None or SPEC.loader is None:
    raise AssertionError("could not load course creator")
creator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(creator)


with tempfile.TemporaryDirectory() as directory:
    creator.APPS = Path(directory)
    course = creator.scaffold(
        Namespace(
            slug="fixture-course",
            title="Fixture Course",
            course_id="owos-course-fixture-001",
            runtime_key="fixture001",
            owner="Fixture Owner",
            adopt=False,
        )
    )
    record = yaml.safe_load((course / "course.yaml").read_text(encoding="utf-8"))
    quality = record["quality_contract"]
    if quality.get("version") != 3:
        raise AssertionError("new course did not receive quality contract version 3")
    if quality.get("full_module_conformance_required") is not True:
        raise AssertionError("new course can opt out of full-module conformance")

    architecture = json.loads(
        (course / ".course/experience-architecture.json").read_text(encoding="utf-8")
    )
    if "full_module_conformance" not in architecture:
        raise AssertionError("new course lacks full-module evidence path conventions")
    if not (course / ".course/full-module-contract.json").is_file():
        raise AssertionError("new course lacks a full-module contract")
    authoring = json.loads((course / ".course/authoring.json").read_text(encoding="utf-8"))
    if authoring.get("authoritative_source") != "structured_modules":
        raise AssertionError("new course does not use structured modules as the authoring source")
    if authoring.get("html_role") != "compiled_delivery_output":
        raise AssertionError("new course treats HTML as an authoring source")
    if not (course / "modules/README.md").is_file():
        raise AssertionError("new course lacks the structured module directory")
    if not (course / "qa/COURSE-COHERENCE-REPORT.md").is_file():
        raise AssertionError("new course lacks the course coherence gate")
    if not (course / "qa/rendered/README.md").is_file():
        raise AssertionError("new course lacks the rendered evidence directory")
    if record.get("source_format") != "structured_modules_with_compiled_html":
        raise AssertionError("new course record does not declare compiler-based delivery")
    if not (course / "curriculum/scripts/README.md").is_file():
        raise AssertionError("new course lacks the optional script directory")
    agents = (course / "AGENTS.md").read_text(encoding="utf-8")
    if "tools/course_full_conformance.py" not in agents:
        raise AssertionError("new course instructions omit the whole-course gate")

print(
    "Course creator full-conformance QA passed: new workspaces receive contract "
    "version 3, structured authoring, evidence conventions, and release instructions."
)
