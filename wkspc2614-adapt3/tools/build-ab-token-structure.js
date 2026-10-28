#!/usr/bin/env node
/**
 * build-ab-token-structure.js
 *
 * Structure-first lens over the same 2083 token rows as ab-token-values.less.
 * Same values, same comments, same rows - pure permutation into a different
 * taxonomy modelled on the CM Global CSS concatenation convention: utilities
 * first (sub-ordered by function), then objects following Adapt's real
 * rendered page hierarchy top-to-bottom (sub-ordered by BEM sub-element),
 * then components with natives before "ours".
 *
 * Ground truth (established by read-only exploration, see plan
 * "snappy-launching-scroll"):
 *   - Exactly ONE drawer: `dialog.drawer` is a core singleton
 *     (src/core/js/drawer.js). pageLevelProgress/resources/languagePicker
 *     render INTO it via drawer.openCustomView() - they are components that
 *     happen to be drawer-hosted, not separate drawers. Their own LESS never
 *     nests under `.drawer`, so their rows live in the component tier with a
 *     note, not in object-drawer.
 *   - No page footer exists in core or vanilla theme. Footer only exists as
 *     a card/modal sub-element in local adapt-ab-* plugins, which this file
 *     (compiled from core+vanilla only) never touches.
 *   - This file carries no "ours" (adapt-ab-* / adapt-abbott-* / cm-*) rows
 *     at all, so the "ours" component section is emitted empty, with an
 *     explanatory header.
 *   - ~250 rows are LESS mixin *definitions* (trailing `()`), not real DOM
 *     selectors - they only resolve where invoked elsewhere. Object-specific
 *     mixins (e.g. .page-title()) travel with their object; generic ones
 *     (e.g. .bg-color-mixin()) live in utilities (decided with the user).
 *   - .shadow is a real DOM overlay element, not a box-shadow utility.
 *   - .mejs-container (legacy markup) and .mejs__container (BEM markup) are
 *     the same media player and merge into one component-media section.
 *
 * Classification approach: every row's outermost selector (chain[0]) is run
 * through the same componentOf() leading-identifier heuristic used by
 * build-ab-token-values.js, collapsing e.g. .btn-color-outline-focus and
 * .btn-color-disabled onto "btn". Each resulting bucket is then assigned to
 * exactly one section via the curated CLASSIFY table below - a handful of
 * buckets split across sections by exact selector string where the mechanical
 * bucket is not fine-grained enough (e.g. "item" bucket: .item-title() is
 * typography, every other .item-*color*() is colour). Any row that still
 * fails to classify is FATAL: this keeps the table honest rather than
 * letting rows silently fall into a catch-all.
 *
 * Reads (never writes, via tools/lib/ab-token-source.js): the same three
 * source LESS files as build-ab-token-values.js.
 *
 * Writes:
 *   ab-token-structure.less (new file; ab-token-values.less is untouched)
 *
 * Usage: node tools/build-ab-token-structure.js
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { DIR, GROUP_ORDER, LAYER_WORD, groupOf, loadTokenSource } = require('./lib/ab-token-source');

const OUT = path.join(DIR, 'ab-token-structure.less');

// Same leading-identifier heuristic as build-ab-token-values.js's
// componentOf(), reused here as the first classification step.
function componentOf(chain0) {
  const sel = chain0.trim();
  if (sel.startsWith('@media')) return 'media-queries';
  if (sel.startsWith('@font-face')) return 'font-face';
  if (sel.startsWith('@keyframes')) return 'keyframes';
  if (sel.startsWith(':root')) return 'root-vars';
  if (sel.startsWith('.') || sel.startsWith('#')) {
    const m = sel.slice(1).match(/^[a-zA-Z0-9]+/);
    if (m) return m[0].toLowerCase();
  }
  return 'base-elements';
}

// ---------------------------------------------------------------------------
// Section order (document order of the output file)
// ---------------------------------------------------------------------------
const UTILITY_SECTIONS = [
  'utility-variables', 'utility-colours', 'utility-typography', 'utility-layout',
  'utility-display', 'utility-animations', 'utility-icons', 'utility-a11y', 'utility-test',
];
const OBJECT_SECTIONS = [
  'object-document', 'object-element-reset', 'object-nav', 'object-drawer',
  'object-shadow', 'object-notify', 'object-tooltip', 'object-loading',
  'object-shared-structure', 'object-menu', 'object-page', 'object-article',
  'object-block', 'object-component', 'object-buttons',
];
const COMPONENT_SECTIONS = [
  // native components, alphabetical
  'component-accordion', 'component-assessmentresults', 'component-confidenceslider',
  'component-gmcq', 'component-hotgraphic', 'component-matching', 'component-mcq',
  'component-media', 'component-narrative', 'component-slider', 'component-textinput',
  // native extensions, alphabetical (glossary/languagepicker/pagelevelprogress/
  // resources are drawer-hosted - see header note on object-drawer)
  'component-glossary', 'component-languagepicker', 'component-pagelevelprogress',
  'component-resources', 'component-trickle', 'component-tutor',
  // theme project layer, then ours (present, empty)
  'component-theme-project-layer', 'component-ours',
];
const SECTION_ORDER = [...UTILITY_SECTIONS, ...OBJECT_SECTIONS, ...COMPONENT_SECTIONS];

const SECTION_HEADER = {
  'utility-variables': 'UTILITY - VARIABLES - :root custom properties (--adapt-cubic-bezier-*, --adapt-tooltip-*, viewport/nav height)',
  'utility-colours': 'UTILITY - COLOURS - generic colour mixins: .bg-color-mixin(), .header-color-mixin(), .item-color*(), .item-ui-color*(), .ui-btn-ctrl()',
  'utility-typography': 'UTILITY - TYPOGRAPHY - .quote-body(), .quote-attribution(), .pull-quote-body(), .link-text(), .button-text(), .instruction-text(), .priority-label(), .item-title(), .text-align-mixin(), .font-smoothing(), .is-bold, .is-italic',
  'utility-layout': 'UTILITY - LAYOUT - .l-*(), .make-columns(), .make-margin-start/end(), .u-float-*(), .u-clearfix*, .u-no-select',
  'utility-display': 'UTILITY - DISPLAY - .u-display-none, .u-visibility-hidden, .visually-hidden, .hide-on-desktop, .size-*/.hide-on-*, [hidden], template',
  'utility-animations': 'UTILITY - ANIMATIONS - .animation(), .transition(), .transform(), .filter(), .filter-mixin(), .on-screen-anim(), .fade-in-*, .img-zoom(), @keyframes, html:not(.is-prefers-reduced-motion)',
  'utility-icons': 'UTILITY - ICONS - @font-face (icon font), .icon, the glyph bases, .inline-icon',
  'utility-a11y': 'UTILITY - A11Y - .a11y-focusguard, #a11y-focuser, .a11y-disable-focusoutline, .aria-label',
  'utility-test': 'UTILITY - TEST - .test harness (core tooltip test scaffolding)',

  'object-document': 'OBJECT - DOCUMENT - html/body/#wrapper scaffolding: .adapt-scrolling, .is-nav-top/bottom, .dir-rtl body',
  'object-element-reset': 'OBJECT - ELEMENT RESET - the normalize tag rules (incl. zw, nb, dialog, *, [type=*], and the IE11 img/object/embed .svg fix)',
  'object-nav': 'OBJECT - NAV - + .nav-ui-btn-ctrl-color*(), .show-nav-label()',
  'object-drawer': 'OBJECT - DRAWER - the one shared drawer singleton (dialog.drawer). pageLevelProgress, resources and languagePicker all render INTO this drawer via drawer.openCustomView() but are tokenised under their own component sections below, not here - their LESS never nests under .drawer.',
  'object-shadow': 'OBJECT - SHADOW - .shadow, a real DOM overlay element (body sibling), not a box-shadow utility',
  'object-notify': 'OBJECT - NOTIFY - + .notify-title(), .notify-btn-color*(), .notify-ui-btn-ctrl-color*()',
  'object-tooltip': 'OBJECT - TOOLTIP',
  'object-loading': 'OBJECT - LOADING',
  'object-shared-structure': 'OBJECT - SHARED STRUCTURE - the single combined .menu,.menu-item,.page,.article,.block,.component rule',
  'object-menu': 'OBJECT - MENU - + boxmenu, menu-item, .menu-*()/.menu-item-*() mixins',
  'object-page': 'OBJECT - PAGE - + .page-*()',
  'object-article': 'OBJECT - ARTICLE - + .article-*()',
  'object-block': 'OBJECT - BLOCK - + .block-*(), .block-color-mixin(), .block.extend-*',
  'object-component': 'OBJECT - COMPONENT - + .component-*(), .component-header-bg-mixin(), .component__attribution, .has-attribution',
  'object-buttons': 'OBJECT - BUTTONS - .btn, .btn-icon, .btn-text, .btn-color*(), button:not(.is-disabled)',

  'component-accordion': 'COMPONENT (native) - ACCORDION',
  'component-assessmentresults': 'COMPONENT (native) - ASSESSMENTRESULTS',
  'component-confidenceslider': 'COMPONENT (native) - CONFIDENCESLIDER',
  'component-gmcq': 'COMPONENT (native) - GMCQ',
  'component-hotgraphic': 'COMPONENT (native) - HOTGRAPHIC',
  'component-matching': 'COMPONENT (native) - MATCHING (incl. .dropdown*)',
  'component-mcq': 'COMPONENT (native) - MCQ',
  'component-media': 'COMPONENT (native) - MEDIA (incl. .mejs-container legacy + .mejs__container BEM - same player, two markup eras; .offset-media-controls)',
  'component-narrative': 'COMPONENT (native) - NARRATIVE',
  'component-slider': 'COMPONENT (native) - SLIDER',
  'component-textinput': 'COMPONENT (native) - TEXTINPUT',
  'component-glossary': 'COMPONENT (native extension) - GLOSSARY',
  'component-languagepicker': 'COMPONENT (native extension) - LANGUAGEPICKER (drawer-hosted)',
  'component-pagelevelprogress': 'COMPONENT (native extension) - PAGELEVELPROGRESS (drawer-hosted)',
  'component-resources': 'COMPONENT (native extension) - RESOURCES (drawer-hosted)',
  'component-trickle': 'COMPONENT (native extension) - TRICKLE',
  'component-tutor': 'COMPONENT (native extension) - TUTOR',
  'component-theme-project-layer': 'COMPONENT (theme project layer) - .aside-pull-quote, .figure-quote, blockquote,figure',
  'component-ours': 'COMPONENT (ours) - EMPTY: this file is compiled from Adapt core + the vanilla theme only, so it carries no adapt-ab-*/adapt-abbott-* selectors. "Ours" will only have rows once a local-plugin LESS pass is tokenised the same way.',
};

