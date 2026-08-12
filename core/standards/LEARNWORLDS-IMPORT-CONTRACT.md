# OWOS Module Authoring and LearnWorlds Import Contract

**Schema:** `owos-learnworlds-module/v1`
**Status:** prototype for owner review
**Applies to:** every module authored under `apps/<course>/curriculum/modules/`
**Authority:** this contract governs file structure only. It does not approve facts, claims,
placements, assessments, or release. Those remain governed by `CLAIMS-REGISTER.md`,
`SOURCE-REGISTER.md`, `EVIDENCE-BOUNDARIES.md`, `CONTENT-PLACEMENT-REGISTER.json`, and
`APPROVALS.md`.

---

## 1. Why this file exists

The governed authoring path produces a markdown manuscript. LearnWorlds does not consume a
markdown manuscript. Verified against current LearnWorlds documentation:

- A LearnWorlds course has exactly two structural levels. A course contains **sections**, and a
  section contains **learning activities**. There are no subsections and no nested units.
- There is no markdown import. The real import surfaces are: bulk upload of files, SCORM and HTML5
  package upload including graded SCORM, Microsoft Word import into an Ebook learning activity,
  spreadsheet question import into an assessment, and course or section duplication.
- The platform's own AI can draft a course outline. It cannot be the authority for course facts.

So a module cannot be handed to LearnWorlds as prose and become a course. It has to be built into
the shapes LearnWorlds already accepts. This contract defines a single markdown source file that a
build script can fan out into those shapes without a human interpreting anything.

## 2. The mapping

| OWOS artifact | LearnWorlds object | Build output |
| --- | --- | --- |
| Course workspace `apps/<course>/` | Course | course manifest |
| One governed module | One section | section manifest entry |
| One `##` heading block | One learning activity | per type, below |
| `owos-activity` type `ebook` | Ebook learning activity | `.docx` for Word import |
| `owos-activity` type `video` or `audio` | Video or Audio activity | media reference plus transcript `.docx` |
| `owos-activity` type `exam` or `self-assessment` | Assessment activity | `questions.xlsx` for question import |
| `owos-activity` type `html5` | HTML5 package activity | self contained `.zip` |
| `owos-activity` type `scorm` | Graded SCORM activity | SCORM 1.2 `.zip` with `imsmanifest.xml` |
| `owos-activity` type `pdf` | PDF activity | `.pdf` |
| `owos-activity` type `form` or `reflection-journal` | Form or Reflection Journal activity | prompt manifest |
| `owos-activity` type `external-link` or `embed` | External Link or Embed activity | URL manifest |

Because a section is flat, a module may not contain nested lesson groupings. If a module needs
sub-grouping, it is two modules. This is a hard structural limit of the platform, not a style
preference.

## 3. File identity

One module produces one source file:

```text
apps/<course>/curriculum/modules/module-NN-slug/MODULE-PACKAGE.md
```

It is generated from `MODULE-MANUSCRIPT.md` and must never be hand edited after generation. The
manuscript stays the human reading copy. The package is the machine copy.

## 4. Front matter

YAML front matter is required and must be the first bytes of the file.

```yaml
---
schema: owos-learnworlds-module/v1
courseId: ai-masterclass
moduleId: legacy:M00
moduleCode: M00
title: Orientation, Setup, and Your Learning Path
sectionTitle: Start Here, Orientation and Your Learning Path
status: research-draft
approvalState: proposed
approvalRecord: none
workProduct: One Water AI Learning Charter
seatTimeMinutes: 45
readingLevelTarget: grade-10
accessibilityTarget: WCAG-2.2-AA
registers:
  claims: research/CLAIMS-REGISTER.md
  sources: research/SOURCE-REGISTER.md
  evidenceBoundaries: research/EVIDENCE-BOUNDARIES.md
  placement: curriculum/modules/module-00-orientation-setup-learning-path/CONTENT-PLACEMENT-REGISTER.json
reviewers:
  utilityPractitioner: unassigned
  noviceLearner: unassigned
  accessibility: unassigned
  sourceVerification: unassigned
outcomes:
  - id: M00.O01
    verb: explain
    statement: Explain what One Water AI teaches, what it does not authorize, and where human accountability remains.
    evidence: M00.A02, M00.Q01
  - id: M00.O02
    verb: identify
    statement: Identify one real One Water problem that will anchor the learning.
    evidence: M00.A04, M00.X01
claims:
  - CLM-M00-001
  - CLM-M00-002
---
```

Rules:

- `status` must be one of `research-draft`, `blueprint-candidate`, `manuscript-candidate`,
  `production-candidate`, `release-candidate`. The words approved, production ready, public,
  complete, certified, and released are prohibited unless `approvalRecord` names a committed
  repository record.
- `approvalState` is `proposed` until an owner decision is recorded.
- Every outcome needs an `evidence` list naming the activity or question IDs that prove it. An
  outcome with no evidence is a validator failure. This is the backward design gate, enforced.
- `claims` lists every claim ID this module depends on. Every ID must exist in the claims register.

## 5. Activity blocks

Each `##` heading is one learning activity and must be immediately followed by a fenced
`owos-activity` block. No prose may appear between the heading and the block.

````markdown
## What this program does and does not authorize

```owos-activity
id: M00.A02
type: ebook
title: What this program does and does not authorize
placementRefs: [M00.02, M00.05]
outcomeRefs: [M00.O01]
estimatedMinutes: 6
```
````

