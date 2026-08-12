#!/usr/bin/env python3
"""Regression checks for the OWOS Concept Brief Compiler."""

from __future__ import annotations

import re
import shutil
import tempfile
from pathlib import Path

import yaml

from concept_brief_compiler import (
    ConceptBriefError,
    build_html,
    portfolio_check,
    validate_package,
)


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "concept-briefs/coagulation-vs-flocculation"
# The pilot has no matching check, so the matching guards use brief 003.
MATCHING_BRIEF = ROOT / "concept-briefs/detention-retention-and-infiltration"


package = validate_package(PILOT)
if package["brief"]["brief_id"] != "owos:concept-brief:001":
    raise AssertionError("pilot brief identifier did not resolve")
if package["verification_coverage_percent"] != 0.0:
    raise AssertionError("unverified pilot must report zero verification coverage")
if not package["warnings"]:
    raise AssertionError("working validation did not expose unresolved claims")

with tempfile.TemporaryDirectory() as directory:
    first = Path(directory) / "first.html"
    second = Path(directory) / "second.html"
    cited_html_allowed = bool(
        yaml.safe_load((PILOT / "research-plan.yaml").read_text(encoding="utf-8"))
        .get("cited_html", {})
        .get("allowed")
    )
    if cited_html_allowed:
        build_html(PILOT, first)
    else:
        try:
            build_html(PILOT, first)
        except ConceptBriefError as error:
            if "cited HTML generation is blocked" not in str(error):
                raise AssertionError("pre-research generation failed for the wrong reason") from error
        else:
            raise AssertionError("pre-research package generated cited HTML without an override")
    first_result = build_html(PILOT, first, allow_pre_research_prototype=True)
    second_result = build_html(PILOT, second, allow_pre_research_prototype=True)
    if first.read_bytes() != second.read_bytes():
        raise AssertionError("the same package did not compile deterministically")
    if first_result["package_checksum"] != second_result["package_checksum"]:
        raise AssertionError("deterministic builds reported different package checksums")
    text = first.read_text(encoding="utf-8")
    for phrase in (
        "Working preview",
        "Verification coverage: 0.0%",
        'id="owos-concept-community"',
        "Community discussion is practitioner conversation",
        "treatment-train-placeholder.svg",
        "prefers-reduced-motion",
    ):
        if phrase not in text:
            raise AssertionError(f"compiled pilot is missing: {phrase}")

    public_output = Path(directory) / "public-preview.html"
    build_html(
        PILOT,
        public_output,
        allow_pre_research_prototype=True,
        public_preview=True,
    )
    public_text = public_output.read_text(encoding="utf-8")
    for phrase in (
        "OWOS CONCEPT BRIEF",
        "Live jar",
        "Sources and scope",
        "From understanding to action",
        "IN 30 SECONDS",
        "What changed",
        "What to observe",
        "What not to assume",
        "COMMENT ON THIS BRIEF",
        "What worked for me",
        "data-concept-testimonials",
        "data-testimonial-consent",
        "WORKED DECISION REHEARSAL",
        "TEMPTING SHORTCUT",
        "THE BETTER QUESTION",
        "OPTIONAL PRACTICE",
        "Try it yourself",
        'data-optional="true"',
        'id="graph-drawer"',
        'data-drawer-open="graph-drawer"',
        "Open the full OWOS Graph",
        "history.pushState",
        "owosConnectedDrawer",
        "window.addEventListener('popstate'",
        "location.protocol!=='file:'",
        "'/concept-brief-runtime.js'",
        "This brief explains the concept. Facility decisions still require your approved procedures and qualified judgment.",
        "Educational concept brief",
        "Built and powered by APAS",
        'id="owos-commercial-placements"',
        '--owos-concept-shell-version: "graphite-reference-1"',
        "width: min(1160px, calc(100% - 80px))",
        "body[data-owos-theme=\"graphite\"] .community-public",
        "body[data-owos-theme=\"graphite\"] .concept-finish",
    ):
        if phrase not in public_text:
            raise AssertionError(f"public preview is missing: {phrase}")
    if (
        "GRAPHITE EDITION" not in public_text
        and "FINAL FEDERAL EDITION" not in public_text
        and "EDITION 1.0" not in public_text
    ):
        raise AssertionError("public preview is missing an approved edition label")
    for internal_phrase in (
        "Perplexity",
        "What the research changed",
        "Evidence and research decisions",
        "Verification coverage:",
        "Pending material claims:",
        'id="owos-concept-graph"',
        "Concept Brief Compiler",
        "source checked",
        "claim review pending",
        "Connected in the graph",
    ):
        if internal_phrase in public_text:
            raise AssertionError(
                f"public preview exposed internal production language: {internal_phrase}"
            )
    if "Paid vendor placement" in public_text or "Vendor placeholder" in public_text:
        raise AssertionError("inactive vendor placeholders must not appear in public output")
    if "../visuals/" in public_text:
        raise AssertionError("public output contains a route-dependent Concept Brief asset path")
    if public_text.count("data:image/svg+xml;base64,") < 3:
        raise AssertionError("public output did not embed its instructional and publisher SVG assets")
    if "without turning public instruction into facility authority" in public_text:
        raise AssertionError("public preview retained the cryptic transfer instruction")
    if public_text.index('id="owos-commercial-placements"') > public_text.index(
        'id="owos-concept-finish"'
    ):
        raise AssertionError("the compact comment and recap must follow commercial content")
    nav = public_text.split('<nav class="quick-nav"', 1)[1].split("</nav>", 1)[0]
    if nav.count("<a ") + nav.count("<button ") != 4:
        raise AssertionError("public primary navigation must contain exactly four controls")

    default_shell_fixture = Path(directory) / "default-shell-brief"
    shutil.copytree(PILOT, default_shell_fixture)
    default_shell_config_path = default_shell_fixture / "public-preview.yaml"
    default_shell_config = yaml.safe_load(
        default_shell_config_path.read_text(encoding="utf-8")
    )
    default_shell_config.pop("brand_css", None)
    default_shell_config_path.write_text(
        yaml.safe_dump(default_shell_config, sort_keys=False),
        encoding="utf-8",
    )
    default_shell_output = Path(directory) / "default-shell.html"
    build_html(
        default_shell_fixture,
        default_shell_output,
        allow_pre_research_prototype=True,
        public_preview=True,
    )
    default_shell_text = default_shell_output.read_text(encoding="utf-8")
    if '--owos-concept-shell-version: "graphite-reference-1"' not in default_shell_text:
        raise AssertionError(
            "a public brief without package brand CSS did not inherit the shared Graphite shell"
        )

