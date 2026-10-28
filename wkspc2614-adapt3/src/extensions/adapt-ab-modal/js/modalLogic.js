/**
 * modalLogic — pure, DOM-free logic for the ab-modal extension.
 * No Adapt/DOM dependencies; unit-testable in isolation.
 */

export const SIZES = ['sm', 'lg', 'xl'];

/**
 * Normalise a requested modal size to a Bootstrap-shaped dialog class suffix.
 * Unknown/empty -> '' (default width).
 * @param {string} size
 * @returns {string} '', 'modal-sm', 'modal-lg' or 'modal-xl'
 */
export function sizeClass(size) {
  return SIZES.includes(size) ? `modal-${size}` : '';
}

/**
 * Resolve the content/options for a modal open request from a trigger's data-*
 * attributes, optionally backed by a configured modal (matched by id).
 *
 * Inline data-* attributes always override the matched config, so a configured
 * modal can be reused and tweaked per trigger.
 *
 * @param {Object} dataset - a trigger's dataset-like object. Recognised keys:
 *   abModal (id), abModalTitle, abModalBody, abModalSize,
 *   abModalStatic ("true"), abModalCentered ("true"), abModalScrollable ("true")
 * @param {Array<Object>} [modals] - configured modals: { _id, title, body, _size,
 *   _isStatic, _isCentered, _isScrollable }
 * @returns {Object|null} resolved content, or null if there is nothing to show
 */
export function resolveModal(dataset = {}, modals = []) {
  const id = dataset.abModal || '';
  const cfg = (modals || []).find(m => m && m._id === id) || {};

  const title = pick(dataset.abModalTitle, cfg.title, '');
  const body = pick(dataset.abModalBody, cfg.body, '');

  // nothing to show at all
  if (!title && !body) return null;

  return {
    id: id || null,
    title,
    body,
    size: sizeClass(pick(dataset.abModalSize, cfg._size, '')),
    isStatic: boolOf(dataset.abModalStatic, cfg._isStatic, false),
    isCentered: boolOf(dataset.abModalCentered, cfg._isCentered, false),
    isScrollable: boolOf(dataset.abModalScrollable, cfg._isScrollable, false)
  };
}

/**
 * Given the count of focusable elements and the currently focused index, return
 * the next index when Tab (or Shift+Tab) would otherwise leave the trap.
 * Returns -1 when no wrap is needed (focus stays where the browser puts it).
 *
 * @param {number} activeIndex - index of the focused element (-1 if none/outside)
 * @param {number} count - number of focusable elements in the trap
 * @param {boolean} shiftKey
 * @returns {number} the index to force focus to, or -1 for "no change"
 */
export function trapWrapIndex(activeIndex, count, shiftKey) {
  if (count <= 0) return -1;
  if (count === 1) return 0; // single focusable: keep it focused
  if (!shiftKey && activeIndex === count - 1) return 0;      // Tab off the end -> first
  if (shiftKey && activeIndex <= 0) return count - 1;         // Shift+Tab off the start -> last
  return -1;
}

function pick(...vals) {
  for (const v of vals) {
    if (v !== undefined && v !== null && v !== '') return v;
  }
  return vals.length ? vals[vals.length - 1] : undefined;
}

function boolOf(...vals) {
  for (const v of vals) {
    if (v === true) return true;
    if (v === false) return false;
    if (v === 'true') return true;
    if (v === 'false') return false;
  }
  return false;
}
