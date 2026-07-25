const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const target = process.env.OWOS_TARGET || "build";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const captureRoot = path.join(__dirname, "rendered/module-18");

function lessonUrl() {
  if (process.env.OWOS_BASE_URL) {
    const lessonPath = process.env.OWOS_LESSON_PATH || "/lesson-meaning-before-models-18-graph-grounded-agentic-applications.html";
    return `${process.env.OWOS_BASE_URL.replace(/\/$/, "")}${lessonPath}?module18=1`;
  }
  if (target === "dist") {
    return `file://${path.join(root, "dist/site/lesson-meaning-before-models-18-graph-grounded-agentic-applications.html")}`;
  }
  return `file://${path.join(root, "modules/module-18-graph-grounded-agentic-applications/build/index.html")}`;
}

async function complete(page) {
  let exportPassed = true;
  for (const group of await page.locator("[data-choice-group]").all()) {
    await group.locator("[data-choice][data-correct=true]").click();
    await group.locator("[data-check-choice]").click();
  }
  for (const group of await page.locator("[data-matching]").all()) {
    for (const field of await group.locator("[data-match-answer]").all()) {
      await field.selectOption(await field.getAttribute("data-match-answer"));
    }
    await group.locator("[data-check-matching]").click();
  }
  for (const group of await page.locator("[data-multi-select]").all()) {
    for (const option of await group.locator("[data-multi-option]").all()) {
      if (await option.getAttribute("data-correct") === "true") await option.check();
    }
    await group.locator("[data-check-multi]").click();
  }
  for (const group of await page.locator("[data-flip-group]").all()) {
    for (const card of await group.locator("[data-flip-card]").all()) await card.click();
  }
  const labs = [
    ["[data-agent-action-control]", "[data-action-case]", "data-action-choice"],
    ["[data-idempotency-recovery]", "[data-retry-case]", "data-retry-choice"],
  ];
  for (const [labSelector, caseSelector, choiceAttribute] of labs) {
    for (const lab of await page.locator(labSelector).all()) {
      for (const card of await lab.locator(caseSelector).all()) {
        const answer = await card.getAttribute("data-answer");
        await card.locator(`[${choiceAttribute}="${answer}"]`).click();
      }
    }
  }
  for (const form of await page.locator("[data-work-product]").all()) {
    let index = 0;
    for (const field of await form.locator("input[required]:not([type=radio]), textarea[required], select[required]").all()) {
      await field.fill(`Specific controlled operating boundary and evidence statement ${++index}`);
    }
    await form.locator('input[name="contract_defense"][data-correct="true"]').check();
    await form.locator('button[type="submit"]').click();
    const downloadPromise = page.waitForEvent("download");
    await form.locator("[data-export-artifact]").click();
    const download = await downloadPromise;
    exportPassed = exportPassed && download.suggestedFilename().endsWith(".json");
  }
  return exportPassed;
}

async function inspectVisuals(page, mobileCompositionExpected) {
  const results = [];
  for (const visual of await page.locator(".learning-visual").all()) {
    const id = await visual.getAttribute("id");
    const overview = visual.locator("[data-visual-overview]");
    const frame = visual.locator(".visual-frame");
    const composition = visual.locator("[data-mobile-visual-composition]");
    const trigger = visual.locator("[data-open-visual-detail]");
    const dialog = visual.locator("[data-visual-detail]");
    const pan = dialog.locator("[data-visual-pan]");
    const detailImage = dialog.locator("[data-visual-detail-image]");
    const before = await overview.boundingBox();
    const frameBox = await frame.boundingBox();
    const overviewFits = Boolean(before && frameBox && before.width <= frameBox.width + 1);
    const frameScrollLeft = await frame.evaluate((node) => node.scrollLeft);
    const frameScrollable = await frame.evaluate((node) => node.scrollWidth > node.clientWidth + 1);
    const compositionVisible = await composition.isVisible();

    await trigger.focus();
    await page.keyboard.press("Enter");
    const dialogOpen = await dialog.evaluate((node) => node.open);
    const initialWidth = (await detailImage.boundingBox())?.width || 0;
    await dialog.locator("[data-visual-zoom-in]").click();
    const zoomStatus = await dialog.locator("[data-visual-zoom-status]").textContent();
    const zoomedWidth = (await detailImage.boundingBox())?.width || 0;
    const zoomMetrics = await detailImage.evaluate((node) => ({
      inlineStyle: node.parentElement.getAttribute("style"),
      canvasComputedWidth: getComputedStyle(node.parentElement).width,
      canvasRectWidth: node.parentElement.getBoundingClientRect().width,
      computedWidth: getComputedStyle(node).width,
      panClientWidth: node.parentElement.parentElement.clientWidth,
      panScrollWidth: node.parentElement.parentElement.scrollWidth,
    }));
    await pan.focus();
    await page.keyboard.press("ArrowRight");
    await page.waitForTimeout(40);
    const panned = await pan.evaluate((node) => node.scrollLeft > 0);
    await dialog.locator("[data-visual-reset]").click();
    const resetStatus = await dialog.locator("[data-visual-zoom-status]").textContent();
    const resetScroll = await pan.evaluate((node) => node.scrollLeft === 0 && node.scrollTop === 0);
    await dialog.locator("[data-close-visual-detail]").click();
    const dialogClosed = !(await dialog.evaluate((node) => node.open));
    const focusReturned = await trigger.evaluate((node) => document.activeElement === node);
    const textEquivalentCount = await visual.locator(".visual-text-equivalent").count();

    results.push({
      id,
      overviewFits,
      frameScrollLeft,
      frameScrollable,
      compositionVisible,
      compositionExpected: mobileCompositionExpected,
      dialogOpen,
      initialWidth,
      zoomStatus: zoomStatus?.trim(),
      zoomedWidth,
      zoomMetrics,
      zoomed: zoomStatus?.trim() === "150%" && zoomedWidth > initialWidth,
      panned,
      reset: resetStatus?.trim() === "100%" && resetScroll,
      dialogClosed,
      focusReturned,
      textEquivalentCount,
    });
  }
  return results;
}

