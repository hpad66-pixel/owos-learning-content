# Connected-learning right-drawer standard

Status: approved implementation direction  
Owner: Hardeep Anand  
Captured: 2026-07-26

Every OWOS course, lesson, and Concept Brief exposes Graph and Community controls in the top action
area. Each control opens one temporary right-side drawer over the unchanged HTML learning page.

Required behavior:

- Graph and Community are both available at the top.
- Only one connected-learning drawer is open at a time.
- The drawer enters from and remains anchored to the right edge.
- The underlying course, lesson, or brief URL remains the learning destination.
- Close, Escape, backdrop selection, and browser Back remove the drawer.
- Removing the drawer restores the unchanged learning page and returns focus to the control that
  opened it.
- The runtime carries the current course, lesson, brief, and Graph context into the connected
  experience.
- The rule is implemented in the Course Engine, Concept Engine, platform runtime, templates,
  conformance checks, and rendered browser QA. It is not a one-page HTML patch.

This direction changes interaction and navigation behavior. It does not approve Graph publication,
Community content, technical claims, credentials, commercial placement, or a course release.
