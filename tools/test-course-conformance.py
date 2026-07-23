#!/usr/bin/env python3
"""Regression checks for reusable full-module conformance enforcement."""

from pathlib import Path

from course_conformance import DEFAULT_CONTRACT, ConformanceError, validate_module


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps/meaning-before-models"

required_contract_keys = {
    "minimum_visual_types",
    "minimum_purposeful_interactions",
    "minimum_quiz_types",
    "minimum_faq_questions",
    "minimum_defined_terms",
    "approved_component_sources",
    "approved_quiz_sources",
    "visual_catalog_terms",
    "required_community_features",
}
if not required_contract_keys.issubset(DEFAULT_CONTRACT):
    raise AssertionError("full-module contract is missing reusable enforcement keys")

result = validate_module(
    COURSE / "curriculum/module-05-five-layers-of-meaning.html",
    COURSE / "qa/module-05-quality-control-report.md",
    COURSE / "curriculum/design-briefs/module-05-five-layers-of-meaning.md",
    COURSE / "curriculum/scripts/module-05-five-layers-of-meaning-video-script.md",
    COURSE / ".course/full-module-contract.json",
)
if len(result["visual_types"]) < 4:
    raise AssertionError("Module 05 needs at least four governed visual types")
if len(result["quiz_types"]) < 3:
    raise AssertionError("Module 05 needs at least three governed quiz types")
if result["purposeful_interactions"] < 2:
    raise AssertionError("Module 05 needs at least two purposeful interactions")

print("Reusable full-module conformance QA passed for Meaning Before Models Module 05.")
