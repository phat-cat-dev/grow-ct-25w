/**
 * adapt-ab-modal
 *
 * A single, globally-triggerable Bootstrap-5-shaped modal (.ab.modal), usable
 * ANYWHERE. Dependency-free — no Bootstrap JS, Popper or jQuery.
 *
 * Trigger from any element, in any text field, by adding a data attribute:
 *
 *   <button type="button" data-ab-modal="refs">References</button>
 *
 * where "refs" is the _id of a modal configured in course.json:
 *
 *   "_abModal": {
 *     "_isEnabled": true,
 *     "_modals": [
 *       { "_id": "refs", "title": "References", "body": "<p>…</p>", "_size": "lg" }
 *     ]
 *   }
 *
 * Or build an ad-hoc modal inline, with no config:
 *
 *   <button type="button"
 *     data-ab-modal
 *     data-ab-modal-title="Quick note"
 *     data-ab-modal-body="&lt;p&gt;Any HTML.&lt;/p&gt;">More</button>
 *
 * Programmatic API (for other components/extensions):
 *   Adapt.trigger('abModal:open', '<id>');            // open a configured modal
 *   Adapt.trigger('abModal:open', { title, body });   // open an ad-hoc modal
 *   Adapt.trigger('abModal:close');
 *
 * Accessibility: role="dialog" aria-modal, labelled by the title; focus moves
 * into the dialog on open and is trapped; Escape and backdrop-click close
 * (unless _isStatic); focus returns to the trigger on close; background scroll
 * is locked while open.
 *
 * Enable/disable (course.json), default ENABLED when absent:
 *   "_abModal": { "_isEnabled": false }
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { resolveModal, trapWrapIndex } from './modalLogic';

const LOG_PREFIX = '[ab-modal]';
const ROOT_ID = 'ab-modal-root';
const TITLE_ID = 'ab-modal-title';
const BODY_ID = 'ab-modal-body';
const TRIGGER_SELECTOR = '[data-ab-modal]';
const INIT_ATTR = 'data-ab-modal-init';
const FOCUSABLE = [
  'a[href]', 'button:not([disabled])', 'textarea:not([disabled])',
  'input:not([disabled])', 'select:not([disabled])', '[tabindex]:not([tabindex="-1"])'
].join(',');

let root = null;
let dialog = null;
let titleEl = null;
let bodyEl = null;
let isOpen = false;
let isStatic = false;
let lastTrigger = null;

function isEnabled() {
  const course = Adapt.course;
  if (!course) return true; // default on
  const config = course.get('_abModal');
  return !config || config._isEnabled !== false;
}

function getModals() {
  const config = Adapt.course && Adapt.course.get('_abModal');
  return (config && config._modals) || [];
}

// --- single shared host, built once, appended to <body> ---

function getRoot() {
  if (root) return root;
  root = document.createElement('div');
  root.className = 'ab-modal__root';
  root.id = ROOT_ID;
  root.hidden = true;
  root.innerHTML = `
    <div class="ab-modal__backdrop" data-ab-modal-dismiss></div>
    <div class="ab modal" role="dialog" aria-modal="true" aria-labelledby="${TITLE_ID}">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h2 class="modal-title" id="${TITLE_ID}"></h2>
            <button type="button" class="btn-close ab-modal__close" data-ab-modal-dismiss aria-label="Close"></button>
          </div>
          <div class="modal-body" id="${BODY_ID}"></div>
        </div>
      </div>
    </div>`;
  document.body.appendChild(root);
  dialog = root.querySelector('.ab.modal');
  titleEl = root.querySelector(`#${TITLE_ID}`);
  bodyEl = root.querySelector(`#${BODY_ID}`);
  return root;
}

function getFocusable() {
  if (!dialog) return [];
  return Array.from(dialog.querySelectorAll(FOCUSABLE))
    .filter(el => el.offsetParent !== null || el === document.activeElement);
}

// --- open / close ---

function open(content, trigger) {
  if (!content) return;
  getRoot();

  // reset dialog size/variant classes, then apply requested ones
  const dialogBox = dialog.querySelector('.modal-dialog');
  dialogBox.className = 'modal-dialog';
  if (content.size) dialogBox.classList.add(content.size);
  if (content.isCentered) dialogBox.classList.add('modal-dialog-centered');
  if (content.isScrollable) dialogBox.classList.add('modal-dialog-scrollable');

  titleEl.innerHTML = content.title || '';
  bodyEl.innerHTML = content.body || '';
  if (content.body) {
    dialog.setAttribute('aria-describedby', BODY_ID);
  } else {
    dialog.removeAttribute('aria-describedby');
  }

  isStatic = !!content.isStatic;
  lastTrigger = trigger || document.activeElement;

  root.hidden = false;
  document.body.classList.add('ab-modal-is-open');
  isOpen = true;

  // move focus into the dialog (close button is always present)
  const closeBtn = root.querySelector('.ab-modal__close');
  if (closeBtn && closeBtn.focus) closeBtn.focus();

  Adapt.trigger('abModal:opened', content.id || null);
  logging.debug(`${LOG_PREFIX} opened`, content.id || '(inline)');
}

function close() {
  if (!isOpen) return;
  root.hidden = true;
  document.body.classList.remove('ab-modal-is-open');
  isOpen = false;
  isStatic = false;
  const t = lastTrigger;
  lastTrigger = null;
  if (t && t.focus) t.focus();
  Adapt.trigger('abModal:closed');
  logging.debug(`${LOG_PREFIX} closed`);
}

// --- delegated interaction (works for any trigger, now or added later) ---

function closestTrigger(node) {
  return node && node.closest ? node.closest(TRIGGER_SELECTOR) : null;
}

function onClick(e) {
  // a dismiss control (close button or backdrop)
  if (isOpen && e.target.closest && e.target.closest('[data-ab-modal-dismiss]')) {
    if (!isStatic) close();
    return;
  }
  // a trigger anywhere on the page
  const trigger = closestTrigger(e.target);
  if (!trigger) return;
  if (!isEnabled()) return;
  e.preventDefault();
  const content = resolveModal(trigger.dataset, getModals());
  if (content) open(content, trigger);
  else logging.warn(`${LOG_PREFIX} trigger has no resolvable content`, trigger);
}

function onKeydown(e) {
  if (!isOpen) return;
  if (e.key === 'Escape') {
    if (!isStatic) { e.preventDefault(); close(); }
    return;
  }
  if (e.key === 'Tab') {
    const focusable = getFocusable();
    const activeIndex = focusable.indexOf(document.activeElement);
    const wrapTo = trapWrapIndex(activeIndex, focusable.length, e.shiftKey);
    if (wrapTo !== -1) {
      e.preventDefault();
      focusable[wrapTo].focus();
    }
  }
}

// --- init: make non-button triggers keyboard-operable (interaction delegated) ---

function enrich() {
  if (!isEnabled()) return;
  const triggers = document.querySelectorAll(`${TRIGGER_SELECTOR}:not([${INIT_ATTR}])`);
  triggers.forEach(trigger => {
    const isButton = trigger.tagName === 'BUTTON' || trigger.getAttribute('role') === 'button';
    if (!isButton) {
      trigger.setAttribute('role', 'button');
      if (!trigger.hasAttribute('tabindex')) trigger.setAttribute('tabindex', '0');
    }
    trigger.setAttribute(INIT_ATTR, 'true');
  });
  if (triggers.length) logging.debug(`${LOG_PREFIX} enriched ${triggers.length} trigger(s)`);
}

function onTriggerKeyActivate(e) {
  if (e.key !== 'Enter' && e.key !== ' ') return;
  const trigger = closestTrigger(e.target);
  if (!trigger || trigger.tagName === 'BUTTON') return; // native buttons handle this
  e.preventDefault();
  onClick(e);
}

// --- programmatic API ---

function onApiOpen(idOrContent) {
  if (!isEnabled()) return;
  let content = null;
  if (typeof idOrContent === 'string') {
    content = resolveModal({ abModal: idOrContent }, getModals());
  } else if (idOrContent && typeof idOrContent === 'object') {
    content = {
      id: idOrContent.id || null,
      title: idOrContent.title || '',
      body: idOrContent.body || '',
      size: idOrContent.size || '',
      isStatic: !!idOrContent.isStatic,
      isCentered: !!idOrContent.isCentered,
      isScrollable: !!idOrContent.isScrollable
    };
    if (!content.title && !content.body) content = null;
  }
  if (content) open(content, document.activeElement);
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abModal._isEnabled`);
    return;
  }
  document.addEventListener('click', onClick);
  document.addEventListener('keydown', onKeydown);
  document.addEventListener('keydown', onTriggerKeyActivate);
  Adapt.on('abModal:open', onApiOpen);
  Adapt.on('abModal:close', close);
  logging.debug(`${LOG_PREFIX} listeners attached`);
}

// attach once; enrich on every view render; close on navigation
Adapt.once('adapt:start', setUp);
Adapt.on('pageView:ready menuView:ready', enrich);
Adapt.on('router:location', close);

logging.debug(`${LOG_PREFIX} extension loaded`);

export default {};
