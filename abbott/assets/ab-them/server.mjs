#!/usr/bin/env node
// server.mjs — AB Theme Studio dev server.
//
//   npm install && npm start   →   http://localhost:5173
//
// Serves the HSL tuner (editor) at /, the cheat-sheet at /cheatsheet.html, the
// live theme.css at /theme.css, and a tiny JSON API to list / load / save theme
// configs and build them. KEEP-DYNAMIC: build emits theme.css + a trailing
// ingredient override; nothing is flattened.

import express from 'express';
import { readFile, writeFile, readdir, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { buildTokens } from './src/tokens.js';
import { emitCss } from './src/emit-css.js';
import { emitJson } from './src/emit-json.js';

const ROOT = dirname(fileURLToPath(import.meta.url));
const safe = (s) => /^[a-z0-9_-]+$/i.test(s);
const themePath = (n) => join(ROOT, 'themes', `${n}.json`);

const app = express();
app.use(express.json());
app.use(express.static(join(ROOT, 'public')));
app.use('/dist', express.static(join(ROOT, 'dist')));

// the live design system, served from the project root
app.get('/theme.css', async (_req, res) => {
  res.type('css').send(await readFile(join(ROOT, 'theme.css'), 'utf8'));
});

// list saved themes
app.get('/api/themes', async (_req, res) => {
  const files = (await readdir(join(ROOT, 'themes'))).filter((f) => f.endsWith('.json'));
  res.json(files.map((f) => f.replace(/\.json$/, '')));
});

// load one config
app.get('/api/themes/:name', async (req, res) => {
  if (!safe(req.params.name)) return res.status(400).json({ error: 'bad name' });
  try {
    res.json(JSON.parse(await readFile(themePath(req.params.name), 'utf8')));
  } catch {
    res.status(404).json({ error: 'not found' });
  }
});

// save a config (POST the tuner's current knobs here)
app.post('/api/themes/:name', async (req, res) => {
  if (!safe(req.params.name)) return res.status(400).json({ error: 'bad name' });
  const cfg = { name: req.params.name, ...req.body };
  await writeFile(themePath(req.params.name), JSON.stringify(cfg, null, 2) + '\n');
  res.json({ ok: true });
});

// build a config → dist/<name>/{theme.css,tokens.json}
app.post('/api/build/:name', async (req, res) => {
  if (!safe(req.params.name)) return res.status(400).json({ error: 'bad name' });
  try {
    const cfg = JSON.parse(await readFile(themePath(req.params.name), 'utf8'));
    const tokens = buildTokens(cfg);
    const outDir = join(ROOT, 'dist', req.params.name);
    await mkdir(outDir, { recursive: true });
    const template = await readFile(join(ROOT, 'theme.css'), 'utf8');
    await writeFile(join(outDir, 'theme.css'), emitCss(tokens, template, cfg.customCss, cfg.connectors, cfg.colorSystem, cfg.typography, cfg.spacing, cfg.layout, cfg.cards));
    await writeFile(join(outDir, 'tokens.json'), emitJson(tokens, cfg));
    res.json({ ok: true, out: `dist/${req.params.name}` });
  } catch (e) {
    res.status(400).json({ error: String(e) });
  }
});

const PORT = process.env.PORT || 5173;
app.listen(PORT, () => {
  console.log(`AB Theme Studio  →  http://localhost:${PORT}`);
  console.log(`  editor      /           (HSL tuner)`);
  console.log(`  cheat-sheet /cheatsheet.html`);
  console.log(`  system      /theme.css`);
});
