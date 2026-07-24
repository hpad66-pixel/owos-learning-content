(() => {
  const body = document.body;
  const store = `mbm:${body.dataset.module || "lesson"}:retrofit`;
  const state = JSON.parse(localStorage.getItem(store) || '{"done":{}}');
  const save = () => localStorage.setItem(store, JSON.stringify(state));
  const mark = (key) => {
    if (!key) return;
    state.done[key] = true;
    save();
    document.querySelectorAll(`[data-requirement="${key}"]`).forEach((node) => node.classList.add("done"));
    updateComplete();
  };
  const updateComplete = () => {
    const required = [...document.querySelectorAll("[data-requirement]")].map((n) => n.dataset.requirement);
    const complete = required.length > 0 && required.every((key) => state.done[key]);
    const button = document.querySelector("[data-complete]");
    if (button) button.disabled = !complete;
  };
  Object.keys(state.done).forEach(mark);

  document.querySelectorAll("[data-lens]").forEach((button) => button.addEventListener("click", () => {
    if (!button.closest(".lenses")) return;
    body.dataset.lens = button.dataset.lens;
    document.querySelectorAll(".lenses [data-lens]").forEach((item) => {
      const on = item === button;
      item.classList.toggle("on", on);
      item.setAttribute("aria-selected", String(on));
    });
  }));

  let returnFocus = null;
  const scrim = document.querySelector(".drawer-scrim");
  const closeDrawers = () => {
    document.querySelectorAll(".drawer.open").forEach((drawer) => {
      drawer.classList.remove("open");
      drawer.setAttribute("aria-hidden", "true");
    });
    if (scrim) scrim.classList.remove("on");
    if (returnFocus) returnFocus.focus();
  };
  document.querySelectorAll("[data-open-graph],[data-open-community]").forEach((button) => button.addEventListener("click", () => {
    returnFocus = button;
    const drawer = document.querySelector(button.hasAttribute("data-open-graph") ? "#graphDrawer" : "#communityDrawer");
    if (!drawer) return;
    drawer.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    if (scrim) scrim.classList.add("on");
    drawer.querySelector("button, a, input")?.focus();
  }));
  document.querySelectorAll("[data-close-drawer]").forEach((button) => button.addEventListener("click", closeDrawers));
  document.addEventListener("keydown", (event) => { if (event.key === "Escape") closeDrawers(); });

  document.querySelectorAll("[data-quiz]").forEach((quiz) => {
    quiz.querySelectorAll(".choice").forEach((choice) => choice.addEventListener("click", () => {
      quiz.querySelectorAll(".choice").forEach((item) => item.classList.remove("selected"));
      choice.classList.add("selected");
    }));
    quiz.querySelector("[data-check-quiz]")?.addEventListener("click", () => {
      const selected = quiz.querySelector(".choice.selected");
      const feedback = quiz.querySelector(".feedback");
      if (!selected) {
        feedback.textContent = "Choose an answer first.";
        feedback.className = "feedback bad";
        return;
      }
      const correct = selected.dataset.correct === "1";
      selected.classList.add(correct ? "correct" : "wrong");
      feedback.textContent = correct ? quiz.dataset.correctFeedback : quiz.dataset.retry;
      feedback.className = `feedback ${correct ? "good" : "bad"}`;
      if (correct) mark(quiz.dataset.required);
    });
  });

  document.querySelectorAll("form[data-artifact]").forEach((form) => {
    const saved = state.artifacts?.[form.dataset.artifact];
    if (saved) Object.entries(saved).forEach(([name, value]) => { if (form.elements[name]) form.elements[name].value = value; });
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const values = Object.fromEntries(new FormData(form).entries());
      state.artifacts ||= {};
      state.artifacts[form.dataset.artifact] = values;
      save();
      const preview = form.closest(".panel")?.querySelector("[data-artifact-preview]");
      if (preview) preview.textContent = Object.entries(values).map(([key, value]) => `${key.replaceAll("_", " ")}: ${value}`).join("\n\n");
      const feedback = form.querySelector(".feedback");
      if (feedback) {
        feedback.textContent = "Draft saved on this device. Review the preview before you treat it as governed work.";
        feedback.className = "feedback good";
      }
      mark(form.dataset.required || "artifact");
    });
  });

  document.querySelectorAll("[data-final-check]").forEach((button) => button.addEventListener("click", () => {
    const form = document.querySelector(`form[data-artifact="${button.dataset.finalCheck}"]`);
    const feedback = button.parentElement.querySelector(".feedback");
    const complete = form && [...form.querySelectorAll("input,textarea,select")].every((field) => String(field.value).trim().length >= Number(field.dataset.min || 3));
    feedback.textContent = complete
      ? "Applied check passed. Your artifact contains the minimum specific evidence for review."
      : "Revise the artifact. Every required field needs a specific utility statement, identifier, source, rule, or decision.";
    feedback.className = `feedback ${complete ? "good" : "bad"}`;
    if (complete) mark(button.dataset.required || "applied");
  }));

  document.querySelector("[data-complete]")?.addEventListener("click", (event) => {
    event.currentTarget.textContent = "Lesson complete on this device";
    event.currentTarget.disabled = true;
    const live = document.querySelector("#live");
    if (live) live.textContent = "Lesson marked complete in local working state. No credential or production record was issued.";
  });

  const tooltip = document.querySelector("#tt");
  const hideTip = () => tooltip?.classList.remove("on");
  document.querySelectorAll(".term[data-def]").forEach((term) => {
    const show = () => {
      if (!tooltip) return;
      const box = term.getBoundingClientRect();
      tooltip.textContent = term.dataset.def;
      tooltip.style.left = `${Math.min(innerWidth - 160, Math.max(160, box.left + box.width / 2))}px`;
      tooltip.style.top = `${Math.max(70, box.top)}px`;
      tooltip.classList.add("on");
    };
    term.addEventListener("mouseenter", show);
    term.addEventListener("focus", show);
    term.addEventListener("mouseleave", hideTip);
    term.addEventListener("blur", hideTip);
    term.tabIndex = 0;
  });

  addEventListener("scroll", () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    document.documentElement.style.setProperty("--read", `${max > 0 ? (scrollY / max) * 100 : 0}%`);
  }, { passive: true });
  updateComplete();
  window.MBM = { mark, state, save };
})();
