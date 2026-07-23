# OWOS Academy Visual Arsenal

The rule: **the visual comes from the idea, never from habit.** Do not reuse the same triangle,
curve, or bar chart in every chapter. Before you build a section, look at what the idea actually is,
then pick the visual from this arsenal that shows it best. If two ideas in a chapter would use the
same visual, change one of them so the chapter has variety.

Run the **Selection Prompt** (bottom of this file) first, every module. It looks at each teaching
point and picks the fitting visuals. Only then do you build.

**Copy, do not hand-roll.** Once you pick a visual, copy its exact markup, CSS, and JavaScript out of
`component-gallery.html`. Do not draw a simpler version by hand. If a module's diagram looks worse
than the one in the gallery, it is wrong. Also: spell out every acronym in full the first time it
appears (for example "Design-Build (DB)"), and give every term and acronym a hover tooltip. Use one
tooltip element per page, never a second `title`-attribute tooltip.

**Simulate, do not just describe.** If an idea is a *process, an algorithm, or something that unfolds
over time*, do not settle for a static diagram plus prose. Build an interactive that shows it happening:
a step-through with Play/Step/Back controls (like `cpmsim`, which derives the critical path live), a
live model the learner drives (`calc`, `triangle`, `recommender`), or a reveal (`tree`, `process`,
`spectrum`). If the learner still has to take your word for how the mechanism works, the section is not
done. When the needed interactive does not exist, build it into the shared library so every chapter can reuse it.

**Explain the graphic.** A learner should never be expected to decode a diagram alone. Introduce the graphic in plain English, tell the learner where to look first, explain the relationship or change, and state what the picture helps the learner conclude. A graphic that only decorates a heading does not count.

**Use an instructional test.** Before keeping a graphic, finish this sentence: "After reading this picture, the learner can explain..." If the sentence has no clear answer, remove the graphic or redesign it.

---

## How to choose: match the visual to the JOB the idea is doing

### Showing the parts of a whole, or a balance
| Visual | Shows | Use when | Utility / PM example | Interactive? |
|---|---|---|---|---|
| **Three-legged stool** | 3 parts that all must hold or it tips | exactly three balanced pillars | sustainability: environmental, social, economic | tip it when one leg is weak |
| **Pillars / columns** | 3 to 5 supports holding a roof | a few named foundations | the pillars of asset management | click a pillar |
| **Pyramid / hierarchy of needs** | layers that build on each other | maturity, priority, foundation-first | data before AI: data, then analytics, then AI | highlight a layer |
| **Layered stack** | tiers stacked, bottom enables top | architecture, tech stack | SCADA, historian, analytics, decision layer | peel a layer |
| **Venn (2 or 3 circles)** | overlap between groups | shared ground, intersection | where safety, cost, and schedule overlap | drag circles |
| **Donut / 100% stacked bar** | shares of one total | budget split, time split | where the capital dollar goes | hover a slice |

### Showing a process or a sequence
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Linear flow** | steps in order with arrows | a straightforward process | permit application steps | click a step |
| **Phase-gate flow** | phases with go/no-go gates between | staged delivery | the project life cycle | step through gates |
| **Swimlane** | who does what, across steps | handoffs between roles | design to bid to build, by party | highlight a lane |
| **Cycle / loop** | steps that repeat forever | continuous improvement, PDCA | plan-do-check-act, the weekly ritual | spin the loop |
| **Timeline / roadmap** | events along a time axis | milestones, program plan | 5-year capital plan | scrub the timeline |

### Showing a trade-off or a position
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **2x2 matrix** | items placed on two axes | prioritizing, categorizing | risk: likelihood vs impact; effort vs value | drag items into quadrants |
| **Iron triangle** | 3 forces locked together | scope-time-cost only | the triple constraint | move the corners |
| **Spectrum / slider scale** | a range between two ends | how much of something | predictive to agile | slide the marker |
| **Radar / spider** | one thing rated on many axes | profiles, readiness scores | AI readiness across 6 dimensions | move the points |

### Showing structure or relationships
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Network / wire diagram** | things connected by lines | systems, dependencies, graphs | the knowledge graph, a SCADA network | click a node |
| **Org / tree** | branching hierarchy | reporting, breakdown | the Work Breakdown Structure | expand a branch |
| **RACI grid** | who is R/A/C/I per task | decision rights | permit approvals by party | fill a cell |
| **Dependency arrows (Gantt-style)** | what waits on what | schedules | the critical path | drag a bar |

