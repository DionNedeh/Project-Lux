const { chromium } = require('@playwright/test');
const path = require('node:path');
const fs = require('node:fs/promises');
(async()=>{
  const base=process.env.LUX_CAPTURE_URL||'http://127.0.0.1:8768/Project-Lux/';
  const out=path.resolve(__dirname,'../../output/site-release-preview');
  await fs.mkdir(out,{recursive:true});
  const browser=await chromium.launch({headless:true,executablePath:process.env.LUX_BROWSER_EXECUTABLE||undefined});
  try{
    const page=await browser.newPage({viewport:{width:1440,height:1050},reducedMotion:'reduce'});
    await page.goto(base);await page.screenshot({path:path.join(out,'home-desktop.png')});await page.screenshot({path:path.join(out,'home-full.png'),fullPage:true});
    await page.goto(new URL('library/index.html',base).href);await page.screenshot({path:path.join(out,'library-desktop.png')});
    await page.locator('#catalogue-search').fill('"400 ms"');await page.locator('#browse-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'library-search.png')});
    await page.goto(new URL('library/yang-2026-st-e1-tritium-tmap8-surrogate-models.html',base).href);await page.screenshot({path:path.join(out,'source-desktop.png')});
    await page.locator('#internal-inconsistencies-preserved').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'source-limitations.png')});
    await page.setViewportSize({width:390,height:844});await page.goto(base);await page.screenshot({path:path.join(out,'home-mobile.png')});
    await page.goto(new URL('library/index.html',base).href);await page.screenshot({path:path.join(out,'library-mobile.png')});
    await page.goto(new URL('library/01-fusion-physics-fundamentals.html',base).href);await page.locator('.table-wrap').first().scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'table-mobile.png')});
    console.log(`Saved local review screenshots in ${out}`);
  }finally{await browser.close();}
})();
