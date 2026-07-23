#!/usr/bin/env python3
"""Create or adopt a governed OWOS course workspace."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "apps"
SOURCE_EXTENSIONS = {
    ".csv", ".doc", ".docx", ".jpeg", ".jpg", ".m4a", ".md", ".mp3", ".mp4",
    ".pdf", ".png", ".ppt", ".pptx", ".txt", ".wav", ".webp", ".xls", ".xlsx",
}
CONTROL_FILES = {
    "AGENTS.md", "APPROVALS.md", "COURSE-BRIEF.md", "README.md", "STATE.md",
    "SYLLABUS.md", "course.yaml",
}


def stable_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug or slug != value:
        raise ValueError("Slug must contain only lowercase letters, numbers, and hyphens.")
    return slug


def write_once(path: Path, content: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.rstrip() + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def course_yaml(args: argparse.Namespace) -> str:
    return f"""schema_version: 1
course_id: {args.course_id}
slug: {args.slug}
title: "{args.title}"
course_family: focused_course
source_format: native_html
status: research
visibility: private_preview
course_version: 0.1.0
release_date: null
content_owner: "{args.owner}"
organization: One Water Operating System
platform: APAS.ai

quality_contract:
  version: 1
  enforce_on_release: true
  minimum_purposeful_interactions: 2

provenance:
  repository: hpad66-pixel/owos-learning-content
  ref: main
  content_baseline_commit: pending
  content_baseline_reason: Initial governed research workspace

structure:
  parts: 0
  chapters: 0
  sections: 0
  capstone: not_decided
  chapter_range: pending

primary_roles:
  - utility-manager
  - data-leader
  - emerging-leader

assessment:
  chapter_checks: pending
  final_assessment: not_configured
  deterministic_scoring: required_before_release

credential:
  status: not_configured
  name: pending
  type: course_completion
  certification_claim: false

source_files:
  syllabus: SYLLABUS.md
  source_register: research/SOURCE-REGISTER.md
  claims_register: research/CLAIMS-REGISTER.md
  evidence_boundaries: research/EVIDENCE-BOUNDARIES.md
  architecture: ../../docs/OWOS-COURSE-TO-LEARN-ARCHITECTURE.md

delivery:
  release_state: research
  available_chapters: 0
  released_chapters: []
  landing_output: dist/site/course-{args.slug}.html
  runtime_manifest: dist/release-manifest.json
  chapter_output_pattern: dist/site/lesson-{args.slug}-{{chapter}}-{{lesson}}.html
  runtime_repository: hpad66-pixel/onewater-os-platform
  runtime_path: site
  runtime_store_key: {args.runtime_key}
  runtime_canonical: /course-{args.slug}
  learner_records: supabase
  semantic_alignment: owos_knowledge_graph
  edge_delivery: cloudflare_pages_and_worker
  completion_events_enabled: false
"""


def scaffold(args: argparse.Namespace) -> Path:
    stable_slug(args.slug)
    course_dir = APPS / args.slug
    if course_dir.exists() and not args.adopt:
        raise FileExistsError(f"{course_dir} already exists. Use --adopt to scaffold it safely.")
    course_dir.mkdir(parents=True, exist_ok=True)

    for relative in [
        ".course",
        "inbox",
        "conversations",
        "research/originals",
        "research/annotations",
        "author-input/approved-transcripts",
        "curriculum",
        "curriculum/design-briefs",
        "assessments",
        "assets",
        "work-products",
        "release",
    ]:
        (course_dir / relative).mkdir(parents=True, exist_ok=True)

    for source in list(course_dir.iterdir()):
        if (
            source.is_file()
            and source.name not in CONTROL_FILES
            and source.suffix.lower() in SOURCE_EXTENSIONS
        ):
            destination = course_dir / "research" / "originals" / source.name
            if source != destination and not destination.exists():
                shutil.move(str(source), str(destination))

    write_once(
        course_dir / "AGENTS.md",
        f"""# {args.title} Course Instructions

