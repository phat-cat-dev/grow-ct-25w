'use strict';
/**
 * ab-map-cascade.js
 *
 * Reads the LIVE AB theme cascade for adapt-styles-mapping.js. Two distinct
 * sources exist and this module keeps them distinct rather than merging them:
 *
 *   PORTABLE — adapt-ab-theme/layers/*.css (plain CSS, L2-L6). The clean,
 *     fully-reconciled extraction. Source of the regression numbers in the
 *     plan (15 L2 aliases, 300 sweep pairs is NOT here - see LIVE; 114 L3
 *     pivots/52 themeable, 154 L4 defaults/37 themeable, 43 L5 advertised,
 *     ~1830 consumed, ~1787 undocumented, 0 dead-contract, 2 non-parity).
 *
 *   LIVE — src/extensions/adapt-ab-theme/less/ab-vanilla-overrides.less. What
 *     actually ships. Its :root alias block (the L2 seam) is MID-MIGRATION:
 *     some of its 15 roles point at the portable L3 pivot (--ab-base-*), the
 *     rest still point at a THIRD, older flat semantic system (--ab-primary,
 *     --ab-white, --ab-light, --ab-success, --ab-danger, ... defined in
 *     ab-core.less / ab-palette.less / cm-corporate.less / cm-theme-packs.less)
 *     that bypasses L3/L4/L5 entirely. This module reports that divergence
 *     per-role rather than resolving it, and tags every such target
 *     `legacy_semantic` instead of silently treating it as an L3 pivot - the
 *     resolution of THAT chain is a separate, further remap, not assumed here.
 *     It also carries the 300 (selector, property) -> token sweep pairs that
 *     are Adapt's only bridge from a rendered class back to a live token.
 *
 * Reads only. Never writes.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const PORTABLE_DIR = path.join(ROOT, 'adapt-ab-theme', 'layers');
const LIVE_DIR = path.join(ROOT, 'src', 'extensions', 'adapt-ab-theme', 'less');

const PORTABLE_FILES = {
  l2: 'L2-adapter.css',
  l3: ['L3-pivot.css', 'L3-semantics.css', 'L3-accent-spectrum.css'],
  l4: ['L4-defaults.css', 'L4-semantics.css', 'L4-accent-spectrum.css'],
  l5: 'L5-template.css',
  l6: { pink: 'L6-thm-pink.css', blue: 'L6-thm-blue.css' },
};

// ---------------------------------------------------------------------------
// Generic plain-CSS declaration reader. Handles both `/* */` (CSS/LESS) and
// `//` (LESS-only) comments, and the `*/`-inside-a-comment hazard the sandbox
// side already proved exists, by stripping block comments across the whole
// text (not line-by-line) before splitting into statements.
// ---------------------------------------------------------------------------
function stripComments(text) {
  // Block comments first, across newlines, non-greedy.
  let out = text.replace(/\/\*[\s\S]*?\*\//g, '');
  // Then LESS line comments. Guard against `//` inside a quoted string
  // (none of these files use urls or quoted content with `//`, but be safe).
  out = out.split('\n').map((line) => {
    const q = line.indexOf('"');
    const slash = line.indexOf('//');
    if (slash === -1) return line;
    if (q !== -1 && q < slash) return line; // leave quoted lines alone
    return line.slice(0, slash);
  }).join('\n');
  return out;
}

/**
 * declarations: [{ selector, prop, value, raw }]
 * selector is the full nested chain joined with ' > ' (e.g. ':root' or
 * ':root[data-theme="dark"]').
 */
function parseDeclarations(text) {
  const clean = stripComments(text);
  const decls = [];
  const stack = [];
  let i = 0;
  let depth = 0; // paren depth, to avoid splitting inside var(a, b)
  let buf = '';
  const flushDecl = () => {
    const d = buf.trim();
    buf = '';
    if (!d) return;
    // Portable layer files only ever declare custom properties (--ab-*).
    // The live sweep file (ab-vanilla-overrides.less) declares plain CSS
    // properties (color, border-color, background-color, ...) whose VALUES
    // reference custom properties via var(...) - the property name itself
    // is not --prefixed, so this must accept both shapes.
    const m = d.match(/^(-{0,2}[a-zA-Z][a-zA-Z0-9_-]*)\s*:\s*([\s\S]*)$/);
    if (m) decls.push({ selector: stack.join(' > ') || ':root', prop: m[1], value: m[2].trim(), raw: d });
  };
  while (i < clean.length) {
    const c = clean[i];
    if (c === '(') { depth++; buf += c; i++; continue; }
    if (c === ')') { depth = Math.max(0, depth - 1); buf += c; i++; continue; }
    if (depth > 0) { buf += c; i++; continue; }
    if (c === '{') { stack.push(buf.trim().replace(/\s+/g, ' ')); buf = ''; i++; continue; }
    if (c === '}') { flushDecl(); stack.pop(); i++; continue; }
    if (c === ';') { flushDecl(); i++; continue; }
    buf += c; i++;
  }
  return decls;
}

/** Every `var(--token...)` reference inside a value, outermost first. */
function varRefs(value) {
  const refs = [];
  const re = /var\(\s*(--[a-zA-Z0-9_-]+)/g;
  let m;
  while ((m = re.exec(value))) refs.push(m[1]);
  return refs;
}

const read = (p) => fs.readFileSync(p, 'utf8');
const existsAll = (dir, names) => (Array.isArray(names) ? names : [names]).every((n) => fs.existsSync(path.join(dir, n)));

function readPortableGroup(names) {
  const list = Array.isArray(names) ? names : [names];
  const decls = [];
  for (const name of list) {
    const file = path.join(PORTABLE_DIR, name);
    if (!fs.existsSync(file)) continue;
    for (const d of parseDeclarations(read(file))) decls.push({ ...d, file: name });
  }
  return decls;
}

/**
 * Builds the node map keyed by custom-property name. A token can be declared
 * more than once (e.g. the dark-mode override block), so value is kept as a
 * list of { value, selector, file, varRefs }.
 */
function indexByName(decls) {
  const byName = new Map();
  for (const d of decls) {
    if (!byName.has(d.prop)) byName.set(d.prop, []);
    byName.get(d.prop).push({ value: d.value, selector: d.selector, file: d.file, varRefs: varRefs(d.value) });
  }
  return byName;
}

const L2_PREFIX = '--ab-base-if-adapt-';
const L4_PREFIX = '--ab-base-pf-default-';
const L5_PREFIX = '--ab-theme-pf-default-';
const L6_PREFIX = { pink: '--ab-thm-pink-', blue: '--ab-thm-blue-' };
const L3_PREFIX = '--ab-base-';

function bandOf(name) {
  if (name.startsWith(L2_PREFIX)) return 'L2';
  if (name.startsWith(L4_PREFIX)) return 'L4';
  if (name.startsWith(L5_PREFIX)) return 'L5';
  if (name.startsWith('--ab-thm-')) return 'L6';
  if (name.startsWith(L3_PREFIX)) return 'L3';
  return 'other';
}

/**
 * Classifies a single L3 pivot or L4 default declaration's hook shape by
 * inspecting its var() chain, WITHOUT assuming name parity between the
 * consumer and the theme token it reads (two real cases in this cascade -
 * accent-l/accent-l-dark and l-surface/l-surface-dark - break parity).
 *
 *   themeable : var(--ab-theme-pf-default-X, <fallback>)   - L5 wins if set
 *   fixed     : var(--ab-base-pf-default-X)  with no theme ref anywhere      (L3 only)
 *   literal   : no var() at all - a hand-written literal default            (L4 only)
 */
function hookShape(entry) {
  const hasThemeRef = entry.varRefs.some((r) => r.startsWith(L5_PREFIX));
  if (hasThemeRef) return 'themeable';
  if (entry.varRefs.length) return 'fixed';
  return 'literal';
}

function loadPortable(pack) {
  pack = pack === 'blue' ? 'blue' : 'pink';
  const l2Decls = readPortableGroup(PORTABLE_FILES.l2);
  const l3Decls = readPortableGroup(PORTABLE_FILES.l3);
  const l4Decls = readPortableGroup(PORTABLE_FILES.l4);
  const l5Decls = readPortableGroup(PORTABLE_FILES.l5);
  const l6File = PORTABLE_FILES.l6[pack];
  const l6Decls = readPortableGroup(l6File);

  const l2 = indexByName(l2Decls);
  const l3 = indexByName(l3Decls);
  const l4 = indexByName(l4Decls);
  const l6 = indexByName(l6Decls);

  // L5 advertised: scan the RAW text (comments included) for the contract -
  // every token the file DECLARES, live or commented-out, is "advertised".
  // Lookahead for the declaration colon excludes prose mentions such as the
  // docblock's own placeholder example `var(--ab-theme-pf-default-X, ...)`,
  // which is followed by a comma, not a colon.
  const l5Raw = read(path.join(PORTABLE_DIR, PORTABLE_FILES.l5));
  const advertised = new Set((l5Raw.match(/--ab-theme-pf-default-[a-zA-Z0-9_-]+(?=\s*:)/g) || []));
  const l5Live = indexByName(l5Decls); // only the 1-3 uncommented lines

  // Every live L5-token consumption site across L2/L3/L4/L6 (and L5 itself,
  // for the font-heading/-body self-reference pattern).
  const consumed = new Set();
  const nonParity = [];
  const allDecls = [...l2Decls, ...l3Decls, ...l4Decls, ...l5Decls, ...l6Decls];
  for (const d of allDecls) {
    for (const ref of varRefs(d.value)) {
      if (ref.startsWith(L5_PREFIX)) {
        consumed.add(ref);
        const consumerSuffix = d.prop.replace(L4_PREFIX, '').replace(L3_PREFIX, '');
        const themeSuffix = ref.replace(L5_PREFIX, '');
        if (consumerSuffix !== themeSuffix) {
          nonParity.push({ file: d.file, consumer: d.prop, themeToken: ref });
        }
      }
    }
  }

  const deadContract = [...advertised].filter((t) => !consumed.has(t));
  const undocumented = [...consumed].filter((t) => !advertised.has(t));

  const l3Hooks = l3Decls.map((d) => ({ name: d.prop, shape: hookShape({ varRefs: varRefs(d.value) }) }));
  const l4Hooks = l4Decls.map((d) => ({ name: d.prop, shape: hookShape({ varRefs: varRefs(d.value) }) }));

  return {
    pack,
    byName: new Map([...l2, ...l3, ...l4, ...l5Live, ...l6]),
    l2, l3, l4, l5Live, l6,
    l5Advertised: advertised,
    l5Consumed: consumed,
    deadContract,
    undocumentedHooks: undocumented,
    nonParityHooks: nonParity,
    l3Pivots: { total: l3Decls.length, themeable: l3Hooks.filter((h) => h.shape === 'themeable').length, fixed: l3Hooks.filter((h) => h.shape === 'fixed').length },
    l4Defaults: { total: l4Decls.length, themeable: l4Hooks.filter((h) => h.shape === 'themeable').length, literal: l4Hooks.filter((h) => h.shape === 'literal').length },
    rawDecls: { l2: l2Decls, l3: l3Decls, l4: l4Decls, l5: l5Decls, l6: l6Decls },
  };
}

// ---------------------------------------------------------------------------
// LIVE: ab-vanilla-overrides.less — the :root alias block (first ~65 lines,
// up to the first non-:root selector) is the L2 seam; everything after it is
// the (selector, property) -> token sweep.
// ---------------------------------------------------------------------------
function loadLiveVanillaOverrides() {
  const file = path.join(LIVE_DIR, 'ab-vanilla-overrides.less');
  const text = read(file);
  const decls = parseDeclarations(text).map((d) => ({ ...d, file: 'ab-vanilla-overrides.less' }));

  const aliasDecls = decls.filter((d) => d.selector.includes(':root') && d.prop.startsWith(L2_PREFIX));
  const sweepDecls = decls.filter((d) => !d.selector.includes(':root'));

  const aliases = aliasDecls.map((d) => {
    const ref = varRefs(d.value)[0] || null;
    const legacy = ref !== null && !ref.startsWith(L3_PREFIX) && bandOf(ref) === 'other';
    return { role: d.prop, target: ref, legacy, selector: d.selector };
  });

  const sweepPairs = [];
  for (const d of sweepDecls) {
    const selectors = d.selector.split(',').map((s) => s.trim()).filter(Boolean);
    const ref = varRefs(d.value)[0] || null;
    const important = /!important/i.test(d.value);
    for (const sel of selectors) {
      sweepPairs.push({ selector: sel, property: d.prop, token: ref, important, file: 'ab-vanilla-overrides.less' });
    }
  }

  return { aliases, sweepPairs, legacyAliasCount: aliases.filter((a) => a.legacy).length };
}

/**
 * Loads everything this module provides, for one pack/mode.
 * Returns the portable cascade (the numeric source of truth), the live L2
 * seam + sweep (the bridge back to Adapt selectors), and a divergence report
 * between the two L2 seams (portable vs live), keyed by role.
 */
function loadCascade({ pack = 'pink' } = {}) {
  const portable = loadPortable(pack);
  const live = loadLiveVanillaOverrides();

  const portableL2ByRole = new Map();
  for (const [name, entries] of portable.l2) portableL2ByRole.set(name, entries[0].varRefs[0] || null);

  const l2Divergence = live.aliases.map((a) => {
    const portableTarget = portableL2ByRole.get(a.role) || null;
    return {
      role: a.role,
      liveTarget: a.target,
      liveIsLegacy: a.legacy,
      portableTarget,
      diverges: portableTarget !== a.target,
    };
  });

  return {
    portable,
    live,
    l2Divergence,
    counts: {
      l2AliasesLive: live.aliases.length,
      l2AliasesLegacy: live.legacyAliasCount,
      sweepPairs: live.sweepPairs.length,
      sweepProperties: new Set(live.sweepPairs.map((p) => p.property)).size,
      l3PivotsTotal: portable.l3Pivots.total,
      l3PivotsThemeable: portable.l3Pivots.themeable,
      l4DefaultsTotal: portable.l4Defaults.total,
      l4DefaultsThemeable: portable.l4Defaults.themeable,
      l5Advertised: portable.l5Advertised.size,
      l5Consumed: portable.l5Consumed.size,
      l5DeadContract: portable.deadContract.length,
      l5Undocumented: portable.undocumentedHooks.length,
      nonParityHooks: portable.nonParityHooks.length,
    },
  };
}

module.exports = {
  PORTABLE_DIR,
  LIVE_DIR,
  parseDeclarations,
  varRefs,
  bandOf,
  hookShape,
  loadPortable,
  loadLiveVanillaOverrides,
  loadCascade,
};

if (require.main === module) {
  const pack = process.argv.includes('--pack') ? process.argv[process.argv.indexOf('--pack') + 1] : 'pink';
  const data = loadCascade({ pack });
  console.log(JSON.stringify(data.counts, null, 2));
  console.log('\nL2 divergence (live vs portable):');
  for (const d of data.l2Divergence) {
    console.log(`  ${d.role.padEnd(42)} live=${String(d.liveTarget).padEnd(30)} legacy=${d.liveIsLegacy}  portable=${d.portableTarget}  diverges=${d.diverges}`);
  }
  console.log('\nNon-parity hooks:');
  for (const n of data.portable.nonParityHooks) console.log(`  ${n.file}: ${n.consumer} <- ${n.themeToken}`);
  console.log('\nDead contract (advertised, unconsumed):', data.portable.deadContract);
  console.log('Undocumented hooks (consumed, unadvertised): count =', data.portable.undocumentedHooks.length);
}
