/**
 * adapt-ab-toast
 *
 * Bootstrap-5-shaped toasts (.ab.toast) — transient notifications stacked in a
 * live region, shown programmatically. Dependency-free.
 *
 * Show one from anywhere:
 *   Adapt.trigger('abToast:show', {
 *     title: 'Saved', body: 'Your answer was recorded.',
 *     variant: 'success', autohide: true, delay: 5000
 *   });
 *   Adapt.trigger('abToast:hideAll');
 *
 * Emits `abToast:shown` (el, spec) and `abToast:hidden` (el). A close button
 * dismisses immediately; autohide dismisses after `delay` ms (default 5000).
 *
 * Accessibility: toasts append to a shared region with aria-live="polite" so
 * they are announced. For urgent messages consider styling/behaviour that the
 * learner can't miss; polite is the safe default for incidental feedback.
 *
 * Enable/disable (course.json), default ENABLED when absent:
 *   "_abToast": { "_isEnabled": false }
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { resolveToast, VARIANTS } from './toastLogic';

const LOG_PREFIX = '[ab-toast]';
const REGION_ID = 'ab-toast-region';

let region = null;

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abToast');
  return !config || config._isEnabled !== false;
}

function prefersReducedMotion() {
  return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

function getRegion() {
  if (region && document.body.contains(region)) return region;
  region = document.createElement('div');
  region.className = 'ab-toast__region';
  region.id = REGION_ID;
  region.setAttribute('role', 'region');
  region.setAttribute('aria-label', 'Notifications');
  region.setAttribute('aria-live', 'polite');
  region.setAttribute('aria-atomic', 'false');
  document.body.appendChild(region);
  return region;
}

function buildToast(spec) {
  const el = document.createElement('div');
  el.className = `ab toast${spec.variant ? ' ' + spec.variant : ''}`;
  if (spec.id) el.setAttribute('data-ab-toast-id', spec.id);

  let html = '';
  if (spec.title || spec.showClose) {
    html += '<div class="toast-header">';
    if (spec.title) html += `<strong class="toast-title">${spec.title}</strong>`;
    if (spec.showClose) html += '<button type="button" class="btn-close ab-toast__close" aria-label="Close"></button>';
    html += '</div>';
  }
  if (spec.body) html += `<div class="toast-body">${spec.body}</div>`;
  el.innerHTML = html;
  return el;
}

function dismiss(el) {
  if (!el || el.getAttribute('data-ab-toast-closing')) return;
  el.setAttribute('data-ab-toast-closing', 'true');
  if (el._abToastTimer) clearTimeout(el._abToastTimer);

  const finish = () => {
    el.removeEventListener('transitionend', finish);
    if (el.parentNode) el.parentNode.removeChild(el);
    Adapt.trigger('abToast:hidden', el);
  };

  if (prefersReducedMotion()) {
    finish();
  } else {
    el.classList.remove('is-visible');
    el.addEventListener('transitionend', finish);
    setTimeout(finish, 400); // safety net
  }
}

function show(spec) {
  if (!isEnabled()) return null;
  const host = getRegion();
  const el = buildToast(spec);
  host.appendChild(el);

  // reflow then reveal
  void el.offsetHeight;
  requestAnimationFrame(() => el.classList.add('is-visible'));

  if (spec.autohide) {
    el._abToastTimer = setTimeout(() => dismiss(el), spec.delay);
  }

  Adapt.trigger('abToast:shown', el, spec);
  logging.debug(`${LOG_PREFIX} shown`, spec.id || '(inline)');
  return el;
}

function onClick(e) {
  const closer = e.target.closest ? e.target.closest('.ab-toast__close') : null;
  if (!closer) return;
  const toast = closer.closest('.ab.toast');
  if (toast) dismiss(toast);
}

function hideAll() {
  if (!region) return;
  Array.prototype.slice.call(region.querySelectorAll('.ab.toast')).forEach(dismiss);
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abToast._isEnabled`);
    return;
  }
  document.addEventListener('click', onClick);
  Adapt.on('abToast:show', opts => show(resolveToast(opts)));
  Adapt.on('abToast:hideAll', hideAll);
  logging.debug(`${LOG_PREFIX} ready (variants: ${VARIANTS.join('/')})`);
}

Adapt.once('adapt:start', setUp);
Adapt.on('router:location', hideAll); // clear stale toasts on navigation

logging.debug(`${LOG_PREFIX} extension loaded`);

export default {};
