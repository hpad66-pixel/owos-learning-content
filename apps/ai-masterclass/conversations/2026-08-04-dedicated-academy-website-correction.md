# Dedicated Academy website correction

**Date:** 2026-08-04

## Hardeep's correction

The master curriculum website must not be presented as part of Capture Call or the personal One
Water OS interface. It is a dedicated One Water AI Academy authoring and production application.

The entire Academy uses the APAS.dev product language. The curriculum is the center of the
experience, with editable working manuscripts, annotations, assignments, research handoffs,
stage-specific quality control, graphics production, Articulate production, final assembly,
packaging, release review, and audit history.

## Recorded implementation boundary

- The application lives at the protected `/academy` route in `onewater-os-platform`.
- Capture Call remains a separate product and no longer displays the Academy registry.
- `owos-learning-content` remains the authority for approved curriculum and generated artifacts.
- The Academy database stores collaboration and working state, not the approved curriculum source.
- No public deployment or learner-facing release is authorized by this correction.
