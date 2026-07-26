#!/usr/bin/env python3
"""Regression checks for OWOS learning records, credentials, and pathways."""

from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def validate(instance, schema_path: str) -> None:
    schema = load_json(schema_path)
    errors = sorted(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(instance),
        key=lambda item: list(item.path),
    )
    if errors:
        raise AssertionError("\n".join(error.message for error in errors))


system = yaml.safe_load(
    (ROOT / "core/credentials/credential-system.yaml").read_text(encoding="utf-8")
)
if system["interoperability"]["canonical_event_profile"] != "owos-xapi-profile/1":
    raise AssertionError("xAPI profile is not canonical")
if system["interoperability"]["lms_launch_preferred"] != "cmi5":
    raise AssertionError("cmi5 must be the preferred LMS launch profile")
if system["interoperability"]["legacy_lms_adapter"] != "SCORM 2004":
    raise AssertionError("SCORM 2004 compatibility adapter is missing")

accreditor = yaml.safe_load(
    (ROOT / "core/credentials/accreditors/nccs-unresolved.yaml").read_text(
        encoding="utf-8"
    )
)
if accreditor["status"] != "unresolved" or accreditor["credit_claim"] != "disabled":
    raise AssertionError("unresolved NCCS credit must fail closed")

credential = load_json("examples/learner-dashboard/sample-credential.json")
validate(credential, "core/schemas/owos-credential-record.schema.json")
if credential["state"] == "issued" or credential["credit"]["claim_state"] != "disabled":
    raise AssertionError("specimen credential cannot be issued or credit-bearing")

recommendations = load_json("examples/learner-dashboard/sample-recommendations.json")
for recommendation in recommendations:
    validate(
        recommendation,
        "core/schemas/owos-learning-recommendation.schema.json",
    )
if {item["lane"] for item in recommendations} != {"deepen", "reskill", "cross-skill"}:
    raise AssertionError("all three learning-path lanes are required")

dashboard = (ROOT / "examples/learner-dashboard/index.html").read_text(encoding="utf-8")
for phrase in (
    "DASHBOARD SPECIMEN",
    "Professional credit ledger",
    "AI-assisted skills-based learning pathways",
    "Evidence pending",
    "Completion is not automatically a PDH, CEU, or CU.",
):
    if phrase not in dashboard:
        raise AssertionError(f"learner dashboard is missing: {phrase}")

certificate = ROOT / "output/pdf/owos-learning-certificate-specimen.pdf"
if not certificate.is_file() or not certificate.read_bytes().startswith(b"%PDF"):
    raise AssertionError("certificate specimen PDF is missing or invalid")

print(
    "OWOS credential QA passed: xAPI, cmi5, SCORM compatibility, fail-closed credit, "
    "certificate specimen, learner dashboard, and explainable deepen, reskill, and "
    "cross-skill pathways are wired."
)
