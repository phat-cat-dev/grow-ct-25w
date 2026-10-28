/**
 * marksCatalogue.js — the mark artwork, as data.
 *
 * Pure data + accessors, no DOM. Each mark is one small SVG built from a list
 * of elements. Two animation kinds carry across both source galleries:
 *   - 'ink'  : a stroked outline that DRAWS on (stroke-dashoffset). marks.html.
 *   - 'pop'  : a filled shape that POPS in (scale). bullets.html.
 * Plus 'knob' (a filled shape that slides, for the toggle) and text badges.
 *
 * Geometry (viewBox + path data) is copied verbatim from the studies
 * `tool-theming/elearning-assets/gallery/marks.html` and `bullets.html`, so the
 * marks look identical. Only the class names are renamed to a `gm-` namespace.
 *
 * kind drives how the engine places a mark:
 *   'wrap'      — overlay the SVG on a word (underline, oval, box, strike …).
 *   'inline'    — an em-sized SVG dropped into a target (glyphs, bullets, badges).
 *   'highlight' — no SVG; a CSS marker sweep applied to the word.
 * category is metadata for grouping in a picker/demo.
 * color is the default colour role; callers may override.
 */

export const COLOR_ROLES = ['accent', 'positive', 'negative', 'neutral', 'comment', 'soft'];

// ---------------------------------------------------------------------------
// Emphasis marks that WRAP a word (preserveAspectRatio none so they stretch).
// ---------------------------------------------------------------------------
const EMPHASIS = {
  underline: {
    kind: 'wrap', category: 'emphasis', color: 'accent', place: 'under',
    viewBox: '0 0 200 12', preserveAspectRatio: 'none',
    els: [{ type: 'path', anim: 'ink', d: 'M4 7 C 60 1,120 11,196 6' }]
  },
  double: {
    kind: 'wrap', category: 'emphasis', color: 'accent', place: 'under2',
    viewBox: '0 0 200 16', preserveAspectRatio: 'none',
    els: [
      { type: 'path', anim: 'ink', d: 'M4 5 C 60 0,120 9,196 4' },
      { type: 'path', anim: 'ink', delay: 0.18, d: 'M6 13 C 62 8,118 15,194 11' }
    ]
  },
  wavy: {
    kind: 'wrap', category: 'emphasis', color: 'accent', place: 'under',
    viewBox: '0 0 200 16', preserveAspectRatio: 'none',
    els: [{ type: 'path', anim: 'ink', d: 'M4 9 q 14 -8 28 0 t 28 0 t 28 0 t 28 0 t 28 0 t 28 0' }]
  },
  oval: {
    kind: 'wrap', category: 'emphasis', color: 'accent', place: 'around',
    viewBox: '0 0 200 70', preserveAspectRatio: 'none',
    els: [{ type: 'path', anim: 'ink', width: 3, d: 'M152 14 C 60 2,10 20,18 44 C 26 68,140 70,182 52 C 214 40,204 15,150 11' }]
  },
  box: {
    kind: 'wrap', category: 'emphasis', color: 'accent', place: 'box',
    viewBox: '0 0 200 64', preserveAspectRatio: 'none',
    els: [{ type: 'path', anim: 'ink', width: 3, d: 'M9 9 L192 6 L195 55 L6 58 Z' }]
  },
  bracket: {
    kind: 'wrap', category: 'emphasis', color: 'accent', place: 'bracket',
    viewBox: '0 0 200 64', preserveAspectRatio: 'none',
    els: [
      { type: 'path', anim: 'ink', width: 3, d: 'M22 8 L8 8 L8 56 L22 56' },
      { type: 'path', anim: 'ink', width: 3, delay: 0.18, d: 'M178 8 L192 8 L192 56 L178 56' }
    ]
  },
  strike: {
    kind: 'wrap', category: 'emphasis', color: 'negative', place: 'through',
    viewBox: '0 0 200 14', preserveAspectRatio: 'none',
    els: [{ type: 'path', anim: 'ink', d: 'M4 8 C 60 3,120 12,196 7' }]
  },
  scribble: {
    kind: 'wrap', category: 'emphasis', color: 'negative', place: 'cover',
    viewBox: '0 0 200 40', preserveAspectRatio: 'none',
    els: [{ type: 'path', anim: 'ink', width: 5, d: 'M6 24 L36 10 L66 26 L96 10 L126 26 L156 11 L192 22 M186 13 L150 29 L116 14 L84 28 L52 14 L12 27' }]
  },
  highlight: {
    kind: 'highlight', category: 'emphasis', color: 'accent'
  }
};

