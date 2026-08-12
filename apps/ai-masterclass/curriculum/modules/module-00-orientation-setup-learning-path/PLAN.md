# PLAN: Module M00, Orientation, Setup, and Your Learning Path

Companion to `GOAL.md`. Research draft, proposed only. Execution of stages 3 and later is blocked
until the six decisions in `GOAL.md` section 7 are recorded.

---

## 1. Source inventory and extraction

M00 is unusual. It is almost entirely internal. That is a finding worth stating plainly, because it
means the research effort belongs on placement fidelity and boundary language rather than on
external citation hunting.

| Source | Type | Use in M00 | Extraction step |
| --- | --- | --- | --- |
| `MODULE-GUIDANCE.json` | governed curriculum | outcomes, scope boundary, definition of done | already extracted into `GOAL.md` |
| `STAFF-DIRECTION.md` | governed curriculum | required teaching sections, rejection conditions | mapped to activity list in section 4 |
| M00 design brief | governed curriculum | concept to experience plan, FAQ plan, recording script | mapped to visual, interaction, and assessment plans |
| `CONTENT-PLACEMENT-REGISTER.json` | governed curriculum | 48 placement records | full reconciliation in section 3 |
| `COURSE-BRIEF.md` | governed curriculum | audience, series rule, five non negotiable module outcomes | boundary language for what the program does not authorize |
| `EVIDENCE-BOUNDARIES.md` | governed curriculum | what is not yet approved | copied into the module evidence boundary section |
| `INT-002`, Shreya | registered contributor input | `STF-002`, `STF-007`, `STF-008` placement | preserve provenance, route per register, never cite as technical authority |
| Cornell CTI | external framework | backward design rationale | design rationale only, not learner facing |
| UIC CATE | external framework | outcome verbs, Bloom | design rationale only |
| CAST UDL 3.0 | external framework | multiple means of representation, action, engagement | design rationale only |

**External sources still to acquire, and only these.** M00 needs primary authority for a very small
set of load-bearing claims. Each requires exact title, issuing organization, date, direct link, and
section locator.

1. The accessibility conformance standard the module claims to meet, W3C WCAG 2.2, cited to the
   published recommendation with the specific success criteria referenced.
2. Any statement M00 makes about what a large language model does with submitted text, if the module
   makes one. Recommendation, it should not. Route that to M01 and keep M00's boundary rule as a
   program policy statement instead of a technical claim about vendor behavior.
3. Nothing else. If a fourth external claim appears during drafting, that is a signal the module has
   drifted into teaching AI, which is M01's job.

## 2. Claim verification plan

1. Draft every intended claim into `research/CLAIMS-REGISTER.md` with an ID in the form
   `CLM-M00-NNN` before any prose is written. Prose cites IDs. Prose does not introduce claims.
2. Assign each claim exactly one evidence class: sourced fact, internal curriculum decision, Hardeep
   Anand position, instructional scenario, expert interpretation, or unresolved question.
3. Expected distribution for M00, which is itself a check. If more than roughly three claims come
   back as sourced fact, the module has probably drifted out of orientation and into instruction.
4. Every sourced fact gets current United States primary authority with an exact locator. No vendor
   page, marketing page, search snippet, or AI summary is admissible.
5. Anything unsupported or conflicting is marked `VERIFY` with a written statement of what evidence
   is missing and who must supply it.
6. The validator blocks any `VERIFY` claim from surviving into a manuscript candidate. This does not
   require anyone to remember the rule.

## 3. Content scrub and placement reconciliation

All 48 records reviewed. Nothing deleted. Nine current sections, four proposals, 32 proposal
subtopics, three contributor inputs.

**Nine current sections, all destined for M00.**

| ID | Title | Disposition | Rewritten learning job |
| --- | --- | --- | --- |
| M00.01 | By the end of this module | refine | replace broad orientation language with the seven observable outcomes |
| M00.02 | How this course works | retain | shared curriculum, role lens, evidence, assessment, support model |
| M00.03 | Getting set up | refine | universal access only, technical setup routed out |
| M00.04 | The placement diagnostic | refine | becomes a support routing baseline, no scoring language |
| M00.05 | The rules of the road | refine | becomes the participation, evidence, privacy, and authority contract |
| M00.06 | Role takeaways | refine | becomes the role lens selection and the role to decision network |
| M00.07 | Glossary | retain | pending decision D6, module glossary or course wide |
| M00.08 | Now you're ready | refine | becomes completion criteria plus the first accountable action |
| M00.09 | Sources | retain | becomes the evidence boundary and source map |

**Four proposals, preserved, none universal.**

| ID | Title | Disposition | Destination |
| --- | --- | --- | --- |
| M00.P01 | The terminal, from zero | optional preparation | M40, Builder Readiness |
| M00.P02 | API keys and the .env file | cross-reference | M25, security preview only in M00 |
| M00.P03 | Code editor setup | optional preparation | M40 |
| M00.P04 | Get an API key without a surprise bill | consolidate under M00.P02 | blocked by decision D2 |

