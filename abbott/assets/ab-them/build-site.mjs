import { readFile, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import less from 'less';
import { lessonExperiment, horizontalPanels } from './src/lesson-experiments.mjs';
import { educationalAnimations } from './src/educational-animations.mjs';

const root = dirname(fileURLToPath(import.meta.url));
const publicDir = join(root, 'public');
const fluidDir = join(publicDir, 'site', 'fragments', '04_spacing');
const fluidSource = (await Promise.all(['abbott-core-default.less', 'abbott-core-fluid.less', 'abbott-core-legacy.less']
  .map(file => readFile(join(fluidDir, file), 'utf8')))).join('\n');
const fluid = await less.render(fluidSource, { math: 'parens-division' });
await writeFile(join(publicDir, 'site', 'fluid-core.js'),
  `// Generated from fragments/04_spacing/*.less by build-site.mjs.\nexport const FLUID_CORE_CSS = ${JSON.stringify(fluid.css)};\n`);
const sources = [
  ['00_index.md', 'index', 'Index'],
  ['01_color.md', 'color', 'Color tuning'],
  ['02_typography.md', 'typography', 'Typography'],
  ['03_icons.md', 'icons', 'Icons'],
  ['04_spacing.md', 'spacing', 'Spacing'],
  ['05_motion.md', 'motion', 'Motion'],
  ['06_obects.md', 'objects', 'objects'],
  ['07_layout.md', 'layout', 'Layout'],
  ['08_structure.md', 'structure', 'Adapt structure'],
  ['fragments\\10_adapt experiments.md', 'lessons', 'Lesson experiments'],
  ['fragments\\12_educational_animations.md', 'educational', 'Educational animations'],
];
const reference = await readFile(join(publicDir, 'cheatsheet copy.html'), 'utf8');
const tunerControls = await readFile(join(publicDir, 'site', 'fragments', 'tuner-controls.html'), 'utf8');
const accordion = await readFile(join(publicDir, 'site', 'fragments', 'accordions.html'), 'utf8');
const cards = await readFile(join(publicDir, 'site', 'fragments', 'cards.html'), 'utf8');
const escape = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const slug = text => text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const usedIds = new Map();
function uniqueId(id) {
  const count = (usedIds.get(id) || 0) + 1;
  usedIds.set(id, count);
  return count === 1 ? id : `${id}-${count}`;
}
sources.forEach(([, id]) => uniqueId(id));

function contentSections(markdown, areaId) {
  const lines = markdown.replace(/\r\n/g, '\n').split('\n');
  let html = '';
  const levels = [];
  for (const line of lines) {
    const heading = line.match(/^\s{0,3}(#{1,3}) (.+?)\s*$/);
    if (heading) {
      const depth = heading[1].length;
      if (depth === 1) continue;
      while (levels.length && levels.at(-1) >= depth) {
        html += '</section>\n';
        levels.pop();
      }
      const id = uniqueId(`${areaId}-${slug(heading[2])}`);
      html += `<section id="${id}" class="outline-section" aria-labelledby="${id}-title">\n<h${depth + 1} id="${id}-title" class="outline-title">${escape(heading[2])}</h${depth + 1}>\n`;
      levels.push(depth);
    } else {
      html += line + '\n';
    }
  }
  while (levels.length) { html += '</section>\n'; levels.pop(); }
  return html.replace(/(<h[34]\b[^>]*class="outline-title"[^>]*>[^<]*<\/h[34]>)(\s*<\/section>)/g,
    '$1\n<p class="placeholder">Content to be defined.</p>$2');
}

const areas = [];
const descriptions = {
  index: 'Your design-system workspace',
  color: 'Palettes, harmony and semantic meaning',
  typography: 'Heading systems, reading and web fonts',
  icons: 'Your SVG library and Google Material Symbols',
  spacing: 'Rhythm and layout foundations',
  motion: 'Playful icons and expressive typography',
  objects: 'Cards, buttons, callouts and accordions',
  layout: 'Page structure and composition',
  structure: 'Adapt page hierarchy and theme integration',
  lessons: 'Six compositions with progressive, collapsible learning stages',
  educational: 'Composable chalk strokes, cycles and nodes on one master clock',
};
const fontPanel = `<div class="connector-panel" data-connector>
<div class="connector-heading"><span class="eyebrow">Google Fonts</span><span class="connector-badge">Live connector</span></div>
<p>Pair a heading face with a readable body font. Preview across the page; your choices travel with your scheme.</p>
<div class="connector-controls">
<label>Heading font <select id="font-heading"></select></label>
<label>Body font <select id="font-body"></select></label>
<button type="button" id="fonts-apply">Apply font pairing</button>
</div>
<div class="font-specimen"><span class="eyebrow">The reading room · Aa Bb 0123</span><h4>Good typography gives ideas room to breathe.</h4><p>A thoughtful balance of character, clarity and rhythm. Compare the shapes, the spacing and the way each line carries you into the next.</p></div>
<p id="fonts-status" class="connector-status" role="status"></p>
<a href="https://fonts.google.com/" target="_blank" rel="noreferrer">Explore Google Fonts ↗</a>
</div>`;
const symbolPanel = `<div class="connector-panel" data-connector>
<div class="connector-heading"><span class="eyebrow">Google Material Symbols</span><span class="connector-badge">Live connector</span></div>
<p>A companion to your existing SVG packs, not a replacement. Choose a style, tune the strokes and copy a symbol's markup.</p>
<div class="connector-controls">
<label>Style <select id="symbol-style"><option>Outlined</option><option>Rounded</option><option>Sharp</option></select></label>
<label>Weight <select id="symbol-weight">${[100,200,300,400,500,600,700].map(w=>`<option${w===400?' selected':''}>${w}</option>`).join('')}</select></label>
<label>Size <input id="symbol-size" type="range" min="20" max="48" value="32"><output id="symbol-size-value">32 px</output></label>
<label class="check-label"><input id="symbol-fill" type="checkbox"> Filled</label>
</div>
<label>Find a symbol <input id="symbol-search" type="search" placeholder="Search the preview set"></label>
<div id="symbol-gallery" class="symbol-gallery"></div>
<p id="symbols-status" class="connector-status" role="status"></p>
<label for="symbol-markup">Selected symbol markup</label><pre id="symbol-markup">&lt;span class="material-symbol" aria-hidden="true"&gt;home&lt;/span&gt;</pre>
<div class="connector-controls"><button type="button" id="symbol-copy">Copy markup</button><a href="https://fonts.google.com/icons" target="_blank" rel="noreferrer">Browse all Google symbols ↗</a></div>
</div>`;
for (const [file, id, title] of sources) {
  let markdown = await readFile(join(publicDir, 'site', file), 'utf8');
  if (id === 'lessons') markdown = markdown.replace(/LESSON_EXPERIMENT_(\w+)/g, (_, name) => lessonExperiment(name));
  if (id === 'lessons') markdown = markdown.replace('HORIZONTAL_PANELS', horizontalPanels().replace(/aria-(controls|labelledby)="(sideways-[^"]+)"/g, 'aria-$1="lessons-demo-$2"'));
  if (id === 'educational') markdown = markdown.replace('EDUCATIONAL_ANIMATIONS', educationalAnimations());
  if (id === 'color') {
    markdown = markdown.replace(/^(## 1\.0 HSL Tuner)\s*$/m, `$1\n<div class="card-doc"><div class="token-controls">${tunerControls}</div></div>\n`);
    markdown = markdown.replace(/(## 5\.0 Color theme)[\s\S]*$/, '$1\n<p>Your selected colour layers form the portable theme. Set a main system, include the other layers you want, then use CSS / scheme tools to copy, export or build it.</p>\n');
  }
  if (id === 'objects') {
    markdown = markdown.replace(/## 1\.0 Cards[\s\S]*?(?=## 2\.0 Buttons)/, `## 1.0 Cards\n${cards}\n`);
    markdown = markdown.replace(/^(## 4\.0 Accordions)\s*$/m, `$1\n${accordion}\n`);
  }
  if (id === 'typography') markdown = markdown.replace('CHOICE of OOGLE FONTS', fontPanel);
  if (id === 'icons') {
    if ((markdown.match(/id="iconPacks"/g) || []).length > 1) {
      markdown = markdown.replace(/^<div id="iconPacks">[^\r\n]*\r?\n/, '');
    }
    markdown = symbolPanel + `
<div class="connector-panel" data-connector>
<p class="eyebrow">SVG icon frames</p>
<div class="connector-controls">
<label>Icon size <input type="range" id="svg-icon-size" min="20" max="48" value="32"><output id="svg-icon-size-value">32 px</output></label>
<label class="check-label"><input type="checkbox" id="svg-icon-circle" role="switch"> Circular frames (off: square)</label>
</div>
<p class="note">Click an icon to copy its SVG markup. Frame size and border thickness follow icon size; names remain available on hover and to screen readers.</p>
</div>\n` + markdown;
  }
  // The Markdown headings are the outline; pasted demo headings are captions.
  markdown = markdown
    .replace(/blue-grey/gi, 'Color-grey')
    .replace(/<\/?section\b[^>]*>/g, '')
    .replace(/<button\b[^>]*class="sendcss"[^>]*>[\s\S]*?<\/button>/g, '')
    .replace(/<h2\b[^>]*class="sec"[^>]*>([\s\S]*?)<\/h2>/g,
      (_, caption) => `<p class="demo-caption">${caption.replace(/^\d+\s*·\s*/, '')}</p>`)
    .replace(/\sdata-css-index="\d+"/g, '')
    .replace(/\sfor="([^"]+)"/g, (_, old) => ` for="${id}-demo-${old}"`)
    .replace(/\sid="([^"]+)"/g, (_, old) => ` id="${uniqueId(`${id}-demo-${old}`)}"`);
  let content = markdown.trim()
    ? contentSections(markdown, id)
    : '<p class="placeholder">Content to be defined.</p>';
  if (id === 'color') {
    content = content.replace(/(<button type="button" id="color-demo-seed-apply">Apply<\/button>)/, '$1\n<button type="button" id="color-seed-set-base" title="Use the current hue and saturation at 50% lightness; keep grey saturation and reset stage 2">Set as new base</button>');
    const chooseSystem = `<div class="color-selection" data-color-live>
<p class="eyebrow">Assemble your colour theme</p>
<p>Choose the main system for your site's colours, then add any other systems you want to take with you. Click any HSL, brand or semantic shade to make its exact colour the main accent. Harmony applies the whole palette by role. Only one main system is active.</p>
<label>Main system <select id="color-main"><option value="hsl">1 · Generated HSL</option><option value="brand" selected>2 · Refined brand</option><option value="harmony">3 · Harmony</option><option value="semantics">4 · Semantics</option></select></label>
<div class="connector-controls">${['hsl', 'brand', 'harmony', 'semantics'].map((name, i) => `<label class="check-label"><input type="checkbox" data-color-include="${name}" checked> Include ${i + 1} · ${name}</label>`).join('')}</div>
<label>Harmony main colour <select id="color-main-hue">${[1, 2, 3, 4].map(n => `<option value="${n}">Hue ${n}</option>`).join('')}</select></label>
<label>Semantic main colour <select id="color-main-role">${['info', 'positive', 'neutral', 'negative', 'comment'].map(role => `<option>${role}</option>`).join('')}</select></label>
<p id="color-selection-status" role="status"></p>
</div>`;
    const brandTweaks = `<p>Keep stage 1's hue; experiment with saturation and tonal character. Each click starts fresh from stage 1, not the last remix. The result feeds harmony and semantics.</p>`;
    const bounds = `<div class="semantic-bounds" data-color-live><p>Hue locked to meaning: red 0°, green 145°, amber 42°, purple 270°, blue 210°. Saturation and brightness follow the main colour; sliders adjust them relative to that source. If Semantics is main, section 2's remix is the source. Hue identity is not a contrast/accessibility guarantee.</p><p id="color-semantic-values"></p><p id="color-semantic-mode"></p></div>`;
    content = chooseSystem + content;
    content = content.replace(/(<input type="range" id="color-demo-sem(?:S|WS|L|WL)" )min="\d+" max="\d+" step="1"/g, '$1min="0" max="100" step="0.1"');
    content = content.replace(/(<h3 id="color-2-0-brand-tuner-title"[^>]*>[^<]*<\/h3>)/, '$1\n' + brandTweaks);
    content = content.replace(/(<div class="swrow" id="color-demo-scaleRow">)/, '<div class="connector-controls remix-toolbar" data-color-live><button type="button" id="color-brand-remix">Remix colours</button><p id="color-brand-remix-status" role="status"></p></div>\n$1');
    content = content.replace(/(<h3 id="color-4-0-semantic-tuning-title"[^>]*>[^<]*<\/h3>)/, '$1\n' + bounds);
    content = content.replace(/(<h3 id="color-5-0-color-theme-title"[^>]*>[^<]*<\/h3>)/, '$1\n<p>The selected layers below are included in Copy CSS, CSS/JSON exports and saved builds. Baseline component defaults remain in the full design-system build.</p><pre id="color-theme-preview"></pre>');
    ['hsl', 'brand', 'harmony', 'semantics'].forEach((system, i) => {
      const headings = ['hsl-tuner', 'brand-tuner', 'color-theory', 'semantic-tuning'];
      const pattern = new RegExp('(<h3 id="color-' + (i + 1) + '-0-' + headings[i] + '-title"[^>]*>[^<]*</h3>)');
      content = content.replace(pattern, `$1\n<div class="stage-theme-actions" data-color-live><label><input type="checkbox" data-color-include="${system}" checked> Add this system to theme</label><button type="button" data-color-main="${system}">Use as main system</button><button type="button" data-theme-export data-color-live>Export theme CSS</button><button type="button" data-theme-tools data-color-live>Save complete theme</button></div>`);
    });
  }
  areas.push(`<section id="${id}" class="site-area" aria-labelledby="${id}-title">
<h2 id="${id}-title" class="area-title"><button type="button" class="area-trigger" aria-expanded="true" aria-controls="${id}-content"><span class="area-number" aria-hidden="true">${String(areas.length + 1).padStart(2, '0')}</span><span class="area-label">${escape(title)}<span class="area-description">${descriptions[id]}</span></span><span class="area-chevron" aria-hidden="true"></span></button></h2>
<div id="${id}-content" class="area-content">
${content}
</div>
</section>`);
}
const sprite = reference.match(/<svg\b[\s\S]*?<\/svg>/)?.[0];
if (!sprite) throw new Error('Reference icon sprite not found');
// Symbol IDs are used by SVG references, so retain them rather than prefixing.
const restoredAreas = areas.join('\n').replace(/id="icons-demo-(ic-[^"]+)"/g, 'id="$1"');
const connectorSource = await readFile(join(publicDir, 'site', 'connectors.js'), 'utf8');
const colorSource = await readFile(join(publicDir, 'site', 'color-system.js'), 'utf8');
const typographySource = await readFile(join(publicDir, 'site', 'typography-system.js'), 'utf8');
const spacingSource = await readFile(join(publicDir, 'site', 'spacing-system.js'), 'utf8');
const layoutSource = await readFile(join(publicDir, 'site', 'layout-system.js'), 'utf8');
const cardsSource = await readFile(join(publicDir, 'site', 'card-system.js'), 'utf8');
const themeTemplate = await readFile(join(root, 'theme.css'), 'utf8');
const html = `<!doctype html>
<html lang="en" data-harmony="complementary">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AB Theme Studio — Site</title>
  <link rel="stylesheet" href="../tuner.css">
  <link rel="stylesheet" href="../reference.css">
  <link rel="stylesheet" href="site.css">
  <script>window.ABConnectors = (function () {
${connectorSource.replace(/^export /gm, '')}
return { FONT_FAMILIES, DEFAULT_CONNECTORS, connectorAssets, connectorImports };
})();</script>
  <script>window.ABColor = (function () {
${colorSource.replace(/^export /gm, '')}
return { COLOR_SYSTEMS, COLOR_HARMONIES, COLOR_STOPS, SEMANTIC_BANDS, SEMANTIC_PRESETS, SEMANTIC_APPEARANCES, defaultColorSystem, randomizeColorSystem, validateColorSystem, semanticHue, mainColor, colorSystemCss, harmonyPalette, paletteLightness, remixBrand, semanticSettings };
})();</script>
  <script src="color-ui.js" defer></script>
  <script>window.ABTypography = (function () {
${typographySource.replace(/^export /gm, '')}
return { DEFAULT_TYPOGRAPHY, TYPOGRAPHY_RATIOS, HEADING_HARMONIES, headingSizes, validateTypography, typographyCss };
})();</script>
  <script src="typography-ui.js" defer></script>
  <script>window.ABSpacing = (function () {
const FLUID_CORE_CSS = ${JSON.stringify(fluid.css)};
${spacingSource.replace(/^import .+;\r?\n/gm, '').replace(/^export /gm, '')}
return { DEFAULT_SPACING, SPACING_PROFILES, validateSpacing, spacingCss };
})();</script>
  <script src="spacing-ui.js" defer></script>
  <script>window.ABLayout = (function () {
${layoutSource.replace(/^export /gm, '')}
return { DEFAULT_LAYOUT, validateLayout, layoutCss };
})();</script>
  <script src="layout-ui.js" defer></script>
  <script>window.ABCards = (function () {
${cardsSource.replace(/^export /gm, '')}
return { DEFAULT_CARDS, validateCards, cardsCss };
})();</script>
  <script src="card-ui.js" defer></script>
  <script src="lesson-ui.js" defer></script>
  <script src="educational-ui.js" defer></script>
  <script>window.ABThemeTemplate = ${JSON.stringify(themeTemplate).replaceAll('<', '\\u003c')};</script>
  <script src="site.js" defer></script>
</head>
<body>
${sprite}
<main class="wrap">
  <header class="hero"><span class="eyebrow">AB / Design system workbench</span><h1>One system.<br>A world of possibilities.</h1><p>Shape a coherent visual language. Explore colour, pair type, collect symbols and build a scheme that is yours.</p><div class="hero-meta"><span>Single-hue foundations</span><span>Live font &amp; symbol connectors</span><span>Portable CSS</span></div></header>
  <div class="rail">
    <div class="theme-toggle" role="group" aria-label="Preview theme">
      <button type="button" data-theme-set="light" aria-pressed="false">Light</button>
      <button type="button" data-theme-set="dark" aria-pressed="false">Dark</button>
      <button type="button" data-theme-set="system" aria-pressed="true">System</button>
    </div>
    <div class="active-source" role="group" aria-label="Active source colour">
      <button type="button" id="colour-random" aria-label="Randomise colour theme" title="Randomise colour theme"><span class="material-symbol" aria-hidden="true">shuffle</span></button>
      <span id="active-source-chip" class="active-source-chip"><span id="active-source-rgb" class="active-source-rgb" aria-hidden="true"></span><input id="active-source-hsl" type="text" aria-label="Active colour: paste hex, RGB, HSL or a CSS colour; Enter to apply" aria-describedby="active-source-status" autocomplete="off" spellcheck="false"><span id="active-source-hsltext" class="active-source-hsltext" aria-hidden="true"></span></span>
      <button type="button" id="base-colour-lock" aria-pressed="false" aria-label="Lock current colour as base theme"><span class="material-symbol" aria-hidden="true">lock_open</span></button>
    </div>
    <button type="button" id="scheme-open" aria-expanded="false" aria-controls="scheme-tools">CSS / scheme tools</button>
  </div>
  <p id="active-source-status" role="status"></p>
  <nav class="page-nav" aria-label="Site areas">${sources.map(([, id, title]) => `<a href="#${id}">${escape(title)}</a>`).join('')}</nav>
  <aside id="scheme-tools" class="card-doc" aria-label="CSS and scheme tools" hidden>
    <p>Inject CSS into this page, export it, or save and build a scheme. These tools are independent of the preview controls below.</p>
    <div class="scheme-actions">
      <label>Scheme name <input id="scheme-name" value="my-scheme" pattern="[a-zA-Z0-9_\\-]+" autocomplete="off"></label>
      <label>Saved schemes <select id="scheme-list"><option value="">Choose a scheme</option></select></label>
      <button type="button" id="scheme-load">Load</button>
      <button type="button" id="scheme-save">Save scheme</button>
      <button type="button" id="scheme-build">Save &amp; build scheme</button>
    </div>
    <label for="scheme-css">Scheme CSS</label>
    <textarea id="scheme-css" rows="10" spellcheck="false">/* Optional custom CSS. Selected colour systems, fonts and symbols are exported automatically.
   Rules here are applied last and can intentionally override generated tokens. */</textarea>
    <p class="note">Colour, typography and spacing preview live. Copy/export includes the full design system, active main theme, included colour layers, fluid typography and spacing, Google imports, connector styles and editor CSS. Saved themes retain all settings and the Light/Dark/System choice. Local saves stay in this browser; export/import theme JSON for a portable backup.</p>
    <div class="scheme-actions">
      <button type="button" id="scheme-inject">Inject CSS</button>
      <button type="button" id="scheme-reset">Remove injection</button>
      <button type="button" id="scheme-copy">Copy CSS</button>
      <button type="button" id="scheme-export">Export CSS</button>
      <button type="button" id="scheme-json">Export scheme JSON</button>
      <label>Import theme JSON <input type="file" id="scheme-import" accept=".json,application/json"></label>
    </div>
    <p id="scheme-status" role="status" aria-live="polite"></p>
    <div id="scheme-downloads"></div>
  </aside>
  <p class="structure-notice"><strong>Your workspace, your order.</strong> Colour generation, brand remix, harmony, semantics, fluid typography, Google Fonts and Material Symbols are live.</p>
  <div id="site-content">
${restoredAreas}
  </div>
</main>
</body>
</html>
`;
await writeFile(join(publicDir, 'site', 'index.html'), html);
console.log(`Built public/site/index.html from ${sources.length} ordered Markdown sources.`);
