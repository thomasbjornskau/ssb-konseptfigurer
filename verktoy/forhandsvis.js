// Lager PNG-forhåndsvisning av alle SVG-er i utdata/<serie>/ med Open Sans.
// Bruk: node verktoy/forhandsvis.js [serie]   (uten serie: alle)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const ROT = path.resolve(__dirname, '..');
const FONT = path.join(ROT, 'node_modules/@fontsource/open-sans/files/');
const css = [400, 600, 700].map(w => `@font-face{font-family:'Open Sans';font-weight:${w};src:url(file://${FONT}open-sans-latin-${w}-normal.woff)}`).join('');
(async () => {
  const opts = process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {};
  const b = await chromium.launch(opts);
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const utdata = path.join(ROT, 'utdata');
  const serier = process.argv[2] ? [process.argv[2]] : fs.readdirSync(utdata).filter(d => fs.statSync(path.join(utdata, d)).isDirectory());
  for (const s of serier) {
    const dir = path.join(utdata, s);
    const png = path.join(ROT, 'forhandsvisning', s);
    fs.mkdirSync(png, { recursive: true });
    for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.svg'))) {
      const svg = fs.readFileSync(path.join(dir, f), 'utf8');
      const tmp = path.join(png, '_tmp.html');
      fs.writeFileSync(tmp, `<html><head><style>${css}body{margin:0}</style></head><body>${svg}</body></html>`);
      await p.goto('file://' + tmp);
      await p.waitForTimeout(200);
      await p.screenshot({ path: path.join(png, f.replace('.svg', '.png')) });
      fs.unlinkSync(tmp);
    }
    console.log('forhåndsvist', s);
  }
  await b.close();
})();
