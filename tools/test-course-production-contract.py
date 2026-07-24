#!/usr/bin/env python3
"""Mechanical checks for the binding OWOS Course Production Contract."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "core/standards/COURSE-PRODUCTION-CONTRACT.md"
OPERATING = ROOT / "core/standards/COURSE-OPERATING-STANDARD.md"
DESIGN = ROOT / "core/standards/COURSE-DESIGN-SYSTEM.md"
SKILL = ROOT / ".codex/skills/continue-owos-course/SKILL.md"
CREATOR = ROOT / "tools/create-course.py"
CONFORMANCE = ROOT / "tools/course_conformance.py"
FULL_CONFORMANCE = ROOT / "tools/course_full_conformance.py"
DISTINCTIVENESS = ROOT / "tools/course_distinctiveness.py"
RELEASE_BUILDER = ROOT / "tools/build-course-release.py"
COURSE_COMPILER = ROOT / "tools/course_compiler.py"
AUTHORING_AUDIT = ROOT / "tools/audit-structured-authoring.py"
AUTHOR_STUDIO = ROOT / "tools/course_author_studio.py"
ALL_EXPERIENCES = ROOT / "tools/test-all-course-experiences.py"
COURSE_TEMPLATE = ROOT / "apps/_course-template/course.yaml"
BRIEF = ROOT / "core/templates/MODULE-DESIGN-BRIEF.md"
QA = ROOT / "core/templates/MODULE-QA-REPORT.md"


def require(path: Path, phrases: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path} is missing: {phrase}")
    if "—" in text or "–" in text:
        raise AssertionError(f"prohibited dash found in {path}")


require(
    CONTRACT,
    [
        "Syllabus and blueprint gate",
        "Complete lesson experience",
        "Instructor voice and explanation",
        "Graphics, interaction, and pacing",
        "Course navigation and connected learning",
        "compact Graph, Community, and Start actions",
        "white, right-side drawers",
        "complete graph and community section at the bottom",
        "#owos-course-community",
        "module-specific FAQ",
        "dark surface is a release blocker",
        "Deterministic learning and records",
        "Quality assurance and release",
        "Definition of done",
        "course-level distinctiveness gate",
        "Course Experience Brief",
        "Course Compiler and Author Studio contract",
        "Visual truth gate",
        "Storyboard approval gate",
        "Cognitive quality gate",
        "Rendered experience gate",
        "Course coherence gate",
        "Portability, analytics, localization, and lifecycle",
        "owos-course-compiler/1",
        "legacy modules remaining",
    ],
)
require(OPERATING, ["COURSE-PRODUCTION-CONTRACT.md"])
require(DESIGN, ["COURSE-PRODUCTION-CONTRACT.md"])
require(SKILL, ["COURSE-PRODUCTION-CONTRACT.md", "floating cards or hanging rails", "module-specific FAQ", "contrast guard", "course_distinctiveness.py", "course_compiler.py", "visual manifest", "Author Studio"])
require(CREATOR, ["Course Production Contract", "#owos-course-community", "Graph, Community, and Start", "Floating cards and hanging rails are prohibited", "module-specific FAQ", "course_conformance.py", "full-module-contract.json", "experience-architecture.json", "structured_modules_with_compiled_html", "authoring.json"])
require(COURSE_COMPILER, ["visual manifest", "storyboard", "rendered_review_status", "release_ready", "package_checksum"])
require(
    AUTHORING_AUDIT,
    [
        "owos-course-compiler/1",
        "legacy_pending_migration",
        "hybrid_migration",
        "fully_structured",
        "compiled checksum does not match source package",
    ],
)
require(AUTHOR_STUDIO, ["preserves snapshots", "validate_package", "build_module", ".history"])
require(CONFORMANCE, ["minimum_visual_types", "minimum_quiz_types", "minimum_conversational_teaching_words", "minimum_worked_examples", "data-final-applied-check", "required_community_features", "approved_quiz_sources", "visual_catalog_terms", "validate_qa_report"])
require(
    FULL_CONFORMANCE,
    [
        "experience-architecture.json",
        "full_module_conformance",
        "module design brief",
        "scored QA report",
        "script_policy",
        "release_status: approved",
        "release-ready QA hard gate",
        "validate_module",
    ],
)
require(DISTINCTIVENESS, ["factory-pattern", "adjacent structural similarity", "signature mechanism"])
release_builder_text = RELEASE_BUILDER.read_text(encoding="utf-8")
for phrase in (
    "course_distinctiveness_required",
    "course distinctiveness gate failed before release",
    "full_module_conformance_required",
    "whole-course full-module conformance gate failed before release",
    "structured authoring gate failed before release",
    "structured_modules_validated",
):
    if phrase not in release_builder_text:
        raise AssertionError(f"{RELEASE_BUILDER} is missing: {phrase}")
require(ALL_EXPERIENCES, ["course_distinctiveness_required", "governed OWOS course experience audits"])
require(
    COURSE_TEMPLATE,
    [
        "version: 3",
        "course_distinctiveness_required: true",
        "full_module_conformance_required: true",
    ],
)
require(
    ROOT / "apps/_course-template/.course/experience-architecture.json",
    ["full_module_conformance", "module-01-example.html", "evidence"],
)
require(
    ROOT / "apps/_course-template/.course/full-module-contract.json",
    ["minimum_visual_types", "approved_component_sources"],
)
require(ROOT / "tools/course_quality.py", ["data-purposeful-interaction", "purposeful:"])
require(BRIEF, ["Header Graph, Community, and Start actions", "#owos-course-community", "Learner FAQ plan", "Dark-surface contrast plan", "Storyboard approval", "Cognitive design", "Rendered evidence plan"])
require(QA, ["Header Graph, Community, and Start actions", "Explicit bottom connected-learning anchor", "Module-specific FAQ coverage", "Dark-surface contrast guard"])

print("OWOS Course Production Contract QA passed.")
