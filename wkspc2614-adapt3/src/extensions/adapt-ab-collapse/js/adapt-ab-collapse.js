/**
 * adapt-ab-collapse
 *
 * A Bootstrap-5 collapse (show/hide with height animation) as an extension,
 * usable anywhere. Dependency-free — no Bootstrap JS/jQuery.
 *
 * A trigger targets a collapsible element by selector:
 *
 *   <button type="button" class="ab btn" data-ab-collapse="#more">Show more</button>
 *   <div class="ab collapse" id="more"> … hidden until toggled … </div>
 *
 * Start open by adding `show`: <div class="ab collapse show" id="more">.
 * Accordion-style (one open at a time) with a parent selector:
 *
 *   <button data-ab-collapse="#p1" data-ab-collapse-parent="#faq">…</button>
 *
 * Accessibility: triggers get aria-expanded + aria-controls (auto-added),
 * kept in sync on toggle; the height animation respects prefers-reduced-motion.
 * Emits `abCollapse:shown` / `abCollapse:hidden` (targetEl).
 *
 * Enable/disable (course.json), default ENABLED when absent:
 *   "_abCollapse": { "_isEnabled": false }
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { resolveCollapse, ariaExpanded } from './collapseLogic';

const LOG_PREFIX = '[ab-collapse]';
const TRIGGER = '[data-ab-collapse]';
const INIT_ATTR = 'data-ab-collapse-init';
const DURATION = 250;

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abCollapse');
  return !config || config._isEnabled !== false;
}

function prefersReducedMotion() {
  return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

function targetsFor(trigger) {
  const { selector } = resolveCollapse(trigger.dataset);
  if (!selector) return [];
  try { return Array.prototype.slice.call(document.querySelectorAll(selector)); }
  catch (e) { return []; }
}

function triggersFor(target) {
  const id = target.id;
  if (!id) return [];
  return Array.prototype.slice.call(document.querySelectorAll(TRIGGER)).filter(t => {
    const { selector } = resolveCollapse(t.dataset);
    if (!selector) return false;
    try { return Array.prototype.slice.call(document.querySelectorAll(selector)).indexOf(target) !== -1; }
    catch (e) { return false; }
  });
}

function syncTriggers(target, isOpen) {
  triggersFor(target).forEach(t => t.setAttribute('aria-expanded', ariaExpanded(isOpen)));
}

function expand(target) {
  if (target.classList.contains('show') || target.classList.contains('collapsing')) return;
  if (prefersReducedMotion()) {
    target.classList.add('show');
    finishOpen(target);
    return;
  }
  target.classList.add('collapsing');
  target.style.height = '0px';
  void target.offsetHeight;
  target.style.height = `${target.scrollHeight}px`;
  onEnd(target, () => {
    target.classList.remove('collapsing');
    target.classList.add('show');
    target.style.height = '';
    finishOpen(target);
  });
}

function collapse(target) {
  if (!target.classList.contains('show') || target.classList.contains('collapsing')) return;
  if (prefersReducedMotion()) {
    target.classList.remove('show');
    finishClose(target);
    return;
  }
  target.style.height = `${target.scrollHeight}px`;
  void target.offsetHeight;
  target.classList.add('collapsing');
  target.classList.remove('show');
  target.style.height = '0px';
  onEnd(target, () => {
    target.classList.remove('collapsing');
    target.style.height = '';
    finishClose(target);
  });
}

function finishOpen(target) { syncTriggers(target, true); Adapt.trigger('abCollapse:shown', target); }
function finishClose(target) { syncTriggers(target, false); Adapt.trigger('abCollapse:hidden', target); }

function onEnd(el, cb) {
  let done = false;
  const handler = () => { if (done) return; done = true; el.removeEventListener('transitionend', handler); cb(); };
  el.addEventListener('transitionend', handler);
  setTimeout(handler, DURATION + 50);
}

function toggle(trigger) {
  const { parent } = resolveCollapse(trigger.dataset);
  const targets = targetsFor(trigger);
  targets.forEach(target => {
    const willOpen = !target.classList.contains('show');
    // accordion-style: close other open collapses in the parent first
    if (willOpen && parent) {
      const scope = trigger.closest(parent) || document.querySelector(parent);
      if (scope) {
        scope.querySelectorAll('.ab.collapse.show').forEach(other => {
          if (other !== target) collapse(other);
        });
      }
    }
    willOpen ? expand(target) : collapse(target);
  });
}

function onClick(e) {
  if (!isEnabled()) return;
  const trigger = e.target.closest ? e.target.closest(TRIGGER) : null;
  if (!trigger) return;
  e.preventDefault();
  toggle(trigger);
}

function onKeyActivate(e) {
  if (e.key !== 'Enter' && e.key !== ' ') return;
  const trigger = e.target.closest ? e.target.closest(TRIGGER) : null;
  if (!trigger || trigger.tagName === 'BUTTON') return; // native buttons handle this
  e.preventDefault();
  toggle(trigger);
}

function enrich() {
  if (!isEnabled()) return;
  const triggers = document.querySelectorAll(`${TRIGGER}:not([${INIT_ATTR}])`);
  triggers.forEach(trigger => {
    if (trigger.tagName !== 'BUTTON' && trigger.getAttribute('role') !== 'button') {
      trigger.setAttribute('role', 'button');
      if (!trigger.hasAttribute('tabindex')) trigger.setAttribute('tabindex', '0');
    }
    const targets = targetsFor(trigger);
    const ids = targets.map(t => t.id).filter(Boolean).join(' ');
    if (ids && !trigger.getAttribute('aria-controls')) trigger.setAttribute('aria-controls', ids);
    const anyOpen = targets.some(t => t.classList.contains('show'));
    trigger.setAttribute('aria-expanded', ariaExpanded(anyOpen));
    trigger.setAttribute(INIT_ATTR, 'true');
  });
  if (triggers.length) logging.debug(`${LOG_PREFIX} wired ${triggers.length} trigger(s)`);
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abCollapse._isEnabled`);
    return;
  }
  document.addEventListener('click', onClick);
  document.addEventListener('keydown', onKeyActivate);
  enrich();
  logging.debug(`${LOG_PREFIX} ready`);
}

Adapt.once('adapt:start', setUp);
Adapt.on('pageView:ready menuView:ready', enrich);

logging.debug(`${LOG_PREFIX} extension loaded`);

export default {};
