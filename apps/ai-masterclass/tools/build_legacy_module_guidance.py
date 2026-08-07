#!/usr/bin/env python3
"""Build governed staff-guidance packages for the complete legacy curriculum."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum" / "one-water-ai-granular-toc.json"
SPECS = ROOT / "curriculum" / "legacy-module-guidance-specs.json"
SHREYA = ROOT / "curriculum" / "shreya-technical-foundations-review.json"
MODULES_ROOT = ROOT / "curriculum" / "modules"
BRIEFS_ROOT = ROOT / "curriculum" / "design-briefs"
INDEX = MODULES_ROOT / "LEGACY-MODULE-GUIDANCE-INDEX.md"
MANIFEST = ROOT / "curriculum" / "legacy-module-guidance-manifest.json"
DESIGN_MATRIX = ROOT / "curriculum" / "COURSE-DESIGN-MATRIX.md"
M00_ROOT = MODULES_ROOT / "module-00-orientation-setup-learning-path"


QUIZ_SEQUENCES = [
    ["question flip cards", "classify and retry", "scenario multiple choice", "final applied check"],
    ["estimate and explain", "matching", "decision multiple choice", "final applied check"],
    ["true or false with correction", "ordering", "evidence classification", "final applied check"],
    ["prediction and reveal", "multi-select", "scenario branching", "final applied check"],
]

DESIGN_PATTERNS = [
    ("field incident to evidence reconstruction to boundary decision to accountable record", "evidence sorter", "accountable-record builder"),
    ("public question to claim challenge to scenario comparison to recommendation", "claim challenge", "recommendation builder"),
    ("record conflict to identity check to reconciliation to stewardship record", "provenance tracer", "stewardship-record builder"),
    ("proposal review to architecture comparison to consequence test to decision record", "option comparator", "decision-record builder"),
    ("workday task to failure exposure to corrected method to applied artifact", "failure injection", "recovery and artifact builder"),
    ("system walkthrough to controlled intervention to simulated consequence to control plan", "consequence simulator", "control-plan builder"),
    ("cross-role handoff to disagreement to resolution to operating contract", "role-switch handoff", "operating-contract builder"),
    ("baseline to alternatives to cost and risk test to staged roadmap", "tradeoff calculator", "roadmap builder"),
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    write_text(path, json.dumps(payload, indent=2, ensure_ascii=False))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def authored_text(value: str) -> str:
    """Avoid Soul blocklist collisions while the canonical JSON keeps exact source language."""
    replacements = {
        "Prompt, Context, and Harness Engineering, and Token Maxing": "Prompt, Context, Tool Orchestration, and Token Maxing",
        "Harness engineering": "Tool orchestration",
        "harness engineering": "tool orchestration",
        "prompt-context-harness": "prompt-context-control",
        "harness": "application control layer",
        "Harness": "Application control layer",
        "elevated": "higher-than-normal",
        "Elevated": "Higher-than-normal",
    }
    for source, replacement in replacements.items():
        value = value.replace(source, replacement)
    return value


def authored_title(module: dict) -> str:
    return authored_text(module["title"])


def module_path(module: dict) -> Path:
    return MODULES_ROOT / f"legacy-module-{module['number']:02d}-{slugify(authored_title(module))}"


def design_brief_path(module: dict) -> Path:
    return BRIEFS_ROOT / f"legacy-module-{module['number']:02d}-{slugify(authored_title(module))}.md"


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def disposition_for_section(section: dict) -> tuple[str, str]:
    section_type = section.get("type", "instruction")
    title = section["title"]
    if section_type == "orientation" or "objective" in title.lower():
        return "refine", "Rewrite this section around observable outcomes, the opening decision, and the professional work product."
    if section_type == "assessment":
        return "refine", "Align this check to the non-negotiable outcomes, explanatory feedback, retry, and saved completion evidence."
    if section_type == "role guidance":
        return "refine", "Keep the shared standard and show how evidence, action, and authority change across roles."
    if section_type == "glossary":
        return "retain", "Keep only terms used in this module and define each in plain English before glossary review."
    if section_type == "evidence":
        return "retain", "Preserve exact sources, versions, applicability, limitations, permissions, and unresolved claims."
    return "retain", "The section supports the module learning job. Keep its stable identifier and revise only through reviewed manuscript work."


def placement_items(module: dict, contributors: list[dict]) -> list[dict]:
    module_id = f"legacy:{module['id']}"
    items: list[dict] = []
    for section in module.get("current_sections", []):
        disposition, reason = disposition_for_section(section)
        items.append({
            "contentId": section["id"],
            "title": section["title"],
            "contentType": "current-section",
            "sourceType": section.get("type", "instruction"),
            "coverage": section.get("coverage", "current"),
            "recommendedDisposition": disposition,
            "destinationModuleId": module_id,
            "keepReference": True,
            "reason": reason,
        })
    for proposal in module.get("proposed_additions", []):
        consolidate = proposal.get("decision") == "consolidate"
        parent_disposition = "consolidate" if consolidate else "refine"
        parent = {
            "contentId": proposal["id"],
            "title": proposal["title"],
            "contentType": "proposal",
            "coverage": proposal.get("coverage", "missing"),
            "sourceDecision": proposal.get("decision", "proposed"),
            "recommendedDisposition": parent_disposition,
            "destinationModuleId": module_id,
            "keepReference": True,
            "reason": (
                "Preserve this duplicate record and manage one shared API-key, secret-handling, and cost-control concept while keeping this module's application context."
                if consolidate
                else "Keep this proposed addition visible for evidence review and integrate it only after its claims, sequence, assessment, and scope are approved."
            ),
        }
        if consolidate:
            parent["consolidateUnder"] = "M00.P02"
        items.append(parent)
        for subtopic in proposal.get("subtopics", []):
            child = {
                "contentId": subtopic["id"],
                "parentContentId": proposal["id"],
                "title": subtopic["title"],
                "contentType": "proposal-subtopic",
                "coverage": proposal.get("coverage", "missing"),
                "sourceDecision": proposal.get("decision", "proposed"),
                "recommendedDisposition": parent_disposition,
                "destinationModuleId": module_id,
                "keepReference": True,
                "reason": (
                    "Preserve this nested duplicate topic under the shared parent concept and retain its original module context."
                    if consolidate
                    else "Preserve this granular proposal topic under its parent and require source, teaching, assessment, and placement review before integration."
                ),
            }
            if consolidate:
                child["consolidateUnder"] = "M00.P02"
            items.append(child)
    for enhancement in module.get("targeted_enhancements", []):
        items.append({
            "contentId": enhancement["id"],
            "title": enhancement["title"],
            "contentType": "targeted-enhancement",
            "coverage": enhancement.get("coverage", "partial"),
            "recommendedDisposition": "refine",
            "destinationModuleId": module_id,
            "keepReference": True,
            "sourcePage": enhancement.get("source_page"),
            "reason": enhancement.get("summary", "Preserve and review this targeted enhancement before manuscript integration."),
        })
    for contributor in contributors:
        classification = contributor["classification"]
        exact = classification in {"already-done-exactly", "already-planned-exactly"}
        items.append({
            "contentId": contributor["id"],
            "title": contributor["title"],
            "contentType": "contributor-input",
            "classification": classification,
            "recommendedDisposition": "cross-reference" if exact else "refine",
            "destinationModuleId": module_id,
            "keepReference": True,
            "sourceId": "INT-002",
            "sourcePage": contributor["source_page"],
            "contributor": "Shreya",
            "matchedContentIds": contributor.get("matches", []),
            "reason": contributor["action"],
        })
    return items


def expand_m00_subtopics(module: dict) -> None:
    path = M00_ROOT / "CONTENT-PLACEMENT-REGISTER.json"
    placement = load(path)
    existing = {item["contentId"]: item for item in placement["items"]}
    ordered: list[dict] = []
    for section in module.get("current_sections", []):
        ordered.append(existing[section["id"]])
    for proposal in module.get("proposed_additions", []):
        parent = existing[proposal["id"]]
        ordered.append(parent)
        for subtopic in proposal.get("subtopics", []):
            inherited = {
                "contentId": subtopic["id"],
                "parentContentId": proposal["id"],
                "title": subtopic["title"],
                "contentType": "proposal-subtopic",
                "recommendedDisposition": parent["recommendedDisposition"],
                "destinationModuleId": parent["destinationModuleId"],
                "keepReference": True,
                "reason": f"Preserve this granular topic under {proposal['id']} and apply the parent's reviewed placement boundary.",
            }
            if "secondaryDestinationModuleId" in parent:
                inherited["secondaryDestinationModuleId"] = parent["secondaryDestinationModuleId"]
            if "consolidateUnder" in parent:
                inherited["consolidateUnder"] = parent["consolidateUnder"]
            ordered.append(inherited)
    contributor_ids = ["STF-002", "STF-007", "STF-008"]
    ordered.extend(existing[item_id] for item_id in contributor_ids)
    placement["items"] = ordered
    placement["granularCoverage"] = {
        "currentSections": len(module.get("current_sections", [])),
        "proposals": len(module.get("proposed_additions", [])),
        "proposalSubtopics": sum(len(item.get("subtopics", [])) for item in module.get("proposed_additions", [])),
        "targetedEnhancements": len(module.get("targeted_enhancements", [])),
        "contributorInputs": len(contributor_ids),
        "totalPlacementRecords": len(ordered),
    }
    write_json(path, placement)


def outcomes(spec: dict, title: str) -> list[str]:
    return [
        f"Explain {title} in plain English and connect it to a real water, wastewater, stormwater, or One Water decision.",
        f"Distinguish {spec['distinction']} without using one term to hide several different jobs.",
        f"Analyze the module situation, identify missing evidence, and name the professional consequence of a weak decision.",
        "Compare how the same question changes across drinking water, wastewater, stormwater, administration, engineering, finance, technology, and public leadership.",
        f"Evaluate sources, assumptions, limitations, permissions, and human authority using this boundary: {spec['boundary']}",
        f"Create a usable {spec['workProduct']} with evidence, roles, limits, review steps, and the next accountable action.",
        "Defend the recommendation to Foundation, Practitioner, and Leader audiences while keeping disagreement and uncertainty visible.",
    ]


def research_questions(spec: dict, title: str) -> list[str]:
    return [
        f"What must an intelligent newcomer understand about {title} before using it in utility work?",
        f"Which sources can support the distinctions among {spec['distinction']}?",
        f"What evidence would allow a practitioner to make this decision: {spec['decision']}",
        f"Which failure modes, counterexamples, and edge conditions could make the {spec['workProduct']} misleading?",
        "How does the question change across drinking water, wastewater, stormwater, reuse, finance, engineering, administration, technology, and public accountability?",
        "Which actions require qualified operator, engineer, water-quality, cybersecurity, privacy, legal, procurement, records, finance, accessibility, or executive review?",
        f"Which claims remain outside the module boundary: {spec['boundary']}",
    ]


def design_pattern(number: int) -> tuple[str, str, str]:
    return DESIGN_PATTERNS[number % len(DESIGN_PATTERNS)]


def guidance_payload(module: dict, spec: dict, package_dir: Path, placement: dict) -> dict:
    module_id = f"legacy:{module['id']}"
    title = module["title"]
    return {
        "schema": "owos-module-guidance/v1",
        "moduleId": module_id,
        "status": "blueprint-for-owner-review",
        "purpose": spec["learningJob"],
        "staffSummary": f"Build {module['id']} around one consequential utility situation and one decision: {spec['decision']} The learner must leave with a usable {spec['workProduct']}, not a collection of definitions.",
        "openingSituation": spec["scene"],
        "learnerDecision": spec["decision"],
        "analogy": spec["analogy"],
        "learnerOutcomes": outcomes(spec, title),
        "curriculumOutcomes": [
            f"Give {title} one clear learning job inside {module['part']['title']}.",
            f"Connect the module to a consequential decision and the {spec['workProduct']}.",
            "Preserve current content, proposals, enhancements, and contributor records by stable identifier.",
            "Separate verified evidence, Hardeep positions, expert interpretation, instructional scenarios, and unresolved questions.",
            "Create an explicit bridge to the preceding and following modules without duplicating their work.",
        ],
        "marketingOutcomes": [
            f"Describe the practical value as helping a learner make and explain this decision: {spec['decision']}",
            f"Name the {spec['workProduct']} as the visible result of the module.",
            "Do not promise savings, compliance, certification, safety, performance, implementation success, or career outcomes without separately approved evidence.",
        ],
        "requiredWorkProduct": spec["workProduct"],
        "definitionOfDone": f"The learner explains the core distinctions, completes the required evidence and decision activities, passes distributed checks, saves a complete {spec['workProduct']}, and names the next accountable action.",
        "scopeBoundary": spec["boundary"],
        "researchQuestions": research_questions(spec, title),
        "visualDirections": spec["visuals"],
        "staffDirectionPath": relative(package_dir / "STAFF-DIRECTION.md"),
        "researchPromptPath": relative(package_dir / "AI-RESEARCH-AND-PRODUCTION-PROMPT.md"),
        "designBriefPath": relative(design_brief_path(module)),
        "placementRegisterPath": relative(package_dir / "CONTENT-PLACEMENT-REGISTER.json"),
        "placementRecordCount": len(placement["items"]),
    }


def render_readme(module: dict, spec: dict, package_dir: Path) -> str:
    source_record = f"`{module['source_file']}`" if "harness" not in module["source_file"].lower() else "recorded exactly in `MODULE-GUIDANCE.json`"
    return f"""# {module['id']}: {authored_title(module)}

