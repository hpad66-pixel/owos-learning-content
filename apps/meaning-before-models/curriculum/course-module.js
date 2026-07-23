(() => {
  "use strict";
  const moduleId = document.body.dataset.module;
  const key = `mbm001:${moduleId}:v2`;
  let state = {};
  try { state = JSON.parse(localStorage.getItem(key)) || {}; } catch { state = {}; }
  state.done ||= {};
  state.artifact ||= {};
  const required = ["opening", "cards", "process", "quiz2", "quiz3", "artifact", "applied"];
  let lastTrigger = null;

  const save = () => localStorage.setItem(key, JSON.stringify(state));
  function feedback(root, text, good) {
    const node = root.querySelector(".feedback");
    if (!node) return;
    node.textContent = text;
    node.className = `feedback show ${good ? "good" : "bad"}`;
  }
  function mark(name) {
    if (!name) return;
    state.done[name] = true;
    save();
    renderCompletion();
  }
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

  document.querySelectorAll(".flip-question").forEach(card => card.addEventListener("click", () => {
    card.classList.toggle("turned");
    card.setAttribute("aria-pressed", String(card.classList.contains("turned")));
    const deck = card.closest("[data-quiz-type='flip-cards']");
    if ([...deck.querySelectorAll(".flip-question")].every(item => item.classList.contains("turned"))) {
      feedback(deck, "All cards turned. Explain one answer in your own words before moving on.", true);
      if (deck.dataset.required) mark(deck.dataset.required);
    }
  }));

  const process = document.querySelector("#process-lab");
  const processButtons = [...process.querySelectorAll("[data-step]")];
  const selectedSteps = new Set();
  processButtons.forEach((button, index) => button.addEventListener("click", () => {
    selectedSteps.add(index);
    button.classList.add("selected");
    process.querySelector("[data-step-detail]").innerHTML = `<b>Step ${index + 1}: ${button.textContent}</b>${button.dataset.detail}`;
    feedback(process, `${selectedSteps.size} of ${processButtons.length} steps inspected.`, true);
    if (selectedSteps.size === processButtons.length) mark("process");
  }));

  document.querySelectorAll(".quiz-panel").forEach(quiz => {
    quiz.querySelectorAll(".choice, .option-check").forEach(button => button.addEventListener("click", () => {
      if (button.classList.contains("choice")) {
        quiz.querySelectorAll(".choice").forEach(item => item.classList.remove("selected"));
      }
      button.classList.toggle("selected");
    }));

    const pairState = { left: null, right: null, done: new Set() };
    quiz.querySelectorAll("[data-pair]").forEach(button => button.addEventListener("click", () => {
      const side = button.dataset.side;
      quiz.querySelectorAll(`[data-side="${side}"]`).forEach(item => item.classList.remove("selected"));
      button.classList.add("selected");
      pairState[side] = button;
      if (!pairState.left || !pairState.right) return;
      const good = pairState.left.dataset.pair === pairState.right.dataset.pair;
      if (good) {
        pairState.left.classList.add("correct");
        pairState.right.classList.add("correct");
        pairState.done.add(pairState.left.dataset.pair);
      }
      feedback(quiz, good ? `${pairState.done.size} of 4 pairs connected.` : "Those jobs differ. Inspect the visual and retry.", good);
      pairState.left.classList.remove("selected");
      pairState.right.classList.remove("selected");
      pairState.left = pairState.right = null;
      if (pairState.done.size === 4) mark(quiz.dataset.required);
    }));

    quiz.querySelectorAll("[data-order]").forEach(button => button.addEventListener("click", () => {
      const list = button.parentElement;
      const selected = list.querySelector(".selected");
      if (!selected) return button.classList.add("selected");
      if (selected === button) return button.classList.remove("selected");
      const marker = document.createElement("span");
      list.insertBefore(marker, selected);
      list.insertBefore(selected, button);
      list.insertBefore(button, marker);
      marker.remove();
      selected.classList.remove("selected");
    }));

    quiz.querySelector("[data-estimate]")?.addEventListener("input", event => {
      event.target.nextElementSibling.value = `${event.target.value} seconds`;
    });

    quiz.querySelector("[data-check-generic]")?.addEventListener("click", () => {
      const type = quiz.dataset.quizType;
      let good = false;
      if (["multiple-choice", "true-false", "path-choice", "timeline-choice"].includes(type)) {
        good = quiz.querySelector(".choice.selected")?.dataset.correct === "1";
      } else if (["classify", "multi-select", "capstone-rubric"].includes(type)) {
        good = [...quiz.querySelectorAll(".option-check")].every(button => button.classList.contains("selected") === (button.dataset.correct === "1"));
      } else if (type === "fill-in") {
        const input = quiz.querySelector("input");
        good = input.value.trim().toLowerCase().includes(input.dataset.answer);
      } else if (type === "ordering") {
        good = [...quiz.querySelectorAll("[data-order]")].every((button, index) => Number(button.dataset.order) === index);
      } else if (type === "reflection") {
        good = quiz.querySelector("[data-reflection]").value.trim().length >= 30;
      } else if (type === "estimate") {
        const input = quiz.querySelector("[data-estimate]");
        good = Math.abs(Number(input.value) - Number(input.dataset.answer)) <= Number(input.dataset.tolerance || 0);
      }
      feedback(quiz, good ? "Correct. The answer is explicit enough to inspect and govern." : `${quiz.dataset.retry} Try again.`, good);
      if (good) mark(quiz.dataset.required);
    });
  });

  document.querySelectorAll("[data-visual-action]").forEach(button => button.addEventListener("click", () => {
    const panel = button.closest(".visual-panel");
    panel.querySelectorAll("[data-visual-action]").forEach(item => item.classList.toggle("active", item === button));
    const result = panel.querySelector(".visual-insight");
    if (result) result.textContent = button.dataset.detail;
  }));

  const form = document.querySelector("#work-product");
  Object.entries(state.artifact).forEach(([name, value]) => {
    if (form.elements.namedItem(name)) form.elements.namedItem(name).value = value;
  });
  const preview = document.querySelector("[data-artifact-preview]");
  const formData = () => Object.fromEntries(new FormData(form).entries());
  const drawPreview = data => {
    preview.textContent = Object.entries(data).map(([name, value], index) => `${index + 1}. ${name.toUpperCase()}\n${value || "Not yet defined"}`).join("\n\n");
  };
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

  const criteria = ["Bounded operational question", "Module responsibilities are specific", "Evidence boundary is named", "Reviewers are named", "Human authority or stop condition is explicit"];
  const criteriaBox = document.querySelector("[data-criteria]");
  const drawCriteria = (results = criteria.map(() => false)) => {
    criteriaBox.innerHTML = criteria.map((label, index) => `<div class="criterion ${results[index] ? "pass" : ""}"><i>${results[index] ? "✓" : "○"}</i><span>${label}</span></div>`).join("");
  };
  drawCriteria();
  const applied = document.querySelector("#applied-check");
  applied.querySelector("[data-check-applied]").addEventListener("click", () => {
    if (!state.done.artifact) return feedback(applied, "Save the work product first.", false);
    const values = Object.values(state.artifact);
    const results = [values[0]?.length >= 24, values.slice(1, 5).every(value => value?.length >= 20), values[5]?.length >= 20, values[6]?.length >= 14, /\b(human|approve|review|cannot|must not|stop|decide)\b/i.test(values[7] || "")];
    drawCriteria(results);
    const good = results.every(Boolean);
    feedback(applied, good ? "Applied assessment passed. Another team can review this artifact." : applied.dataset.retry, good);
    if (good) mark("applied");
  });

  function closeDrawers() {
    document.querySelectorAll("[data-drawer]").forEach(drawer => {
      drawer.classList.remove("open");
      drawer.setAttribute("aria-hidden", "true");
    });
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
    document.querySelectorAll("[data-thread]").forEach(thread => {
      thread.hidden = !thread.textContent.toLowerCase().includes(communitySearch.value.toLowerCase());
    });
  });
  document.querySelector("[data-bookmark]").addEventListener("click", event => event.currentTarget.classList.toggle("on"));
  document.querySelector("[data-reply-form]").addEventListener("submit", event => {
    event.preventDefault();
    const input = event.currentTarget.querySelector("input");
    if (!input.value.trim()) return;
    const reply = document.createElement("p");
    reply.textContent = `Your local draft: ${input.value.trim()}`;
    document.querySelector(".replies").append(reply);
    input.value = "";
  });
  document.querySelector("[data-complete]").addEventListener("click", () => {
    feedback(document.querySelector(".complete"), "Module marked complete in this browser. This is not a credential or release record.", true);
  });
  renderCompletion();
})();
