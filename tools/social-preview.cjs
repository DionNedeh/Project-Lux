// Optional asset authoring tool. The checked-in PNG is served without a runtime.
const { chromium } = require('@playwright/test');
const fs = require('node:fs/promises');
const path = require('node:path');
(async () => {
  const root = path.resolve(__dirname, '..');
  const field = await fs.readFile(path.join(root, 'assets/field.svg'), 'utf8');
  const browser = await chromium.launch({ headless: true, executablePath: process.env.LUX_BROWSER_EXECUTABLE || undefined });
  try {
    const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
    await page.setContent(`<!doctype html><html><head><style>*{box-sizing:border-box}body{margin:0;background:#f7f2e9;color:#352e27;font-family:Georgia,serif}main{width:1200px;height:630px;padding:66px;display:grid;grid-template-columns:1.1fr 1fr;align-items:center;gap:20px;background:radial-gradient(ellipse at 80% 50%,#edc79255,transparent 50%)}small{font:15px system-ui;letter-spacing:3px;color:#9f492c}h1{font-size:67px;font-weight:400;line-height:1.08;letter-spacing:-3px;margin:27px 0}em{color:#9f492c}p{font:18px/1.6 system-ui;color:#6c6155}svg{width:100%}.brand{font:22px system-ui;letter-spacing:6px;margin-bottom:42px}.brand span{font-size:12px;letter-spacing:0;margin-left:12px}</style></head><body><main><div><div class="brand">LUX <span>by Voelori</span></div><small>AI × FUSION × EVIDENCE</small><h1>Intelligence for<br>a <em>brighter</em><br>energy future.</h1><p>A research library for the possibilities ahead.</p></div><div>${field}</div></main></body></html>`);
    await page.screenshot({ path: path.join(root, 'assets/social-card.png') });
  } finally { await browser.close(); }
})();
