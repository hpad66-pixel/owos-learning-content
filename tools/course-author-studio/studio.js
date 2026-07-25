(() => {
  "use strict";

  const views = [
    ["design-brief.md", "Design Brief", "Learning job, concept-to-experience trace, cognitive design, and approval boundary."],
    ["module.yaml", "Narrative", "Module identity, learning design, teaching sequence, FAQ, and evidence blocks."],
    ["storyboard.yaml", "Storyboard", "Beat-by-beat learner question, explanation, asset, action, realization, and approval."],
    ["visuals/visual-manifest.yaml", "Visuals", "Actual asset locators, teaching purpose, reading guide, accessibility, license, and review state."],
    ["interactions.yaml", "Interactions", "Purpose, instructions, component, completion evidence, and authored configuration."],
    ["assessments.yaml", "Assessments", "Cognitive job, prompt, scoring, feedback, retry, and work-product contract."],
    ["sources.yaml", "Sources", "Authority, locator, and the exact instructional use of each source."],
    ["glossary.yaml", "Glossary", "Terms, acronyms, and plain-English definitions."],
    ["qa.yaml", "QA", "Visible quality gates. Pending human review remains pending."],
    ["preview", "Preview", "Compiled learner experience at desktop, tablet, and phone widths."],
  ];

  const state = {
    course: null,
    module: null,
    data: null,
    file: "module.yaml",
  };
  const courseList = document.querySelector("[data-course-list]");
  const empty = document.querySelector("[data-empty]");
  const workspace = document.querySelector("[data-module-workspace]");
  const editorView = document.querySelector("[data-editor-view]");
  const previewView = document.querySelector("[data-preview-view]");
  const editor = document.querySelector("[data-editor]");
  const tabs = document.querySelector("[data-tabs]");
  const toast = document.querySelector("[data-toast]");
  const preview = document.querySelector("[data-preview]");

  function notify(message, error = false) {
    toast.textContent = message;
    toast.className = `toast show${error ? " error" : ""}`;
    window.clearTimeout(notify.timer);
    notify.timer = window.setTimeout(() => {
      toast.className = "toast";
    }, error ? 7000 : 3500);
  }

  async function api(url, options = {}) {
    const response = await fetch(url, {
      headers: {"Content-Type": "application/json"},
      ...options,
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Request failed.");
    return data;
  }

  function renderTabs() {
    tabs.innerHTML = "";
    views.forEach(([file, label]) => {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = label;
      button.classList.toggle("active", state.file === file);
      button.addEventListener("click", () => selectView(file));
      tabs.append(button);
    });
  }

  function selectView(file) {
    state.file = file;
    renderTabs();
    const config = views.find(([name]) => name === file);
    const isPreview = file === "preview";
    editorView.hidden = isPreview;
    previewView.hidden = !isPreview;
    if (isPreview) {
      refreshPreview();
      return;
    }
    document.querySelector("[data-current-label]").textContent = config[1];
    document.querySelector("[data-current-help]").textContent = config[2];
    editor.value = state.data.files[file] || "";
  }

  function evidenceCard(label, value) {
    const card = document.createElement("article");
    card.className = "evidence-card";
    const small = document.createElement("span");
    small.textContent = label;
    const strong = document.createElement("strong");
    strong.textContent = value;
    card.append(small, strong);
    return card;
  }

  function renderModule() {
    const module = state.data.package.module;
    document.querySelector("[data-module-id]").textContent = module.module_id;
    document.querySelector("[data-module-title]").textContent = module.title;
    document.querySelector("[data-module-promise]").textContent = module.promise;
    document.querySelector("[data-source-version]").textContent = module.source_version;
    document.querySelector("[data-compiler-version]").textContent = state.data.package.compiler_version;
    const evidence = document.querySelector("[data-evidence-grid]");
    evidence.innerHTML = "";
    evidence.append(
      evidenceCard("Storyboard", state.data.package.storyboard.status),
      evidenceCard("Real visuals", String(state.data.package.visuals.length)),
      evidenceCard("Interactions", String(state.data.package.interactions.length)),
      evidenceCard("Assessments", String(state.data.package.assessments.length)),
      evidenceCard("Archetype", module.archetype),
      evidenceCard("Signature mechanism", module.signature_mechanism),
      evidenceCard("Package checksum", state.data.package.checksum.slice(0, 16)),
      evidenceCard("Release gate", state.data.package.qa.gates.release),
    );
    empty.hidden = true;
    workspace.hidden = false;
    renderTabs();
    selectView(state.file);
  }

  async function selectModule(course, module, button) {
    document.querySelectorAll(".module-link").forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    state.course = course;
    state.module = module;
    state.file = "design-brief.md";
    try {
      state.data = await api(`/api/module?course=${encodeURIComponent(course)}&module=${encodeURIComponent(module)}`);
      renderModule();
    } catch (error) {
      notify(error.message, true);
    }
  }

  async function loadCourses() {
    try {
      const data = await api("/api/courses");
      courseList.innerHTML = "";
      const route = window.location.pathname.match(/^\/review\/([^/]+)\/([^/]+)\/?$/);
      let requestedButton = null;
      data.courses.forEach((course) => {
        const group = document.createElement("section");
        group.className = "course-group";
        const heading = document.createElement("h3");
        heading.textContent = course.title;
        group.append(heading);
        course.modules.forEach((module) => {
          const button = document.createElement("button");
          button.className = "module-link";
          button.type = "button";
          button.textContent = module.title;
          button.addEventListener("click", () => selectModule(course.slug, module.slug, button));
          if (route && decodeURIComponent(route[1]) === course.slug && decodeURIComponent(route[2]) === module.slug) {
            requestedButton = {course: course.slug, module: module.slug, button};
          }
          group.append(button);
        });
        courseList.append(group);
      });
      if (requestedButton) {
        await selectModule(requestedButton.course, requestedButton.module, requestedButton.button);
      } else if (route) {
        notify("The requested structured module was not found.", true);
      }
    } catch (error) {
      notify(error.message, true);
    }
  }

  async function save() {
    if (!state.course || state.file === "preview") return;
    try {
      await api("/api/save", {
        method: "POST",
        body: JSON.stringify({
          course: state.course,
          module: state.module,
          file: state.file,
          content: editor.value,
        }),
      });
      state.data.files[state.file] = editor.value;
      notify(`${state.file} saved. The prior source was preserved in module history.`);
    } catch (error) {
      notify(error.message, true);
    }
  }

  async function validate() {
    if (!state.course) return notify("Select a module first.", true);
    try {
      const result = await api("/api/validate", {
        method: "POST",
        body: JSON.stringify({course: state.course, module: state.module}),
      });
      notify(`Package valid.\n${result.checksum.slice(0, 20)}\nCompiler ${result.compiler_version}`);
    } catch (error) {
      notify(error.message, true);
    }
  }

  async function build() {
    if (!state.course) return notify("Select a module first.", true);
    try {
      const result = await api("/api/build", {
        method: "POST",
        body: JSON.stringify({course: state.course, module: state.module}),
      });
      state.data.preview_url = result.preview_url;
      preview.src = `${result.preview_url}?build=${Date.now()}`;
      selectView("preview");
      notify(`Preview built with compiler ${result.compiler_version}.`);
    } catch (error) {
      notify(error.message, true);
    }
  }

  function refreshPreview() {
    if (!state.data?.preview_url) return;
    preview.src = `${state.data.preview_url}?refresh=${Date.now()}`;
  }

  document.querySelector("[data-save]").addEventListener("click", save);
  document.querySelector('[data-action="validate"]').addEventListener("click", validate);
  document.querySelector('[data-action="build"]').addEventListener("click", build);
  document.querySelector("[data-refresh-preview]").addEventListener("click", refreshPreview);
  document.querySelectorAll("[data-width]").forEach((button) => {
    button.addEventListener("click", () => {
      preview.style.width = button.dataset.width;
    });
  });
  loadCourses();
})();
