const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const target = path.resolve(
  process.argv[2]
    || path.join(
      root,
      "concept-briefs/detention-retention-and-infiltration/dist/public-review-preview.html",
    ),
);
const outputDir = path.resolve(
  process.argv[3]
    || path.join(
      root,
      "concept-briefs/detention-retention-and-infiltration/dist/browser-qa",
    ),
);
const targetUrl = pathToFileURL(target).href;
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const modes = [
  { name: "desktop", width: 1440, height: 1000, reducedMotion: "no-preference" },
  { name: "phone-reduced-motion", width: 390, height: 844, reducedMotion: "reduce" },
];

fs.mkdirSync(outputDir, { recursive: true });

async function inspect(browser, mode) {
  const page = await browser.newPage({
    viewport: { width: mode.width, height: mode.height },
    reducedMotion: mode.reducedMotion,
  });
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto(targetUrl, { waitUntil: "load" });
  await page.waitForSelector(".path-tracer");
  await page.screenshot({
    path: path.join(outputDir, `${mode.name}-top.png`),
    fullPage: false,
  });
  await page.locator("#beat-00-foundation").screenshot({
    path: path.join(outputDir, `${mode.name}-foundation.png`),
  });
  await page.locator("#block-wet-pond").screenshot({
    path: path.join(outputDir, `${mode.name}-wet-pond.png`),
  });

  const tracer = page.locator(".path-tracer");
  const initialStep = await tracer.locator(".path-step-label").innerText();
  await tracer.locator(".path-next").click();
  const advancedStep = await tracer.locator(".path-step-label").innerText();
  await tracer.getByRole("button", { name: /Infiltration route/ }).click();
  const selectedRoute = await tracer.getAttribute("data-route");
  await tracer.locator(".path-next").click();
  await tracer.locator(".path-next").click();
  await tracer.locator(".path-next").click();
  const tracerComplete = await tracer.getAttribute("data-complete");
  await tracer.screenshot({
    path: path.join(outputDir, `${mode.name}-path-tracer.png`),
  });

  const terminology = page.locator("#assessment-terminology-boundary");
  await terminology.locator('input[data-correct="true"]').check();
  await terminology.getByRole("button", { name: "Check answer" }).click();
  const terminologyComplete = await terminology.getAttribute("data-complete");

  const detentionCheck = page.locator("#assessment-detention-function");
  await detentionCheck.locator('input[data-correct="true"]').check();
  await detentionCheck.getByRole("button", { name: "Check answer" }).click();
  const detentionCheckComplete = await detentionCheck.getAttribute("data-complete");

  const permanentPool = page.locator("#assessment-permanent-pool");
  const poolCards = permanentPool.locator("[data-flip-card]");
  for (let index = 0; index < await poolCards.count(); index += 1) {
    await poolCards.nth(index).click();
  }
  const permanentPoolComplete = await permanentPool.getAttribute("data-complete");

  const failureTrace = page.locator(".failure-trace");
  const failureChoices = failureTrace.locator("[data-failure-scenario]");
  for (let index = 0; index < await failureChoices.count(); index += 1) {
    await failureChoices.nth(index).click();
  }
  const failureTraceComplete = await failureTrace.getAttribute("data-complete");

  const workProduct = page.locator("#assessment-system-conversation");
  const workFields = workProduct.locator("textarea");
  for (let index = 0; index < await workFields.count(); index += 1) {
    await workFields.nth(index).fill(`Bounded conceptual response ${index + 1} with evidence and uncertainty.`);
  }
  await workProduct.getByRole("button", { name: "Check completeness" }).click();
  const workProductComplete = await workProduct.getAttribute("data-complete");

  const graphOpener = page.getByRole("button", { name: "Graph", exact: true });
  await graphOpener.click();
  const graphDrawerVisible = await page.locator("#graph-drawer").isVisible();
  const graphDrawerCards = await page.locator("#graph-drawer .drawer-connection").count();
  await page.keyboard.press("Escape");
  const graphFocusReturned = await graphOpener.evaluate(
    (node) => document.activeElement === node,
  );
  const communityOpener = page.getByRole("button", { name: "Community", exact: true });
  await communityOpener.click();
  const communityDrawerVisible = await page.locator("#community-drawer").isVisible();
  await page.keyboard.press("Escape");
  const communityFocusReturned = await communityOpener.evaluate(
    (node) => document.activeElement === node,
  );

  await tracer.locator(".path-reset").focus();
  const focusOutline = await tracer.locator(".path-reset").evaluate(
    (node) => getComputedStyle(node).outlineStyle,
  );

  const state = await page.evaluate(() => {
    const images = [...document.querySelectorAll("figure img")];
    const text = document.body.innerText;
    return {
      h1: document.querySelectorAll("h1").length,
      main: document.querySelectorAll("main").length,
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      routeChoices: document.querySelectorAll("[data-path-route]").length,
      liveRegion: Boolean(document.querySelector('.path-step-panel[aria-live="polite"]')),
      primaryNavControls: document.querySelectorAll(".quick-nav > a, .quick-nav > button").length,
      finalRecapItems: document.querySelectorAll(".final-recap-grid article").length,
      feedbackForm: Boolean(document.querySelector("#owos-concept-finish [data-concept-feedback]")),
      relatedAnchor: Boolean(document.querySelector("#owos-concept-related")),
      communityAnchor: Boolean(document.querySelector("#owos-concept-community")),
      sopAnchor: Boolean(document.querySelector("#owos-concept-sop")),
      assessmentCount: document.querySelectorAll("[data-concept-assessment]").length,
      imageCount: images.length,
      imagesReady: images.every((image) => image.complete && image.naturalWidth > 0),
      containsUndefined: /\bundefined\b/.test(text),
      containsNaN: /\bNaN\b/.test(text),
      emptyButtons: [...document.querySelectorAll("button")].some(
        (button) => !button.textContent.trim() && !button.getAttribute("aria-label"),
      ),
      reduced: matchMedia("(prefers-reduced-motion: reduce)").matches,
      scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior,
      overflowElements: [...document.querySelectorAll("body *")]
        .map((node) => ({ node, rect: node.getBoundingClientRect() }))
        .filter(({ rect }) => rect.right > innerWidth + 0.5 || rect.left < -0.5)
        .slice(0, 12)
        .map(({ node, rect }) => ({
          tag: node.tagName,
          id: node.id || "",
          className: node.className?.baseVal || node.className || "",
          left: Math.round(rect.left * 10) / 10,
          right: Math.round(rect.right * 10) / 10,
        })),
    };
  });

  await page.locator("#block-subsurface-boundary").screenshot({
    path: path.join(outputDir, `${mode.name}-subsurface.png`),
  });
  const visualBlockIds = [
    "block-dry-detention",
    "block-practice-family",
    "block-hydrograph",
    "block-water-pollutant-ledger",
    "block-wastewater-ii",
    "block-permit-value",
    "block-five-ledgers",
    "block-role-meeting",
  ];
  for (const visualBlockId of visualBlockIds) {
    const visualBlock = page.locator(`#${visualBlockId}`);
    if (await visualBlock.count()) {
      await visualBlock.screenshot({
        path: path.join(
          outputDir,
          `${mode.name}-${visualBlockId.replace("block-", "")}.png`,
        ),
      });
    }
  }
  await page.locator("#owos-concept-finish").screenshot({
    path: path.join(outputDir, `${mode.name}-finish.png`),
  });
  await page.close();

  return {
    mode: mode.name,
    errors,
    initialStep,
    advancedStep,
    selectedRoute,
    tracerComplete,
    terminologyComplete,
    detentionCheckComplete,
    permanentPoolComplete,
    failureTraceComplete,
    workProductComplete,
    graphDrawerVisible,
    graphDrawerCards,
    graphFocusReturned,
    communityDrawerVisible,
    communityFocusReturned,
    focusOutline,
    ...state,
  };
}

