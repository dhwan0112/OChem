// SVG를 라이트/다크 모드로 렌더링해 PNG로 저장한다 (그림 검수용).
// 사용법: NODE_PATH=$(npm root -g) node tools/preview.js in.svg out.png [배율=3] [dark|light]
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [input, output, scale, scheme = 'dark'] = process.argv.slice(2);
  const svg = fs.readFileSync(input, 'utf8');
  const browser = await chromium.launch();
  const page = await browser.newPage({ colorScheme: scheme, deviceScaleFactor: Number(scale) || 3 });
  const bg = scheme === 'dark' ? '#16171b' : '#ffffff';
  const src = 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');
  await page.setContent(`<body style="margin:0;padding:12px;background:${bg};display:inline-block"><img src="${src}"></body>`);
  await page.waitForTimeout(200);
  await (await page.$('body')).screenshot({ path: output });
  await browser.close();
})();