Use `$continue-owos-course` for every material task in this folder.

The user adds documents to `inbox/` or speaks and types directly into the Codex task. Preserve substantive direction in `conversations/`. Run internal inventory, extraction, research, course generation, validation, and release tools yourself. Never ask the user to operate Python scripts.

Before drafting, read `COURSE-BRIEF.md`, `STATE.md`, `APPROVALS.md`, `course.yaml`, `SYLLABUS.md`, Hardeep Soul, the Course Production Contract, Course Operating Standard, Course Design System, Visual Arsenal, component catalog, quiz catalog, and writing standard. Preserve originals, distinguish evidence from Hardeep's positions, and require approval before locking the blueprint, golden lesson, or release.

Create a module design brief before each lesson and maintain the course design matrix. Chapter 09 is a capability benchmark, not a page template. Every module must select its visual, interaction, quiz, animation, and work-product mix from the learning problem and must be checked against adjacent modules for repetition.

Use compact Graph and Community buttons in the lesson header. Each opens a white responsive drawer. Reserve an explicit `#owos-course-community` anchor inside `main`, immediately before bottom navigation, for the complete connected-learning section. Floating cards and hanging rails are prohibited. Dark blue, navy, and gradient surfaces always use tested light text.

End every module with a module-specific FAQ before the evidence boundary and bottom connected-learning section. Anticipate novice questions, answer them directly in plain English, use a utility example, and add a diagram, comparison, or worked sequence when it improves understanding.
""",
    )
    write_once(
        course_dir / "COURSE-BRIEF.md",
        f"""# Course Brief

## Working title

{args.title}

## Course promise

Pending research and owner approval.

## Utility connection

Pending Hardeep Anand's spoken or written direction.

## Current boundary

Research material remains private until permissions, claims, and release decisions are approved.
""",
    )
    write_once(
        course_dir / "STATE.md",
        f"""# Course State

Updated: {date.today().isoformat()}

## Current phase

Research intake

## Completed

- Created the governed course workspace.
- Connected the course to Hardeep Soul and the OWOS course standards.
- Enabled conversational intake and persistent source change tracking.

## Next action

Add research to `inbox/`, dictate or type the course direction, and say, “Continue this course.”
""",
    )
    write_once(
        course_dir / "APPROVALS.md",
        """# Course Approvals

| Decision | Status | Date | Evidence or note |
| --- | --- | --- | --- |
| Research boundary | pending | | |
| Curriculum blueprint | pending | | |
| Golden lesson | pending | | |
| Graph publication | pending | | |
| Credential claim | pending | | |
| Course release | pending | | |
""",
    )
    write_once(
        course_dir / "README.md",
        f"""# {args.title}

This is the governed course workspace for `{args.course_id}`.

## Current state

The course is in research. No lesson, assessment, credential, or completion claim is released.

## Operating path

1. Preserve original sources in `research/originals/`.
2. Record sources, claims, permissions, limitations, and Hardeep's approved input.
3. Approve `SYLLABUS.md` before producing lessons.
4. Build and approve one golden lesson.
5. Run the Course Quality Contract before every release.
6. Publish only through a reviewed GitHub release and OWOS platform intake.
""",
    )
    write_once(course_dir / "course.yaml", course_yaml(args))
    write_once(
        course_dir / "SYLLABUS.md",
        f"""# {args.title}

## Course promise

Pending research and owner approval.

## Intended learners

- Utility managers
- Data and technology leaders
- Emerging utility leaders

## Learning outcomes

Pending research, evidence review, and Hardeep Anand's direction.

## Proposed curriculum

The curriculum will be approved only after the research pack, claims register, utility examples, and evidence boundaries are complete.
""",
    )
    write_once(
        course_dir / "research" / "CLAIMS-REGISTER.md",
        """# Claims Register

