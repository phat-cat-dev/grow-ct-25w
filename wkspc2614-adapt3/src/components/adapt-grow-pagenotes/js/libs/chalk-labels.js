/* chalk-labels.js - turns a pattern's data object into SVG text or HTML boxes.
   Vendored from adapt-content-templates/adapt-grow-animations/chalk-patterns and
   converted from UMD to an ES module for the Adapt build: the pattern data is
   imported directly instead of read off window.CHALK_PATTERN_DATA. Behaviour is
   otherwise unchanged. render()/play() are what adapt-grow-pagenotes uses. */
import CHALK_PATTERN_DATA from './chalk-pattern-data.js';

const VIEW = { width: 300, height: 160 };
const FONT = 12;
const LINE = 14;
const TOKEN = /\{\{\s*([A-Za-z][\w-]*(?:\.[\w-]+)*)\s*\}\}/g;
const NS = 'http://www.w3.org/2000/svg';

const escapeHtml = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const writeName = ([from, to]) => `chalk-write-${Math.round(from * 100)}-${Math.round(to * 100)}`;

function firstBaseline(y, valign) {
  if (valign === 'top') return y + FONT * 0.8;
  if (valign === 'bottom') return y - FONT * 0.25;
  return y + FONT * 0.35;
}

function strokePaths(pattern) {
  return pattern.strokes.map(stroke => `<path class="edu-stroke${stroke.arrow ? ' edu-arrow' : ''}" pathLength="1" d="${stroke.d}"${stroke.stage ? ` data-chalk-stage="${stroke.stage}"` : ''} style="--edu-animation:${stroke.animation}"/>`).join('');
}

function rootAttributes({ tone, palette, labelTone, labelStyle, font }) {
  return [
    tone && `data-chalk-tone="${escapeHtml(tone)}"`,
    palette && `data-chalk-palette="${escapeHtml(palette)}"`,
    labelTone && `data-chalk-label-tone="${escapeHtml(labelTone)}"`,
    labelStyle && `data-chalk-label-style="${escapeHtml(labelStyle)}"`,
    font && `data-chalk-font="${escapeHtml(font)}"`
  ].filter(Boolean).map(attribute => ` ${attribute}`).join('');
}

/* SVG mode: each label is a live <text> element inside the drawing. */
function toSvg(pattern, options = {}) {
  const { running = false, styles = '', tone = pattern.tone } = options;
  const labels = pattern.slots.map(slot => {
    const { x, y, w, align, valign } = slot.box;
    return `<text class="chalk-label" data-chalk-slot="${slot.key}"${slot.stage ? ` data-chalk-stage="${slot.stage}"` : ''} data-w="${w}" data-valign="${valign}" x="${x}" y="${firstBaseline(y, valign).toFixed(2)}" text-anchor="${align}" style="--chalk-write:${writeName(slot.reveal)}">${slot.token}</text>`;
  }).join('');
  return `<svg xmlns="${NS}" class="edu-svg edu-chalk${running ? ' edu-running' : ''}" viewBox="0 0 ${VIEW.width} ${VIEW.height}" role="img" aria-label="{{title}}"${rootAttributes({ ...options, tone })}>${styles ? `<style>${styles}</style>` : ''}${strokePaths(pattern)}${labels}</svg>`;
}

/* HTML mode: each label is an absolutely placed box over a decorative drawing. */
function toHtml(pattern, options = {}) {
  const { running = false, tone = pattern.tone } = options;
  const labels = pattern.slots.map(slot => {
    const { x, y, w, align, valign } = slot.box;
    return `<div class="chalk-label" data-chalk-slot="${slot.key}"${slot.stage ? ` data-chalk-stage="${slot.stage}"` : ''} data-align="${align}" data-valign="${valign}" style="--x:${x};--y:${y};--w:${w};--chalk-write:${writeName(slot.reveal)}">${slot.token}</div>`;
  }).join('');
  /* A detail is too long to sit beside a stroke, so it goes in a list under the drawing. */
  const details = pattern.slots.map(slot => `<li class="chalk-detail" data-chalk-slot="${slot.key}"${slot.stage ? ` data-chalk-stage="${slot.stage}"` : ''} style="--chalk-write:${writeName(slot.reveal)}"><span class="chalk-detail-term">${slot.token}</span> <span class="chalk-detail-text">{{${slot.key}.detail}}</span></li>`).join('');
  return `<figure class="chalk-stage${running ? ' edu-running' : ''}" role="group" aria-label="{{title}}"${rootAttributes({ ...options, tone })}><div class="chalk-canvas"><svg xmlns="${NS}" class="edu-svg edu-chalk" viewBox="0 0 ${VIEW.width} ${VIEW.height}" aria-hidden="true" focusable="false">${strokePaths(pattern)}</svg>${labels}</div><ol class="chalk-details">${details}</ol></figure>`;
}

