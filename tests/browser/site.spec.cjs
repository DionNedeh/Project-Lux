const { test, expect } = require('@playwright/test');
const fs = require('node:fs');
const path = require('node:path');
const axePath = require.resolve('axe-core/axe.min.js');
const root=path.resolve(__dirname,'../..');
const manifest=JSON.parse(fs.readFileSync(path.join(root,'tools/library-manifest.json'),'utf8'));
const samples=['','library/index.html','library/L01.html','library/40-ai-for-fusion-transferable-control.html','library/01-fusion-physics-fundamentals.html','library/yang-2026-st-e1-tritium-tmap8-surrogate-models.html','library/moc-start-here.html','method.html'];

test('All rendered research notes are reachable under the Pages base path', async ({ request }) => {
  test.setTimeout(120000);
  const slugs=Object.keys(manifest).map(file=>path.basename(file,'.md'));
  for(let i=0;i<slugs.length;i+=12){
    await Promise.all(slugs.slice(i,i+12).map(async slug=>{
      const response=await request.get(`library/${slug}.html`);
      expect(response.status(),slug).toBe(200);
      expect(await response.text(),slug).toContain('id="doc-title"');
    }));
  }
});

test('Homepage roles, featured search and filters work',async({page})=>{
  const errors=[];page.on('pageerror',error=>errors.push(error.message));
  await page.goto('');
  for(const stage of ['predict','control','learn']){
    await page.locator(`[data-stage=${stage}]`).click();
    await expect(page.locator(`#stage-${stage}`)).toBeVisible();
    await expect(page.locator('.stage-panel:visible')).toHaveCount(1);
    await expect(page.locator(`[data-stage=${stage}]`)).toHaveAttribute('aria-pressed','true');
  }
  await page.locator('[data-filter=engineering]').click();
  await expect(page.locator('.library-section .library-row:visible')).toHaveCount(3);
  await page.locator('[data-filter=all]').click();
  await page.locator('#library-search').fill('TCV');
  await expect(page.locator('.library-section .library-row:visible')).toHaveCount(1);
  await page.locator('#library-search').fill('zzznomatch');
  await expect(page.locator('.empty-state')).toBeVisible();
  await page.locator('#reset-search').click();
  await expect(page.locator('.library-section .library-row:visible')).toHaveCount(8);
  expect(errors).toEqual([]);
});

test('Catalogue filters, full-text search, URL persistence and reset',async({page})=>{
  await page.goto('library/index.html');
  await expect(page.locator('.catalogue-row')).toHaveCount(282);
  await page.locator('[data-kind=source]').click();
  await expect(page.locator('.catalogue-row:visible')).toHaveCount(48);
  await page.locator('#catalogue-search').fill('"400 ms"');
  await expect(page.locator('.catalogue-row:visible')).toHaveCount(1);
  await expect(page.locator('.catalogue-row:visible')).toHaveAttribute('href','hl3-data-driven-rl-control-2025.html');
  await page.reload();
  await expect(page.locator('#catalogue-search')).toHaveValue('"400 ms"');
  await expect(page.locator('.catalogue-row:visible')).toHaveCount(1);
  await page.locator('#catalogue-search').fill('zzznomatch');
  await expect(page.locator('.catalogue-empty')).toBeVisible();
  await page.locator('.catalogue-empty .clear-filters').click();
  await expect(page.locator('.catalogue-row:visible')).toHaveCount(282);
  await page.locator('#topic-filter').selectOption('computation');
  const visible=page.locator('.catalogue-row:visible');
  expect(await visible.count()).toBeGreaterThan(5);
  expect(await visible.evaluateAll(rows=>rows.every(row=>row.dataset.topics.split(' ').includes('computation')))).toBe(true);
  await page.locator('#sort-order').selectOption('updated');
  const dates=await visible.evaluateAll(rows=>rows.map(row=>row.dataset.updated));
  expect(dates).toEqual([...dates].sort().reverse());
});

test('Citations open full notes and return to the right panel',async({page})=>{
  await page.goto('library/L01.html');
  await page.getByRole('link',{name:'Read the full research note'}).click();
  await expect(page).toHaveURL(/tcv-predict-first-rampdown-2025\.html/);
  await page.getByRole('link',{name:'AI roles: Control',exact:true}).click();
  await expect(page.locator('#stage-control')).toBeVisible();
  await expect(page.locator('#stage-learn')).toBeHidden();
});

test('Original source downloads retain their complete text',async({request})=>{
  for(const file of ['sources/yang-2026-st-e1-tritium-tmap8-surrogate-models.md','synthesis/40-ai-for-fusion-transferable-control.md']){
    const response=await request.get(`research/${file}`);
    expect(response.ok()).toBe(true);
    expect((await response.text()).replace(/\r\n/g,'\n')).toBe(fs.readFileSync(path.join(root,'research',file),'utf8').replace(/\r\n/g,'\n'));
  }
});

