# Release

## Version 0.9.0 public live review

Status: deployed for unauthenticated public live review on 2026-07-23

Content baseline: `fddf2f842903756589e94fbdd5f40c3a67850032`

| Evidence | Value |
| --- | --- |
| Release ID | `owos-course-semantic-data-ai-001-v0.9.0` |
| Learning source merge | `c7f8b6bc1c519dcc71de2b7c4d4c169c38c81758` |
| Runtime platform merge | `c061988d4fd3c9337b8227312a08db0c09d354c8` |
| Runtime files | 24 checksum-verified files |
| Rendered browser QA | 18 lessons, 36 views, zero failures |
| Course landing | `https://owos.ai/course-meaning-before-models` |
| Cloudflare deployment | `https://78247e29.owos-3n1.pages.dev` |
| Access | Unauthenticated public live review |
| Available modules | 18 |
| Completion events | Disabled |
| Credential | Not configured |

This release replaces the rejected 0.8.0 rendered experience. It introduces eighteen distinct
lesson narratives and card compositions, working question-and-answer cards, meaningful visual and
process outputs, corrected assessment logic, and browser-operated desktop and phone QA for every
module. Its release manifest must carry a current passing rendered-browser receipt bound to the
exact lesson HTML, CSS, and JavaScript.

The production registry identifies the exact source merge, release ID, all eighteen available
modules, and disabled credential state. The landing, all eighteen canonical lesson routes, required
public asset, and representative live component paths passed unauthenticated production checks.

The existing 0.8.0 deployment remains historical evidence only and must not be treated as an
accepted design benchmark.

## Version 0.8.0 live review

Status: deployed on 2026-07-23 and rejected after rendered learner review

| Evidence | Value |
| --- | --- |
| Release ID | `owos-course-semantic-data-ai-001-v0.8.0` |
| Learning source commit | `8f87aecbcf5afb145d69e4acf117d08a3ff34a9c` |
| Runtime platform commit | `b53337183f64fd9999fa7d6d56826f8b998e5199` |
| Runtime files | 24 checksum-verified files |
| Course landing | `https://owos.ai/course-meaning-before-models` |
| Cloudflare deployment | `https://b2ee424d.owos-3n1.pages.dev` |
| Access | Authenticated live review |
| Available modules | 18 |
| Completion events | Disabled |
| Credential | Not configured |

The production Learn registry was checked after deployment on both the immutable deployment URL and
`https://owos.ai`. It identified the exact source commit, release ID, eighteen available modules,
and disabled credential state. Protected course routes correctly redirect unauthenticated requests
to sign-in.

This release rebuilds every lesson with four lesson-specific explanatory graphics, question flip
cards, and varied module assessments. Its release gate compares source and packaged visual shapes,
quiz sequences, JavaScript, and CSS so stale runtime output cannot pass behind a fresh manifest.

Human, practitioner, accessibility, device, authenticated-event, capstone, graph-publication, and
credential gates remain separate. This deployment does not convert those unperformed reviews into
passes.
