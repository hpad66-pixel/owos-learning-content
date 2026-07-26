---
title: OWOS Course Operating Standard
version: 2.2.0
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
| OWOS Learning Record Service (Supabase implementation) | Enrollment, progress, attempts, work-product evidence, competency records, and credential evidence |
| Knowledge Graph | Concepts, sources, roles, competencies, contributors, and semantic relationships |
| Cloudflare | Protected delivery, edge APIs, caching, and rate controls |

No runtime copy becomes the curriculum source of truth. No generator becomes the author of record.

For new courses and materially rebuilt modules, the curriculum source is the structured module
package. The Course Compiler produces deterministic delivery HTML from that package. Author Studio
edits the package, preserves source snapshots, and previews the compiled result. Neither tool may
invent instruction or promote a pending human gate.

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
11. A module-specific FAQ that anticipates novice questions and answers them in plain English with utility examples and visual explanation where useful.
12. A completion rule, recap, and connection to the next lesson.

Animations must teach a relationship, consequence, sequence, or change. Decorative motion does not
satisfy the interaction requirement. Reduced-motion behavior is mandatory.

## Lesson completion

### Instructor explanation and optional media

The learner-facing page must stand on its own when no video is available. Every major visual, animation, simulation, assessment, and work-product interface must include one or two visible instructor paragraphs. The paragraphs explain what the learner is seeing, what action to take, what to notice, why it matters in utility work, and what the result means. Add a debrief when a change or consequence needs interpretation. Tooltips define terms but never replace instruction.

Recording scripts are optional and follow the approved course modality plan. When a recording is
planned, visual directions must remain separate from spoken words. The learner-facing page still
carries the complete instruction.

Explanatory graphics are required when the teaching idea has a meaningful visual shape. Each graphic must clarify a concept, method, framework, relationship, sequence, comparison, or cause. The lesson must explain how to read it and what conclusion it supports. Decorative stock art and repeated icon tiles do not count toward visual quality.

Long lessons also require a visual pacing plan. Do not place more than two consecutive full prose blocks without a meaningful visual, interaction, worked example, comparison, or instructor callout unless the module brief records why uninterrupted prose is necessary. An original editorial illustration may break visual monotony only when it teaches a utility setting, asset, record relationship, or accountable decision and includes accessible reading guidance.

Distribute checks throughout the lesson. Place each check immediately after the idea or mechanism it
evaluates. Match the assessment to the thinking being taught, provide immediate explanatory feedback
and retry where appropriate, and finish with an applied check connected to the professional work
product. Do not rely on reflection alone for deterministic completion, and do not impose one quiz
sequence on every lesson.

End every module with an FAQ before the source boundary and bottom connected-learning section. Questions must come from the actual lesson's likely misunderstandings. Answers must be complete, conversational, and grounded in a utility example. Use an explanatory diagram, comparison, or worked sequence when prose alone leaves the relationship unclear. The FAQ supports proactive learning but does not replace the lesson's instructor explanation.

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
validates every chapter listed in `released_chapters` before it creates a manifest. Quality contract
version 3 and later must also declare `full_module_conformance_required: true`. The release builder
runs `tools/course_full_conformance.py` across every lesson included by the course experience
architecture and blocks release if a lesson, design brief, scored QA report, configured script, or
full-module contract is missing or nonconforming. Release-ready mode also blocks any unchecked manual
review, non-passing hard gate, or QA report without an explicit Release approval record.

The release is also blocked when any released lesson has:

- fewer than two purposeful interactions;
- malformed interactive-component JSON or an invalid table or deterministic multi-select shape;
- an `undefined` sentinel that could reach the learner interface;
- no mobile viewport or responsive layout rule;
- no reduced-motion behavior;
- no accessible live-feedback region; or
- no keyboard-operable learner control.

For a fully migrated structured course, the release builder also validates every module package. It
blocks unresolved visual assets, unknown component identifiers, missing storyboard approval,
missing completion producers, unsupported assessment contracts, mismatched module identifiers, and
pending release-ready visual or QA states.

The lightweight lesson gate is a minimum technical floor. The whole-course conformance gate proves
that module evidence exists and passes the automated contract. Neither gate replaces qualified
utility-practice review, source review, learning-design judgment, contrast inspection, learner pilot,
or explicit release approval. Future course templates carry contract version 3 by default. Legacy
contract versions remain readable, but must migrate to version 3 before claiming this stronger gate.

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
- The shared OWOS learning-record, credential, and pathway contract, including canonical xAPI
  events, cmi5 or the governed SCORM 2004 adapter, fail-closed issuance gates, and learner-controlled
  deepen, reskill, and cross-skill recommendations.
- Complete provenance and an explicit instructional evidence boundary.

After approval, Chapters 10 through 24 use this lesson as their implementation benchmark. Chapters
00 through 08 are retrofitted only where they fail the standard. Project Delivery keeps its 21 lessons
and receives the missing provenance, event, graph, competency, and release controls.

## Release path

```text
controlled evidence
-> syllabus and course record
-> module design brief and approved storyboard
-> structured module package and visual manifest
-> deterministic Course Compiler output
-> five-gate review
-> rendered experience and course coherence evidence
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
