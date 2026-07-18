# apps

One folder per application. Each app reuses the shared foundation in `../core/`, so they all look and
behave consistently.

- **`project-management/`** the Project Management masterclass (course chrome, chapters, playbook,
  starter kit). Built.
- Coming next: `living-graph/`, `fable-agent/`, `one-water-os/`, and others.

To start a new app: make a folder here, copy `../core/components/module-template.html`, point at
`../core/brand` and `../core/standards`, and follow the build order in
`../core/standards/WRITING-STANDARD.md`.
