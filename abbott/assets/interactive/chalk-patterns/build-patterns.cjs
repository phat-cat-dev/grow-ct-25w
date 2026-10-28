const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.resolve(__dirname, '..', '..', '..', '.dev', 'assets', 'ab-them', 'public', 'site', 'source_index.html'), 'utf8');
const section = source.slice(source.indexOf('<section id="educational"'));
const styles = section.match(/<style id="educational-demo-edu-draw-styles">([\s\S]*?)<\/style>/)?.[1];
const articles = [...section.matchAll(/<article class="ab card primary soft edu-demo" data-edu-demo>([\s\S]*?)<\/article>/g)];
if (!styles || articles.length !== 18) throw new Error(`Expected the drawing stylesheet and 18 patterns; found ${articles.length}.`);
const additions = [
  { title: 'Double-headed arrow', paths: ['M55 80 H245', 'M67 69 L55 80 L67 91', 'M233 69 L245 80 L233 91'], arrows: [1, 2] },
  { title: 'Return arrow', paths: ['M60 45 H215 Q250 45 250 80 Q250 115 215 115 H60', 'M73 104 L60 115 L73 126'], arrows: [1] },
  { title: 'S-curve arrow', paths: ['M45 120 C170 120 130 40 255 40', 'M242 29 L255 40 L242 51'], arrows: [1] },
  { title: 'Rounded elbow arrow', paths: ['M55 125 V65 Q55 40 80 40 H245', 'M232 29 L245 40 L232 51'], arrows: [1] },
  { title: 'Fork connector', paths: ['M45 80 H125 Q145 80 160 60 L200 30 H250', 'M238 20 L250 30 L238 40', 'M125 80 Q145 80 160 100 L200 130 H250', 'M238 120 L250 130 L238 140'], arrows: [1, 3] },
  { title: 'Merge connector', paths: ['M45 30 H95 L150 80', 'M45 130 H95 L150 80', 'M150 80 H250', 'M237 69 L250 80 L237 91'], arrows: [3] },
  { title: 'Loop-back arrow', paths: ['M65 105 C20 30 100 10 175 30 C260 50 260 120 190 125 C135 130 115 95 150 70', 'M135 71 L150 70 L148 85'], arrows: [1] },
  { title: 'Decision diamond', paths: ['M150 20 L250 80 L150 140 L50 80 Z'] },
  { title: 'Oval node', paths: ['M150 30 C285 30 285 130 150 130 C15 130 15 30 150 30 Z'] },
  { title: 'Rounded node', paths: ['M80 35 H220 Q245 35 245 60 V100 Q245 125 220 125 H80 Q55 125 55 100 V60 Q55 35 80 35 Z'] },
  { title: 'Hexagon node', paths: ['M90 30 H210 L255 80 L210 130 H90 L45 80 Z'] },
  { title: 'Speech bubble', paths: ['M70 30 H230 Q250 30 250 50 V95 Q250 115 230 115 H125 L90 140 V115 H70 Q50 115 50 95 V50 Q50 30 70 30 Z'] },
  { title: 'Check mark', paths: ['M85 85 L130 125 L220 35'] },
  { title: 'Cross mark', paths: ['M105 35 L195 125', 'M195 35 L105 125'] },
  { title: 'Five-point star', paths: ['M150 20 L167 61 L212 65 L178 94 L189 137 L150 114 L111 137 L122 94 L88 65 L133 61 Z'] },
  { title: 'Paired brackets', paths: ['M110 25 H85 V135 H110', 'M190 25 H215 V135 H190'] },
  { title: 'Grouping brace', paths: ['M195 20 Q150 20 150 50 V60 Q150 80 115 80 Q150 80 150 100 V110 Q150 140 195 140'] },
  { title: 'Double underline', paths: ['M45 70 Q150 55 255 70', 'M60 90 Q150 78 240 90'] },
];
const escape = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
const baseArticle = articles.find(([, body]) => body.includes('<h4 class="card-title">Straight arrow</h4>'))?.[1];
if (!baseArticle) throw new Error('Straight arrow card is required as the shared pattern template.');
for (const { title, paths, arrows = [] } of additions) {
  const count = paths.length;
  const svg = `<svg class="edu-svg edu-chalk" viewBox="0 0 300 160" role="img" aria-label="${escape(title)}">${paths.map((d, index) =>
    `<path class="edu-stroke${arrows.includes(index) ? ' edu-arrow' : ''}" pathLength="1" d="${d}" style="--edu-animation:edu-draw-${count}-${index}"></path>`).join('')}</svg>`;
  const body = baseArticle.replace('<h4 class="card-title">Straight arrow</h4>', `<h4 class="card-title">${escape(title)}</h4>`)
    .replace(/<div class="edu-drawing"><svg[\s\S]*?<\/svg>/, `<div class="edu-drawing">${svg}`)
    .replace('aria-label="Straight arrow reusable code"', `aria-label="${escape(title)} reusable code"`);
  articles.push([null, body]);
}
function standalone(svg) {
  return svg.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ')
    .replace('class="edu-svg edu-chalk"', 'class="edu-svg edu-chalk edu-running"')
    .replace(/(<svg[^>]*>)/, `$1<style>${styles}</style>`);
}
const records = articles.map(([, body], index) => {
  const title = body.match(/<h4 class="card-title">([^<]+)<\/h4>/)?.[1];
  const svg = body.match(/<div class="edu-drawing">(<svg[\s\S]*?<\/svg>)/)?.[1];
  if (!title || !svg) throw new Error(`Incomplete drawing ${index}.`);
  const slug = index === 0 ? 'line-box' : title.toLowerCase().replaceAll(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  fs.writeFileSync(path.join(__dirname, `${slug}.svg`), `${standalone(svg)}\n`);
  if (index === 0) for (const [, line, box, variant] of body.matchAll(/<template data-line="([^"]+)" data-box="([^"]+)">(<svg[\s\S]*?<\/svg>)<\/template>/g)) {
    fs.writeFileSync(path.join(__dirname, `line-${line}-box-${box}.svg`), `${standalone(variant)}\n`);
  }
  body = body.replace('<h4 class="card-title">', '<h2 class="card-title">').replace('</h4>', '</h2>');
  body = body.replace('<div class="edu-actions"><button', '<div class="edu-actions"><label>Local speed <input type="range" data-pattern-speed min=".25" max="3" step=".25" value="1"><output>1x</output></label><button');
  body = body.replace('</textarea></details>', '</textarea><button type="button" data-pattern-download>Download current SVG</button></details>');
  return { title, slug, html: `<article class="edu-demo" data-edu-demo>${body}</article>` };
});
function page(title, selected) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title} | Chalk patterns</title><link rel="stylesheet" href="patterns.css"></head><body><main class="pattern-page"><nav aria-label="Pattern assets"><a href="index.html">All chalk patterns</a> | <a href="../../diagrams/index.html">Node diagrams</a> | <a href="../lesson-sequences/sequential.html">Sequential lesson templates</a></nav>
<h1>${title}</h1><p>Reusable draw-on patterns. Choose a combination or segment count, then draw once or repeat. Finished artwork stays visible. Downloads and copied SVGs include animation styles and your current speed, repeat and arrow settings.</p>
<div data-chalk-pattern-library><style data-pattern-animation>${styles}</style>
<div class="pattern-master"><label>Master speed <input type="range" data-edu-speed min=".25" max="3" step=".25" value="1"><output data-edu-speed-output>1x</output></label><button type="button" data-edu-all>Draw all</button><button type="button" data-edu-stop>Pause all</button><p>Playback is opt-in. Reduced motion shows finished drawings. Each cycle is one closed outline split into sequential parts.</p></div>
<div class="pattern-grid">${selected.map(record => `<div class="pattern-card-link">${record.html}<p class="asset-links"><a href="${record.slug}.html">Individual example</a> | <a href="${record.slug}.svg" download>Default SVG</a></p></div>`).join('\n')}</div></div>
</main><script src="patterns.js"></script></body></html>\n`;
}
fs.writeFileSync(path.join(__dirname, 'index.html'), page('Chalk drawing patterns', records));
for (const record of records) fs.writeFileSync(path.join(__dirname, `${record.slug}.html`), page(record.title, [record]));
console.log(`Built ${records.length} independent chalk patterns, nine line/box variants and gallery.`);
