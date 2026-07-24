const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const lesson = process.env.OWOS_LESSON_URL || "file:///Users/apas/dev/owos-learning-content/apps/meaning-before-models/modules/module-02-anatomy-of-a-triple/build/index.html";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const captureRoot = path.join(__dirname, "rendered/module-02");

async function inspect(browser, mode) {
  const mobile = mode === "phone";
  const tablet = mode === "tablet";
  const context = await browser.newContext({
    viewport: mobile ? {width: 390, height: 844} : tablet ? {width: 820, height: 1080} : {width: 1440, height: 1000},
    reducedMotion: mobile ? "reduce" : "no-preference",
    hasTouch: mobile || tablet,
    isMobile: mobile,
  });
  const page = await context.newPage();
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(lesson, {waitUntil: "load"});
  await page.waitForSelector("main");

  const graph = page.getByRole("button", {name: "Graph"}).first();
  await graph.click();
  const graphDrawer = page.locator('[data-drawer="graph"]');
  const graphOpen = await graphDrawer.getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await graphDrawer.getAttribute("aria-hidden") === "true";
  const graphFocusReturned = await graph.evaluate((node) => document.activeElement === node);
  await page.getByRole("button", {name: "Glossary"}).click();
  const glossaryOpen = await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");

  async function choose(id) {
    const group = page.locator(`#${id}`);
    await group.locator("[data-choice][data-correct=true]").click();
    await group.getByRole("button", {name: "Check my answer"}).click();
  }
  await choose("mbm02-opening-repair");
  await choose("mbm02-identity-check");

  const router = page.locator("#mbm02-object-router");
  const routeItems = router.locator("[data-route-item]");
  for (let index = 0; index < await routeItems.count(); index += 1) {
    const item = routeItems.nth(index);
    const answer = await item.getAttribute("data-answer");
    await item.locator(`[data-route-choice="${answer}"]`).click();
  }

  const literal = page.locator("#mbm02-literal-check");
  const options = literal.locator("[data-multi-option]");
  for (let index = 0; index < await options.count(); index += 1) {
    const option = options.nth(index);
    if (await option.getAttribute("data-correct") === "true") await option.check();
  }
  await literal.getByRole("button", {name: "Check the packet"}).click();

  const bench = page.locator("#mbm02-triple-repair-bench");
  const cards = bench.locator("[data-repair-card]");
  for (let index = 0; index < await cards.count(); index += 1) {
    const card = cards.nth(index);
    await card.locator("[data-defect-field]").selectOption(await card.getAttribute("data-defect"));
    await card.locator("[data-repair-field]").selectOption(await card.getAttribute("data-repair"));
  }
  await bench.getByRole("button", {name: "Review all repairs"}).click();
  await choose("mbm02-repair-boundary");
  await choose("mbm02-serialization-check");
  await choose("mbm02-transfer-check");

  const artifact = page.locator("#mbm02-triple-deck form");
  const fields = artifact.locator("[required]");
  for (let index = 0; index < await fields.count(); index += 1) {
    await fields.nth(index).fill(`Specific reviewable Module 02 evidence ${index + 1}`);
  }
  await artifact.getByRole("button", {name: "Save Reviewed Triple Deck"}).click();

  const state = await page.evaluate(() => {
    const images = [...document.images];
    return {
      h1Count: document.querySelectorAll("h1").length,
      sectionCount: document.querySelectorAll(".lesson-section").length,
      visualCount: document.querySelectorAll(".learning-visual").length,
      visualTypes: [...document.querySelectorAll(".learning-visual")].map((node) => node.dataset.visualType),
      imagesLoaded: images.every((image) => image.complete && image.naturalWidth > 0),
      requiredComplete: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
      completeEnabled: !document.querySelector("[data-complete-module]").disabled,
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      emptyButtons: [...document.querySelectorAll("button")].filter(
        (button) => !button.textContent.trim() && !button.getAttribute("aria-label")
      ).length,
      maxTransitionMs: Math.max(0, ...[...document.querySelectorAll("*")].map((node) => {
        const duration = getComputedStyle(node).transitionDuration.split(",")[0];
        return duration.endsWith("ms") ? Number.parseFloat(duration) : Number.parseFloat(duration) * 1000;
      }).filter(Number.isFinite)),
    };
  });

  const captureDir = path.join(captureRoot, mode);
  fs.mkdirSync(captureDir, {recursive: true});
  await page.screenshot({path: path.join(captureDir, "full-page.png"), fullPage: true});
  await page.locator("#mbm02-object-router").screenshot({path: path.join(captureDir, "object-router.png")});
  await page.locator("#mbm02-triple-repair-bench").screenshot({path: path.join(captureDir, "repair-bench.png")});
  await context.close();
  return {mode, errors, graphOpen, graphClosed, graphFocusReturned, glossaryOpen, ...state};
}

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: chrome});
  const results = [];
  for (const mode of ["desktop", "tablet", "phone"]) results.push(await inspect(browser, mode));
  await browser.close();
  const failures = [];
  for (const result of results) {
    if (result.errors.length) failures.push({mode: result.mode, errors: result.errors});
    if (!result.graphOpen || !result.graphClosed || !result.graphFocusReturned || !result.glossaryOpen) failures.push({mode: result.mode, drawers: result});
    if (result.h1Count !== 1 || result.sectionCount !== 8 || result.visualCount !== 5 || !result.imagesLoaded) failures.push({mode: result.mode, visuals: result});
    if (new Set(result.visualTypes).size !== 5) failures.push({mode: result.mode, visualTypes: result.visualTypes});
    if (!result.requiredComplete || !result.completeEnabled) failures.push({mode: result.mode, completion: result});
    if (result.scrollWidth > result.width + 1 || result.emptyButtons) failures.push({mode: result.mode, layout: result});
    if (result.mode === "phone" && result.maxTransitionMs > 1) failures.push({mode: result.mode, reducedMotionMs: result.maxTransitionMs});
  }
  console.log(JSON.stringify({pageRuns: results, failureCount: failures.length, failures}, null, 2));
  if (failures.length) process.exitCode = 1;
})();