async function inspect(browser, mode) {
  const phone = mode === "phone" || mode === "reduced";
  const tablet = mode === "tablet";
  const zoom200 = mode === "zoom200";
  const zoom400 = mode === "zoom400";
  const context = await browser.newContext({
    viewport: phone ? { width: 390, height: 844 } : tablet ? { width: 820, height: 1080 } : zoom200 ? { width: 720, height: 1000 } : zoom400 ? { width: 360, height: 900 } : { width: 1440, height: 1000 },
    reducedMotion: mode === "reduced" ? "reduce" : "no-preference",
    hasTouch: phone || tablet,
    isMobile: false,
  });
  const page = await context.newPage();
  const errors = [];
  page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(lessonUrl(), { waitUntil: "load" });
  await page.waitForSelector("main");
  await page.evaluate(async () => Promise.all([...document.images].map((image) => image.complete && image.naturalWidth ? Promise.resolve() : image.decode())));

  const graph = page.getByRole("button", { name: "Graph" }).first();
  await graph.focus();
  await page.keyboard.press("Enter");
  const graphOpen = await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden") === "true";
  const focusReturned = await graph.evaluate((node) => document.activeElement === node);
  await page.getByRole("button", { name: "Glossary", exact: true }).click();
  const glossaryOpen = await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const community = page.getByRole("button", { name: "Community", exact: true }).first();
  await community.focus();
  await page.keyboard.press("Enter");
  const communityOpen = await page.locator('[data-drawer="community"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const communityFocusReturned = await community.evaluate((node) => document.activeElement === node);

  const visualChecks = await inspectVisuals(page, mode !== "desktop");
  const exportPassed = await complete(page);
  const state = await page.evaluate(() => ({
    h1: document.querySelectorAll("h1").length,
    sections: document.querySelectorAll(".lesson-section").length,
    visuals: document.querySelectorAll(".learning-visual").length,
    visualTypes: [...document.querySelectorAll(".learning-visual")].map((node) => node.dataset.visualType),
    interactions: document.querySelectorAll(".signature-component").length,
    assessmentTypes: [...document.querySelectorAll("[data-quiz-type]")].map((node) => node.dataset.quizType),
    images: [...document.images].every((image) => image.complete && image.naturalWidth > 0),
    completed: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
    enabled: !document.querySelector("[data-complete-module]").disabled,
    width: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    emptyButtons: [...document.querySelectorAll("button")].filter((button) => !button.textContent.trim() && !button.getAttribute("aria-label")).length,
    faqCount: document.querySelectorAll("[data-module-faq] details").length,
    maxTransition: Math.max(0, ...[...document.querySelectorAll("*")].map((node) => {
      const duration = getComputedStyle(node).transitionDuration.split(",")[0];
      return duration.endsWith("ms") ? Number.parseFloat(duration) : Number.parseFloat(duration) * 1000;
    }).filter(Number.isFinite)),
  }));

  const directory = path.join(captureRoot, mode);
  fs.mkdirSync(directory, { recursive: true });
  await page.screenshot({ path: path.join(directory, "full-page.png"), fullPage: true });
  for (const [index, visual] of (await page.locator(".learning-visual").all()).entries()) {
    await visual.screenshot({ path: path.join(directory, `visual-${index + 1}.png`) });
  }
  for (const [index, lab] of (await page.locator(".signature-component").all()).entries()) {
    await lab.screenshot({ path: path.join(directory, `signature-${index + 1}.png`) });
  }
  await context.close();
  return { mode, errors, graphOpen, graphClosed, focusReturned, glossaryOpen, communityOpen, communityFocusReturned, exportPassed, visualChecks, ...state };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const runs = [];
  const modes = (process.env.OWOS_MODES || "desktop,tablet,phone,zoom200,zoom400,reduced").split(",");
  for (const mode of modes) runs.push(await inspect(browser, mode));
  await browser.close();
  const failures = runs.filter((run) =>
    run.errors.length ||
    !run.graphOpen || !run.graphClosed || !run.focusReturned || !run.glossaryOpen ||
    !run.communityOpen || !run.communityFocusReturned || !run.exportPassed ||
    run.h1 !== 1 || run.sections !== 9 || run.visuals !== 5 ||
    new Set(run.visualTypes).size !== 5 || run.interactions !== 2 ||
    new Set(run.assessmentTypes).size !== 4 || !run.images || !run.completed || !run.enabled ||
    run.scrollWidth > run.width + 1 || run.emptyButtons || run.faqCount !== 8 ||
    run.visualChecks.some((visual) =>
      !visual.overviewFits || visual.frameScrollLeft !== 0 || visual.frameScrollable ||
      visual.compositionVisible !== visual.compositionExpected ||
      !visual.dialogOpen || (run.mode !== "reduced" && (!visual.zoomed || !visual.panned)) || !visual.reset ||
      !visual.dialogClosed || !visual.focusReturned || visual.textEquivalentCount < 2
    ) ||
    (run.mode === "reduced" && run.maxTransition > 1)
  );
  console.log(JSON.stringify({ pageRuns: runs, failureCount: failures.length, failures }, null, 2));
  if (failures.length) process.exitCode = 1;
})();
