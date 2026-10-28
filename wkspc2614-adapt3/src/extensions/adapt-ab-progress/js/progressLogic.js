/**
 * progressLogic — pure, DOM-free logic for the ab-progress extension.
 * No Adapt/DOM dependencies; unit-testable in isolation.
 */

/**
 * Percentage fill for value/max, clamped to [0,100] and rounded to 1 dp.
 * Returns 0 for non-finite input or max <= 0.
 * @param {*} value
 * @param {*} max
 * @returns {number}
 */
export function clampPercent(value, max) {
  const v = Number(value);
  const m = Number(max);
  if (!Number.isFinite(v) || !Number.isFinite(m) || m <= 0) return 0;
  const pct = (v / m) * 100;
  return Math.max(0, Math.min(100, Math.round(pct * 10) / 10));
}

/**
 * Normalise a progress element's data-* attributes into a render spec.
 *
 * Recognised keys (element.dataset):
 *   abProgressValue, abProgressMax, abProgressLabel,
 *   abProgressShowLabel ("true"), abProgressVariant (success|danger|warning|info),
 *   abProgressStriped ("true"), abProgressAnimated ("true")
 *
 * @param {Object} dataset
 * @returns {{value:number,max:number,percent:number,label:string,
 *   showLabel:boolean,variant:string,striped:boolean,animated:boolean}}
 */
export function resolveProgress(dataset = {}) {
  const value = toNum(dataset.abProgressValue, 0);
  const max = toNum(dataset.abProgressMax, 100);
  return {
    value,
    max,
    percent: clampPercent(value, max),
    label: dataset.abProgressLabel || '',
    showLabel: dataset.abProgressShowLabel === 'true',
    variant: dataset.abProgressVariant || '',
    striped: dataset.abProgressStriped === 'true',
    animated: dataset.abProgressAnimated === 'true'
  };
}

/**
 * The visible/aria text for a resolved spec: an explicit label wins, else the
 * percentage when showLabel is set, else ''.
 * @param {Object} p - a resolveProgress() result
 * @returns {string}
 */
export function progressText(p) {
  if (p.label) return p.label;
  if (p.showLabel) return `${p.percent}%`;
  return '';
}

function toNum(value, fallback) {
  if (value === undefined || value === null || value === '') return fallback;
  const n = Number(value);
  return Number.isFinite(n) ? n : fallback;
}
