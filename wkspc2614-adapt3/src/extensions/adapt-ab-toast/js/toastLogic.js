/**
 * toastLogic — pure, DOM-free logic for the ab-toast extension.
 * No Adapt/DOM dependencies; unit-testable in isolation.
 */

export const VARIANTS = ['accent', 'success', 'danger', 'warning', 'info'];

/**
 * Parse a delay (ms) to a non-negative integer, else the fallback.
 * @param {*} value
 * @param {number} fallback
 * @returns {number}
 */
export function toDelay(value, fallback) {
  if (value === undefined || value === null || value === '') return fallback;
  const n = parseInt(value, 10);
  return Number.isFinite(n) && n >= 0 ? n : fallback;
}

/**
 * Normalise a toast request into a render spec.
 *
 * @param {Object} opts - { id, title, body, variant, autohide, delay, showClose }
 * @returns {{id:(string|null),title:string,body:string,variant:string,
 *   autohide:boolean,delay:number,showClose:boolean}}
 */
export function resolveToast(opts = {}) {
  return {
    id: opts.id || null,
    title: opts.title || '',
    body: opts.body || '',
    variant: VARIANTS.includes(opts.variant) ? opts.variant : '',
    autohide: opts.autohide !== false,
    delay: toDelay(opts.delay, 5000),
    showClose: opts.showClose !== false
  };
}
