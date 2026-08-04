# One Water AI Executive Fellowship Synchronization Contract

## The rule

The fellowship curriculum, curriculum prospectus, and Fieldbook are one governed product. A change
to the program title, course sequence, module title, learning job, applied result, or module count is
not complete until all three agree.

## The controlled relationship

1. `SYLLABUS.md` is the canonical curriculum blueprint.
2. `course.yaml` carries the matching program identity and expected counts.
3. `work-products/ONE-WATER-AI-FIELDBOOK-BLUEPRINT.md` defines the Fieldbook experience and record
   system.
4. `tools/build_fellowship_pdfs.py` reads the controlled syllabus and builds both PDFs in one run.
5. `output/pdf/fellowship-sync-manifest.json` records the exact source and output fingerprints.

The current blueprint contains exactly eight courses and 64 numbered modules. The eight live
executive forums, 16 applied studios, fieldwork, and capstone defense are additional learning
experiences. They do not increase the numbered module count unless the curriculum blueprint is
deliberately revised and approved.

## What must change together

| Curriculum change | Required synchronized work |
| --- | --- |
| Program name or positioning | Course brief, syllabus, metadata, both PDFs, and public copy |
| Course or module sequence | Syllabus, Fieldbook record order, both PDFs, scripts, and delivery map |
| Module learning job | Syllabus, module design brief, manuscript, Fieldbook prompt, and curriculum PDF |
| Applied result or capstone evidence | Syllabus, Fieldbook record, assessment plan, capstone checklist, and both PDFs |
| Source or factual teaching | Module source map, claims register, manuscript, recording script, FAQ, and QA report |
| Module added, merged, or retired | Explicit blueprint approval, renumbering review, Fieldbook review, metadata, and both PDFs |

## Build and check

Build the two PDFs and their synchronization manifest together:

```bash
/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  apps/ai-masterclass/tools/build_fellowship_pdfs.py
```

Check that no controlled source or PDF has drifted since that build:

```bash
/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  apps/ai-masterclass/tools/build_fellowship_pdfs.py --check
```

The check fails when the title, expected counts, module sequence, Fieldbook course sections, source
fingerprints, builder, or generated PDFs no longer agree.

## Module-content boundary

The synchronized PDFs reflect the approved curriculum blueprint. A completed lesson still requires
its module design brief, source map, manuscript, Articulate package, assessment plan, FAQ, recording
script, Fieldbook instrument, and QA report. The synchronization check does not turn an unfinished
module into approved teaching.