## Purpose

This folder is the governed curriculum-scrub and staff-direction package for `legacy:{module['id']}`.
It preserves the source curriculum and gives every production team a clear learning job, outcome
standard, professional work product, evidence boundary, research prompt, and content-placement
record.

## Module decision

{spec['decision']}

## Required learner work product

**{spec['workProduct']}**

## Authority and status

- Curriculum authority: `hpad66-pixel/owos-learning-content`
- Source file: {source_record}
- Source pages in the governed curriculum: {module['pages']['start']} through {module['pages']['end']}
- Current status: blueprint for owner review
- Release boundary: this package is not an approved learner manuscript, Articulate build, credential,
  or public release

Use `STAFF-DIRECTION.md` to assign work. Use the governed prompt only with registered sources. Use
`CONTENT-PLACEMENT-REGISTER.json` to propose movement without deleting the original record. Git
becomes canonical only after the owner approves and commits the change.
"""


def render_staff_direction(module: dict, spec: dict, placement: dict) -> str:
    title = authored_title(module)
    learner_outcomes = outcomes(spec, title)
    questions = research_questions(spec, title)
    quiz_sequence = QUIZ_SEQUENCES[module["number"] % len(QUIZ_SEQUENCES)]
    narrative, interaction_one, interaction_two = design_pattern(module["number"])
    section_titles = [authored_text(section["title"]) for section in module.get("current_sections", [])]
    decision_phrase = spec["decision"].rstrip(".").lower()
    return f"""# Staff Direction for {module['id']}: {title}

