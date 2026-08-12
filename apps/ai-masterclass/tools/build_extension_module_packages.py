#!/usr/bin/env python3
"""Build governed Markdown packages for optional One Water AI extensions."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "curriculum" / "extension-programs.json"
OUTPUT = ROOT / "curriculum" / "extensions"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def bullets(values: list[str]) -> str:
    return "\n".join(f"- {value}" for value in values)


def numbered(values: list[str]) -> str:
    return "\n".join(f"{index}. {value}" for index, value in enumerate(values, 1))


def blueprint(program: dict, module: dict) -> str:
    lessons = []
    for index, topic in enumerate(module["topics"], 1):
        objective = module["outcomes"][(index - 1) % len(module["outcomes"])]
        lessons.append(
            f"| {index} | {topic.capitalize()} | {objective} | "
            "explanation, worked water-sector example, boundary or failure case, and evidence check |"
        )
    return f"""# {module['code']}: {module['title']}

## Governance record

- Program: {program['title']}
- Curriculum line: optional extension
- Blueprint status: accepted curriculum blueprint
- Guided effort: {module['guidedHours']} hours
- Source audit records: {', '.join(module['sourceAuditIds'])}
- Authority boundary: this blueprint does not authorize public release, credential issuance, or operational action.

## Learning job

{module['learningJob']}

## Why this belongs in One Water AI

This module translates a technical capability into water, wastewater, and stormwater judgment. The
learner must connect the mechanism to records, roles, permissions, consequences, evidence, failure,
and human authority. A generic technology demonstration does not meet the module standard.

## Entry evidence

{bullets(module['prerequisites'])}

## Observable learning objectives

{numbered(module['outcomes'])}

## Lesson sequence

| Lesson | Focus | Objective connection | Required teaching pattern |
| ---: | --- | --- | --- |
{chr(10).join(lessons)}

## Required One Water contexts

Research and instruction must use at least three distinct contexts selected from drinking-water
operations, wastewater operations, stormwater management, laboratory or compliance work,
maintenance and asset management, engineering and capital delivery, customer service, finance and
procurement, emergency response, and public communication. At least one context must expose a
consequential failure or authority boundary.

## Applied result

**{module['appliedResult']}**

The artifact must preserve the learner, date, problem, source boundary, assumptions, tool or method,
ordinary case, boundary case, failure case, correction, reviewer, and disposition.

## Assessment evidence

{bullets(module['assessments'])}

The module is complete only when the learner can explain the artifact, respond to a challenge,
correct a weak element, and state what remains unknown or unauthorized.

## Visual and interaction directions

{bullets(module['visuals'])}

Every visual must teach a relationship, sequence, comparison, or boundary. It requires a text
alternative and may not depend on color alone. Any drag interaction requires a keyboard-equivalent
route.

## Evidence and safety boundary

- Use current United States primary authorities for law, regulation, public standards, and public
  operational guidance when applicable.
- Preserve source title, issuing body, date or version, locator, accessed date, and limitation.
- Label instructional scenarios and synthetic data clearly.
- Do not invent utility statistics, incidents, vendor performance, legal duties, or regulatory
  requirements.
- Do not connect to operational systems or use protected records without written local authority.
- Treat model output as material to test, not as an authority.

## Production acceptance rules

- All objectives map to instruction and assessment.
- The module contains an authentic utility problem, at least one failure, and a correction.
- Claims have approved sources and locators.
- The work product can be reviewed without the author's verbal explanation.
- Accessibility, technical, domain, assessment, and packaging reviews are complete.
- Release approval is explicit and recorded separately.
"""


def research_prompt(program: dict, module: dict) -> str:
    return f"""# Research and production prompt for {module['code']}

You are developing **{module['title']}** for the {program['title']}. Work as a curriculum
researcher, One Water domain analyst, technical educator, evidence reviewer, assessment designer,
and accessibility-minded visual planner.

## Outcome to produce

Create a source-backed research and production package that enables a separate authoring team to
teach this learning job:

> {module['learningJob']}

The required applied result is **{module['appliedResult']}**.

## Non-negotiable objectives

{numbered(module['outcomes'])}

## Required research scope

Cover each topic and show how the topics connect:

{bullets(module['topics'])}

For every topic, provide:

1. a plain-English explanation;
2. the underlying mechanism;
3. at least one drinking-water, wastewater, or stormwater example;
4. one boundary, failure, misuse, or counterexample;
5. the role that remains accountable;
6. source-backed claims with precise locators;
7. an assessment opportunity; and
8. a visual or interaction that materially improves understanding.

