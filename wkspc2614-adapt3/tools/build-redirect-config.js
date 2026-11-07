#!/usr/bin/env node
/**
 * build-redirect-config.js
 *
 * Compiles redirect/links.md (a human-editable markdown source - see that
 * file's own header) into redirect/links.json, the machine-readable config
 * actually fetched at runtime by redirect/redirects-excelling.html.
 *
 * This split exists so a non-technical editor can safely change one word
 * ("Use: Primary" / "Use: Fallback") in a markdown file - flipping every
 * chapter's reference link across every SCORM package at once if the EBSCO
 * database link ever breaks - without touching JSON syntax or any course
 * content.
 *
 * Usage:
 *   node tools/build-redirect-config.js
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SRC = path.join(ROOT, 'redirect', 'links.md');
const OUT = path.join(ROOT, 'redirect', 'links.json');

function parseMarkdown(md) {
  const useMatch = md.match(/^Use:\s*(\S+)/m);
  if (!useMatch) throw new Error('No "Use: Primary" / "Use: Fallback" line found in redirect/links.md');
  const mode = useMatch[1].toLowerCase();
  if (mode !== 'primary' && mode !== 'fallback') {
    throw new Error(`"Use:" line must say Primary or Fallback, found "${useMatch[1]}"`);
  }

  const rows = [];
  const tableLines = md.split('\n').filter(l => l.trim().startsWith('| exc'));
  for (const line of tableLines) {
    const cells = line.split('|').map(c => c.trim()).filter((_, i) => i !== 0); // drop leading empty cell from split
    const [ref, , primary, fallback] = cells;
    if (!ref || !primary || !fallback) throw new Error(`Malformed table row in redirect/links.md: ${line}`);
    rows.push({ ref, primary, fallback });
  }
  if (!rows.length) throw new Error('No link rows found in redirect/links.md - expected rows starting "| exc..."');

  return { mode, rows };
}

function main() {
  const md = fs.readFileSync(SRC, 'utf8');
  const { mode, rows } = parseMarkdown(md);

  const refs = {};
  for (const r of rows) refs[r.ref] = { primary: r.primary, fallback: r.fallback };

  const config = { mode, refs };
  fs.writeFileSync(OUT, JSON.stringify(config, null, 2) + '\n');
  console.log(`Wrote ${OUT}: mode="${mode}", ${rows.length} ref(s).`);
}

main();
