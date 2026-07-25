const { chromium } = require("playwright");
const fs = require("node:fs"), path = require("node:path");
const modules = [
  ["12","module-12-running-knowledge-spine","lesson-meaning-before-models-12-running-knowledge-spine.html"],
  ["13","module-13-map-meaning-to-data","lesson-meaning-before-models-13-map-meaning-to-data.html"],
  ["14","module-14-virtualize-cache-index-or-materialize","lesson-meaning-before-models-14-virtualize-cache-index-or-materialize.html"],
];
const root=path.resolve(__dirname,".."), captureRoot=path.join(__dirname,"rendered");
const target=process.env.OWOS_TARGET||"build", chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
function url(slug,file){if(process.env.OWOS_BASE_URL)return`${process.env.OWOS_BASE_URL.replace(/\/$/,"")}/${file}?batch=1214`;if(target==="dist")return`file://${path.join(root,"dist/site",file)}`;return`file://${path.join(root,"modules",slug,"build/index.html")}`}
async function complete(page){
 for(const g of await page.locator("[data-choice-group]").all()){await g.locator("[data-choice][data-correct=true]").click();await g.locator("[data-check-choice]").click()}
 for(const g of await page.locator("[data-flip-group]").all())for(const c of await g.locator("[data-flip-card]").all())await c.click();
 for(const g of await page.locator("[data-matching]").all()){for(const f of await g.locator("[data-match-answer]").all())await f.selectOption(await f.getAttribute("data-match-answer"));await g.locator("[data-check-matching]").click()}
 for(const g of await page.locator("[data-multi-select]").all()){for(const o of await g.locator("[data-multi-option]").all())if(await o.getAttribute("data-correct")==="true")await o.check();await g.locator("[data-check-multi]").click()}
 const labs=[
  ["[data-knowledge-spine-router]","[data-spine-case]","data-spine-choice"],
  ["[data-accountability-handoff]","[data-handoff-case]","data-handoff-choice"],
  ["[data-mapping-workbench]","[data-mapping-case]","data-mapping-choice"],
  ["[data-mapping-break-repair]","[data-map-repair-case]","data-map-repair-choice"],
  ["[data-access-pattern-stress-test]","[data-access-case]","data-access-choice"],
  ["[data-stale-copy-diagnosis]","[data-stale-case]","data-stale-choice"],
 ];
 for(const [ls,cs,ca] of labs)for(const lab of await page.locator(ls).all())for(const card of await lab.locator(cs).all()){const answer=await card.getAttribute("data-answer");await card.locator(`[${ca}="${answer}"]`).click()}
 for(const form of await page.locator("[data-work-product]").all()){let n=0;for(const f of await form.locator("[required]").all())await f.fill(`Reviewed operating evidence ${++n}`);await form.locator('button[type="submit"]').click()}
}
async function inspect(browser,number,slug,file,mode){
 const phone=mode==="phone",tablet=mode==="tablet";
 const context=await browser.newContext({viewport:phone?{width:390,height:844}:tablet?{width:820,height:1080}:{width:1440,height:1000},reducedMotion:phone?"reduce":"no-preference",hasTouch:phone||tablet,isMobile:phone});
 const page=await context.newPage(),errors=[];page.on("console",m=>{if(m.type()==="error")errors.push(m.text())});page.on("pageerror",e=>errors.push(e.message));
 await page.goto(url(slug,file),{waitUntil:"load"});await page.waitForSelector("main");await page.evaluate(async()=>Promise.all([...document.images].map(x=>x.complete&&x.naturalWidth?Promise.resolve():x.decode())));
 const graph=page.getByRole("button",{name:"Graph"}).first();await graph.click();const graphOpen=await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden")==="false";await page.keyboard.press("Escape");const graphClosed=await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden")==="true";const focusReturned=await graph.evaluate(n=>document.activeElement===n);
 await page.getByRole("button",{name:"Glossary",exact:true}).click();const glossaryOpen=await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden")==="false";await page.keyboard.press("Escape");await complete(page);
 const state=await page.evaluate(()=>({h1:document.querySelectorAll("h1").length,sections:document.querySelectorAll(".lesson-section").length,visuals:document.querySelectorAll(".learning-visual").length,visualTypes:[...document.querySelectorAll(".learning-visual")].map(n=>n.dataset.visualType),interactions:document.querySelectorAll(".signature-component").length,images:[...document.images].every(i=>i.complete&&i.naturalWidth>0),completed:[...document.querySelectorAll("[data-completion-id]")].every(i=>i.classList.contains("done")),enabled:!document.querySelector("[data-complete-module]").disabled,width:document.documentElement.clientWidth,scrollWidth:document.documentElement.scrollWidth,emptyButtons:[...document.querySelectorAll("button")].filter(b=>!b.textContent.trim()&&!b.getAttribute("aria-label")).length,maxTransition:Math.max(0,...[...document.querySelectorAll("*")].map(n=>{const d=getComputedStyle(n).transitionDuration.split(",")[0];return d.endsWith("ms")?parseFloat(d):parseFloat(d)*1000}).filter(Number.isFinite))}));
 const dir=path.join(captureRoot,`module-${number}`,mode);fs.mkdirSync(dir,{recursive:true});await page.screenshot({path:path.join(dir,"full-page.png"),fullPage:true});for(const [n,lab] of (await page.locator(".signature-component").all()).entries())await lab.screenshot({path:path.join(dir,`signature-component-${n+1}.png`)});
 await context.close();return{number,mode,errors,graphOpen,graphClosed,focusReturned,glossaryOpen,...state}
}
(async()=>{const browser=await chromium.launch({headless:true,executablePath:chrome}),runs=[];for(const m of modules)for(const mode of["desktop","tablet","phone"])runs.push(await inspect(browser,...m,mode));await browser.close();const failures=runs.filter(r=>r.errors.length||!r.graphOpen||!r.graphClosed||!r.focusReturned||!r.glossaryOpen||r.h1!==1||r.sections!==7||r.visuals!==4||new Set(r.visualTypes).size!==4||r.interactions!==2||!r.images||!r.completed||!r.enabled||r.scrollWidth>r.width+1||r.emptyButtons||(r.mode==="phone"&&r.maxTransition>1));console.log(JSON.stringify({pageRuns:runs,failureCount:failures.length,failures},null,2));if(failures.length)process.exitCode=1})();
