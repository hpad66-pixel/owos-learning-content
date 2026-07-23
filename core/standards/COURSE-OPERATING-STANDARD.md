---
title: OWOS Course Operating Standard
version: 2.0.0
status: APPROVED
owner: Hardeep Anand
approved: 2026-07-22
---

# OWOS Course Operating Standard

`COURSE-PRODUCTION-CONTRACT.md` is the binding completeness and release contract. Read it first. This operating standard explains the systems and gates behind that contract.

## Decision

Every OWOS course combines the strongest parts of the existing Master Classes:

- Project Delivery supplies the learner-experience benchmark: human teaching, utility scenarios,
  purposeful interaction, simulations, and applied decisions.
- Data Before AI supplies the production benchmark: controlled sources, explicit method versions,
  machine-readable course records, release states, checksums, and evidence boundaries.
- Hardeep Soul supplies the authoring benchmark when Hardeep's knowledge is used: natural voice,
  source discipline, argument quality, and approval control.
- One Water OS supplies identity, delivery, learner state, the in-lesson Knowledge Graph, competency
  evidence, and credentials.

The courses do not share subject matter. They share one operating system for producing trustworthy,
useful learning.

## System ownership

| System | Owns |
| --- | --- |
| `hardeep-soul` | Hardeep's source knowledge, voice, books, articles, and author approval |
| Controlled method repository | Versioned method, criteria, evidence, and technical authority |
| `owos-learning-content` | Curriculum, lesson sources, interactions, assessments, work products, and release packages |
| `onewater-os-platform` | OWOS Learn delivery, authentication, graph panel, and transaction APIs |
| Supabase | Enrollment, progress, attempts, work-product evidence, competency records, and credentials |
| Knowledge Graph | Concepts, sources, roles, competencies, contributors, and semantic relationships |
| Cloudflare | Protected delivery, edge APIs, caching, and rate controls |

No runtime copy becomes the curriculum source of truth. No generator becomes the author of record.

## Required lesson journey

Every released lesson contains these eleven elements in a coherent experience:

1. A consequential utility situation that establishes why the lesson matters.
2. An initial learner decision before the full framework is taught.
3. One clear mental model or relationship map.
4. Plain-language teaching grounded in the controlled sources.
5. An in-lesson Knowledge Graph view connected to the current concepts.
6. At least one purposeful interaction or simulation that reveals cause and effect.
7. Foundation, Practitioner, and Leader perspectives when the decision changes by role.
8. An applied exercise that produces a usable work product.
9. Knowledge checks with immediate explanatory feedback.
10. A source map, evidence boundary, and honest release status.
11. A completion rule, recap, and connection to the next lesson.

Animations must teach a relationship, consequence, sequence, or change. Decorative motion does not
satisfy the interaction requirement. Reduced-motion behavior is mandatory.

## Lesson completion

### Instructor explanation and recording package

The learner-facing page must stand on its own when no video is available. Every major visual, animation, simulation, assessment, and work-product interface must include one or two visible instructor paragraphs. The paragraphs explain what the learner is seeing, what action to take, what to notice, why it matters in utility work, and what the result means. Add a debrief when a change or consequence needs interpretation. Tooltips define terms but never replace instruction.

Every module must include a complete recording script. Every course must include one overview script that explains all modules in order. Visual directions are separate from spoken words. A curriculum change that affects the lesson sequence requires an overview-script update.

Explanatory graphics are required when the teaching idea has a meaningful visual shape. Each graphic must clarify a concept, method, framework, relationship, sequence, comparison, or cause. The lesson must explain how to read it and what conclusion it supports. Decorative stock art and repeated icon tiles do not count toward visual quality.

Long lessons also require a visual pacing plan. Do not place more than two consecutive full prose blocks without a meaningful visual, interaction, worked example, comparison, or instructor callout unless the module brief records why uninterrupted prose is necessary. An original editorial illustration may break visual monotony only when it teaches a utility setting, asset, record relationship, or accountable decision and includes accessible reading guidance.

Distribute quizzes and checks throughout the lesson. Place each check immediately after the idea or mechanism it evaluates. Use at least three different quiz types in a full module, provide immediate explanatory feedback and retry, and finish with an applied check connected to the professional work product. Do not rely on reflection alone for deterministic completion.

Page scroll is not completion. A lesson declares its requirements in the course record and records
completion only when the required evidence exists.

The default rule is:

