#!/usr/bin/env node
/**
 * ab-resolve-tokens.js — resolve the L3 --ab-base-* pivot tokens through the
 * fold output, optionally with an L6 user-theme profile layered on, to SEE what a
 * build actually renders (the thing lessc alone cannot show — it passes var()
 * through without resolving it).
 *
 *   node tools/ab-resolve-tokens.js                         # pure L4 defaults
 *   node tools/ab-resolve-tokens.js <l6-profile.less>       # with a user-theme profile
 *   node tools/ab-resolve-tokens.js <l6-profile.less> --dark # dark-mode context
 *
 * It concatenates exports/ab-fold/ab-base-pf-default.less (L4) + the optional L6
 * profile + exports/ab-fold/ab-base-pivot.less (L3), compiles with lessc, then
 * resolves the CSS custom-property cascade (balanced-paren var(), last-wins,
 * dropping the dark block unless --dark) and prints the resolved value of each
 * --ab-base-* role token. Proves the L4 -> L5 -> L6 round-trip:
 * a user theme overrides what it sets; everything else inherits the L4 default.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const os = require('os');
const { spawnSync } = require('child_process');

function findRoot(s) { let d = s; for (let i = 0; i < 10; i++) { if (fs.existsSync(path.join(d, 'Gruntfile.js'))) return d; const u = path.dirname(d); if (u === d) break; d = u; } return s; }
const ROOT = findRoot(fs.existsSync(path.join(process.cwd(), 'Gruntfile.js')) ? process.cwd() : __dirname);
const FOLD = path.join(ROOT, 'exports', 'ab-fold');

const args = process.argv.slice(2);
const dark = args.includes('--dark');
const l6 = args.find(a => !a.startsWith('--'));

const parts = [path.join(FOLD, 'ab-base-pf-default.less')];
if (l6) parts.push(path.resolve(l6));
parts.push(path.join(FOLD, 'ab-base-pivot.less'));

const srcLess = parts.map(p => fs.readFileSync(p, 'utf8')).join('\n');
const tmpLess = path.join(os.tmpdir(), `ab-resolve-${process.pid}.less`);
const tmpCss = path.join(os.tmpdir(), `ab-resolve-${process.pid}.css`);
fs.writeFileSync(tmpLess, srcLess);
const r = spawnSync('npx', ['lessc', tmpLess, tmpCss], { cwd: ROOT, encoding: 'utf8', shell: true });
if (r.status !== 0) { console.error('lessc failed:\n' + r.stderr); process.exit(1); }

let css = fs.readFileSync(tmpCss, 'utf8');
if (!dark) css = css.replace(/:root\[data-theme="dark"\][^{]*\{[^}]*\}/g, '');

const map = {};
for (const m of css.matchAll(/(--[\w-]+)\s*:\s*([^;]+);/g)) map[m[1]] = m[2].trim();

function firstVar(s) { const i = s.indexOf('var('); if (i < 0) return null; let d = 0, j = i + 3; for (; j < s.length; j++) { if (s[j] === '(') d++; else if (s[j] === ')') { d--; if (d === 0) break; } } return { i, j, inner: s.slice(i + 4, j) }; }
function splitTop(s) { let d = 0; for (let k = 0; k < s.length; k++) { if (s[k] === '(') d++; else if (s[k] === ')') d--; else if (s[k] === ',' && d === 0) return [s.slice(0, k).trim(), s.slice(k + 1).trim()]; } return [s.trim(), undefined]; }
function resolve(s, depth) { if (depth > 40) return s; let v; while ((v = firstVar(s))) { const [name, fb] = splitTop(v.inner); let rep; if (map[name] !== undefined && map[name] !== '') rep = resolve(map[name], depth + 1); else rep = fb !== undefined ? resolve(fb, depth + 1) : ''; s = s.slice(0, v.i) + rep + s.slice(v.j + 1); } return s; }

const tokens = Object.keys(map).filter(k => /^--ab-base-[a-z]/.test(k) && !k.startsWith('--ab-base-pf-')).sort();
console.log(`context: ${dark ? 'dark' : 'light/default'}${l6 ? `, profile: ${path.basename(l6)}` : ', no user theme (pure L4 defaults)'}`);
for (const t of tokens) console.log('  ' + t.padEnd(28) + ' = ' + resolve(map[t], 0));
fs.unlinkSync(tmpLess); fs.unlinkSync(tmpCss);
