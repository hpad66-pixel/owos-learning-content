---
title: OWOS Course Experience Architecture
version: 1.1.0
status: APPROVED IMPLEMENTATION STANDARD
owner: Hardeep Anand
effective: 2026-07-23
---

# OWOS Course Experience Architecture

This standard prevents an OWOS course from becoming a branded stack of repeated lesson templates.
It governs the course as a complete learner experience, not merely one module at a time.

## 1. Start with a course identity

Before module design, define the course's own:

- intellectual promise and central argument;
- conversational teaching voice;
- utility world, recurring people, assets, records, places, and decisions;
- visual language, including diagrams, illustration style, information density, color behavior, and motion;
- signature learning mechanisms that belong to this subject;
- professional artifacts learners will produce;
- emotional rhythm, including curiosity, surprise, tension, diagnosis, practice, synthesis, and confidence; and
- motifs, layouts, simulations, and interaction patterns the course will deliberately avoid.

OWOS navigation, accessibility, identity, evidence, and completion controls remain consistent. The
teaching surface does not. A course about project delivery should not feel like a course about data
governance. A course about semantic meaning should not look like either one.

## 2. The lesson must stand without video

The written lesson is the instruction. Video, narration, and animation are optional supplements.
Removing them must not remove the explanation.

Every material idea must be taught conversationally:

1. Begin with the learner's likely question or misconception.
2. Explain the idea in ordinary language.
3. Work through a specific utility example.
4. Expose the mechanism, relationship, calculation, or decision.
5. Explain what changed and why.
6. Show where the idea stops applying.
7. Ask the learner to use it.
8. Debrief the result in plain English.

Definitions, labels, tooltips, diagrams, and quiz feedback do not replace the teaching paragraphs.
Recording scripts are optional production artifacts and never count as lesson instruction.

## 3. Use lesson archetypes, not lesson templates

An archetype describes the learner's job and the arc of thought. It is not reusable page markup.
Examples include:

- field incident investigation;
- control-room timeline;
- guided construction;
- forensic record review;
- relationship discovery lab;
- query laboratory;
- model courtroom;
- validation clinic;
- architecture design studio;
- evidence reconciliation;
- executive decision room;
- map-based exploration;
- before-and-after diagnosis;
- scenario branch;
- worked case conversation; and
- capstone design review.

The course blueprint must use enough archetypes to create a real rhythm. For courses with:

- 1 to 5 lessons, use at least 3 archetypes;
- 6 to 10 lessons, use at least 4 archetypes;
- 11 to 16 lessons, use at least 5 archetypes; and
- 17 or more lessons, use at least 6 archetypes.

No archetype may dominate more than one third of a course without a written instructional reason.
Adjacent lessons may not share the same archetype, opening move, dominant visual, interaction
signature, quiz sequence, and work-product format.

## 4. Give every lesson a signature mechanism

Each lesson needs one mechanism learners will remember and could describe afterward. It might be:

- constructing and connecting triples;
- resolving five records that may or may not identify one pump;
- running a query and watching the answer path light up;
- admitting or rejecting an inference in a proof trace;
- repairing a failed Shapes Constraint Language validation report;
- reconciling an operating procedure with a sensor record and permit clause;
- changing latency, authority, and freshness constraints in an architecture decision; or
- stopping an agent when permission, evidence, or confidence is insufficient.

The signature mechanism must be specific to the lesson. "Click through four steps," "match terms,"
"select the governed answer," and "fill in eight fields" are generic control patterns, not signature
mechanisms.

## 5. Match visual grammar to the subject

Visual variation is not a quota. It is a consequence of choosing the right representation.

- Project delivery may naturally use plan views, schedules, dependency networks, cost curves,
  decision gates, field photographs, contract markups, and risk maps.
- Data governance may use evidence desks, record journeys, lineage maps, control boundaries,
  responsibility maps, quality profiles, and decision forums.
- RDF and knowledge graphs may use triple construction, identity bridges, animated graph growth,
  path illumination, query consoles, inference proofs, validation reports, semantic mappings, and
  context packet assembly.

Do not force four unrelated diagrams into a lesson to satisfy a count. A full lesson normally needs
two to five substantial explanatory visuals. One deep simulation may do more teaching than four
static graphics. Every selection must be justified by the idea's natural shape.

