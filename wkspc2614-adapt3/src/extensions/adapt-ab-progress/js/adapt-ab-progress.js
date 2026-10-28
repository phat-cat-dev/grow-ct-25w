/**
 * adapt-ab-progress
 *
 * A Bootstrap-5 progress bar (.ab.progress > .progress-bar) as an extension,
 * usable ANYWHERE — authored inline, or embedded and driven by an interactive
 * component / modal. Dependency-free.
 *
 * Declarative (static): author the container; the extension builds the fill +
 * ARIA from its data-* attributes:
 *
 *   <div class="ab progress"
 *     data-ab-progress
 *     data-ab-progress-value="40" data-ab-progress-max="100"
 *     data-ab-progress-show-label="true"></div>
 *
 * Programmatic (dynamic): a host updates a bar by element or selector —
 *
 *   Adapt.trigger('abProgress:set', { target: el, value: 7, max: 10 });
 *   Adapt.trigger('abProgress:set', { target: '#load', value: 100, variant: 'success' });
 *
 * Only the keys you pass change; the rest are read from the element's current
 * data-*. Emits Adapt.trigger('abProgress:changed', el, spec).
 *
 * Options (data-* / event fields): value, max, label, showLabel, variant
 * (success|danger|warning|info), striped, animated.
 *
 * Enable/disable (course.json), default ENABLED when absent:
 *   "_abProgress": { "_isEnabled": false }
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { resolveProgress, progressText } from './progressLogic';

const LOG_PREFIX = '[ab-progress]';
const SELECTOR = '[data-ab-progress]';
const INIT_ATTR = 'data-ab-progress-init';
const VARIANTS = ['success', 'danger', 'warning', 'info'];

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abProgress');
  return !config || config._isEnabled !== false;
}

function ensureBar(container) {
  let bar = container.querySelector(':scope > .progress-bar');
  if (!bar) {
    bar = document.createElement('div');
    bar.className = 'progress-bar';
    bar.setAttribute('role', 'progressbar');
    bar.setAttribute('aria-valuemin', '0');
    container.appendChild(bar);
  }
  return bar;
}

/**
 * Apply a resolved spec to a .ab.progress container (building the bar if needed).
 */
function applyProgress(container, p) {
  container.classList.add('cm', 'progress');
  VARIANTS.forEach(v => container.classList.toggle(v, p.variant === v));

  const bar = ensureBar(container);
  bar.classList.toggle('progress-bar-striped', p.striped || p.animated);
  bar.classList.toggle('progress-bar-animated', p.animated);
  bar.style.width = `${p.percent}%`;
  bar.setAttribute('aria-valuenow', String(p.value));
  bar.setAttribute('aria-valuemax', String(p.max));

  const text = progressText(p);
  if (p.label) bar.setAttribute('aria-valuetext', p.label);
  else bar.removeAttribute('aria-valuetext');
  bar.textContent = text;
}

function resolveEl(target) {
  if (!target) return null;
  if (typeof target === 'string') return document.querySelector(target);
  return target.nodeType === 1 ? target : null;
}

// --- declarative: build bars from authored markup ---

function enrich() {
  if (!isEnabled()) return;
  const els = document.querySelectorAll(`${SELECTOR}:not([${INIT_ATTR}])`);
  els.forEach(el => {
    applyProgress(el, resolveProgress(el.dataset));
    el.setAttribute(INIT_ATTR, 'true');
  });
  if (els.length) logging.debug(`${LOG_PREFIX} built ${els.length} bar(s)`);
}

// --- programmatic: update a bar imperatively ---

function onSet(payload = {}) {
  if (!isEnabled()) return;
  const el = resolveEl(payload.target);
  if (!el) { logging.warn(`${LOG_PREFIX} abProgress:set — no target`, payload); return; }

  // merge passed fields onto the element's current data-* then re-resolve
  const ds = { ...el.dataset };
  const map = {
    value: 'abProgressValue', max: 'abProgressMax', label: 'abProgressLabel',
    showLabel: 'abProgressShowLabel', variant: 'abProgressVariant',
    striped: 'abProgressStriped', animated: 'abProgressAnimated'
  };
  Object.keys(map).forEach(k => {
    if (payload[k] !== undefined) {
      ds[map[k]] = String(payload[k]);
      el.setAttribute(`data-${map[k].replace(/[A-Z]/g, c => '-' + c.toLowerCase())}`, String(payload[k]));
    }
  });

  const spec = resolveProgress(ds);
  applyProgress(el, spec);
  el.setAttribute(INIT_ATTR, 'true');
  Adapt.trigger('abProgress:changed', el, spec);
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abProgress._isEnabled`);
    return;
  }
  Adapt.on('abProgress:set', onSet);
  logging.debug(`${LOG_PREFIX} ready`);
}

Adapt.once('adapt:start', setUp);
Adapt.on('pageView:ready menuView:ready', enrich);

logging.debug(`${LOG_PREFIX} extension loaded`);

export default {};
