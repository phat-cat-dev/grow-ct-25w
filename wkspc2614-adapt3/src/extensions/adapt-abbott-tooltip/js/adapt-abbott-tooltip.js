/**
 * adapt-abbott-tooltip
 *
 * Inline vocabulary tooltips that work on ANY text, in any component. An author
 * marks a term in any text field:
 *
 *   <span class="cm-tooltip" data-cm-tip="A self-contained definition.">term</span>
 *
 * and this extension shows an accessible definition bubble on hover, keyboard
 * focus and tap. Dependency-free — no Popper, Bootstrap JS or jQuery.
 *
 * Behaviour:
 *   - one shared bubble element (role="tooltip") appended to <body>;
 *   - show on mouseenter / focusin; hide on mouseleave / focusout;
 *   - click / tap toggles a "pinned" state (so touch users can open it, and it
 *     stays open to read); Escape or an outside click unpins and hides;
 *   - repositions on scroll / resize while open (flip above/below, clamp to
 *     viewport — see tooltipLogic.computePlacement);
 *   - a11y: triggers are focusable (tabindex=0); while shown the trigger gets
 *     aria-describedby pointing at the bubble.
 *
 * Enable/disable (course.json), default ENABLED when absent:
 *   "_abbottTooltip": { "_isEnabled": false }   // set false to turn off
 *
 * @author Abbott
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { computePlacement } from './tooltipLogic';

const LOG_PREFIX = '[tooltip]';
const BUBBLE_ID = 'cm-tooltip-bubble';
const INIT_ATTR = 'data-cm-tip-init';
const GAP = 8;

let bubble = null;
let currentTrigger = null;
let pinned = false;
let rafId = null;

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abbottTooltip');
  // zero-config: enabled unless explicitly disabled
  return !config || config._isEnabled !== false;
}

function getBubble() {
  if (bubble) return bubble;
  bubble = document.createElement('div');
  bubble.className = 'cm-tooltip-bubble';
  bubble.id = BUBBLE_ID;
  bubble.setAttribute('role', 'tooltip');
  bubble.hidden = true;
  document.body.appendChild(bubble);
  return bubble;
}

function position() {
  if (!currentTrigger || !bubble || bubble.hidden) return;
  const t = currentTrigger.getBoundingClientRect();
  const b = bubble.getBoundingClientRect();
  const { top, left, placement } = computePlacement(
    { top: t.top, left: t.left, width: t.width, height: t.height },
    { width: b.width, height: b.height },
    { width: window.innerWidth, height: window.innerHeight },
    GAP
  );
  bubble.style.top = `${Math.round(top)}px`;
  bubble.style.left = `${Math.round(left)}px`;
  bubble.setAttribute('data-placement', placement);
}

function show(trigger) {
  const text = trigger.getAttribute('data-cm-tip');
  if (!text) return;
  const el = getBubble();
  el.textContent = text;
  el.hidden = false;
  currentTrigger = trigger;
  trigger.setAttribute('aria-describedby', BUBBLE_ID);
  // measure then place (two frames so layout settles before read)
  position();
  requestAnimationFrame(() => {
    el.classList.add('is-visible');
    position();
  });
}

function hide() {
  if (!bubble) return;
  pinned = false;
  bubble.classList.remove('is-visible');
  bubble.hidden = true;
  if (currentTrigger) {
    currentTrigger.removeAttribute('aria-describedby');
    currentTrigger = null;
  }
}

function closestTrigger(node) {
  return node && node.closest ? node.closest('.cm-tooltip[data-cm-tip]') : null;
}

// --- delegated interaction (works for any .cm-tooltip, now or later added) ---

function onPointerOver(e) {
  if (pinned) return;
  const trigger = closestTrigger(e.target);
  if (trigger) show(trigger);
}

function onPointerOut(e) {
  if (pinned) return;
  const trigger = closestTrigger(e.target);
  // ignore moves within the same trigger
  if (trigger && trigger === currentTrigger) hide();
}

function onFocusIn(e) {
  const trigger = closestTrigger(e.target);
  if (trigger) show(trigger);
}

function onFocusOut(e) {
  if (pinned) return;
  const trigger = closestTrigger(e.target);
  if (trigger && trigger === currentTrigger) hide();
}

function onClick(e) {
  const trigger = closestTrigger(e.target);
  if (trigger) {
    e.preventDefault();
    if (currentTrigger === trigger && pinned) {
      hide();
    } else {
      show(trigger);
      pinned = true;
    }
    return;
  }
  // click outside an open pinned tooltip closes it
  if (pinned && !(bubble && bubble.contains(e.target))) hide();
}

function onKeydown(e) {
  if (e.key === 'Escape' && currentTrigger) {
    const t = currentTrigger;
    hide();
    if (t.focus) t.focus();
  } else if ((e.key === 'Enter' || e.key === ' ') && closestTrigger(e.target)) {
    // keyboard activation toggles pin, matching click
    e.preventDefault();
    onClick(e);
  }
}

function onReflow() {
  if (!currentTrigger) return;
  if (rafId) cancelAnimationFrame(rafId);
  rafId = requestAnimationFrame(position);
}

// --- init: make triggers focusable + announce (interaction is delegated) ---

function enrich() {
  if (!isEnabled()) return;
  const triggers = document.querySelectorAll(`.cm-tooltip[data-cm-tip]:not([${INIT_ATTR}])`);
  triggers.forEach(trigger => {
    if (!trigger.hasAttribute('tabindex')) trigger.setAttribute('tabindex', '0');
    trigger.setAttribute(INIT_ATTR, 'true');
  });
  if (triggers.length) {
    logging.debug(`${LOG_PREFIX} enriched ${triggers.length} trigger(s)`);
  }
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abbottTooltip._isEnabled`);
    return;
  }
  document.addEventListener('mouseover', onPointerOver);
  document.addEventListener('mouseout', onPointerOut);
  document.addEventListener('focusin', onFocusIn);
  document.addEventListener('focusout', onFocusOut);
  document.addEventListener('click', onClick);
  document.addEventListener('keydown', onKeydown);
  window.addEventListener('scroll', onReflow, true);
  window.addEventListener('resize', onReflow);
  logging.debug(`${LOG_PREFIX} listeners attached`);
}

// attach once; enrich on every view render and hide any open bubble on navigation
Adapt.once('adapt:start', setUp);
Adapt.on('pageView:ready menuView:ready', enrich);
Adapt.on('router:location', hide);

logging.debug(`${LOG_PREFIX} extension loaded`);
