const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");

(async () => {
  const root = path.resolve(__dirname, "..");
  const source = path.join(root, "figures");
  const output = path.join(root, "generated", "figure-png");
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1200, height: 680 }, deviceScaleFactor: 2 });
  for (const file of fs.readdirSync(source).filter((name) => name.endsWith(".svg")).sort()) {
    await page.goto(pathToFileURL(path.join(source, file)).href);
    await page.screenshot({
      path: path.join(output, file.replace(/\.svg$/, ".png")),
      fullPage: false,
    });
  }
  await browser.close();
  process.stdout.write(`Rendered SVG figures to ${output}\n`);
})();
