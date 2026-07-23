const { chromium } = require("playwright");
const { createHash } = require("crypto");
const { readFileSync, writeFileSync } = require("fs");
const { resolve } = require("path");

const root = resolve(__dirname, "..");
const curriculum = resolve(root, "curriculum");
const base = process.env.MBM_PREVIEW_URL || "http://127.0.0.1:8765/apps/meaning-before-models/curriculum/";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const lessons = [
  "module-01-rdf-in-15-minutes.html",
  "module-02-anatomy-of-a-triple.html",
  "module-03-which-pump-do-you-mean.html",
  "module-04-from-triples-to-a-utility-knowledge-graph.html",
  "module-05-five-layers-of-meaning.html",
  "module-06-taxonomies-vocabularies-and-rdfs.html",
  "module-07-ontology-engineering-in-plain-language.html",
  "module-08-ask-the-graph-with-sparql.html",
  "module-09-reasoning-and-inference-with-owl.html",
  "module-10-validation-with-shacl.html",
  "module-11-references-provenance-authority-and-time.html",
  "module-12-running-knowledge-spine.html",
  "module-13-map-meaning-to-data.html",
  "module-14-virtualize-cache-index-or-materialize.html",
  "module-15-structured-and-unstructured-knowledge.html",
  "module-16-context-engines-and-runtime-ai-context.html",
  "module-17-bi-rag-graph-and-agentic-applications.html",
  "module-18-design-the-one-water-knowledge-spine.html",
];

function digestSource() {
  const hash = createHash("sha256");
  for (const file of [...lessons, "module-05-golden.css", "course-module.js"]) {
    hash.update(file);
    hash.update(readFileSync(resolve(curriculum, file)));
  }
  return hash.digest("hex");
}

async function solveQuiz(quiz) {
  const type = await quiz.getAttribute("data-quiz-type");
  if (type === "matching") {
    const pairs = await quiz.locator("[data-pair]").evaluateAll(nodes => [...new Set(nodes.map(node => node.dataset.pair))]);
    for (const pair of pairs) {
      await quiz.locator(`[data-side="left"][data-pair="${pair}"]`).click();
      await quiz.locator(`[data-side="right"][data-pair="${pair}"]`).click();
    }
  } else if (type === "fill-in") {
    const input = quiz.locator("input[data-answer]");
    await input.fill(await input.getAttribute("data-answer"));
    await quiz.locator("[data-check-generic]").click();
  } else if (type === "ordering") {
    const list = quiz.locator("[data-order]").first().locator("..");
    const count = await list.locator("[data-order]").count();
    for (let target = 0; target < count; target += 1) {
      const order = await list.locator("[data-order]").evaluateAll(nodes => nodes.map(node => Number(node.dataset.order)));
      const current = order.indexOf(target);
      if (current !== target) {
        await list.locator("[data-order]").nth(target).click();
        await list.locator("[data-order]").nth(current).click();
      }
    }
    await quiz.locator("[data-check-generic]").click();
  } else if (type === "reflection") {
    await quiz.locator("[data-reflection]").fill("The utility owner reviews the evidence, names the limitation, and records the next authorized decision.");
    await quiz.locator("[data-check-generic]").click();
  } else if (type === "estimate") {
    const input = quiz.locator("[data-estimate]");
    await input.evaluate(node => {
      node.value = node.dataset.answer;
      node.dispatchEvent(new Event("input", { bubbles: true }));
    });
    await quiz.locator("[data-check-generic]").click();
  } else if (["classify", "multi-select", "capstone-rubric"].includes(type)) {
    const correct = quiz.locator('.option-check[data-correct="1"]');
    for (let index = 0; index < await correct.count(); index += 1) await correct.nth(index).click();
    await quiz.locator("[data-check-generic]").click();
  } else {
    await quiz.locator('[data-correct="1"]').click();
    await quiz.locator("[data-check-generic]").click();
  }
  await quiz.locator(".feedback.good").waitFor({ state: "visible" });
}

