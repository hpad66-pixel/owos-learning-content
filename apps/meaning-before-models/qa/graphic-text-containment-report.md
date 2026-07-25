# Graphic Text-Containment Report

Date: 2026-07-24

## Scope

All source SVG graphics in structured Modules 01 through 17.

## Method

`qa/svg-text-containment-audit.cjs` loaded every SVG in Chrome, measured every visible text element,
identified the smallest rendered rectangular container holding its center, and compared the rendered
text bounds with an internal padding boundary. Rotated labels were reviewed as rotated labels rather
than compared against horizontal width.

## Initial result

- SVG files checked: 71
- Text elements checked: 1,119
- Files with containment failures: 12
- Text-containment failures: 21

Failures appeared in Modules 01, 02, 03, 04, 05, 13, and 14. They included long relationship
captions, evidence-state labels, source-change labels, and a materialized-graph label.

## Repairs

The source SVGs were repaired with explicit bounded text lengths and spacing-and-glyph adjustment.
The corrections preserve the original words and container hierarchy. No raster substitution or
decorative replacement was used.

## Final result

- SVG files checked: 71
- Text elements checked: 1,119
- Files with containment failures: 0
- Text-containment failures: 0
- Audit exit status: passed

The repaired source assets were recompiled into module previews, curriculum delivery pages, and the
checksum-controlled distributable release. Independent human visual, zoom, and assistive-technology
review remains required for final credential-bearing release.