// ---------------------------------------------------------------------------
// Standalone glyphs — inline, em-sized. Ticks, crosses, arrows, feedback marks.
// ---------------------------------------------------------------------------
const GLYPH = {
  tick: {
    kind: 'inline', category: 'glyph', color: 'positive', viewBox: '0 0 48 48',
    els: [{ type: 'path', anim: 'ink', d: 'M9 26 L21 38 L40 11' }]
  },
  cross: {
    kind: 'inline', category: 'glyph', color: 'negative', viewBox: '0 0 48 48',
    els: [
      { type: 'path', anim: 'ink', d: 'M12 12 L37 37' },
      { type: 'path', anim: 'ink', delay: 0.25, d: 'M37 12 L12 37' }
    ]
  },
  arrow: {
    kind: 'inline', category: 'glyph', color: 'accent', viewBox: '0 0 40 40',
    els: [{ type: 'path', anim: 'ink', d: 'M9 20 L29 20 M29 20 L22 13 M29 20 L22 27' }]
  },
  'arrow-curved': {
    kind: 'inline', category: 'glyph', color: 'accent', viewBox: '0 0 60 48',
    els: [
      { type: 'path', anim: 'ink', d: 'M6 20 C 26 8,44 16,52 34' },
      { type: 'path', anim: 'ink', delay: 0.3, d: 'M52 34 L40 30 M52 34 L50 20' }
    ]
  },
  star: {
    kind: 'inline', category: 'glyph', color: 'neutral', viewBox: '0 0 54 54',
    els: [{ type: 'path', anim: 'ink', d: 'M27 5 L34 22 L52 22 L37 33 L43 50 L27 39 L11 50 L17 33 L2 22 L20 22 Z' }]
  },
  caret: {
    kind: 'inline', category: 'glyph', color: 'comment', viewBox: '0 0 48 34',
    els: [{ type: 'path', anim: 'ink', d: 'M6 28 L24 6 L42 28' }]
  },
  checkbox: {
    kind: 'inline', category: 'glyph', color: 'positive', viewBox: '0 0 52 52',
    els: [
      { type: 'path', anim: 'ink', width: 3, d: 'M9 9 L43 7 L45 43 L7 45 Z' },
      { type: 'path', anim: 'ink', delay: 0.3, d: 'M15 26 L23 34 L39 16' }
    ]
  },
  exclaim: {
    kind: 'inline', category: 'glyph', color: 'neutral', viewBox: '0 0 52 58',
    els: [
      { type: 'path', anim: 'ink', width: 6, d: 'M26 10 L26 34' },
      { type: 'path', anim: 'ink', width: 7, delay: 0.2, d: 'M26 44 L26 45.5' }
    ]
  },
  question: {
    kind: 'inline', category: 'glyph', color: 'accent', viewBox: '0 0 52 58',
    els: [
      { type: 'path', anim: 'ink', width: 5, d: 'M13 19 C 12 7,40 6,40 19 C 40 29,26 28,26 38' },
      { type: 'path', anim: 'ink', width: 6, delay: 0.25, d: 'M26 46 L26 47.5' }
    ]
  },
  plus: {
    kind: 'inline', category: 'glyph', color: 'accent', viewBox: '0 0 40 40',
    els: [
      { type: 'path', anim: 'ink', d: 'M20 10 L20 30' },
      { type: 'path', anim: 'ink', delay: 0.15, d: 'M10 20 L30 20' }
    ]
  },
  heart: {
    kind: 'inline', category: 'glyph', color: 'negative', viewBox: '0 0 40 40',
    els: [{ type: 'path', anim: 'pop', d: 'M20 31 C 6 22,8 11,16 12 C 19 12,20 15,20 15 C 20 15,21 12,24 12 C 32 11,34 22,20 31 Z' }]
  }
};

// ---------------------------------------------------------------------------
// Bullets / list markers — inline, em-sized. Round, angular, pointers.
// ---------------------------------------------------------------------------
const BULLET = {
  dot: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'circle', anim: 'pop', cx: 20, cy: 20, r: 7 }] },
  disc: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'circle', anim: 'pop', cx: 20, cy: 20, r: 11 }] },
  ring: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'circle', anim: 'ink', width: 3, cx: 20, cy: 20, r: 11 }] },
  'ring-dot': {
    kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40',
    els: [
      { type: 'circle', anim: 'ink', width: 3, cx: 20, cy: 20, r: 12 },
      { type: 'circle', anim: 'pop', delay: 0.25, cx: 20, cy: 20, r: 5 }
    ]
  },
  'check-ring': {
    kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40',
    els: [
      { type: 'circle', anim: 'ink', width: 3, cx: 20, cy: 20, r: 12 },
      { type: 'path', anim: 'ink', width: 3.5, color: 'positive', delay: 0.25, d: 'M14 20 L18 25 L27 14' }
    ]
  },
  square: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'rect', anim: 'ink', width: 3, x: 9, y: 9, w: 22, h: 22, rx: 3 }] },
  'square-fill': { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'rect', anim: 'pop', x: 10, y: 10, w: 20, h: 20, rx: 3 }] },
  diamond: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'ink', width: 3, d: 'M20 7 L33 20 L20 33 L7 20 Z' }] },
  'diamond-fill': { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'pop', d: 'M20 8 L32 20 L20 32 L8 20 Z' }] },
  triangle: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'ink', width: 3, d: 'M20 9 L31 29 L9 29 Z' }] },
  hexagon: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'ink', width: 3, d: 'M8 13 L20 9 L32 13 L30 27 L20 32 L10 27 Z' }] },
  chevron: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'ink', d: 'M16 11 L26 20 L16 29' }] },
  'chevron-down': { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'ink', d: 'M11 16 L20 26 L29 16' }] },
  play: { kind: 'inline', category: 'bullet', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'pop', d: 'M13 10 L31 20 L13 30 Z' }] }
};