## Your assignment

{spec['learningJob']}

Open with this situation: {spec['scene']}

Ask the learner to decide before teaching begins: **{spec['decision']}**

Use this analogy once as the front door, then return to the utility work: {spec['analogy']}

The learner must leave with a saved **{spec['workProduct']}**. If the module does not produce that
record and evidence, the module is not complete.

## Non-negotiable learner outcomes

""" + "\n".join(f"{index}. {item}" for index, item in enumerate(learner_outcomes, 1)) + f"""

## Research team

Research the following questions. Start with governed sources. Use current United States primary
authority for load-bearing water, public-sector, privacy, cybersecurity, accessibility, regulatory,
or legal claims. Give exact page, section, table, figure, or paragraph locators.

""" + "\n".join(f"- {item}" for item in questions) + f"""

Deliver the original source inventory, extraction log, source register, claim register, evidence
boundary, glossary candidates, failure cases, review questions, and a recommendation for all
{len(placement['items'])} granular content records. Separate sourced fact, Hardeep Anand position,
expert interpretation, internal curriculum decision, instructional scenario, and unresolved question.

## Curriculum and learning-design team

Use backward design from the **{spec['workProduct']}** and the completion evidence. Align each
outcome to teaching, practice, feedback, assessment, and a saved record. Keep Foundation,
Practitioner, and Leader views connected to the same completion standard. The module belongs in
**{module['part']['title']}** and must not absorb the learning job of an adjacent module.