for(const width of [1440,768,390,320]){
  test(`Representative pages fit at ${width}px`,async({page})=>{
    await page.setViewportSize({width,height:900});
    for(const sample of samples){
      await page.goto(sample);
      expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),sample).toBe(true);
    }
  });
}

for(const sample of samples){
  test(`Accessibility scan: ${sample||'homepage'}`,async({page})=>{
    await page.goto(sample);
    const axeURL=new URL('__axe-test.js',page.url()).href;
    await page.route(axeURL,route=>route.fulfill({contentType:'text/javascript',body:fs.readFileSync(axePath,'utf8')}));
    await page.addScriptTag({url:axeURL});
    const results=await page.evaluate(async()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}}));
    expect(results.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>n.target)}))).toEqual([]);
  });
}

test('Keyboard entry, reduced motion, and custom 404',async({page})=>{
  await page.emulateMedia({reducedMotion:'reduce'});
  await page.goto('');
  await page.keyboard.press('Tab');
  await expect(page.locator('.skip')).toBeFocused();
  expect(await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior)).toBe('auto');
  await page.keyboard.press('Enter');
  await page.locator('[data-stage=predict]').focus();
  await page.keyboard.press('Enter');
  await expect(page.locator('#stage-predict')).toBeVisible();
  const response=await page.goto('missing/page/');
  expect(response.status()).toBe(404);
  await page.getByRole('link',{name:'Search the research library'}).click();
  await expect(page).toHaveURL(/library\/index.html/);
});

test('Field grid visibly flows inside a stationary diagram, pauses, and stops off-screen',async({page})=>{
  await page.emulateMedia({reducedMotion:'no-preference'});
  await page.goto('');
  const scene=page.locator('.plasma-scene');
  await scene.scrollIntoViewIfNeeded();
  await expect(scene).toHaveClass(/motion-running/);
  const initialBounds=await scene.boundingBox();
  const before=await scene.screenshot();
  await page.waitForTimeout(800);
  expect((await scene.screenshot()).equals(before)).toBe(false);
  expect(await scene.boundingBox()).toEqual(initialBounds);
  await expect(page.locator('.plasma-art')).toHaveCSS('transform','none');
  await page.getByRole('button',{name:'Pause motion',exact:true}).click();
  await expect(scene).not.toHaveClass(/motion-running/);
  const stopped=await scene.screenshot();
  await page.waitForTimeout(300);
  expect((await scene.screenshot()).equals(stopped)).toBe(true);
  await page.getByRole('button',{name:'Play motion',exact:true}).click();
  await expect(scene).toHaveClass(/motion-running/);
  await page.locator('.site-footer').scrollIntoViewIfNeeded();
  await expect(scene).not.toHaveClass(/motion-running/);
});

test('Conceptual field respects reduced motion and live preference changes',async({page})=>{
  await page.emulateMedia({reducedMotion:'reduce'});
  await page.goto('');
  await expect(page.locator('.field-grid-canvas')).toBeHidden();
  await expect(page.locator('.field-body')).toBeVisible();
  await expect(page.getByRole('button',{name:'Reduced motion enabled'})).toBeDisabled();
  await expect(page.locator('.plasma-scene')).not.toHaveClass(/motion-running/);
  await page.emulateMedia({reducedMotion:'no-preference'});
  await expect(page.locator('.plasma-scene')).toHaveClass(/motion-running/);
  await expect(page.locator('.field-grid-canvas')).toBeVisible();
  await expect(page.getByRole('button',{name:'Pause motion',exact:true})).toBeEnabled();
  await page.emulateMedia({reducedMotion:'reduce'});
  await expect(page.locator('.field-grid-canvas')).toBeHidden();
  await expect(page.locator('.field-body')).toBeVisible();
});

test('No-script reading remains complete',async({browser,baseURL})=>{
  const context=await browser.newContext({javaScriptEnabled:false,baseURL});
  const page=await context.newPage();
  await page.goto('');
  await expect(page.locator('.stage-panel:visible')).toHaveCount(3);
  await expect(page.locator('.library-section .library-row')).toHaveCount(8);
  await page.goto('library/index.html');
  await expect(page.locator('.catalogue-row:visible')).toHaveCount(282);
  await page.goto('library/yang-2026-st-e1-tritium-tmap8-surrogate-models.html');
  await expect(page.getByRole('heading',{name:'Internal inconsistencies preserved'})).toBeVisible();
  await context.close();
});

test('No client request to third-party services on normal reading',async({page})=>{
  const external=[];
  page.on('request',request=>{if(new URL(request.url()).origin!==new URL(page.url()==='about:blank'?'http://127.0.0.1:8768':page.url()).origin&&!request.isNavigationRequest())external.push(request.url());});
  await page.goto('');await page.goto('library/index.html');await page.locator('#catalogue-search').fill('fusion');
  expect(external).toEqual([]);
});