The 32 subtopics inherit their parent's disposition and keep their IDs. None appears as required M00
setup. This is the staff direction rejection condition, so it is also a build failure, not a
preference.

**Three contributor inputs, provenance preserved.**

| ID | Contributor | Disposition | Destination | M00 treatment |
| --- | --- | --- | --- | --- |
| STF-002 | Shreya, via INT-002 | cross-reference | M25, secondary M40 | named in the optional preparation map only |
| STF-007 | Shreya, via INT-002 | optional preparation | M34, secondary M16 | light format diagnostic item in M00 |
| STF-008 | Shreya, via INT-002 | optional preparation | M40 | named in the optional preparation map only |

**Reconciliation check.** Every record dispositioned into M00 must be referenced by at least one
activity in the package file. Validator rule `PLC-003` fails the build otherwise, and it was proven
to fire during the Stage 0 self test.

## 4. Backward design alignment

Read this table right to left. Evidence was chosen first, then assessment, then activity, then
teaching. That order is the method, not a formatting choice.

| Outcome | Teaching | Learner activity | Feedback and assessment | Completion evidence |
| --- | --- | --- | --- | --- |
| O01 program boundary | what One Water AI is and does not authorize | read plus inspect the recommendation compared with decision view | flip card addressing the entry misconception that AI decides | orientation acknowledgement plus scenario question |
| O02 anchor problem | how to choose an anchor problem | draft the anchor problem in the charter builder | prompted revision against a specificity test | anchor problem field, role connected |
| O03 readiness | how to complete and read the baseline | six dimension self diagnostic | plain language support routing, never a score | diagnostic complete plus written interpretation of one need |
| O04 pathway | how pathway emphasis works | pathway decision tree | scenario multiple choice on reasoning | pathway selection event |
| O05 boundaries | protecting sources, privacy, and authority | information boundary sorter | classify and retry with explanation | boundary check passed |
| O06 charter | how to complete the charter | builder with preview, revise, save | field completeness check with named gaps | saved charter, all eight fields |
| O07 optional preparation | where to find help and technical preparation | optional preparation map | true or false on entry requirements | question passed |

Ten required teaching sections from staff direction map onto this without remainder. The FAQ and the
evidence boundary are sections nine and ten and are not assessed.

## 5. Universal Design for Learning plan

The rule is multiple ways in, one standard out. Options change how a learner receives and expresses
learning. They never lower the completion standard.

**Representation.** Every visual carries alt text, a reading guide, and a stated learner conclusion.
Every animation has a reduced motion equivalent that shows all relationships as a numbered map.
Narration is captioned and transcripted, and the transcript is a first class activity rather than an
accessibility afterthought. Every acronym is defined at first use, including artificial intelligence,
application programming interface, and any water sector acronym in an example.

**Action and expression.** The charter accepts typed entry, and where the platform allows it, an
uploaded or spoken equivalent. The anchor problem may be expressed as a sentence, a short scenario,
or a labeled decision. Field completeness is the standard, not format.

**Engagement.** The learner chooses their own anchor problem and role lens, which is the engagement
mechanism. Role examples span drinking water, wastewater, stormwater, reuse, administration, finance,
engineering, and public leadership so no professional reads the module as written for someone else.

**Mobile and input.** The role network becomes a role selector with a relationship list. The
diagnostic and charter stack vertically. Keyboard, touch, focus order, contrast, and focus return
after drawer dismissal are tested before, not after.

## 6. Role and One Water example plan

One utility problem, seen from every professional door. The design brief names the cross functional
morning meeting as the editorial illustration, and the examples should reinforce that single scene
rather than scatter.

| Lens | Anchor example | The decision at stake |
| --- | --- | --- |
| Operations | repeat overflow at one lift station | which alarm to trust on a night shift |
| Maintenance and planning | pump rehabilitation sequencing | which asset goes first with a fixed budget |
| Engineering | inflow and infiltration in one basin | which basin to model and which to inspect |
| Stormwater | recurring drainage complaints after rain | whether the complaint pattern is a system defect |
| Drinking water quality | distribution system sampling pattern | where to sample next and why |
| Reuse | permit condition monitoring | whether a reporting obligation is being met |
| Finance | rate case defensibility | whether the capital request survives scrutiny |
| Administration and customer service | complaint routing and response | what a caller is told and by whom |
| Executive and elected | resilience across jurisdictions | what to commit to publicly |

Each example connects to a real decision, record, asset, service, or public consequence. Generic
examples are a rejection condition.

## 7. Visual and interaction plan

Minimum four visual types and two interactions, enforced. The design brief already selected five
visuals and two interactions, so the plan is to build what is specified rather than reopen it.

