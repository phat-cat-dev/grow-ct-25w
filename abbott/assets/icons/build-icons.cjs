const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.resolve(__dirname, '..', '..', '.dev', 'assets', 'ab-them', 'public', 'site', 'source_index.html'), 'utf8');
const start = source.indexOf('<div id="icons-demo-iconPacks">');
const end = source.indexOf('</section>', start);
if (start < 0 || end < 0) throw new Error('SVG icon pack gallery was not found.');
const symbols = new Map([...source.matchAll(/<symbol id="([^"]+)" viewBox="([^"]+)">([\s\S]*?)<\/symbol>/g)]
  .map(([, id, viewBox, body]) => [id, { viewBox, body }]));
const escape = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
const titles = { 'Academic practice areas': 'academic-practice', Resources: 'resources', Library: 'library' };
const packs = [...source.slice(start, end).matchAll(/<div class="card-doc"><div class="packhead"><span class="t">([^<]+)<\/span><span class="c">\d+<\/span><\/div><div class="icongrid">([\s\S]*?)<\/div><\/div>(?=<div class="card-doc">|<\/div>)/g)]
  .map(([, title, content]) => ({ title, slug: titles[title], ids: [...content.matchAll(/<use href="#([^"]+)"/g)].map(match => match[1]) }));
if (packs.length !== 3 || packs.some(pack => !pack.slug || !pack.ids.length)) throw new Error('Expected the three existing icon collections.');
const icons = new Map();
for (const pack of packs) {
  for (const id of pack.ids) {
    const symbol = symbols.get(id);
    if (!symbol) throw new Error(`Missing sprite icon: ${id}`);
    const name = id.replace(/^ic-/, '').replaceAll('-', ' ');
    const markup = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${symbol.viewBox}" fill="currentColor" role="img" aria-label="${escape(name)}">${symbol.body}</svg>`;
    icons.set(id, { markup, name });
    fs.writeFileSync(path.join(__dirname, `${id}.svg`), `${markup}\n`);
  }
  const sprite = `<svg xmlns="http://www.w3.org/2000/svg">${pack.ids.map(id => {
    const symbol = symbols.get(id);
    return `<symbol id="${id}" viewBox="${symbol.viewBox}" fill="currentColor">${symbol.body}</symbol>`;
  }).join('')}</svg>`;
  fs.writeFileSync(path.join(__dirname, `${pack.slug}.sprite.svg`), `${sprite}\n`);
}
function card(pack) {
  return `<section class="icon-pack" data-icon-pack="${pack.slug}" aria-labelledby="pack-${pack.slug}">
<header class="packhead"><h2 id="pack-${pack.slug}">${escape(pack.title)}</h2><span class="pack-count" aria-label="${pack.ids.length} icons" data-pack-count>${pack.ids.length}</span><a href="${pack.slug}.sprite.svg" download>Download sprite</a></header>
<div class="icongrid">${pack.ids.map(id => {
    const { markup, name } = icons.get(id);
    return `<button type="button" class="iconcell" data-icon="${id}" aria-label="Copy ${escape(name)} icon SVG" aria-pressed="false" title="Select and copy ${escape(name)}"><span class="icon-frame">${markup.replace('role="img"', 'aria-hidden="true"')}</span></button>`;
  }).join('\n')}</div><p class="pack-empty" hidden>No matching icons in this collection.</p></section>`;
}
function page(title, selected) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${escape(title)} | Icon collections</title><link rel="stylesheet" href="icon-gallery.css"></head><body>
<main class="icon-library"><nav aria-label="Icon collections"><a href="index.html">All collections</a>${packs.map(pack => ` | <a href="${pack.slug}.html">${escape(pack.title)}</a>`).join('')}</nav>
<header class="library-heading"><p class="eyebrow">Reusable SVG collections</p><h1>${escape(title)}</h1><p>Named packs, icon-only buttons and self-contained SVG markup. Select an icon to copy it; Enter and Space work too. These are the existing SVG icons, not a search of Google's full catalogue.</p></header>
<label class="icon-search">Find an icon <input type="search" data-icon-search placeholder="Search names or sprite IDs"></label>
<p role="status" data-search-status>${selected.reduce((sum, pack) => sum + pack.ids.length, 0)} icons</p>
<div data-icon-packs>${selected.map(card).join('\n')}</div>
<section class="icon-controls" aria-labelledby="icon-controls-title"><h2 id="icon-controls-title">Preview controls</h2>
<div class="control-row"><label>Icon size <input type="range" data-icon-size min="20" max="64" value="32"><output data-icon-size-value>32 px</output></label>
<label>Border thickness <input type="range" data-icon-border min="0" max="8" step="1" value="0"><output data-icon-border-value>0 px</output></label>
<label>Border style <select data-icon-border-style><option value="solid">Solid</option><option value="dashed">Dashed</option><option value="dotted">Dotted</option><option value="double">Double</option><option value="none">None</option></select></label>
<label><input type="checkbox" data-icon-circle> Rounded buttons</label></div>
<div class="control-row">
<label>Entrance <select data-icon-effect><option value="none">None</option><option value="fade">Fade in</option><option value="rise">Fade + rise</option><option value="pop">Gentle pop</option></select></label>
<label>Duration <input type="range" data-icon-duration min="100" max="2000" step="50" value="500"><output data-icon-duration-value>500 ms</output></label>
<label>Stagger <input type="range" data-icon-stagger min="0" max="300" step="10" value="50"><output data-icon-stagger-value>50 ms</output></label>
<button type="button" data-icon-replay>Replay entrance</button></div>
<p>Plain buttons by default: increase border thickness to add an optional outline. These controls affect the preview only. Copied SVGs inherit <code>currentColor</code>; downloads remain the original artwork. Reduced motion skips entrance effects.</p>
</section>
<section class="icon-selection" aria-labelledby="icon-selection-title"><h2 id="icon-selection-title">Selected icon</h2>
<p data-selected-name>Select an icon above.</p><div class="selected-preview" data-selected-preview></div>
<label>Self-contained SVG markup<textarea data-icon-markup rows="5" readonly spellcheck="false" aria-label="Selected self-contained SVG markup"></textarea></label>
<div class="control-row"><button type="button" data-icon-copy disabled>Copy SVG markup</button><a data-icon-download hidden download>Download SVG</a></div>
<p data-copy-status role="status">SVG copies contain their own paths: no sprite or font dependency.</p></section>
<p class="library-note">For variable Google font symbols, use the existing <a href="../../.dev/assets/ab-them/public/site/source_index.html#icons">studio connector</a>. Its search covers a 24-symbol preview set; these three local SVG collections work offline.</p>
</main><script src="icon-gallery.js"></script></body></html>\n`;
}
fs.writeFileSync(path.join(__dirname, 'index.html'), page('Icon collections', packs));
for (const pack of packs) fs.writeFileSync(path.join(__dirname, `${pack.slug}.html`), page(pack.title, [pack]));
console.log(`Built ${packs.length} collection pages, ${icons.size} standalone SVGs, sprites and combined gallery.`);