try:
    validate_package(PILOT, release_ready=True)
except ConceptBriefError as error:
    message = str(error)
    for phrase in (
        "release requires 100 percent material-claim verification coverage",
        "qualified technical review",
        "owner_release must be completed",
        "approval release must be approved",
        "release requires approved privacy review",
        "assessment governance: release requires approved review",
    ):
        if phrase not in message:
            raise AssertionError(f"release gate did not expose: {phrase}") from error
else:
    raise AssertionError("the unverified pilot passed the release gate")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    commercial_path = fixture / "commercial.yaml"
    commercial = yaml.safe_load(commercial_path.read_text(encoding="utf-8"))
    commercial["relationships"] = [
        {
            "organization_node": "org:test-sponsor",
            "relationship_type": "sponsor",
            "disclosure": "Paid placement",
            "editorial_rights": "approve_claims",
        }
    ]
    commercial_path.write_text(
        yaml.safe_dump(commercial, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        if "editorial_rights must be none" not in str(error):
            raise AssertionError("commercial firewall failed for the wrong reason") from error
    else:
        raise AssertionError("a sponsor with claim approval rights passed validation")

with tempfile.TemporaryDirectory() as directory:
    portfolio_root = Path(directory) / "briefs"
    shutil.copytree(PILOT, portfolio_root / "001")
    shutil.copytree(PILOT, portfolio_root / "002")
    second_brief_path = portfolio_root / "002/brief.yaml"
    second_brief = yaml.safe_load(second_brief_path.read_text(encoding="utf-8"))
    second_brief["brief"]["brief_id"] = "owos:concept-brief:002"
    second_brief_path.write_text(
        yaml.safe_dump(second_brief, sort_keys=False),
        encoding="utf-8",
    )
    try:
        portfolio_check(portfolio_root)
    except ConceptBriefError as error:
        if "full design fingerprint duplicates" not in str(error):
            raise AssertionError("duplicate design failed for the wrong reason") from error
    else:
        raise AssertionError("a duplicate Concept Brief design fingerprint passed")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    sources_path = fixture / "sources.yaml"
    sources = yaml.safe_load(sources_path.read_text(encoding="utf-8"))
    for source in sources["sources"]:
        if source["source_id"] == "source-epa-lt1":
            source["country"] = "Canada"
            break
    sources_path.write_text(
        yaml.safe_dump(sources, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        if "governing authority must be from the United States" not in str(error):
            raise AssertionError("United States authority guard failed for the wrong reason") from error
    else:
        raise AssertionError("a non-United States governing source passed validation")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    learning_path = fixture / "learning.yaml"
    learning = yaml.safe_load(learning_path.read_text(encoding="utf-8"))
    learning["learning_events"]["facility_sensitive_data_collection"] = "allowed"
    learning["capability_lock"]["required_capability_ids"].remove("reflection")
    learning_path.write_text(
        yaml.safe_dump(learning, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        for phrase in (
            "facility_sensitive_data_collection must be prohibited",
            "learning capability lock is missing used capabilities: reflection",
        ):
            if phrase not in str(error):
                raise AssertionError(
                    f"durable learning-record guard did not expose: {phrase}"
                ) from error
    else:
        raise AssertionError("an unsafe or incomplete learning-record contract passed")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    learning_path = fixture / "learning.yaml"
    learning = yaml.safe_load(learning_path.read_text(encoding="utf-8"))
    learning["learner_experience"].pop("orientation", None)
    learning_path.write_text(
        yaml.safe_dump(learning, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        if "missing orientation" not in str(error):
            raise AssertionError(
                "the instructional orientation gate failed for the wrong reason"
            ) from error
    else:
        raise AssertionError("a brief without a learner orientation passed validation")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    narrative_path = fixture / "narrative.yaml"
    narrative = yaml.safe_load(narrative_path.read_text(encoding="utf-8"))
    narrative["blocks"] = [
        block for block in narrative["blocks"] if block.get("type") != "definition"
    ]
    narrative_path.write_text(
        yaml.safe_dump(narrative, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        if "requires at least one definition block" not in str(error):
            raise AssertionError(
                "the define-before-use gate failed for the wrong reason"
            ) from error
    else:
        raise AssertionError("a brief that defines no terms passed validation")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    narrative_path = fixture / "narrative.yaml"
    narrative = yaml.safe_load(narrative_path.read_text(encoding="utf-8"))
    narrative["blocks"] = [
        block for block in narrative["blocks"] if block.get("type") != "example"
    ]
    narrative_path.write_text(
        yaml.safe_dump(narrative, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        if "requires at least one worked example" not in str(error):
            raise AssertionError(
                "the worked-example gate failed for the wrong reason"
            ) from error
    else:
        raise AssertionError("a brief with no worked example passed validation")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    storyboard_path = fixture / "storyboard.yaml"
    storyboard = yaml.safe_load(storyboard_path.read_text(encoding="utf-8"))
    definition_ids = {
        block["block_id"]
        for block in yaml.safe_load(
            (fixture / "narrative.yaml").read_text(encoding="utf-8")
        )["blocks"]
        if block.get("type") == "definition"
    }
    moved: list[str] = []
    for beat in storyboard["beats"]:
        remaining = [
            block_id
            for block_id in beat.get("block_ids") or []
            if block_id not in definition_ids
        ]
        moved.extend(
            block_id
            for block_id in beat.get("block_ids") or []
            if block_id in definition_ids
        )
        beat["block_ids"] = remaining
    storyboard["beats"][-1]["block_ids"] = list(
        storyboard["beats"][-1]["block_ids"]
    ) + moved
    storyboard_path.write_text(
        yaml.safe_dump(storyboard, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        if "definitions must be placed before the first visual" not in str(error):
            raise AssertionError(
                "the definition-ordering gate failed for the wrong reason"
            ) from error
    else:
        raise AssertionError("a brief that defines its terms after using them passed")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(MATCHING_BRIEF, fixture)
    assessments_path = fixture / "assessments.yaml"
    assessments = yaml.safe_load(assessments_path.read_text(encoding="utf-8"))
    for item in assessments["assessments"]:
        if item.get("type") == "matching":
            item["pairs"][0].pop("left", None)
            item["pairs"][0].pop("prompt", None)
            item["pairs"][1]["right"] = "not a declared target"
            break
    else:
        raise AssertionError("brief 003 no longer contains a matching assessment")
    assessments_path.write_text(
        yaml.safe_dump(assessments, sort_keys=False),
        encoding="utf-8",
    )
    try:
        validate_package(fixture)
    except ConceptBriefError as error:
        for phrase in (
            "needs a visible statement in left or prompt",
            "is not one of the declared targets",
        ):
            if phrase not in str(error):
                raise AssertionError(
                    f"matching pair integrity guard did not expose: {phrase}"
                ) from error
    else:
        raise AssertionError("a matching check with a blank row and a bad answer passed")

with tempfile.TemporaryDirectory() as directory:
    # A matching check must reach the page with a visible statement and a real
    # graded answer. Authoring uses left/right; the renderer previously read
    # prompt/answer and silently emitted blank rows that graded against "".
    output = Path(directory) / "matching.html"
    build_html(
        MATCHING_BRIEF, output, allow_pre_research_prototype=True, public_preview=True
    )
    rendered = output.read_text(encoding="utf-8")
    rows = re.findall(
        r'<label class="assessment-match-row"><span>(.*?)</span>'
        r'<select data-answer="(.*?)"',
        rendered,
    )
    if not rows:
        raise AssertionError("no matching rows were rendered")
    for prompt_text, answer_text in rows:
        if not prompt_text.strip():
            raise AssertionError("a matching row rendered without a visible statement")
        if not answer_text.strip():
            raise AssertionError("a matching row rendered without a graded answer")

with tempfile.TemporaryDirectory() as directory:
    fixture = Path(directory) / "brief"
    shutil.copytree(PILOT, fixture)
    (fixture / "white-paper.md").write_text("# placeholder\n", encoding="utf-8")
    result = validate_package(fixture)
    if any("missing white-paper.md" in warning for warning in result["warnings"]):
        raise AssertionError("a package with a white paper still warned about it")
    (fixture / "white-paper.md").unlink()
    result = validate_package(fixture)
    if not any("missing white-paper.md" in warning for warning in result["warnings"]):
        raise AssertionError("a package without a white paper did not warn")

print(
    "OWOS Concept Brief Compiler QA passed: deterministic working builds, complete verification "
    "coverage, qualified review, United States authority scope, commercial firewall, Community "
    "mount, durable learning records, instructional orientation, define-before-use, worked "
    "examples, matching-check integrity, and portfolio uniqueness are fail-closed."
)
