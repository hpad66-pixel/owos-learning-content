# Meaning Before Models Structured Authoring Migration Plan

## Decision

Module 01 now uses compiled structured source in the curriculum and live-review distribution after
explicit owner approval. The existing live-review HTML remains available for Modules 02 through 18
while each lesson is rebuilt as a structured module package. A compiled candidate replaces each
remaining live lesson only after its package, behavior, rendered evidence, and owner review pass.

## Reference conversion

Module 01 is the first reference package:

- governed narrative in `modules/module-01-rdf-in-15-minutes/module.yaml`;
- approved reference storyboard in `storyboard.yaml`;
- three actual, original visual assets with a visual manifest;
- a triple builder and evidence-path tracer with explicit completion contracts;
- multiple choice, working flip cards, path judgment, and an applied Relationship Card;
- primary World Wide Web Consortium sources and a module glossary;
- deterministic compiler output in `build/index.html`; and
- QA gates that remain honest about pending human review.

## Migration order

1. Retain Module 01 as the versioned reference package under `owos-course-compiler/1`.
2. Complete its remaining factual, practitioner, novice, and screen-reader review for final release.
3. Convert Modules 02 through 04, then run the course distinctiveness and coherence checks.
5. Convert Modules 05 through 18 in three-module review batches.
6. Build a complete release candidate and compare it with the existing live-review release.
7. Replace the runtime only after explicit release approval.

## Prevention

Future course scaffolds start with structured authoring enabled. The compiler rejects unresolved
visual labels, missing assets, unknown components, missing completion evidence, unsupported
assessments, prohibited punctuation, mismatched module identifiers, and unapproved storyboards.
Release-ready mode also rejects pending visual and human QA gates.
