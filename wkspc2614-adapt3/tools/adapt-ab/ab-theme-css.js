#!/usr/bin/env node
/**
 * ab-theme-css.js — compile each adapt-ab-theme LESS file to plain CSS in a
 * visible folder, so you can read the PRODUCED css (what actually ships in
 * build/adapt.css) and see where hardcoded values should become theme-token
 * cascades (as the button set already does).
 *
 *   node tools/ab-theme-css.js            (or: npm run theme-css)
 *
 * Output: exports/theme-css/<file>.css, one per LESS source, plus _index.md
 * listing which selectors still carry raw hex/rem instead of a --ab-* token.
 * exports/ is version-controlled, so the produced CSS is reviewable in git.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

function findRoot(s) { let d = s; for (let i = 0; i < 10; i++) { if (fs.existsSync(path.join(d, 'Gruntfile.js'))) return d; const u = path.dirname(d); if (u === d) break; d = u; } return s; }
const ROOT = findRoot(fs.existsSync(path.join(process.cwd(), 'Gruntfile.js')) ? process.cwd() : __dirname);
const LESS_DIR = path.join(ROOT, 'src', 'extensions', 'adapt-ab-theme', 'less');
const OUT_DIR = path.join(ROOT, 'exports', 'theme-css');

const lessFiles = fs.readdirSync(LESS_DIR).filter(f => f.endsWith('.less')).sort();
fs.mkdirSync(OUT_DIR, { recursive: true });

const rawHexRe = /:\s*#[0-9a-fA-F]{3,8}\b/;   // a literal hex colour in a value (not a --ab-* var)
const summary = [];

for (const f of lessFiles) {
  const inPath = path.join(LESS_DIR, f);
  const outName = f.replace(/\.less$/, '.css');
  const outPath = path.join(OUT_DIR, outName);
  const r = spawnSync('npx', ['lessc', inPath, outPath], { cwd: ROOT, encoding: 'utf8', shell: true });
  if (r.status !== 0) { console.error(`FAIL ${f}:\n${r.stderr}`); summary.push({ f, ok: false, rawHex: 0 }); continue; }
  const css = fs.readFileSync(outPath, 'utf8');
  // count value lines that use a raw hex instead of a token (candidates to tokenise)
  const rawHex = css.split('\n').filter(l => rawHexRe.test(l) && !l.includes('var(')).length;
  summary.push({ f, ok: true, rawHex });
  console.log(`✓ ${outName}  (${css.split('\n').length} lines, ${rawHex} raw-hex value(s))`);
}

// index with the tokenise candidates
const idx = ['# Produced theme CSS', '',
  'Compiled from `src/extensions/adapt-ab-theme/less/*.less`. This is what',
  'ships (concatenated) into `build/adapt.css`. "raw-hex" counts values using a',
  'literal `#hex` instead of a `--ab-*` token — candidates to convert to theme',
  'cascades like the button set.', '',
  '| file | raw-hex values |', '|---|---|',
  ...summary.map(s => `| ${s.f.replace(/\.less$/, '.css')} | ${s.ok ? s.rawHex : 'COMPILE FAIL'} |`)];
fs.writeFileSync(path.join(OUT_DIR, '_index.md'), idx.join('\n') + '\n');

console.log(`\nWrote ${summary.filter(s => s.ok).length} CSS file(s) + _index.md to ${path.relative(ROOT, OUT_DIR)}/`);