`type` is a closed list, each value mapping to a real LearnWorlds activity:

`ebook`, `video`, `audio`, `pdf`, `presentation`, `embed`, `external-link`, `html5`, `scorm`,
`exam`, `self-assessment`, `form`, `reflection-journal`, `certificate`.

`id` matches `M<NN>.A<NN>` and must be unique and sequential within the module.
`placementRefs` must resolve to `contentId` values in that module's placement register. This is
what keeps the no-delete rule honest. If a placement record has no activity referencing it and its
disposition is retain or refine, the validator flags dropped content.

## 6. Question blocks

Questions live in fenced `owos-question` blocks and must reference an activity whose type is
`exam` or `self-assessment`.

````markdown
```owos-question
id: M00.Q01
activity: M00.A07
type: multiple-choice
outcomeRef: M00.O01
claimRefs: [CLM-M00-001]
stem: A vendor tells your utility that its model will decide which pumps to replace next year. Under this program's accountability rule, what is the correct reading of that statement?
options:
  - The model decides and staff implement the decision.
  - The model produces a ranked recommendation and a named person remains accountable for the decision.
  - The decision is automated, so accountability transfers to the vendor.
  - Accountability is shared equally between the model and the utility.
correct: 2
feedbackCorrect: Correct. The program teaches recommendation, not authority. A named human stays accountable for the capital decision.
feedbackIncorrect: Not quite. Review the accountability rule. A model can rank and recommend. It cannot hold accountability for a capital decision, and accountability cannot transfer to a vendor.
```
````

`type` closed list: `multiple-choice`, `multiple-response`, `true-false`, `fill-blank`,
`matching`, `ordering`, `open-ended`.

Rules:

- Every question needs `feedbackCorrect` and `feedbackIncorrect`. Retry with explanation is a
  design requirement, so silent scoring is a failure.
- Every question needs an `outcomeRef`. A question that proves no outcome does not belong.
- A full module needs at least three distinct question types.

## 7. Visual and interaction blocks

````markdown
```owos-visual
id: M00.V01
type: role-network
title: Who touches a One Water decision
altText: A network diagram showing an operator, an engineer, a finance analyst, a regulator, and a customer service representative all connected to a single pump replacement decision at the center.
sourceRefs: [SRC-012]
placementRefs: [M00.06]
```
````

`owos-visual` type closed list: `diagram`, `flow`, `matrix`, `role-network`, `timeline`,
`comparison`, `data-chart`, `map`, `annotated-screenshot`.

`owos-interaction` type closed list: `decision-branch`, `sorter`, `self-diagnostic`, `builder`,
`hotspot`, `comparison-table`, `scenario-walkthrough`.

Rules:

- `altText` is required on every visual, must be non-empty, and must not exceed 250 characters.
  This is the accessibility gate and the validator enforces it.
- A full module needs at least four distinct visual types and two purposeful interactions, unless
  the design brief records an approved exception in `approvalRecord`.
- The Learning Charter builder is an `owos-interaction` of type `builder` and is mandatory in M00.

## 8. Claim citation in prose

Every load bearing sentence carries its claim ID in square brackets at the end of the sentence.

> Utilities in the United States operate under a federal drinking water standard set by the Safe
> Drinking Water Act. [CLM-M00-004]

Rules:

- Every bracketed ID in the body must appear in front matter `claims`.
- Every ID in front matter `claims` must appear in the claims register with a support state.
- A claim whose register state is `verify` may appear only in a file whose `status` is
  `research-draft` or `blueprint-candidate`. It is a failure in a manuscript candidate or later.
- The evidence class, which is sourced fact, internal curriculum decision, Hardeep Anand position,
  instructional scenario, expert interpretation, or unresolved question, lives in the claims
  register. It is not repeated inline. One truth, one place.

## 9. Writing gates the validator enforces

- No em dash and no en dash anywhere. Use "to" for ranges and restructure the sentence otherwise.
- Every acronym defined on first use, checked by pattern for a parenthetical or preceding gloss.
- No banned marketing verbs in learner facing prose: guarantee, ensure compliance, certify,
  eliminate risk, transform, revolutionize, seamless, cutting edge, unlock, leverage as a verb.
- Sum of `estimatedMinutes` across activities must land within ten percent of `seatTimeMinutes`.
- Heading text and activity `title` must match exactly.

## 10. Build outputs

`tools/build_learnworlds_package.py` reads `MODULE-PACKAGE.md` and writes:

```text
apps/<course>/dist/learnworlds/module-NN-slug/
  section-manifest.json
  activities/M00.A01.docx
  activities/M00.A07-questions.xlsx
  activities/M00.A12.zip          (html5 or scorm only)
  assets/M00.V01.svg
  IMPORT-RUNBOOK.md
  conformance-report.json
```

`IMPORT-RUNBOOK.md` states the exact click path for the person loading the section into
LearnWorlds, because the platform has no API path for creating content. The runbook is part of the
deliverable, not an afterthought.

## 11. Order of operations

The package is generated last. It is generated from an approved manuscript, which is written from
approved claims, which come from verified sources. Generating the package earlier produces a well
formed file full of unverified content, which is worse than no file at all.

```text
GOAL -> PLAN -> evidence registers -> blueprint -> manuscript -> package -> conformance -> QA
```

No stage skips. No stage is marked complete by the authoring model. Each is recorded in
`production-status.md` and approved by a named human.