// ---------------------------------------------------------------------------
// Classification table: componentOf() bucket -> section.
// A bucket listed here with a plain string always maps every row in that
// bucket to that section. A bucket listed with an object of
// { default, overrides: [{test, section}] } is split: each row's full
// selector chain is tested against overrides in order (first match wins),
// falling back to `default` if none match.
// ---------------------------------------------------------------------------
const BUCKET_CLASSIFY = {
  // ----- utility-variables -----
  'root-vars': 'utility-variables',

  // ----- utility-colours -----
  bg: 'utility-colours',
  header: 'utility-colours',
  ui: 'utility-colours',
  item: {
    default: 'utility-colours',
    overrides: [{ test: sel => sel === '.item-title()', section: 'utility-typography' }],
  },

  // ----- utility-typography -----
  quote: 'utility-typography',
  pull: 'utility-typography',
  link: 'utility-typography',
  button: 'utility-typography',
  instruction: 'utility-typography',
  priority: 'utility-typography',
  text: 'utility-typography',
  font: 'utility-typography',
  is: 'utility-typography',

  // ----- utility-layout -----
  l: 'utility-layout',
  make: 'utility-layout',
  u: {
    default: 'utility-layout',
    overrides: [
      { test: sel => sel === '.u-display-none', section: 'utility-display' },
      { test: sel => sel === '.u-visibility-hidden', section: 'utility-display' },
    ],
  },

  // ----- utility-display -----
  visually: 'utility-display',
  size: 'utility-display',
  hide: 'utility-display',

  // ----- utility-animations -----
  on: 'utility-animations',
  fade: 'utility-animations',
  img: 'utility-animations', // .img-zoom() mixin only (bare <img> tag is base-elements)
  filter: 'utility-animations',
  animation: 'utility-animations',
  transition: 'utility-animations',
  transform: 'utility-animations',
  keyframes: 'utility-animations',

  // ----- utility-icons -----
  icon: 'utility-icons',
  inline: 'utility-icons',
  'font-face': 'utility-icons',

  // ----- utility-a11y -----
  a11y: 'utility-a11y',
  aria: 'utility-a11y',

  // ----- utility-test -----
  test: 'utility-test',

  // ----- object-document -----
  html: 'object-document', // the ".html.is-nav-top/bottom/.adapt-scrolling" class bucket
  dir: 'object-document',

  // ----- object-nav -----
  nav: 'object-nav',
  show: 'object-nav',

  // ----- object-drawer -----
  drawer: 'object-drawer',

  // ----- object-shadow -----
  shadow: 'object-shadow',

  // ----- object-notify -----
  notify: 'object-notify',

  // ----- object-tooltip -----
  tooltip: 'object-tooltip',

  // ----- object-loading -----
  loading: 'object-loading',

  // ----- object-menu (+ object-shared-structure split out) -----
  menu: {
    default: 'object-menu',
    overrides: [{
      test: sel => sel === '.menu,.menu-item,.page,.article,.block,.component',
      section: 'object-shared-structure',
    }],
  },
  boxmenu: 'object-menu',

  // ----- object-page / article / block / component / buttons -----
  page: 'object-page',
  article: 'object-article',
  block: 'object-block',
  component: 'object-component',
  has: 'object-component', // .has-attribution, defined next to .component__attribution
  btn: 'object-buttons',

  // ----- native components -----
  accordion: 'component-accordion',
  assessmentresults: 'component-assessmentresults',
  confidenceslider: 'component-confidenceslider',
  gmcq: 'component-gmcq',
  hotgraphic: 'component-hotgraphic',
  matching: 'component-matching',
  dropdown: 'component-matching',
  mcq: 'component-mcq',
  mejs: 'component-media',
  media: 'component-media', // literal .media class (player chrome), not @media
  offset: 'component-media',
  narrative: 'component-narrative',
  slider: 'component-slider',
  textinput: 'component-textinput',

  // ----- native extensions -----
  glossary: 'component-glossary',
  languagepicker: 'component-languagepicker',
  pagelevelprogress: 'component-pagelevelprogress',
  js: 'component-pagelevelprogress', // .js-heading + .pagelevelprogress__indicator, from pageLevelProgressIndicator.less
  resources: 'component-resources',
  trickle: 'component-trickle',
  tutor: 'component-tutor',

  // ----- theme project layer -----
  aside: 'component-theme-project-layer',
  figure: 'component-theme-project-layer',

  // the only literal @media-rooted row: an IE11 .svg-in-<img> fix sitting
  // inline in the normalize reset sheet, right after the img/object/embed
  // rule it patches.
  'media-queries': 'object-element-reset',
};

