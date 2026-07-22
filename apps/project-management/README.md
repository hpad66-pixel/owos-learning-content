# Utility Project Delivery

This folder is the governed curriculum source for the One Water Operating System Master Class
**Utility Project Delivery: From Scope to Service**.

## Start here

- [Machine-readable course record](course.yaml)
- [Complete syllabus](curriculum/SYLLABUS.md)
- [Course-to-Learn architecture](../../docs/OWOS-COURSE-TO-LEARN-ARCHITECTURE.md)

## Current release

All 21 native OWOS chapters are available. The course contains 60 sections across eight parts,
including the applied capstone and the PMP and CAPM preparation chapter. Chapter checks are learning
activities. A final scored assessment and completion credential remain separate governed releases.

The content baseline is commit `808c82fa1fff2c7f46703fe0955c0a3d546ae0f3`, which completed Chapters
19 through 21. Subsequent releases must retain this provenance and identify their own reviewed source
commit in the generated course manifest.

## Build and release

1. Change the curriculum source in `curriculum/`.
2. Rebuild the affected page with `tools/build-selfcontained.py`.
3. Generate and verify the release manifest with `tools/build-course-release.py`.
4. Review the source, build, checksums, accessibility, navigation, and release claims.
5. Dispatch the approved release to `hpad66-pixel/onewater-os-platform`.
6. Review and merge the intake pull request before production deployment.

The files under `dist/site/` are reproducible delivery outputs. They are not an alternate authoring
location.

