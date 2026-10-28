/**
 * scrollScenesLogic.js
 *
 * Pure functions for the scroll-scenes engine. Extracted from the original
 * `scroll-scenes.js` / `scroll-scenes.patched.js` study so the maths can be
 * unit-tested without Backbone or the DOM (matches the family convention, e.g.
 * timelineLogic.js / confidenceLogic.js).
 *
 * The driver (scrollScenesDriver.js) owns the DOM; this file owns the numbers
 * and the presentation vocabulary.
 */

// ---------------------------------------------------------------------------
// Vocabulary — the allowed values for each design dial.
// ---------------------------------------------------------------------------

/** JavaScript-driven effects written as inline styles on [data-scene-content]. */
export const EFFECTS = ['none', 'fade', 'slide', 'zoom', 'blur'];

/** CSS background libraries (scroll-scenes.backgrounds.css, section 4). */
export const BACKGROUNDS = ['lines', 'aurora', 'mesh', 'dots', 'grid', 'contour', 'horizon', 'spotlight', 'weave', 'wash', 'plain'];

/** CSS transition models (scroll-scenes.backgrounds.css, section 5). */
export const TRANSITIONS = ['none', 'rise', 'drift', 'tilt', 'wipe', 'stagger'];

/** Colour schemes (scroll-scenes.backgrounds.css, section 1). */
export const SCHEMES = ['default', 'night', 'warm', 'dusk'];

/**
 * Preset bundles — a scheme, background, transition model and effect that suit
 * each other (STYLE-STRUCTURE.md section 6). `custom` is the neutral base used
 * when an author wants to drive every dial by hand.
 */
export const PRESETS = {
  original: { scheme: 'default', background: 'lines', transition: 'none', effect: 'zoom' },
  calm: { scheme: 'default', background: 'wash', transition: 'none', effect: 'zoom' },
  technical: { scheme: 'default', background: 'grid', transition: 'drift', effect: 'fade' },
  editorial: { scheme: 'warm', background: 'spotlight', transition: 'stagger', effect: 'fade' },
  atlas: { scheme: 'dusk', background: 'contour', transition: 'tilt', effect: 'fade' },
  'horizon-rise': { scheme: 'default', background: 'horizon', transition: 'rise', effect: 'fade' },
  'night-study': { scheme: 'night', background: 'aurora', transition: 'none', effect: 'blur' },
  custom: { scheme: 'default', background: 'lines', transition: 'none', effect: 'zoom' }
};

/**
 * Resolve a preset plus optional overrides into the four concrete design
 * values. Mirrors the precedence in the retired scenes.py render_page: start
 * from the preset, then let any non-empty, valid override win. An unknown or
 * empty override falls back to the preset's value (never throws — authoring
 * input should degrade, not break the page).
 *
 * @param {object} props - component model attributes
 * @param {string} [props._preset]
 * @param {string} [props._scheme]  '' = inherit preset
 * @param {string} [props._background]
 * @param {string} [props._transition]
 * @param {string} [props._effect]
 * @param {boolean} [props._snap]
 * @returns {{scheme:string, background:string, transition:string, effect:string, snap:boolean}}
 */
export function resolvePresentation(props = {}) {
  const base = PRESETS[props._preset] || PRESETS.original;
  const pick = (override, allowed, fallback) => {
    const value = (override == null ? '' : String(override)).trim();
    if (!value) return fallback;
    return allowed.includes(value) ? value : fallback;
  };
  return {
    scheme: pick(props._scheme, SCHEMES, base.scheme),
    background: pick(props._background, BACKGROUNDS, base.background),
    transition: pick(props._transition, TRANSITIONS, base.transition),
    effect: pick(props._effect, EFFECTS, base.effect),
    snap: props._snap === undefined ? true : !!props._snap
  };
}

// ---------------------------------------------------------------------------
// Scroll maths — position in, style out. Scrolling back reverses everything
// because every value comes from position, not from time.
// ---------------------------------------------------------------------------

/** Signed position of a scene relative to the viewport centre, in viewport heights. */
export function sceneOffset(sceneCenter, viewportCenter, viewportHeight) {
  return (sceneCenter - viewportCenter) / Math.max(1, viewportHeight);
}

/** Distance from centre, clamped to one viewport height (0 at centre, 1 far away). */
export function clampDistance(offset) {
  return Math.min(1, Math.abs(offset));
}

/** Index of the scene nearest the centre (first wins on a tie, matching the original). */
export function nearestIndex(offsets) {
  let index = 0;
  let best = Infinity;
  offsets.forEach((offset, i) => {
    const absolute = Math.abs(offset);
    if (absolute < best) {
      best = absolute;
      index = i;
    }
  });
  return index;
}

/** Scroll progress of the viewport, 0..1 (1 when there is nothing to scroll). */
export function scrollProgress(scrollTop, scrollHeight, clientHeight) {
  const range = scrollHeight - clientHeight;
  return range > 0 ? scrollTop / range : 1;
}

/**
 * The inline styles the driver writes onto one [data-scene-content], derived
 * from its offset and the active effect. Identical formulae to the original
 * render() loop (opacity never drops below 0.35, so neighbours stay legible),
 * plus the two custom properties the CSS transition models read.
 *
 * @param {number} offset - from sceneOffset()
 * @param {string} effect - one of EFFECTS
 * @param {boolean} reducedMotion - system / .no-motion / data-tm-no-motion
 * @returns {{opacity:string, translate:string, scale:string, filter:string,
 *            ['--scene-offset']:string, ['--scene-distance']:string}}
 */
export function computeSceneStyles(offset, effect, reducedMotion) {
  const distance = clampDistance(offset);
  const still = reducedMotion || effect === 'none';
  return {
    '--scene-offset': offset.toFixed(4),
    '--scene-distance': distance.toFixed(4),
    opacity: still ? '1' : String(1 - distance * 0.65),
    translate: (!reducedMotion && effect === 'slide') ? `${offset * 45}px 0` : 'none',
    scale: (!reducedMotion && (effect === 'zoom' || effect === 'blur')) ? String(1 - distance * 0.12) : 'none',
    filter: (!reducedMotion && effect === 'blur') ? `blur(${distance * 7}px)` : 'none'
  };
}

/** Is this a known effect? Used by the driver's set() guard. */
export function isValidEffect(effect) {
  return EFFECTS.includes(effect);
}