// base-elements is split by exact chain0 string rather than by bucket, since
// it mixes document scaffolding, the normalize reset sheet, and two rows the
// plan explicitly relocates to other tiers (utility-display, utility-
// animations, theme project layer).
const BASE_ELEMENTS_SECTION = (sel) => {
  if (sel === 'html' || sel === 'body' || sel === 'main'
    || sel === ':not(.adapt-scrolling), .adapt-scrolling body') return 'object-document';
  if (sel === '[hidden]' || sel === 'template') return 'utility-display';
  if (sel === 'html:not(.is-prefers-reduced-motion) .has-animation') return 'utility-animations';
  if (sel === 'blockquote,figure') return 'component-theme-project-layer';
  // the IE11 img/object/embed .svg fix sits inline in the normalize sheet
  if (sel.startsWith('@media screen and (-ms-high-contrast')) return 'object-element-reset';
  return 'object-element-reset';
};

function sectionOf(chain0) {
  const comp = componentOf(chain0);
  if (comp === 'base-elements') return BASE_ELEMENTS_SECTION(chain0);
  const entry = BUCKET_CLASSIFY[comp];
  if (!entry) return null;
  if (typeof entry === 'string') return entry;
  const hit = entry.overrides.find(o => o.test(chain0));
  return hit ? hit.section : entry.default;
}

