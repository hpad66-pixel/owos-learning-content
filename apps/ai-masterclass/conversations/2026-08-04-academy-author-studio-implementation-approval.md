# Academy Author Studio implementation approval

**Date:** 2026-08-04

## Hardeep's direction

Hardeep approved the Academy Author Studio plan and instructed the team to build it. The product will
eventually use the branding of APAS.dev.

## Recorded architecture decision

- `owos-learning-content` remains the canonical home for curriculum, evidence, manuscripts, quality
  records, and generated curriculum artifacts.
- `onewater-os-platform` remains the canonical home for the protected application, authentication,
  workflow runtime, and internal Academy experience.
- No new Git repository is created.
- The legacy M00 through M63 curriculum is the source curriculum line.
- The Fellowship M1 through M64 curriculum is a curated program and delivery sequence.
- Namespaced IDs preserve both numbering systems without collision.

## Approved first implementation slice

- Build a deterministic two-line curriculum registry with source and output hashes.
- Connect the registry to the authenticated Author Studio.
- Provide an APAS.dev-inspired read-only command center with curriculum-line switching, grouped module
  browsing, search, filtering, metrics, and visible authority boundaries.
- Preserve existing production candidates and the Course Production Bible.

## Boundary

This approval does not authorize public deployment, curriculum editing, staff assignments, release
actions, Articulate production, credentialing, or learner-facing publication. Those capabilities
remain gated behind later role, checklist, workflow, and release decisions.