## 6. Assess the kind of thinking being taught

Do not impose the same quiz inventory on every lesson.

- Recognition may use a short choice or flip card.
- Relationship understanding may use matching, graph construction, or path tracing.
- Sequence may use ordering or a step-through.
- Judgment may use a scenario decision with consequences.
- Diagnosis may use error finding and repair.
- Application may use a calculation, query, model, design, or professional artifact.
- Synthesis may use a defended recommendation or review panel.

Every lesson needs checks at the point of teaching and a final applied demonstration. The number and
format follow the learning job. Repeating the same quiz sequence across more than two lessons is a
course-level release blocker.

## 7. Preserve consistency only where consistency helps

Keep these stable:

- OWOS identity and accessibility;
- predictable navigation;
- progress and completion semantics;
- evidence and attribution controls;
- keyboard, touch, mobile, and reduced-motion behavior;
- Graph and Community access; and
- honest release states.

Vary these deliberately:

- page composition;
- narrative opening;
- section rhythm and length;
- information density;
- dominant visual;
- learner action;
- simulation behavior;
- quiz sequence;
- work-product form;
- scenario cast;
- debrief structure; and
- visual mood inside the OWOS brand.

## 8. Course-level anti-repetition gate

Before a golden lesson is approved and after every three produced lessons, run:

```bash
python3 tools/course_distinctiveness.py --course apps/<course>
```

The gate examines the rendered lessons together. It checks declared archetypes, signature mechanisms,
opening patterns, visual sequences, quiz sequences, interaction signatures, work-product modes,
section and control-count clustering, repeated frequently asked questions, and adjacent structural
similarity.

A module can pass its own conformance test and still fail the course-level distinctiveness gate.
Both must pass before release.

## 9. Whole-course full-module evidence

The `lessons` object in `.course/experience-architecture.json` is also the authoritative source
lesson inventory for full-module conformance. Every included lesson must resolve to:

- its lesson HTML;
- one module design brief;
- one scored module QA report;
- the course full-module contract, or a declared lesson-specific contract; and
- its recording script when one is present or explicitly required.

Use the conventional directories `curriculum/`, `curriculum/design-briefs/`, `qa/`, and
`curriculum/scripts/`. A lesson may declare exact paths inside an `evidence` object when legacy
naming or a special production package requires an override. Evidence paths must remain inside the
course directory.

Before release, run:

```bash
python3 tools/course_full_conformance.py --release-ready --course apps/<course>
```

Passing the distinctiveness audit alone is never full-course conformance. Quality contract version 3
and later makes the whole-course runner a mandatory release gate. Working conformance may run without
`--release-ready`; that mode never grants release or substitutes for human approval.

## 10. Golden lesson rule

The golden lesson proves depth, credibility, accessibility, and usefulness. It does not establish:

- a standard number of sections;
- a standard page composition;
- a standard quiz order;
- a standard artifact form;
- a standard graphic set; or
- a standard interaction pair.

Production planning must demonstrate how the next three lessons differ from the golden lesson before
bulk production begins.

## 11. Failure conditions

The course fails experience review when:

- lesson files are generated from one large page function with content substituted into fixed slots;
- most lessons have nearly identical section, button, field, FAQ, visual, and quiz counts;
- the same quiz sequence appears throughout the course;
- instructor explanation is generic enough to move unchanged to another lesson;
- graphics are simple boxes, blobs, icon rows, or arrows that do not reveal the mechanism;
- the course changes color while preserving the same learning experience;
- simulations only reveal prewritten text and do not model a relationship, consequence, or decision;
- FAQs are generated by substituting vocabulary into repeated questions;
- every work product is the same form with different field labels; or
- a course-level audit is replaced by individual module pass results.

## 12. Release evidence

The release record must include:

- the approved Course Experience Brief;
- the completed Course Design Matrix;
- every approved module storyboard and visual manifest;
- the distinctiveness report;
- the whole-course full-module conformance result with per-lesson evidence paths;
- rendered desktop and mobile review evidence;
- rendered tablet review evidence;
- the completed course coherence report;
- at least one novice read-without-video review;
- a utility-practitioner review;
- course-specific visual and interaction review; and
- a list of intentional repetitions with their instructional reasons.