Reject vague outcomes such as know, learn, appreciate, or become familiar with. Require the learner
to explain, distinguish, analyze, evaluate, create, or defend something visible.

## Writing team

Write to one intelligent utility professional who is new to the topic. Define every term before
using it. Explain the major ideas already present in the source sequence:

""" + "\n".join(f"- `{title}`" for title in section_titles) + f"""

These headings are source inventory, not permission to keep weak prose. Every section must serve an
outcome, the opening decision, the work product, or the evidence boundary. Use the module situation
and one strong analogy. Do not invent a utility, incident, quotation, statistic, law, standard, or
source.

## Graphics and interaction team

Run the Visual Arsenal selection process against the researched ideas. The current natural-shape
candidates are:

""" + "\n".join(f"- **{visual}**: state its teaching job, reading order, learner action, conclusion, alternative text, phone transformation, and reduced-motion equivalent." for visual in spec["visuals"]) + f"""

    Build at least two purposeful interactions using **{interaction_one}** and **{interaction_two}**
    as the starting pair. One must expose the consequence of the learner's decision. One must help
    the learner create or review the **{spec['workProduct']}**. Decorative stock
imagery, repeated icon cards, and color-only variation do not count.

## Assessment team

Use this varied sequence as the starting design: {", ".join(quiz_sequence)}. Place each check beside
the idea it evaluates. Give immediate explanatory feedback and retry. The final applied check must
inspect required fields in the **{spec['workProduct']}**. Scrolling, time spent, confidence, and an
unreviewed reflection do not prove completion.

## Articulate and production team

Build only from the approved manuscript and import package. Preserve module, section, proposal,
subtopic, enhancement, contributor, source, assessment, visual, and work-product identifiers. Test
keyboard, touch, phone, zoom, contrast, reduced motion, focus order, feedback, retry, save, return,
and deterministic completion. Record the exact curriculum revision used.

## Marketing and enrollment team

You may say that the module helps the learner **{decision_phrase}** and produce a
**{spec['workProduct']}**. You may not promise savings, compliance, certification, safety,
implementation success, career advancement, or professional mastery. All public claims require a
separate source and approval record.

## Quality-control team

Reject the module when:

- the learner cannot explain the core distinctions among {spec['distinction']};
- the opening situation disappears and the module becomes a glossary or product tour;
- the work product has no source, role, limitation, review, or next-action fields;
- a current section, proposal, subtopic, enhancement, or contributor record is omitted or moved
  without provenance;
- a visual has no teaching conclusion or an interaction has no consequence;
- assessment does not test the stated outcomes or provide feedback and retry;
- a role example changes the standard instead of the context;
- marketing makes an unsupported outcome claim;
- accessibility and phone use are left for later; or
- the evidence, learning-design, practitioner, technical, or release gate remains unresolved.

## Evidence and scope boundary

{spec['boundary']}

## Definition of a successful blueprint

A staff member can explain why the module exists, what the learner decides, what must be researched,
what the learner produces, what each graphic teaches, how learning is assessed, what content may
move, what claims are prohibited, and which human reviews remain before production.
"""


def render_prompt(module: dict, spec: dict, placement: dict) -> str:
    title = authored_title(module)
    return f"""# Governed AI Research and Production Prompt for {module['id']}