async function inspectLesson(browser, lesson, mode) {
  const mobile = mode === "mobile";
  const page = await browser.newPage({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 1000 },
    reducedMotion: mobile ? "reduce" : "no-preference",
  });
  const errors = [];
  page.on("console", message => {
    if (message.type() === "error") errors.push(`console: ${message.text()}`);
  });
  page.on("pageerror", error => errors.push(`page: ${error.message}`));
  await page.goto(base + lesson, { waitUntil: "networkidle" });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: "networkidle" });

  const number = lesson.slice(7, 9);
  const graphTrigger = page.locator("[data-open-graph]:visible").first();
  await graphTrigger.click();
  if (await page.locator("#graphDrawer").getAttribute("aria-hidden") !== "false") errors.push("graph drawer did not open");
  await page.keyboard.press("Escape");
  await page.waitForTimeout(60);
  if (await page.locator("#graphDrawer").getAttribute("aria-hidden") !== "true") errors.push("graph drawer did not close");
  if (!await graphTrigger.evaluate(node => document.activeElement === node)) errors.push("graph trigger did not regain focus");

  const frontScreenshot = `/private/tmp/mbm-qaqc-${number}-${mode}-top.png`;
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(60);
  await page.screenshot({ path: frontScreenshot, fullPage: false });

  const deck = page.locator("#question-deck");
  await deck.scrollIntoViewIfNeeded();
  const firstCard = deck.locator(".flip-question").first();
  await firstCard.focus();
  await page.keyboard.press("Enter");
  await page.waitForTimeout(mobile ? 20 : 560);
  const firstState = await firstCard.evaluate(node => {
    const front = node.querySelector(".flip-front");
    const back = node.querySelector(".flip-back");
    const rect = back.getBoundingClientRect();
    const hit = document.elementsFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
    return {
      pressed: node.getAttribute("aria-pressed"),
      frontText: front.textContent.trim(),
      backText: back.textContent.trim(),
      backOnTop: hit.some(item => back === item || back.contains(item)),
      frontDisplay: getComputedStyle(front).display,
      backDisplay: getComputedStyle(back).display,
      color: getComputedStyle(front).color,
      backgroundImage: getComputedStyle(front).backgroundImage,
      width: rect.width,
      height: rect.height,
    };
  });
  if (firstState.pressed !== "true") errors.push("flip card did not update pressed state");
  if (!firstState.backText.includes("ANSWER 1") || firstState.backText.length < 45) errors.push("flip card answer is missing or too short");
  if (mobile) {
    if (firstState.frontDisplay !== "none" || firstState.backDisplay === "none") errors.push("reduced-motion flip state is not explicit");
  } else if (!firstState.backOnTop) {
    errors.push("animated flip answer is not the visible face");
  }
  if (firstState.color !== "rgb(15, 23, 40)") errors.push(`question card text is not dark on the light face: ${firstState.color}`);
  if (!firstState.backgroundImage || firstState.backgroundImage === "none") errors.push("question card has no intentional light surface");
  if (firstState.width < 220 || firstState.height < 110) errors.push("question card geometry collapsed");

  const cards = deck.locator(".flip-question");
  for (let index = 0; index < await cards.count(); index += 1) {
    if (index === 0) continue;
    await cards.nth(index).click();
  }
  await page.waitForTimeout(mobile ? 20 : 560);
  if (await deck.locator(".flip-question.turned").count() !== 4) errors.push("not all four question cards reached the answer state");
  if (!await deck.locator(".feedback.good").isVisible()) errors.push("question deck completion feedback is missing");
  const cardScreenshot = `/private/tmp/mbm-qaqc-${number}-${mode}-cards.png`;
  await page.screenshot({ path: cardScreenshot, fullPage: false });

  const actionPanels = page.locator(".visual-panel:has([data-visual-action])");
  let interactiveVisuals = 0;
  for (let index = 0; index < await actionPanels.count(); index += 1) {
    const panel = actionPanels.nth(index);
    const result = panel.locator(".visual-insight");
    const before = await result.textContent();
    await panel.locator("[data-visual-action]").first().click();
    const after = await result.textContent();
    if (after === before || after.length < 25) errors.push(`visual interaction ${index + 1} did not explain its result`);
    else interactiveVisuals += 1;
  }

  const process = page.locator("#process-lab");
  const steps = process.locator("[data-step]");
  for (let index = 0; index < await steps.count(); index += 1) await steps.nth(index).click();
  if (!await process.locator(".feedback.good").isVisible()) errors.push("mechanism lab did not complete");
  const processText = await process.locator("[data-step-detail]").textContent();
  if (processText.length < 80) errors.push("mechanism lab result is generic or incomplete");

  for (const id of ["#opening-quiz", "#mid-quiz", "#boundary-quiz"]) await solveQuiz(page.locator(id));

  const form = page.locator("#work-product");
  const fields = form.locator("textarea");
  for (let index = 0; index < await fields.count(); index += 1) {
    const value = index === 7
      ? "A named human must review and approve the result before any utility action."
      : `Specific utility evidence statement ${index + 1} names the source, relationship, owner, and review boundary.`;
    await fields.nth(index).fill(value);
  }
  await form.locator('button[type="submit"]').click();
  await page.locator("#applied-check [data-check-applied]").click();
  if (!await page.locator("#applied-check .feedback.good").isVisible()) errors.push("applied assessment did not pass a complete work product");
  if (await page.locator("[data-complete]").isDisabled()) errors.push("completion remained disabled after all required evidence");

  const evidence = await page.evaluate(() => {
    const visuals = [...document.querySelectorAll('[id^="visual-"][data-visual-shape]')];
    const sequence = [...document.querySelectorAll("[data-opening-decision],#question-deck,[id^='visual-'],#process-lab,#mid-quiz,#boundary-quiz,#work-product")]
      .map(node => node.dataset.visualType || node.dataset.quizType || node.dataset.purposefulInteraction || node.id);
    const unlabeledButtons = [...document.querySelectorAll("button")].filter(button =>
      !(button.getAttribute("aria-label") || button.getAttribute("aria-labelledby") || button.textContent.trim())
    ).length;
    return {
      title: document.querySelector("h1")?.textContent.trim(),
      experience: document.body.dataset.experience,
      cardLayout: document.querySelector(".question-flips")?.dataset.cardLayout,
      visualTypes: visuals.map(node => node.dataset.visualType),
      visualShapes: visuals.map(node => node.dataset.visualShape),
      quizTypes: [...document.querySelectorAll("[data-quiz-type][data-required]")].map(node => node.dataset.quizType),
      sequence,
      viewportWidth: innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      unlabeledButtons,
      requirementsDone: document.querySelectorAll(".req.done").length,
      requirementsTotal: document.querySelectorAll(".req").length,
      reducedTransition: getComputedStyle(document.querySelector(".drawer")).transitionDuration,
    };
  });
  if (evidence.visualTypes.length !== 4) errors.push(`expected four lesson visuals, found ${evidence.visualTypes.length}`);
  if (new Set(evidence.visualShapes).size !== 4) errors.push("lesson visual shapes are not distinct");
  if (new Set(evidence.quizTypes).size < 5) errors.push("lesson quiz sequence lacks variety");
  if (evidence.scrollWidth > evidence.viewportWidth + 1) errors.push(`horizontal overflow ${evidence.scrollWidth}/${evidence.viewportWidth}`);
  if (evidence.unlabeledButtons) errors.push(`${evidence.unlabeledButtons} unlabeled buttons`);
  if (evidence.requirementsDone !== evidence.requirementsTotal) errors.push(`only ${evidence.requirementsDone}/${evidence.requirementsTotal} completion requirements passed`);
  if (mobile && evidence.reducedTransition !== "0s") errors.push(`reduced-motion drawer transition remains ${evidence.reducedTransition}`);

  await page.close();
  return {
    lesson,
    module: number,
    mode,
    passed: errors.length === 0,
    errors,
    interactiveVisuals,
    screenshots: [frontScreenshot, cardScreenshot],
    flipCard: firstState,
    ...evidence,
  };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = [];
  for (const lesson of lessons) {
    results.push(await inspectLesson(browser, lesson, "desktop"));
    results.push(await inspectLesson(browser, lesson, "mobile"));
  }
  await browser.close();

  const desktop = results.filter(result => result.mode === "desktop");
  const experiences = desktop.map(result => result.experience);
  const cardLayouts = desktop.map(result => result.cardLayout);
  const sequences = desktop.map(result => result.sequence.join(" > "));
  const courseErrors = [];
  if (new Set(experiences).size !== lessons.length) courseErrors.push("every module must have a unique narrative architecture");
  if (new Set(cardLayouts).size !== lessons.length) courseErrors.push("every module must have a unique question-card composition");
  for (let index = 1; index < desktop.length; index += 1) {
    if (sequences[index] === sequences[index - 1]) courseErrors.push(`modules ${index} and ${index + 1} have identical rendered component sequences`);
    if (desktop[index].visualShapes.join("|") === desktop[index - 1].visualShapes.join("|")) courseErrors.push(`modules ${index} and ${index + 1} repeat the same visual-shape sequence`);
    if (desktop[index].quizTypes.join("|") === desktop[index - 1].quizTypes.join("|")) courseErrors.push(`modules ${index} and ${index + 1} repeat the same quiz sequence`);
  }
  const failures = results.filter(result => !result.passed);
  const report = {
    schema: "owos-rendered-course-qa/v1",
    generatedAt: new Date().toISOString(),
    course: "meaning-before-models",
    sourceDigest: digestSource(),
    previewBase: base,
    lessons: lessons.length,
    renderedViews: results.length,
    passed: failures.length === 0 && courseErrors.length === 0,
    courseErrors,
    failures,
    moduleResults: results,
  };
  writeFileSync(resolve(root, "qa", "rendered-browser-report.json"), JSON.stringify(report, null, 2) + "\n");
  console.log(JSON.stringify({
    passed: report.passed,
    lessons: report.lessons,
    renderedViews: report.renderedViews,
    uniqueExperiences: new Set(experiences).size,
    uniqueCardLayouts: new Set(cardLayouts).size,
    failures: failures.map(({ lesson, mode, errors }) => ({ lesson, mode, errors })),
    courseErrors,
    sourceDigest: report.sourceDigest,
  }, null, 2));
  if (!report.passed) process.exit(1);
})().catch(error => {
  console.error(error);
  process.exit(1);
});
