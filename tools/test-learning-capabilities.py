#!/usr/bin/env python3
"""Regression checks for the shared OWOS learning-capability registry."""

from __future__ import annotations

from learning_capabilities import (
    assessment_types,
    interaction_components,
    load_learning_capabilities,
)


registry = load_learning_capabilities()
if registry["engines"]["course"]["standard_name"] != "OWOS Course Engine":
    raise AssertionError("course engine standard name changed")
if registry["engines"]["concept_brief"]["standard_name"] != "OWOS Concept Engine":
    raise AssertionError("Concept Engine standard name changed")
if registry["engines"]["concept_brief"]["contract"] != "owos-concept-brief/2":
    raise AssertionError("Concept Engine contract is not version 2")

required_assessments = {
    "multiple-choice",
    "multi-select",
    "flip-cards",
    "matching",
    "classify-sort",
    "estimate",
    "true-false",
    "fill-blank",
    "put-in-order",
    "reflection",
    "applied-work-product",
}
if not required_assessments.issubset(assessment_types(registry)):
    raise AssertionError("shared quiz catalog is incomplete")
course_assessments = assessment_types(registry, "course")
concept_assessments = assessment_types(registry, "concept_brief")
if not course_assessments.issubset(concept_assessments):
    raise AssertionError(
        "Concept Brief Compiler does not support every assessment renderer available to courses"
    )
if "concept-jar-model" not in interaction_components(registry):
    raise AssertionError("Concept Brief dynamic model is not registered")

experience = registry["experience_contract"]
for key in (
    "visual_explanations_minimum",
    "distributed_checks_minimum",
    "dynamic_explanation_required",
    "final_applied_check_required",
    "cross_sector_connection_required",
):
    if key not in experience:
        raise AssertionError(f"shared experience contract is missing {key}")

if registry["continuing_education"]["credit_claim_allowed_without_approval"] is not False:
    raise AssertionError("continuing-education credit claims must fail closed")

learning_record_contract = registry["learning_record_contract"]
for key in (
    "placement_required",
    "capability_lock_required",
    "stable_event_namespace_required",
    "privacy_classification_required",
    "supersession_and_correction_notification_required",
    "assessment_version_required",
    "simulation_model_version_required",
    "language_and_unit_policy_required",
    "measured_time_basis_required",
):
    if learning_record_contract.get(key) is not True:
        raise AssertionError(f"learning-record contract is missing required control: {key}")
if learning_record_contract.get("facility_sensitive_data_default") != "prohibited":
    raise AssertionError("facility-sensitive learning data must be prohibited by default")

credential_contract = registry["credential_and_pathway_contract"]
expected_credential_controls = {
    "contract": "owos-learning-record-credential/1",
    "canonical_event_profile": "owos-xapi-profile/1",
    "preferred_lms_launch": "cmi5",
    "legacy_lms_adapter": "SCORM 2004",
    "portable_credential_target": "Open Badges 3.0",
    "learner_record_export_target": "Comprehensive Learner Record 2.0",
}
for key, value in expected_credential_controls.items():
    if credential_contract.get(key) != value:
        raise AssertionError(f"credential/pathway contract mismatch: {key}")
if set(credential_contract.get("required_recommendation_lanes", [])) != {
    "deepen",
    "reskill",
    "cross-skill",
}:
    raise AssertionError("credential/pathway contract must require all three pathway lanes")
for key in (
    "explainability_required",
    "learner_control_required",
    "protected_traits_prohibited",
    "facility_sensitive_data_prohibited",
    "accreditor_gate_required_for_credit",
    "issuance_fail_closed",
):
    if credential_contract.get(key) is not True:
        raise AssertionError(f"credential/pathway contract must fail closed: {key}")

print(
    "OWOS learning-capability QA passed: both engines resolve one registry, standard names are "
    "stable, the complete quiz catalog is connected, dynamic explanation and durable learning "
    "records are required, credential interoperability converges, all three recommendation lanes "
    "are present, and continuing-education claims fail closed."
)
