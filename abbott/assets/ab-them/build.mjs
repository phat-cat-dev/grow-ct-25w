#!/usr/bin/env node
// build.mjs — compile a saved theme config into dist/<name>/{theme.css,tokens.json}
//
//   node build.mjs navy
//   node build.mjs            # builds every theme in themes/
//
// KEEP-DYNAMIC: theme.css is emitted whole, with a trailing ingredient
// override block. No colour is flattened.

import { readFile, writeFile, readdir, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { buildTokens } from './src/tokens.js';
import { emitCss } from './src/emit-css.js';
import { emitJson } from './src/emit-json.js';

const ROOT = dirname(fileURLToPath(import.meta.url));
const TEMPLATE = join(ROOT, 'theme.css');

const safe = (s) => /^[a-z0-9_-]+$/i.test(s);

async function buildOne(name, template) {
  if (!safe(name)) throw new Error(`unsafe theme name: ${name}`);
  const cfg = JSON.parse(await readFile(join(ROOT, 'themes', `${name}.json`), 'utf8'));
  const tokens = buildTokens(cfg);
  const outDir = join(ROOT, 'dist', name);
  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, 'theme.css'), emitCss(tokens, template, cfg.customCss, cfg.connectors, cfg.colorSystem, cfg.typography, cfg.spacing, cfg.layout, cfg.cards));
  await writeFile(join(outDir, 'tokens.json'), emitJson(tokens, cfg));
  console.log(`built  dist/${name}/theme.css  +  tokens.json`);
}

const template = await readFile(TEMPLATE, 'utf8');
const arg = process.argv[2];

if (arg) {
  await buildOne(arg, template);
} else {
  const files = (await readdir(join(ROOT, 'themes'))).filter((f) => f.endsWith('.json'));
  if (!files.length) console.log('no themes/*.json found');
  for (const f of files) await buildOne(f.replace(/\.json$/, ''), template);
}