```text
required teaching sections viewed
+ required interaction completed
+ required knowledge check passed
+ required work product saved
= lesson complete
```

The platform records the supporting events in Supabase. The event vocabulary is designed so that it
can later be emitted as xAPI statements to a Learning Record Store. Native OWOS HTML remains the
primary experience. cmi5 is the preferred packaged interoperability target. SCORM is an optional
compatibility export for legacy systems and is not the OWOS authoring format.

## Course production gates

### Module quality-control report

After every module build or material revision, complete `core/templates/MODULE-QA-REPORT.md`. Score the module out of 100 across instructor teaching, learning design, explanatory graphics, interactions, utility credibility, assessment, work product, accuracy and evidence, accessibility and responsive behavior, and platform integration.

The report also records the five production gates, automated evidence, manual reviews, missing work, and required revisions. The numeric score never overrides a blocked accuracy, utility-practitioner, technical and accessibility, or release gate. A module may receive a conditional working pass while remaining blocked from production or release.

Every lesson passes five visible gates:

1. **Accuracy:** claims, sources, method version, scope, and limitations are correct.
2. **Learning design:** outcomes, scenario, mental model, interaction, feedback, and work product are complete.
3. **Utility practice:** a qualified reviewer confirms that the decisions and artifacts are credible in practice.
4. **Technical quality:** accessibility, keyboard use, mobile layout, reduced motion, deterministic scoring,
   graph identifiers, and learner events pass.
5. **Release control:** stable identifiers, checksums, manifest, intake receipt, review, and deployment state pass.

No lesson may claim release, mastery, certification, or assurance before the relevant gate passes.

## Machine-enforced release gate

The course record must declare `quality_contract.enforce_on_release: true`. The release builder
validates every chapter listed in `released_chapters` before it creates a manifest. A release is
blocked when any released lesson has:

- fewer than two purposeful interactions;
- malformed interactive-component JSON or an invalid table or deterministic multi-select shape;
- an `undefined` sentinel that could reach the learner interface;
- no mobile viewport or responsive layout rule;
- no reduced-motion behavior;
- no accessible live-feedback region; or
- no keyboard-operable learner control.

This gate is a minimum technical floor. It does not replace the qualified utility-practice review,
source review, learning-design judgment, contrast inspection, or learner pilot. Future course
templates must carry the contract by default. A course cannot opt out when it is released.

## Golden lesson

Data Before AI Chapter 09, **D02: Accountability and Stewardship**, is the first golden hybrid lesson.
It proves the complete standard without rewriting released chapters prematurely.

The golden lesson must implement:

- Riverbend's lead-service-line inventory as the consequential decision.
- Criteria D02.1 through D02.5 from the controlled Version 2.3 method.
- A role and authority simulation.
- A segregation-of-duties decision exercise.
- An ownership and stewardship operating-pack builder.
- An evidence tracker and deterministic knowledge checks.
- In-lesson graph concepts and competency identifiers.
- Supabase enrollment and completion events.
- Complete provenance and an explicit instructional evidence boundary.

After approval, Chapters 10 through 24 use this lesson as their implementation benchmark. Chapters
00 through 08 are retrofitted only where they fail the standard. Project Delivery keeps its 21 lessons
and receives the missing provenance, event, graph, competency, and release controls.

## Release path

```text
controlled evidence
-> syllabus and course record
-> product-specific lesson source
-> interaction and work-product build
-> five-gate review
-> self-contained distribution
-> checksum release manifest
-> platform intake pull request
-> OWOS Learn deployment
-> Supabase learning evidence and Knowledge Graph relationships
```

The platform intake must always identify the exact curriculum repository and commit. Manual copying
is not a governed release.

## Acceptance checklist

- [ ] The lesson satisfies all eleven lesson elements.
- [ ] The learner produces or practices a professional work product.
- [ ] Every scored response is deterministic and explains the result.
- [ ] Every material claim has a source or is clearly marked as an instructional scenario.
- [ ] Graph concept and competency identifiers resolve.
- [ ] Supabase event identifiers are stable and idempotent.
- [ ] Dark backgrounds use light text and pass contrast review.
- [ ] Keyboard, touch, mobile, and reduced-motion behavior pass.
- [ ] The machine-enforced quality contract passes for every released lesson.
- [ ] No prohibited punctuation or generic artificial-intelligence phrasing appears.
- [ ] The release manifest, intake receipt, review state, and deployment state are visible.