/* Replaces {{tokens}} with escaped values. A token with no value becomes empty,
   and CSS hides empty labels, so optional slots can be left out of the data. */
function fill(template, data = {}) {
  return template.replace(TOKEN, (_, path) => {
    const value = path.split('.').reduce((node, key) => (node == null ? undefined : node[key]), data);
    return value == null ? '' : escapeHtml(value);
  });
}

function resolve(pattern) {
  if (typeof pattern !== 'string') return pattern;
  const found = CHALK_PATTERN_DATA?.patterns?.[pattern];
  if (!found) throw new Error(`Unknown chalk pattern: ${pattern}.`);
  return found;
}

/* A misspelt key would otherwise leave a label silently blank. */
function check(pattern, data) {
  const known = new Set(['title', ...pattern.slots.map(slot => slot.key)]);
  const unknown = Object.keys(data).filter(key => !known.has(key));
  if (unknown.length) throw new Error(`${pattern.slug} has no slot called: ${unknown.join(', ')}. Available: ${[...known].join(', ')}.`);
  for (const [key, value] of Object.entries(data)) {
    if (key === 'title') continue;
    const fields = Object.keys(value).filter(field => field !== 'label' && field !== 'detail');
    if (fields.length) throw new Error(`${pattern.slug}/${key} has an unknown field: ${fields.join(', ')}. Use label or detail.`);
  }
}

function accessibleName(pattern, data) {
  if (data.title) return data.title;
  const labels = pattern.slots.map(slot => data[slot.key]?.label).filter(Boolean);
  return labels.length ? `${pattern.title}: ${labels.join(', ')}` : pattern.title;
}

/* SVG text cannot wrap on its own, so measure it and break it into tspans. */
function wrapSvgLabels(svg) {
  svg.querySelectorAll('text.chalk-label').forEach(text => {
    const content = text.textContent.trim();
    const limit = Number(text.dataset.w);
    if (!content || typeof text.getComputedTextLength !== 'function' || text.getComputedTextLength() <= limit) return;
    const x = text.getAttribute('x');
    const baseline = Number(text.getAttribute('y'));
    const lines = [];
    let line = '';
    for (const word of content.split(/\s+/)) {
      const trial = line ? `${line} ${word}` : word;
      text.textContent = trial;
      if (line && text.getComputedTextLength() > limit) {
        lines.push(line);
        line = word;
      } else line = trial;
    }
    lines.push(line);
    const block = (lines.length - 1) * LINE;
    const offset = { top: 0, middle: block / 2, bottom: block }[text.dataset.valign];
    text.textContent = '';
    lines.forEach((value, index) => {
      const tspan = document.createElementNS(NS, 'tspan');
      tspan.setAttribute('x', x);
      tspan.setAttribute('y', (baseline - offset + index * LINE).toFixed(2));
      tspan.textContent = value;
      text.append(tspan);
    });
  });
}

/* Waits for play(), like the gallery previews: finished artwork shows until then. */
function render(host, { pattern, mode = 'svg', data = {}, ...options }) {
  const resolved = resolve(pattern);
  if (mode !== 'svg' && mode !== 'html') throw new Error(`Unknown chalk label mode: ${mode}. Use "svg" or "html".`);
  check(resolved, data);
  const template = mode === 'svg' ? toSvg(resolved, options) : toHtml(resolved, options);
  host.innerHTML = fill(template, { ...data, title: accessibleName(resolved, data) });
  const element = host.firstElementChild;
  if (mode === 'svg') wrapSvgLabels(element);
  return element;
}

function play(element) {
  element.classList.remove('edu-running', 'edu-paused');
  void element.getBoundingClientRect();
  element.classList.add('edu-running');
}

function pause(element, paused = !element.classList.contains('edu-paused')) {
  element.classList.toggle('edu-paused', paused);
  return paused;
}

export { VIEW, toSvg, toHtml, fill, render, play, pause, writeName };
export default { VIEW, toSvg, toHtml, fill, render, play, pause, writeName };