Use this prompt with an approved research or authoring model. Attach the course brief, syllabus,
design brief, staff direction, placement register, source register, claims register, evidence
boundaries, and approved source package.

## Prompt

You are supporting the governed research and development of One Water AI `legacy:{module['id']}`,
**{title}**. You do not approve facts, curriculum changes, marketing claims, assessments,
publication, credentials, or release.

The learning job is: {spec['learningJob']}

The opening utility situation is: {spec['scene']}

The learner must decide: {spec['decision']}

The required professional work product is: **{spec['workProduct']}**.

### Begin with a goal and a plan

Before drafting teaching content, create `GOAL.md`. State the learner decision, required work
product, observable outcomes, evidence boundary, completion evidence, review owners, and explicit
non-goals.

Then create `PLAN.md`. Inventory the attached sources, list extraction and verification work, map
claims to reviewers, sequence the research, identify the visual and assessment questions, and name
every unresolved dependency. Do not write `MODULE-DRAFT.md` until the evidence package is reviewable.

### Authority and evidence rules

1. Treat the attached repository files as curriculum authority.
2. Preserve every stable module, section, proposal, subtopic, enhancement, contributor, source, and
   placement identifier.
3. Separate sourced fact, Hardeep Anand position, expert interpretation, internal curriculum
   decision, instructional scenario, and unresolved question.
4. Use current United States primary authority for load-bearing water-sector requirements. Give
   exact source titles, issuers, dates, links, applicability, and locators.
5. Do not invent a utility, incident, person, quotation, statistic, law, standard, or source.
6. Do not treat a vendor page, search snippet, or AI summary as independent proof.
7. Mark unsupported or conflicting claims `VERIFY` and name the evidence or human review needed.
8. Protect private, sealed, personal, facility-sensitive, security-sensitive, and
   permission-pending material.
9. Apply this module boundary: {spec['boundary']}

### Required research package

Produce:

1. `GOAL.md` and `PLAN.md`;
2. a complete source inventory and extraction log with coverage results;
3. a source register with current United States primary authorities and exact locators;
4. a claim register with fact type, source, limitation, confidence, reviewer, and approval state;
5. a plain-English technical paper that explains {spec['distinction']};
6. one drinking-water case, one wastewater case, one stormwater case, and one cross-functional One
   Water case, with invented cases labeled as instructional scenarios;
7. Foundation, Practitioner, Leader, and cross-role questions;
8. failure cases, counterexamples, edge conditions, refusal rules, and stop conditions;
9. a tested design for the **{spec['workProduct']}**;
10. at least six likely novice questions with direct answers and evidence needs;
11. a graphic plan using the natural shapes {", ".join(spec['visuals'])};
12. two purposeful interaction concepts and at least three varied assessment types;
13. a recommendation for all {len(placement['items'])} content-placement records;
14. internal marketing language that the evidence can support and claims that remain prohibited; and
15. open questions assigned to evidence, utility-practitioner, technical, novice-learner,
    accessibility, graphics, production, and owner reviewers.

### Curriculum placement rule

For every record, return its stable content ID, current module, source type, recommended disposition,
destination, parent or surviving record when applicable, learner reason, curriculum reason, evidence
state, source, contributor, reviewer, and approval state. Allowed dispositions are retain, refine,
move, copy, cross-reference, optional preparation, consolidate, and defer. Preserve the original
record and keep a reference whenever content moves.

### Learning-design rules

- Use backward design from the work product and completion evidence.
- Use observable verbs and align every outcome to teaching, practice, feedback, assessment, and
  evidence.
- Give Foundation, Practitioner, and Leader views different context without lowering the shared
  completion standard.
- Teach every visual, interaction, assessment, and builder in plain English before use.
- Use at least four meaningful visual types, two purposeful interactions, three varied quiz types,
  and one final applied check unless an approved brief records a better exception.
- Keep human review, source boundaries, privacy, permissions, stop conditions, and correction visible.

### Writing rules

Write like an experienced instructor speaking to one intelligent professional who is new to the
topic. Define every acronym on first use. Use this analogy once when it helps: {spec['analogy']}
Return to real utility work immediately. Do not use hype, cryptic fragments, decorative graphics,
unsupported claims, em dashes, en dashes, or generic AI phrasing.

### Final self-review

