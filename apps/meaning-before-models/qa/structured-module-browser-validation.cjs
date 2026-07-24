const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "../../..");
const base = "http://127.0.0.1:8787";
const lessonPath = "/repo/apps/meaning-before-models/dist/site/lesson-meaning-before-models-01-rdf-in-15-minutes.html";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const captureRoot = path.join(__dirname, "rendered/module-01");

function durationMs(value) {
  if (!value) return 0;
  return value.endsWith("ms") ? Number.parseFloat(value) : Number.parseFloat(value) * 1000;
}

async function inspectPreview(browser, mode) {
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
  page.on("response", (response) => {
    if (response.status() >= 400 && !response.url().endsWith("favicon.ico")) {
      errors.push(`${response.status()} ${response.url()}`);
    }
  });
  await page.goto(base + lessonPath, {waitUntil: "networkidle"});
  await page.waitForSelector("main");

  const graph = page.getByRole("button", {name: "Graph"}).first();
  await graph.click();
  const graphDrawer = page.locator('[data-drawer="graph"]');
  const graphOpen = await graphDrawer.getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await graphDrawer.getAttribute("aria-hidden") === "true";
  const graphFocusReturned = await graph.evaluate((node) => document.activeElement === node);

  const glossary = page.getByRole("button", {name: "Glossary"});
  await glossary.click();
  const glossaryOpen = await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden") === "false";
  await page.getByRole("button", {name: "Close"}).last().click();

  const opening = page.locator("#mbm01-opening-choice");
  await opening.getByRole("button", {name: "Pump P-104 serves Pressure Zone 3."}).click();
  await opening.getByRole("button", {name: "Check my answer"}).click();

  const triple = page.locator("#mbm01-triple-builder");
  await triple.locator("select").nth(0).selectOption("Pump_P104");
  await triple.locator("select").nth(1).selectOption("serves");
  await triple.locator("select").nth(2).selectOption("Pressure_Zone_3");
  await triple.getByRole("button", {name: "Check triple"}).click();
  await triple.getByRole("button", {name: "Reverse the ends"}).click();
  await triple.locator("textarea").fill("The direction now claims that the pressure zone serves the pump.");
  await triple.getByRole("button", {name: "Finish construction"}).click();

  const cards = page.locator("#mbm01-term-cards [data-flip-card]");
  for (let index = 0; index < await cards.count(); index += 1) {
    await cards.nth(index).click();
  }

  const tracer = page.locator("#mbm01-path-tracer");
  const edges = tracer.locator("[data-edge-index]");
  for (let index = 0; index < await edges.count(); index += 1) {
    await edges.nth(index).click();
  }

  const pathClaim = page.locator("#mbm01-path-claim");
  await pathClaim.getByRole("button", {name: /Service Account 901 is linked/}).click();
  await pathClaim.getByRole("button", {name: "Check my answer"}).click();

  const card = page.locator("#mbm01-relationship-card form");
  await card.locator('[name="subject"]').fill("Lift_Station_7");
  await card.locator('[name="predicate"]').fill("flows_to");
  await card.locator('[name="object"]').fill("Treatment_Plant_2");
  await card.locator('[name="source"]').fill("Approved wastewater network model");
  await card.locator('[name="question"]').fill("Which treatment plant receives flow from this lift station?");
  await card.getByRole("button", {name: "Save Relationship Card"}).click();

  const state = await page.evaluate(() => {
    const images = [...document.images];
    const darkSurfaces = [...document.querySelectorAll(".component-header, .conclusion, .connected article, footer")];
    return {
      h1Count: document.querySelectorAll("h1").length,
      visualCount: document.querySelectorAll(".learning-visual").length,
      imagesLoaded: images.every((image) => image.complete && image.naturalWidth > 0),
      imageWidths: images.map((image) => image.naturalWidth),
      requiredComplete: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
      completeEnabled: !document.querySelector("[data-complete-module]").disabled,
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      emptyButtons: [...document.querySelectorAll("button")].filter(
        (button) => !button.textContent.trim() && !button.getAttribute("aria-label")
      ).length,
      darkTextFailures: darkSurfaces.filter((node) => {
        const color = getComputedStyle(node).color;
        const match = color.match(/\d+/g)?.map(Number) || [];
        return match.length >= 3 && match[0] < 180 && match[1] < 180 && match[2] < 180;
      }).length,
      maxTransitionMs: Math.max(
        0,
        ...[...document.querySelectorAll("*")].map((node) => {
          const duration = getComputedStyle(node).transitionDuration.split(",")[0];
          return duration.endsWith("ms") ? Number.parseFloat(duration) : Number.parseFloat(duration) * 1000;
        }).filter(Number.isFinite)
      ),
    };
  });

  const captureDir = path.join(captureRoot, mode);
  fs.mkdirSync(captureDir, {recursive: true});
  await page.screenshot({path: path.join(captureDir, "full-page.png"), fullPage: true});
  await page.locator("#mbm01-triple-anatomy").screenshot({path: path.join(captureDir, "triple-anatomy.png")});
  await page.locator("#mbm01-term-cards").screenshot({path: path.join(captureDir, "flip-cards.png")});
  await context.close();

  return {
    mode,
    errors,
    graphOpen,
    graphClosed,
    graphFocusReturned,
    glossaryOpen,
    ...state,
  };
}