## Evidence rules

- Start with current United States primary authorities and official technical documentation.
- Use secondary sources only for synthesis, comparison, or context, and label them.
- Create a claim register with claim, source, issuing body, date or version, locator, accessed date,
  jurisdiction, and limitation.
- Separate fact, interpretation, scenario, analogy, recommendation, and unresolved question.
- Record contradictory evidence instead of forcing agreement.
- Never infer legal, regulatory, operational, or safety authority from a marketing page.

## One Water transfer test

Use at least three different contexts across drinking water, wastewater, stormwater, laboratory and
compliance, operations and maintenance, engineering and capital delivery, customer and public
communication, finance and procurement, and emergency response. Explain which parts transfer and
which do not. Do not erase domain-specific authority or consequence.

## Assessment design

Build assessment evidence for:

{bullets(module['assessments'])}

Include recognition, explanation, application, diagnosis and correction, and defense. Provide
feedback for plausible wrong answers. A score without the artifact, criteria, reviewer, revision,
and disposition is incomplete.

## Visual plan

Develop the following visual directions:

{bullets(module['visuals'])}

For each visual, state the teaching job, content, layout, accessibility alternative, and the exact
misconception it is intended to correct.

## Required output package

Return Markdown files for:

1. `RESEARCH-BRIEF.md`
2. `SOURCE-REGISTER.md`
3. `CLAIM-REGISTER.md`
4. `LESSON-ARCHITECTURE.md`
5. `ASSESSMENT-PLAN.md`
6. `VISUAL-PLAN.md`
7. `WORK-PRODUCT-SPECIFICATION.md`
8. `OPEN-QUESTIONS-AND-BOUNDARIES.md`

End with a compliance table mapping every objective and topic to source evidence, lesson coverage,
assessment evidence, visual support when useful, and remaining gaps. Do not call the module ready
for release. Report exactly which production gates remain.
"""


def status_file(program: dict, module: dict) -> str:
    return f"""# Production status: {module['code']}

| Gate | Status | Evidence |
| --- | --- | --- |
| Curriculum blueprint accepted | complete | `MODULE-BLUEPRINT.md` |
| Research package | not started | required outputs in `RESEARCH-AND-PRODUCTION-PROMPT.md` |
| Claims and locators verified | not started | claim and source registers required |
| Full lesson manuscript | not started | complete lesson sequence required |
| Assessments and feedback | not started | objective-aligned assessment package required |
| Visuals and text alternatives | not started | visual plan and approved assets required |
| Domain and technical review | not started | named reviewer dispositions required |
| Accessibility review | not started | accessibility evidence required |
| Articulate build | not started | clean-room package required |
| LearnWorlds package test | not started | tracking and learner test required |
| Release approval | blocked | explicit approval required after every prior gate |

The module is an accepted curriculum blueprint. It is not learner-facing production content and is
not authorized for release or credential evidence.
"""


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    index_rows = []
    for program in data["programs"]:
        program_dir = OUTPUT / program["id"]
        for module in program["modules"]:
            module_dir = program_dir / f"{module['code'].lower()}-{slug(module['title'])}"
            module_dir.mkdir(parents=True, exist_ok=True)
            (module_dir / "MODULE-BLUEPRINT.md").write_text(
                blueprint(program, module), encoding="utf-8"
            )
            (module_dir / "RESEARCH-AND-PRODUCTION-PROMPT.md").write_text(
                research_prompt(program, module), encoding="utf-8"
            )
            (module_dir / "PRODUCTION-STATUS.md").write_text(
                status_file(program, module), encoding="utf-8"
            )
            relative = module_dir.relative_to(OUTPUT)
            index_rows.append(
                f"| {program['shortTitle']} | {module['code']} | {module['title']} | "
                f"{module['guidedHours']} | [{relative}/MODULE-BLUEPRINT.md]({relative}/MODULE-BLUEPRINT.md) |"
            )

    index = """# One Water AI optional extension modules

These packages implement the approved optional curriculum lines without changing the 64-module
universal core. Each package contains an accepted module blueprint, a research and production
prompt, and an honest production-gate record.

| Program | Module | Title | Hours | Blueprint |
| --- | --- | --- | ---: | --- |
""" + "\n".join(index_rows) + "\n"
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "README.md").write_text(index, encoding="utf-8")
    print(f"Built {len(index_rows)} extension module packages at {OUTPUT}")


if __name__ == "__main__":
    main()
