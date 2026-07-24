const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const lesson = process.env.OWOS_LESSON_URL || "file:///Users/apas/dev/owos-learning-content/apps/meaning-before-models/modules/module-03-which-pump-do-you-mean/build/index.html";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const captureRoot = path.join(__dirname, "rendered/module-03");

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
  page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(lesson, {waitUntil: "load"});
  await page.waitForSelector("main");
  await page.evaluate(async () => Promise.all([...document.images].map((image) => image.complete && image.naturalWidth > 0 ? Promise.resolve() : image.decode())));

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
  await choose("mbm03-opening-hold");

  const evidence = page.locator("#mbm03-evidence-check");
  const options = evidence.locator("[data-multi-option]");
  for (let index = 0; index < await options.count(); index += 1) {
    const option = options.nth(index);
    if (await option.getAttribute("data-correct") === "true") await option.check();
  }
  await evidence.getByRole("button", {name: "Check the packet"}).click();

  const matching = page.locator("#mbm03-role-check");
  const matchFields = matching.locator("[data-match-answer]");
  for (let index = 0; index < await matchFields.count(); index += 1) {
    const field = matchFields.nth(index);
    await field.selectOption(await field.getAttribute("data-match-answer"));
  }
  await matching.getByRole("button", {name: "Check the matches"}).click();

  const docket = page.locator("#mbm03-identity-docket");
  const records = docket.locator("[data-docket-record]");
  for (let index = 0; index < await records.count(); index += 1) {
    const record = records.nth(index);
    await record.locator("select").selectOption(await record.getAttribute("data-answer"));
  }
  await docket.getByRole("button", {name: "Submit findings"}).click();

  const blast = page.locator("#mbm03-false-merge-trace");
  const paths = blast.locator("[data-failure-trigger]");
  for (let index = 0; index < await paths.count(); index += 1) await paths.nth(index).click();
  await choose("mbm03-control-check");
  await choose("mbm03-transfer-check");

  const artifact = page.locator("#mbm03-identity-crosswalk form");
  const fields = artifact.locator("[required]");
  for (let index = 0; index < await fields.count(); index += 1) {
    await fields.nth(index).fill(`Specific reviewable Module 03 identity evidence ${index + 1}`);
  }
  await artifact.getByRole("button", {name: "Save Identity Crosswalk and Conflict Queue"}).click();

  const state = await page.evaluate(() => ({
    h1Count: document.querySelectorAll("h1").length,
    sectionCount: document.querySelectorAll(".lesson-section").length,
    visualCount: document.querySelectorAll(".learning-visual").length,
    visualTypes: [...document.querySelectorAll(".learning-visual")].map((node) => node.dataset.visualType),
    imagesLoaded: [...document.images].every((image) => image.complete && image.naturalWidth > 0),
    requiredComplete: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
    completeEnabled: !document.querySelector("[data-complete-module]").disabled,
    width: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    emptyButtons: [...document.querySelectorAll("button")].filter((button) => !button.textContent.trim() && !button.getAttribute("aria-label")).length,
    maxTransitionMs: Math.max(0, ...[...document.querySelectorAll("*")].map((node) => {
      const duration = getComputedStyle(node).transitionDuration.split(",")[0];
      return duration.endsWith("ms") ? Number.parseFloat(duration) : Number.parseFloat(duration) * 1000;
    }).filter(Number.isFinite)),
  }));
  const captureDir = path.join(captureRoot, mode);
  fs.mkdirSync(captureDir, {recursive: true});
  await page.screenshot({path: path.join(captureDir, "full-page.png"), fullPage: true});
  await docket.screenshot({path: path.join(captureDir, "identity-docket.png")});
  await blast.screenshot({path: path.join(captureDir, "blast-radius.png")});
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
    if (result.h1Count !== 1 || result.sectionCount !== 9 || result.visualCount !== 5 || !result.imagesLoaded) failures.push({mode: result.mode, visuals: result});
    if (new Set(result.visualTypes).size !== 5) failures.push({mode: result.mode, visualTypes: result.visualTypes});
    if (!result.requiredComplete || !result.completeEnabled) failures.push({mode: result.mode, completion: result});
    if (result.scrollWidth > result.width + 1 || result.emptyButtons) failures.push({mode: result.mode, layout: result});
    if (result.mode === "phone" && result.maxTransitionMs > 1) failures.push({mode: result.mode, reducedMotionMs: result.maxTransitionMs});
  }
  console.log(JSON.stringify({pageRuns: results, failureCount: failures.length, failures}, null, 2));
  if (failures.length) process.exitCode = 1;
})();
