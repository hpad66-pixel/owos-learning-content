(() => {
  "use strict";
  const moduleId = document.body.dataset.module;
  const key = `mbm001:${moduleId}:v1`;
  let state = {};
  try { state = JSON.parse(localStorage.getItem(key)) || {}; } catch { state = {}; }
  state.done ||= {};
  state.artifact ||= {};
  const required = ["opening", "process", "matching", "multi", "artifact", "applied"];
  let lastTrigger = null;

  function save() { localStorage.setItem(key, JSON.stringify(state)); }
  function feedback(root, text, good) {
    const node = root.querySelector(".feedback");
    if (!node) return;
    node.textContent = text;
    node.className = `feedback show ${good ? "good" : "bad"}`;
  }
  function mark(name) { state.done[name] = true; save(); renderCompletion(); }
  function renderCompletion() {
    required.forEach(name => document.querySelector(`[data-requirement="${name}"]`)?.classList.toggle("done", Boolean(state.done[name])));
    const count = required.filter(name => state.done[name]).length;
    document.querySelector("[data-completion-status]").textContent = `${count} of ${required.length} required pieces complete.`;
    document.querySelector("[data-complete]").disabled = count !== required.length;
  }

  document.querySelectorAll(".lenses [data-lens]").forEach(button => button.addEventListener("click", () => {
    document.body.dataset.lens = button.dataset.lens;
    document.querySelectorAll(".lenses [data-lens]").forEach(item => item.classList.toggle("on", item === button));
  }));

  const reading = document.querySelector(".reading");
  addEventListener("scroll", () => {
    const distance = document.documentElement.scrollHeight - innerHeight;
    reading.style.transform = `scaleX(${distance > 0 ? Math.min(1, scrollY / distance) : 0})`;
  }, { passive: true });

  const tt = document.querySelector("#tt");
  document.querySelectorAll(".term").forEach(term => {
    term.tabIndex = 0;
    const show = () => {
      tt.textContent = term.dataset.def;
      tt.classList.add("show");
      const rect = term.getBoundingClientRect();
      tt.style.left = `${Math.max(12, Math.min(innerWidth - 332, rect.left))}px`;
      tt.style.top = `${rect.bottom + 8}px`;
    };
    const hide = () => tt.classList.remove("show");
    term.addEventListener("mouseenter", show);
    term.addEventListener("focus", show);
    term.addEventListener("mouseleave", hide);
    term.addEventListener("blur", hide);
  });

  const opening = document.querySelector("#opening-quiz");
  opening.querySelectorAll(".choice").forEach(choice => choice.addEventListener("click", () => {
    opening.querySelectorAll(".choice").forEach(item => item.classList.remove("selected"));
    choice.classList.add("selected");
  }));
  opening.querySelector("[data-check-quiz]").addEventListener("click", () => {
    const selected = opening.querySelector(".choice.selected");
    if (!selected) return feedback(opening, "Choose one answer before checking.", false);
    const good = selected.dataset.correct === "1";
    feedback(opening, good ? "Correct. The answer preserves an explicit, reviewable boundary." : `${opening.dataset.retry} Choose again and retry.`, good);
    if (good) mark("opening");
  });

  const process = document.querySelector("#process-lab");
  const processButtons = [...process.querySelectorAll("[data-step]")];
  const detail = process.querySelector("[data-step-detail]");
  const selectedSteps = new Set();
  processButtons.forEach((button, index) => button.addEventListener("click", () => {
    selectedSteps.add(index);
    button.classList.add("selected");
    detail.innerHTML = `<b>Step ${index + 1}: ${button.textContent}</b>This step adds named evidence, a controlled relationship or rule, and an accountable review point.`;
    feedback(process, `${selectedSteps.size} of ${processButtons.length} steps inspected.`, true);
    if (selectedSteps.size === processButtons.length) mark("process");
  }));

  const matching = document.querySelector("#concept-match");
  let left = null;
  let right = null;
  const matched = new Set();
  function checkPair() {
    if (left === null || right === null) return;
    const good = left + right === 3;
    if (good) {
      matching.querySelector(`[data-match-question="${left}"]`).classList.add("correct");
      matching.querySelector(`[data-match-job="${right}"]`).classList.add("correct");
      matched.add(left);
      feedback(matching, `${matched.size} of 4 pairs correct.`, true);
    } else {
      feedback(matching, `${matching.dataset.retry} Retry this pair.`, false);
    }
    matching.querySelectorAll(".selected").forEach(node => node.classList.remove("selected"));
    left = right = null;
    if (matched.size === 4) mark("matching");
  }
  matching.querySelector("[data-match-left]").addEventListener("click", event => {
    const button = event.target.closest("[data-match-question]");
    if (!button || button.classList.contains("correct")) return;
    matching.querySelector("[data-match-left]").querySelectorAll(".selected").forEach(node => node.classList.remove("selected"));
    button.classList.add("selected");
    left = Number(button.dataset.matchQuestion);
    checkPair();
  });
  matching.querySelector("[data-match-right]").addEventListener("click", event => {
    const button = event.target.closest("[data-match-job]");
    if (!button || button.classList.contains("correct")) return;
    matching.querySelector("[data-match-right]").querySelectorAll(".selected").forEach(node => node.classList.remove("selected"));
    button.classList.add("selected");
    right = Number(button.dataset.matchJob);
    checkPair();
  });

  const multi = document.querySelector("#boundary-check");
  multi.querySelectorAll(".option-check").forEach(button => button.addEventListener("click", () => button.classList.toggle("selected")));
  multi.querySelector("[data-check-multi]").addEventListener("click", () => {
    const good = [...multi.querySelectorAll(".option-check")].every(button => button.classList.contains("selected") === (button.dataset.correct === "1"));
    feedback(multi, good ? "Correct. Evidence, explicit meaning, and accountable review belong in the path." : `${multi.dataset.retry} Change your selections and retry.`, good);
    if (good) mark("multi");
  });

  const form = document.querySelector("#work-product");
  Object.entries(state.artifact).forEach(([name, value]) => { if (form.elements.namedItem(name)) form.elements.namedItem(name).value = value; });
  const preview = document.querySelector("[data-artifact-preview]");
  function formData() { return Object.fromEntries(new FormData(form).entries()); }
  function drawPreview(data) { preview.textContent = Object.entries(data).map(([name, value], index) => `${index + 1}. ${name.toUpperCase()}\n${value || "Not yet defined"}`).join("\n\n"); }
  drawPreview(state.artifact);
  form.addEventListener("input", () => drawPreview(formData()));
  form.addEventListener("submit", event => {
    event.preventDefault();
    const data = formData();
    if (Object.values(data).some(value => value.trim().length < 14)) return feedback(form, "Every field needs a specific statement of at least 14 characters.", false);
    state.artifact = data;
    save();
    drawPreview(data);
    feedback(form, "Working draft saved locally. Now evaluate it.", true);
    mark("artifact");
  });

  const criteria = [
    "Bounded operational question", "Four module responsibilities are specific",
    "Evidence and source boundary is named", "Reviewers are named",
    "Human authority or stop condition is explicit"
  ];
  const criteriaBox = document.querySelector("[data-criteria]");
  function drawCriteria(results = criteria.map(() => false)) {
    criteriaBox.innerHTML = criteria.map((label, index) => `<div class="criterion ${results[index] ? "pass" : ""}"><i>${results[index] ? "✓" : "○"}</i><span>${label}</span></div>`).join("");
  }
  drawCriteria();
  const applied = document.querySelector("#applied-check");
  applied.querySelector("[data-check-applied]").addEventListener("click", () => {
    if (!state.done.artifact) return feedback(applied, "Save the work product first.", false);
    const values = Object.values(state.artifact);
    const results = [
      values[0]?.length >= 24,
      values.slice(1, 5).every(value => value?.length >= 20),
      values[5]?.length >= 20,
      values[6]?.length >= 14,
      /\b(human|approve|review|cannot|must not|stop|decide)\b/i.test(values[7] || "")
    ];
    drawCriteria(results);
    const good = results.every(Boolean);
    feedback(applied, good ? "Applied assessment passed. Another team can review this artifact." : `${applied.dataset.retry}`, good);
    if (good) mark("applied");
  });

  function closeDrawers() {
    document.querySelectorAll("[data-drawer]").forEach(drawer => { drawer.classList.remove("open"); drawer.setAttribute("aria-hidden", "true"); });
    document.querySelector(".drawer-scrim").classList.remove("open");
    document.body.classList.remove("drawer-open");
    const trigger = lastTrigger;
    lastTrigger = null;
    if (trigger) setTimeout(() => trigger.focus(), 0);
  }
  function openDrawer(name, trigger) {
    lastTrigger = trigger;
    const drawer = document.querySelector(`[data-drawer="${name}"]`);
    drawer.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    document.querySelector(".drawer-scrim").classList.add("open");
    document.body.classList.add("drawer-open");
    drawer.querySelector("button, input")?.focus();
  }
  document.querySelectorAll("[data-open-graph]").forEach(button => button.addEventListener("click", () => openDrawer("graph", button)));
  document.querySelectorAll("[data-open-community]").forEach(button => button.addEventListener("click", () => openDrawer("community", button)));
  document.querySelectorAll("[data-close-drawer]").forEach(button => button.addEventListener("click", closeDrawers));
  document.addEventListener("keydown", event => { if (event.key === "Escape") closeDrawers(); });

  document.querySelectorAll("[data-graph-id]").forEach(node => node.addEventListener("click", () => {
    document.querySelectorAll("[data-graph-id]").forEach(item => item.classList.toggle("active", item === node));
    document.querySelector("[data-graph-detail]").innerHTML = `<b>${node.dataset.graphKind}: ${node.textContent}</b><p>This node is connected to the module evidence path and competency.</p>`;
  }));
  const communitySearch = document.querySelector("[data-community-search]");
  communitySearch.addEventListener("input", () => {
    document.querySelectorAll("[data-thread]").forEach(thread => thread.hidden = !thread.textContent.toLowerCase().includes(communitySearch.value.toLowerCase()));
  });
  document.querySelector("[data-bookmark]").addEventListener("click", event => event.currentTarget.classList.toggle("on"));
  document.querySelector("[data-reply-form]").addEventListener("submit", event => {
    event.preventDefault();
    const input = event.currentTarget.querySelector("input");
    if (!input.value.trim()) return;
    const p = document.createElement("p");
    p.textContent = `Your local draft: ${input.value.trim()}`;
    document.querySelector(".replies").append(p);
    input.value = "";
  });

  document.querySelector("[data-complete]").addEventListener("click", () => {
    const live = document.querySelector("#live");
    live.textContent = "Module marked complete in this browser. This is not a credential or release record.";
    live.className = "feedback show good";
  });
  renderCompletion();
})();
