---
title: OWOS Shared Learning Capability Standard
version: 1.1.0
status: APPROVED IMPLEMENTATION DIRECTION
owner: Hardeep Anand
effective: 2026-07-26
---

# OWOS Shared Learning Capability Standard

## Standard engine names

- **OWOS Course Engine** is the multi-module course lifecycle. Its deterministic renderer is the
  **OWOS Course Compiler**, governed by `owos-course-compiler/1`.
- **OWOS Concept Engine** is the one-module Concept Brief lifecycle. Its deterministic renderer is
  the **OWOS Concept Brief Compiler**, governed by `owos-concept-brief/2`.

These names must be used in activation prompts, documentation, administrative interfaces, QA
reports, and release records.

## One capability source

Both engines consume `core/learning-capabilities/registry.yaml`. The registry points to the Visual
Arsenal, component catalog and gallery, and quiz catalog and gallery. A capability is defined once.
A new or revised component becomes available to both engines only after its shared registry record,
accessible implementation, responsive behavior, reduced-motion equivalent, no-JavaScript meaning,
tests, and documentation are updated.

Product packages select capabilities by stable identifier. They do not copy the catalog definition
into a course or Concept Brief. Topic-specific configuration, teaching explanation, evidence, and
review remain in the package.

## Concept Brief learning floor

A full Concept Brief is one module of focused learning, not a long article. Its approved storyboard
must normally provide:

1. at least two substantial explanatory visuals;
2. at least one dynamic explanation that lets the learner step, play, compare, manipulate, trace, or
   diagnose how the concept works;
3. at least two distributed learning checks;
4. immediate explanatory feedback and retry;
5. one final applied check;
6. deterministic completion evidence;
7. a cross-sector connection when the mechanism transfers across water, wastewater, and stormwater;
8. same-page Graph and Community context; and
9. governed directory, contributor, and commercial connections with the editorial firewall intact.

An approved exception is allowed only when animation or interaction would distort the concept. The
exception must explain how the same change, cause, sequence, or relationship is taught more
accurately.

## Motion and interaction

Motion must reveal change, cause, consequence, sequence, dependency, or hidden structure. It cannot
be ornamental. Every dynamic mechanism must expose:

- the model boundary and illustrative status;
- authored inputs, outputs, and failure states;
- keyboard, touch, focus, and live-feedback behavior;
- mobile composition;
- reduced-motion state;
- no-JavaScript and structured-text equivalent;
- deterministic completion evidence; and
- qualified review where the behavior represents engineering, operations, health, safety,
  compliance, or environmental consequences.

## Assessments

Assessment types come from the shared quiz registry. Selection follows the cognitive job, not a
fixed inventory. Checks are placed where the concept is taught and culminate in an applied transfer
task. Recognition-only questions cannot prove applied capability.

## Continuing-education readiness

Both engines may preserve learning outcomes, instructional-time basis, participation evidence,
assessment rules, completion records, content version, provider records, and evaluation evidence.
They may not claim contact hours, professional-development hours, continuing-education units, or
accreditor acceptance until the named accreditor's current requirements are verified and the exact
offering is approved.

## Final learning-system records

Every learning package locks its registry dependency, placement and remediation routes, stable
learning events, privacy and retention boundary, assessment item versions and passing policy, simulation
model assurance, language and unit policy, and measured time basis. Analytics may record learning
events and component performance. They must not silently collect facility-sensitive operating,
security, personnel, customer, or compliance information from a public learning experience.
Prior completions preserve the exact content and assessment versions; approved material corrections
use an explicit supersession and affected-learner notification policy.

## Public learning economy

The two engines share a public experience rule: governance may be deep without making the learner
operate the governance system. A focused learning product must orient quickly, expose only the
navigation needed for the current learning job, end with a concise transfer recap, and provide one
clear feedback path.

For Concept Briefs, the binding implementation is the learner-economy section of the Concept Brief
Production Contract: a short orientation, at most four primary controls, minimal public governance
metadata, a compact Community entry point, an outline-only SOP boundary, hidden inactive commercial
placements, and a three-part closing recap. Courses apply the same principle at module scale through
their approved Course Experience Brief and module storyboard rather than copying the Concept Brief
page pattern.
