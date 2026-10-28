const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.resolve(__dirname, '..', '..', '..', '.dev', 'assets', 'gallery', 'washes.html'), 'utf8');
const variants = ['top', 'bottom', 'corner', 'centre', 'diagonal', 'dual', 'vignette', 'band', 'dots', 'hairlines', 'crosshatch', 'microgrid', 'grain', 'paper', 'washgrain'];
const rules = variants.map(name => {
  const match = source.match(new RegExp(`\\.${name}::before\\{([^}]+)\\}`));
  if (!match) throw new Error(`Missing wash rule: ${name}`);
  return [name, match[1].replaceAll('var(--i)', 'var(--wash-strength)').replaceAll('var(--accent)', 'var(--wash-accent)').replaceAll('var(--ink-soft)', 'var(--wash-ink-soft)').replaceAll('var(--noise)', 'var(--wash-noise)').replaceAll('var(--h)', 'var(--wash-hue)').replaceAll('var(--s)', 'var(--wash-saturation)')];
});
for (const [name, rule] of rules) {
  fs.writeFileSync(path.join(__dirname, `${name}.css`), `.wash-bg.wash-bg--${name}::before { ${rule} }\n`);
  fs.writeFileSync(path.join(__dirname, `${name}.html`), `<section class="wash-bg wash-bg--${name}">\n  <h2>${name[0].toUpperCase() + name.slice(1)} background</h2>\n  <p>Your content stays above the decorative wash.</p>\n</section>\n`);
}
fs.writeFileSync(path.join(__dirname, 'washes.css'), '@import url("./wash-base.css");\n' + variants.map(name => `@import url("./${name}.css");`).join('\n') + '\n');
fs.writeFileSync(path.join(__dirname, 'index.html'), `<!doctype html>
<html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Individual background washes</title><link rel="stylesheet" href="./washes.css">
<style>
:root { --h:202; --s:72%; --surface-1:#fbfcfd; --ink:#24313b; --ink-soft:#526674; --accent:hsl(var(--h) var(--s) 42%); --line:#bdcbd5; }
:root[data-theme="dark"] { --surface-1:#182934; --ink:#edf2f6; --ink-soft:#b7c8d3; --accent:hsl(var(--h) var(--s) 72%); --line:#4e6574; color-scheme:dark; }
body { margin:0; padding:1rem; background:var(--surface-1); color:var(--ink); font:1rem/1.6 system-ui,sans-serif; }
main { max-width:85rem; margin:auto; } .wash-gallery { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,18rem),1fr)); gap:1rem; }
.wash-bg { min-height:12rem; padding:1.25rem; border:1px solid var(--line); border-radius:.75rem; }
.controls { display:flex; flex-wrap:wrap; gap:1rem; margin-block:1rem; } label { display:grid; } button { font:inherit; min-height:2.75rem; } :focus-visible { outline:3px solid var(--accent); outline-offset:3px; }
</style></head><body><main>
<h1>Individual background washes</h1><p>Static, token-driven backgrounds. Each has its own CSS file and HTML fragment. No animation, fonts or network requests.</p>
<div class="controls"><label>Intensity <output id="intensity-value">1x</output><input id="intensity" type="range" min=".3" max="2.2" step=".05" value="1"></label><label>Hue <output id="hue-value">202 deg</output><input id="hue" type="range" min="0" max="360" value="202"></label><button id="theme" type="button" aria-pressed="false">Dark theme</button></div>
<div class="wash-gallery">${variants.map(name => `<section class="wash-bg wash-bg--${name}"><h2>${name}</h2><p>Quiet decoration behind your content.</p><a href="./${name}.html">HTML fragment</a> / <a href="./${name}.css">CSS</a></section>`).join('\n')}</div></main>
<script>
document.getElementById('intensity').addEventListener('input',function(){document.documentElement.style.setProperty('--wash-intensity',this.value);document.getElementById('intensity-value').textContent=this.value+'x';});
document.getElementById('hue').addEventListener('input',function(){document.documentElement.style.setProperty('--h',this.value);document.getElementById('hue-value').textContent=this.value+' deg';});
document.getElementById('theme').addEventListener('click',function(){const dark=this.getAttribute('aria-pressed')!=='true';this.setAttribute('aria-pressed',String(dark));document.documentElement.dataset.theme=dark?'dark':'light';});
</script></body></html>\n`);
console.log(`Extracted ${variants.length} backgrounds with individual CSS/HTML and a preview gallery.`);
