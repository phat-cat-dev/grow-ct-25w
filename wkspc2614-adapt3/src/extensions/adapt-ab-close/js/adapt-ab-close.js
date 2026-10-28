/**
 * adapt-ab-close
 *
 * A Bootstrap-5 close button (.btn-close) plus a generic "dismiss" behaviour,
 * usable ANYWHERE. Dependency-free — no Bootstrap JS/jQuery.
 *
 * Put a close button inside anything dismissible:
 *
 *   <div class="ab alert" data-ab-dismissible>
 *     <button type="button" class="btn-close" data-ab-dismiss aria-label="Close"></button>
 *     <p>A dismissible notice.</p>
 *   </div>
 *
 * Clicking it dismisses the nearest ancestor marked `data-ab-dismissible`
 * (or `.ab.alert` / `.ab.card`). Target a specific element by selector instead:
 *
 *   <button type="button" class="btn-close" data-ab-dismiss="#notice-1" aria-label="Close"></button>
 *
 * Options (data-* on the button):
 *   data-ab-dismiss="<selector>"   target a specific element (default: nearest dismissible)
 *   data-ab-dismiss-remove="false" hide instead of removing from the DOM
 *   data-ab-dismiss-fade="0"       disable the fade-out
 *
 * Emits: Adapt.trigger('abClose:dismissed', targetEl).
 *
 * Enable/disable (course.json), default ENABLED when absent:
 *   "_abClose": { "_isEnabled": false }
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { resolveDismiss } from './closeLogic';

const LOG_PREFIX = '[ab-close]';
const BTN_SELECTOR = '[data-ab-dismiss]';
const DISMISSIBLE_SELECTOR = '[data-ab-dismissible], .ab.alert, .ab.card';
const INIT_ATTR = 'data-ab-dismiss-init';

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abClose');
  return !config || config._isEnabled !== false;
}

function prefersReducedMotion() {
  return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

function findTarget(button, selector) {
  if (selector) {
    return button.closest(selector) || document.querySelector(selector);
  }
  return button.closest(DISMISSIBLE_SELECTOR);
}

/**
 * Move focus somewhere sensible before the target leaves the DOM: the element
 * after it, else before it, else its parent.
 */
function moveFocusAway(target) {
  const next = target.nextElementSibling;
  const prev = target.previousElementSibling;
  const dest = next || prev || target.parentElement;
  if (dest && dest.focus) {
    if (!dest.hasAttribute('tabindex')) dest.setAttribute('tabindex', '-1');
    dest.focus();
  }
}

function finalize(target, remove) {
  if (remove) {
    target.remove();
  } else {
    target.hidden = true;
  }
  Adapt.trigger('abClose:dismissed', target);
  logging.debug(`${LOG_PREFIX} dismissed`, target);
}

function dismiss(target, opts) {
  if (!target) return;
  moveFocusAway(target);

  if (opts.fadeMs > 0 && !prefersReducedMotion()) {
    target.style.transition = `opacity ${opts.fadeMs}ms ease`;
    target.classList.add('is-dismissing');
    // force a reflow so the transition runs, then start it
    void target.offsetHeight;
    target.style.opacity = '0';

    let done = false;
    const end = () => {
      if (done) return;
      done = true;
      target.removeEventListener('transitionend', end);
      finalize(target, opts.remove);
    };
    target.addEventListener('transitionend', end);
    setTimeout(end, opts.fadeMs + 50); // safety net if transitionend never fires
  } else {
    finalize(target, opts.remove);
  }
}

function onClick(e) {
  const button = e.target.closest ? e.target.closest(BTN_SELECTOR) : null;
  if (!button) return;
  if (!isEnabled()) return;
  e.preventDefault();
  const opts = resolveDismiss(button.dataset);
  const target = findTarget(button, opts.selector);
  if (target) dismiss(target, opts);
  else logging.warn(`${LOG_PREFIX} no dismiss target for`, button);
}

function onKeyActivate(e) {
  if (e.key !== 'Enter' && e.key !== ' ') return;
  const button = e.target.closest ? e.target.closest(BTN_SELECTOR) : null;
  if (!button || button.tagName === 'BUTTON') return; // native buttons handle this
  e.preventDefault();
  onClick(e);
}

function enrich() {
  if (!isEnabled()) return;
  const buttons = document.querySelectorAll(`${BTN_SELECTOR}:not([${INIT_ATTR}])`);
  buttons.forEach(button => {
    if (button.tagName !== 'BUTTON' && button.getAttribute('role') !== 'button') {
      button.setAttribute('role', 'button');
      if (!button.hasAttribute('tabindex')) button.setAttribute('tabindex', '0');
    }
    if (!button.getAttribute('aria-label') && !button.textContent.trim()) {
      button.setAttribute('aria-label', 'Close');
    }
    button.setAttribute(INIT_ATTR, 'true');
  });
  if (buttons.length) logging.debug(`${LOG_PREFIX} enriched ${buttons.length} button(s)`);
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abClose._isEnabled`);
    return;
  }
  document.addEventListener('click', onClick);
  document.addEventListener('keydown', onKeyActivate);
  logging.debug(`${LOG_PREFIX} listeners attached`);
}

Adapt.once('adapt:start', setUp);
Adapt.on('pageView:ready menuView:ready', enrich);

logging.debug(`${LOG_PREFIX} extension loaded`);

export default {};
