#!/usr/bin/env node
/**
 * ab-theme-computed.js — export the RUNTIME (computed) theme styles.
 *
 * theme-css.js emits the COMPILED css (LESS -> CSS), but there the tokens are
 * still live CSS functions: var(--x), color-mix(...), clamp(...). This tool goes
 * one step further and exports what those actually RESOLVE TO at runtime — the
 * real hex of every color-mix, the px of every clamp, the end of every var()
 * chain — by loading the compiled theme in headless Chromium under each colour
 * theme pack x mode and reading getComputedStyle.
 *
 *   node tools/ab-theme-computed.js                      (or: npm run theme-computed)
 *   node tools/ab-theme-computed.js --viewport=1280x800  (clamp/length resolve per viewport)
 *
 * For each pack x mode it writes, to exports/theme-computed/:
 *   <pack>-<mode>.json  — every --ab-* token -> { raw, resolved, type }
 *   <pack>-<mode>.css   — a flat :root{} block with the RESOLVED values (no
 *                         var()/color-mix()/clamp() left), i.e. the runtime look
 *                         as plain CSS you can read or diff.
 *   _index.md           — what was produced and the viewport used.
 *
 * Colours resolve exactly (color-mix in srgb is what the browser computes).
 * Lengths with clamp()/vw/vh resolve for the stated viewport only — the file
 * header and _index.md record which viewport, since those values are viewport
 * dependent by design.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

function findRoot(s) { let d = s; for (let i = 0; i < 10; i++) { if (fs.existsSync(path.join(d, 'Gruntfile.js'))) return d; const u = path.dirname(d); if (u === d) break; d = u; } return s; }
const ROOT = findRoot(fs.existsSync(path.join(process.cwd(), 'Gruntfile.js')) ? process.cwd() : __dirname);
const LESS_DIR = path.join(ROOT, 'src', 'extensions', 'adapt-ab-theme', 'less');
const OUT_DIR = path.join(ROOT, 'exports', 'theme-computed');

// packs and modes to export. Add a pack name here when a new cm-theme-<name> pack
// is added in cm-theme-packs.less; '' is the no-pack generic fallback. A pack
// name already containing '-theme-' (e.g. 'cmab-theme-dual', from
// cmab-theme-packs.less) is used as the literal html class as-is, rather than
// prefixed with cm-theme- — see the cls expression below.
const PACKS = ['', 'dark-blue', 'dark-grey', 'dark-blue-grey', 'cmab-theme-dual'];
const MODES = ['light', 'dark'];

// ---- args ----
const args = Object.fromEntries(process.argv.slice(2).map(a => {
  const m = a.replace(/^--/, '').split('='); return [m[0], m[1] ?? true];
}));
const [VW, VH] = String(args.viewport || '1280x800').split('x').map(Number);

// ---- 1. compile every theme LESS file to CSS and concatenate ----
function compileThemeCss() {
  const files = fs.readdirSync(LESS_DIR).filter(f => f.endsWith('.less')).sort();
  // palette first (base hexes), then the rest; order is not load-bearing for
  // correctness (var() resolves live, packs out-specify by class), but keeps the
  // bundle readable.
  files.sort((a, b) => (a === 'ab-palette.less' ? -1 : b === 'ab-palette.less' ? 1 : a.localeCompare(b)));
  let bundle = '';
  const failed = [];
  for (const f of files) {
    const r = spawnSync('npx', ['lessc', path.join(LESS_DIR, f)], { cwd: ROOT, encoding: 'utf8', shell: true });
    if (r.status !== 0) { failed.push(f); continue; }
    bundle += `\n/* ${f} */\n` + r.stdout;
  }
  return { bundle, failed, fileCount: files.length };
}

// ---- 2. collect every --ab-* token name declared in the bundle ----
function tokenNames(css) {
  const set = new Set();
  const re = /(--ab-[A-Za-z0-9-]+)\s*:/g;
  let m; while ((m = re.exec(css))) set.add(m[1]);
  return [...set].sort();
}

// ---- 3. in-browser probe (runs in page context) ----
/* eslint-disable */
function PAGE_PROBE(names) {
  const root = document.documentElement;
  const rootCS = getComputedStyle(root);
  const colorEl = document.getElementById('probe-color');
  const lenBox = document.getElementById('probe-len');   // 1000px-wide parent for % tokens
  const lenEl = document.getElementById('probe-len-child');
  const out = {};
  for (const name of names) {
    const raw = rootCS.getPropertyValue(name).trim();
    // color probe: set a standard color property to the token and read it back
    colorEl.style.removeProperty('color');
    colorEl.style.setProperty('color', 'var(' + name + ')');
    const color = getComputedStyle(colorEl).color;
    // length probe: set width to the token (child of a fixed 1000px box)
    lenEl.style.removeProperty('width');
    lenEl.style.setProperty('width', 'var(' + name + ')');
    const width = getComputedStyle(lenEl).width;
    // classify by the raw (computed) custom-property value
    let type, resolved;
    if (/#[0-9a-f]|rgba?\(|hsla?\(|color-mix\(|oklch\(|\blab\(|color\(/i.test(raw)) {
      type = 'color'; resolved = color;
    } else if (/clamp\(|calc\(|[-0-9.]+\s*(px|rem|em|vw|vh|vi|vmin|vmax|%)/i.test(raw)) {
      type = 'length'; resolved = width;
    } else {
      type = 'raw'; resolved = raw;
    }
    out[name] = { raw, resolved, type };
  }
  return out;
}
/* eslint-enable */

// ---- computed colour -> #hex for the flat css, where possible ----
// Handles both forms Chromium returns: rgb()/rgba() (0-255), and the
// color(srgb r g b / a) form (0-1 floats) that color-mix() computes to.
function toHex(v) {
  const h = x => Math.max(0, Math.min(255, x)).toString(16).padStart(2, '0');
  let r, g, b, a = 1;
  let m = /^rgba?\(([^)]+)\)/.exec(v);
  if (m) {
    const p = m[1].split(/[,\/]/).map(s => s.trim()).filter(Boolean);
    [r, g, b] = p.slice(0, 3).map(n => Math.round(parseFloat(n)));
    if (p[3] != null) a = parseFloat(p[3]) > 1 ? parseFloat(p[3]) / 100 : parseFloat(p[3]);
  } else if ((m = /^color\(srgb\s+([^)]+)\)/.exec(v))) {
    const p = m[1].split(/[\s/]+/).map(s => s.trim()).filter(Boolean);
    [r, g, b] = p.slice(0, 3).map(n => Math.round(parseFloat(n) * 255));
    if (p[3] != null) a = parseFloat(p[3]);
  } else { return null; }
  if ([r, g, b].some(n => Number.isNaN(n))) return null;
  const base = '#' + h(r) + h(g) + h(b);
  return a >= 1 ? base : base + h(Math.round(a * 255));
}

async function main() {
  let chromium;
  try { ({ chromium } = require('playwright')); }
  catch { console.error('REFUSED: playwright not installed. npm i -D playwright (Chromium is at /opt/pw-browsers).'); process.exit(1); }

  console.log('Compiling theme LESS -> CSS ...');
  const { bundle, failed, fileCount } = compileThemeCss();
  if (failed.length) console.error(`  WARNING: ${failed.length} file(s) failed to compile: ${failed.join(', ')}`);
  const names = tokenNames(bundle);
  console.log(`  ${fileCount} less file(s), ${names.length} --ab-* token(s) found.`);

  fs.mkdirSync(OUT_DIR, { recursive: true });
  // Use a pre-installed Chromium when present (cloud sandboxes pin one and
  // forbid `playwright install`): CM_CHROMIUM env, else the /opt/pw-browsers
  // symlink, else Playwright's own bundled download.
  const pinned = process.env.CM_CHROMIUM
    || (fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : null);
  const browser = await chromium.launch(pinned ? { executablePath: pinned } : {});
  const index = [];

  for (const pack of PACKS) {
    for (const mode of MODES) {
      const cls = !pack ? '' : pack.includes('-theme-') ? pack : `cm-theme-${pack}`;
      // data-theme pins the mode deterministically (no OS emulation needed).
      const html = `<!doctype html><html class="${cls}" data-theme="${mode}"><head><meta charset="utf8">`
        + `<style>${bundle}</style></head><body>`
        + `<span id="probe-color"></span>`
        + `<div id="probe-len" style="width:1000px"><div id="probe-len-child"></div></div>`
        + `</body></html>`;
      const page = await browser.newPage({ viewport: { width: VW, height: VH } });
      await page.setContent(html, { waitUntil: 'load' });
      const result = await page.evaluate(PAGE_PROBE, names);
      await page.close();

      const label = `${pack || 'base'}-${mode}`;
      // json
      fs.writeFileSync(path.join(OUT_DIR, `${label}.json`),
        JSON.stringify({ pack: pack || null, mode, viewport: `${VW}x${VH}`, tokens: result }, null, 2) + '\n');
      // flat css (resolved values, hex where colour)
      const sel = `:root${cls ? '.' + cls : ''}[data-theme="${mode}"]`;
      const lines = [
        `/* RUNTIME (computed) theme styles — pack: ${pack || 'base'}, mode: ${mode}`,
        `   Resolved by Chromium at viewport ${VW}x${VH}. color-mix/clamp/var all`,
        `   evaluated; length/clamp values are for this viewport only.`,
        `   Generated by tools/ab-theme-computed.js — do not edit by hand. */`,
        `${sel} {`,
        ...names.map(n => {
          const t = result[n];
          const val = t.type === 'color' ? (toHex(t.resolved) || t.resolved) : t.resolved;
          return `  ${n}: ${val};`;
        }),
        `}`, ''];
      fs.writeFileSync(path.join(OUT_DIR, `${label}.css`), lines.join('\n'));
      const colors = names.filter(n => result[n].type === 'color').length;
      console.log(`✓ ${label}  (${names.length} tokens; ${colors} colour)`);
      index.push(`| ${pack || 'base'} | ${mode} | ${label}.css / .json |`);
    }
  }

  await browser.close();
  fs.writeFileSync(path.join(OUT_DIR, '_index.md'), [
    '# Runtime (computed) theme styles', '',
    `Every \`--ab-*\` token resolved to its real value by headless Chromium, per`,
    `colour theme pack x mode. Unlike \`exports/theme-css/\` (compiled but still`,
    `\`var()\`/\`color-mix()\`/\`clamp()\`), these are the values the browser actually`,
    `computes. **Viewport: ${VW}x${VH}** (length/clamp values are viewport-specific).`, '',
    'Regenerate: `npm run theme-computed` (or `node tools/ab-theme-computed.js`).', '',
    '| pack | mode | files |', '|---|---|---|', ...index, ''].join('\n'));

  console.log(`\nWrote ${PACKS.length * MODES.length * 2} file(s) + _index.md to ${path.relative(ROOT, OUT_DIR)}/`);
}

main().catch(err => { console.error('ab-theme-computed.js failed:', err); process.exit(1); });
