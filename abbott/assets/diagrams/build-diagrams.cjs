const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.resolve(__dirname, '..', '..', '.dev', 'assets', 'gallery', 'flows.html'), 'utf8');
const css = fs.readFileSync(path.join(__dirname, 'diagrams.css'), 'utf8');
const names = ['Circle', 'Triangle', 'Square', 'Vertical', 'Horizontal'];
const cards = [];
for (const name of names) {
  const match = source.match(new RegExp(`<h3>${name}</h3><div class="flow">\\s*(<svg[\\s\\S]*?<\\/svg>)`));
  if (!match) throw new Error(`The source gallery is missing ${name}. No replacement was inferred.`);
  const svg = match[1].replace('<svg ', '<svg class="flow-diagram" xmlns="http://www.w3.org/2000/svg" ');
  const filename = name.toLowerCase();
  const nodeCount = (svg.match(/class="node(?: key)?"/g) || []).length;
  fs.writeFileSync(path.join(__dirname, `${filename}.svg`), svg.replace(/(<svg[^>]*>)/, `$1\n<style>${css.slice(0, css.indexOf('.flow-card'))}</style>`) + '\n');
  const controls = `<div class="flow-card__controls">
    <label>Nodes<select data-flow-nodes>${Array.from({ length: 11 }, (_, i) => `<option value="${i + 2}"${i + 2 === nodeCount ? ' selected' : ''}>${i + 2}</option>`).join('')}</select></label>
    <button type="button" data-flow-play>Play / replay</button>
    <button type="button" data-flow-pause aria-pressed="false">Pause</button>
    <label>Speed<select data-flow-rate><option value=".5">0.5x</option><option value="1" selected>1x</option><option value="2">2x</option><option value="3">3x</option></select></label>
    <label>Runner layer<select data-flow-layer><option value="over">Over nodes</option><option value="behind">Behind nodes</option></select></label>
  </div>`;
  const card = `<article class="flow-card" data-flow-card data-flow-shape="${filename}"><h2>${name}</h2>${svg}${controls}<p role="status" data-flow-status></p><p><a href="./${filename}.svg" data-flow-download download="${filename}.svg">Download current ${name} SVG</a></p></article>`;
  cards.push(card);
  fs.writeFileSync(path.join(__dirname, `${filename}.html`), `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${name} flow diagram</title><link rel="stylesheet" href="./diagrams.css"></head>
<body>${card}<script src="./diagrams.js"></script></body></html>\n`);
}
fs.writeFileSync(path.join(__dirname, 'index.html'), `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Individual flow diagrams</title><link rel="stylesheet" href="./diagrams.css">
<style>body { margin: 0; background: #edf2f6; color: #24313b; font: 1rem/1.6 system-ui, sans-serif; padding: 1rem; } main { max-width: 85rem; margin: auto; } .diagram-gallery { display: grid; grid-template-columns: repeat(auto-fit,minmax(min(100%,20rem),1fr)); gap: 1rem; }</style></head>
<body><main><h1>Individual flow diagrams</h1><p>Choose 2 to 12 nodes on each shape. Download exports your current configuration as a static SVG. Animation starts only when you press Play; reduced motion keeps every diagram still.</p><div class="diagram-gallery">${cards.join('\n')}</div></main><script src="./diagrams.js"></script></body></html>\n`);
console.log('Built 5 independent SVG files, 5 HTML components and the diagram gallery.');
