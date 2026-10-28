export const LINE_PATHS = {
  straight: 'M20 80 H130',
  elbow: 'M20 40 H75 V80 H130',
  curved: 'M20 100 C65 100 70 30 130 80',
};
export const BOX_PATHS = {
  rectangle: 'M140 40 H260 V120 H140 Z',
  rounded: 'M154 35 H246 Q265 35 265 54 V106 Q265 125 246 125 H154 Q135 125 135 106 V54 Q135 35 154 35 Z',
  sketch: 'M141 42 L258 38 L263 121 L138 118 L141 42',
};
const esc = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
function arrow(x, y, angle) {
  const size = 10, spread = .5;
  const point = offset => `${(x - size * Math.cos(angle + offset)).toFixed(2)} ${(y - size * Math.sin(angle + offset)).toFixed(2)}`;
  return `M${point(-spread)} L${x.toFixed(2)} ${y.toFixed(2)} L${point(spread)}`;
}
function circlePieces(count) {
  return Array.from({ length: count }, (_, i) => {
    const start = -Math.PI / 2 + i * Math.PI * 2 / count;
    const end = start + Math.PI * 2 / count;
    const point = angle => [150 + 57 * Math.cos(angle), 80 + 57 * Math.sin(angle)];
    const [x, y] = point(end);
    const d = count === 1
      ? 'M150 23 A57 57 0 1 1 150 137 A57 57 0 1 1 150 23'
      : `M${point(start).join(' ')} A57 57 0 ${count === 1 ? 1 : 0} 1 ${x} ${y}`;
    return { d, arrow: arrow(x, y, end + Math.PI / 2) };
  });
}
function trianglePieces(count) {
  // Equilateral sides make perimeter fractions exact even when a piece crosses a corner.
  const vertices = [[150, 18], [150 + 62 * Math.sqrt(3) / 2, 111], [150 - 62 * Math.sqrt(3) / 2, 111], [150, 18]];
  const point = t => {
    const edge = Math.min(2, Math.floor(t));
    const f = t - edge;
    return vertices[edge].map((v, axis) => v + (vertices[edge + 1][axis] - v) * f);
  };
  return Array.from({ length: count }, (_, i) => {
    const start = i * 3 / count, end = (i + 1) * 3 / count;
    const points = [point(start)];
    for (let corner = Math.floor(start) + 1; corner < end; corner++) points.push(vertices[corner]);
    points.push(point(end));
    const last = points.at(-1), previous = points.at(-2);
    return { d: points.map((p, j) => `${j ? 'L' : 'M'}${p.join(' ')}`).join(' '), arrow: arrow(...last, Math.atan2(last[1] - previous[1], last[0] - previous[0])) };
  });
}
export function cyclePieces(shape, count) {
  if (!['circle', 'triangle'].includes(shape) || ![1, 2, 3, 4].includes(count)) throw new Error('Invalid educational cycle shape or part count.');
  return shape === 'circle' ? circlePieces(count) : trianglePieces(count);
}
function keyframes(count) {
  return Array.from({ length: count }, (_, i) => `@keyframes edu-draw-${count}-${i}{0%,${i * 100 / count}%{stroke-dashoffset:1}${(i + 1) * 100 / count}%,100%{stroke-dashoffset:0}}`).join('\n');
}
export const DRAW_CSS = `.edu-svg{width:100%;height:auto;display:block;color:var(--accent,#65d5ca);overflow:visible}
.edu-stroke{fill:none;stroke:currentColor;stroke-width:2.7;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:0}
.edu-stroke.edu-arrow{stroke-width:2}
.edu-running .edu-stroke{animation-name:var(--edu-animation);animation-duration:calc(var(--edu-duration,4s) / var(--edu-speed,1) / var(--edu-local-speed,1));animation-timing-function:linear;animation-fill-mode:both;animation-iteration-count:var(--edu-iterations,1)}
.edu-paused .edu-stroke{animation-play-state:paused}
.edu-no-arrows .edu-arrow{display:none}
.edu-chalk .edu-stroke{stroke-width:3.2;filter:drop-shadow(.5px .3px 0 currentColor)}
${[1, 2, 3, 4, 6, 8].map(keyframes).join('\n')}
@media(prefers-reduced-motion:reduce){.edu-running .edu-stroke{animation:none!important;stroke-dashoffset:0}}`;
function svg(parts, title, chalk = true) {
  const strokes = parts.flatMap(part => [{ d: part.d, arrow: false }, ...(part.arrow ? [{ d: part.arrow, arrow: true }] : [])]);
  return `<svg class="edu-svg${chalk ? ' edu-chalk' : ''}" viewBox="0 0 300 160" role="img" aria-label="${esc(title)}">${strokes.map((stroke, i) => `<path class="edu-stroke${stroke.arrow ? ' edu-arrow' : ''}" pathLength="1" d="${stroke.d}" style="--edu-animation:edu-draw-${strokes.length}-${i}"/>`).join('')}</svg>`;
}
export function lineBoxSvg(line, box) {
  if (!Object.hasOwn(LINE_PATHS, line) || !Object.hasOwn(BOX_PATHS, box)) throw new Error('Unknown line or box variant.');
  return svg([{ d: LINE_PATHS[line] }, { d: BOX_PATHS[box] }], `${line} line then ${box} box`);
}
function demo(title, graphic, options = '') {
  return `<article class="ab card primary soft edu-demo" data-edu-demo><div class="card-body"><h4 class="card-title">${title}</h4>${options}<div class="edu-board"><div class="edu-drawing">${graphic}</div></div><div class="edu-actions"><button type="button" class="ab btn primary btn-sm" data-edu-play>Draw / replay</button><button type="button" class="ab btn secondary outline btn-sm" data-edu-pause disabled>Pause</button><label><input type="checkbox" data-edu-loop> Repeat</label><label><input type="checkbox" data-edu-arrows checked> Arrows</label><button type="button" class="ab btn secondary link btn-sm" data-edu-copy>Copy reusable code</button></div><details><summary>Reusable SVG + styles</summary><textarea class="edu-code" rows="5" readonly aria-label="${esc(title)} reusable code"></textarea></details><p class="edu-status" role="status"></p></div></article>`;
}
export function educationalAnimations() {
  const sequences = demo('Line → box: mix your own', lineBoxSvg('straight', 'rectangle'),
    `<div class="edu-actions"><label>Line <select data-edu-line>${Object.keys(LINE_PATHS).map(name => `<option>${name}</option>`).join('')}</select></label><label>Box <select data-edu-box>${Object.keys(BOX_PATHS).map(name => `<option>${name}</option>`).join('')}</select></label></div><div class="edu-templates" hidden>${Object.keys(LINE_PATHS).flatMap(line => Object.keys(BOX_PATHS).map(box => `<template data-line="${line}" data-box="${box}">${lineBoxSvg(line, box)}</template>`)).join('')}</div>`);
  const cycles = ['circle', 'triangle'].map(shape => `<h4>${shape === 'circle' ? 'Circle' : 'Triangle'} cycles</h4><div class="edu-grid">${[1, 2, 3, 4].map(count => demo(`${shape} · ${count} ${count === 1 ? 'whole cycle' : 'parts'}`, svg(cyclePieces(shape, count), `${shape} drawn as ${count} parts with separate arrows`))).join('')}</div>`).join('');
  const nodes = {
    Rectangle: [{ d: 'M70 35 H230 V125 H70 Z' }],
    Square: [{ d: 'M100 30 H200 V130 H100 Z' }],
    Circle: [{ d: circlePieces(1)[0].d }],
    Triangle: [{ d: trianglePieces(1)[0].d }],
    'Straight line': [{ d: 'M50 80 H250' }],
    'Straight arrow': [{ d: 'M50 80 H250', arrow: arrow(250, 80, 0) }],
    'Elbow arrow': [{ d: 'M60 120 V45 H240', arrow: arrow(240, 45, 0) }],
    'Curved arrow': [{ d: 'M45 110 C110 110 130 30 245 60', arrow: arrow(245, 60, Math.atan2(30, 115)) }],
    'Exclamation mark': [{ d: 'M150 30 V100' }, { d: 'M150 123 v.1' }],
  };
  return `<div data-edu-library><div class="card-doc edu-master"><label>Master speed <input type="range" data-edu-speed min=".25" max="3" step=".25" value="1"><output data-edu-speed-output>1×</output></label><button type="button" class="ab btn primary" data-edu-all>Draw all</button><button type="button" class="ab btn secondary outline" data-edu-stop>Pause all</button><p>One master clock; local speed overrides remain available in the reusable code. Drawings wait for Play. Reduced-motion mode shows the finished artwork without animation.</p></div><style id="edu-draw-styles">${DRAW_CSS}</style><h4>Interchangeable line and box strokes</h4>${sequences}${cycles}<h4>Individual nodes, marks and arrows</h4><div class="edu-grid">${Object.entries(nodes).map(([title, parts]) => demo(title, svg(parts, title))).join('')}</div></div>`;
}