| Element | Type | Teaching job | Mobile behavior |
| --- | --- | --- | --- |
| Role and decision network | role-network | no role acts alone on a One Water decision | role selector plus relationship list |
| Readiness profile | matrix or radar | readiness is uneven and supportable | vertical stack |
| Pathway decision tree | flow | a pathway is emphasis, and it reconnects | vertical stack |
| Information boundary sorter | comparison plus interaction | uncertainty triggers review, not guessing | full width cards |
| Charter anatomy | diagram | each field creates a future review point | vertical stack |

| Interaction | Type | Behavior |
| --- | --- | --- |
| Readiness diagnostic | self-diagnostic | six dimensions, support routing output, no score shown |
| Learning Charter builder | builder | draft, preview, revise, save, versioned |

No decorative imagery. Every visual needs a teaching job, reading guide, learner conclusion, alt
text, phone behavior, and reduced motion equivalent before it is built.

## 8. Assessment and feedback plan

Assess only the non negotiable outcomes. Four distributed checks, each with immediate explanatory
feedback and retry. Three distinct question types minimum, enforced.

| Location | Type | Outcome | Feedback |
| --- | --- | --- | --- |
| After the program promise | question flip card | O01 | corrects the entry misconception that a model decides |
| After information boundaries | classify and retry | O05 | explains why each item lands where it lands |
| After pathway selection | scenario multiple choice | O04 | explains why emphasis is not a separate curriculum |
| At charter completion | applied work product check | O02, O06 | names which fields are incomplete and why each matters |

Explicitly not completion: scrolling, time on page, self reported confidence, diagnostic score.

## 9. Learning Charter work product plan

Eight fields, versioned, learner owned, exportable, readable by later modules and the capstone.

Build path is blocked by decision D4. Two candidate paths, with the tradeoff stated:

- **Platform native.** LearnWorlds Form or Reflection Journal activity. Fast to build. Produces no
  versioning, no export, and no clean read path for later modules. Not recommended.
- **Packaged activity.** HTML5 or SCORM activity that renders the builder, saves locally, exports a
  file, and reports a completion event to the platform. More build effort. Produces an artifact the
  learner actually owns and the Fieldbook can hold.

Recommendation is the packaged path, because the charter is the module's entire reason to exist and
a record nobody can export is not a work product. Owner decision required.

## 10. Writing, recording, and production steps

1. Write `MODULE-MANUSCRIPT.md` from approved claim IDs only. Voice, one experienced instructor
   speaking to one intelligent professional who is new to the program. Full sentences. Every acronym
   defined at first use. One analogy maximum, and only where it clarifies.
2. Generate `MODULE-PACKAGE.md` from the manuscript per the import contract.
3. Run `validate_learnworlds_package.py`. Zero failures required.
4. Build the recording script at `curriculum/scripts/module-00-orientation-setup-learning-path-video-script.md`,
   10 to 14 minutes excluding activities, opening on the learner facing a large curriculum.
5. Build the LearnWorlds section outputs: Word files for ebook activities, a question spreadsheet for
   assessments, packaged activities for the diagnostic and the charter builder, and the import runbook.
6. Articulate, if used, drafts only from the approved import package and decides nothing.
7. Test keyboard, touch, phone, reduced motion, contrast, focus order, feedback, retry, save, return,
   and completion. Record the exact source revision used for any build.

## 11. Review gates and accountable roles

| Gate | Accountable role | Blocks | Status |
| --- | --- | --- | --- |
| Blueprint lock | owner, Hardeep Anand | manuscript | pending, six decisions open |
| Source and claim verification | source verification reviewer | manuscript | unassigned |
| Placement approval | owner | package build | proposed only |
| Utility practice review | qualified utility practitioner | production candidate | unassigned |
| Novice learner review | novice learner reviewer | production candidate | unassigned |
| Accessibility review | accessibility reviewer | production candidate | unassigned |
| Conformance | automated validator | release candidate | ready to run |
| Release | owner | everything | not authorized |

Three reviewer roles are unassigned. This is the critical path.

## 12. Definition of done

M00 is a release candidate only when all of the following are true and recorded:

1. Every one of the seven outcomes has completion evidence that resolves to a real ID.
2. All 48 placement records are dispositioned, referenced or routed, and none deleted.
3. Every claim carries an evidence class and a support state, and no claim is marked VERIFY.
4. Every external load-bearing claim has primary authority with an exact locator.
5. The validator returns zero failures.
6. Four named humans have signed the source, practitioner, novice learner, and accessibility gates.
7. The charter builder produces a saved, versioned, exportable eight field record.
8. Marketing language contains no promise of promotion, savings, compliance, certification,
   implementation success, or mastery.
9. `production-status.md` reflects every stage honestly.
10. The owner has recorded a release decision in `APPROVALS.md`.

Until item 10 exists as a committed record, M00 is not approved, not production ready, not public,
not complete, not certified, and not released.

---

**Stop point.** Per the governed sequence, work halts here. Stage 2, the evidence pass, begins when
the six decisions in `GOAL.md` section 7 are recorded.
