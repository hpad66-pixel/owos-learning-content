#!/usr/bin/env python3
"""Validate and compile governed OWOS Concept Brief packages.

The structured package is the source of truth. HTML and release manifests are
deterministic delivery outputs.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

import yaml

from learning_capabilities import (
    assessment_types,
    interaction_components,
    load_learning_capabilities,
    visual_component_ids,
)

ROOT = Path(__file__).resolve().parents[1]
LEARNING_CAPABILITIES = load_learning_capabilities()
ENGINE = LEARNING_CAPABILITIES["engines"]["concept_brief"]
EXPERIENCE_CONTRACT = LEARNING_CAPABILITIES["experience_contract"]
SUPPORTED_ASSESSMENTS = assessment_types(LEARNING_CAPABILITIES, "concept_brief")
SUPPORTED_INTERACTIONS = interaction_components(LEARNING_CAPABILITIES)
SUPPORTED_VISUAL_COMPONENTS = visual_component_ids(LEARNING_CAPABILITIES)
COMPILER_VERSION = "2.1.0"
CONTRACT = "owos-concept-brief/2"
REQUIRED_FILES = (
    "intake.yaml",
    "brief.yaml",
    "design-brief.md",
    "storyboard.yaml",
    "narrative.yaml",
    "learning.yaml",
    "assessments.yaml",
    "claims.yaml",
    "sources.yaml",
    "visuals/visual-manifest.yaml",
    "interactions.yaml",
    "graph.yaml",
    "community.yaml",
    "commercial.yaml",
    "qa.yaml",
    "approvals.yaml",
)
CLAIM_TYPES = {
    "sourced_fact",
    "regulatory_requirement",
    "technical_standard",
    "expert_interpretation",
    "hardeep_position",
    "instructional_scenario",
    "commercial_claim",
    "unresolved_question",
}
TECHNICAL_CLAIM_TYPES = {
    "sourced_fact",
    "regulatory_requirement",
    "technical_standard",
}
CLAIM_STATUSES = {"pending", "verified", "contested", "rejected", "superseded"}
BLOCK_TYPES = {
    "heading",
    "prose",
    "callout",
    "metric",
    "visual",
    "interaction",
    "assessment",
    "decision",
    "protocol",
    "diagnostic",
    "role",
    "faq",
    "evidence",
    "connected_learning",
    "definition",
    "example",
}
DEFINITION_FIELDS = ("term", "meaning", "example", "not_established")
EXAMPLE_FIELDS = ("situation", "reasoning", "result", "boundary")
SURFACES = {"black", "white", "off_white", "blue"}
EDGE_TYPES = {
    "DEFINES",
    "EXPLAINS",
    "CITES",
    "CORRECTS",
    "CONTESTS",
    "CAUSES",
    "FAILS_DOWNSTREAM_IN",
    "ADJACENT_TO",
    "PREREQUISITE_FOR",
    "TEACHES_INTO",
    "ANSWERS",
    "APPLIES_TO_ROLE",
    "DEVELOPS_COMPETENCY",
    "GENERATES_WORK_PRODUCT",
    "CONTRIBUTED_TO",
    "REVIEWED_BY",
    "SPONSORED_BY",
}
HARD_GATES = (
    "source_preservation",
    "claim_verification_accuracy",
    "learning_editorial_design",
    "utility_technical_practice",
    "visual_interaction_accessibility",
    "graph_community_integrity",
    "commercial_integrity",
    "release_control",
)
MANUAL_REVIEWS = (
    "independent_source",
    "qualified_technical_practitioner",
    "editorial",
    "desktop",
    "tablet",
    "phone",
    "keyboard",
    "touch",
    "screen_reader",
    "reduced_motion",
    "no_javascript",
    "read_without_animation",
    "novice_reader",
    "graph",
    "community",
    "commercial_conflict",
    "owner_release",
)
APPROVALS = (
    "product_boundary",
    "evidence_boundary",
    "design_brief",
    "storyboard",
    "technical_accuracy",
    "editorial",
    "graph_publication",
    "community_connection",
    "commercial_placement",
    "release",
)
BANNED_PHRASES = (
    "delve",
    "tapestry",
    "testament to",
    "paradigm",
    "holistic",
    "synergy",
    "ever-evolving",
    "fast-paced world",
    "moreover",
    "furthermore",
    "it's important to note",
    "in conclusion",
    "at the end of the day",
    "treasure trove",
    "beacon",
    "myriad",
    "plethora",
    "vibrant",
    "bustling",
    "pivotal",
    "crucial role",
    "embark",
    "game-changer",
)


# Rendered-accessibility floor. This is appended AFTER the package brand
# CSS and the shared shell so a package cannot reintroduce a contrast, gutter,
# or touch-target defect by loading its own palette later in the cascade.
ACCESSIBILITY_FLOOR = """
/* The Graphite shell defaults headings and body copy to light, so any surface
   introduced here must declare its own treatment or it inherits light text onto
   a light panel. These follow the shell palette rather than overriding it. */