| Claim ID | Proposed claim | Source locator | Status | Limitations | Reviewer |
| --- | --- | --- | --- | --- | --- |

Statuses: proposed, verified, supported with limitation, expert interpretation, Hardeep Anand position, unresolved, rejected.
""",
    )
    write_once(
        course_dir / "research" / "EVIDENCE-BOUNDARIES.md",
        """# Evidence Boundaries

## What the evidence supports

Pending source review.

## What the evidence does not support

Pending source review.

## Licensing and permitted use

Pending owner confirmation.
""",
    )
    write_once(
        course_dir / "author-input" / "HARDEEP-DIRECTION.md",
        """# Hardeep's Direction

Use this file for approved course intent, utility examples, personal positions, stories, teaching instructions, and questions requiring further research.

Nothing in this file becomes public or enters the shared graph without explicit approval.
""",
    )

    source_rows = []
    for index, source in enumerate(sorted((course_dir / "research" / "originals").iterdir()), start=1):
        if source.is_file():
            source_rows.append(
                f"| SRC-{index:03d} | {source.name} | {source.stat().st_size} | `{sha256(source)}` | private research | pending |"
            )
    source_table = "\n".join(source_rows) or "| SRC-001 | Pending | 0 | pending | private research | pending |"
    write_once(
        course_dir / "research" / "SOURCE-REGISTER.md",
        f"""# Source Register

Generated {date.today().isoformat()}.

| Source ID | Original file | Bytes | SHA-256 | Visibility | Permission status |
| --- | --- | ---: | --- | --- | --- |
{source_table}

The original file is preserved. Extraction, citation coverage, licensing, and factual review remain pending.
""",
    )
    write_once(course_dir / "research" / "annotations" / "README.md", "# Annotations\n\nStore page-addressable research notes and approved annotations here.")
    write_once(
        course_dir / "inbox" / "README.md",
        "# Course Inbox\n\nAdd new PDFs, Word files, notes, images, spreadsheets, or audio here. Codex preserves originals and records changes when the course continues.\n",
    )
    write_once(
        course_dir / "conversations" / "README.md",
        "# Course Conversations\n\nCodex records substantive spoken and typed course direction here so chat is never the only memory.\n",
    )
    write_once(course_dir / "author-input" / "approved-transcripts" / "README.md", "# Approved Transcripts\n\nOnly transcripts approved for course use belong here.")
    write_once(course_dir / "curriculum" / "README.md", "# Curriculum\n\nLessons begin only after the syllabus and golden lesson plan are approved.")
    write_once(
        course_dir / "curriculum" / "COURSE-DESIGN-MATRIX.md",
        "# Course Design Matrix\n\nCopy the structure from `core/templates/COURSE-DESIGN-MATRIX.md` and update it before module production.\n",
    )
    write_once(
        course_dir / "curriculum" / "design-briefs" / "README.md",
        "# Module Design Briefs\n\nCreate one brief per module from `core/templates/MODULE-DESIGN-BRIEF.md` before writing lesson HTML.\n",
    )
    write_once(course_dir / "assessments" / "README.md", "# Assessments\n\nDeterministic assessments and scoring contracts will be stored here.")
    write_once(course_dir / "assets" / "README.md", "# Assets\n\nStore governed course graphics and small reproducible assets here.")
    write_once(course_dir / "work-products" / "README.md", "# Work Products\n\nTemplates and applied learner deliverables will be stored here.")
    write_once(course_dir / "release" / "README.md", "# Release\n\nRelease evidence is generated only after the quality contract passes.")
    return course_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--course-id", required=True)
    parser.add_argument("--runtime-key", required=True)
    parser.add_argument("--owner", default="Hardeep Anand")
    parser.add_argument("--adopt", action="store_true", help="Scaffold an existing folder without overwriting files.")
    return parser.parse_args()


if __name__ == "__main__":
    options = parse_args()
    created = scaffold(options)
    print(f"Course workspace ready: {created}")
