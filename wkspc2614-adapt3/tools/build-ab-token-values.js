#!/usr/bin/env node
/**
 * build-ab-token-values.js
 *
 * Assigns real values to the --ab-<semantic> names (ab-token-base.less only
 * renamed the registry, it never defined anything). One row per original
 * tokenised declaration (2083 - not deduplicated, deliberately: where core
 * and theme both set the same --ab-<semantic>, both rows are kept, in
 * document order (core before theme, matching Adapt's real build order), so
 * a human can see every core/theme pair side by side and decide what moves
 * to --ab-base-pf-default-* versus a theme profile later. Comment is the
 * ab-token-base.less full-ruleset style, with a "core " / "theme " word
 * prefixed so the origin is visible without cross-referencing the registry.
 *
 * Reads (never writes, via tools/lib/ab-token-source.js):
 *   adapt-core-vanilla-interface.less       - plain, untokenised structure + values
 *   adapt-core-vanilla-interface-uuid.tokens.less - which declarations are
 *     tokenised, their registry group/layer/number, in document order
 *   ab-token-base.less                      - registry -> --ab-<semantic> names
 *
 * Writes:
 *   ab-token-values.less
 *
 * Usage: node tools/build-ab-token-values.js
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { DIR, GROUP_ORDER, LAYER_WORD, loadTokenSource } = require('./lib/ab-token-source');

const OUT = path.join(DIR, 'ab-token-values.less');

// Second split: within each of the 11 functional groups, cluster rows by
// the "component" (or utility-class family) their base selector belongs
// to. Derived mechanically from chain[0] (the outermost selector of the
// rule, before any &-nesting): @media/@font-face/@keyframes/:root get
// their own cross-cutting bucket; a class or id selector contributes its
// leading identifier up to the first '-', '_', ':', '[' or space (so
// .btn-color-outline-focus and .btn-color-disabled both collapse onto
// "btn", .icon-arrow-up-2 collapses onto "icon", .gmcq-item__label
// collapses onto "gmcq"); anything else (bare tags, attribute selectors,
// the universal selector) falls into "base-elements", since those are
// the browser-reset rules with no class to key off.
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
const PINNED_LAST = ['media-queries', 'font-face', 'keyframes', 'root-vars'];
function compareComponents(x, y) {
  if (x === 'base-elements') return y === 'base-elements' ? 0 : -1;
  if (y === 'base-elements') return 1;
  const xp = PINNED_LAST.includes(x), yp = PINNED_LAST.includes(y);
  if (xp && !yp) return 1;
  if (!xp && yp) return -1;
  if (xp && yp) return PINNED_LAST.indexOf(x) - PINNED_LAST.indexOf(y);
  return x < y ? -1 : x > y ? 1 : 0;
}

// Property list used to derive each group, for the section headers.
const GROUP_HEADER = {
  layout: 'LAYOUT - display, position, top/right/bottom/left, float, clear, overflow(-x/-y), box-sizing, align-items, justify-content, flex-*, order, z-index, scroll-padding-*, --adapt-tooltip-*',
  colour: 'COLOUR - color, background-color, border-color, border-bottom-color, border-top-color',
  typography: 'TYPOGRAPHY - font, font-*, line-height, letter-spacing, text-*, white-space, direction, vertical-align, speak, src, font-smoothing, -webkit-text-size-adjust',
  content: 'CONTENT - content',
  spacing: 'SPACING - margin*, padding*, column-gap, row-gap',
  sizing: 'SIZING - width, height, min/max-width, min/max-height, --adapt-viewport-height, --adapt-navigation-height',
  motion: 'MOTION - animation, transition, transition-delay, transform, transform-origin, --adapt-cubic-bezier-*',
  effect: 'EFFECT - box-shadow, filter, opacity, visibility, zoom, clip',
  border: 'BORDER - border, border-bottom/-right, border-radius (+vendor), border-style, border-width, outline, outline-offset',
  background: 'BACKGROUND - background, background-position, background-repeat, background-size',
  interaction: 'INTERACTION - cursor, pointer-events, user-select (+vendor), -webkit-touch-callout, -webkit-overflow-scrolling, -webkit-appearance',
};

function main() {
  const { rows, rules, reorderedGroups } = loadTokenSource();

  const lines = [];
  lines.push('/* =====================================================');
  lines.push('   AB TOKEN VALUES - semantic tokens given real values');
  lines.push('   =====================================================');
  lines.push('');
  lines.push('   One row per originally-tokenised declaration (not deduplicated):');
  lines.push('   where core and a theme both set the same --ab-<semantic> name,');
  lines.push('   BOTH rows are kept, so a human can see every core/theme pair side');
  lines.push('   by side and decide what belongs in a --ab-base-pf-default-*');
  lines.push('   profile versus a theme profile. Rows are otherwise in this');
  lines.push('   comparison document\'s own section order (NOT Adapt\'s real build');
  lines.push('   order - this document interleaves theme-only and core-only');
  lines.push('   sections, so a theme row can sit above its core counterpart here);');
  lines.push('   where the same name repeats, core is always placed immediately');
  lines.push('   before theme so the later row is always the real-build-order');
  lines.push('   override if this file is compiled as-is.');
  lines.push('');
  lines.push('   Values are copied verbatim from adapt-core-vanilla-interface.less.');
  lines.push('   Some are LESS variables or mixin calls (e.g. @icon-size,');
  lines.push('   ~\'@{btn-padding}\') that only resolve inside their original Adapt');
  lines.push('   scope - carried over as-authored, not pre-resolved.');
  lines.push('');
  lines.push('   Rows are organised in two levels inside this one :root block:');
  lines.push('   first by the 11 functional groups (layout, colour, typography,');
  lines.push('   content, spacing, sizing, motion, effect, border, background,');
  lines.push('   interaction - largest to smallest), then within each group by');
  lines.push('   "component": the leading class/id identifier of the row\'s base');
  lines.push('   selector (e.g. .btn-color-outline-focus and .btn-color-disabled');
  lines.push('   both collapse onto "btn"; .icon-arrow-up-2 onto "icon"). Bare');
  lines.push('   tag/attribute/universal selectors with no class to key off land');
  lines.push('   in "base-elements"; @media/@font-face/@keyframes/:root land in');
  lines.push('   their own cross-cutting buckets at the end of each group. This is');
  lines.push('   a mechanical heuristic on the selector text, not a curated taxonomy');
  lines.push('   - sense-check any component bucket before relying on it.');
  lines.push('   ===================================================== */');
  lines.push('');
  lines.push(':root {');

  const byGroup = new Map();
  for (const r of rows) {
    if (!byGroup.has(r.a.group)) byGroup.set(r.a.group, []);
    byGroup.get(r.a.group).push(r);
  }
  const knownGroups = new Set(GROUP_ORDER);
  const leftoverGroups = [...byGroup.keys()].filter(g => !knownGroups.has(g)).sort();
  if (leftoverGroups.length > 0) {
    console.error(`FATAL: unexpected token group(s) not in the 11-group taxonomy: ${leftoverGroups.join(', ')}`);
    process.exit(1);
  }

  let emittedRows = 0;
  for (const group of GROUP_ORDER) {
    const groupRows = byGroup.get(group);
    if (!groupRows || groupRows.length === 0) continue;

    const byComponent = new Map();
    for (const r of groupRows) {
      const comp = componentOf(rules.get(r.a.key).chain[0]);
      if (!byComponent.has(comp)) byComponent.set(comp, []);
      byComponent.get(comp).push(r);
    }
    const components = [...byComponent.keys()].sort(compareComponents);

    lines.push('');
    lines.push(`  /* ===== ${GROUP_HEADER[group]} (${groupRows.length} tokens) ===== */`);
    for (const comp of components) {
      const compRows = byComponent.get(comp);
      lines.push(`  /* --- ${comp} (${compRows.length}) --- */`);
      for (const { sem, a } of compRows) {
        const rule = rules.get(a.key);
        const word = LAYER_WORD[a.layer];
        const comment = `${word} ${rule.chain.join(' ').trim()} { ${rule.decls.join('; ')}; }`;
        lines.push(`  ${sem}: ${a.value}; // ${comment}`);
        emittedRows++;
      }
    }
  }
  console.log(`Reordered groups (theme moved after its core counterpart): ${reorderedGroups}`);
  console.log(`Groups emitted: ${GROUP_ORDER.filter(g => byGroup.has(g)).length} of ${GROUP_ORDER.length}`);
  console.log(`Rows emitted: ${emittedRows}`);

  lines.push('}');
  lines.push('');
  fs.writeFileSync(OUT, lines.join('\n'));

  const rowCount = lines.filter(l => /^\s*--ab-/.test(l)).length;
  console.log(`Written: ${OUT} (${rowCount} rows)`);
}

main();