// ---------------------------------------------------------------------------
// BEM sub-element ordering, used inside OBJECT tier sections only.
// ---------------------------------------------------------------------------
const BEM_ORDER = ['root', 'inner', 'outer', 'container', 'container-inner', 'background',
  'header', 'header-inner', 'header-content', 'priority', 'priority-label',
  'title', 'title-inner', 'subtitle', 'subtitle-inner', 'body', 'body-inner',
  'instruction', 'instruction-inner', 'widget'];
// Longest-first so e.g. "header-inner" is tested before "header".
const BEM_SUFFIXES = [...BEM_ORDER].filter(s => s !== 'root').sort((a, b) => b.length - a.length);

function subElementOf(chain) {
  const joined = chain.join(' ');
  for (const s of BEM_SUFFIXES) {
    if (new RegExp(`__${s}\\b`).test(joined)) return s;
  }
  for (const s of BEM_SUFFIXES) {
    if (new RegExp(`-${s}\\(`).test(joined)) return s;
  }
  // bare object selector, no suffix at all (e.g. ".block", ".page", ".menu")
  const last = chain[chain.length - 1].trim();
  if (/^[.#]?[a-zA-Z][a-zA-Z0-9-]*(\([^)]*\))?(:[a-zA-Z-]+(\([^)]*\))?)?$/.test(last)
    && !/__/.test(last) && !/-(inner|outer|container|background|header|title|subtitle|body|instruction|widget)/.test(last)) {
    return 'root';
  }
  return null; // remainder - sorted alphabetically by its own label below
}

function bemSortKey(chain) {
  const s = subElementOf(chain);
  if (s !== null) return [BEM_ORDER.indexOf(s), ''];
  // remainder: alphabetical by the last chain segment, after "widget"
  return [BEM_ORDER.length, chain[chain.length - 1].trim().toLowerCase()];
}

function main() {
  const { rows, rules } = loadTokenSource();

  const bySection = new Map();
  const unclassified = [];
  for (const r of rows) {
    const chain = rules.get(r.a.key).chain;
    const chain0 = chain[0].trim();
    const section = sectionOf(chain0);
    if (!section) { unclassified.push(chain0); continue; }
    if (!bySection.has(section)) bySection.set(section, []);
    bySection.get(section).push({ ...r, chain });
  }

  if (unclassified.length > 0) {
    const uniq = [...new Set(unclassified)];
    console.error(`FATAL: ${unclassified.length} row(s) across ${uniq.length} distinct base selector(s) did not classify into any section:`);
    for (const sel of uniq.slice(0, 40)) console.error(`  ${JSON.stringify(sel)}`);
    process.exit(1);
  }

  const knownSections = new Set(SECTION_ORDER);
  const leftoverSections = [...bySection.keys()].filter(s => !knownSections.has(s));
  if (leftoverSections.length > 0) {
    console.error(`FATAL: classifier produced section(s) not in SECTION_ORDER: ${leftoverSections.join(', ')}`);
    process.exit(1);
  }

  const lines = [];
  lines.push('/* =====================================================');
  lines.push('   AB TOKEN STRUCTURE - structure-first view of the same rows');
  lines.push('   =====================================================');
  lines.push('');
  lines.push('   Pure permutation of ab-token-values.less: identical --ab-<semantic>');
  lines.push('   names, values and comments, same 2083 rows - only the order and the');
  lines.push('   section headers differ. ab-token-values.less (function-first: the');
  lines.push('   11 functional groups, then component) is unchanged by this file.');
  lines.push('');
  lines.push('   Modelled on a CM Global CSS-style concatenation: utilities first');
  lines.push('   (sub-ordered by function - see tools/lib/ab-token-source.js\'s');
  lines.push('   groupOf()), then objects in Adapt\'s real rendered page order,');
  lines.push('   top to bottom (sub-ordered by BEM sub-element: root, inner, outer,');
  lines.push('   container(-inner), background, header(-inner/-content), priority');
  lines.push('   (-label), title(-inner), subtitle(-inner), body(-inner),');
  lines.push('   instruction(-inner), widget, then any remainder alphabetically),');
  lines.push('   then components - native Adapt components and extensions before');
  lines.push('   "ours" (empty here; see object-drawer and component-ours headers).');
  lines.push('');
  lines.push('   ~250 rows are LESS mixin *definitions* (trailing "()"), not real');
  lines.push('   DOM selectors - object-specific mixins travel with their object');
  lines.push('   (e.g. .page-title() is in object-page); generic ones live in');
  lines.push('   utilities (e.g. .bg-color-mixin() is in utility-colours).');
  lines.push('');
  lines.push('   There is exactly ONE drawer (dialog.drawer, a core singleton).');
  lines.push('   pageLevelProgress/resources/languagePicker render INTO it at');
  lines.push('   runtime but are tokenised under their own component sections,');
  lines.push('   since their LESS never nests under .drawer - see object-drawer\'s');
  lines.push('   header. There is no page footer in core or vanilla theme at all.');
  lines.push('   ===================================================== */');
  lines.push('');
  lines.push(':root {');

  let emittedRows = 0;
  const inventory = [];
  const tierOf = (section) => UTILITY_SECTIONS.includes(section) ? 'UTILITIES'
    : OBJECT_SECTIONS.includes(section) ? 'OBJECTS' : 'COMPONENTS';
  let lastTier = null;
  for (const section of SECTION_ORDER) {
    const secRows = bySection.get(section) || [];
    const tier = tierOf(section);
    if (tier !== lastTier) {
      lines.push('');
      lines.push(`  /* ===================================================== */`);
      lines.push(`  /* ${tier}`);
      lines.push(`  /* ===================================================== */`);
      lastTier = tier;
    }
    lines.push('');
    lines.push(`  /* --- ${SECTION_HEADER[section]} (${secRows.length}) --- */`);
    inventory.push({ tier, section, count: secRows.length });
    if (secRows.length === 0) continue;

    let ordered;
    if (OBJECT_SECTIONS.includes(section)) {
      ordered = secRows
        .map((r, i) => ({ r, i, key: bemSortKey(r.chain) }))
        .sort((x, y) => {
          if (x.key[0] !== y.key[0]) return x.key[0] - y.key[0];
          if (x.key[1] !== y.key[1]) return x.key[1] < y.key[1] ? -1 : 1;
          return x.i - y.i;
        })
        .map(({ r }) => r);
    } else if (UTILITY_SECTIONS.includes(section)) {
      ordered = secRows
        .map((r, i) => ({ r, i, g: GROUP_ORDER.indexOf(groupOf(r.a.prop)) }))
        .sort((x, y) => {
          const xg = x.g === -1 ? GROUP_ORDER.length : x.g;
          const yg = y.g === -1 ? GROUP_ORDER.length : y.g;
          if (xg !== yg) return xg - yg;
          return x.i - y.i;
        })
        .map(({ r }) => r);
    } else {
      ordered = secRows; // components tier: keep original document order
    }

    for (const { sem, a, chain } of ordered) {
      const rule = rules.get(a.key);
      const word = LAYER_WORD[a.layer];
      const comment = `${word} ${chain.join(' ').trim()} { ${rule.decls.join('; ')}; }`;
      lines.push(`  ${sem}: ${a.value}; // ${comment}`);
      emittedRows++;
    }
  }

  lines.push('}');
  lines.push('');
  fs.writeFileSync(OUT, lines.join('\n'));

  console.log(`Rows emitted: ${emittedRows}`);
  console.log(`Sections: ${SECTION_ORDER.length} (${inventory.filter(s => s.count > 0).length} non-empty, ${inventory.filter(s => s.count === 0).length} empty)`);
  console.log('');
  console.log('Section inventory:');
  console.log('Tier       | Section                        | Rows');
  console.log('-----------|--------------------------------|-----');
  let tierTotals = {};
  for (const { tier, section, count } of inventory) {
    tierTotals[tier] = (tierTotals[tier] || 0) + count;
    console.log(`${tier.padEnd(10)} | ${section.padEnd(30)} | ${count}`);
  }
  console.log('');
  for (const [tier, total] of Object.entries(tierTotals)) {
    console.log(`${tier} total: ${total}`);
  }
  console.log(`Grand total: ${Object.values(tierTotals).reduce((a, b) => a + b, 0)}`);
  console.log(`Written: ${OUT}`);
}

main();