// ---------------------------------------------------------------------------
// Objects & states — inline. Radios, checkboxes, toggle, pin, bookmark, tag.
// ---------------------------------------------------------------------------
const STATE = {
  'radio-off': { kind: 'inline', category: 'state', color: 'soft', viewBox: '0 0 40 40', els: [{ type: 'circle', anim: 'ink', width: 3, cx: 20, cy: 20, r: 12 }] },
  'radio-on': {
    kind: 'inline', category: 'state', color: 'accent', viewBox: '0 0 40 40',
    els: [
      { type: 'circle', anim: 'ink', width: 3, cx: 20, cy: 20, r: 12 },
      { type: 'circle', anim: 'pop', delay: 0.25, cx: 20, cy: 20, r: 6 }
    ]
  },
  'check-off': { kind: 'inline', category: 'state', color: 'soft', viewBox: '0 0 40 40', els: [{ type: 'rect', anim: 'ink', width: 3, x: 9, y: 9, w: 22, h: 22, rx: 4 }] },
  'check-on': {
    kind: 'inline', category: 'state', color: 'positive', viewBox: '0 0 40 40',
    els: [
      { type: 'rect', anim: 'ink', width: 3, x: 9, y: 9, w: 22, h: 22, rx: 4 },
      { type: 'path', anim: 'ink', width: 3.5, delay: 0.25, d: 'M14 20 L18 25 L27 14' }
    ]
  },
  toggle: {
    kind: 'inline', category: 'state', color: 'accent', viewBox: '0 0 48 40',
    els: [
      { type: 'rect', anim: 'ink', width: 3, x: 7, y: 13, w: 34, h: 16, rx: 8 },
      { type: 'circle', anim: 'knob', cx: 31, cy: 21, r: 6, fill: 'var(--accent)' }
    ]
  },
  pin: {
    kind: 'inline', category: 'state', color: 'accent', viewBox: '0 0 40 40',
    els: [
      { type: 'path', anim: 'ink', width: 3, d: 'M20 6 C 12 6,8 13,12 22 L20 34 L28 22 C 32 13,28 6,20 6 Z' },
      { type: 'circle', anim: 'pop', delay: 0.3, cx: 20, cy: 17, r: 4.5, fill: 'var(--surface-2)' }
    ]
  },
  bookmark: { kind: 'inline', category: 'state', color: 'accent', viewBox: '0 0 40 40', els: [{ type: 'path', anim: 'ink', width: 3, d: 'M13 7 L27 7 L27 33 L20 26 L13 33 Z' }] },
  tag: {
    kind: 'inline', category: 'state', color: 'accent', viewBox: '0 0 40 40',
    els: [
      { type: 'path', anim: 'ink', width: 3, d: 'M9 9 L22 9 L33 20 L22 31 L9 31 Z' },
      { type: 'circle', anim: 'pop', delay: 0.25, cx: 16, cy: 16, r: 2.6, fill: 'var(--accent)' }
    ]
  }
};

/** The full static catalogue, id -> definition. */
export const MARKS = { ...EMPHASIS, ...GLYPH, ...BULLET, ...STATE };

/** Build a numbered or lettered badge definition on demand (not stored). */
export function makeBadge(label) {
  const text = String(label);
  return {
    kind: 'inline', category: 'badge', color: 'accent', viewBox: '0 0 40 40',
    els: [
      { type: 'circle', anim: 'pop', cx: 20, cy: 20, r: 15 },
      { type: 'text', anim: 'pop', delay: 0.08, x: 20, y: 20, content: text, fontSize: text.length > 1 ? 13 : 16 }
    ]
  };
}

export function getMark(id) {
  return Object.prototype.hasOwnProperty.call(MARKS, id) ? MARKS[id] : null;
}

export function hasMark(id) {
  return Object.prototype.hasOwnProperty.call(MARKS, id);
}

export function listMarks(category) {
  const ids = Object.keys(MARKS);
  return category ? ids.filter(id => MARKS[id].category === category) : ids;
}

export function categories() {
  return [...new Set(Object.values(MARKS).map(m => m.category))];
}
