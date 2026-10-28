/**
 * closeLogic — pure, DOM-free logic for the ab-close extension.
 * No Adapt/DOM dependencies; unit-testable in isolation.
 */

/**
 * Normalise a close button's data-* attributes into dismiss options.
 *
 * Recognised keys (from element.dataset):
 *   abDismiss        — a target selector, OR "" / "true" meaning "nearest
 *                      dismissible ancestor".
 *   abDismissRemove  — "false" keeps the element in the DOM (hidden) instead of
 *                      removing it. Default: remove.
 *   abDismissFade    — fade duration in ms (number-ish). Default 200; "0" = none.
 *
 * @param {Object} dataset
 * @returns {{ selector: (string|null), remove: boolean, fadeMs: number }}
 */
export function resolveDismiss(dataset = {}) {
  const raw = dataset.abDismiss;
  const selector = (raw && raw !== 'true') ? String(raw).trim() : null;
  return {
    selector: selector || null,
    remove: dataset.abDismissRemove !== 'false',
    fadeMs: toMs(dataset.abDismissFade, 200)
  };
}

/**
 * @param {*} value
 * @param {number} fallback
 * @returns {number} a non-negative integer millisecond value
 */
export function toMs(value, fallback) {
  if (value === undefined || value === null || value === '') return fallback;
  const n = parseInt(value, 10);
  return Number.isFinite(n) && n >= 0 ? n : fallback;
}
