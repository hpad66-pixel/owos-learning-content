const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const modules = [
  ["09", "module-09-reasoning-and-inference-with-owl", "lesson-meaning-before-models-09-reasoning-and-inference-with-owl.html"],
  ["10", "module-10-validation-with-shacl", "lesson-meaning-before-models-10-validation-with-shacl.html"],
  ["11", "module-11-references-provenance-authority-and-time", "lesson-meaning-before-models-11-references-provenance-authority-and-time.html"],
];
const root = path.resolve(__dirname, "..");
const captureRoot = path.join(__dirname, "rendered");
const target = process.env.OWOS_TARGET || "build";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

function url(slug, distName) {
  if (process.env.OWOS_BASE_URL) return `${process.env.OWOS_BASE_URL.replace(/\/$/, "")}/${distName}?batch=0911`;
  if (target === "dist") return `file://${path.join(root, "dist/site", distName)}`;
  return `file://${path.join(root, "modules", slug, "build/index.html")}`;
}

async function complete(page) {
  for (const group of await page.locator("[data-choice-group]").all()) {
    await group.locator("[data-choice][data-correct=true]").click();
    await group.locator("[data-check-choice]").click();
  }
  for (const group of await page.locator("[data-flip-group]").all())
    for (const card of await group.locator("[data-flip-card]").all()) await card.click();
  for (const group of await page.locator("[data-matching]").all()) {
    for (const field of await group.locator("[data-match-answer]").all())
      await field.selectOption(await field.getAttribute("data-match-answer"));
    await group.locator("[data-check-matching]").click();
  }
  for (const group of await page.locator("[data-multi-select]").all()) {
    for (const option of await group.locator("[data-multi-option]").all())
      if (await option.getAttribute("data-correct") === "true") await option.check();
    await group.locator("[data-check-multi]").click();
  }
  const labs = [
    ["[data-inference-court]", "[data-inference-case]", "data-inference-choice"],
    ["[data-shacl-clinic]", "[data-shacl-case]", "data-shacl-choice"],
    ["[data-evidence-reconciliation]", "[data-evidence-case]", "data-evidence-choice"],
  ];
  for (const [labSelector, caseSelector, choiceAttribute] of labs)
    for (const lab of await page.locator(labSelector).all())
      for (const item of await lab.locator(caseSelector).all()) {
        const answer = await item.getAttribute("data-answer");
        await item.locator(`[${choiceAttribute}="${answer}"]`).click();
      }
  for (const form of await page.locator("[data-work-product]").all()) {
    let i = 0;
    for (const field of await form.locator("[required]").all()) await field.fill(`Specific reviewed utility evidence ${++i}`);
    await form.locator('button[type="submit"]').click();
  }
}

async function inspect(browser, number, slug, distName, mode) {
  const phone = mode === "phone", tablet = mode === "tablet";
  const context = await browser.newContext({
    viewport: phone ? {width:390,height:844} : tablet ? {width:820,height:1080} : {width:1440,height:1000},
    reducedMotion: phone ? "reduce" : "no-preference", hasTouch: phone || tablet, isMobile: phone
  });
  const page = await context.newPage(), errors = [];
  page.on("console", m => { if (m.type() === "error") errors.push(m.text()); });
  page.on("pageerror", e => errors.push(e.message));
  await page.goto(url(slug, distName), {waitUntil:"load"});
  await page.waitForSelector("main");
  await page.evaluate(async () => Promise.all([...document.images].map(i => i.complete && i.naturalWidth ? Promise.resolve() : i.decode())));
  const graph = page.getByRole("button",{name:"Graph"}).first();
  await graph.click();
  const graphOpen = await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden") === "true";
  const focusReturned = await graph.evaluate(n => document.activeElement === n);
  await page.getByRole("button",{name:"Glossary",exact:true}).click();
  const glossaryOpen = await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  await complete(page);
  const state = await page.evaluate(() => ({
    h1:document.querySelectorAll("h1").length, sections:document.querySelectorAll(".lesson-section").length,
    visuals:document.querySelectorAll(".learning-visual").length,
    visualTypes:[...document.querySelectorAll(".learning-visual")].map(n=>n.dataset.visualType),
    images:[...document.images].every(i=>i.complete&&i.naturalWidth>0),
    completed:[...document.querySelectorAll("[data-completion-id]")].every(i=>i.classList.contains("done")),
    enabled:!document.querySelector("[data-complete-module]").disabled,
    width:document.documentElement.clientWidth, scrollWidth:document.documentElement.scrollWidth,
    emptyButtons:[...document.querySelectorAll("button")].filter(b=>!b.textContent.trim()&&!b.getAttribute("aria-label")).length,
    maxTransition:Math.max(0,...[...document.querySelectorAll("*")].map(n=>{const d=getComputedStyle(n).transitionDuration.split(",")[0];return d.endsWith("ms")?parseFloat(d):parseFloat(d)*1000}).filter(Number.isFinite))
  }));
  const dir = path.join(captureRoot,`module-${number}`,mode); fs.mkdirSync(dir,{recursive:true});
  await page.screenshot({path:path.join(dir,"full-page.png"),fullPage:true});
  await page.locator(".signature-component").screenshot({path:path.join(dir,"signature-component.png")});
  await context.close();
  return {number,mode,errors,graphOpen,graphClosed,focusReturned,glossaryOpen,...state};
}

(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:chrome}), runs=[];
  for(const m of modules) for(const mode of ["desktop","tablet","phone"]) runs.push(await inspect(browser,...m,mode));
  await browser.close();
  const failures=runs.filter(r=>r.errors.length||!r.graphOpen||!r.graphClosed||!r.focusReturned||!r.glossaryOpen||r.h1!==1||r.sections!==7||r.visuals!==4||new Set(r.visualTypes).size!==4||!r.images||!r.completed||!r.enabled||r.scrollWidth>r.width+1||r.emptyButtons||(r.mode==="phone"&&r.maxTransition>1));
  console.log(JSON.stringify({pageRuns:runs,failureCount:failures.length,failures},null,2));
  if(failures.length) process.exitCode=1;
})();
