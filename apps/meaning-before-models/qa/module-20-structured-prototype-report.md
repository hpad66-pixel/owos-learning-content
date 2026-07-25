# Module 20 Structured Authoring and Interaction Prototype Report

## Candidate identity

- Module: One Water Knowledge Spine Lab: From Utility Question to Governed Action
- Structured package: `apps/meaning-before-models/modules/module-20-one-water-knowledge-spine-lab`
- Compiler: `owos-course-compiler/1`, version 1.1.0
- Structured source checksum: `7baddc5a423ef7f037fa84361b0d28126a782e5244bbd7f9ee7b0f4590ece962`
- Candidate state: interaction prototype
- Release ready: false
- Publication state: not requested

## Structured package evidence

The prototype contains:

- one approved lesson contract;
- one approved fifteen-beat storyboard;
- complete conversational teaching for all fifteen steps;
- seven original governed SVG visual assets;
- four new purposeful interaction components;
- thirty-eight scenario decisions across three decision laboratories plus a three-scenario iPhone prompt-to-graph simulator;
- eight distributed assessments;
- one Portable One Water Knowledge Spine Use-Case Configuration;
- twelve glossary terms;
- seven authoritative source records;
- explicit Module 19 handoff;
- explicit production, evidence, security, and authority boundaries.

## Compiler results

Validation command:

```text
python3 tools/course_compiler.py validate apps/meaning-before-models/modules/module-20-one-water-knowledge-spine-lab
```

Result: passed.

Build command:

```text
python3 tools/course_compiler.py build apps/meaning-before-models/modules/module-20-one-water-knowledge-spine-lab
```

Result: passed. Deterministic prototype created at `build/index.html`.

The compiler and shared runtime were extended with:

- `knowledge-spine-live-lab`;
- `graph-path-illuminator`;
- `scenario-transfer-lab`.
- `prompt-graph-simulator`.

These components use the governed structured-package contract and do not reuse Module 18's control-room identity.

## Rendered browser evidence

Browser command:

```text
NODE_PATH=/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules \
/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node \
apps/meaning-before-models/qa/module-20-prototype-browser-validation.cjs
```

| Mode | Runtime errors | Width containment | Visual instances | Images loaded | Purposeful components | Completion | Drawer focus | Motion |
|---|---:|---|---:|---|---:|---|---|---|
| Desktop, 1440 by 1000 | 0 | passed | 8 | passed | 12 | passed | passed | standard |
| iPad, 820 by 1080 | 0 | passed | 8 | passed | 12 | passed | passed | standard |
| iPhone, 390 by 844 | 0 | passed | 8 | passed | 12 | passed | passed | 0.01 ms maximum |

Eight visual instances appear because the Scenario Transfer Map is intentionally taught once at the opening and again during final transfer. Seven distinct governed visual assets exist.

Screenshots are stored under:

```text
apps/meaning-before-models/qa/rendered/module-20-prototype/
```

## Prototype findings

### Passed automated checks

- Twenty lesson contracts validate.
- Module 20 structured package validates.
- Deterministic compilation succeeds.
- All six distinct visual assets resolve and load.
- All completion identifiers have a producing component.
- All four new interaction components execute.
- The iPhone prompt-to-graph simulator executes wastewater, water, and stormwater fixed traces.
- The finale reveals seven governed stages before rendering the evidence answer.
- The answer labels its frozen snapshot, query, shapes, policy, role, and response template.
- All thirty-eight laboratory cases provide deterministic explanatory feedback.
- All distributed assessments and the work-product save path execute.
- Graph drawer opens, closes, and returns focus.
- Desktop, tablet, and phone have no horizontal page overflow.
- Phone uses a one-column laboratory sequence.
- Reduced-motion behavior passes the prototype threshold.
- No empty buttons appear.
- No runtime JavaScript errors remain.

### Repaired prototype defects

1. The first storyboard retained the design-review schema rather than the compiler storyboard schema. It was converted without changing the approved fifteen-step sequence.
2. The completion package lacked its plain-language completion rule. The rule was added.
3. The compiler did not yet recognize the three Module 20 interaction archetypes. Governed renderers and runtime bindings were added.
4. The first browser harness used outdated button labels and matching attributes. The harness was corrected to test the rendered controls.
5. The browser harness initially counted six distinct visuals rather than seven rendered instances and expected twelve components rather than the actual eleven rendered purposeful components. The test now distinguishes asset uniqueness from rendered instances.
6. The synthesis experience lacked a visible prompt-to-graph culmination. A governed iPhone simulator, original trace visual, responsive runtime, reduced-motion path, and deterministic-boundary explanation were added.

## Gates that remain open

- Owner review of the structured narrative and prototype interactions
- Practitioner review across water, wastewater, and stormwater
- RDF, SPARQL, SHACL, OWL, provenance, and semantic-architecture factual review
- Cybersecurity and operational-technology review
- Novice-learner observation
- Screen-reader review
- Physical iPhone and iPad review
- 200 and 400 percent zoom review
- Detailed visual readability and full-screen viewer implementation
- Export format and persistence review
- Module 19 to Module 20 course-coherence review
- Final scoring rubric
- Credential and release review

## Recommendation

Return the structured prototype to owner review. Do not replace the curriculum lesson, create a live course route, publish, issue completion authority, or mark final release approved.
