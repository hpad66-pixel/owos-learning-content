#!/usr/bin/env python3
"""Regression checks for the structured OWOS Course Compiler."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import yaml

from course_compiler import ModulePackageError, build_module, validate_package


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "apps/meaning-before-models/modules/module-01-rdf-in-15-minutes"


package = validate_package(SOURCE)
if len(package["visuals"]) != 3:
    raise AssertionError("reference module must resolve three actual visual assets")
if len(package["interactions"]) != 2:
    raise AssertionError("reference module must resolve two purposeful interactions")
if {item["type"] for item in package["assessments"].values()} != {
    "multiple-choice",
    "flip-cards",
    "applied-work-product",
}:
    raise AssertionError("reference module assessment variety is incomplete")

with tempfile.TemporaryDirectory() as directory:
    output = Path(directory) / "preview.html"
    result = build_module(SOURCE, output)
    text = output.read_text(encoding="utf-8")
    for phrase in (
        "The relationship hiding inside the alarm",
        "Build it, reverse it, explain it",
        "Trace the evidence path",
        "Flip-card retrieval",
        "Relationship Card",
        'data-open-drawer="graph"',
        "prefers-reduced-motion",
    ):
        if phrase not in text:
            raise AssertionError(f"compiled module is missing: {phrase}")
    if result["checksum"] != package["checksum"]:
        raise AssertionError("compiler output did not retain the validated source checksum")

with tempfile.TemporaryDirectory() as directory:
    output = Path(directory) / "curriculum-module.html"
    build_module(
        SOURCE,
        output,
        asset_prefix="../modules/module-01-rdf-in-15-minutes/",
        course_href="course-meaning-before-models.html",
    )
    text = output.read_text(encoding="utf-8")
    if (
        'src="../modules/module-01-rdf-in-15-minutes/visuals/'
        not in text
    ):
        raise AssertionError("curriculum build did not preserve portable visual paths")
    if 'href="course-meaning-before-models.html"' not in text:
        raise AssertionError("curriculum build did not preserve the course landing link")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "module"
    shutil.copytree(SOURCE, fixture)
    manifest_path = fixture / "visuals/visual-manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["visuals"][0]["locator"] = "visuals/does-not-exist.svg"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    try:
        validate_package(fixture)
    except ModulePackageError as error:
        if "asset does not exist" not in str(error):
            raise AssertionError("missing asset failed for the wrong reason") from error
    else:
        raise AssertionError("a declared visual without an asset passed validation")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "module"
    shutil.copytree(SOURCE, fixture)
    manifest_path = fixture / "visuals/visual-manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["visuals"][0]["rendered_review_status"] = "pending"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    try:
        validate_package(fixture, release_ready=True)
    except ModulePackageError as error:
        if "rendered_review_status is not release approved" not in str(error):
            raise AssertionError("release-ready mode did not expose the pending rendered review") from error
    else:
        raise AssertionError("a pending rendered review passed the release-ready gate")

print("OWOS Course Compiler QA passed: structured source, real assets, interactions, assessment variety, deterministic build, and fail-closed release gates are enforced.")
