const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir:'./tests/browser',
  timeout:60000,
  expect:{timeout:8000},
  workers:2,
  forbidOnly:Boolean(process.env.CI),
  retries:0,
  reporter:[['list'],['html',{open:'never'}]],
  use:{
    baseURL:process.env.LUX_TEST_URL || 'http://127.0.0.1:8768/Project-Lux/',
    headless:true,
    launchOptions:{executablePath:process.env.LUX_BROWSER_EXECUTABLE || undefined},
    viewport:{width:1440,height:1000},
    screenshot:'only-on-failure',
    trace:'retain-on-failure'
  },
  webServer:process.env.LUX_TEST_URL ? undefined : {
    command:'node tools/serve.cjs',
    url:'http://127.0.0.1:8768/Project-Lux/',
    reuseExistingServer:!process.env.CI,
    timeout:30000
  }
});
