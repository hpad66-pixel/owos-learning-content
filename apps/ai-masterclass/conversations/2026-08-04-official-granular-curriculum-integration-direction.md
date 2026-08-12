# Official Granular Curriculum Integration Direction

Date: 2026-08-04

Owner: Hardeep Anand

## Direction

The detailed module breakdown must be part of the official One Water AI curriculum documents. It
must not remain a separate review page that leaves the downloadable PDF unchanged.

Each of the 64 modules must show its current sections and subsections with stable identifiers. The
official HTML must let a reader expand or collapse each module, search by identifier or subject, and
open the selected section inside the same reader. The official PDF must show the same hierarchy with
exact page references and nested bookmarks. PDF pages cannot collapse, so bookmarks provide the
equivalent navigation behavior in a PDF reader.

## Implementation boundary

Current instruction and proposed additions must remain visibly different. Proposed additions from
the gap review appear in gold and retain their stable `Mxx.Pnn` identifiers. Showing them in the
official contents does not approve them as completed lessons or authorize learner release.

The canonical source for this structure is:

`curriculum/one-water-ai-granular-toc.json`

The official generated outputs are:

`output/html/one-water-ai-applied-intelligence-curriculum.html`

`output/pdf/one-water-ai-applied-intelligence-curriculum.pdf`

## Acceptance evidence

- 64 module groups are present in the HTML contents.
- 1,341 current, planned, and subtopic navigation links are searchable in the HTML reader.
- The PDF contains 788 pages, a complete granular contents section, exact page references, and
  nested bookmarks.
- Stable-ID search and deep links work on desktop and phone.
- Browser QA reports no JavaScript errors and no page-level horizontal overflow.
- The generated-output manifest and both build checks pass.
