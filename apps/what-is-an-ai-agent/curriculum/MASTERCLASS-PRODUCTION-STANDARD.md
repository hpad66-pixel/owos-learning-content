# AI Agent Master Class Production Standard

Version: 1.3

This standard captures the complete learner-facing quality contract established through Module 4 and applied to Modules 1 through 8. It implements the shared OWOS Course Production Contract for this Master Class and supplements the Course Operating Standard, Course Design System, Visual Arsenal, Writing Standard, component catalog, quiz catalog, and module QA template.

## Required module architecture

Every full module must include:

1. A recognizable water, wastewater, or stormwater situation with a real professional consequence.
2. An initial learner decision before the preferred answer is taught.
3. Plain-English instructor explanation before every major visual, simulation, assessment, and builder.
4. At least four meaningful visual types selected from the natural shape of the teaching ideas.
5. At least one original explanatory graphic or editorial illustration when a setting, physical asset, record relationship, mechanism, or decision path benefits from a picture.
6. At least two purposeful interactions that reveal sequence, cause, consequence, trade-off, failure, repair, or change.
7. Explicit Back, Step, Play, Pause, and Reset controls for any automatic or step-through process.
8. A visible event, result, state, or evidence record. Never represent private hidden model reasoning as a professional record.
9. At least three different quiz types distributed immediately after the ideas they measure.
10. Immediate explanatory feedback, unlimited review and retry, and deterministic answer keys where the result is scored.
11. A final applied assessment connected to a useful professional work product.
12. A same-page Knowledge Graph drawer that connects concepts, evidence, roles, controls, competencies, and work products.
13. Browser persistence for learner drafts and required activities.
14. Completion based on decision, interaction, assessment, and work-product evidence rather than scrolling.
15. Responsive mobile transformation, keyboard semantics, accessible names, live feedback, contrast review, and a reduced-motion equivalent.
16. Claim-level evidence identifiers and a visible instructional boundary.
17. A module recording script and an updated course-overview script.
18. A scored module QA report with separate automated, manual, practitioner, integration, benchmark, and release gates.
19. A module-specific FAQ before the evidence boundary that answers likely novice questions in plain English and uses utility examples, explanatory diagrams, comparisons, or worked sequences where useful.

## Instructor-led reading contract

Every module must feel like an instructor is present even when no video has been recorded.

- Introduce the utility situation in complete, conversational paragraphs.
- Explain the distinction or mechanism before asking the learner to use it.
- Place a visible reading guide before every explanatory graphic.
- Place a visible operating guide before every simulation or interactive control.
- Debrief the result in plain English and connect it to a utility decision.
- Explain the professional work product as a tool for real work, not as a course form.
- Define technical terms in ordinary language at the point where they first appear.
- Use bullets only for scannable details after the idea has been taught in prose.

Every module also carries an instructor bridge with four elements:

1. Two or more paragraphs that connect the lesson concepts.
2. A module-specific operating sequence with four visible stages.
3. A sentence the learner should be able to explain in their own words.
4. A direct connection to the professional work product.

The learner-facing HTML, shared runtime, and recording script must tell the same story.

## Lesson tools and community placement

Graph and community controls must not consume a full-width band at the top of a lesson.

- Desktop lessons use compact Graph, Community, and Start actions in the lesson header. Start moves directly to the beginning of the lesson.
- Mobile lessons keep those compact buttons in the header without creating a persistent bottom dock.
- Graph and Community each open in a white same-page drawer or dialog and return focus to the trigger that opened them.
- The complete learning community remains after the teaching content.
- Every landing page and module reserves `#owos-course-community` inside `main`, immediately before bottom navigation. This anchor is part of the source HTML and is not inferred from a generic wrapper.
- Closing the Community drawer returns the complete community to its original location at the bottom.
- Floating cards, hanging rails, and fixed side controls are prohibited.

This placement is shared across OWOS master classes. A course may change the labels, but not the behavior.

## Learner FAQ

Every module closes its teaching content with questions learners are likely to ask after completing that specific lesson.

- Answer the question directly before adding detail.
- Use conversational plain English and define technical terms.
- Ground each answer in a water, wastewater, or stormwater example.
- Add a small explanatory diagram, comparison, or worked sequence when the relationship is easier to see than to describe.
- Use accessible disclosure controls that work with keyboard, touch, and small screens.
- Place the FAQ before the evidence boundary, completion controls, bottom Graph and Community section, and previous or next navigation.
- Send questions not covered by the FAQ to the Community. Do not present an unverified community response as course instruction.

Do not copy a generic FAQ across modules. The questions must reflect the module's actual concepts, decisions, and likely misunderstandings.

## Contrast and typography gate

Light reading surfaces use dark text. Dark blue or brand-gradient surfaces explicitly set headings, paragraphs, labels, captions, and control text to white or a tested light color. Inherited text color is not accepted on dark surfaces. The shared runtime contrast guard checks dynamic content, and manual desktop and mobile inspection remains required.

The module must use the OWOS type family, a readable line length, calm heading weights, and enough spacing to distinguish teaching, practice, assessment, and work-product sections. A visual theme does not pass when typography is technically visible but tiring to read.

## Visual pacing

Do not place more than two consecutive full prose blocks without a meaningful visual, interaction, worked example, comparison, or instructor callout unless the module design brief records why uninterrupted prose is necessary.

A visual must teach. It should reveal a part, relationship, sequence, cause, quantity, comparison, status, place, or decision. Decorative stock photography, generic technology imagery, repeated icon rows, and color changes do not satisfy the standard.

Every explanatory graphic requires:

- a clear title;
- accessible text;
- a visible plain-English reading guide;
- a mobile transformation;
- a reduced-motion equivalent when movement carries meaning; and
- one conclusion the learner can explain.

## Distributed assessment

Assessments must appear where learning happens. A full module uses at least three varied types from the governed quiz library, such as classification, matching, ordering, scenario choice, multi-select, true or false, estimate, checklist, or reflection.

Reflection can deepen judgment, but it does not satisfy deterministic completion by itself. The final applied check must test the professional work product against explicit criteria.

## Work-product progression

The eight modules produce:

1. AI Terms Field Card
2. Agent Loop Trace
3. Agent Dependency and Readiness Map
4. Orchestration and Handoff Contract
5. Autonomy and Consequence Decision Record
6. Guardrail and Human-Authority Plan
7. Utility Agent Opportunity Portfolio
8. Utility Agent Canvas and 90-Day Pilot Brief

Each artifact remains a professional draft until an accountable utility reviewer accepts it.

## Diversity requirement

Module 4 is the minimum capability benchmark, not a page template. Adjacent modules must not repeat the same opening situation, narrative architecture, dominant visual, interaction pair, quiz sequence, work-product format, or mobile transformation without an instructional reason.

The current master class uses:

- Module 1: progressive system comparison and capability ladder
- Module 2: step-through operating loop and observable event sequence
- Module 3: functional cutaway and diagnostic repair laboratory
- Module 4: orchestration room, handoff packet, and failure propagation
- Module 5: autonomy spectrum and consequence matrix
- Module 6: layered-defense and permission laboratory
- Module 7: utility opportunity landscape and portfolio review
- Module 8: guided canvas, adversarial review, and pilot roadmap

## Release truth

A high working score does not authorize release. Qualified utility-practitioner review, novice-learner testing, real-device and assistive-technology review, authenticated OWOS and Supabase verification, benchmark approval, credential approval, and release approval remain separate recorded decisions.
