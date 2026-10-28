const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.resolve(__dirname, '..', '..', '..', '.dev', 'assets', 'gallery', 'process.html'), 'utf8');
const names = ['flowchart', 'fork-join', 'loop-counter', 'pipeline', 'show-working'];
const cards = [];
const starts = [...source.matchAll(/<div class="pat"(?: style="[^"]*")?>/g)];
if (starts.length !== names.length) throw new Error('Expected the five named process examples.');
for (let i = 0; i < starts.length; i++) {
  const start = starts[i].index;
  const tags = /<\/?div\b[^>]*>/g;
  tags.lastIndex = start;
  let depth = 0, end;
  for (let tag; (tag = tags.exec(source));) {
    depth += tag[0].startsWith('</') ? -1 : 1;
    if (!depth) { end = tags.lastIndex; break; }
  }
  if (!end) throw new Error(`Unclosed example: ${names[i]}`);
  let fragment = source.slice(start, end)
    .replace(/^<div[^>]*>/, `<article class="process-asset" data-process-asset="${names[i]}">`)
    .replace(/<\/div>$/, '</article>')
    .replaceAll('id="loopn"', 'data-process-count')
    .replace(/<path class="edge"/g, '<path pathLength="1" class="edge"')
    .replace('(independent of Replay)', '(press Play to begin)');
  fragment = fragment.replace('</article>', `<div class="process-asset__controls">
  <button type="button" data-process-play>Play / replay</button>
  <button type="button" data-process-pause aria-pressed="false">Pause</button>
  <label>Speed<select data-process-rate><option value=".5">0.5x</option><option value="1" selected>1x</option><option value="2">2x</option><option value="3">3x</option></select></label>
</div><p role="status" data-process-status>Still preview. Press Play to animate.</p></article>`);
  const name = names[i];
  cards.push(fragment);
  fs.writeFileSync(path.join(__dirname, `${name}.html`), `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${name} process asset</title><link rel="stylesheet" href="./process.css"></head><body>${fragment}<script src="./process.js"></script></body></html>\n`);
}
fs.writeFileSync(path.join(__dirname, 'index.html'), `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Process assets</title><link rel="stylesheet" href="./process.css"><style>body{margin:0;padding:1rem;background:#edf2f6;color:#24313b;font:1rem/1.6 system-ui,sans-serif}main{max-width:85rem;margin:auto}.process-gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,24rem),1fr));gap:1rem}</style></head><body><main><h1>Individual process assets</h1><p>Five independent examples: play, pause and change speed on each. No autoplay. Reduced motion keeps all content readable without movement.</p><div class="process-gallery">${cards.join('\n')}</div></main><script src="./process.js"></script></body></html>\n`);
console.log('Built 5 independent process assets and their gallery.');
