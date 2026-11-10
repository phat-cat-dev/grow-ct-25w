/**
 * growMarks.js — the DOM engine.
 *
 * Draws a mark onto a target element and plays its animation. Framework-
 * agnostic: an Adapt component view or extension imports this and calls
 * playMark(); a plain page (the demo) does the same. No external dependencies.
 *
 * The CSS (grow-marks.css, or its LESS port inside an Adapt plugin) must be
 * loaded by the host. This module injects only the shared ink filter.
 *
 * API:
 *   ensureMarkDefs(doc?)            inject the #gm-ink filter once
 *   drawMark(target, opts)         insert a mark; plays unless opts.autoplay===false
 *   playMark(target, opts)         insert a mark and play it
 *   playWithin(root?, opts)        draw every [data-gm-mark] under root
 * Each draw returns a handle: { host, svg, play(), replay(), remove() }.
 *
 * opts: { mark, color, speed, hold, autoplay, variant }
 *   mark    — a catalogue id (string) or a definition object (e.g. makeBadge('3'))
 *   color   — accent | positive | negative | neutral | comment | soft
 *   speed   — multiplier, clamped to 0.4–2.5 (default 1)
 *   hold    — keep the mark after it draws (default true); false removes it
 *   variant — highlight only: a style/colour variant class suffix
 */

import { getMark, makeBadge } from './marksCatalogue.js';
import { buildSvg, colorClass, clampSpeed, placeClass, markFromDataset } from './marksLogic.js';

const FILTER_MARKUP =
  '<svg width="0" height="0" aria-hidden="true" focusable="false">' +
  '<filter id="gm-ink" x="-25%" y="-25%" width="150%" height="150%">' +
  '<feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="4" result="n"/>' +
  '<feDisplacementMap in="SourceGraphic" in2="n" scale="1.7"/>' +
  '</filter></svg>';

/** Inject the shared ink turbulence filter once per document. */
export function ensureMarkDefs(doc = typeof document !== 'undefined' ? document : null) {
  if (!doc || doc.getElementById('gm-defs')) return;
  const holder = doc.createElement('div');
  holder.id = 'gm-defs';
  holder.setAttribute('aria-hidden', 'true');
  holder.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden';
  holder.innerHTML = FILTER_MARKUP;
  (doc.body || doc.documentElement).appendChild(holder);
}

function reducedMotion() {
  return typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
}

function resolveMark(mark) {
  if (mark && typeof mark === 'object') return mark;
  return getMark(mark);
}

const HIGHLIGHT_COLOR_CLASS = {
  positive: 'gm-hl-green',
  negative: 'gm-hl-red',
  neutral: 'gm-hl-amber',
  comment: 'gm-hl-violet',
  'fluro-pink': 'gm-hl-pink',
  'fluro-yellow': 'gm-hl-yellow',
  'fluro-green': 'gm-hl-fgreen',
  'fluro-blue': 'gm-hl-blue',
  'fluro-purple': 'gm-hl-purple'
};

function makeHandle({ host, svg, speed, hold, cleanup, autoplay }) {
  let timer = null;
  function play() {
    host.style.setProperty('--gm-flow-rate', String(speed));
    host.classList.remove('gm-playing');
    void host.offsetWidth; // reflow so the animation restarts
    host.classList.add('gm-playing');
    if (!hold) {
      const after = reducedMotion() ? 0 : 900 / speed;
      clearTimeout(timer);
      timer = setTimeout(remove, after + 60);
    }
  }
  function remove() {
    clearTimeout(timer);
    cleanup();
  }
  const handle = { host, svg, play, replay: play, remove };
  if (autoplay) play();
  return handle;
}

function drawHighlight(el, { color, variant, speed, hold, autoplay, jitter, jitterAmount }) {
  const added = ['gm-hl'];
  const cc = HIGHLIGHT_COLOR_CLASS[color];
  if (cc) added.push(cc);
  if (variant) added.push(`gm-hl-${variant}`);
  added.forEach(c => el.classList.add(c));

  // Random vertical wobble so highlights don't all sit at the same band — a
  // hand-drawn highlighter rides a little higher or lower on each word. On by
  // default; pass jitter:false (or data-gm-jitter="off") to pin it uniform.
  let wobbled = false;
  if (jitter !== false) {
    const amt = Number.isFinite(jitterAmount) ? Math.abs(jitterAmount) : 6; // ± % of the line box
    const shift = (Math.random() * 2 - 1) * amt;
    el.style.setProperty('--gm-hl-shift', `${shift.toFixed(1)}%`);
    wobbled = true;
  }

  return makeHandle({
    host: el,
    svg: null,
    speed,
    hold,
    autoplay,
    cleanup: () => { added.forEach(c => el.classList.remove(c)); if (wobbled) el.style.removeProperty('--gm-hl-shift'); }
  });
}

/**
 * Draw a mark onto a target (an element or a selector).
 * @returns {{host:HTMLElement, svg:?SVGElement, play:Function, replay:Function, remove:Function}}
 */
export function drawMark(target, options = {}) {
  ensureMarkDefs();
  const el = typeof target === 'string' ? document.querySelector(target) : target;
  if (!el) throw new Error('grow-marks: target element not found.');

  const def = resolveMark(options.mark);
  if (!def) throw new Error(`grow-marks: unknown mark "${options.mark}".`);

  const color = options.color || def.color || 'accent';
  const speed = clampSpeed(options.speed == null ? 1 : options.speed);
  const hold = options.hold !== false;
  const autoplay = options.autoplay !== false;

  if (def.kind === 'highlight') {
    return drawHighlight(el, { color, variant: options.variant, speed, hold, autoplay, jitter: options.jitter, jitterAmount: options.jitterAmount });
  }

  const cc = colorClass(color);
  const svgMarkup = buildSvg(def, { colorClass: cc });

  if (def.kind === 'wrap') {
    const place = placeClass(def.place);
    el.classList.add('gm-mark', place);
    el.insertAdjacentHTML('beforeend', svgMarkup);
    const svg = el.lastElementChild;
    return makeHandle({
      host: el,
      svg,
      speed,
      hold,
      autoplay,
      cleanup: () => { svg.remove(); el.classList.remove('gm-mark', place); }
    });
  }

  // inline (glyph / bullet / state / badge): a span we own, dropped into target
  const span = (el.ownerDocument || document).createElement('span');
  span.className = 'gm-mark gm-inline';
  span.innerHTML = svgMarkup;
  const svg = span.firstElementChild;
  el.appendChild(span);
  return makeHandle({
    host: span,
    svg,
    speed,
    hold,
    autoplay,
    cleanup: () => span.remove()
  });
}

/** Draw a mark and play it (convenience alias; same as drawMark with autoplay). */
export function playMark(target, options = {}) {
  return drawMark(target, { ...options, autoplay: true });
}

/**
 * Draw every element under `root` that carries a data-gm-mark attribute,
 * reading its options from data-gm-* attributes. Useful for author-tagged
 * passages and for inview triggering.
 * @returns {Array} one handle per tagged element
 */
export function playWithin(root = document, options = {}) {
  const scope = typeof root === 'string' ? document.querySelector(root) : root;
  if (!scope) return [];
  const nodes = [...scope.querySelectorAll('[data-gm-mark]')];
  return nodes.map(node => drawMark(node, { ...markFromDataset(node.dataset), ...options }));
}

export { makeBadge };