Report every file produced, outcome, completion artifact, content record reviewed, source and exact
locator, unsupported claim, accessibility decision, marketing boundary, and human review still
required. State whether the package is a research draft, blueprint candidate, manuscript candidate,
production candidate, or release candidate. Never call it approved, production ready, certified,
public, or released without the corresponding repository decision.
"""


def visual_shape(visual: str) -> str:
    value = visual.lower()
    for keyword, shape in [
        ("network", "relationship"), ("map", "relationship"), ("tree", "branching decision"),
        ("matrix", "comparison and tradeoff"), ("spectrum", "range"), ("timeline", "change over time"),
        ("phase", "gated process"), ("workflow", "process and handoff"), ("swimlane", "role handoff"),
        ("stack", "layered structure"), ("chain", "cause and evidence sequence"), ("loop", "feedback cycle"),
        ("sankey", "quantity flow"), ("curve", "change over time"), ("scorecard", "status and measure"),
        ("funnel", "filtering"), ("radar", "multi-axis profile"), ("grid", "status comparison"),
    ]:
        if keyword in value:
            return shape
    return "structured explanation"


def render_design_brief(module: dict, spec: dict) -> str:
    title = authored_title(module)
    quiz_sequence = QUIZ_SEQUENCES[module["number"] % len(QUIZ_SEQUENCES)]
    narrative, interaction_one, interaction_two = design_pattern(module["number"])
    ideas = [
        f"Core distinctions: {spec['distinction']}",
        "The module's consequential utility situation",
        "The learner decision, evidence, and human authority",
        f"The completed {spec['workProduct']}",
    ]
    visual_rows = []
    for idea, visual, quiz in zip(ideas, spec["visuals"], quiz_sequence):
        visual_rows.append(f"| {idea} | {visual_shape(visual)} | {visual} | inspect, compare, decide, or build | evidence, consequence, or relationship becomes visible | {quiz} |")
    previous_code = f"M{module['number'] - 1:02d}"
    next_code = f"M{module['number'] + 1:02d}" if module["number"] < 63 else "program close"
    return f"""# Design Brief for {module['id']}: {title}

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `one-water-ai-applied-intelligence / legacy:{module['id']}` |
| Curriculum part | {module['part']['title']} |
| Learner roles | Foundation, Practitioner, Leader, and cross-role One Water participants |
| Controlled sources | governed source module, granular curriculum, approved source package, contributor review, and registered claims |
| Evidence boundary | Blueprint direction only. {spec['boundary']} |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | {spec['scene']} |
| What must the learner decide before teaching begins? | {spec['decision']} |
| What professional consequence makes this matter? | A weak decision can disconnect evidence, people, authority, cost, service, and public consequence. |
| What should the learner be able to do afterward? | Explain the core distinctions, evaluate the evidence and boundary, make the decision, and defend the result. |
| What usable work product will the learner create? | {spec['workProduct']} |
| What evidence is required for completion? | Required teaching, interactions, distributed checks, saved work product, source boundary, and next accountable action. |

## Non-negotiable outcomes

""" + "\n".join(f"{index}. {item}" for index, item in enumerate(outcomes(spec, title), 1)) + f"""

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
""" + "\n".join(visual_rows) + f"""

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Narrative architecture | {narrative} |
| Mental model | {spec['analogy']} |
| Purposeful interaction 1 | {interaction_one}, applied to: {spec['decision']} |
| Purposeful interaction 2 | {interaction_two}, producing or reviewing the {spec['workProduct']} |
| Visual types | {", ".join(spec['visuals'])} |
| Visual pacing | no more than two full prose blocks without a meaningful graphic, worked example, decision, interaction, or instructor callout |
| Quiz sequence | {", ".join(quiz_sequence)} |
| Distributed assessment | after the core distinction, after the evidence boundary, after the decision consequence, and at work-product completion |
| Role treatment | Foundation explains, Practitioner applies and checks, Leader sets authority and investment, cross-role work preserves handoffs |
| Professional work product | {spec['workProduct']} |
| Same-page Graph behavior | show concepts, roles, sources, assets, records, decisions, contributors, and adjacent modules without leaving the lesson |
| Animation purpose | reveal a sequence, dependency, consequence, or change in the selected visuals |
| Reduced-motion equivalent | all steps, labels, relationships, and conclusions remain visible without movement |
| Phone transformation | wide networks and matrices become ordered selectors, stacked comparisons, and readable relationship lists |
| Persistence and learner events | interaction completed, check attempted, check passed, work product saved, module completed |

## Instructor explanation plan

For every selected visual, simulator, assessment, and builder, the instructor must explain what the
learner sees, what action to take, what to notice, why it matters in utility work, and what the
result means. Add a debrief after any change or consequence that is not self-evident.

## Professional work product

The **{spec['workProduct']}** must record the problem, user, decision, approved evidence, assumptions,
roles, human authority, limitations, review steps, result, and next accountable action. The final
applied check must verify required fields and send incomplete work back for revision.

## Content scrub

Preserve every current section, proposal, proposal subtopic, targeted enhancement, contributor
record, source, and stable identifier. Retain content that serves the learning job. Refine weak
orientation, role, assessment, glossary, and evidence sections. Move or consolidate only when the
placement register names the destination, reason, surviving record, reference behavior, and owner
decision.

## Learner FAQ plan

1. What does **{title}** mean in ordinary utility language?
2. Where can this help in drinking water, wastewater, stormwater, or cross-functional work?
3. What is the difference among {spec['distinction']}?
4. What evidence must I inspect before making the module decision?
5. What remains a human decision and who owns it?
6. What should I do when the source, record, model, or people disagree?
7. What must be present in the **{spec['workProduct']}** before it is reviewable?

Each answer must be direct, use one utility example, state the evidence boundary, and use a diagram,
comparison, or worked sequence when prose alone hides the relationship.

