/**
 * adapt-ab-flipbutton
 *
 * An auto-width, two-face toggle button as an extension, usable from any text
 * field. Dependency-free — no Bootstrap JS/jQuery.
 *
 * Markup: a button with two decorative face spans occupying the same grid
 * cell, so both face sizes count toward the button's own size (auto-width,
 * no JS measurement):
 *
 *   <button type="button" class="ab btn flipbutton" data-ab-flipbutton
 *     aria-pressed="false" aria-label="Toggle example">
 *     <span class="flipbutton__face flipbutton__face--front" aria-hidden="true">Explore</span>
 *     <span class="flipbutton__face flipbutton__face--back" aria-hidden="true">See what is possible</span>
 *   </button>
 *
 * `btn` is the shared .ab.btn object (colour/padding/states); flipbutton
 * supplies the grid-stack mechanics and centres each face within the cell.
 *
 * Hover/focus previews the back face without committing; click/Enter/Space
 * toggles the pressed state (aria-pressed, data-flipped), which persists
 * independently of hover/focus. Give the button a stable, meaningful
 * aria-label for the action — the face spans are decorative and aria-hidden,
 * so changing the visible face never alters the accessible name.
 *
 * Accessibility: non-button triggers are made keyboard-operable
 * (role="button", tabindex="0", Enter/Space); aria-pressed is kept in sync.
 * The face swap respects prefers-reduced-motion (instant, no transition).
 *
 * Emits `abFlipbutton:changed` (triggerEl, isFlipped).
 *
 * Enable/disable (course.json), default ENABLED when absent:
 *   "_abFlipbutton": { "_isEnabled": false }
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { nextFlipped, ariaPressed } from './flipbuttonLogic';

const LOG_PREFIX = '[ab-flipbutton]';
const TRIGGER = '[data-ab-flipbutton]';
const INIT_ATTR = 'data-ab-flipbutton-init';

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abFlipbutton');
  return !config || config._isEnabled !== false;
}

function toggle(trigger) {
  const isFlipped = nextFlipped(trigger.dataset.flipped === 'true');
  trigger.dataset.flipped = String(isFlipped);
  trigger.setAttribute('aria-pressed', ariaPressed(isFlipped));
  Adapt.trigger('abFlipbutton:changed', trigger, isFlipped);
}

function onClick(e) {
  if (!isEnabled()) return;
  const trigger = e.target.closest ? e.target.closest(TRIGGER) : null;
  if (!trigger || trigger.disabled) return;
  e.preventDefault();
  toggle(trigger);
}

function onKeyActivate(e) {
  if (e.key !== 'Enter' && e.key !== ' ') return;
  const trigger = e.target.closest ? e.target.closest(TRIGGER) : null;
  if (!trigger || trigger.disabled || trigger.tagName === 'BUTTON') return; // native buttons handle this
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
    if (!trigger.hasAttribute('aria-pressed')) {
      trigger.setAttribute('aria-pressed', ariaPressed(trigger.dataset.flipped === 'true'));
    }
    trigger.setAttribute(INIT_ATTR, 'true');
  });
  if (triggers.length) logging.debug(`${LOG_PREFIX} wired ${triggers.length} trigger(s)`);
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abFlipbutton._isEnabled`);
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