async function inspectNoJavaScript(browser) {
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    javaScriptEnabled: false,
  });
  const page = await context.newPage();
  await page.goto(targetUrl, { waitUntil: "load" });
  const state = await page.evaluate(() => {
    const fallback = document.querySelector(".path-tracer-fallback");
    const images = [...document.querySelectorAll("figure img")];
    return {
      fallbackVisible: Boolean(fallback && fallback.innerText.includes("Structured text equivalent")),
      fallbackRoutes: fallback?.querySelectorAll("section").length || 0,
      boundaryVisible: Boolean(document.querySelector(".path-tracer .boundary")?.innerText.trim()),
      imagesReady: images.every((image) => image.complete && image.naturalWidth > 0),
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
    };
  });
  await page.locator(".path-tracer").screenshot({
    path: path.join(outputDir, "phone-no-javascript-path-tracer.png"),
  });
  await context.close();
  return {
    mode: "phone-no-javascript",
    contained: state.scrollWidth <= state.width + 1,
    ...state,
  };
}

function failed(item) {
  return (
    item.errors.length
    || item.h1 !== 1
    || item.main !== 1
    || item.scrollWidth > item.width + 1
    || item.routeChoices !== 3
    || item.initialStep === item.advancedStep
    || item.selectedRoute !== "infiltration"
    || item.tracerComplete !== "true"
    || item.terminologyComplete !== "true"
    || item.workProductComplete !== "true"
    || item.detentionCheckComplete !== "true"
    || item.permanentPoolComplete !== "true"
    || item.failureTraceComplete !== "true"
    || !item.liveRegion
    || item.primaryNavControls !== 4
    || item.finalRecapItems !== 3
    || !item.feedbackForm
    || !item.relatedAnchor
    || !item.communityAnchor
    || !item.sopAnchor
    || item.assessmentCount < 7
    || item.imageCount < 10
    || !item.imagesReady
    || item.containsUndefined
    || item.containsNaN
    || item.emptyButtons
    || item.overflowElements.length
    || !item.graphDrawerVisible
    || item.graphDrawerCards < 3
    || !item.graphFocusReturned
    || !item.communityDrawerVisible
    || !item.communityFocusReturned
    || item.focusOutline === "none"
    || (
      item.mode === "phone-reduced-motion"
      && (!item.reduced || item.scrollBehavior !== "auto")
    )
  );
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = [];
  for (const mode of modes) results.push(await inspect(browser, mode));
  const noJavaScript = await inspectNoJavaScript(browser);
  await browser.close();

  const failures = results.filter(failed);
  if (
    !noJavaScript.fallbackVisible
    || noJavaScript.fallbackRoutes !== 3
    || !noJavaScript.boundaryVisible
    || !noJavaScript.imagesReady
    || !noJavaScript.contained
  ) {
    failures.push(noJavaScript);
  }
  const report = {
    target,
    generated_at: new Date().toISOString(),
    page_runs: results.length + 1,
    failure_count: failures.length,
    results,
    no_javascript: noJavaScript,
  };
  fs.writeFileSync(
    path.join(outputDir, "report.json"),
    `${JSON.stringify(report, null, 2)}\n`,
  );
  console.log(JSON.stringify(report, null, 2));
  if (failures.length) process.exitCode = 1;
})();