### Showing change over time
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Line graph** | a value moving over time | trend | non-revenue water by year | scrub |
| **S-curve / cumulative** | running total, slow-fast-slow | spend, progress | the cost-loaded schedule | slide inputs |
| **Burn-down / burn-up** | remaining vs done | tracking to a target | budget burn | live |
| **Before / after (slider)** | two states compared | the change a project makes | pipe condition before and after | drag the divider |

### Showing comparison or ranking
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Bar chart** | quantities side by side | compare amounts | spend vs get back; option A vs B | sort |
| **Comparison table** | options across criteria | decision matrix | DBB vs DB vs CMAR | score cells |
| **Tornado** | which input swings the result most | sensitivity | what drives the cost most | live |
| **Dot / gap plot** | current vs target | gaps | actual vs planned by workstream | live |

### Showing cause and effect, or a decision
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Fishbone (Ishikawa)** | causes feeding a problem | root cause | why did the main break | add a bone |
| **Driver tree** | how one number breaks into drivers | decomposition | what makes up non-revenue water | expand |
| **Decision tree / flow** | branching choices | if-this-then-that | is it a project? which delivery method? | walk the branches |

### Showing what is hidden, or a flow of quantity
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Iceberg** | small visible, large hidden | what lies beneath | the true cost of deferral | reveal below the line |
| **Funnel** | narrowing from many to few | filtering, conversion | proposals to shortlist to award | animate |
| **Sankey** | quantity splitting and flowing | where things go | water: produced, billed, lost | hover a flow |

### Showing status or a measure
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Gauge / dial** | one value against a range | a single metric | quality, confidence, capacity used | live |
| **KPI tiles** | a few headline numbers | dashboards | cost, schedule, safety at a glance | live |
| **Traffic-light / heat grid** | status across a matrix | risk register, RAG | workstreams by status | live |
| **Progress ring** | percent complete | completion | chapter progress, project percent | live |

### Showing place
| Visual | Shows | Use when | Example | Interactive? |
|---|---|---|---|---|
| **Map / corridor / plan view** | something in space | location, alignment | the pipe route, the service area | pan, click |

---

## The rule of variety
- Every module: use **at least 4 different visual types**, and no type more than once unless it truly earns it.
- If a section is just text and a quiz, ask "what is the shape of this idea?" and reach for the arsenal.
- Never default to the iron triangle or a curve because it is easy. Pick what fits.
- Do not allow more than two consecutive full prose blocks without a meaningful visual, interaction, worked example, comparison, or instructor callout. Document any necessary exception.
- Use an original editorial illustration when a utility setting, physical asset, group of records, or accountable decision is easier to understand as a scene. Every illustration needs a reading guide and a learner conclusion.

---

## The Selection Prompt (run this per module, before building)

```
You are designing an OWOS Academy module on: [CONCEPT / CHAPTER TITLE].

Here are the key ideas it needs to teach, in order:
1. [idea one]
2. [idea two]
3. [idea three]
... (list them all)

For EACH idea, do the following:
- Name the "shape" of the idea (parts of a whole? a process? a trade-off? cause and effect?
  change over time? a comparison? structure? status? hidden depth? place?).
- Pick the best-fit visual from the Visual Arsenal for that shape. Give the exact visual name.
- Say in one plain sentence why that visual fits this specific idea, with a water example.
- Say whether it should be interactive, and what the reader would do with it.
- Pick a suitable quiz type for that idea (classify, multiple choice, estimate, reflection, matching).

Hard rules:
- Do NOT reuse the same visual type twice in one module unless it genuinely fits better than anything else.
- Do NOT default to the iron triangle or a cash-flow curve out of habit. Choose from the whole arsenal.
- Aim for at least 4 different visual types across the module.
- Mark the visual pacing breaks and confirm that no long run of text remains unexplained.
- If an idea has no good visual, say so, and keep it as plain text plus a quiz instead of forcing a picture.

Output a short table: Idea | Shape | Visual | Why it fits | Interactive (what) | Quiz type.
Then list which visuals you will build, confirming they are varied.
```
