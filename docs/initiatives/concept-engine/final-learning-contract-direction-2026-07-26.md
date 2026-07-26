# Final learning-contract direction — 2026-07-26

Hardeep asked for a final architecture review before the Concept Brief inventory is activated at
scale, because package-shape changes after production would require migrating every built brief.

The final review preserves six migration-sensitive records in every Concept Brief:

1. placement, prerequisites, remediation, next learning, and course connections;
2. the authoritative shared-capability registry version and exact used capability identifiers;
3. stable learning-event names, attempt history, record authority, consent, privacy, retention,
   completion-version preservation, supersession, material-correction notification, and a
   prohibition on collecting facility-sensitive data in public briefs;
4. assessment passing, retry, item-version, feedback, accommodation, and review policy;
5. dynamic-model identity, version, visible assumptions, deterministic replay, qualified review,
   and a prohibition on operational use; and
6. primary language, units, localization state, instructional-time fields, and the method by which
   time will be measured before any continuing-education claim.

These records extend the existing `owos-concept-brief/2` package contract without duplicating shared
visual, interaction, animation, or quiz definitions. Continuing-education credit remains disabled
until the exact accreditor and offering are approved.