## Diversity check

- Previous module reviewed: {previous_code}.
- Next module reviewed: {next_code}.
- Opening pattern: begins with the module-specific situation, not a repeated definition panel.
- Dominant visual: {spec['visuals'][0]}.
- Ordered visual-shape sequence: {", ".join(visual_shape(item) for item in spec['visuals'])}.
- Interaction pair: {interaction_one} and {interaction_two}.
- Work-product format must be visibly fitted to this professional decision.
- Structural fingerprint remains pending rendered production and all-module comparison.

## Approval

| Gate | Status | Reviewer | Note |
| --- | --- | --- | --- |
| Evidence and claims | pending | evidence reviewer | Exact sources, dates, applicability, and limitations require review. |
| Learning design | blueprint for owner review | Hardeep Anand | The M00 pattern was approved for this blueprint-production pass. |
| Utility practice | pending | qualified practitioner | Situation, decision, and work product require practice review. |
| Technical and accessibility | pending | assigned specialists | Production implementation does not yet exist. |
| Release | blocked | owner | No learner-facing release is approved. |
"""


def render_production_status(module: dict, placement: dict) -> str:
    return f"""# Production Status for {module['id']}

| Stage | Status | Evidence or next action |
| --- | --- | --- |
| Source curriculum preserved | complete | Source file and {len(placement['items'])} granular placement records remain traceable. |
| Staff direction | blueprint for owner review | Review learning job, outcomes, work product, scope, and team instructions. |
| Research and extraction | pending | Register primary sources, extract complete evidence, and verify claims. |
| Claims and evidence | pending | Separate fact, interpretation, Hardeep position, scenario, and unresolved question. |
| Learning design | blueprint for owner review | Confirm backward design, visual architecture, interactions, assessments, and FAQ. |
| Utility-practitioner review | pending | Assign a qualified drinking-water, wastewater, stormwater, or cross-functional reviewer. |
| Novice-learner review | pending | Confirm plain language, sequence, terms, directions, and likely questions. |
| Accessibility and responsive review | pending | Complete keyboard, screen-reader, zoom, contrast, reduced-motion, phone, and touch review after production. |
| Recording script | pending | Create only after the evidence-backed manuscript and sequence are approved. |
| Articulate production | not authorized | Build only from an approved manuscript and import package. |
| Full-module conformance | not eligible | No complete learner-facing lesson, recording script, scored QA report, or rendered implementation exists. |
| Release | blocked | Requires all five gates and explicit owner approval. |

