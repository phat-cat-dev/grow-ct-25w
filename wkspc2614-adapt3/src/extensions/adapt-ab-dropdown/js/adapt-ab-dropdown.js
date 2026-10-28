/**
 * adapt-ab-dropdown
 *
 * An interface/adapter over the Adapt matching-component dropdown
 * (adapt-contrib-matching's matchingDropDown: the .dropdown root with
 * .dropdown__btn / .dropdown__list / .dropdown-item). Vanilla ships it with a
 * hard-coded palette; this adapter re-themes it from --ab-* tokens and exposes a
 * selection data layer. It renders no widget of its own.
 *
 *  1. STYLE SEAM — stamps a stable `.ab-dropdown` hook on each `.dropdown` so
 *     our LESS (ab-dropdown.less, on --ab-base-dropdown-* tokens) restyles the
 *     trigger / list / items in one place, without patching vendor.
 *
 *  2. DATA LAYER — observes item selection (a click on a `.dropdown-item`) and
 *     emits `abDropdown:change` (el, { text, value }). Observe-only — it never
 *     preventDefaults, so the matching component's own open/close/select logic
 *     still runs.
 *
 * Dependency-free; no core source required. Enable/disable (course.json),
 * default ENABLED when absent:  "_abDropdown": { "_isEnabled": false }
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';

const LOG_PREFIX = '[ab-dropdown]';
const HOOK = 'ab-dropdown';
const INIT_ATTR = 'data-ab-dropdown-init';

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abDropdown');
  return !config || config._isEnabled !== false;
}

function enrich() {
  if (!isEnabled()) return;
  // only Adapt dropdown widgets (a .dropdown that carries a .dropdown__btn),
  // never unrelated elements that happen to use the class
  const widgets = document.querySelectorAll(`.dropdown:not([${INIT_ATTR}])`);
  let count = 0;
  widgets.forEach(el => {
    if (!el.querySelector('.dropdown__btn')) return;
    el.classList.add(HOOK);
    el.setAttribute(INIT_ATTR, 'true');
    count++;
  });
  if (count) logging.debug(`${LOG_PREFIX} hooked ${count} dropdown(s)`);
}

function onClick(e) {
  if (!isEnabled()) return;
  const item = e.target.closest ? e.target.closest(`.${HOOK} .dropdown-item`) : null;
  if (!item) return;
  const root = item.closest(`.${HOOK}`);
  const inner = item.querySelector('.dropdown-item__inner') || item;
  Adapt.trigger('abDropdown:change', root, {
    text: (inner.textContent || '').trim(),
    value: item.getAttribute('data-value') || item.getAttribute('value') || null
  });
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abDropdown._isEnabled`);
    return;
  }
  // observe only — never preventDefault, so matching's own handling runs
  document.addEventListener('click', onClick);
  enrich();
  logging.debug(`${LOG_PREFIX} ready`);
}

Adapt.once('adapt:start', setUp);
Adapt.on('pageView:ready', enrich);

logging.debug(`${LOG_PREFIX} extension loaded`);

export default {};
