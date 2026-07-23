# Release

## Version 0.8.0 live review

Status: deployed for authenticated review on 2026-07-23

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