body[data-owos-theme="graphite"] .orientation{background:var(--owos-graphite);
border-bottom-color:var(--owos-water)}
body[data-owos-theme="graphite"] .orientation h2{color:var(--owos-white)}
body[data-owos-theme="graphite"] .orientation-card{background:var(--owos-charcoal);
border-left-color:var(--owos-water)}
body[data-owos-theme="graphite"] .orientation-card h3{color:var(--owos-water)}
body[data-owos-theme="graphite"] .orientation-card p,
body[data-owos-theme="graphite"] .orientation-card li{color:var(--owos-body)}
body[data-owos-theme="graphite"] .orientation-outcomes{background:var(--owos-charcoal)}
body[data-owos-theme="graphite"] .orientation-outcomes li{color:var(--owos-body)}
body[data-owos-theme="graphite"] .orientation-boundary{background:rgba(125,198,232,.09);
border-left-color:var(--owos-water);color:var(--owos-body)}
body[data-owos-theme="graphite"] .orientation-boundary b{color:var(--owos-white)}
body[data-owos-theme="graphite"] .definition{background:var(--owos-charcoal);
border-left-color:var(--owos-water)}
body[data-owos-theme="graphite"] .definition-term{color:var(--owos-white)}
body[data-owos-theme="graphite"] .definition-meaning{color:var(--owos-body)}
body[data-owos-theme="graphite"] .definition-example{color:#bcd9e8}
body[data-owos-theme="graphite"] .definition-limit{color:#e8cf95}
body[data-owos-theme="graphite"] .definition b{color:var(--owos-white)}
body[data-owos-theme="graphite"] .worked-example{background:var(--owos-charcoal);
border-left-color:var(--owos-water)}
body[data-owos-theme="graphite"] .worked-example p{color:var(--owos-body)}
body[data-owos-theme="graphite"] .worked-example b{color:var(--owos-white)}
body[data-owos-theme="graphite"] .worked-label{color:var(--owos-water)}
/* Contrast repairs for surfaces the Graphite theme inverts. The theme turns the
   off_white beat band into charcoal and keeps the assessment card and drawers
   light, so headings and kickers set for the light composition end up unreadable
   on the surface they actually land on. */
/* Cards carry a correct text colour for their own background, and a brief
   may use a light or a dark variant of the same card. Headings and links
   inherit from the card instead of being forced to one surface. */
.concept-assessment h3,.concept-assessment h4{color:inherit}
body[data-owos-theme="graphite"] .concept-assessment h3,
body[data-owos-theme="graphite"] .concept-assessment h4{color:inherit}
body[data-owos-theme="graphite"] .learner-question{color:var(--owos-water)}
body[data-owos-theme="graphite"] .context-drawer .section-kicker{color:#1d5c90}
/* Gutter repairs. The band header and the status bar carried colour and type
   but no content geometry, so their text ran to the viewport edge while every
   beat body sat inside the wrapper. The bar stays full bleed; only its text
   moves in. */
.band-in{width:min(1080px,calc(100% - 32px));margin:0 auto;padding:18px 0;
display:grid;grid-template-columns:auto minmax(0,1fr);gap:6px 18px;align-items:baseline}
.band-txt{min-width:0}
.status{padding-inline:max(16px,calc((100% - 1080px)/2))}
body[data-owos-theme="graphite"] .band-in{width:min(1160px,calc(100% - 80px))}
body[data-owos-theme="graphite"] .status{padding-inline:max(40px,calc((100% - 1160px)/2))}
@media (max-width:760px){
.band-in{width:min(1080px,calc(100% - 32px))}
body[data-owos-theme="graphite"] .band-in{width:min(1160px,calc(100% - 32px))}
body[data-owos-theme="graphite"] .status{padding-inline:16px}
}
/* Native form controls inherit the theme's dark color-scheme, which renders a
   dark dropdown on the light assessment card. Controls follow the surface they
   sit on, not the page. */
.concept-assessment, .concept-assessment select, .concept-assessment input,
.concept-assessment textarea, .concept-assessment button,
.community-feedback, .community-feedback input, .community-feedback textarea,
.community-feedback select, .context-drawer, .context-drawer input,
.context-drawer select, .context-drawer textarea{color-scheme:light}
.concept-assessment select, .concept-assessment input[type="text"],
.concept-assessment textarea, .community-feedback input,
.community-feedback textarea{background:#fff;color:#10263b;
border:1px solid #8ba6b8;border-radius:3px;font:inherit;padding:10px 12px;
min-height:44px}
.concept-assessment select{appearance:none;
background-image:linear-gradient(45deg,transparent 50%,#1d5c90 50%),
linear-gradient(135deg,#1d5c90 50%,transparent 50%);
background-position:calc(100% - 19px) 50%,calc(100% - 13px) 50%;
background-size:6px 6px,6px 6px;background-repeat:no-repeat;padding-right:38px}
input[type="radio"],input[type="checkbox"]{width:24px;height:24px;min-height:0;
accent-color:#1d5c90;flex:0 0 auto}
.assessment-option{display:flex;gap:12px;align-items:flex-start;
min-height:44px;padding:11px 14px;cursor:pointer}
/* Inline links inside cards were 17px tall, below the 24px touch minimum, and
   were coloured for a surface the card does not always use. They inherit the
   card's colour and carry an underline so the affordance survives. */
.feedback-actions a,.community-public a,.connection-card a,
.commercial-card a:not(.commercial-action),.drawer-connection a:not(.primary-action),
.commercial-directory-note a,.concept-finish a:not(.primary-action),
.editorial-table a,.source-table a{
color:inherit;text-decoration:underline;text-underline-offset:2px;
display:inline-block;min-height:24px;padding:4px 0}
body[data-owos-theme="graphite"] .feedback-actions a,
body[data-owos-theme="graphite"] .community-public a,
body[data-owos-theme="graphite"] .connection-card a,
body[data-owos-theme="graphite"] .commercial-card a:not(.commercial-action),
body[data-owos-theme="graphite"] .commercial-directory-note a,
body[data-owos-theme="graphite"] .concept-finish a:not(.primary-action){
color:inherit;text-decoration:underline}
/* The primary action read dark blue on light cyan at 3.72:1. A primary control
   should be the most legible thing on its surface, so it becomes solid. */
a.primary-action,button.primary-action,
a.commercial-action,button.commercial-action{background:#1d5c90;color:#fff;
border-color:#1d5c90;text-decoration:none}
body[data-owos-theme="graphite"] a.primary-action,
body[data-owos-theme="graphite"] button.primary-action,
body[data-owos-theme="graphite"] a.commercial-action,
body[data-owos-theme="graphite"] button.commercial-action{background:#1d5c90;
color:#fff;border-color:#1d5c90;text-decoration:none}

/* Full-bleed pull quotes escape the wrapper with a negative inline margin
   computed from the parent width, which only lands exactly when the parent is
   perfectly centred. It is not, so the box drifted a couple of pixels past the
   viewport. Anchoring the bleed to the viewport itself removes the dependency:
   the element is positioned relative to its own left edge, so it cannot overshoot
   regardless of what the wrapper is doing. */
.pullquote{position:relative;left:0;width:auto;max-width:100%;
margin-inline:calc(-1 * clamp(0px, var(--pq-bleed, 0px), 100px));
overflow-wrap:break-word}
@media (max-width:760px){.pullquote{margin-inline:0}}
"""


def _match_pair_prompt(pair: dict[str, Any]) -> str:
    """The learner-visible statement of a matching pair.

    Packages author these as ``left``/``right``. ``prompt``/``answer`` are
    accepted as aliases so either spelling renders and grades.
    """
    for key in ("left", "prompt", "statement"):
        if pair.get(key):
            return str(pair[key])
    return ""


def _match_pair_answer(pair: dict[str, Any]) -> str:
    """The correct target of a matching pair."""
    for key in ("right", "answer", "target"):
        if pair.get(key):
            return str(pair[key])
    return ""


class ConceptBriefError(ValueError):
    """Raised when a Concept Brief package is incomplete or unsafe."""


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _portable_asset_href(
    package_dir: Path,
    locator: str,
    asset_prefix: str,
    *,
    inline: bool,
) -> str:
    asset_path = (package_dir / locator).resolve()
    if inline and asset_path.is_file() and asset_path.suffix.lower() == ".svg":
        payload = base64.b64encode(asset_path.read_bytes()).decode("ascii")
        return f"data:image/svg+xml;base64,{payload}"
    return f"{asset_prefix}{locator}"


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise ConceptBriefError(f"{path}: cannot read YAML: {error}") from error
    if not isinstance(data, dict):
        raise ConceptBriefError(f"{path}: expected a YAML object")
    return data


def text_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(text_values(item))
        return result
    if isinstance(value, dict):
        result = []
        for item in value.values():
            result.extend(text_values(item))
        return result
    return []


def require_fields(
    record: dict[str, Any],
    fields: tuple[str, ...],
    label: str,
    errors: list[str],
) -> None:
    for field in fields:
        if record.get(field) in (None, "", []):
            errors.append(f"{label}: missing {field}")


def unique_records(
    records: Any,
    key: str,
    label: str,
    errors: list[str],
) -> dict[str, dict[str, Any]]:
    if not isinstance(records, list):
        errors.append(f"{label}: expected a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            errors.append(f"{label} item {index}: expected an object")
            continue
        identifier = record.get(key)
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"{label} item {index}: missing {key}")
            continue
        if identifier in result:
            errors.append(f"{label}: duplicate {key} {identifier}")
            continue
        result[identifier] = record
    return result


def package_files(package_dir: Path) -> list[Path]:
    ignored_parts = {"dist", "__pycache__", ".git"}
    return sorted(
        path
        for path in package_dir.rglob("*")
        if path.is_file()
        and not any(part in ignored_parts for part in path.relative_to(package_dir).parts)
        and path.name != ".DS_Store"
    )


def package_checksum(package_dir: Path) -> str:
    digest = hashlib.sha256()
    for path in package_files(package_dir):
        digest.update(path.relative_to(package_dir).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    compiler_path = Path(__file__).resolve()
    digest.update(compiler_path.name.encode("utf-8"))
    digest.update(b"\0")
    digest.update(compiler_path.read_bytes())
    digest.update(b"\0")
    digest.update(COMPILER_VERSION.encode("utf-8"))
    return digest.hexdigest()


def _verification_state(
    claim: dict[str, Any],
    sources: dict[str, dict[str, Any]],
) -> tuple[bool, list[str]]:
    failures: list[str] = []
    claim_type = str(claim.get("claim_type", ""))
    status = str(claim.get("verification_status", ""))
    source_ids = claim.get("source_ids")
    methods = set(claim.get("verification_methods") or [])

    if status not in {"verified", "contested"}:
        failures.append("verification status is not release accepted")
    if claim_type not in {"instructional_scenario", "hardeep_position", "unresolved_question"}:
        if not isinstance(source_ids, list) or not source_ids:
            failures.append("no source identifiers")
    for source_id in source_ids or []:
        source = sources.get(str(source_id))
        if not source:
            failures.append(f"unknown source {source_id}")
            continue
        if not source.get("locator"):
            failures.append(f"source {source_id} has no exact locator")
        if source.get("verification_status") != "verified":
            failures.append(f"source {source_id} is not verified")
    if claim_type not in {"instructional_scenario", "hardeep_position", "unresolved_question"}:
        if "source_trace" not in methods:
            failures.append("no independent source trace")
    if claim.get("technical") is True or claim_type in TECHNICAL_CLAIM_TYPES:
        if "qualified_technical_review" not in methods:
            failures.append("no qualified technical review")
        if not claim.get("technical_reviewer"):
            failures.append("no qualified technical reviewer")
    if claim_type == "regulatory_requirement":
        if "jurisdiction_effective_date_review" not in methods:
            failures.append("no jurisdiction and effective-date review")
        if not claim.get("jurisdiction") or not claim.get("effective_date"):
            failures.append("missing jurisdiction or effective date")
    if not claim.get("independent_verifier"):
        failures.append("no independent verifier")
    if not claim.get("verified_on") or not claim.get("next_review_on"):
        failures.append("missing verification or freshness date")
    if not claim.get("affected_blocks"):
        failures.append("claim is not mapped to narrative blocks")
    if status == "contested" and not claim.get("contested_boundary"):
        failures.append("contested claim has no visible boundary")
    return not failures, failures


def validate_package(package_dir: Path, *, release_ready: bool = False) -> dict[str, Any]:
    package_dir = package_dir.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for name in REQUIRED_FILES:
        if not (package_dir / name).is_file():
            errors.append(f"missing required package file: {name}")
    if errors:
        raise ConceptBriefError("\n".join(errors))

    # The production contract lists white-paper.md in the governed package: it is
    # the teaching artifact every later stage is derived from. It is warned here
    # rather than added to REQUIRED_FILES so that an existing package is not
    # failed into a fabricated paper, and it is a hard gate at release.
    if not (package_dir / "white-paper.md").is_file():
        message = (
            "missing white-paper.md: the production contract requires the research "
            "white paper as the teaching source for storyboard, visuals, and claims"
        )
        if release_ready:
            errors.append(message)
        else:
            warnings.append(message)

    intake = load_yaml(package_dir / "intake.yaml")
    brief_data = load_yaml(package_dir / "brief.yaml")
    storyboard = load_yaml(package_dir / "storyboard.yaml")
    narrative_data = load_yaml(package_dir / "narrative.yaml")
    learning = load_yaml(package_dir / "learning.yaml")
    assessment_data = load_yaml(package_dir / "assessments.yaml")
    claim_data = load_yaml(package_dir / "claims.yaml")
    source_data = load_yaml(package_dir / "sources.yaml")
    visual_data = load_yaml(package_dir / "visuals/visual-manifest.yaml")
    interaction_data = load_yaml(package_dir / "interactions.yaml")
    graph_data = load_yaml(package_dir / "graph.yaml")
    community = load_yaml(package_dir / "community.yaml")
    commercial = load_yaml(package_dir / "commercial.yaml")
    qa = load_yaml(package_dir / "qa.yaml")
    approvals_data = load_yaml(package_dir / "approvals.yaml")

    documents = (
        ("intake", intake),
        ("brief", brief_data),
        ("storyboard", storyboard),
        ("narrative", narrative_data),
        ("learning", learning),
        ("assessments", assessment_data),
        ("claims", claim_data),
        ("sources", source_data),
        ("visual manifest", visual_data),
        ("interactions", interaction_data),
        ("graph", graph_data),
        ("community", community),
        ("commercial", commercial),
        ("QA", qa),
        ("approvals", approvals_data),
    )
    for label, document in documents:
        if document.get("schema_version") != 1:
            errors.append(f"{label}: schema_version must be 1")
        if document.get("contract") != CONTRACT:
            errors.append(f"{label}: contract must be {CONTRACT}")

    brief = brief_data.get("brief")
    design = brief_data.get("design_fingerprint")
    if not isinstance(brief, dict):
        errors.append("brief.yaml: brief must be an object")
        brief = {}
    if not isinstance(design, dict):
        errors.append("brief.yaml: design_fingerprint must be an object")
        design = {}
    require_fields(
        brief,
        (
            "brief_id",
            "slug",
            "title",
            "version",
            "status",
            "owner",
            "promise",
            "audiences",
            "scope",
            "authority_scope",
            "evidence_cutoff",
            "language",
        ),
        "brief",
        errors,
    )
    if brief.get("authority_scope") != "united_states_only":
        errors.append("brief: authority_scope must be united_states_only")
    require_fields(
        design,
        (
            "learner_job",
            "opening_pattern",
            "narrative_archetype",
            "central_mental_model",
            "signature_mechanism",
            "dominant_visual",
            "interaction_signature",
            "role_treatment",
            "closing_action",
            "surface_rhythm",
            "intentionally_avoided",
            "adjacent_differences",
        ),
        "design fingerprint",
        errors,
    )
    brief_id = str(brief.get("brief_id", ""))
    for label, document in documents:
        if brief_id and document.get("brief_id") != brief_id:
            errors.append(f"{label}: brief_id does not match {brief_id}")

    learning_profile = learning.get("learning")
    completion = learning.get("completion")
    continuing_education = learning.get("continuing_education")
    placement = learning.get("placement")
    capability_lock = learning.get("capability_lock")
    learning_events = learning.get("learning_events")
    assessment_governance = learning.get("assessment_governance")
    simulation_assurance = learning.get("simulation_assurance")
    language_units_time = learning.get("language_units_time")
    learner_experience = learning.get("learner_experience")
    credential_readiness = learning.get("credential_readiness")
    learning_pathways = learning.get("learning_pathways")
    if not isinstance(learning_profile, dict):
        errors.append("learning.yaml: learning must be an object")
        learning_profile = {}
    if not isinstance(completion, dict):
        errors.append("learning.yaml: completion must be an object")
        completion = {}
    if not isinstance(continuing_education, dict):
        errors.append("learning.yaml: continuing_education must be an object")
        continuing_education = {}
    learning_contracts = (
        ("placement", placement),
        ("capability_lock", capability_lock),
        ("learning_events", learning_events),
        ("assessment_governance", assessment_governance),
        ("simulation_assurance", simulation_assurance),
        ("language_units_time", language_units_time),
        ("learner_experience", learner_experience),
        ("credential_readiness", credential_readiness),
        ("learning_pathways", learning_pathways),
    )
    for label, record in learning_contracts:
        if not isinstance(record, dict):
            errors.append(f"learning.yaml: {label} must be an object")
    placement = placement if isinstance(placement, dict) else {}
    capability_lock = capability_lock if isinstance(capability_lock, dict) else {}
    learning_events = learning_events if isinstance(learning_events, dict) else {}
    assessment_governance = (
        assessment_governance if isinstance(assessment_governance, dict) else {}
    )
    simulation_assurance = (
        simulation_assurance if isinstance(simulation_assurance, dict) else {}
    )
    language_units_time = (
        language_units_time if isinstance(language_units_time, dict) else {}
    )
    learner_experience = (
        learner_experience if isinstance(learner_experience, dict) else {}
    )
    credential_readiness = (
        credential_readiness if isinstance(credential_readiness, dict) else {}
    )
    learning_pathways = (
        learning_pathways if isinstance(learning_pathways, dict) else {}
    )
    require_fields(
        learning_profile,
        (
            "outcomes",
            "prior_knowledge",
            "misconception",
            "transfer_task",
            "cross_sector_connections",
            "experience_profile",
        ),
        "learning profile",
        errors,
    )
    require_fields(completion, ("required_ids", "rule"), "learning completion", errors)
    require_fields(
        continuing_education,
        (
            "state",
            "credit_claim",
            "instructional_time_basis",
            "identity_evidence",
            "participation_evidence",
            "assessment_rule",
            "completion_record",
            "content_version",
            "provider_record",
            "evaluation_record",
            "accreditor_approval",
        ),
        "continuing education",
        errors,
    )
    if continuing_education.get("credit_claim") not in {"disabled", "approved"}:
        errors.append("continuing education: credit_claim must be disabled or approved")
    if (
        continuing_education.get("credit_claim") == "approved"
        and continuing_education.get("accreditor_approval") != "approved"
    ):
        errors.append(
            "continuing education: credit_claim requires explicit accreditor approval"
        )
    require_fields(
        credential_readiness,
        (
            "contract",
            "event_profile",
            "lms_launch_preferred",
            "legacy_lms_adapter",
            "portable_credential_target",
            "learner_record_export_target",
            "credit_profile_id",
            "credit_claim",
            "certificate_state",
        ),
        "credential readiness",
        errors,
    )
    credential_contract = LEARNING_CAPABILITIES["credential_and_pathway_contract"]
    credential_expectations = {
        "contract": credential_contract["contract"],
        "event_profile": credential_contract["canonical_event_profile"],
        "lms_launch_preferred": credential_contract["preferred_lms_launch"],
        "legacy_lms_adapter": credential_contract["legacy_lms_adapter"],
        "portable_credential_target": credential_contract["portable_credential_target"],
        "learner_record_export_target": credential_contract["learner_record_export_target"],
    }
    for field, expected in credential_expectations.items():
        if credential_readiness.get(field) != expected:
            errors.append(
                f"credential readiness: {field} must match shared registry value {expected}"
            )
    if credential_readiness.get("credit_claim") != continuing_education.get(
        "credit_claim"
    ):
        errors.append(
            "credential readiness: credit_claim must match continuing education"
        )
    require_fields(
        learning_pathways,
        (
            "recommendation_policy",
            "lanes",
            "explainability_required",
            "learner_control_required",
            "protected_traits_prohibited",
            "facility_sensitive_data_prohibited",
        ),
        "learning pathways",
        errors,
    )
    if set(learning_pathways.get("lanes", [])) != set(
        credential_contract["required_recommendation_lanes"]
    ):
        errors.append(
            "learning pathways: lanes must be deepen, reskill, and cross-skill"
        )
    for field in (
        "explainability_required",
        "learner_control_required",
        "protected_traits_prohibited",
        "facility_sensitive_data_prohibited",
    ):
        if learning_pathways.get(field) is not True:
            errors.append(f"learning pathways: {field} must be true")
    require_fields(
        placement,
        ("content_type",),
        "learning placement",
        errors,
    )
    if placement.get("content_type") != "concept_brief":
        errors.append("learning placement: content_type must be concept_brief")
    for field in (
        "prerequisite_brief_ids",
        "remediation_brief_ids",
        "next_learning_ids",
        "course_connections",
    ):
        if field not in placement:
            errors.append(f"learning placement: missing {field}")
            continue
        value = placement.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            errors.append(f"learning placement.{field} must be a list of strings")
    require_fields(
        capability_lock,
        (
            "registry_id",
            "registry_version",
            "required_capability_ids",
            "compatibility_policy",
        ),
        "learning capability lock",
        errors,
    )
    if capability_lock.get("registry_id") != LEARNING_CAPABILITIES["registry_id"]:
        errors.append("learning capability lock: registry_id does not match the shared registry")
    if capability_lock.get("registry_version") != LEARNING_CAPABILITIES["registry_version"]:
        errors.append(
            "learning capability lock: registry_version does not match the shared registry"
        )
    locked_capabilities = capability_lock.get("required_capability_ids")
    if not isinstance(locked_capabilities, list) or not all(
        isinstance(item, str) for item in locked_capabilities
    ):
        errors.append(
            "learning capability lock.required_capability_ids must be a list of strings"
        )
        locked_capabilities = []
    elif len(set(locked_capabilities)) != len(locked_capabilities):
        errors.append("learning capability lock: required_capability_ids must be unique")
    require_fields(
        learning_events,
        (
            "event_namespace",
            "stable_event_ids",
            "attempt_policy",
            "record_authority",
            "privacy_classification",
            "consent_boundary",
            "retention_rule",
            "facility_sensitive_data_collection",
            "privacy_review_status",
            "supersession_policy",
            "material_correction_notification",
        ),
        "learning events",
        errors,
    )
    stable_event_ids = learning_events.get("stable_event_ids")
    if not isinstance(stable_event_ids, list) or not all(
        isinstance(item, str) for item in stable_event_ids
    ):
        errors.append("learning events.stable_event_ids must be a list of strings")
    elif len(set(stable_event_ids)) != len(stable_event_ids):
        errors.append("learning events: stable_event_ids must be unique")
    if learning_events.get("facility_sensitive_data_collection") != "prohibited":
        errors.append(
            "learning events: facility_sensitive_data_collection must be prohibited"
        )
    if release_ready and learning_events.get("privacy_review_status") != "approved":
        errors.append("learning events: release requires approved privacy review")
    require_fields(
        assessment_governance,
        (
            "passing_rule",
            "retry_policy",
            "item_version_policy",
            "feedback_policy",
            "accommodation_policy",
            "review_status",
        ),
        "assessment governance",
        errors,
    )
    if release_ready and assessment_governance.get("review_status") != "approved":
        errors.append("assessment governance: release requires approved review")
    require_fields(
        simulation_assurance,
        (
            "model_id",
            "model_version",
            "assumptions_visible",
            "illustrative_values_labeled",
            "deterministic_replay",
            "qualified_review_required",
            "operational_use",
        ),
        "simulation assurance",
        errors,
    )
    for field in (
        "assumptions_visible",
        "illustrative_values_labeled",
        "qualified_review_required",
    ):
        if simulation_assurance.get(field) is not True:
            errors.append(f"simulation assurance: {field} must be true")
    if simulation_assurance.get("operational_use") != "prohibited":
        errors.append("simulation assurance: operational_use must be prohibited")
    require_fields(
        language_units_time,
        (
            "primary_language",
            "reading_target",
            "unit_policy",
            "localization_state",
            "instructional_minutes",
            "active_participation_minutes",
            "assessment_minutes",
            "timing_method",
        ),
        "language, units, and time",
        errors,
    )
    require_fields(
        learner_experience,
        (
            "quick_orientation",
            "primary_navigation_maximum",
            "closing_recap_labels",
            "comment_placement",
            "community_mode",
            "sop_boundary",
            "inactive_commercial_placement",
            "learner_facing_governance_metadata",
            "orientation",
        ),
        "learner experience",
        errors,
    )
    orientation = learner_experience.get("orientation")
    if not isinstance(orientation, dict):
        errors.append("learner experience: orientation must be an object")
    else:
        require_fields(
            orientation,
            (
                "subject",
                "audience",
                "why_it_matters",
                "time_estimate",
                "scope_boundary",
            ),
            "learner experience orientation",
            errors,
        )
    if learner_experience.get("primary_navigation_maximum") != 4:
        errors.append("learner experience: primary_navigation_maximum must be 4")
    if learner_experience.get("comment_placement") != "after_learning_and_commercial":
        errors.append(
            "learner experience: comment_placement must be after_learning_and_commercial"
        )
    if learner_experience.get("community_mode") != "compact_entry_plus_drawer":
        errors.append(
            "learner experience: community_mode must be compact_entry_plus_drawer"
        )
    if learner_experience.get("sop_boundary") != "outline_only":
        errors.append("learner experience: sop_boundary must be outline_only")
    if learner_experience.get("inactive_commercial_placement") != "hidden":
        errors.append("learner experience: inactive_commercial_placement must be hidden")
    if learner_experience.get("learner_facing_governance_metadata") != "minimal":
        errors.append(
            "learner experience: learner_facing_governance_metadata must be minimal"
        )

    intake_items = unique_records(intake.get("items"), "source_item_id", "intake items", errors)
    for item_id, item in intake_items.items():
        require_fields(
            item,
            (
                "kind",
                "title",
                "original_locator",
                "creator",
                "captured_on",
                "visibility",
                "permission_status",
                "extraction_coverage",
                "limitations",
                "disposition",
            ),
            f"intake item {item_id}",
            errors,
        )
        snapshot = item.get("snapshot_locator")
        checksum = item.get("checksum_sha256")
        if release_ready and (not snapshot or not checksum):
            errors.append(f"intake item {item_id}: release requires a snapshot and checksum")
        if snapshot:
            snapshot_path = package_dir / str(snapshot)
            if not snapshot_path.is_file():
                errors.append(f"intake item {item_id}: snapshot does not exist: {snapshot}")
            elif checksum:
                actual = hashlib.sha256(snapshot_path.read_bytes()).hexdigest()
                if actual != checksum:
                    errors.append(f"intake item {item_id}: snapshot checksum does not match")

    sources = unique_records(source_data.get("sources"), "source_id", "sources", errors)
    for source_id, source in sources.items():
        require_fields(
            source,
            (
                "title",
                "source_type",
                "authority_tier",
                "country",
                "governing_use",
                "issuer_or_author",
                "locator",
                "published_or_effective",
                "accessed_on",
                "permission_status",
                "verification_status",
                "limitations",
            ),
            f"source {source_id}",
            errors,
        )
        if source.get("verification_status") not in {"pending", "verified", "rejected", "superseded"}:
            errors.append(f"source {source_id}: invalid verification_status")
        country = str(source.get("country", ""))
        governing_use = str(source.get("governing_use", ""))
        if governing_use not in {
            "us_governing_or_context",
            "research_only",
            "source_material_only",
        }:
            errors.append(f"source {source_id}: invalid governing_use")
        if governing_use == "us_governing_or_context" and country != "United States":
            errors.append(
                f"source {source_id}: governing authority must be from the United States"
            )
        if governing_use == "research_only" and source.get("authority_tier") != "peer_reviewed_research":
            errors.append(
                f"source {source_id}: research_only requires peer_reviewed_research authority"
            )
        if country not in {"United States", "not_applicable"} and governing_use != "research_only":
            errors.append(
                f"source {source_id}: non-United States source may be used only as research"
            )
        if release_ready and source.get("verification_status") != "verified":
            errors.append(f"source {source_id}: release requires verified source status")

    claims = unique_records(claim_data.get("claims"), "claim_id", "claims", errors)
    material_claims: list[dict[str, Any]] = []
    release_verified_claims: list[dict[str, Any]] = []
    for claim_id, claim in claims.items():
        require_fields(
            claim,
            (
                "claim_text",
                "claim_type",
                "material",
                "evidence_tier",
                "verification_status",
                "scope",
                "limitations",
                "affected_blocks",
            ),
            f"claim {claim_id}",
            errors,
        )
        if claim.get("claim_type") not in CLAIM_TYPES:
            errors.append(f"claim {claim_id}: unsupported claim_type")
        if claim.get("verification_status") not in CLAIM_STATUSES:
            errors.append(f"claim {claim_id}: unsupported verification_status")
        if claim.get("claim_type") in {"regulatory_requirement", "technical_standard"}:
            for source_id in claim.get("source_ids") or []:
                source = sources.get(str(source_id), {})
                if source.get("governing_use") == "research_only":
                    errors.append(
                        f"claim {claim_id}: research-only source cannot support a "
                        f"{claim.get('claim_type')}"
                    )
        if claim.get("material") is True:
            material_claims.append(claim)
            verified, failures = _verification_state(claim, sources)
            if verified:
                release_verified_claims.append(claim)
            elif release_ready:
                for failure in failures:
                    errors.append(f"claim {claim_id}: {failure}")
            else:
                warnings.append(f"claim {claim_id}: " + "; ".join(failures))

    blocks = unique_records(narrative_data.get("blocks"), "block_id", "narrative blocks", errors)
    for block_id, block in blocks.items():
        require_fields(block, ("type", "title", "body", "claim_ids"), f"block {block_id}", errors)
        if block.get("type") not in BLOCK_TYPES:
            errors.append(f"block {block_id}: unsupported type {block.get('type')}")
        for claim_id in block.get("claim_ids") or []:
            if str(claim_id) not in claims:
                errors.append(f"block {block_id}: unknown claim {claim_id}")
        if block.get("type") == "definition":
            entries = block.get("terms")
            if not isinstance(entries, list) or not entries:
                errors.append(f"block {block_id}: definition block requires terms")
                continue
            for position, entry in enumerate(entries, start=1):
                if not isinstance(entry, dict):
                    errors.append(
                        f"block {block_id} term {position}: expected an object"
                    )
                    continue
                require_fields(
                    entry,
                    DEFINITION_FIELDS,
                    f"block {block_id} term {position}",
                    errors,
                )
        if block.get("type") == "example":
            require_fields(block, EXAMPLE_FIELDS, f"block {block_id}", errors)

    beats = storyboard.get("beats")
    if not isinstance(beats, list) or len(beats) < 2:
        errors.append("storyboard: at least two beats are required")
        beats = []
    seen_beat_ids: set[str] = set()
    for index, beat in enumerate(beats, start=1):
        if not isinstance(beat, dict):
            errors.append(f"storyboard beat {index}: expected an object")
            continue
        require_fields(
            beat,
            (
                "beat_id",
                "learner_question",
                "instructor_purpose",
                "block_ids",
                "learner_action",
                "intended_realization",
                "transition",
                "surface",
                "mobile_treatment",
                "reduced_motion_treatment",
            ),
            f"storyboard beat {index}",
            errors,
        )
        beat_id = str(beat.get("beat_id", ""))
        if beat_id in seen_beat_ids:
            errors.append(f"storyboard: duplicate beat_id {beat_id}")
        seen_beat_ids.add(beat_id)
        if beat.get("surface") not in SURFACES:
            errors.append(f"storyboard beat {beat_id}: unsupported surface")
        for block_id in beat.get("block_ids") or []:
            if str(block_id) not in blocks:
                errors.append(f"storyboard beat {beat_id}: unknown block {block_id}")

    visuals = unique_records(visual_data.get("visuals"), "visual_id", "visuals", errors)
    for visual_id, visual in visuals.items():
        require_fields(
            visual,
            (
                "title",
                "asset_class",
                "teaching_idea",
                "learner_conclusion",
                "reading_guide",
                "alternative_text",
                "mobile_treatment",
                "reduced_motion_treatment",
                "creator",
                "source",
                "license",
                "permission_status",
                "originality_status",
                "storyboard_status",
                "rendered_review_status",
            ),
            f"visual {visual_id}",
            errors,
        )
        locator = visual.get("locator")
        component_id = visual.get("component_id")
        if not locator and not component_id:
            errors.append(f"visual {visual_id}: locator or component_id is required")
        if locator and not (package_dir / str(locator)).is_file():
            errors.append(f"visual {visual_id}: asset does not exist: {locator}")
        if component_id and component_id not in SUPPORTED_VISUAL_COMPONENTS:
            errors.append(
                f"visual {visual_id}: unsupported shared component_id {component_id}"
            )
        if release_ready:
            for field in (
                "permission_status",
                "originality_status",
                "storyboard_status",
                "rendered_review_status",
            ):
                if visual.get(field) != "approved":
                    errors.append(f"visual {visual_id}: {field} is not approved")

    interactions = unique_records(
        interaction_data.get("interactions"),
        "interaction_id",
        "interactions",
        errors,
    )
    for interaction_id, interaction in interactions.items():
        require_fields(
            interaction,
            (
                "title",
                "component",
                "teaching_job",
                "model_boundary",
                "inputs",
                "outputs",
                "failure_states",
                "keyboard_behavior",
                "touch_behavior",
                "live_feedback",
                "mobile_treatment",
                "reduced_motion_treatment",
                "completion_evidence",
                "review_status",
            ),
            f"interaction {interaction_id}",
            errors,
        )
        if interaction.get("component") not in SUPPORTED_INTERACTIONS:
            errors.append(
                f"interaction {interaction_id}: unsupported shared component "
                f"{interaction.get('component')}"
            )
        if interaction.get("dynamic_concept") is True:
            require_fields(
                interaction,
                (
                    "motion_behavior",
                    "no_javascript_treatment",
                    "reduced_motion_treatment",
                ),
                f"dynamic interaction {interaction_id}",
                errors,
            )
        if release_ready and interaction.get("review_status") != "approved":
            errors.append(f"interaction {interaction_id}: review_status is not approved")

    assessments = unique_records(
        assessment_data.get("assessments"),
        "assessment_id",
        "assessments",
        errors,
    )
    for assessment_id, assessment in assessments.items():
        require_fields(
            assessment,
            (
                "version",
                "type",
                "cognitive_job",
                "prompt",
                "feedback",
                "retry",
                "completion_id",
                "review_status",
            ),
            f"assessment {assessment_id}",
            errors,
        )
        assessment_type = assessment.get("type")
        if assessment_type not in SUPPORTED_ASSESSMENTS:
            errors.append(
                f"assessment {assessment_id}: unsupported shared assessment type "
                f"{assessment_type}"
            )
        if assessment_type == "multiple-choice":
            options = assessment.get("options")
            if not isinstance(options, list) or len(options) < 2:
                errors.append(f"assessment {assessment_id}: multiple-choice needs options")
            elif sum(
                bool(option.get("correct"))
                for option in options
                if isinstance(option, dict)
            ) != 1:
                errors.append(
                    f"assessment {assessment_id}: exactly one option must be correct"
                )
        if assessment_type == "multi-select":
            options = assessment.get("options")
            if not isinstance(options, list) or len(options) < 3:
                errors.append(f"assessment {assessment_id}: multi-select needs options")
            elif not any(
                bool(option.get("correct"))
                for option in options
                if isinstance(option, dict)
            ):
                errors.append(
                    f"assessment {assessment_id}: multi-select needs a correct option"
                )
        if assessment_type == "reflection":
            if not assessment.get("model_response"):
                errors.append(f"assessment {assessment_id}: reflection needs model_response")
            worked_example = assessment.get("worked_example")
            if assessment.get("guided_rehearsal") is True:
                if not isinstance(worked_example, dict):
                    errors.append(
                        f"assessment {assessment_id}: guided reflection needs worked_example"
                    )
                else:
                    require_fields(
                        worked_example,
                        ("scenario", "shortcut", "steps", "result"),
                        f"assessment {assessment_id} worked_example",
                        errors,
                    )
                    steps = worked_example.get("steps")
                    if not isinstance(steps, list) or len(steps) < 3:
                        errors.append(
                            f"assessment {assessment_id}: worked_example needs at least three steps"
                        )
            if assessment.get("optional") is not True:
                errors.append(
                    f"assessment {assessment_id}: public reflection practice must be optional"
                )
        if assessment_type == "flip-cards":
            cards = assessment.get("cards")
            if not isinstance(cards, list) or len(cards) < 3:
                errors.append(f"assessment {assessment_id}: flip-cards needs three cards")
        if assessment_type == "matching":
            pairs = assessment.get("pairs")
            targets = assessment.get("targets")
            if not isinstance(pairs, list) or len(pairs) < 3:
                errors.append(f"assessment {assessment_id}: matching needs three pairs")
            if not isinstance(targets, list) or len(targets) < 3:
                errors.append(f"assessment {assessment_id}: matching needs three targets")
            # A pair whose prompt or answer key is missing renders a blank row and
            # grades against an empty string, so the check silently stops working.
            if isinstance(pairs, list):
                for position, pair in enumerate(pairs, start=1):
                    if not isinstance(pair, dict):
                        errors.append(
                            f"assessment {assessment_id} pair {position}: expected an object"
                        )
                        continue
                    prompt_text = _match_pair_prompt(pair)
                    answer_text = _match_pair_answer(pair)
                    if not str(prompt_text).strip():
                        errors.append(
                            f"assessment {assessment_id} pair {position}: needs a visible "
                            "statement in left or prompt"
                        )
                    if not str(answer_text).strip():
                        errors.append(
                            f"assessment {assessment_id} pair {position}: needs an answer "
                            "in right or answer"
                        )
                    elif isinstance(targets, list) and answer_text not in targets:
                        errors.append(
                            f"assessment {assessment_id} pair {position}: answer "
                            f"{answer_text!r} is not one of the declared targets"
                        )
        if assessment_type == "applied-work-product":
            fields = assessment.get("required_fields")
            if not isinstance(fields, list) or not fields:
                errors.append(
                    f"assessment {assessment_id}: applied work product needs required_fields"
                )
        if release_ready and assessment.get("review_status") != "approved":
            errors.append(f"assessment {assessment_id}: review_status is not approved")

    used_assessments: set[str] = set()
    for block_id, block in blocks.items():
        if block.get("type") != "assessment":
            continue
        assessment_id = str(block.get("assessment_id", ""))
        if assessment_id not in assessments:
            errors.append(f"block {block_id}: unknown assessment {assessment_id}")
        else:
            used_assessments.add(assessment_id)
    unused_assessments = sorted(set(assessments) - used_assessments)
    if unused_assessments:
        errors.append(
            "assessment manifest contains unused assessments: "
            + ", ".join(unused_assessments)
        )

    experience_profile = learning_profile.get("experience_profile")
    if not isinstance(experience_profile, dict):
        errors.append("learning profile: experience_profile must be an object")
        experience_profile = {}
    required_dynamic = EXPERIENCE_CONTRACT["dynamic_explanation_required"]
    if required_dynamic and experience_profile.get("dynamic_explanation_required") is not True:
        errors.append("learning profile: dynamic_explanation_required must be true")
    dynamic_interactions = [
        item for item in interactions.values() if item.get("dynamic_concept") is True
    ]
    if required_dynamic and not dynamic_interactions:
        errors.append("Concept Brief requires at least one dynamic concept interaction")
    visual_minimum = int(EXPERIENCE_CONTRACT["visual_explanations_minimum"])
    if len(visuals) < visual_minimum:
        errors.append(
            f"Concept Brief requires at least {visual_minimum} explanatory visuals"
        )
    check_minimum = int(EXPERIENCE_CONTRACT["distributed_checks_minimum"])
    if len(assessments) < check_minimum:
        errors.append(f"Concept Brief requires at least {check_minimum} learning checks")
    if not any(item.get("final_applied_check") is True for item in assessments.values()):
        errors.append("Concept Brief requires one final applied check")
    cross_sector = learning_profile.get("cross_sector_connections")
    if not isinstance(cross_sector, list) or not cross_sector:
        errors.append("Concept Brief requires a cross-sector connection")

    definition_blocks = [
        block_id
        for block_id, block in blocks.items()
        if block.get("type") == "definition"
    ]
    if not definition_blocks:
        errors.append(
            "Concept Brief requires at least one definition block that defines its "
            "dependent terms in plain English before first use"
        )
    if not any(block.get("type") == "example" for block in blocks.values()):
        errors.append(
            "Concept Brief requires at least one worked example block"
        )

    ordered_block_ids: list[str] = []
    for beat in beats:
        if not isinstance(beat, dict):
            continue
        for block_id in beat.get("block_ids") or []:
            if str(block_id) not in ordered_block_ids:
                ordered_block_ids.append(str(block_id))
    if definition_blocks and ordered_block_ids:
        first_definition = min(
            (
                ordered_block_ids.index(block_id)
                for block_id in definition_blocks
                if block_id in ordered_block_ids
            ),
            default=None,
        )
        first_teaching = next(
            (
                index
                for index, block_id in enumerate(ordered_block_ids)
                if blocks.get(block_id, {}).get("type")
                in {"visual", "interaction", "assessment"}
            ),
            None,
        )
        if first_definition is None:
            errors.append(
                "Concept Brief: no definition block is placed in the storyboard"
            )
        elif first_teaching is not None and first_definition > first_teaching:
            errors.append(
                "Concept Brief: definitions must be placed before the first visual, "
                "interaction, or check so terms are defined before use"
            )

    used_capability_ids = {
        str(item.get("component"))
        for item in interactions.values()
        if item.get("component")
    }
    used_capability_ids.update(
        str(item.get("type")) for item in assessments.values() if item.get("type")
    )
    used_capability_ids.update(
        str(item.get("component_id"))
        for item in visuals.values()
        if item.get("component_id")
    )
    missing_capability_locks = sorted(used_capability_ids - set(locked_capabilities))
    if missing_capability_locks:
        errors.append(
            "learning capability lock is missing used capabilities: "
            + ", ".join(missing_capability_locks)
        )
    unknown_capability_locks = sorted(
        set(locked_capabilities)
        - (
            SUPPORTED_ASSESSMENTS
            | SUPPORTED_INTERACTIONS
            | SUPPORTED_VISUAL_COMPONENTS
        )
    )
    if unknown_capability_locks:
        errors.append(
            "learning capability lock contains unknown capabilities: "
            + ", ".join(unknown_capability_locks)
        )
    dynamic_model_ids = {
        str(item.get("component"))
        for item in dynamic_interactions
        if item.get("component")
    }
    if simulation_assurance.get("model_id") not in dynamic_model_ids:
        errors.append(
            "simulation assurance.model_id must identify a declared dynamic interaction"
        )

    required_ids = completion.get("required_ids", [])
    if not isinstance(required_ids, list) or not all(
        isinstance(item, str) for item in required_ids
    ):
        errors.append("learning completion.required_ids must be a list of strings")
        required_ids = []
    produced_ids = {
        str(record.get("completion_id"))
        for record in [*interactions.values(), *assessments.values()]
        if record.get("completion_id")
    }
    missing_completion = sorted(set(required_ids) - produced_ids)
    if missing_completion:
        errors.append(
            "learning completion IDs have no producing component: "
            + ", ".join(missing_completion)
        )

    nodes = unique_records(graph_data.get("nodes"), "node_id", "graph nodes", errors)
    edges = unique_records(graph_data.get("edges"), "edge_id", "graph edges", errors)
    if brief_id and brief_id not in nodes:
        errors.append("graph: brief node is missing")
    for edge_id, edge in edges.items():
        require_fields(
            edge,
            (
                "edge_type",
                "from_node",
                "to_node",
                "provenance",
                "review_status",
                "visibility",
                "editorial_use",
            ),
            f"graph edge {edge_id}",
            errors,
        )
        edge_type = edge.get("edge_type")
        if edge_type not in EDGE_TYPES:
            errors.append(f"graph edge {edge_id}: unsupported edge_type")
        if str(edge.get("from_node")) not in nodes or str(edge.get("to_node")) not in nodes:
            errors.append(f"graph edge {edge_id}: endpoint does not resolve")
        if edge_type == "SPONSORED_BY" and edge.get("editorial_use") != "prohibited":
            errors.append(f"graph edge {edge_id}: sponsorship must prohibit editorial use")
        if edge_type == "CITES" and str(edge.get("to_node")) not in {
            f"source:{source_id}" for source_id in sources
        }:
            errors.append(f"graph edge {edge_id}: CITES must target a declared source node")
        if release_ready and edge.get("review_status") != "approved":
            errors.append(f"graph edge {edge_id}: review_status is not approved")

    require_fields(
        community,
        (
            "forum_space_id",
            "mount_id",
            "version_context",
            "seed_questions",
            "moderation_owner",
            "verified_answer_policy",
            "discussion_boundary",
            "correction_escalation",
            "focus_return",
            "review_status",
        ),
        "community",
        errors,
    )
    if community.get("mount_id") != "owos-concept-community":
        errors.append("community: mount_id must be owos-concept-community")
    if release_ready and community.get("review_status") != "approved":
        errors.append("community: review_status is not approved")

    require_fields(
        commercial,
        (
            "state",
            "editorial_firewall",
            "ranking_policy",
            "review_status",
        ),
        "commercial",
        errors,
    )
    if not isinstance(commercial.get("relationships"), list):
        errors.append("commercial: relationships must be a list")
    if not isinstance(commercial.get("conflicts"), list):
        errors.append("commercial: conflicts must be a list")
    if commercial.get("editorial_firewall") is not True:
        errors.append("commercial: editorial_firewall must be true")
    for index, relationship in enumerate(commercial.get("relationships") or [], start=1):
        if not isinstance(relationship, dict):
            errors.append(f"commercial relationship {index}: expected an object")
            continue
        require_fields(
            relationship,
            ("organization_node", "relationship_type", "disclosure", "editorial_rights"),
            f"commercial relationship {index}",
            errors,
        )
        if relationship.get("editorial_rights") != "none":
            errors.append(f"commercial relationship {index}: editorial_rights must be none")
    if release_ready and commercial.get("review_status") != "approved":
        errors.append("commercial: review_status is not approved")

    qa_gates = qa.get("hard_gates")
    manual_reviews = qa.get("manual_reviews")
    if not isinstance(qa_gates, dict):
        errors.append("QA: hard_gates must be an object")
        qa_gates = {}
    if not isinstance(manual_reviews, dict):
        errors.append("QA: manual_reviews must be an object")
        manual_reviews = {}
    for gate in HARD_GATES:
        if gate not in qa_gates:
            errors.append(f"QA: missing hard gate {gate}")
        elif release_ready and qa_gates.get(gate) != "passed":
            errors.append(f"QA hard gate {gate} must be passed for release")
    for review in MANUAL_REVIEWS:
        if review not in manual_reviews:
            errors.append(f"QA: missing manual review {review}")
        elif release_ready and manual_reviews.get(review) != "completed":
            errors.append(f"QA manual review {review} must be completed for release")

    coverage = (
        100.0
        if not material_claims
        else round(len(release_verified_claims) / len(material_claims) * 100, 2)
    )
    declared_coverage = qa.get("verification_coverage_percent")
    if declared_coverage != coverage:
        errors.append(
            "QA: verification_coverage_percent does not match computed coverage "
            f"({coverage})"
        )
    if release_ready and coverage != 100.0:
        errors.append("QA: release requires 100 percent material-claim verification coverage")

    approvals = approvals_data.get("approvals")
    if not isinstance(approvals, dict):
        errors.append("approvals: approvals must be an object")
        approvals = {}
    for approval in APPROVALS:
        if approval not in approvals:
            errors.append(f"approvals: missing {approval}")
        elif release_ready and approvals.get(approval, {}).get("status") != "approved":
            errors.append(f"approval {approval} must be approved for release")
    if release_ready and not approvals_data.get("release_build_timestamp"):
        errors.append("approvals: release_build_timestamp is required for release")

    learner_text = "\n".join(text_values(narrative_data))
    if "—" in learner_text or "–" in learner_text:
        errors.append("narrative: prohibited em dash or en dash")
    lower_text = learner_text.lower()
    for phrase in BANNED_PHRASES:
        if re.search(rf"\b{re.escape(phrase)}\b", lower_text):
            errors.append(f"narrative: prohibited phrase: {phrase}")

    if release_ready and brief.get("status") != "release_approved":
        errors.append("brief: status must be release_approved for release")
    if not blocks:
        errors.append("narrative: at least one block is required")

    if errors:
        raise ConceptBriefError("\n".join(errors))

    return {
        "package_dir": package_dir,
        "brief": brief,
        "design": design,
        "intake": intake,
        "storyboard": storyboard,
        "blocks": blocks,
        "claims": claims,
        "sources": sources,
        "visuals": visuals,
        "interactions": interactions,
        "assessments": assessments,
        "learning": learning,
        "nodes": nodes,
        "edges": edges,
        "community": community,
        "commercial": commercial,
        "qa": qa,
        "approvals": approvals_data,
        "verification_coverage_percent": coverage,
        "checksum": package_checksum(package_dir),
        "release_ready": release_ready,
        "warnings": warnings,
    }


def _claim_badges(block: dict[str, Any], claims: dict[str, dict[str, Any]]) -> str:
    badges = []
    seen: set[tuple[str, str]] = set()
    tier_labels = {
        "government_guidance": "REGULATORY CONTEXT",
        "government_guidance_and_research": "MIXED EVIDENCE",
        "technical_hypothesis_needing_full_review": "TECHNICAL REVIEW",
        "illustrative_interface_only": "ILLUSTRATIVE",
        "peer_reviewed_research": "RESEARCH",
        "professional_practice": "PRACTICE",
        "expert_judgment": "JUDGMENT",
        "source_material_only": "SOURCE MATERIAL",
    }
    for claim_id in block.get("claim_ids") or []:
        claim = claims.get(str(claim_id), {})
        status = str(claim.get("verification_status", "pending"))
        tier = str(claim.get("evidence_tier", "unclassified"))
        tier = tier_labels.get(tier, tier.replace("_", " ").upper())
        badge_key = (tier, status)
        if badge_key in seen:
            continue
        seen.add(badge_key)
        badges.append(
            f'<span class="claim claim-{esc(status)}">{esc(tier)} · {esc(status)}</span>'
        )
    return "".join(badges)


def _claim_evidence(
    block: dict[str, Any],
    claims: dict[str, dict[str, Any]],
    sources: dict[str, dict[str, Any]],
) -> str:
    records = []
    block_id = str(block.get("block_id", "block"))
    for claim_id_value in block.get("claim_ids") or []:
        claim_id = str(claim_id_value)
        claim = claims.get(claim_id)
        if not claim:
            continue
        source_links = []
        for source_id_value in claim.get("source_ids") or []:
            source_id = str(source_id_value)
            source = sources.get(source_id)
            if not source:
                continue
            use = str(source.get("governing_use", "")).replace("_", " ")
            source_links.append(
                "<li>"
                f'<a href="{esc(source.get("locator", ""))}">{esc(source.get("title", source_id))}</a>'
                f'<span>{esc(source.get("issuer_or_author", ""))} · '
                f'{esc(source.get("authority_tier", ""))} · {esc(use)}</span>'
                f'<small>{esc(source.get("limitations", ""))}</small>'
                "</li>"
            )
        if not source_links:
            source_links.append(
                "<li><b>No external evidence source assigned.</b>"
                "<small>This record is an owner position, internal governance boundary, "
                "instructional scenario, or unresolved question.</small></li>"
            )
        disposition = str(claim.get("research_disposition", "pending")).replace("_", " ")
        disposition_key = disposition.lower()
        withheld = any(
            marker in disposition_key
            for marker in ("withhold", "hold ", "remove", "reject", "do not publish")
        )
        if withheld:
            decision_state = "WITHHELD"
        elif any(marker in disposition_key for marker in ("narrow", "recast", "upgrade", "replace")):
            decision_state = "NARROWED"
        elif "retain" in disposition_key:
            decision_state = "RETAINED"
        else:
            decision_state = "UNDER REVIEW"
        learner_claim_text = (
            "Historical claim wording is withheld from this learner-facing page."
            if withheld
            else str(claim.get("claim_text", ""))
        )
        verification_status = str(claim.get("verification_status", "pending")).replace("_", " ")
        records.append(
            f'<article class="evidence-claim" id="evidence-{esc(block_id)}-{esc(claim_id)}">'
            f'<div class="evidence-claim-head"><code>{esc(claim_id)}</code>'
            f'<span>{esc(decision_state)} · {esc(verification_status)}</span></div>'
            f'<p>{esc(learner_claim_text)}</p>'
            f'<p class="evidence-decision"><b>Research decision:</b> {esc(disposition)}</p>'
            f'<ul>{"".join(source_links)}</ul>'
            f'<p class="evidence-limit"><b>Limit:</b> {esc(claim.get("limitations", ""))}</p>'
            "</article>"
        )
    if not records:
        return ""
    return (
        '<details class="evidence-trace">'
        f'<summary>Evidence and research decisions <span>{len(records)} claims</span></summary>'
        '<div class="evidence-trace-intro"><b>Research is not verification.</b> '
        "These records show what was retained, narrowed, held, corrected, or rejected. "
        "Independent and qualified technical review remain separate gates.</div>"
        f'<div class="evidence-claim-grid">{"".join(records)}</div></details>'
    )


def _render_jar_model(interaction: dict[str, Any]) -> str:
    stages = interaction.get("stages") or []
    conditions = interaction.get("conditions") or {}
    initial = interaction.get("initial_state") or {}
    coagulant = conditions.get("coagulant") or []
    flocculation = conditions.get("flocculation") or []
    stage_id = str(initial.get("stage") or (stages[0].get("id") if stages else "raw"))
    coagulant_id = str(
        initial.get("coagulant_condition")
        or (coagulant[0].get("id") if coagulant else "balanced")
    )
    flocculation_id = str(
        initial.get("flocculation_energy")
        or (flocculation[0].get("id") if flocculation else "balanced")
    )

    def buttons(records: list[dict[str, Any]], control: str, selected: str) -> str:
        return "".join(
            f'<button type="button" class="jar-control" data-jar-control="{esc(control)}" '
            f'data-jar-value="{esc(record.get("id", ""))}" '
            f'aria-pressed="{"true" if str(record.get("id")) == selected else "false"}">'
            f'{esc(record.get("label", ""))}</button>'
            for record in records
        )

    stage_buttons = "".join(
        f'<button type="button" class="jar-control stage-button" '
        f'data-jar-control="stage" data-jar-value="{esc(record.get("id", ""))}" '
        f'aria-label="{esc(record.get("label", ""))}" '
        f'aria-pressed="{"true" if str(record.get("id")) == stage_id else "false"}">'
        f'<span class="stage-number">STAGE {index:02d}</span>'
        f'<span class="stage-title">{esc(record.get("label", ""))}</span>'
        f'<span class="stage-note">{esc(record.get("explanation", ""))}</span></button>'
        for index, record in enumerate(stages)
    )
    fallback_stages = "".join(
        f'<li><b>{esc(record.get("label", ""))}:</b> '
        f'{esc(record.get("explanation", ""))}</li>'
        for record in stages
    )
    fallback_conditions = "".join(
        f'<li><b>{esc(record.get("label", ""))}:</b> {esc(record.get("result", ""))}</li>'
        for record in [*coagulant, *flocculation]
    )
    payload = json.dumps(
        {
            "stages": stages,
            "coagulant": coagulant,
            "flocculation": flocculation,
            "next_evidence_question": interaction.get("next_evidence_question", ""),
        },
        ensure_ascii=True,
        separators=(",", ":"),
    ).replace("<", "\\u003c")
    return (
        f'<div class="interaction jar-model" data-stage="{esc(stage_id)}" '
        f'data-coagulant="{esc(coagulant_id)}" data-flocculation="{esc(flocculation_id)}">'
        f'<h3>{esc(interaction["title"])}</h3>'
        f'<p>{esc(interaction["teaching_job"])}</p>'
        f'<p class="boundary"><b>Model boundary:</b> {esc(interaction["model_boundary"])}</p>'
        '<div class="sim">'
        f'<div class="sim-top">{stage_buttons}</div>'
        '<div class="canvas-shell" aria-hidden="true"><canvas class="jar-canvas"></canvas>'
        '<div class="canvas-label">QUALITATIVE PARTICLE MODEL</div></div>'
        '<div class="condition-rail">'
        f'<fieldset><legend>COAGULANT CONDITION</legend>{buttons(coagulant, "coagulant", coagulant_id)}</fieldset>'
        f'<fieldset><legend>FLOCCULATION ENERGY</legend>{buttons(flocculation, "flocculation", flocculation_id)}</fieldset>'
        "</div>"
        '<div class="sim-cap"><div class="jar-result" role="status" aria-live="polite" aria-atomic="true">'
        '<p class="jar-stage-result"></p><p class="jar-condition-result"></p>'
        '<p class="jar-question"></p></div><div class="qualitative-readout">'
        '<span>PARTICLE STATE <b class="readout-particle">DISPERSED</b></span>'
        '<span>AGGREGATE STATE <b class="readout-aggregate">FINE</b></span>'
        '<span>NEXT PROCESS <b class="readout-next">COAGULATION</b></span></div></div>'
        "</div>"
        '<div class="stability-graphic"><svg viewBox="0 0 900 260" role="img" '
        'aria-labelledby="stability-title stability-desc">'
        '<title id="stability-title">From particle stability to separable aggregates</title>'
        '<desc id="stability-desc">A qualitative sequence shows a dispersed particle population, '
        'a changed coagulation condition, controlled contact, and larger aggregates that can reach separation.</desc>'
        '<rect width="900" height="260" fill="#151515"/>'
        '<text x="24" y="30" class="svg-kicker">FROM STABILITY TO SEPARATION</text>'
        '<g class="dispersed-particles"><circle cx="105" cy="126" r="25"/><circle cx="196" cy="100" r="18"/>'
        '<circle cx="184" cy="178" r="15"/><circle cx="90" cy="191" r="11"/></g>'
        '<text x="145" y="235" class="svg-label">A particle population may remain dispersed</text>'
        '<path d="M265 132H350" class="svg-arrow"/><text x="307" y="112" class="svg-step">CHANGE CONDITION</text>'
        '<g class="prepared-particles"><circle cx="430" cy="126" r="22"/><circle cx="481" cy="126" r="22"/>'
        '<circle cx="456" cy="171" r="17"/></g>'
        '<text x="455" y="235" class="svg-label">A changed condition creates contact</text>'
        '<path d="M545 132H630" class="svg-arrow"/><text x="587" y="112" class="svg-step">CONTROL CONTACT</text>'
        '<g class="aggregate"><circle cx="744" cy="139" r="52"/><circle cx="727" cy="124" r="16"/>'
        '<circle cx="762" cy="130" r="18"/><circle cx="742" cy="159" r="15"/></g>'
        '<text x="744" y="235" class="svg-label">Aggregates reach separation</text>'
        '</svg><div class="stability-mobile">'
        '<div><b>01 · DISPERSED</b><span>A particle population may remain dispersed.</span></div>'
        '<div><b>02 · CONDITION CHANGES</b><span>Destabilization or precipitate capture creates contact.</span></div>'
        '<div><b>03 · AGGREGATES GROW</b><span>Larger aggregates can reach the next separation step.</span></div>'
        "</div></div>"
        '<noscript><div class="jar-fallback"><h4>Text equivalent</h4>'
        f'<ol>{fallback_stages}</ol><ul>{fallback_conditions}</ul>'
        f'<p><b>Next evidence question:</b> {esc(interaction.get("next_evidence_question", ""))}</p>'
        "</div></noscript>"
        f'<script type="application/json" class="jar-data">{payload}</script>'
        "</div>"
    )


def _render_scenario_transfer_lab(interaction: dict[str, Any]) -> str:
    interaction_id = str(interaction.get("interaction_id", "scenario-transfer-lab"))
    root_id = f"scenario-transfer-{interaction_id}"
    initial = interaction.get("initial_state") or {}
    boundaries = interaction.get("authored_scenarios") or []
    time_bases = interaction.get("time_bases") or []
    measurement_conditions = interaction.get("measurement_conditions") or []
    model = interaction.get("illustrative_model") or {}

    def choice_buttons(
        records: list[dict[str, Any]],
        group: str,
        selected: str,
    ) -> str:
        return "".join(
            f'<button type="button" class="transfer-choice" data-transfer-group="{esc(group)}" '
            f'data-transfer-value="{esc(record.get("id", ""))}" '
            f'aria-pressed="{"true" if str(record.get("id")) == selected else "false"}">'
            f'<b>{esc(record.get("label", ""))}</b>'
            f'<span>{esc(record.get("explanation", record.get("result", "")))}</span></button>'
            for record in records
        )

    boundary_selected = str(initial.get("selected_boundary", ""))
    time_selected = str(initial.get("selected_time_basis", ""))
    measurement_selected = str(initial.get("measurement_condition", ""))
    payload = json.dumps(
        {
            "model": model,
            "initial": initial,
            "boundaries": boundaries,
            "time_bases": time_bases,
            "measurement_conditions": measurement_conditions,
        },
        ensure_ascii=True,
        separators=(",", ":"),
    ).replace("<", "\\u003c")
    fallback_rows = "".join(
        f'<tr><th>{esc(record.get("label", ""))}</th>'
        f'<td>{esc(record.get("explanation", record.get("result", "")))}</td></tr>'
        for record in [*boundaries, *time_bases, *measurement_conditions]
    )
    script = """
<script>
(function(){
  var root=document.getElementById(__ROOT_ID__);
  if(!root)return;
  var data=JSON.parse(root.querySelector('.transfer-data').textContent);
  var state={
    boundary:data.initial.selected_boundary,
    time:data.initial.selected_time_basis,
    storage:Boolean(data.initial.include_storage_change),
    side:Boolean(data.initial.include_known_side_stream),
    measurement:data.initial.measurement_condition
  };
  function selected(records,id){return records.find(function(item){return item.id===id})||{};}
  function update(){
    var model=data.model||{};
    var residual=Number(model.base_residual_percent||0);
    residual+=Number((model.boundary_adjustments||{})[state.boundary]||0);
    residual+=Number((model.time_adjustments||{})[state.time]||0);
    if(state.storage)residual+=Number(model.storage_adjustment_when_included||0);
    if(state.side)residual+=Number(model.side_stream_adjustment_when_included||0);
    residual+=Number((model.measurement_adjustments||{})[state.measurement]||0);
    residual=Math.abs(Math.round(residual*10)/10);
    root.dataset.boundary=state.boundary;
    root.dataset.time=state.time;
    root.querySelector('.transfer-boundary-label').textContent=selected(data.boundaries,state.boundary).label||state.boundary;
    root.querySelector('.transfer-time-label').textContent=selected(data.time_bases,state.time).label||state.time;
    root.querySelector('.transfer-storage-label').textContent=state.storage?'Included':'Not included';
    root.querySelector('.transfer-side-label').textContent=state.side?'Included':'Not included';
    root.querySelector('.transfer-measurement-label').textContent=selected(data.measurement_conditions,state.measurement).label||state.measurement;
    root.querySelector('.transfer-residual-value').textContent=residual.toFixed(1)+'%';
    root.querySelector('.transfer-result').textContent='This illustrative ledger shows a '+residual.toFixed(1)+'% closure gap. Review the accounting evidence. The gap does not prove one cause.';
    root.querySelectorAll('[data-transfer-group]').forEach(function(button){
      var group=button.dataset.transferGroup;
      var pressed=(group==='boundary'&&button.dataset.transferValue===state.boundary)
        ||(group==='time'&&button.dataset.transferValue===state.time)
        ||(group==='measurement'&&button.dataset.transferValue===state.measurement)
        ||(group==='storage'&&state.storage)
        ||(group==='side'&&state.side);
      button.setAttribute('aria-pressed',pressed?'true':'false');
    });
    var changed=state.boundary!==data.initial.selected_boundary
      ||state.time!==data.initial.selected_time_basis
      ||state.storage!==Boolean(data.initial.include_storage_change)
      ||state.side!==Boolean(data.initial.include_known_side_stream)
      ||state.measurement!==data.initial.measurement_condition;
    if(changed)root.dataset.complete='true';
  }
  root.querySelectorAll('[data-transfer-group]').forEach(function(button){
    button.addEventListener('click',function(){
      var group=button.dataset.transferGroup;
      if(group==='storage')state.storage=!state.storage;
      else if(group==='side')state.side=!state.side;
      else state[group]=button.dataset.transferValue;
      update();
    });
  });
  update();
})();
</script>
""".replace("__ROOT_ID__", json.dumps(root_id))
    return (
        f'<div class="interaction transfer-lab" id="{esc(root_id)}" '
        f'data-interaction="{esc(interaction_id)}" data-complete="false">'
        f'<h3>{esc(interaction["title"])}</h3>'
        f'<p>{esc(interaction["teaching_job"])}</p>'
        f'<p class="boundary"><b>Model boundary:</b> {esc(interaction["model_boundary"])}</p>'
        '<div class="transfer-layout"><div class="transfer-controls">'
        '<fieldset><legend>1. SELECT THE BOUNDARY</legend>'
        f'{choice_buttons(boundaries, "boundary", boundary_selected)}</fieldset>'
        '<fieldset><legend>2. SELECT THE TIME BASIS</legend>'
        f'{choice_buttons(time_bases, "time", time_selected)}</fieldset>'
        '<fieldset><legend>3. COMPLETE THE LEDGER</legend>'
        f'<button type="button" class="transfer-choice compact" data-transfer-group="storage" '
        f'aria-pressed="{"true" if initial.get("include_storage_change") else "false"}">'
        '<b>Storage change</b><span>Include the authored change in stored mass.</span></button>'
        f'<button type="button" class="transfer-choice compact" data-transfer-group="side" '
        f'aria-pressed="{"true" if initial.get("include_known_side_stream") else "false"}">'
        '<b>Known side stream</b><span>Include the authored path that crosses the fence.</span></button>'
        '</fieldset><fieldset><legend>4. REVIEW THE MEASUREMENTS</legend>'
        f'{choice_buttons(measurement_conditions, "measurement", measurement_selected)}</fieldset>'
        '</div><div class="transfer-stage">'
        '<div class="transfer-boundary-graphic" aria-hidden="true">'
        '<span class="transfer-arrow in">INPUT</span><div class="transfer-box">'
        '<b class="transfer-boundary-label"></b><span>selected accounting fence</span>'
        '</div><span class="transfer-arrow out">OUTPUT</span></div>'
        '<dl class="transfer-ledger">'
        '<div><dt>Clock</dt><dd class="transfer-time-label"></dd></div>'
        '<div><dt>Storage change</dt><dd class="transfer-storage-label"></dd></div>'
        '<div><dt>Side stream</dt><dd class="transfer-side-label"></dd></div>'
        '<div><dt>Measurement basis</dt><dd class="transfer-measurement-label"></dd></div>'
        '<div class="transfer-residual"><dt>Illustrative closure gap</dt>'
        '<dd class="transfer-residual-value"></dd></div></dl>'
        '<p class="transfer-result" role="status" aria-live="polite" aria-atomic="true"></p>'
        '<p class="transfer-stop"><b>What not to assume:</b> The residual alone does not prove '
        'leakage, process failure, model failure, or bad data.</p></div></div>'
        '<noscript><div class="transfer-fallback"><h4>Structured text equivalent</h4>'
        f'<table><tbody>{fallback_rows}</tbody></table>'
        '<p>Changing the fence, clock, storage term, side stream, or measurement basis changes '
        'the illustrative closure gap. The gap still does not diagnose one cause.</p></div></noscript>'
        f'<script type="application/json" class="transfer-data">{payload}</script>'
        '</div>'
        f'{script}'
    )


def _render_path_tracer(interaction: dict[str, Any]) -> str:
    interaction_id = str(interaction.get("interaction_id", "path-tracer"))
    root_id = f"path-tracer-{interaction_id}"
    routes = interaction.get("routes") or []
    initial_route = str(
        interaction.get("initial_route")
        or (routes[0].get("route_id") if routes else "")
    )
    route_buttons = "".join(
        f'<button type="button" class="path-route-choice" '
        f'data-path-route="{esc(route.get("route_id", ""))}" '
        f'aria-pressed="{"true" if str(route.get("route_id")) == initial_route else "false"}">'
        f'<b>{esc(route.get("short_label", route.get("label", "")))}</b>'
        f'<span>{esc(route.get("objective", ""))}</span></button>'
        for route in routes
    )
    fallback_routes = "".join(
        "<section>"
        f'<h4>{esc(route.get("label", ""))}</h4>'
        f'<p>{esc(route.get("objective", ""))}</p>'
        "<ol>"
        + "".join(
            f'<li><b>{esc(step.get("label", ""))}:</b> '
            f'{esc(step.get("detail", ""))} '
            f'<span>Destination: {esc(step.get("destination", ""))}</span></li>'
            for step in route.get("steps") or []
        )
        + "</ol>"
        f'<p><b>What not to assume:</b> {esc(route.get("what_not_to_assume", ""))}</p>'
        "</section>"
        for route in routes
    )
    payload = json.dumps(
        {
            "routes": routes,
            "initial_route": initial_route,
            "evidence_prompt": interaction.get("evidence_prompt", ""),
        },
        ensure_ascii=True,
        separators=(",", ":"),
    ).replace("<", "\\u003c")
    script = """
<script>
(function(){
  var root=document.getElementById(__ROOT_ID__);
  if(!root)return;
  var data=JSON.parse(root.querySelector('.path-tracer-data').textContent);
  var routeId=data.initial_route;
  var stepIndex=0;
  function route(){
    return data.routes.find(function(item){return item.route_id===routeId})||data.routes[0]||{};
  }
  function update(){
    var current=route();
    var steps=current.steps||[];
    if(stepIndex>=steps.length)stepIndex=Math.max(0,steps.length-1);
    var step=steps[stepIndex]||{};
    root.dataset.route=routeId;
    root.dataset.step=String(stepIndex+1);
    root.querySelector('.path-route-label').textContent=current.label||'';
    root.querySelector('.path-objective').textContent=current.objective||'';
    root.querySelector('.path-step-count').textContent='STEP '+String(stepIndex+1)+' OF '+String(steps.length);
    root.querySelector('.path-step-label').textContent=step.label||'';
    root.querySelector('.path-step-detail').textContent=step.detail||'';
    root.querySelector('.path-destination').textContent=step.destination||'';
    root.querySelector('.path-nonclaim').textContent=current.what_not_to_assume||'';
    root.querySelector('.path-evidence').textContent=data.evidence_prompt||'';
    root.querySelector('.path-back').disabled=stepIndex===0;
    root.querySelector('.path-next').disabled=stepIndex>=steps.length-1;
    root.querySelectorAll('[data-path-route]').forEach(function(button){
      button.setAttribute('aria-pressed',button.dataset.pathRoute===routeId?'true':'false');
    });
    root.querySelectorAll('.path-node').forEach(function(node,index){
      node.dataset.state=index<stepIndex?'complete':(index===stepIndex?'active':'pending');
      node.querySelector('b').textContent=(steps[index]||{}).label||'';
    });
    if(stepIndex>=steps.length-1)root.dataset.complete='true';
  }
  root.querySelectorAll('[data-path-route]').forEach(function(button){
    button.addEventListener('click',function(){
      routeId=button.dataset.pathRoute;
      stepIndex=0;
      update();
    });
  });
  root.querySelector('.path-back').addEventListener('click',function(){
    stepIndex=Math.max(0,stepIndex-1);
    update();
  });
  root.querySelector('.path-next').addEventListener('click',function(){
    var steps=route().steps||[];
    stepIndex=Math.min(steps.length-1,stepIndex+1);
    update();
  });
  root.querySelector('.path-reset').addEventListener('click',function(){
    routeId=data.initial_route;
    stepIndex=0;
    root.dataset.complete='false';
    update();
  });
  update();
})();
</script>
""".replace("__ROOT_ID__", json.dumps(root_id))
    nodes = "".join(
        '<div class="path-node" data-state="pending"><span aria-hidden="true"></span><b></b></div>'
        for _ in range(max((len(route.get("steps") or []) for route in routes), default=4))
    )
    styles = """
<style>
.path-tracer{padding:clamp(20px,3vw,34px);border:1px solid #4b4842;background:#171614;color:#f2f1ec}
.path-route-choices{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:22px 0}
.path-route-choice{min-height:92px;padding:14px;text-align:left;border:1px solid #59554d;background:#292826;color:#f2f1ec;cursor:pointer}
.path-route-choice b,.path-route-choice span{display:block}.path-route-choice span{margin-top:6px;color:#d9d6cf;line-height:1.4}
.path-route-choice[aria-pressed="true"]{border-color:#8ed0ed;box-shadow:inset 0 0 0 2px #8ed0ed;background:#10232e}
.path-tracer-stage{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(260px,.65fr);gap:20px}
.path-track{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-items:start;margin:22px 0}
.path-node{position:relative;min-height:84px;padding:36px 9px 9px;border-top:3px solid #59554d;color:#a29c91}
.path-node span{position:absolute;top:-10px;left:0;width:18px;height:18px;border-radius:50%;background:#59554d}
.path-node[data-state="active"]{border-color:#8ed0ed;color:#f2f1ec}.path-node[data-state="active"] span{background:#8ed0ed;box-shadow:0 0 18px #7dc6e8}
.path-node[data-state="complete"]{border-color:#4ac88c;color:#d9d6cf}.path-node[data-state="complete"] span{background:#4ac88c}
.path-step-panel{padding:20px;border:1px solid #42677a;background:#10232e}
.path-step-count{font:700 11px "Courier New",monospace;letter-spacing:.14em;color:#8ed0ed}
.path-destination-line{padding-top:12px;border-top:1px solid #42677a}.path-destination{color:#8ed0ed}
.path-controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}.path-controls button{min-height:44px;padding:10px 16px;border:1px solid #8ed0ed;background:#10232e;color:#f2f1ec;cursor:pointer}
.path-controls button:disabled{opacity:.45;cursor:not-allowed}.path-controls button:focus-visible,.path-route-choice:focus-visible{outline:3px solid #e0a64a;outline-offset:3px}
.path-boundaries{display:grid;gap:12px}.path-boundary-card{padding:16px;border:1px solid #59554d;background:#292826}
.path-boundary-card b{display:block;margin-bottom:7px;color:#e0a64a}.path-boundary-card p{margin:0;color:#d9d6cf}
@media(max-width:760px){.path-route-choices,.path-tracer-stage{grid-template-columns:1fr}.path-track{grid-template-columns:1fr}.path-node{min-height:52px;padding:14px 10px 10px 34px;border-top:0;border-left:3px solid #59554d}.path-node span{top:14px;left:-10px}}
@media(prefers-reduced-motion:reduce){.path-node span{box-shadow:none}}
</style>
"""
    return (
        f'{styles}<div class="interaction path-tracer" id="{esc(root_id)}" '
        f'data-interaction="{esc(interaction_id)}" data-complete="false">'
        f'<h3>{esc(interaction["title"])}</h3>'
        f'<p>{esc(interaction["teaching_job"])}</p>'
        f'<p class="boundary"><b>Model boundary:</b> {esc(interaction["model_boundary"])}</p>'
        f'<div class="path-route-choices" aria-label="Choose a water pathway">{route_buttons}</div>'
        '<div class="path-tracer-stage"><div><p class="path-step-count"></p>'
        '<h4 class="path-route-label"></h4><p class="path-objective"></p>'
        f'<div class="path-track" aria-hidden="true">{nodes}</div>'
        '<div class="path-step-panel" role="status" aria-live="polite" aria-atomic="true">'
        '<h4 class="path-step-label"></h4><p class="path-step-detail"></p>'
        '<p class="path-destination-line"><b>Current destination:</b> '
        '<span class="path-destination"></span></p></div>'
        '<div class="path-controls"><button type="button" class="path-back">Back</button>'
        '<button type="button" class="path-next">Step</button>'
        '<button type="button" class="path-reset">Reset</button></div></div>'
        '<aside class="path-boundaries"><div class="path-boundary-card"><b>WHAT NOT TO ASSUME</b>'
        '<p class="path-nonclaim"></p></div><div class="path-boundary-card">'
        '<b>NEXT EVIDENCE QUESTION</b><p class="path-evidence"></p></div></aside></div>'
        f'<noscript><style>#{esc(root_id)} .path-route-choices,'
        f'#{esc(root_id)} .path-tracer-stage{{display:none}}</style>'
        '<div class="path-tracer-fallback"><h4>Structured text equivalent</h4>'
        f'{fallback_routes}</div></noscript>'
        f'<script type="application/json" class="path-tracer-data">{payload}</script></div>{script}'
    )


def _render_failure_trace(interaction: dict[str, Any]) -> str:
    interaction_id = str(interaction.get("interaction_id", "failure-trace"))
    root_id = f"failure-trace-{interaction_id}"
    scenarios = interaction.get("scenarios") or []
    scenario_buttons = "".join(
        f'<button type="button" class="failure-choice" '
        f'data-failure-scenario="{esc(scenario.get("scenario_id", ""))}" '
        f'aria-pressed="{"true" if index == 0 else "false"}">'
        f'{esc(scenario.get("observation", ""))}</button>'
        for index, scenario in enumerate(scenarios)
    )
    fallback_rows = "".join(
        "<tr>"
        f'<th scope="row">{esc(scenario.get("observation", ""))}</th>'
        f'<td>{esc(scenario.get("pathway_question", ""))}</td>'
        f'<td>{esc(scenario.get("possible_consequence", ""))}</td>'
        f'<td>{esc(scenario.get("evidence_needed", ""))}</td>'
        "</tr>"
        for scenario in scenarios
    )
    payload = json.dumps(
        {"scenarios": scenarios},
        ensure_ascii=True,
        separators=(",", ":"),
    ).replace("<", "\\u003c")
    styles = """
<style>
.failure-trace{padding:clamp(20px,3vw,34px);border:1px solid #4b4842;background:#171614;color:#f2f1ec}
.failure-trace-layout{display:grid;grid-template-columns:minmax(230px,.65fr) minmax(0,1.35fr);gap:20px;margin-top:22px}
.failure-choices{display:grid;gap:8px;align-content:start}
.failure-choice{min-height:54px;padding:11px 14px;text-align:left;border:1px solid #59554d;background:#292826;color:#f2f1ec;cursor:pointer}
.failure-choice[aria-pressed="true"]{border-color:#8ed0ed;box-shadow:inset 0 0 0 2px #8ed0ed;background:#10232e}
.failure-stage{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.failure-card{min-height:180px;padding:18px;border:1px solid #42677a;background:#10232e}
.failure-card b{display:block;margin-bottom:12px;color:#8ed0ed;font:700 11px "Courier New",monospace;letter-spacing:.12em}
.failure-card p{margin:0;color:#e8f0f4;line-height:1.55}
.failure-progress{grid-column:1/-1;margin:2px 0 0;color:#d9d6cf}
.failure-progress strong{color:#4ac88c}
.failure-choice:focus-visible{outline:3px solid #e0a64a;outline-offset:3px}
.failure-fallback{max-width:100%;overflow-x:auto}.failure-fallback table{width:100%;border-collapse:collapse}.failure-fallback th,.failure-fallback td{padding:10px;border:1px solid #59554d;text-align:left;vertical-align:top}
@media(max-width:800px){.failure-trace-layout,.failure-stage{grid-template-columns:1fr}.failure-card{min-height:0}}
@media(prefers-reduced-motion:reduce){.failure-choice{scroll-behavior:auto}}
</style>
"""
    script = """
<script>
(function(){
  var root=document.getElementById(__ROOT_ID__);
  if(!root)return;
  var data=JSON.parse(root.querySelector('.failure-trace-data').textContent);
  var selected=(data.scenarios[0]||{}).scenario_id||'';
  var visited={};
  function current(){
    return data.scenarios.find(function(item){return item.scenario_id===selected})||data.scenarios[0]||{};
  }
  function update(){
    var item=current();
    visited[selected]=true;
    root.dataset.scenario=selected;
    root.querySelector('.failure-question').textContent=item.pathway_question||'';
    root.querySelector('.failure-consequence').textContent=item.possible_consequence||'';
    root.querySelector('.failure-evidence').textContent=item.evidence_needed||'';
    root.querySelectorAll('[data-failure-scenario]').forEach(function(button){
      button.setAttribute('aria-pressed',button.dataset.failureScenario===selected?'true':'false');
    });
    var count=Object.keys(visited).length;
    root.querySelector('.failure-progress').innerHTML='<strong>'+String(count)+'</strong> of '+String(data.scenarios.length)+' conditions reviewed';
    if(count>=data.scenarios.length)root.dataset.complete='true';
  }
  root.querySelectorAll('[data-failure-scenario]').forEach(function(button){
    button.addEventListener('click',function(){selected=button.dataset.failureScenario;update();});
  });
  update();
})();
</script>
""".replace("__ROOT_ID__", json.dumps(root_id))
    return (
        f'{styles}<div class="interaction failure-trace" id="{esc(root_id)}" '
        f'data-interaction="{esc(interaction_id)}" data-complete="false">'
        f'<h3>{esc(interaction["title"])}</h3>'
        f'<p>{esc(interaction["teaching_job"])}</p>'
        f'<p class="boundary"><b>Model boundary:</b> {esc(interaction["model_boundary"])}</p>'
        '<div class="failure-trace-layout"><div class="failure-choices" '
        f'aria-label="Choose a condition">{scenario_buttons}</div>'
        '<div class="failure-stage"><div class="failure-card"><b>PATHWAY QUESTION</b>'
        '<p class="failure-question"></p></div><div class="failure-card">'
        '<b>POSSIBLE CONSEQUENCE</b><p class="failure-consequence"></p></div>'
        '<div class="failure-card"><b>EVIDENCE NEEDED NEXT</b>'
        '<p class="failure-evidence"></p></div>'
        '<p class="failure-progress" role="status" aria-live="polite"></p></div></div>'
        f'<noscript><style>#{esc(root_id)} .failure-trace-layout{{display:none}}</style>'
        '<div class="failure-fallback"><h4>Structured text equivalent</h4>'
        '<table><thead><tr><th>Observation</th><th>Pathway question</th>'
        '<th>Possible consequence</th><th>Evidence needed</th></tr></thead>'
        f'<tbody>{fallback_rows}</tbody></table></div></noscript>'
        f'<script type="application/json" class="failure-trace-data">{payload}</script></div>{script}'
    )


def _render_assessment(assessment: dict[str, Any]) -> str:
    assessment_id = str(assessment["assessment_id"])
    assessment_type = str(assessment["type"])
    feedback = assessment.get("feedback") or {}
    if assessment_type == "multiple-choice":
        options = "".join(
            '<label class="assessment-option">'
            f'<input type="radio" name="{esc(assessment_id)}" '
            f'value="{index}" data-correct="{"true" if option.get("correct") else "false"}"> '
            f'{esc(option.get("text", ""))}</label>'
            for index, option in enumerate(assessment.get("options") or [])
        )
        return (
            f'<section class="concept-assessment" id="{esc(assessment_id)}" '
            f'data-concept-assessment="multiple-choice" '
            f'data-completion="{esc(assessment["completion_id"])}">'
            f'<p class="assessment-kicker">LEARNING CHECK</p>'
            f'<h3>{esc(assessment["prompt"])}</h3>'
            f'<div class="assessment-options">{options}</div>'
            '<button type="button" class="assessment-check">Check answer</button>'
            '<p class="assessment-feedback" role="status" aria-live="polite"></p>'
            f'<template data-correct-feedback>{esc(feedback.get("correct", ""))}</template>'
            f'<template data-incorrect-feedback>{esc(feedback.get("incorrect", ""))}</template>'
            f'<p class="assessment-retry">{esc(assessment.get("retry", ""))}</p>'
            '<noscript><p>Enable JavaScript to record this check. The explanation remains in the '
            'evidence-backed lesson and structured assessment record.</p></noscript>'
            '</section>'
        )
    if assessment_type == "reflection":
        worked_example = assessment.get("worked_example") or {}
        if assessment.get("guided_rehearsal") is True and worked_example:
            steps = "".join(
                f'<article class="rehearsal-step" data-rehearsal-step="{index}">'
                f'<span>STEP {index + 1:02d}</span>'
                f'<h4>{esc(step.get("label", ""))}</h4>'
                f'<p>{esc(step.get("body", ""))}</p></article>'
                for index, step in enumerate(worked_example.get("steps") or [])
            )
            return (
                f'<section class="concept-assessment guided-rehearsal" id="{esc(assessment_id)}" '
                f'data-concept-assessment="reflection" data-optional="true" '
                f'data-completion="{esc(assessment["completion_id"])}">'
                '<p class="assessment-kicker">WORKED DECISION REHEARSAL</p>'
                f'<h3>{esc(assessment["prompt"])}</h3>'
                f'<p class="rehearsal-intro">{esc(assessment.get("introduction", ""))}</p>'
                '<div class="rehearsal-case">'
                '<div><span class="rehearsal-label">SCENARIO</span>'
                f'<p>{esc(worked_example.get("scenario", ""))}</p></div>'
                '<div class="rehearsal-shortcut"><span class="rehearsal-label">TEMPTING SHORTCUT</span>'
                f'<p>{esc(worked_example.get("shortcut", ""))}</p></div></div>'
                f'<div class="rehearsal-steps">{steps}</div>'
                '<div class="rehearsal-controls" aria-label="Worked example controls">'
                '<button type="button" class="rehearsal-back">Previous step</button>'
                '<span class="rehearsal-progress" role="status" aria-live="polite"></span>'
                '<button type="button" class="rehearsal-next">Next step</button></div>'
                '<div class="rehearsal-result"><span class="rehearsal-label">THE BETTER QUESTION</span>'
                f'<p>{esc(worked_example.get("result", ""))}</p></div>'
                '<div class="optional-practice">'
                '<div><span class="assessment-kicker">OPTIONAL PRACTICE</span>'
                f'<h4>{esc(assessment.get("try_title", "Want to try it yourself?"))}</h4>'
                f'<p>{esc(assessment.get("try_intro", ""))}</p></div>'
                '<button type="button" class="practice-toggle" aria-expanded="false">Try it yourself</button>'
                '<div class="practice-panel" hidden>'
                f'<label>{esc(assessment.get("response_label", "Write your evidence question"))}'
                f'<textarea rows="5" data-reflection-response '
                f'placeholder="{esc(assessment.get("response_placeholder", ""))}"></textarea></label>'
                '<button type="button" class="assessment-reveal">Compare with the example</button>'
                f'<div class="assessment-model" hidden><p>{esc(assessment.get("model_response", ""))}</p>'
                f'<p><b>Try again:</b> {esc(assessment.get("retry", ""))}</p></div>'
                '<p class="assessment-feedback" role="status" aria-live="polite"></p>'
                '</div></div>'
                '<noscript><p>The worked example remains complete above. Optional practice requires '
                'JavaScript, but it is not required to use or finish this brief.</p></noscript>'
                '</section>'
            )
        return (
            f'<section class="concept-assessment" id="{esc(assessment_id)}" '
            f'data-concept-assessment="reflection" '
            f'data-completion="{esc(assessment["completion_id"])}">'
            '<p class="assessment-kicker">APPLIED CHECK</p>'
            f'<h3>{esc(assessment["prompt"])}</h3>'
            '<label>Record your explanation'
            f'<textarea rows="5" data-reflection-response></textarea></label>'
            '<button type="button" class="assessment-reveal">Compare with the model response</button>'
            f'<div class="assessment-model" hidden><p>{esc(assessment.get("model_response", ""))}</p>'
            f'<p><b>Retry:</b> {esc(assessment.get("retry", ""))}</p></div>'
            '<p class="assessment-feedback" role="status" aria-live="polite"></p>'
            '</section>'
        )
    if assessment_type == "multi-select":
        options = "".join(
            '<label class="assessment-option">'
            f'<input type="checkbox" value="{index}" '
            f'data-correct="{"true" if option.get("correct") else "false"}"> '
            f'{esc(option.get("text", ""))}</label>'
            for index, option in enumerate(assessment.get("options") or [])
        )
        return (
            f'<section class="concept-assessment" id="{esc(assessment_id)}" '
            f'data-concept-assessment="multi-select" '
            f'data-completion="{esc(assessment["completion_id"])}">'
            '<p class="assessment-kicker">LEARNING CHECK</p>'
            f'<h3>{esc(assessment["prompt"])}</h3>'
            f'<div class="assessment-options">{options}</div>'
            '<button type="button" class="assessment-check">Check selections</button>'
            '<p class="assessment-feedback" role="status" aria-live="polite"></p>'
            f'<template data-correct-feedback>{esc(feedback.get("correct", ""))}</template>'
            f'<template data-incorrect-feedback>{esc(feedback.get("incorrect", ""))}</template>'
            f'<p class="assessment-retry">{esc(assessment.get("retry", ""))}</p></section>'
        )
    if assessment_type == "flip-cards":
        cards = "".join(
            f'<button type="button" class="assessment-card" data-flip-card '
            f'data-front="{esc(card.get("front", ""))}" '
            f'data-back="{esc(card.get("back", ""))}" aria-pressed="false">'
            f'{esc(card.get("front", ""))}</button>'
            for card in assessment.get("cards") or []
        )
        return (
            f'<section class="concept-assessment" id="{esc(assessment_id)}" '
            f'data-concept-assessment="flip-cards" '
            f'data-completion="{esc(assessment["completion_id"])}">'
            '<p class="assessment-kicker">RETRIEVAL CHECK</p>'
            f'<h3>{esc(assessment["prompt"])}</h3>'
            f'<div class="assessment-card-grid">{cards}</div>'
            '<p class="assessment-feedback" role="status" aria-live="polite"></p>'
            f'<template data-correct-feedback>{esc(feedback.get("correct", ""))}</template>'
            f'<p class="assessment-retry">{esc(assessment.get("retry", ""))}</p></section>'
        )
    if assessment_type == "matching":
        targets = assessment.get("targets") or []
        options = '<option value="">Choose a match</option>' + "".join(
            f'<option value="{esc(target)}">{esc(target)}</option>' for target in targets
        )
        rows = "".join(
            '<label class="assessment-match-row">'
            f'<span>{esc(_match_pair_prompt(pair))}</span>'
            f'<select data-answer="{esc(_match_pair_answer(pair))}">{options}</select></label>'
            for pair in assessment.get("pairs") or []
            if isinstance(pair, dict)
        )
        return (
            f'<section class="concept-assessment" id="{esc(assessment_id)}" '
            f'data-concept-assessment="matching" '
            f'data-completion="{esc(assessment["completion_id"])}">'
            '<p class="assessment-kicker">RELATIONSHIP CHECK</p>'
            f'<h3>{esc(assessment["prompt"])}</h3>'
            f'<div class="assessment-match-grid">{rows}</div>'
            '<button type="button" class="assessment-check">Check matches</button>'
            '<p class="assessment-feedback" role="status" aria-live="polite"></p>'
            f'<template data-correct-feedback>{esc(feedback.get("correct", ""))}</template>'
            f'<template data-incorrect-feedback>{esc(feedback.get("incorrect", ""))}</template>'
            f'<p class="assessment-retry">{esc(assessment.get("retry", ""))}</p></section>'
        )
    if assessment_type == "applied-work-product":
        labels = assessment.get("field_labels") or {}
        fields = "".join(
            '<label class="assessment-work-field">'
            f'{esc(labels.get(field, str(field).replace("_", " ").title()))}'
            f'<textarea rows="3" data-required-field="{esc(field)}"></textarea></label>'
            for field in assessment.get("required_fields") or []
        )
        return (
            f'<section class="concept-assessment" id="{esc(assessment_id)}" '
            f'data-concept-assessment="applied-work-product" '
            f'data-completion="{esc(assessment["completion_id"])}">'
            '<p class="assessment-kicker">APPLIED WORK PRODUCT</p>'
            f'<h3>{esc(assessment["prompt"])}</h3>'
            f'<div class="assessment-work-grid">{fields}</div>'
            '<button type="button" class="assessment-work-check">Check completeness</button>'
            '<p class="assessment-feedback" role="status" aria-live="polite"></p>'
            f'<template data-correct-feedback>{esc(feedback.get("correct", ""))}</template>'
            f'<template data-incorrect-feedback>{esc(feedback.get("incorrect", ""))}</template>'
            f'<p class="assessment-retry">{esc(assessment.get("retry", ""))}</p></section>'
        )
    return (
        f'<section class="concept-assessment" id="{esc(assessment_id)}" '
        f'data-concept-assessment="{esc(assessment_type)}" '
        f'data-completion="{esc(assessment["completion_id"])}">'
        f'<p class="assessment-kicker">LEARNING CHECK · {esc(assessment_type)}</p>'
        f'<h3>{esc(assessment["prompt"])}</h3>'
        '<p>This shared assessment type is declared in the governed package. Its complete rendered '
        'component must resolve from the shared quiz gallery before release.</p></section>'
    )


def _render_block(
    block: dict[str, Any],
    package: dict[str, Any],
    asset_prefix: str,
    *,
    public_preview: bool = False,
    public_config: dict[str, Any] | None = None,
) -> str:
    public_config = public_config or {}
    if public_preview:
        override = (public_config.get("block_overrides") or {}).get(
            str(block.get("block_id", "")),
            {},
        )
        if isinstance(override, dict):
            block = {**block, **override}
    block_type = str(block.get("type"))
    title = esc(block.get("title", ""))
    paragraphs = [
        f"<p>{esc(paragraph.strip())}</p>"
        for paragraph in str(block.get("body", "")).split("\n\n")
        if paragraph.strip()
    ]
    body = "".join(paragraphs)
    badges = "" if public_preview else _claim_badges(block, package["claims"])
    block_id = esc(block.get("block_id"))
    extra = ""

    if block_type == "visual":
        visual_id = str(block.get("visual_id", ""))
        visual = package["visuals"].get(visual_id)
        if visual and visual.get("locator"):
            locator = esc(
                _portable_asset_href(
                    Path(package["package_dir"]),
                    str(visual["locator"]),
                    asset_prefix,
                    inline=public_preview,
                )
            )
            caption = (
                f'<figcaption><b>How to read this:</b> {esc(visual["reading_guide"])} '
                f'<b>Conclusion:</b> {esc(visual["learner_conclusion"])}'
            )
            if visual.get("not_established"):
                caption += (
                    f' <b>This does not prove:</b> {esc(visual["not_established"])}'
                )
            caption += "</figcaption>"
            extra = (
                f'<figure><img src="{locator}" alt="{esc(visual["alternative_text"])}">'
                f"{caption}</figure>"
            )
        elif visual:
            extra = (
                f'<figure class="visual-component" '
                f'data-visual-component="{esc(visual.get("component_id"))}">'
                f'<figcaption><b>How to read this:</b> {esc(visual["reading_guide"])} '
                f'<b>Conclusion:</b> {esc(visual["learner_conclusion"])}</figcaption>'
                f'<p class="visual-alt">{esc(visual["alternative_text"])}</p></figure>'
            )
    elif block_type == "definition":
        entries = []
        for entry in block.get("terms") or []:
            if not isinstance(entry, dict):
                continue
            entries.append(
                '<div class="definition">'
                f'<h4 class="definition-term">{esc(entry.get("term"))}</h4>'
                f'<p class="definition-meaning">{esc(entry.get("meaning"))}</p>'
                f'<p class="definition-example"><b>For example:</b> '
                f'{esc(entry.get("example"))}</p>'
                f'<p class="definition-limit"><b>What it does not tell you:</b> '
                f'{esc(entry.get("not_established"))}</p>'
                "</div>"
            )
        if entries:
            extra = f'<div class="definition-set">{"".join(entries)}</div>'
    elif block_type == "example":
        extra = (
            '<div class="worked-example">'
            f'<p class="worked-label">Worked example</p>'
            f'<p class="worked-situation"><b>The situation:</b> '
            f'{esc(block.get("situation"))}</p>'
            f'<p class="worked-reasoning"><b>Working it through:</b> '
            f'{esc(block.get("reasoning"))}</p>'
            f'<p class="worked-result"><b>What you conclude:</b> '
            f'{esc(block.get("result"))}</p>'
            f'<p class="worked-boundary"><b>Where this stops:</b> '
            f'{esc(block.get("boundary"))}</p>'
            "</div>"
        )
    elif block_type == "interaction":
        interaction_id = str(block.get("interaction_id", ""))
        interaction = package["interactions"].get(interaction_id)
        if interaction:
            if interaction.get("component") == "concept-jar-model":
                extra = _render_jar_model(interaction)
            elif interaction.get("component") == "scenario-transfer-lab":
                extra = _render_scenario_transfer_lab(interaction)
            elif interaction.get("component") == "path-tracer":
                extra = _render_path_tracer(interaction)
            elif interaction.get("component") == "failure-trace":
                extra = _render_failure_trace(interaction)
            else:
                extra = (
                    f'<div class="interaction" data-interaction="{esc(interaction_id)}">'
                    f'<b>{esc(interaction["title"])}</b>'
                    f'<p>{esc(interaction["teaching_job"])}</p>'
                    f'<p class="boundary">Model boundary: {esc(interaction["model_boundary"])}</p>'
                    "</div>"
                )
    elif block_type == "assessment":
        assessment_id = str(block.get("assessment_id", ""))
        assessment = package["assessments"].get(assessment_id)
        if assessment:
            extra = _render_assessment(assessment)
    elif block_type == "faq":
        extra = (
            f'<details><summary>{title}</summary>{body}</details>'
        )
        title = ""
        body = ""

    display = str(block.get("display", ""))
    items = block.get("items") or []
    if display in {"cards", "stakes"}:
        rendered = []
        for item in items:
            label = (
                f'<span class="card-label">{esc(item.get("label"))}</span>'
                if item.get("label")
                else ""
            )
            example = (
                f'<div class="example"><b>AT THE PLANT</b>{esc(item.get("example"))}</div>'
                if item.get("example")
                else ""
            )
            rendered.append(
                f'<div class="card"><h3>{esc(item.get("title", ""))}</h3>'
                f'<p>{esc(item.get("body", ""))}</p>{label}{example}</div>'
            )
        extra += f'<div class="card-grid {"stakes" if display == "stakes" else ""}">{"".join(rendered)}</div>'
    elif display == "table":
        headings = "".join(f"<th>{esc(value)}</th>" for value in block.get("columns") or [])
        rows = "".join(
            "<tr>" + "".join(f"<td>{esc(value)}</td>" for value in row) + "</tr>"
            for row in block.get("rows") or []
        )
        extra += (
            '<div class="table-wrap"><table class="editorial-table">'
            f"<thead><tr>{headings}</tr></thead><tbody>{rows}</tbody></table></div>"
        )
    elif display == "steps":
        steps = "".join(
            '<div class="protocol-step">'
            f'<div class="step-number">{esc(item.get("label", ""))}</div>'
            f'<h3>{esc(item.get("title", ""))}</h3><p>{esc(item.get("body", ""))}</p>'
            "</div>"
            for item in items
        )
        extra += f'<div class="protocol-grid">{steps}</div>'
    elif display == "comparisons":
        comparisons = "".join(
            '<div class="comparison">'
            f'<div class="not-this"><span>NOT THIS</span><p>{esc(item.get("bad", ""))}</p></div>'
            f'<div class="do-this"><span>DO THIS</span><p>{esc(item.get("good", ""))}</p>'
            f'<div class="consequence">{esc(item.get("consequence", ""))}</div></div>'
            "</div>"
            for item in items
        )
        extra += f'<div class="comparisons">{comparisons}</div>'
    elif display == "checklist":
        questions = "".join(
            f'<li><span>{index:02d}</span><p>{esc(item)}</p></li>'
            for index, item in enumerate(items, start=1)
        )
        extra += f'<ol class="audit-list">{questions}</ol>'
    elif display == "source_manifest":
        source_rows = []
        source_records = package["sources"]
        if public_preview:
            selected_ids = [
                str(source_id)
                for source_id in public_config.get("public_source_ids") or []
            ]
            selected_sources = [
                source_records[source_id]
                for source_id in selected_ids
                if source_id in source_records
            ]
            for source in selected_sources:
                public_note = (public_config.get("public_source_notes") or {}).get(
                    str(source.get("source_id", "")),
                    source.get("limitations", ""),
                )
                source_rows.append(
                    "<tr>"
                    f'<td><span class="source-tier">{esc(source.get("source_type", "").replace("_", " "))}</span></td>'
                    f'<td><a href="{esc(source.get("locator", ""))}">{esc(source.get("title", ""))}</a>'
                    f'<small>{esc(source.get("issuer_or_author", ""))}</small></td>'
                    f'<td>{esc(public_note)}</td>'
                    "</tr>"
                )
            extra += (
                '<div class="table-wrap"><table class="editorial-table source-table"><thead><tr>'
                "<th>TYPE</th><th>SOURCE</th><th>HOW TO USE IT</th>"
                f"</tr></thead><tbody>{''.join(source_rows)}</tbody></table></div>"
            )
        else:
            for source in source_records.values():
                use = str(source.get("governing_use", "")).replace("_", " ")
                source_check = (
                    "source checked"
                    if source.get("verification_status") == "verified"
                    else str(source.get("verification_status", "pending")).replace("_", " ")
                )
                claim_use = str(
                    source.get("claim_use_status", "claim review pending")
                ).replace("_", " ")
                source_rows.append(
                    "<tr>"
                    f'<td><span class="source-tier">{esc(source.get("authority_tier", ""))}</span></td>'
                    f'<td><a href="{esc(source.get("locator", ""))}">{esc(source.get("title", ""))}</a>'
                    f'<small>{esc(source.get("issuer_or_author", ""))}</small></td>'
                    f"<td>{esc(source.get('country', ''))}<small>{esc(use)}</small></td>"
                    f'<td><span class="source-status">{esc(source_check)}</span>'
                    f'<span class="claim-use-status">{esc(claim_use)}</span>'
                    f'<small>{esc(source.get("limitations", ""))}</small></td>'
                    "</tr>"
                )
            extra += (
                '<div class="accuracy-panel"><h3>Working evidence register</h3>'
                '<p>A checked source is not the same as a verified claim. United States governing '
                "sources remain separate from research-only studies, and every claim use stays "
                "pending until its independent and qualified reviews are complete.</p></div>"
                '<div class="table-wrap"><table class="editorial-table source-table"><thead><tr>'
                "<th>TIER</th><th>SOURCE</th><th>SCOPE</th><th>STATUS AND LIMIT</th>"
                f"</tr></thead><tbody>{''.join(source_rows)}</tbody></table></div>"
            )

    heading = f"<h2>{title}</h2>" if title else ""
    pullquote = ""
    if block.get("pullquote"):
        pullquote = (
            '<div class="pullquote">'
            f'<p>{esc(block.get("pullquote", ""))}</p>'
            f'<span>{esc(block.get("pullquote_credit", ""))}</span>'
            "</div>"
        )
    evidence = (
        ""
        if public_preview
        else _claim_evidence(block, package["claims"], package["sources"])
    )
    return (
        f'<article class="block block-{esc(block_type)}" id="{block_id}">'
        f"{heading}{badges}{body}{extra}{evidence}{pullquote}</article>"
    )


def _render_public_orientation(
    learning: dict[str, Any],
    public_config: dict[str, Any],
) -> str:
    """Render the instructional orientation the learner sees before the topic.

    The learning objectives already exist in ``learning.yaml``. This surface is
    where the learner finally sees the promise the package makes internally.
    """
    experience = learning.get("learner_experience") or {}
    orientation = experience.get("orientation") or {}
    profile = learning.get("learning") or {}
    if not orientation:
        return ""

    overrides = public_config.get("orientation_overrides") or {}
    if isinstance(overrides, dict):
        orientation = {**orientation, **overrides}

    outcomes = profile.get("outcomes") or []
    outcome_html = "".join(
        f"<li>{esc(outcome)}</li>" for outcome in outcomes if str(outcome).strip()
    )
    prior = profile.get("prior_knowledge") or []
    prior_html = "".join(
        f"<li>{esc(item)}</li>" for item in prior if str(item).strip()
    )

    prior_section = ""
    if prior_html:
        prior_section = f"""
      <div class="orientation-card">
        <h3>What you need first</h3>
        <ul>{prior_html}</ul>
      </div>"""

    outcome_section = ""
    if outcome_html:
        outcome_section = f"""
    <div class="orientation-outcomes">
      <h3>What you will be able to do</h3>
      <ol>{outcome_html}</ol>
    </div>"""

    return f"""<section class="orientation" aria-labelledby="orientation-title">
  <div class="wrap">
    <p class="section-kicker">START HERE</p>
    <h2 id="orientation-title">{esc(orientation.get("subject"))}</h2>
    <div class="orientation-grid">
      <div class="orientation-card">
        <h3>Who this is for</h3>
        <p>{esc(orientation.get("audience"))}</p>
      </div>
      <div class="orientation-card">
        <h3>Why it matters</h3>
        <p>{esc(orientation.get("why_it_matters"))}</p>
      </div>{prior_section}
      <div class="orientation-card">
        <h3>How long it takes</h3>
        <p>{esc(orientation.get("time_estimate"))}</p>
      </div>
    </div>{outcome_section}
    <p class="orientation-boundary"><b>What this does not cover:</b>
      {esc(orientation.get("scope_boundary"))}</p>
  </div>
</section>"""


def _render_public_takeaway(public_config: dict[str, Any]) -> str:
    takeaway = public_config.get("quick_takeaway") or {}
    items = takeaway.get("items") or []
    if not items:
        return ""
    item_html = "".join(
        f"<li>{esc(item)}</li>" for item in items if str(item).strip()
    )
    return f"""<section class="quick-takeaway" aria-labelledby="quick-takeaway-title">
  <div class="wrap">
    <p class="section-kicker">{esc(takeaway.get("label", "IN 30 SECONDS"))}</p>
    <h2 id="quick-takeaway-title">{esc(takeaway.get("title", "The idea in one pass"))}</h2>
    <ol>{item_html}</ol>
  </div>
</section>"""


def _render_public_navigation(public_config: dict[str, Any]) -> str:
    entries = public_config.get("primary_navigation") or [
        {"label": "Start", "href": "#beat-01-why"},
        {"label": "Explore", "href": "#block-jar"},
        {"label": "Graph", "drawer": "graph-drawer"},
        {"label": "Community", "drawer": "community-drawer"},
    ]
    controls = []
    for entry in entries[:4]:
        if not isinstance(entry, dict):
            continue
        label = esc(entry.get("label", "Open"))
        drawer = str(entry.get("drawer", ""))
        href = str(entry.get("href", ""))
        if drawer:
            controls.append(
                f'<button type="button" data-drawer-open="{esc(drawer)}">{label}</button>'
            )
        elif href:
            controls.append(f'<a href="{esc(href)}">{label}</a>')
    return "".join(controls)


def _render_public_finish(package: dict[str, Any], public_config: dict[str, Any]) -> str:
    integration = public_config.get("integration") or {}
    forum_url = str(integration.get("community_url", "#owos-concept-community"))
    recap = public_config.get("final_recap") or []
    recap_html = "".join(
        "<article>"
        f'<span>{esc(item.get("label", ""))}</span>'
        f'<p>{esc(item.get("body", ""))}</p>'
        "</article>"
        for item in recap
        if isinstance(item, dict)
    )
    disclaimer = str(
        public_config.get(
            "short_disclaimer",
            "This brief explains the concept. Facility decisions still require your approved procedures and qualified judgment.",
        )
    )
    return f"""<section class="concept-finish" id="owos-concept-finish">
  <div class="wrap">
    <div class="final-recap" aria-labelledby="final-recap-title">
      <p class="section-kicker">BEFORE YOU LEAVE</p>
      <h2 id="final-recap-title">Carry three things forward.</h2>
      <div class="final-recap-grid">{recap_html}</div>
    </div>
    <section class="reader-voices" data-concept-testimonials aria-labelledby="reader-voices-title" hidden>
      <p class="section-kicker">FROM THE LEARNING COMMUNITY</p>
      <h2 id="reader-voices-title">What readers carried forward.</h2>
      <div class="reader-voices-grid" data-concept-testimonial-list></div>
      <p class="reader-voices-note">Shared with the reader's permission and approved by an OWOS learning steward. Reader comments are not technical evidence or vendor endorsements.</p>
    </section>
    <div class="community-feedback">
      <div>
        <p class="section-kicker">COMMENT ON THIS BRIEF</p>
        <h3>See something we should check or improve?</h3>
        <p>Tell us what worked, what connected across sectors, or what should be checked. Positive feedback, technical corrections, source suggestions, questions, and field observations all enter the moderated OWOS Community and Concept Brief review queue.</p>
      </div>
      <form data-concept-feedback action="{esc(forum_url)}" method="get">
        <label for="concept-feedback-kind">Comment type</label>
        <select id="concept-feedback-kind" name="kind">
          <option value="appreciation">What worked for me</option>
          <option value="technical-feedback">Technical accuracy</option>
          <option value="source-suggestion">Source suggestion</option>
          <option value="question">Question</option>
          <option value="field-note">Field observation</option>
        </select>
        <label for="concept-feedback-body">Comment</label>
        <textarea id="concept-feedback-body" name="body" maxlength="1800" required placeholder="Tell us what should be checked, corrected, clarified, or discussed. Do not include confidential facility information."></textarea>
        <label class="testimonial-consent" data-testimonial-consent-row>
          <input type="checkbox" name="testimonial-consent" value="yes" data-testimonial-consent>
          If I selected “What worked for me,” OWOS may publish this comment with my name, role, and organization after moderator approval.
        </label>
        <div class="feedback-actions">
          <button class="primary-action" type="submit">Post comment</button>
          <a href="{esc(forum_url)}">Open the full Community</a>
        </div>
        <p class="feedback-status" data-concept-feedback-status role="status" aria-live="polite"></p>
      </form>
    </div>
    <p class="feedback-disclaimer">{esc(disclaimer)}</p>
  </div>
</section>"""


def _render_public_connections(package: dict[str, Any], public_config: dict[str, Any]) -> str:
    integration = public_config.get("integration") or {}
    related_items = integration.get("related_learning") or []
    related_cards = "".join(
        '<article class="connection-card">'
        f'<span>{esc(item.get("kind", "Related concept"))}</span>'
        f'<h3>{esc(item.get("title", ""))}</h3>'
        f'<p>{esc(item.get("description", ""))}</p>'
        f'<a href="{esc(item.get("href", "#"))}">{esc(item.get("action", "Explore"))}</a>'
        "</article>"
        for item in related_items
        if isinstance(item, dict)
    )
    questions = "".join(
        f'<button type="button" class="seed-question">{esc(question)}</button>'
        for question in package["community"].get("seed_questions") or []
    )
    sop_outline_items = integration.get("sop_outline") or []
    sop_outline = "".join(
        "<li>"
        f'<b>{esc(item.get("section", ""))}</b>'
        f'<span>{esc(item.get("prompt", ""))}</span>'
        "</li>"
        for item in sop_outline_items
        if isinstance(item, dict)
    )
    sop_outline_text = "\n\n".join(
        f'{index}. {item.get("section", "")}\n{item.get("prompt", "")}'
        for index, item in enumerate(sop_outline_items, start=1)
        if isinstance(item, dict)
    )
    sop_outline_payload = json.dumps(sop_outline_text, ensure_ascii=True).replace(
        "<", "\\u003c"
    )
    sop_title = str(
        integration.get("sop_title", "Concept response SOP outline")
    )
    sop_intro = str(
        integration.get(
            "sop_intro",
            "The public value is a clear starting structure, not a pretend facility SOP. "
            "Copy this outline into the utility's approved workspace, then fill it with "
            "site-specific evidence and named authority.",
        )
    )
    forum_url = str(integration.get("community_url", "#owos-concept-community"))
    graph_url = str(
        integration.get(
            "graph_url",
            f"/os?node={str(package['brief'].get('slug', 'concept-brief'))}",
        )
    )
    graph_cards = "".join(
        '<article class="drawer-connection">'
        f'<span>{esc(item.get("kind", "Related concept"))}</span>'
        f'<h3>{esc(item.get("title", ""))}</h3>'
        f'<p>{esc(item.get("description", ""))}</p>'
        f'<a href="{esc(item.get("href", "#"))}">{esc(item.get("action", "Review in this brief"))}</a>'
        "</article>"
        for item in related_items[:4]
        if isinstance(item, dict)
    )
    return f"""
<section class="connected-learning" id="owos-concept-related">
  <div class="wrap">
    <p class="section-kicker">KEEP LEARNING</p>
    <h2>Follow the process, not just the definition.</h2>
    <p class="section-lead">These connections help you continue the diagnosis without exposing internal research records or turning a learning page into operating authority.</p>
    <div class="connection-grid">{related_cards}</div>
  </div>
</section>
<section class="community-public" id="owos-concept-community">
  <div class="wrap community-layout">
    <div>
      <p class="section-kicker">PRACTITIONER CONVERSATION</p>
      <h2>Bring the question. Protect the facility.</h2>
      <p>{esc(package["community"]["discussion_boundary"])}</p>
      <p class="privacy-warning"><b>Before posting:</b> {esc(package["community"]["facility_information_warning"])}</p>
      <a class="primary-action" href="{esc(forum_url)}">Open the OWOS Community</a>
    </div>
    <div class="question-list" aria-label="Conversation starters">{questions}</div>
  </div>
</section>
<section class="sop-workspace" id="owos-concept-sop">
  <div class="wrap">
    <p class="section-kicker">A USEFUL NEXT STEP</p>
    <h2>Take the outline. Build the procedure under control.</h2>
    <p class="section-lead">{esc(sop_intro)}</p>
    <div class="sop-grid">
      <article class="sop-outline-card">
        <h3>{esc(sop_title)}</h3>
        <ol>{sop_outline}</ol>
        <div class="sop-actions">
          <button type="button" class="primary-action" id="copy-sop-outline">Copy the outline</button>
          <span class="copy-status" id="copy-sop-status" role="status" aria-live="polite"></span>
        </div>
        <script type="application/json" id="sop-outline-data">{sop_outline_payload}</script>
      </article>
      <aside class="sop-boundary-card">
        <p class="section-kicker">WHERE THE BRIEF STOPS</p>
        <h3>A real SOP is a separate product.</h3>
        <p>A facility-specific SOP needs controlled inputs, applicable authority review, approved chemicals and equipment, named change authority, monitoring, rollback, safety review, version history, and approvals.</p>
        <p>If OWOS builds that later, it should be an authenticated agent workflow. The agent would assemble evidence and route review. It would never invent settings or approve its own work.</p>
      </aside>
    </div>
  </div>
</section>
<div class="drawer-backdrop" data-drawer-close hidden></div>
<aside class="context-drawer" id="graph-drawer" role="dialog" aria-modal="true" aria-labelledby="graph-drawer-title" hidden>
  <button class="drawer-close" type="button" data-drawer-close aria-label="Close concept map">Close</button>
  <p class="section-kicker">CONCEPT MAP</p>
  <h2 id="graph-drawer-title">See what this concept connects to</h2>
  <p>Use these reviewed learning connections to move through the treatment sequence without leaving this brief.</p>
  <div class="drawer-connection-grid">{graph_cards}</div>
  <a class="primary-action" href="{esc(graph_url)}">Open the full OWOS Graph</a>
  <a class="drawer-bottom-link" href="#owos-concept-related">See all related learning</a>
</aside>
<aside class="context-drawer" id="community-drawer" role="dialog" aria-modal="true" aria-labelledby="community-drawer-title" hidden>
  <button class="drawer-close" type="button" data-drawer-close aria-label="Close discussion">Close</button>
  <p class="section-kicker">DISCUSS</p>
  <h2 id="community-drawer-title">Start with a bounded question</h2>
  <div class="question-list">{questions}</div>
  <p class="privacy-warning">{esc(package["community"]["facility_information_warning"])}</p>
  <a class="primary-action" href="{esc(forum_url)}">Continue in the OWOS Community</a>
  <a class="drawer-bottom-link" href="#owos-concept-community">Read the discussion boundary</a>
</aside>"""


def _render_public_commercial(
    package: dict[str, Any],
    asset_prefix: str,
) -> str:
    config = package["commercial"].get("public_placements") or {}
    placements = config.get("placements") or []
    if not placements:
        return ""
    cards = []
    for placement in placements:
        if not isinstance(placement, dict):
            continue
        placement_id = str(placement.get("placement_id", ""))
        slot = str(placement.get("slot", ""))
        image = _portable_asset_href(
            Path(package["package_dir"]),
            str(placement.get("logo", "")),
            asset_prefix,
            inline=True,
        )
        is_placeholder = placement.get("placeholder") is True
        if is_placeholder and config.get("show_inactive_placeholders") is not True:
            continue
        url = str(placement.get("url", ""))
        action = (
            f'<a class="commercial-action" data-placement-link href="{esc(url)}" '
            f'target="_blank" rel="noopener sponsored">{esc(placement.get("cta", "Learn more"))}</a>'
            if url and not is_placeholder
            else '<span class="commercial-action disabled">Reserved preview</span>'
        )
        cards.append(
            f"""<article class="commercial-card{" placeholder" if is_placeholder else ""}"
 data-placement-id="{esc(placement_id)}" data-placement-slot="{esc(slot)}">
  <div class="commercial-label" data-placement-label>{esc(placement.get("label", ""))}</div>
  <div class="commercial-logo-wrap"><img data-placement-logo src="{esc(image)}"
    alt="{esc(placement.get("logo_alt", placement.get("organization", "")))}"></div>
  <div class="commercial-copy">
    <h3 data-placement-headline>{esc(placement.get("headline", ""))}</h3>
    <p data-placement-body>{esc(placement.get("body", ""))}</p>
    {action}
  </div>
</article>"""
        )
    if not cards:
        return ""
    return f"""<aside class="commercial-zone" id="owos-commercial-placements"
 aria-labelledby="commercial-title">
  <div class="wrap">
    <div class="commercial-head">
      <div><p class="section-kicker">PUBLISHER AND VENDOR CONNECTIONS</p>
      <h2 id="commercial-title">Built with independence visible.</h2></div>
      <p>{esc(config.get("disclosure", ""))}</p>
    </div>
    <div class="commercial-grid">{"".join(cards)}</div>
    <p class="commercial-directory-note">Commercial placement is separate from evidence and neutral
      directory results. <a href="/directory">Browse the vendor community</a>.</p>
  </div>
</aside>"""


def build_html(
    package_dir: Path,
    output: Path,
    *,
    allow_pre_research_prototype: bool = False,
    public_preview: bool = False,
    public_config_path: Path | None = None,
) -> dict[str, Any]:
    research_plan_path = package_dir.resolve() / "research-plan.yaml"
    if research_plan_path.is_file():
        research_plan = load_yaml(research_plan_path)
        cited_html = research_plan.get("cited_html") or {}
        if (
            isinstance(cited_html, dict)
            and cited_html.get("allowed") is not True
            and not allow_pre_research_prototype
        ):
            raise ConceptBriefError(
                "cited HTML generation is blocked until research, original-source verification, "
                "and evidence-backed narrative and storyboard approval are complete; the existing "
                "pre-research draft remains frozen"
            )
    package = validate_package(package_dir, release_ready=False)
    public_config: dict[str, Any] = {}
    if public_preview:
        resolved_public_config_path = (
            public_config_path.resolve()
            if public_config_path is not None
            else package_dir.resolve() / "public-preview.yaml"
        )
        if not resolved_public_config_path.is_file():
            raise ConceptBriefError(
                "public preview requires a governed public preview configuration"
            )
        public_config = load_yaml(resolved_public_config_path)
        if public_config.get("mode") != "public_review_preview":
            raise ConceptBriefError(
                "public-preview.yaml mode must be public_review_preview"
            )
        if public_config.get("brief_id") != package["brief"]["brief_id"]:
            raise ConceptBriefError(
                "public-preview.yaml brief_id must match the package brief"
            )
        navigation = public_config.get("primary_navigation") or []
        if not 1 <= len(navigation) <= 4:
            raise ConceptBriefError(
                "public-preview.yaml primary_navigation must contain one to four controls"
            )
        navigation_drawers = {
            str(item.get("drawer", ""))
            for item in navigation
            if isinstance(item, dict) and item.get("drawer")
        }
        for required_drawer in ("graph-drawer", "community-drawer"):
            if required_drawer not in navigation_drawers:
                raise ConceptBriefError(
                    "public-preview.yaml primary_navigation requires top Graph and Community drawer controls"
                )
        takeaway_items = (public_config.get("quick_takeaway") or {}).get("items") or []
        if not 2 <= len(takeaway_items) <= 4:
            raise ConceptBriefError(
                "public-preview.yaml quick_takeaway must contain two to four concise items"
            )
        recap = public_config.get("final_recap") or []
        if len(recap) != 3 or any(
            not isinstance(item, dict)
            or not str(item.get("label", "")).strip()
            or not str(item.get("body", "")).strip()
            for item in recap
        ):
            raise ConceptBriefError(
                "public-preview.yaml final_recap must contain three labeled conclusions"
            )
        if not str(public_config.get("short_disclaimer", "")).strip():
            raise ConceptBriefError(
                "public-preview.yaml short_disclaimer is required"
            )
    output = output.resolve()
    asset_prefix = os.path.relpath(package["package_dir"], output.parent)
    if asset_prefix == ".":
        asset_prefix = ""
    else:
        asset_prefix = asset_prefix.rstrip("/") + "/"
    brief = package["brief"]
    blocks = package["blocks"]
    claims = package["claims"]
    beats_html = []
    public_beat_index = 0
    omitted_blocks = {
        str(block_id)
        for block_id in public_config.get("omit_block_ids") or []
    }
    for beat_index, beat in enumerate(package["storyboard"]["beats"], start=1):
        surface = str(beat.get("surface"))
        learner_question = str(beat["learner_question"])
        if public_preview:
            learner_question = str(
                (public_config.get("beat_question_overrides") or {}).get(
                    str(beat.get("beat_id", "")),
                    learner_question,
                )
            )
        beat_blocks = [
            blocks[str(block_id)]
            for block_id in beat.get("block_ids") or []
            if str(block_id) in blocks
            and (not public_preview or str(block_id) not in omitted_blocks)
        ]
        if public_preview and not beat_blocks:
            continue
        public_beat_index += 1
        display_beat_index = public_beat_index if public_preview else beat_index
        content = "".join(
            _render_block(
                block,
                package,
                asset_prefix,
                public_preview=public_preview,
                public_config=public_config,
            )
            for block in beat_blocks
        )
        band_title = beat_blocks[0].get("title", "") if beat_blocks else ""
        if public_preview and beat_blocks:
            public_override = (public_config.get("block_overrides") or {}).get(
                str(beat_blocks[0].get("block_id", "")),
                {},
            )
            if isinstance(public_override, dict):
                band_title = public_override.get("title", band_title)
        beats_html.append(
            '<div class="band"><div class="band-in">'
            f'<div class="band-n">{display_beat_index:02d}</div><div class="band-txt">'
            f'<div class="band-k">{esc(learner_question)}</div>'
            f'<div class="band-h">{esc(band_title)}</div></div></div></div>'
            f'<section class="beat surface-{esc(surface)}" '
            f'id="{esc(beat["beat_id"])}">'
            f'<div class="wrap"><p class="learner-question">{esc(learner_question)}</p>'
            f"{content}</div></section>"
        )

    graph_links = []
    for edge in package["edges"].values():
        if edge.get("edge_type") == "SPONSORED_BY":
            continue
        graph_links.append(
            "<li>"
            f"<b>{esc(edge['edge_type'])}</b> "
            f"{esc(edge['from_node'])} → {esc(edge['to_node'])}"
            "</li>"
        )
    pending = [
        claim
        for claim in claims.values()
        if claim.get("material") is True
        and claim.get("verification_status") not in {"verified", "contested"}
    ]
    status_text = (
        str(public_config.get("status_notice", "Public review preview."))
        if public_preview
        else (
            "Working preview. Facts and technical review remain incomplete. Do not use as operational, "
            "engineering, regulatory, safety, or health guidance."
        )
    )
    community_questions = "".join(
        f"<li>{esc(question)}</li>"
        for question in package["community"].get("seed_questions") or []
    )
    presentation_css_path = package_dir / "presentation.css"
    presentation_css = (
        presentation_css_path.read_text(encoding="utf-8")
        if presentation_css_path.is_file()
        else ""
    )
    if public_preview:
        configured_brand_css = public_config.get("brand_css")
        graphite_tokens_path = (
            Path(__file__).resolve().parent.parent
            / "core"
            / "brand"
            / "owos-graphite.css"
        )
        if not graphite_tokens_path.is_file():
            raise ConceptBriefError(
                f"shared Graphite token CSS does not exist: {graphite_tokens_path}"
            )
        presentation_css += "\n" + graphite_tokens_path.read_text(encoding="utf-8")
        brand_css_path = (
            (package_dir / str(configured_brand_css)).resolve()
            if configured_brand_css
            else None
        )
        if configured_brand_css:
            try:
                brand_css_path.relative_to(package_dir.resolve())
            except ValueError as error:
                raise ConceptBriefError(
                    "brand_css must stay inside the Concept Brief package"
                ) from error
            if not brand_css_path.is_file():
                raise ConceptBriefError(f"brand_css does not exist: {brand_css_path}")
            presentation_css += "\n" + brand_css_path.read_text(encoding="utf-8")
        shell_css_path = (
            Path(__file__).resolve().parent.parent
            / "core"
            / "brand"
            / "owos-concept-brief-shell.css"
        )
        if not shell_css_path.is_file():
            raise ConceptBriefError(
                f"shared Concept Brief shell CSS does not exist: {shell_css_path}"
            )
        presentation_css += "\n" + shell_css_path.read_text(encoding="utf-8")
    # The accessibility floor goes last on purpose. Contrast, gutter, and touch
    # targets are a release gate, not a palette choice, so a package brand
    # stylesheet must not be able to override them by loading after the shell.
    presentation_css += "\n" + ACCESSIBILITY_FLOOR
    title_parts = re.split(r"\s+vs\s+", str(brief["title"]), maxsplit=1, flags=re.IGNORECASE)
    hero_title = (
        f"{esc(title_parts[0])}<br><span style=\"color:var(--gold)\">VS</span> {esc(title_parts[1])}"
        if len(title_parts) == 2
        else esc(brief["title"])
    )
    display_version = (
        str(public_config.get("public_version_label", "PUBLIC EDITION"))
        if public_preview
        else str(brief["version"])
    )
    scope_label = (
        str(
            public_config.get(
                "scope_label",
                "DRINKING WATER · UNITED STATES AUTHORITY · QUALITATIVE JAR · EDUCATIONAL USE",
            )
        )
        if public_preview
        else "DRINKING WATER · UNITED STATES AUTHORITY · QUALITATIVE JAR · GOVERNED CORRECTIONS"
    )
    body_theme_attr = ' data-owos-theme="graphite"' if public_preview else ""
    html_text = f"""<!doctype html>
<html lang="{esc(brief['language'])}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="owos-contract" content="{CONTRACT}">
<meta name="owos-compiler-version" content="{COMPILER_VERSION}">
<meta name="owos-package-checksum" content="{package['checksum']}">
<meta name="owos-brief-id" content="{esc(brief['brief_id'])}">
<meta name="owos-brief-version" content="{esc(display_version)}">
<meta name="owos-release-state" content="{"public-review-preview" if public_preview else "working-preview"}">
<meta name="owos-evidence-cutoff" content="{esc(brief['evidence_cutoff'])}">
<title>{esc(brief['title'])} | OWOS Concept Brief</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&amp;family=Libre+Baskerville:ital@0;1&amp;family=Space+Mono:wght@400;700&amp;family=Barlow:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet">
<style>
:root{{--black:#080808;--panel:#151515;--white:#fff;--off:#f4f7fa;--ink:#10263b;
--blue:#1d5c90;--gold:#ebca62;--cyan:#bae7f9;--line:#d7e4eb;--red:#9c2226}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;font:16px/1.65
system-ui,sans-serif;color:var(--ink);background:var(--off)}}.wrap{{width:min(1080px,calc(100% -
32px));margin:auto}}.status{{padding:14px 16px;background:#fff3cd;color:#4f3c00;border-bottom:2px
solid #d4a600;font-weight:700}}header{{padding:72px 0;background:var(--black);color:#fff}}header
h1{{font-size:clamp(42px,7vw,82px);line-height:.98;margin:.15em 0}}header p{{max-width:760px;
color:#e8e8e8}}.meta{{font:12px ui-monospace,monospace;color:var(--gold);overflow-wrap:anywhere}}
.beat{{padding:64px 0}}
.surface-white{{background:var(--white)}}.surface-off_white{{background:var(--off)}}
.surface-black{{background:var(--black);color:#eee}}.surface-blue{{background:var(--blue);
color:#fff;border-bottom:4px solid var(--gold)}}.learner-question{{font:700 12px ui-monospace,
monospace;text-transform:uppercase;letter-spacing:1.3px;color:var(--blue)}}
.surface-black .learner-question,.surface-blue .learner-question{{color:var(--cyan)}}.block{{
margin:26px 0;max-width:900px}}.block h2{{font-size:clamp(28px,4vw,45px);line-height:1.08}}
.block-callout,.block-decision,.block-protocol,.block-diagnostic{{padding:24px;border-left:4px
solid var(--gold);background:rgba(29,92,144,.08)}}.surface-black .block-callout,
.surface-black .block-decision,.surface-black .block-protocol,.surface-black .block-diagnostic{{
background:#151515}}.claim{{display:inline-block;margin:0 7px 8px 0;padding:4px 8px;border-radius:3px;
font:700 10px ui-monospace,monospace;text-transform:uppercase;background:#dbeaf3;color:#164f74}}
.block-heading{{margin-top:44px}}.block-metric,.block-evidence,.block-role,
.block-connected_learning{{padding:22px;background:rgba(29,92,144,.05);
border-top:2px solid var(--blue)}}.surface-black .block-metric,.surface-black .block-evidence,
.surface-black .block-role,.surface-black .block-connected_learning{{background:#141414;
border-top-color:var(--cyan)}}
.orientation{{padding:64px 0;background:var(--off);border-bottom:2px solid var(--gold)}}
.orientation h2{{font-size:clamp(26px,3.4vw,40px);line-height:1.12;margin:6px 0 26px;
max-width:900px}}.orientation-grid{{display:grid;
grid-template-columns:repeat(auto-fit,minmax(232px,1fr));gap:18px}}
.orientation-card{{padding:20px;background:var(--white);border-left:3px solid var(--blue)}}
.orientation-card h3{{margin:0 0 8px;font:700 12px ui-monospace,monospace;
text-transform:uppercase;letter-spacing:1.1px;color:var(--blue)}}
.orientation-card p,.orientation-card li{{margin:0 0 6px;font-size:15px;line-height:1.55}}
.orientation-card ul{{margin:0;padding-left:18px}}
.orientation-outcomes{{margin-top:26px;padding:24px;background:var(--black);color:#eee}}
.orientation-outcomes h3{{margin:0 0 12px;font:700 12px ui-monospace,monospace;
text-transform:uppercase;letter-spacing:1.1px;color:var(--cyan)}}
.orientation-outcomes ol{{margin:0;padding-left:20px;max-width:860px}}
.orientation-outcomes li{{margin:0 0 8px;line-height:1.55}}
.orientation-boundary{{margin:22px 0 0;max-width:860px;padding:14px 16px;
border-left:3px solid var(--gold);background:rgba(197,160,74,.1);font-size:15px}}
.definition-set{{display:grid;gap:16px;margin-top:20px}}
.definition{{padding:20px;background:var(--white);border-left:3px solid var(--gold)}}
.surface-black .definition{{background:#141414}}
.definition-term{{margin:0 0 8px;font-size:19px;line-height:1.25}}
.definition p{{margin:0 0 7px;font-size:15px;line-height:1.55}}
.definition-example{{color:#2c4a5e}}.surface-black .definition-example{{color:#b9cbd5}}
.definition-limit{{color:#6b4d16}}.surface-black .definition-limit{{color:#d8bd7c}}
.worked-example{{margin-top:20px;padding:24px;background:rgba(29,92,144,.07);
border-left:4px solid var(--blue)}}.surface-black .worked-example{{background:#131c22}}
.worked-label{{margin:0 0 12px;font:700 11px ui-monospace,monospace;text-transform:uppercase;
letter-spacing:1.2px;color:var(--blue)}}.surface-black .worked-label{{color:var(--cyan)}}
.worked-example p{{margin:0 0 9px;font-size:15px;line-height:1.6}}
.visual-component{{padding:20px;border:1px dashed #9bb3c2}}
.visual-alt{{margin:10px 0 0;font-size:14px;color:#3d5666}}
.claim-pending,.claim-rejected{{background:#fde4e4;color:var(--red)}}figure{{margin:20px 0}}
figure img{{max-width:100%;height:auto;display:block}}figcaption{{padding:14px;background:#edf5f8;
color:#173145}}.interaction{{padding:24px;background:#000;color:#fff;border:1px solid #333}}
.boundary{{color:#c7d8e2;font-size:14px}}.transfer-layout{{display:grid;
grid-template-columns:minmax(280px,.8fr) minmax(320px,1.2fr);gap:24px;margin-top:24px}}
.transfer-controls fieldset{{display:grid;gap:8px;margin:0 0 14px;padding:14px;border:1px solid #3e5869}}
.transfer-controls legend{{padding:0 7px;color:#8ed0ed;font:700 11px ui-monospace,monospace;
letter-spacing:.08em}}.transfer-choice{{display:grid;gap:4px;min-height:58px;padding:11px 12px;
border:1px solid #54788e;background:#10232e;color:#fff;text-align:left;font:inherit;cursor:pointer}}
.transfer-choice span{{color:#b9cbd5;font-size:12px;line-height:1.35}}
.transfer-choice[aria-pressed="true"]{{border-color:var(--gold);box-shadow:inset 4px 0 0 var(--gold);
background:#263321}}.transfer-choice:focus-visible{{outline:3px solid #fff;outline-offset:2px}}
.transfer-choice.compact{{min-height:52px}}.transfer-stage{{display:grid;align-content:start;gap:16px;
padding:20px;background:#111a20;border:1px solid #324754}}.transfer-boundary-graphic{{display:grid;
grid-template-columns:90px minmax(150px,1fr) 90px;align-items:center;gap:10px;padding:26px 8px}}
.transfer-box{{display:grid;place-items:center;min-height:150px;padding:18px;border:3px dashed #42d3b3;
text-align:center}}.transfer-box b{{color:#fff;font-size:22px}}.transfer-box span{{color:#9db4c2;
font-size:12px}}.transfer-arrow{{position:relative;color:#42d3b3;font:700 11px
ui-monospace,monospace;text-align:center}}.transfer-arrow:after{{content:"";display:block;
height:4px;margin-top:8px;background:#42d3b3}}.transfer-arrow.in:after{{clip-path:polygon(0 25%,80% 25%,80% 0,100% 50%,80% 100%,80% 75%,0 75%)}}
.transfer-arrow.out:after{{clip-path:polygon(0 25%,80% 25%,80% 0,100% 50%,80% 100%,80% 75%,0 75%)}}
.transfer-ledger{{display:grid;gap:1px;margin:0;background:#344854}}.transfer-ledger div{{display:grid;
grid-template-columns:1fr 1fr;gap:12px;padding:11px 13px;background:#17242c}}.transfer-ledger dt{{
color:#9db4c2}}.transfer-ledger dd{{margin:0;text-align:right;font-weight:800}}
.transfer-ledger .transfer-residual{{background:#2c2118}}.transfer-residual-value{{color:var(--gold);
font-size:24px}}.transfer-result{{padding:15px;border-left:4px solid #42d3b3;background:#172d28}}
.transfer-stop{{padding:14px;border:1px solid #8e3d3d;background:#281717;color:#ffd8d8}}
.transfer-fallback{{padding:18px;background:#fff;color:#10263b}}.quick-nav{{display:flex;flex-wrap:wrap;gap:10px;
margin-top:28px}}.quick-nav a,.quick-nav button{{display:inline-block;padding:10px 14px;border:1px solid #5f7483;
border-radius:999px;background:transparent;color:#fff;text-decoration:none;font:inherit;font-weight:700;
cursor:pointer}}.quick-nav a:hover,.quick-nav button:hover,
.quick-nav a:focus-visible,.quick-nav button:focus-visible{{background:#fff;color:#07131d;outline:3px solid var(--gold);
outline-offset:2px}}.jar-layout{{display:grid;grid-template-columns:minmax(0,1.35fr)
minmax(250px,.65fr);gap:24px;align-items:start}}.jar-controls fieldset{{border:1px solid #3e5869;
border-radius:8px;margin:0 0 16px;padding:14px}}.jar-controls legend{{padding:0 7px;
font-weight:800}}.jar-control{{min-height:44px;margin:4px;padding:9px 12px;border:1px solid #7dbcd7;
border-radius:6px;background:#102f45;color:#fff;font:inherit;font-weight:700;cursor:pointer}}
.jar-control[aria-pressed="true"]{{background:var(--gold);color:#1f1900;border-color:var(--gold)}}
.jar-control:focus-visible{{outline:3px solid #fff;outline-offset:2px}}.jar-view{{max-width:330px;
margin:auto}}.jar-water{{position:relative;min-height:360px;border:4px solid #bae7f9;
border-top:0;border-radius:0 0 34px 34px;overflow:hidden;background:linear-gradient(#183b54,#0d273a)}}
.jar-water:before{{content:"";position:absolute;left:0;right:0;top:0;border-top:3px solid #7dbcd7}}
.particle-field{{position:absolute;inset:18px}}.particle-field i{{position:absolute;width:8px;
height:8px;border-radius:50%;background:#eaf9ff;box-shadow:0 0 0 1px #66b7d6}}
.particle-field i:nth-child(3n+1){{left:18%;top:15%}}.particle-field i:nth-child(3n+2){{left:52%;top:43%}}
.particle-field i:nth-child(3n){{left:78%;top:72%}}.particle-field i:nth-child(4n){{left:35%;top:68%}}
.particle-field i:nth-child(5n){{left:68%;top:22%}}.particle-field i:nth-child(7n){{left:12%;top:82%}}
.jar-model[data-stage="coagulation"] .particle-field i{{width:12px;height:12px}}
.jar-model[data-stage="flocculation"] .particle-field i{{width:22px;height:22px}}
.jar-model[data-stage="separation"] .particle-field i{{width:24px;height:24px;top:auto;bottom:10%}}
.jar-model[data-coagulant="low"] .particle-field i{{width:7px;height:7px}}
.jar-model[data-coagulant="excess"] .particle-field i{{background:#ffd6d6;box-shadow:0 0 0 2px #9c2226}}
.jar-model[data-flocculation="low"] .particle-field i{{max-width:13px;max-height:13px}}
.jar-model[data-flocculation="excess"] .particle-field i{{border-radius:2px;transform:rotate(25deg);
background:#ffbea8}}.jar-visual-label{{text-align:center;color:#bae7f9;font-size:13px}}
.jar-result{{margin-top:18px;padding:18px;border-left:4px solid var(--gold);background:#10212e}}
.jar-result p{{margin:.35em 0}}.jar-question{{color:#fff5ca;font-weight:700}}
.jar-fallback{{padding:18px;background:#fff;color:#10263b}}details{{padding:15px 0;
border-bottom:1px solid var(--line)}}
.concept-assessment{{margin:24px 0;padding:24px;border:2px solid #8cb8cf;background:#f7fbfd;
color:#10263b}}.assessment-kicker{{font:700 11px ui-monospace,monospace;letter-spacing:.12em;
color:#1d5c90}}.assessment-options{{display:grid;gap:10px;margin:18px 0}}
.assessment-option{{display:block;padding:12px;border:1px solid #b7ccd7;background:#fff}}
.assessment-check,.assessment-reveal{{min-height:44px;padding:10px 16px;border:0;
background:#174f77;color:#fff;font:inherit;font-weight:800;cursor:pointer}}
.assessment-check:focus-visible,.assessment-reveal:focus-visible{{outline:3px solid #ebca62;
outline-offset:3px}}.assessment-feedback{{font-weight:800}}.assessment-retry{{font-size:14px}}
.concept-assessment textarea{{display:block;width:100%;margin:10px 0 14px;padding:12px;
font:inherit}}.assessment-model{{margin-top:16px;padding:16px;background:#e5f0f5}}
.guided-rehearsal{{border-color:#43697d;background:#10232e;color:#f2f1ec}}
.guided-rehearsal .assessment-kicker{{color:#8ed0ed}}.rehearsal-intro{{max-width:760px;
color:#d9d6cf}}.rehearsal-case{{display:grid;grid-template-columns:1fr 1fr;gap:1px;
margin:20px 0;background:#43697d;border:1px solid #43697d}}.rehearsal-case>div{{padding:18px;
background:#1c1b19}}.rehearsal-shortcut{{border-left:4px solid #e0a64a}}
.rehearsal-label{{display:block;margin-bottom:7px;color:#8ed0ed;font:700 11px
ui-monospace,monospace;letter-spacing:.12em}}.rehearsal-shortcut .rehearsal-label{{color:#e0a64a}}
.rehearsal-steps{{min-height:172px;padding:22px;border:1px solid #43697d;background:#292826}}
.rehearsal-step span{{color:#8ed0ed;font:700 11px ui-monospace,monospace;letter-spacing:.12em}}
.rehearsal-step h4{{margin:.45em 0;font-size:23px}}.rehearsal-step p{{margin-bottom:0;
color:#d9d6cf}}.rehearsal-controls{{display:flex;align-items:center;justify-content:space-between;
gap:12px;margin:12px 0 22px}}.rehearsal-controls button,.practice-toggle{{min-height:44px;
padding:10px 15px;border:1px solid #7dc6e8;background:transparent;color:#f2f1ec;
font:inherit;font-weight:800;cursor:pointer}}.rehearsal-controls button:disabled{{opacity:.45;
cursor:default}}.rehearsal-progress{{color:#a29c91;font:700 11px ui-monospace,monospace;
letter-spacing:.08em}}.rehearsal-result{{padding:20px;border-left:4px solid #4ac88c;
background:#172d28}}.rehearsal-result p{{margin:0;font-size:18px;font-weight:750}}
.optional-practice{{display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center;
margin-top:24px;padding-top:22px;border-top:1px solid #43697d}}.optional-practice h4{{margin:.35em 0}}
.optional-practice p{{margin:0;color:#d9d6cf}}.practice-panel{{grid-column:1/-1;padding:20px;
border:1px solid #43697d;background:#1c1b19}}.guided-rehearsal textarea{{border:1px solid #7b8d98;
background:#f2f1ec;color:#10232e}}.guided-rehearsal .assessment-model{{background:#dfeff6;
color:#10263b}}.guided-rehearsal .assessment-model p,
.guided-rehearsal .assessment-model b{{color:#10263b}}.guided-rehearsal .assessment-feedback{{color:#8ed0ed}}
.practice-toggle:focus-visible,.rehearsal-controls button:focus-visible{{outline:3px solid #e0a64a;
outline-offset:3px}}@media(max-width:640px){{.rehearsal-case,.optional-practice{{grid-template-columns:1fr}}
.practice-toggle{{width:100%}}.rehearsal-controls{{display:grid;grid-template-columns:1fr 1fr}}
.rehearsal-progress{{grid-column:1/-1;grid-row:1;text-align:center}}}}
.assessment-card-grid,.assessment-work-grid,.assessment-match-grid{{display:grid;gap:12px;
margin:16px 0}}.assessment-card-grid{{grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}}
.assessment-card{{min-height:120px;padding:16px;border:1px solid #8cb8cf;background:#fff;
color:#10263b;font:inherit;font-weight:800;cursor:pointer}}.assessment-card[aria-pressed="true"]{{
background:#10232e;color:#f2f1ec}}.assessment-match-row{{display:grid;
grid-template-columns:minmax(0,1fr) minmax(180px,.6fr);gap:12px;align-items:center}}
.assessment-match-row select{{min-height:44px;padding:8px;font:inherit}}
.assessment-match-row,.assessment-match-row span,.assessment-match-row select{{min-width:0;
max-width:100%}}.assessment-match-row select{{width:100%}}.assessment-match-row span{{
overflow-wrap:anywhere}}
.assessment-work-check{{min-height:44px;padding:10px 16px;border:0;background:#174f77;color:#fff;
font:inherit;font-weight:800}}@media(max-width:640px){{.assessment-match-row{{grid-template-columns:1fr}}}}
summary{{font-weight:750;cursor:pointer}}.connected{{padding:60px 0;background:#fff}}
.evidence-trace{{margin-top:28px;padding:0;border:1px solid #b9cfdb;border-radius:8px;
background:#f7fbfd;color:#10263b;overflow:hidden}}.evidence-trace>summary{{padding:14px 16px;
font:700 12px ui-monospace,monospace;text-transform:uppercase;letter-spacing:.6px;
background:#e5f0f5;color:#164f74}}.evidence-trace>summary span{{float:right;color:#5a6c76}}
.evidence-trace-intro{{padding:14px 16px;border-bottom:1px solid #d7e4eb;font-size:14px}}
.evidence-claim-grid{{display:grid;gap:1px;background:#d7e4eb}}
.evidence-claim{{padding:16px;background:#fff}}.evidence-claim p{{margin:.45em 0}}
.evidence-claim-head{{display:flex;align-items:center;justify-content:space-between;gap:12px}}
.evidence-claim-head code{{font:700 11px ui-monospace,monospace;color:#164f74;
overflow-wrap:anywhere}}.evidence-claim-head span,.claim-use-status{{display:inline-block;
padding:3px 6px;border-radius:3px;background:#fff0c7;color:#674800;font:700 9px
ui-monospace,monospace;text-transform:uppercase}}.evidence-decision{{color:#164f74}}
.evidence-claim ul{{margin:10px 0;padding-left:20px}}.evidence-claim li{{margin:10px 0}}
.evidence-claim li span,.evidence-claim li small{{display:block;color:#526774;font-size:12px}}
.evidence-limit{{font-size:13px;color:#526774}}.claim-use-status{{margin:0 0 5px 6px;
background:#fde4e4;color:var(--red)}}.surface-black .evidence-trace{{border-color:#3c5666}}
.surface-black .evidence-trace>summary{{background:#173448;color:#bae7f9}}
#owos-concept-community{{padding:60px 0;background:#fff;border-top:1px solid var(--line)}}
.commercial-zone{{padding:64px 0;background:#f3efe8;border-top:1px solid #d6d0c5}}
.commercial-head{{display:grid;grid-template-columns:minmax(0,.8fr) minmax(280px,1.2fr);
gap:28px;align-items:end;margin-bottom:24px}}.commercial-head h2{{font-size:clamp(32px,5vw,58px);
line-height:1;margin:0;color:#211f1b}}.commercial-head>p{{margin:0;color:#565047;font-size:13px}}
.commercial-grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.commercial-card{{display:grid;grid-template-columns:170px minmax(0,1fr);gap:20px;position:relative;
padding:22px;border:1px solid #c8c0b4;background:#fff;color:#211f1b}}
.commercial-card.placeholder{{background:#211f1b;color:#f8f5ef;border-style:dashed}}
.commercial-label{{grid-column:1/-1;font:700 9px "Space Mono",monospace;letter-spacing:.12em;
text-transform:uppercase;color:#1d5c90}}.commercial-card.placeholder .commercial-label{{color:#ebca62}}
.commercial-logo-wrap{{display:grid;place-items:center;min-height:86px;background:#f8f5ef}}
.commercial-logo-wrap img{{display:block;width:100%;height:auto;max-height:86px;object-fit:contain}}
.commercial-copy h3{{margin:0 0 7px;font-size:20px;line-height:1.15}}
.commercial-copy p{{margin:0 0 14px;font-size:13px;line-height:1.5;color:#565047}}
.commercial-card.placeholder .commercial-copy p{{color:#c8c1b6}}
.commercial-action{{display:inline-flex;min-height:42px;align-items:center;color:#174f77;
font-weight:800;text-decoration:none}}.commercial-card.placeholder .commercial-action{{color:#aaa49a}}
.commercial-action:focus-visible{{outline:3px solid var(--gold);outline-offset:3px}}
.commercial-directory-note{{margin:18px 0 0;color:#565047;font-size:12px}}
.commercial-directory-note a{{color:#174f77;font-weight:800}}
.drawer-connection-grid{{display:grid;gap:10px;margin:20px 0}}.drawer-connection{{padding:14px;
border:1px solid #d7e4eb;background:#f7fbfd}}.drawer-connection span{{color:#1d5c90;
font:700 10px ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase}}
.drawer-connection h3{{margin:.35em 0;color:#10263b;font-size:18px}}.drawer-connection p{{
margin:.35em 0;color:#526774;font-size:14px}}.drawer-connection a{{color:#174f77;font-weight:800}}
footer{{padding:32px 0;background:#061f31;color:#bdd5e2;font-size:13px;overflow-wrap:anywhere}}
@media(max-width:760px){{.jar-layout{{grid-template-columns:1fr}}.jar-view{{width:min(100%,330px)}}}}
@media(max-width:760px){{.commercial-head,.commercial-grid{{grid-template-columns:1fr}}
.commercial-card{{grid-template-columns:130px minmax(0,1fr)}}}}
@media(max-width:840px){{.transfer-layout{{grid-template-columns:1fr}}}}
@media(max-width:640px){{header{{padding:50px 0}}.beat{{padding:46px 0}}.interaction{{padding:18px}}
.commercial-card{{grid-template-columns:1fr}}.commercial-logo-wrap{{max-width:220px}}
.jar-control{{width:calc(100% - 8px)}}.transfer-boundary-graphic{{grid-template-columns:1fr;
gap:14px}}.transfer-arrow{{text-align:left}}.transfer-ledger div{{grid-template-columns:1fr}}
.transfer-ledger dd{{text-align:left}}}}
@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important;animation:none!important;
transition:none!important}}}}
</style>
<style>{presentation_css}</style>
</head>
<body{body_theme_attr}>
<div class="status" role="status">{esc(status_text)}</div>
<header><div class="wrap"><div class="hero-copy"><div class="meta">{esc(public_config.get("hero_context", "OWOS CONCEPT BRIEF") if public_preview else "OWOS CONCEPT BRIEF")} ·
{esc(brief['brief_id'])}</div><h1>{hero_title}</h1><p>{esc(brief['promise'])}</p>
<div class="meta">{esc(scope_label)}</div>
</div><div class="hero-side"><div class="meta">{esc(public_config.get("hero_label", "WORKING BUILD") if public_preview else "WORKING BUILD")} · {esc(display_version)}</div>
<p>{esc(public_config.get("hero_summary", brief["promise"]) if public_preview else brief["promise"])}</p>
{"" if public_preview else f'<p class="meta">Verification coverage: {package["verification_coverage_percent"]}% · Pending material claims: {len(pending)}</p>'}<nav class="quick-nav" aria-label="Concept Brief">
{_render_public_navigation(public_config) if public_preview else '<a href="#beat-01-why">Start</a><a href="#block-jar">Live jar</a><a href="#block-terms">Key terms</a><a href="#block-evidence-boundary">Sources</a>'}
</nav></div></div></header>
<main>
{_render_public_orientation(package["learning"], public_config) if public_preview else ""}
{_render_public_takeaway(public_config) if public_preview else ""}
{''.join(beats_html)}
{_render_public_connections(package, public_config) if public_preview and (public_config.get("integration") or {}).get("enabled") is True else ""}
{_render_public_commercial(package, asset_prefix) if public_preview else ""}
{_render_public_finish(package, public_config) if public_preview else ""}
{"" if public_preview else f'''<section class="connected" id="owos-concept-graph"><div class="wrap"><h2>Connected in OWOS</h2>
<ul>{''.join(graph_links)}</ul></div></section>
<section id="owos-concept-community"><div class="wrap"><h2>Community conversation</h2>
<p>{esc(package['community']['discussion_boundary'])}</p>
<h3>Start with a bounded question</h3><ul>{community_questions}</ul>
<p><b>Correction path:</b> {esc(package['community']['correction_escalation'])}</p>
</div></section>'''}
</main>
<footer><div class="wrap">{esc(public_config.get("footer_notice", "")) if public_preview else f"Working preview generated by OWOS Concept Brief Compiler {COMPILER_VERSION}. Package {package['checksum']}. No publication, credential, operational, engineering, regulatory, safety, or health assurance claim."}</div></footer>
<script>
document.querySelectorAll('.jar-model').forEach(function(model){{
  var dataNode=model.querySelector('.jar-data');
  if(!dataNode)return;
  var data=JSON.parse(dataNode.textContent);
  var canvas=model.querySelector('.jar-canvas');
  var context=canvas&&canvas.getContext('2d');
  var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var particles=[];
  var width=0;
  var height=0;
  var animationFrame=0;
  function find(list,id){{return list.find(function(item){{return item.id===id}})||list[0]||{{}}}}
  function stageIndex(){{
    return Math.max(0,data.stages.findIndex(function(item){{return item.id===model.dataset.stage}}));
  }}
  function sizeCanvas(){{
    if(!canvas||!context)return;
    var ratio=window.devicePixelRatio||1;
    width=canvas.clientWidth;
    height=canvas.clientHeight;
    canvas.width=Math.max(1,Math.floor(width*ratio));
    canvas.height=Math.max(1,Math.floor(height*ratio));
    context.setTransform(ratio,0,0,ratio,0,0);
  }}
  function resetParticles(){{
    particles=[];
    for(var i=0;i<160;i++){{
      particles.push({{
        x:8+Math.random()*Math.max(1,width-16),
        y:8+Math.random()*Math.max(1,height-16),
        vx:(Math.random()-.5)*.9,
        vy:(Math.random()-.5)*.9,
        radius:1.7+Math.random()*1.3,
        mass:1,
        active:true
      }});
    }}
  }}
  function updateReadout(){{
    var index=stageIndex();
    var particle='DISPERSED';
    var aggregate='FINE';
    var next='COAGULATION';
    if(index===1){{
      particle=model.dataset.coagulant==='balanced'?'PREPARED FOR CONTACT':
        (model.dataset.coagulant==='low'?'MANY REMAIN DISPERSED':'POSSIBLE PERFORMANCE LOSS');
      aggregate='MICROFLOC';
      next='FLOCCULATION';
    }}else if(index===2){{
      particle='IN CONTACT';
      aggregate=model.dataset.flocculation==='balanced'?'GROWING':
        (model.dataset.flocculation==='low'?'SMALL':'BREAKING');
      next='SEPARATION';
    }}else if(index===3){{
      particle='UPSTREAM CONDITION SET';
      aggregate='MOVING TO SEPARATION';
      next='FILTRATION';
    }}
    model.querySelector('.readout-particle').textContent=particle;
    model.querySelector('.readout-aggregate').textContent=aggregate;
    model.querySelector('.readout-next').textContent=next;
  }}
  function update(){{
    var stage=find(data.stages,model.dataset.stage);
    var coagulant=find(data.coagulant,model.dataset.coagulant);
    var flocculation=find(data.flocculation,model.dataset.flocculation);
    model.querySelector('.jar-stage-result').textContent=(stage.label||'')+': '+(stage.explanation||'');
    model.querySelector('.jar-condition-result').textContent=
      'Coagulant condition: '+(coagulant.result||'')+' Flocculation energy: '+(flocculation.result||'');
    model.querySelector('.jar-question').textContent='Next evidence question: '+data.next_evidence_question;
    updateReadout();
    if(reduced)drawFrame(false);
  }}
  function drawFrame(advance){{
    if(!context)return;
    var index=stageIndex();
    var low=model.dataset.coagulant==='low';
    var excess=model.dataset.coagulant==='excess';
    var lowContact=model.dataset.flocculation==='low';
    var shear=model.dataset.flocculation==='excess'&&index===2;
    var repulsion=index===0 ? 1 : (low ? .82 : (excess ? .7 : 0));
    var attraction=index>=2&&!repulsion&&!shear;
    context.clearRect(0,0,width,height);
    var wash=context.createLinearGradient(0,0,0,height);
    wash.addColorStop(0,'rgba(18,55,79,.24)');
    wash.addColorStop(1,'rgba(4,18,28,.5)');
    context.fillStyle=wash;
    context.fillRect(0,0,width,height);
    if(advance){{
      for(var i=0;i<particles.length;i++){{
        var p=particles[i];
        if(!p.active)continue;
        if(index===1){{
          p.vx+=(Math.random()-.5)*.58;
          p.vy+=(Math.random()-.5)*.58;
        }}else if(index===2){{
          var energy=lowContact ? .04 : (shear ? .52 : .14);
          p.vx+=(Math.random()-.5)*energy;
          p.vy+=(Math.random()-.5)*energy;
        }}else if(index===3){{
          p.vy+=.038*p.mass;
          p.vx*=.94;
        }}else{{
          p.vx+=(Math.random()-.5)*.12;
          p.vy+=(Math.random()-.5)*.12;
        }}
        for(var j=i+1;j<particles.length;j++){{
          var q=particles[j];
          if(!q.active)continue;
          var dx=q.x-p.x;
          var dy=q.y-p.y;
          var distance=Math.sqrt(dx*dx+dy*dy)||1;
          if(distance<27&&repulsion){{
            var force=.15*repulsion/distance;
            p.vx-=dx*force;p.vy-=dy*force;q.vx+=dx*force;q.vy+=dy*force;
          }}else if(attraction&&distance<20&&!lowContact&&p.mass<12&&q.mass<12){{
            if(distance<9){{
              p.mass+=q.mass;
              p.radius=1.9*Math.sqrt(p.mass);
              q.active=false;
            }}else{{
              var pull=.035/distance;
              p.vx+=dx*pull;p.vy+=dy*pull;q.vx-=dx*pull;q.vy-=dy*pull;
            }}
          }}
        }}
        p.vx*=index===3 ? .97 : .94;
        p.vy*=index===3 ? .99 : .94;
        p.x+=p.vx;p.y+=p.vy;
        if(p.x<5){{p.x=5;p.vx*=-.65}}
        if(p.x>width-5){{p.x=width-5;p.vx*=-.65}}
        if(p.y<5){{p.y=5;p.vy*=-.65}}
        if(p.y>height-7){{p.y=height-7;p.vy*=-.35}}
      }}
    }}
    if(index===3){{
      context.fillStyle='rgba(235,202,98,.08)';
      context.fillRect(0,height-30,width,30);
    }}
    for(var k=0;k<particles.length;k++){{
      var point=particles[k];
      if(!point.active)continue;
      var color=(index===0||low)?'56,125,184':
        (excess&&index>0?'242,119,122':(shear?'255,174,145':(point.mass>2?'109,208,163':'235,202,98')));
      var radius=shear?Math.min(point.radius,3.2):point.radius;
      context.beginPath();
      context.arc(point.x,point.y,radius,0,Math.PI*2);
      context.fillStyle='rgba('+color+',.86)';
      context.fill();
      if(point.mass>2&&!shear){{
        context.strokeStyle='rgba('+color+',.35)';
        context.lineWidth=1;
        context.stroke();
      }}
    }}
  }}
  function animate(){{
    drawFrame(true);
    animationFrame=window.requestAnimationFrame(animate);
  }}
  model.querySelectorAll('[data-jar-control]').forEach(function(button){{
    button.addEventListener('click',function(){{
      var control=button.dataset.jarControl;
      var value=button.dataset.jarValue;
      model.dataset[control]=value;
      model.querySelectorAll('[data-jar-control="'+control+'"]').forEach(function(peer){{
        peer.setAttribute('aria-pressed',peer===button?'true':'false');
      }});
      resetParticles();
      update();
    }});
  }});
  sizeCanvas();
  resetParticles();
  window.addEventListener('resize',function(){{
    sizeCanvas();
    resetParticles();
    if(reduced)drawFrame(false);
  }});
  update();
  if(!reduced)animate();
}});
document.querySelectorAll('[data-concept-assessment="multiple-choice"]').forEach(function(check){{
  var button=check.querySelector('.assessment-check');
  if(!button)return;
  button.addEventListener('click',function(){{
    var selected=check.querySelector('input[type="radio"]:checked');
    var output=check.querySelector('.assessment-feedback');
    if(!selected){{
      output.textContent='Choose an answer before checking.';
      return;
    }}
    var correct=selected.dataset.correct==='true';
    var template=check.querySelector(correct?'[data-correct-feedback]':'[data-incorrect-feedback]');
    output.textContent=template?template.textContent:'';
    check.dataset.complete=correct?'true':'false';
  }});
}});
document.querySelectorAll('[data-concept-assessment="reflection"]').forEach(function(check){{
  var steps=[...check.querySelectorAll('[data-rehearsal-step]')];
  var stepIndex=0;
  var back=check.querySelector('.rehearsal-back');
  var next=check.querySelector('.rehearsal-next');
  var progress=check.querySelector('.rehearsal-progress');
  function showStep(){{
    steps.forEach(function(step,index){{step.hidden=index!==stepIndex;}});
    if(back)back.disabled=stepIndex===0;
    if(next){{
      next.disabled=stepIndex===steps.length-1;
      next.textContent=stepIndex===steps.length-1?'Example complete':
        (stepIndex===steps.length-2?'Show the better question':'Next step');
    }}
    if(progress)progress.textContent='Step '+(stepIndex+1)+' of '+steps.length;
  }}
  if(steps.length){{
    showStep();
    back?.addEventListener('click',function(){{if(stepIndex>0){{stepIndex-=1;showStep();}}}});
    next?.addEventListener('click',function(){{if(stepIndex<steps.length-1){{stepIndex+=1;showStep();}}}});
  }}
  var toggle=check.querySelector('.practice-toggle');
  var panel=check.querySelector('.practice-panel');
  toggle?.addEventListener('click',function(){{
    var opening=toggle.getAttribute('aria-expanded')!=='true';
    toggle.setAttribute('aria-expanded',opening?'true':'false');
    toggle.textContent=opening?'Close optional practice':'Try it yourself';
    if(panel)panel.hidden=!opening;
    if(opening)panel?.querySelector('textarea')?.focus();
  }});
  var button=check.querySelector('.assessment-reveal');
  if(!button)return;
  button.addEventListener('click',function(){{
    var response=check.querySelector('[data-reflection-response]');
    var model=check.querySelector('.assessment-model');
    var output=check.querySelector('.assessment-feedback');
    if(!response||response.value.trim().length<20){{
      output.textContent='Write a specific explanation before comparing responses.';
      return;
    }}
    model.hidden=false;
    output.textContent='Compare the two questions. Keep your observation, missing evidence, authority, monitoring, and rollback boundary visible.';
    if(check.dataset.optional!=='true')check.dataset.complete='true';
  }});
}});
document.querySelectorAll('[data-concept-assessment="multi-select"]').forEach(function(check){{
  check.querySelector('.assessment-check')?.addEventListener('click',function(){{
    var options=[...check.querySelectorAll('input[type="checkbox"]')];
    var correct=options.every(function(option){{
      return option.checked===(option.dataset.correct==='true');
    }});
    var template=check.querySelector(correct?'[data-correct-feedback]':'[data-incorrect-feedback]');
    check.querySelector('.assessment-feedback').textContent=template?template.textContent:'';
    check.dataset.complete=correct?'true':'false';
  }});
}});
document.querySelectorAll('[data-concept-assessment="flip-cards"]').forEach(function(check){{
  check.querySelectorAll('[data-flip-card]').forEach(function(card){{
    card.addEventListener('click',function(){{
      var open=card.getAttribute('aria-pressed')==='true';
      card.setAttribute('aria-pressed',open?'false':'true');
      card.textContent=open?card.dataset.front:card.dataset.back;
      var complete=[...check.querySelectorAll('[data-flip-card]')].every(function(item){{
        return item.getAttribute('aria-pressed')==='true';
      }});
      if(complete){{
        check.dataset.complete='true';
        var template=check.querySelector('[data-correct-feedback]');
        check.querySelector('.assessment-feedback').textContent=template?template.textContent:'';
      }}
    }});
  }});
}});
if(location.protocol!=='file:'){{
  window.addEventListener('load',function(){{
    ['/owos-shell.js','/concept-brief-runtime.js'].forEach(function(src){{
      if(document.querySelector('script[src="'+src+'"]'))return;
      var runtime=document.createElement('script');
      runtime.src=src;
      runtime.defer=true;
      document.body.appendChild(runtime);
    }});
  }},{{once:true}});
}}
document.querySelectorAll('[data-concept-assessment="matching"]').forEach(function(check){{
  check.querySelector('.assessment-check')?.addEventListener('click',function(){{
    var selects=[...check.querySelectorAll('select[data-answer]')];
    var correct=selects.every(function(select){{return select.value===select.dataset.answer}});
    var template=check.querySelector(correct?'[data-correct-feedback]':'[data-incorrect-feedback]');
    check.querySelector('.assessment-feedback').textContent=template?template.textContent:'';
    check.dataset.complete=correct?'true':'false';
  }});
}});
document.querySelectorAll('[data-concept-assessment="applied-work-product"]').forEach(function(check){{
  check.querySelector('.assessment-work-check')?.addEventListener('click',function(){{
    var fields=[...check.querySelectorAll('[data-required-field]')];
    var correct=fields.length>0&&fields.every(function(field){{return field.value.trim().length>0}});
    var template=check.querySelector(correct?'[data-correct-feedback]':'[data-incorrect-feedback]');
    check.querySelector('.assessment-feedback').textContent=template?template.textContent:'';
    check.dataset.complete=correct?'true':'false';
  }});
}});
var drawerHistoryActive=false;
var drawerReturnFocus=null;
document.querySelectorAll('[data-drawer-open]').forEach(function(button){{
  button.addEventListener('click',function(){{
    var drawer=document.getElementById(button.dataset.drawerOpen);
    var backdrop=document.querySelector('.drawer-backdrop');
    if(!drawer||!backdrop)return;
    drawerReturnFocus=button;
    document.querySelectorAll('.context-drawer').forEach(function(peer){{peer.hidden=true}});
    drawer.hidden=false;
    backdrop.hidden=false;
    document.body.classList.add('drawer-open');
    if(!drawerHistoryActive){{
      history.pushState(Object.assign({{}},history.state||{{}},{{owosConnectedDrawer:drawer.id}}),'',location.href);
      drawerHistoryActive=true;
    }}
    drawer.querySelector('.drawer-close').focus();
  }});
}});
function hideDrawers(){{
  var openDrawer=document.querySelector('.context-drawer:not([hidden])');
  var opener=drawerReturnFocus||(openDrawer&&document.querySelector('[data-drawer-open="'+openDrawer.id+'"]'));
  document.querySelectorAll('.context-drawer').forEach(function(drawer){{drawer.hidden=true}});
  var backdrop=document.querySelector('.drawer-backdrop');
  if(backdrop)backdrop.hidden=true;
  document.body.classList.remove('drawer-open');
  if(opener)opener.focus();
  drawerReturnFocus=null;
}}
function closeDrawers(fromHistory){{
  if(!fromHistory&&drawerHistoryActive){{
    history.back();
    return;
  }}
  drawerHistoryActive=false;
  hideDrawers();
}}
document.querySelectorAll('[data-drawer-close]').forEach(function(control){{
  control.addEventListener('click',function(){{closeDrawers(false)}});
}});
document.addEventListener('keydown',function(event){{
  if(event.key==='Escape')closeDrawers(false);
}});
window.addEventListener('popstate',function(){{
  if(drawerHistoryActive)closeDrawers(true);
}});
document.querySelectorAll('.context-drawer a[href^="#"]').forEach(function(link){{
  link.addEventListener('click',function(){{closeDrawers(false)}});
}});
var sopCopy=document.getElementById('copy-sop-outline');
if(sopCopy){{
  sopCopy.addEventListener('click',async function(){{
    var dataNode=document.getElementById('sop-outline-data');
    var status=document.getElementById('copy-sop-status');
    var outline=dataNode?JSON.parse(dataNode.textContent):'';
    status.textContent='Copying outline...';
    try{{
      if(navigator.clipboard&&navigator.clipboard.writeText){{
        await navigator.clipboard.writeText(outline);
      }}else{{
        var field=document.createElement('textarea');
        field.value=outline;
        field.setAttribute('readonly','');
        field.style.position='fixed';
        field.style.opacity='0';
        document.body.appendChild(field);
        field.select();
        document.execCommand('copy');
        field.remove();
      }}
      status.textContent='Outline copied. Paste it into your approved workspace.';
    }}catch(error){{
      status.textContent='Copy was blocked. Select the outline and copy it manually.';
    }}
  }});
}}
document.querySelectorAll('.commercial-card[data-placement-slot]').forEach(async function(card){{
  var slot=card.dataset.placementSlot;
  var fallbackId=card.dataset.placementId;
  var briefMeta=document.querySelector('meta[name="owos-brief-id"]');
  var contentId=briefMeta?briefMeta.content:'';
  function hit(id,ev){{
    if(!id||location.protocol==='file:')return;
    fetch('/api/ad/hit',{{method:'POST',headers:{{'content-type':'application/json'}},
      body:JSON.stringify({{id:id,ev:ev,surface:'concept-brief',content:contentId}}),
      keepalive:true}}).catch(function(){{}});
  }}
  if(location.protocol!=='file:'){{
    try{{
      var endpoint='/api/ad?slot='+encodeURIComponent(slot)+'&content='+encodeURIComponent(contentId);
      var response=await fetch(endpoint,{{cache:'no-store'}});
      var payload=response.ok?await response.json():{{ad:null}};
      var ad=payload.ad;
      if(ad&&ad.creative){{
        card.dataset.placementId=ad.id;
        card.querySelector('[data-placement-label]').textContent=ad.disclosureLabel||
          (slot==='concept-house'?'Built and powered by APAS':'Commercial connection');
        card.querySelector('[data-placement-headline]').textContent=ad.creative.headline||'';
        card.querySelector('[data-placement-body]').textContent=ad.creative.body||'';
        var logo=card.querySelector('[data-placement-logo]');
        if(ad.creative.image)logo.src=ad.creative.image;
        logo.alt=ad.sponsor||'Commercial placement';
        var link=card.querySelector('[data-placement-link]');
        if(link&&ad.creative.url){{link.href=ad.creative.url;link.textContent=ad.creative.cta||'Learn more'}}
        hit(ad.id,'imp');
      }}else if(slot==='concept-vendor'){{
        card.hidden=true;
      }}else{{
        hit(fallbackId,'imp');
      }}
    }}catch(error){{if(slot==='concept-vendor')card.hidden=true}}
  }}
  var action=card.querySelector('[data-placement-link]');
  if(action)action.addEventListener('click',function(){{hit(card.dataset.placementId,'click')}});
}});
if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver' in window){{
  document.documentElement.classList.add('motion-ready');
  var revealTargets=document.querySelectorAll(
    '.band-in,.block>p,.card,.sim,.stability-graphic,.editorial-table,'+
    '.protocol-step,.comparison,.audit-list li,.accuracy-panel,.connected li,'+
    '#owos-concept-community li'
  );
  revealTargets.forEach(function(element){{element.classList.add('editorial-reveal')}});
  var revealObserver=new IntersectionObserver(function(entries){{
    entries.forEach(function(entry){{
      if(entry.isIntersecting){{
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }}
    }});
  }},{{threshold:.08,rootMargin:'0px 0px -40px 0px'}});
  revealTargets.forEach(function(element){{revealObserver.observe(element)}});
}}
</script>
</body></html>
"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html_text, encoding="utf-8")
    output_checksum = hashlib.sha256(output.read_bytes()).hexdigest()
    return {
        "output": str(output),
        "output_checksum": output_checksum,
        "package_checksum": package["checksum"],
        "verification_coverage_percent": package["verification_coverage_percent"],
        "warnings": package["warnings"],
    }


def portfolio_check(root: Path) -> dict[str, Any]:
    records: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    errors: list[str] = []
    warnings: list[str] = []
    fields = (
        "opening_pattern",
        "narrative_archetype",
        "dominant_visual",
        "interaction_signature",
        "closing_action",
    )
    for path in sorted(root.rglob("brief.yaml")):
        data = load_yaml(path)
        brief = data.get("brief")
        design = data.get("design_fingerprint")
        if not isinstance(brief, dict) or not isinstance(design, dict):
            continue
        if brief.get("status") == "template":
            continue
        records.append((path.parent, brief, design))

    fingerprints: dict[tuple[str, ...], Path] = {}
    for package_dir, brief, design in records:
        fingerprint = tuple(str(design.get(field, "")) for field in fields)
        if fingerprint in fingerprints:
            errors.append(
                f"{package_dir}: full design fingerprint duplicates {fingerprints[fingerprint]}"
            )
        fingerprints[fingerprint] = package_dir

    for (left_dir, left_brief, left), (right_dir, right_brief, right) in zip(records, records[1:]):
        repeated = [field for field in fields if left.get(field) == right.get(field)]
        if len(repeated) >= 4:
            errors.append(
                f"adjacent briefs {left_brief.get('brief_id')} and {right_brief.get('brief_id')} "
                f"repeat {', '.join(repeated)}"
            )
        elif len(repeated) >= 2:
            warnings.append(
                f"adjacent briefs {left_brief.get('brief_id')} and {right_brief.get('brief_id')} "
                f"share {', '.join(repeated)}; confirm an instructional reason"
            )

    if errors:
        raise ConceptBriefError("\n".join(errors))
    return {
        "briefs_checked": len(records),
        "status": "passed",
        "warnings": warnings,
    }


def build_release_manifest(package_dir: Path, html_path: Path, output: Path) -> dict[str, Any]:
    package = validate_package(package_dir, release_ready=True)
    if not html_path.is_file():
        raise ConceptBriefError(f"compiled HTML does not exist: {html_path}")
    html_text = html_path.read_text(encoding="utf-8")
    expected_meta = f'name="owos-package-checksum" content="{package["checksum"]}"'
    if expected_meta not in html_text:
        raise ConceptBriefError("compiled HTML checksum does not match the release package")
    manifest = {
        "contract": "owos-concept-brief-release/1",
        "brief_id": package["brief"]["brief_id"],
        "brief_version": package["brief"]["version"],
        "compiler_version": COMPILER_VERSION,
        "package_contract": CONTRACT,
        "package_checksum": package["checksum"],
        "compiled_html": {
            "path": str(html_path),
            "sha256": hashlib.sha256(html_path.read_bytes()).hexdigest(),
        },
        "evidence_cutoff": package["brief"]["evidence_cutoff"],
        "verification_coverage_percent": package["verification_coverage_percent"],
        "release_build_timestamp": package["approvals"]["release_build_timestamp"],
        "graph_publication_approved": True,
        "community_connection_approved": True,
        "commercial_placement_approved": True,
        "release_approved": True,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate")
    validate.add_argument("package", type=Path)
    validate.add_argument("--release-ready", action="store_true")

    build = subparsers.add_parser("build")
    build.add_argument("package", type=Path)
    build.add_argument("--output", type=Path, required=True)
    build.add_argument(
        "--allow-pre-research-prototype",
        action="store_true",
        help="Explicitly compile an internal prototype that cannot be treated as cited HTML.",
    )
    build.add_argument(
        "--public-preview",
        action="store_true",
        help="Compile the governed clean public-review surface without internal evidence machinery.",
    )
    build.add_argument(
        "--public-config",
        type=Path,
        help="Use a governed alternate public-preview configuration, such as a brand treatment.",
    )

    portfolio = subparsers.add_parser("portfolio-check")
    portfolio.add_argument("root", type=Path)

    release = subparsers.add_parser("release-manifest")
    release.add_argument("package", type=Path)
    release.add_argument("--html", type=Path, required=True)
    release.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "validate":
            package = validate_package(args.package, release_ready=args.release_ready)
            print(
                json.dumps(
                    {
                        "status": "passed",
                        "brief_id": package["brief"]["brief_id"],
                        "package_checksum": package["checksum"],
                        "verification_coverage_percent": package[
                            "verification_coverage_percent"
                        ],
                        "release_ready": package["release_ready"],
                        "warnings": package["warnings"],
                    },
                    indent=2,
                )
            )
        elif args.command == "build":
            print(
                json.dumps(
                    build_html(
                        args.package,
                        args.output,
                        allow_pre_research_prototype=args.allow_pre_research_prototype,
                        public_preview=args.public_preview,
                        public_config_path=args.public_config,
                    ),
                    indent=2,
                )
            )
        elif args.command == "portfolio-check":
            print(json.dumps(portfolio_check(args.root), indent=2))
        elif args.command == "release-manifest":
            print(
                json.dumps(
                    build_release_manifest(args.package, args.html, args.output),
                    indent=2,
                )
            )
    except ConceptBriefError as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
