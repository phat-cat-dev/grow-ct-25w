/**
 * marksLogic.js — pure helpers, no DOM.
 *
 * Turns a catalogue definition into SVG markup, resolves colour roles and
 * speed, and reads options from a `data-gm-*` dataset. All unit-tested.
 */

/** Colour role -> CSS class. The classes map to GROW theme tokens in the CSS. */
export const COLOR_CLASS = {
  accent: 'gm-accent',
  positive: 'gm-ok',
  negative: 'gm-no',
  neutral: 'gm-warn',
  comment: 'gm-vio',
  soft: 'gm-soft'
};

/** A colour role's class, falling back to accent for anything unknown/empty. */
export function colorClass(role) {
  return COLOR_CLASS[role] || COLOR_CLASS.accent;
}

/** Clamp a speed multiplier to the sane range; non-numbers become 1. */
export function clampSpeed(value) {
  const n = Number(value);
  if (!isFinite(n) || n <= 0) return 1;
  return Math.min(2.5, Math.max(0.4, n));
}

/** The CSS class for one element, from its animation kind. */
export function elementClass(el) {
  if (el.type === 'text') return 'gm-num gm-pop';
  if (el.anim === 'pop') return 'gm-fill gm-pop';
  if (el.anim === 'knob') return 'gm-fill gm-knob';
  if (el.anim === 'static') return 'gm-dash';
  return 'gm-ink';
}

/** Markup for one catalogue element (path / circle / rect / text). */
export function elementMarkup(el) {
  const base = elementClass(el);
  const isInk = base === 'gm-ink';
  const classes = el.color ? `${base} ${colorClass(el.color)}` : base;

  const style = [];
  if (el.delay) style.push(`--gm-d:${el.delay}s`);
  if (el.width != null) style.push(`stroke-width:${el.width}`);
  if (el.fill) style.push(`fill:${el.fill}`);
  if (el.dash) style.push(`stroke-dasharray:${el.dash}`);
  if (el.type === 'text' && el.fontSize) style.push(`font-size:${el.fontSize}px`);
  const styleAttr = style.length ? ` style="${style.join(';')}"` : '';
  const pl = isInk ? ' pathLength="1"' : '';

  switch (el.type) {
    case 'circle':
      return `<circle class="${classes}"${pl}${styleAttr} cx="${el.cx}" cy="${el.cy}" r="${el.r}"/>`;
    case 'rect':
      return `<rect class="${classes}"${pl}${styleAttr} x="${el.x}" y="${el.y}" width="${el.w}" height="${el.h}" rx="${el.rx || 0}"/>`;
    case 'text':
      return `<text class="${classes}"${styleAttr} x="${el.x}" y="${el.y}">${el.content}</text>`;
    default:
      return `<path class="${classes}"${pl}${styleAttr} d="${el.d}"/>`;
  }
}

/** Build the full SVG string for a mark definition. */
export function buildSvg(def, options = {}) {
  const cc = options.colorClass || colorClass(def.color || 'accent');
  const par = def.preserveAspectRatio ? ` preserveAspectRatio="${def.preserveAspectRatio}"` : '';
  const body = (def.els || []).map(elementMarkup).join('');
  return `<svg class="gm-svg ${cc}" viewBox="${def.viewBox}"${par} aria-hidden="true" focusable="false">${body}</svg>`;
}

/** Placement class for a wrap mark (gm-place-under, gm-place-around, …). */
export function placeClass(place) {
  return `gm-place-${place || 'under'}`;
}

/**
 * Read mark options from a data-gm-* dataset (as on a DOM element).
 * data-gm-mark, data-gm-color, data-gm-speed, data-gm-hold, data-gm-variant.
 */
export function markFromDataset(dataset = {}) {
  const out = { mark: dataset.gmMark };
  if (dataset.gmColor) out.color = dataset.gmColor;
  if (dataset.gmVariant) out.variant = dataset.gmVariant;
  if (dataset.gmSpeed != null && dataset.gmSpeed !== '') out.speed = clampSpeed(dataset.gmSpeed);
  if (dataset.gmHold != null) out.hold = dataset.gmHold !== 'false';
  return out;
}