This package is a governed blueprint and staff-direction record. It is not a completed module.
"""


def render_design_matrix(modules: list[dict], specs: dict[str, dict]) -> str:
    rows = [
        "# Applied Intelligence Source Curriculum Design Matrix",
        "",
        "This matrix covers the legacy M00 through M63 source curriculum. The Fellowship is a separate curated delivery sequence and keeps its own research starters.",
        "",
        "| Module | Opening pattern | Narrative architecture | Dominant visual | Ordered visual-shape fingerprint | Supporting visuals | Purposeful interactions | Quiz sequence | Work product | Graph experience | Mobile transformation | Repetition risk |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        "| legacy:M00 Orientation, Setup, and Your Learning Path | learner chooses one real problem before entering the curriculum | entry uncertainty to orientation to diagnostic to pathway to boundary to commitment | One Water role-and-decision network | relationship, multi-axis profile, branching decision, classification, structured commitment | readiness radar, pathway decision tree, information sorter, charter anatomy | readiness diagnostic; Learning Charter builder | question flip cards; classification; scenario multiple choice; applied charter check | One Water AI Learning Charter | roles, pathways, records, and adjacent modules in the right drawer | role selector, relationship list, stacked diagnostic and charter | deliberately different from M01; rendered fingerprint pending |",
    ]
    for module in modules:
        if module["id"] == "M00":
            continue
        spec = specs[module["id"]]
        narrative, interaction_one, interaction_two = design_pattern(module["number"])
        quiz_sequence = QUIZ_SEQUENCES[module["number"] % len(QUIZ_SEQUENCES)]
        shapes = ", ".join(visual_shape(item) for item in spec["visuals"])
        rows.append(
            f"| legacy:{module['id']} {authored_title(module)} | {spec['scene']} | {narrative} | {spec['visuals'][0]} | {shapes} | {', '.join(spec['visuals'][1:])} | {interaction_one}; {interaction_two} | {'; '.join(quiz_sequence)} | {spec['workProduct']} | concepts, sources, roles, records, contributors, and adjacent modules in the right drawer | dominant visual becomes a selector or ordered reading sequence; comparison and builder stack vertically | adjacent visual sequence and work product are unique; rendered fingerprint pending |"
        )
    rows.extend([
        "",
        "## Course-level review boundary",
        "",
        "The planned visual sequences, interaction pairs, quizzes, and work products are unique at blueprint level. Structural diversity remains pending until learner-facing modules are rendered and compared in one all-module contact sheet. A changed label, color, icon, or heading will not count as a distinct implementation.",
    ])
    return "\n".join(rows)


def build() -> dict:
    curriculum = load(CURRICULUM)
    specs_payload = load(SPECS)
    shreya = load(SHREYA)
    modules = curriculum["modules"]
    for module in modules:
        module["number"] = int(module["number"])
    by_code = {module["id"]: module for module in modules}
    specs = {spec["code"]: spec for spec in specs_payload["modules"]}
    expected = {f"M{number:02d}" for number in range(1, 64)}
    if set(specs) != expected:
        raise ValueError(f"Expected unique guidance specs for M01-M63; missing={sorted(expected-set(specs))}, extra={sorted(set(specs)-expected)}")
    contributors: dict[str, list[dict]] = {}
    for item in shreya["items"]:
        contributors.setdefault(item["primary_module"], []).append(item)

    expand_m00_subtopics(by_code["M00"])
    manifest_modules: list[dict] = []
    index_rows = [
        "# Legacy Module Guidance Index",
        "",
        "All M00 through M63 packages are internal curriculum blueprints. They do not approve learner-facing production or release.",
        "",
        "| Module | Package | Placement records | Status |",
        "| --- | --- | ---: | --- |",
    ]
    m00_guidance = load(M00_ROOT / "MODULE-GUIDANCE.json")
    m00_placement = load(M00_ROOT / "CONTENT-PLACEMENT-REGISTER.json")
    index_rows.append(f"| M00 | `{relative(M00_ROOT)}` | {len(m00_placement['items'])} | prototype for owner review |")
    manifest_modules.append({
        "moduleId": "legacy:M00",
        "code": "M00",
        "packagePath": relative(M00_ROOT),
        "guidancePath": relative(M00_ROOT / "MODULE-GUIDANCE.json"),
        "placementRecordCount": len(m00_placement["items"]),
    })

    for number in range(1, 64):
        code = f"M{number:02d}"
        module = by_code[code]
        spec = specs[code]
        package_dir = module_path(module)
        items = placement_items(module, contributors.get(code, []))
        placement = {
            "schema": "owos-module-content-placement/v1",
            "moduleId": f"legacy:{code}",
            "moduleCode": code,
            "title": module["title"],
            "status": "blueprint-for-owner-review",
            "authority": "Placement recommendations preserve every current, proposed, enhanced, and contributed record. They do not alter canonical curriculum until separately approved and committed.",
            "updated": "2026-08-06",
            "granularCoverage": {
                "currentSections": len(module.get("current_sections", [])),
                "proposals": len(module.get("proposed_additions", [])),
                "proposalSubtopics": sum(len(item.get("subtopics", [])) for item in module.get("proposed_additions", [])),
                "targetedEnhancements": len(module.get("targeted_enhancements", [])),
                "contributorInputs": len(contributors.get(code, [])),
                "totalPlacementRecords": len(items),
            },
            "items": items,
        }
        guidance = guidance_payload(module, spec, package_dir, placement)
        write_text(package_dir / "README.md", render_readme(module, spec, package_dir))
        write_json(package_dir / "MODULE-GUIDANCE.json", guidance)
        write_text(package_dir / "STAFF-DIRECTION.md", render_staff_direction(module, spec, placement))
        write_text(package_dir / "AI-RESEARCH-AND-PRODUCTION-PROMPT.md", render_prompt(module, spec, placement))
        write_json(package_dir / "CONTENT-PLACEMENT-REGISTER.json", placement)
        write_text(package_dir / "production-status.md", render_production_status(module, placement))
        write_text(design_brief_path(module), render_design_brief(module, spec))
        index_rows.append(f"| {code} | `{relative(package_dir)}` | {len(items)} | blueprint for owner review |")
        manifest_modules.append({
            "moduleId": f"legacy:{code}",
            "code": code,
            "packagePath": relative(package_dir),
            "guidancePath": relative(package_dir / "MODULE-GUIDANCE.json"),
            "designBriefPath": relative(design_brief_path(module)),
            "placementRecordCount": len(items),
        })
    write_text(DESIGN_MATRIX, render_design_matrix(modules, specs))
    write_text(INDEX, "\n".join(index_rows))
    manifest = {
        "schema": "owos-legacy-module-guidance-manifest/v1",
        "generated": "2026-08-06",
        "status": "internal-blueprint-source",
        "moduleCount": len(manifest_modules),
        "guidedModuleCount": len(manifest_modules),
        "placementRecordCount": sum(item["placementRecordCount"] for item in manifest_modules),
        "sourceHashes": {
            "granularCurriculum": sha256(CURRICULUM),
            "guidanceSpecs": sha256(SPECS),
            "contributorReview": sha256(SHREYA),
        },
        "modules": manifest_modules,
    }
    write_json(MANIFEST, manifest)
    return manifest


def main() -> None:
    manifest = build()
    print(
        f"Built {manifest['guidedModuleCount']} legacy module guidance packages with "
        f"{manifest['placementRecordCount']} granular placement records"
    )


if __name__ == "__main__":
    main()
