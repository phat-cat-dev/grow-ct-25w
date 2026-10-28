#!/usr/bin/env node
'use strict';

/**
 * resolve-subject-context.js - a HECoS code, a CAH code (CAH1, CAH2 or
 * CAH3) or a subject name in, its level, code and label out, plus the
 * CAH chain above it.
 *
 * Built: adp-0223, RJ-0099. Proposed for Phase D's DH gate (ADP-9); this
 * file never names that gate or any other consuming project, per TLS-1
 * (tools/subject/README.md: "core/ never reads or names adapt/, ADAPT or
 * any other consuming project").
 *
 * "universal" is handled before either store is read and always returns
 * an unscoped context (scoped: false, code: null, label: null, chain:
 * []), never a blank subject, per the row's own wording.
 *
 * Match order against the two vocabulary stores (core/vocab/cah.json,
 * core/vocab/hecos.json): an exact HECoS code; an exact CAH code at
 * cah3, then cah2, then cah1 (most specific first, the same ordering
 * subject-lookup.js uses); a subject name against a HECoS term or one
 * of its nonPreferredTerms (case-insensitive); a subject name against a
 * CAH label at cah3, then cah2, then cah1 (case-insensitive). A CAH code
 * is matched case-insensitively (input upper-cased before comparison);
 * a HECoS code is digits only, compared as given. An input matching
 * none of these fails by name: the thrown error's message quotes the
 * exact input, so what was not found is never ambiguous.
 *
 * The CAH chain above a HECoS code is its cah3, cah2 and cah1 ancestors
 * in that order (cah3 first, since a HECoS code sits below cah3). The
 * chain above a CAH code is only the levels strictly above it (cah2 and
 * cah1 above a cah3 code; cah1 above a cah2 code; nothing above cah1).
 */

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..', '..', '..', '..');

const DEFAULT_CAH_PATH = path.join(REPO_ROOT, 'tools', 'subject', 'core', 'vocab', 'cah.json');
const DEFAULT_HECOS_PATH = path.join(REPO_ROOT, 'tools', 'subject', 'core', 'vocab', 'hecos.json');

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

/**
 * The CAH entries strictly above level/code. level is 'hecos', 'cah3',
 * 'cah2' or 'cah1'; code is the HECoS term's own cah3 field when level
 * is 'hecos', otherwise the CAH code itself. Returns [] if code is not
 * found at that level, or if level is 'cah1' (nothing is above it).
 */
function ancestorsAbove(cah, level, code) {
  if (level === 'cah1') {
    return [];
  }
  if (level === 'cah2') {
    const c2 = cah.cah2.find((e) => e.code === code);
    if (!c2) return [];
    const c1 = cah.cah1.find((e) => e.code === c2.parent);
    return c1 ? [{ level: 'cah1', code: c1.code, label: c1.label }] : [];
  }
  // level is 'hecos' or 'cah3': code is a cah3 code either way.
  const c3 = cah.cah3.find((e) => e.code === code);
  if (!c3) return [];
  const chain = [];
  if (level === 'hecos') {
    chain.push({ level: 'cah3', code: c3.code, label: c3.label });
  }
  const c2 = cah.cah2.find((e) => e.code === c3.parent);
  if (c2) {
    chain.push({ level: 'cah2', code: c2.code, label: c2.label });
    const c1 = cah.cah1.find((e) => e.code === c2.parent);
    if (c1) {
      chain.push({ level: 'cah1', code: c1.code, label: c1.label });
    }
  }
  return chain;
}

/**
 * The resolver itself. input: a HECoS code, a CAH code, a subject name,
 * or the literal string "universal". Returns
 * { input, level, scoped, code, label, chain }. Throws an Error naming
 * the input if nothing matches. options.cahPath/hecosPath override the
 * default store paths (the fixture tests use this).
 */
function resolveSubjectContext(input, options = {}) {
  if (input === 'universal') {
    return { input, level: 'universal', scoped: false, code: null, label: null, chain: [] };
  }

  const cahPath = options.cahPath || DEFAULT_CAH_PATH;
  const hecosPath = options.hecosPath || DEFAULT_HECOS_PATH;
  const cah = readJson(cahPath);
  const hecos = readJson(hecosPath);

  const raw = String(input).trim();
  const upper = raw.toUpperCase();
  const lower = raw.toLowerCase();

  const hecosByCode = hecos.terms.find((t) => t.code === raw);
  if (hecosByCode) {
    return {
      input,
      level: 'hecos',
      scoped: true,
      code: hecosByCode.code,
      label: hecosByCode.term,
      chain: ancestorsAbove(cah, 'hecos', hecosByCode.cah3),
    };
  }

  for (const level of ['cah3', 'cah2', 'cah1']) {
    const entry = cah[level].find((e) => e.code === upper);
    if (entry) {
      return {
        input,
        level,
        scoped: true,
        code: entry.code,
        label: entry.label,
        chain: ancestorsAbove(cah, level, entry.code),
      };
    }
  }

  const hecosByName = hecos.terms.find(
    (t) =>
      t.term.toLowerCase() === lower ||
      (Array.isArray(t.nonPreferredTerms) && t.nonPreferredTerms.some((n) => n.toLowerCase() === lower))
  );
  if (hecosByName) {
    return {
      input,
      level: 'hecos',
      scoped: true,
      code: hecosByName.code,
      label: hecosByName.term,
      chain: ancestorsAbove(cah, 'hecos', hecosByName.cah3),
    };
  }

  for (const level of ['cah3', 'cah2', 'cah1']) {
    const entry = cah[level].find((e) => e.label.toLowerCase() === lower);
    if (entry) {
      return {
        input,
        level,
        scoped: true,
        code: entry.code,
        label: entry.label,
        chain: ancestorsAbove(cah, level, entry.code),
      };
    }
  }

  throw new Error('Unknown subject code or name: "' + input + '"');
}

module.exports = {
  REPO_ROOT,
  DEFAULT_CAH_PATH,
  DEFAULT_HECOS_PATH,
  readJson,
  ancestorsAbove,
  resolveSubjectContext,
};

if (require.main === module) {
  const input = process.argv[2];
  if (!input) {
    process.stderr.write('Usage: node resolve-subject-context.js <code-or-name-or-universal>\n');
    process.exit(1);
  }
  try {
    const result = resolveSubjectContext(input);
    process.stdout.write(JSON.stringify(result, null, 2) + '\n');
    process.exit(0);
  } catch (err) {
    process.stderr.write(err.message + '\n');
    process.exit(1);
  }
}