async function inspectStudio(browser) {
  const page = await browser.newPage({viewport: {width: 1440, height: 1000}});
  const errors = [];
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(base, {waitUntil: "networkidle"});
  await page.getByRole("button", {name: "RDF in 15 Minutes"}).click();
  await page.waitForSelector("[data-module-workspace]:not([hidden])");
  const tabs = await page.locator("[data-tabs] button").allTextContents();
  await page.getByRole("button", {name: "Visuals", exact: true}).click();
  const visualManifestVisible = (await page.locator("[data-editor]").inputValue()).includes("mbm01-utility-scene");
  await page.getByRole("button", {name: "Validate package"}).click();
  await page.waitForFunction(() => document.querySelector("[data-toast]").textContent.includes("Package valid."));
  await page.getByRole("button", {name: "Build preview"}).click();
  await page.waitForSelector("[data-preview-view]:not([hidden])");
  await page.locator("[data-preview]").contentFrame().locator("h1").waitFor();
  const previewTitle = await page.locator("[data-preview]").contentFrame().locator("h1").textContent();
  const emptyHidden = await page.locator("[data-empty]").evaluate((node) => getComputedStyle(node).display === "none");
  const previewWidth = await page.locator("[data-preview]").evaluate((node) => node.getBoundingClientRect().width);
  fs.mkdirSync(captureRoot, {recursive: true});
  await page.screenshot({path: path.join(captureRoot, "author-studio.png"), fullPage: true});
  await page.close();
  return {errors, tabs, visualManifestVisible, previewTitle, emptyHidden, previewWidth};
}

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: chrome});
  const studio = await inspectStudio(browser);
  const desktop = await inspectPreview(browser, "desktop");
  const tablet = await inspectPreview(browser, "tablet");
  const phone = await inspectPreview(browser, "phone");
  await browser.close();

  const results = [desktop, tablet, phone];
  const failures = [];
  if (studio.errors.length) failures.push({studio: studio.errors});
  if (!studio.visualManifestVisible) failures.push({studio: "visual manifest did not load"});
  if (studio.previewTitle !== "RDF in 15 Minutes") failures.push({studio: "compiled preview did not load"});
  if (studio.tabs.length !== 10) failures.push({studio: `expected 10 authoring views, found ${studio.tabs.length}`});
  if (!studio.emptyHidden) failures.push({studio: "empty state remained visible after module selection"});
  if (studio.previewWidth < 900) failures.push({studio: `desktop preview defaulted to ${studio.previewWidth}px`});
  for (const result of results) {
    if (result.errors.length) failures.push({mode: result.mode, errors: result.errors});
    if (!result.graphOpen || !result.graphClosed || !result.graphFocusReturned || !result.glossaryOpen) {
      failures.push({mode: result.mode, drawers: result});
    }
    if (result.h1Count !== 1 || result.visualCount !== 3 || !result.imagesLoaded) {
      failures.push({mode: result.mode, visuals: result});
    }
    if (!result.requiredComplete || !result.completeEnabled) {
      failures.push({mode: result.mode, completion: result});
    }
    if (result.scrollWidth > result.width + 1 || result.emptyButtons || result.darkTextFailures) {
      failures.push({mode: result.mode, layout: result});
    }
    if (result.mode === "phone" && result.maxTransitionMs > 1) {
      failures.push({mode: result.mode, reducedMotionMs: result.maxTransitionMs});
    }
  }
  console.log(JSON.stringify({
    authorStudio: studio,
    pageRuns: results,
    failureCount: failures.length,
    failures,
  }, null, 2));
  if (failures.length) process.exitCode = 1;
})();
