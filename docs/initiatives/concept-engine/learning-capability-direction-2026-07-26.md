---
title: Shared Learning Capability and Continuing-Education Direction
date: 2026-07-26
status: IMPLEMENTATION AUTHORIZED
owner: Hardeep Anand
---

# Owner direction

Hardeep directed that Concept Briefs operate as focused one-module learning experiences under the
course destination. They must not become static articles. Concepts across drinking water,
wastewater, stormwater, and One Water should be explained through appropriate diagrams, dynamic
models, animation, interaction, learning checks, and applied transfer so professionals can learn
across sectors.

The Concept Brief and course compilers must not maintain duplicated visual or quiz catalogs. Updates
to shared components must flow to both engines from one authoritative registry.

Concept Briefs must preserve the complete connected product: Graph, Community, directory and vendor
relationships, commercial editorial firewall, completion evidence, accessibility, responsive
behavior, reduced motion, no-JavaScript meaning, verification, qualified review, and release
control.

The system should retain the evidence needed for a future continuing-education submission. It must
not claim credit or accreditor acceptance before current requirements and the exact offering are
approved.

# Standard names

- OWOS Course Engine
- OWOS Course Compiler
- OWOS Concept Engine
- OWOS Concept Brief Compiler

# Implementation decision

The authoritative capability registry is
`core/learning-capabilities/registry.yaml`. It connects the existing Visual Arsenal, component
catalog and gallery, and quiz catalog and gallery. Both compilers consume this registry. Product
packages contain capability identifiers and topic-specific configuration, not copied catalog
definitions.

The Concept Brief contract advances to `owos-concept-brief/2` because `learning.yaml` and
`assessments.yaml` become required governed records.
