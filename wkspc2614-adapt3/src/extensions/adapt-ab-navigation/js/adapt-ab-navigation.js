/**
 * adapt-ab-navigation
 *
 * An interface/adapter over the whole core navigation bar (the
 * role="navigation" .nav region and its .nav__inner). It renders no region of
 * its own — it overlays the core-generated bar on every view. Three jobs:
 *
 *  1. STYLE SEAM — stamps a stable `.ab.navigation` compound hook on the .nav
 *     element so our LESS (ab-navigation.less, on --ab-base-navigation-* tokens)
 *     can restyle the bar + layout in one place.
 *
 *  2. DATA LAYER — emits `abNavigation:ready` with the bar's button inventory
 *     (each button's data-event / name / label / order) and mirrors the
 *     responsive label mode onto data-ab-nav-labels, so other code can read the
 *     nav without poking core.
 *
 *  3. ADD LAYERS — injects author-configured custom nav items into .nav__inner,
 *     ordered by data-order. An item can trigger a core data-event, open an
 *     adapt-ab-modal (data-ab-modal), or be a link (url). This is the "add more
 *     layers within the nav" capability.
 *
 * Pairs with adapt-ab-navbtn (per-button hook + click events). Dependency-free;
 * no core source required. Enable/disable (course.json), default ENABLED:
 *   "_abNavigation": { "_isEnabled": false }
 * Custom items:
 *   "_abNavigation": { "_items": [
 *     { "label": "Glossary", "_icon": "icon-search", "_order": 95, "_abModal": "glossary" }
 *   ]}
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { normaliseItems, insertionIndex } from './navigationLogic';

const LOG_PREFIX = '[ab-navigation]';
const INIT_ATTR = 'data-ab-navigation-init';
const ITEM_CLASS = 'ab-navitem';
const LABEL_MODES = ['hide-label', 'show-label', 'show-label-small', 'show-label-medium', 'show-label-large', 'has-label-auto'];

function config() {
  const course = Adapt.course;
  return (course && course.get('_abNavigation')) || null;
}

function isEnabled() {
  const c = config();
  return !c || c._isEnabled !== false;
}

function buildItem(item) {
  const isLink = !!item.url;
  const el = document.createElement(isLink ? 'a' : 'button');
  if (isLink) el.setAttribute('href', item.url);
  else el.setAttribute('type', 'button');
  el.className = `btn-icon nav__btn ${ITEM_CLASS}${item.classes ? ' ' + item.classes : ''}`;
  el.setAttribute('data-order', String(item.order));
  if (item.event) el.setAttribute('data-event', item.event);
  if (item.abModal) el.setAttribute('data-ab-modal', item.abModal);
  if (item.label) el.setAttribute('aria-label', item.label);

  if (item.icon) {
    const icon = document.createElement('span');
    icon.className = `icon ${item.icon}`;
    icon.setAttribute('aria-hidden', 'true');
    el.appendChild(icon);
  }
  if (item.label) {
    const label = document.createElement('span');
    label.className = 'nav__btn-label';
    label.setAttribute('aria-hidden', 'true');
    label.textContent = item.label;
    el.appendChild(label);
  }
  return el;
}

function injectItems(navInner) {
  const items = normaliseItems((config() || {})._items);
  if (!items.length) return;
  items.forEach(item => {
    const existing = Array.prototype.slice.call(navInner.querySelectorAll(':scope > [data-order]'));
    const orders = existing.map(el => Number(el.getAttribute('data-order')) || 0);
    const at = insertionIndex(orders, item.order);
    const node = buildItem(item);
    if (at >= existing.length) navInner.appendChild(node);
    else navInner.insertBefore(node, existing[at]);
  });
  logging.debug(`${LOG_PREFIX} injected ${items.length} custom item(s)`);
}

function inventory(nav) {
  return Array.prototype.slice.call(nav.querySelectorAll('.nav__btn')).map(btn => {
    const labelEl = btn.querySelector('.nav__btn-label');
    return {
      event: btn.getAttribute('data-event') || null,
      name: btn.getAttribute('name') || null,
      label: (labelEl && labelEl.textContent.trim()) || btn.getAttribute('aria-label') || '',
      order: Number(btn.getAttribute('data-order')) || 0
    };
  });
}

function enrich() {
  if (!isEnabled()) return;
  const nav = document.querySelector('[role="navigation"].nav, .nav[role="navigation"], .nav');
  if (!nav) return;

  // (re)apply on each render; re-inject if a fresh nav lacks our items
  nav.classList.add('ab', 'navigation');

  const mode = LABEL_MODES.filter(m => nav.classList.contains(m)).join(' ');
  nav.setAttribute('data-ab-nav-labels', mode);

  const navInner = nav.querySelector('.nav__inner') || nav;
  if (!navInner.querySelector(`.${ITEM_CLASS}`)) injectItems(navInner);

  if (!nav.getAttribute(INIT_ATTR)) {
    nav.setAttribute(INIT_ATTR, 'true');
  }
  Adapt.trigger('abNavigation:ready', nav, { buttons: inventory(nav), labelMode: mode });
}

function setUp() {
  if (!isEnabled()) {
    logging.debug(`${LOG_PREFIX} disabled via _abNavigation._isEnabled`);
    return;
  }
  enrich();
  logging.debug(`${LOG_PREFIX} ready`);
}

Adapt.once('adapt:start', setUp);
Adapt.on('pageView:ready menuView:ready', enrich);

logging.debug(`${LOG_PREFIX} extension loaded`);

export default {};
