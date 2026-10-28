const fs = require('node:fs');
const path = require('node:path');
const site = path.resolve(__dirname, '..', '..', '.dev', 'assets', 'ab-them', 'public', 'site');
const css = fs.readFileSync(path.join(site, 'site.css'), 'utf8');
const source = fs.readFileSync(path.join(site, 'source_index.html'), 'utf8');
const section = source.slice(source.indexOf('<section id="motion"'), source.indexOf('<section id="objects"'));
const escape = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
const decode = text => text.replaceAll('&amp;', '&');
const paths = {
  spin: '<circle r="19"/><circle r="7"/><path d="M0-29v7m0 44v7m-29-29h7m44 0h7m-49-20 5 5m30 30 5 5m-40 0 5-5m30-30 5-5"/>',
  pulse: '<path d="M0 23C-43-3-22-34 0-15 22-34 43-3 0 23Z"/>',
  jiggle: '<path d="M-20 15h40l-5-8V-9a15 15 0 0 0-30 0V7Zm14 7a6 6 0 0 0 12 0M0-30v5"/>',
  bounce: '<path d="M0 27v-53m-18 18L0-26 18-8"/>',
  shake: '<path d="m0-26 29 50h-58ZM0-9V7"/><circle cy="15" r="1" fill="currentColor"/>',
  launch: '<path d="M-8 9C-4-12 10-24 28-27 26-8 13 7-7 11Zm-1-3-13-1 9-12 15-1M-2 12l1 14 13-10V1M-13 15l-10 10"/><circle cx="14" cy="-12" r="4"/>',
  swing: '<circle cy="-22" r="5"/><path d="M0-17v43M-10-7h20M-26 5c0 28 52 28 52 0m-26 21-7-7M0 26l7-7M-26 5l-4 9m56-9 4 9"/>',
  flip: '<circle r="28"/><path d="m13-16-6 23-20 9 6-23Zm0 0L-7-7M7 7l-20 9"/>',
  float: '<path d="M-19 16C-41 14-33-12-17-10-13-32 17-30 23-10 44-9 37 17 22 16Z"/>',
  pop: '<path d="m0-29 9 7 11 1 2 12 7 9-7 9-2 12-11 1-9 7-9-7-11-1-2-12-7-9 7-9 2-12 11-1Z"/><path d="m-12 0 8 8L14-10"/>',
  tick: '<circle r="27"/><path d="M0-19V0l13 8M0-27v3m27 24h-3M0 27v-3m-27-24h3"/>',
  squash: '<circle r="26"/><path d="M-26 0h52M0-26v52M-18-19C4-8 4 8-18 19M18-19C-4-8-4 8 18 19"/>',
  wave: '<path d="M-18 7-23-6q-3-9 4-9l9 15-5-28q0-8 6-5l7 27-1-32q3-7 7 0l3 30 4-27q4-6 7 1L14-3l7-16q6-4 7 3L22 9c-4 26-30 30-40-2Z"/>',
};
const records = [...section.matchAll(/<button[^>]*data-motion-toggle[^>]*>([\s\S]*?)<\/button>/g)].map(match => {
  const content = match[1];
  const kind = content.match(/class="[^"]*motion-art motion-([a-z]+)"/)?.[1];
  const title = content.match(/class="motion-title">([^<]+)/)?.[1];
  const description = content.match(/class="motion-description">([^<]+)/)?.[1];
  if (!kind || !title || !description) throw new Error('Incomplete motion sample.');
  return { kind, title: decode(title), description: decode(description) };
});
if (records.length !== 22) throw new Error(`Expected 22 motions, found ${records.length}.`);
const timing = {
  spin: [3, 'linear'], pulse: [2], jiggle: [2], bounce: [2, 'ease-in-out', 'hop'],
  shake: [2.4], launch: [2.8], swing: [3], flip: [3.2], float: [4], pop: [2.4],
  tick: [6, 'steps(12,end)', 'spin'], squash: [1.8], wave: [2.6],
  breathe: [3], shimmer: [3], tilt: [2.8], typewriter: [4, 'steps(7,end)'],
  ripple: [2.8, 'ease-in-out', 'letter'], reveal: [3.6], shadow: [3], elastic: [3], shear: [3],
};
const words = { breathe: 'Breathe', shimmer: 'Spectrum', tilt: 'Hello!', typewriter: 'Create.', ripple: 'Ripple', reveal: 'Discover', shadow: 'Echo', elastic: 'Stretch', shear: 'Forward' };
function keyframe(name) {
  const match = css.match(new RegExp(`@keyframes motion-${name} \\{[^\\n]+`));
  if (!match) throw new Error(`Missing motion keyframe: ${name}`);
  return match[0];
}
function svg(record) {
  const { kind, title, description } = record;
  const id = `svg-motion-${kind}`;
  const [duration, easing = 'ease-in-out', animation = kind] = timing[kind];
  const text = word => `<text x="160" y="76" text-anchor="middle" font-size="38" font-family="system-ui,sans-serif" font-weight="700">${word}</text>`;
  let artwork;
  let extra = '';
  let frames = keyframe(animation === 'shimmer' || animation === 'shadow' ? 'breathe' : animation);
  if (paths[kind]) {
    artwork = `<g class="art"><g transform="translate(160 65)" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">${paths[kind]}</g></g>`;
  } else if (kind === 'ripple') {
    artwork = `<g fill="currentColor">${[...words[kind]].map((letter, index) => `<g class="art" style="animation-delay:${index * .12}s"><text x="${104 + index * 22}" y="76" font-size="38" font-family="monospace" font-weight="700">${letter}</text></g>`).join('')}</g>`;
  } else if (kind === 'shimmer') {
    artwork = `<defs><clipPath id="${id}-clip">${text(words[kind])}</clipPath><linearGradient id="${id}-gradient"><stop stop-color="var(--motion-accent,#287baa)"/><stop offset=".5" stop-color="var(--motion-ink,#202c36)"/><stop offset="1" stop-color="var(--motion-accent,#287baa)"/></linearGradient></defs><g clip-path="url(#${id}-clip)"><rect class="art" x="0" y="20" width="640" height="90" fill="url(#${id}-gradient)"/></g>`;
    frames = '@keyframes motion-shimmer {50% {transform:translateX(-320px)}}';
  } else if (kind === 'shadow') {
    artwork = `<g class="echo echo-a" fill="var(--motion-line,#b4c5d0)">${text(words[kind])}</g><g class="echo echo-b" fill="var(--motion-muted,#6a8290)">${text(words[kind])}</g><g fill="currentColor">${text(words[kind])}</g>`;
    extra = `.echo{animation:echo calc(3s / var(--motion-speed,1)) ease-in-out infinite}.echo-b{animation-direction:reverse}@keyframes echo{30%{transform:translate(5px,3px)}70%{transform:translate(-5px,-3px)}}`;
  } else artwork = `<g class="art" fill="currentColor">${text(words[kind])}</g>`;
  const origin = kind === 'swing' ? '160px 37px' : kind === 'wave' ? '163px 90px' : '160px 65px';
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 130" role="img" aria-labelledby="${id}-title ${id}-desc" style="color:var(--motion-accent,#287baa)">
<title id="${id}-title">${escape(title)}</title><desc id="${id}-desc">${escape(description)} Animation respects reduced motion.</desc>
<style>
.art{transform-box:view-box;transform-origin:${origin};animation:motion-${animation} calc(${duration}s / var(--motion-speed,1)) ${easing} infinite}
${frames}
${extra}
svg[data-paused] *{animation-play-state:paused!important}
@media(prefers-reduced-motion:reduce){.art,.echo{animation:none!important;transform:none!important;opacity:1!important;clip-path:none!important}}
</style>${artwork}</svg>`;
}
const transitions = [
  ['fade', 'Fade', 'opacity:.25', 'opacity:1'],
  ['slide', 'Slide', 'transform:translateX(0)', 'transform:translateX(65px)'],
  ['scale', 'Scale', 'transform:scale(.65)', 'transform:scale(1.15)'],
  ['rotate', 'Quarter turn', 'transform:rotate(0)', 'transform:rotate(90deg)'],
  ['colour', 'Colour blend', 'fill:var(--motion-accent,#287baa)', 'fill:var(--motion-ink,#202c36)'],
  ['round', 'Square to circle', 'rx:4px', 'rx:28px'],
];
const assets = records.map(record => ({ ...record, markup: svg(record) }));
for (const [kind, title, from, to] of transitions) {
  assets.push({
    kind: `transition-${kind}`, title, description: 'A forward transition, hold, and return. Standalone SVG repeats this demonstration.',
    markup: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 130" role="img" aria-labelledby="svg-transition-${kind}-title">
<title id="svg-transition-${kind}-title">${title} transition</title>
<style>.art{fill:var(--motion-accent,#287baa);transform-box:view-box;transform-origin:160px 65px;animation:change calc(2.4s / var(--motion-speed,1)) ease-in-out infinite}
@keyframes change{0%,15%,100%{${from}}45%,65%{${to}}}
svg[data-paused] *{animation-play-state:paused!important}
@media(prefers-reduced-motion:reduce){.art{animation:none!important}}
</style><rect class="art" x="132" y="37" width="56" height="56" rx="4"/></svg>`,
  });
}
for (const asset of assets) {
  const scope = `svg[data-motion-asset="${asset.kind}"]`;
  asset.markup = asset.markup.replace('<svg ', `<svg data-motion-asset="${asset.kind}" `)
    .replace(/<style>([\s\S]*?)<\/style>/, (_, styles) => `<style>${styles
      .replace(/\.(art|echo-b|echo)(?![\w-])/g, `${scope} .$1`)
      .replace(/\bchange\b/g, `transition-${asset.kind}`)}</style>`);
  fs.writeFileSync(path.join(__dirname, `${asset.kind}.svg`), `${asset.markup}\n`);
}
const cards = assets.map(asset => `<article class="motion-card"><h2>${escape(asset.title)}</h2><p>${escape(asset.description)}</p>
<div class="stage">${asset.markup.replace('<svg ', '<svg data-paused="" ')}</div>
<div class="controls"><button type="button" data-play aria-pressed="false">Play</button><button type="button" data-replay>Replay</button>
<label>Speed <input data-speed type="range" min=".25" max="3" step=".25" value="1"><output>1x</output></label>
<label>Size <input data-size type="range" min=".5" max="1.5" step=".1" value="1"><output>1x</output></label>
<label>Angle <input data-angle type="range" min="-45" max="45" step="5" value="0"><output>0 degrees</output></label>
<a href="${asset.kind}.svg" download>Download SVG</a></div><p data-status role="status">Paused</p></article>`).join('\n');
fs.writeFileSync(path.join(__dirname, 'index.html'), `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SVG motion assets</title><link rel="stylesheet" href="motion-gallery.css"></head><body><main><h1>SVG motion assets</h1><p>22 icon and typography motions, plus six transition studies. Individual SVGs contain their own animation CSS and need no fonts or scripts. Preview controls do not alter the downloaded originals.</p><p>Icons are original vector interpretations, not Google Material Symbols glyph exports. Text uses your system font. Standalone SVGs animate automatically; previews start paused and reduced motion always wins.</p><div class="grid">${cards}</div></main><script src="motion-gallery.js"></script></body></html>\n`);
console.log(`Built ${assets.length} self-contained animated SVG assets.`);
