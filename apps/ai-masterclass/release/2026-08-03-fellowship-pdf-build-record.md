# Fellowship PDF Build Record

Date: 2026-08-03

Status: working artifacts generated, not released

## Outputs

| Artifact | Pages | SHA-256 |
| --- | ---: | --- |
| `output/pdf/one-water-ai-executive-fellowship-master-curriculum.pdf` | 17 | `bd4856e99d4e101fa36e0b5676a220b6786dfa1324e71498f2af87f4987fccf1` |
| `output/pdf/one-water-ai-fieldbook-working-edition.pdf` | 143 | `5810419d2ec625c9437da77796f86daa1077377646be3ba022823616046a907f` |

## QA completed

- Parsed eight courses and 64 modules from the controlled syllabus.
- Confirmed 64 module markers in the Fieldbook and all 64 module numbers in the curriculum PDF.
- Confirmed zero blank pages and zero `undefined` text.
- Extracted PDF text and passed the Hardeep voice checker.
- Rendered both PDFs to images and reviewed the complete curriculum plus representative Fieldbook pages.
- Corrected the Fieldbook footer safe area and removed a duplicate footer before the final build.
- Generated `fellowship-sync-manifest.json` and passed the fail-closed synchronization check across
  the title, eight courses, 64 modules, controlled sources, builder, and both PDFs.

## Release boundary

This is not evidence of publication to Articulate, LearnWorlds, OWOS, or any public channel. Accessibility
certification, fillable form fields, printer proof, participant testing, and public-release approval remain
pending.
