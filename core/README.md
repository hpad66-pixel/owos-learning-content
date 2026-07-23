# core

The reusable foundation. Build it once here, and every app in `apps/` uses it. Change something in
`core/` and the branding, voice, and approach update everywhere at once.

- **`brand/`** the Clearwater brand: `owos-brand.css`, Droobi, logos, `BRAND-GUIDELINES.md`.
- **`standards/`** how we write and build: `WRITING-STANDARD.md` (voice + component + quiz rules) and
  `VISUAL-ARSENAL.md` (the ~35 visual types plus the Selection Prompt). The approved
  `COURSE-PRODUCTION-CONTRACT.md` is the single, non-optional release floor for syllabus,
  instruction, graphics, interactions, navigation, accessibility, QA, provenance, and deployment.
  `COURSE-OPERATING-STANDARD.md` combines the Project Delivery learner experience with Data Before
  AI governance and defines the required production and release gates for every OWOS course.
- **`components/`** the building blocks: `component-gallery.html` (visuals) and `quiz-gallery.html`
  (quizzes) rendered live, `module-template.html` to copy, and the `COMPONENTS.md` / `QUIZ-TYPES.md`
  Markdown catalogs.

Do not put app-specific content here. Only things meant to be shared by more than one app.
