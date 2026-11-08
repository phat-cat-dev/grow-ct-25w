#!/usr/bin/env node
'use strict';

// validate-map.js <map.json>
//
// Validates a benchmark-to-pathway map against source-mapping-rules.md
// section 6 (fields and nesting) and the checks listed in the prompt that
// commissioned this tool (adp-0196). Node.js, no dependencies. Moved into
// the pathways model's core by RJ-0048 (D-0041, D-0044, adp-0213); it still
// names the `adapt-` tag prefix directly below, a purity gap left for
// RJ-0033 (D-0045) to close when pathway tags move to `path-<pathway-id>`.
//
// Exits non-zero and lists every failure on any check failing. Exits 0 and
// prints a short summary when every check passes.

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const CATALOGUE_PATH = path.join(REPO_ROOT, 'catalogue', 'context', 'pathways.json');
const SOURCE_MAP_SCHEMA_PATH = path.join(REPO_ROOT, 'schemas', 'source-map.schema.json');
const PATHWAY_TERM_LISTS_PATH = path.join(REPO_ROOT, 'tools', 'pathways', 'core', 'rules', 'pathway-term-lists.json');
const MAP_INDEX_PATH = path.join(REPO_ROOT, 'tools', 'pathways', 'core', 'mapping', 'index.json');

function readJSON(absPath) {
  const raw = fs.readFileSync(absPath, 'utf8');
  return JSON.parse(raw);
}

function loadCatalogueIds() {
  const catalogue = readJSON(CATALOGUE_PATH);
  return catalogue.pathways.map((p) => p.id);
}

// BM-1's 15 block types are not retyped here: they are read from
// schemas/source-map.schema.json, the one place in the repo that already
// holds them as a machine-readable enum (BM-1, docs/project/open-decisions.md,
// 20 September 2026; the enum there is quoted from BM-1's own ruling text).
function loadBlockTypes() {
  const schema = readJSON(SOURCE_MAP_SCHEMA_PATH);
  return schema.properties.chunks.items.properties.blockType.enum;
}

function loadPathwayTermLists() {
  return readJSON(PATHWAY_TERM_LISTS_PATH);
}

function isPlainObject(v) {
  return v !== null && typeof v === 'object' && !Array.isArray(v);
}

function collapseWhitespace(s) {
  return s.replace(/\s+/g, ' ');
}

function wordCount(s) {
  const trimmed = s.trim();
  if (trimmed === '') return 0;
  return trimmed.split(/\s+/).length;
}

function fail(failures, msg) {
  failures.push(msg);
}

// Check: fields and nesting of source-mapping-rules.md section 6.
function checkShape(map, failures) {
  const topRequired = ['mapVersion', 'rules', 'project', 'tagPrefix', 'source', 'mappedBy', 'agentInstructions', 'coverage', 'pathways', 'excluded'];
  for (const key of topRequired) {
    if (!(key in map)) fail(failures, `shape: missing top-level field "${key}"`);
  }
  if (typeof map.mapVersion !== 'string') fail(failures, 'shape: "mapVersion" must be a string');
  if (typeof map.rules !== 'string') fail(failures, 'shape: "rules" must be a string');
  if (typeof map.project !== 'string') fail(failures, 'shape: "project" must be a string');
  if (typeof map.tagPrefix !== 'string') fail(failures, 'shape: "tagPrefix" must be a string');

  if (isPlainObject(map.source)) {
    const s = map.source;
    for (const key of ['id', 'title', 'issuer', 'year', 'text', 'chunksFile', 'chunks', 'excludedChunks']) {
      if (!(key in s)) fail(failures, `shape: "source" missing field "${key}"`);
    }
    if (typeof s.id !== 'string') fail(failures, 'shape: "source.id" must be a string');
    if (typeof s.title !== 'string') fail(failures, 'shape: "source.title" must be a string');
    if (typeof s.chunks !== 'number') fail(failures, 'shape: "source.chunks" must be a number');
    if (typeof s.excludedChunks !== 'number') fail(failures, 'shape: "source.excludedChunks" must be a number');
    for (const fileField of ['text', 'chunksFile']) {
      if (isPlainObject(s[fileField])) {
        if (typeof s[fileField].file !== 'string') fail(failures, `shape: "source.${fileField}.file" must be a string`);
        if (typeof s[fileField].sha256 !== 'string') fail(failures, `shape: "source.${fileField}.sha256" must be a string`);
      } else {
        fail(failures, `shape: "source.${fileField}" must be an object`);
      }
    }
  } else {
    fail(failures, 'shape: "source" must be an object');
  }

  if (isPlainObject(map.mappedBy)) {
    for (const key of ['agent', 'date', 'sessionRef']) {
      if (typeof map.mappedBy[key] !== 'string') fail(failures, `shape: "mappedBy.${key}" must be a string`);
    }
  } else {
    fail(failures, 'shape: "mappedBy" must be an object');
  }

  if (!Array.isArray(map.agentInstructions)) {
    fail(failures, 'shape: "agentInstructions" must be an array');
  }

  if (!Array.isArray(map.excluded)) {
    fail(failures, 'shape: "excluded" must be an array');
  } else {
    map.excluded.forEach((entry, i) => {
      if (!isPlainObject(entry) || typeof entry.chunkId !== 'string' || typeof entry.reason !== 'string') {
        fail(failures, `shape: "excluded[${i}]" must be an object with string "chunkId" and "reason"`);
      }
    });
  }

  if (!isPlainObject(map.coverage)) fail(failures, 'shape: "coverage" must be an object');
  if (!isPlainObject(map.pathways)) fail(failures, 'shape: "pathways" must be an object');

  if (isPlainObject(map.pathways)) {
    for (const [tag, group] of Object.entries(map.pathways)) {
      if (!isPlainObject(group)) {
        fail(failures, `shape: "pathways.${tag}" must be an object`);
        continue;
      }
      if (!isPlainObject(group.summary)) {
        fail(failures, `shape: "pathways.${tag}.summary" must be an object`);
      } else {
        if (typeof group.summary.text !== 'string') fail(failures, `shape: "pathways.${tag}.summary.text" must be a string`);
        if (!Array.isArray(group.summary.basis)) fail(failures, `shape: "pathways.${tag}.summary.basis" must be an array`);
        if (typeof group.summary.status !== 'string') fail(failures, `shape: "pathways.${tag}.summary.status" must be a string`);
      }
      if (!Array.isArray(group.statements)) {
        fail(failures, `shape: "pathways.${tag}.statements" must be an array`);
        continue;
      }
      group.statements.forEach((st, i) => {
        const loc = `pathways.${tag}.statements[${i}]`;
        const required = ['chunkId', 'locator', 'tag', 'strength', 'extract', 'blockType', 'orientation', 'orientationExtract', 'agentInstruction', 'status'];
        for (const key of required) {
          if (!(key in st)) fail(failures, `shape: "${loc}" missing field "${key}"`);
        }
        if (typeof st.chunkId !== 'string') fail(failures, `shape: "${loc}.chunkId" must be a string`);
        if (typeof st.tag !== 'string') fail(failures, `shape: "${loc}.tag" must be a string`);
        if (typeof st.strength !== 'string') fail(failures, `shape: "${loc}.strength" must be a string`);
        if (typeof st.extract !== 'string') fail(failures, `shape: "${loc}.extract" must be a string`);
        if (typeof st.blockType !== 'string') fail(failures, `shape: "${loc}.blockType" must be a string`);
        if (typeof st.orientation !== 'string') fail(failures, `shape: "${loc}.orientation" must be a string`);
        if (typeof st.orientationExtract !== 'string') fail(failures, `shape: "${loc}.orientationExtract" must be a string`);
        if (typeof st.agentInstruction !== 'string') fail(failures, `shape: "${loc}.agentInstruction" must be a string`);
        if (typeof st.status !== 'string') fail(failures, `shape: "${loc}.status" must be a string`);
        if (isPlainObject(st.locator)) {
          for (const key of ['section', 'paragraphs', 'pages']) {
            if (!(key in st.locator)) fail(failures, `shape: "${loc}.locator" missing field "${key}"`);
          }
        } else {
          fail(failures, `shape: "${loc}.locator" must be an object`);
        }
      });
    }
  }
}

// Check: every tag is "adapt-" plus a catalogue id; coverage lists every
// catalogue pathway exactly once.
function checkTagsAndCoverage(map, catalogueIds, failures) {
  const validTags = new Set(catalogueIds.map((id) => `adapt-${id}`));

  if (isPlainObject(map.pathways)) {
    for (const tag of Object.keys(map.pathways)) {
      if (!validTags.has(tag)) {
        fail(failures, `tag: "pathways" key "${tag}" is not "adapt-" plus a catalogue/context/pathways.json id`);
      }
      const group = map.pathways[tag];
      if (Array.isArray(group && group.statements)) {
        group.statements.forEach((st, i) => {
          if (st.tag !== tag) {
            fail(failures, `tag: pathways.${tag}.statements[${i}].tag ("${st.tag}") does not match its group key ("${tag}")`);
          } else if (!validTags.has(st.tag)) {
            fail(failures, `tag: pathways.${tag}.statements[${i}].tag "${st.tag}" is not "adapt-" plus a catalogue/context/pathways.json id`);
          }
        });
      }
    }
  }

  if (isPlainObject(map.coverage)) {
    const coverageKeys = Object.keys(map.coverage);
    const coverageSet = new Set(coverageKeys);
    for (const id of catalogueIds) {
      const tag = `adapt-${id}`;
      if (!coverageSet.has(tag)) {
        fail(failures, `coverage: missing entry for catalogue pathway "${tag}"`);
      }
    }
    for (const tag of coverageKeys) {
      if (!validTags.has(tag)) {
        fail(failures, `coverage: entry "${tag}" is not a catalogue/context/pathways.json pathway`);
      }
    }
    const seen = new Set();
    for (const tag of coverageKeys) {
      if (seen.has(tag)) fail(failures, `coverage: entry "${tag}" appears more than once`);
      seen.add(tag);
    }
  }
}

// Check: each pathway's coverage counts equal its statements by strength,
// and "none" appears only where there are no statements.
function checkCoverageCounts(map, failures) {
  if (!isPlainObject(map.coverage) || !isPlainObject(map.pathways)) return;
  for (const [tag, coverageValue] of Object.entries(map.coverage)) {
    const group = map.pathways[tag];
    const statements = (group && Array.isArray(group.statements)) ? group.statements : [];
    if (statements.length === 0) {
      if (coverageValue !== 'none') {
        fail(failures, `coverage: "${tag}" has no statements but coverage is not "none"`);
      }
      continue;
    }
    if (coverageValue === 'none') {
      fail(failures, `coverage: "${tag}" has ${statements.length} statement(s) but coverage says "none"`);
      continue;
    }
    if (!isPlainObject(coverageValue) || typeof coverageValue.direct !== 'number' || typeof coverageValue.indirect !== 'number') {
      fail(failures, `coverage: "${tag}" must be "none" or an object with numeric "direct" and "indirect"`);
      continue;
    }
    const actualDirect = statements.filter((s) => s.strength === 'direct').length;
    const actualIndirect = statements.filter((s) => s.strength === 'indirect').length;
    if (coverageValue.direct !== actualDirect) {
      fail(failures, `coverage: "${tag}".direct is ${coverageValue.direct}, statements give ${actualDirect}`);
    }
    if (coverageValue.indirect !== actualIndirect) {
      fail(failures, `coverage: "${tag}".indirect is ${coverageValue.indirect}, statements give ${actualIndirect}`);
    }
  }
}

// Check: every block type is one of BM-1's 15.
function checkBlockTypes(map, blockTypes, failures) {
  if (!isPlainObject(map.pathways)) return;
  const valid = new Set(blockTypes);
  for (const [tag, group] of Object.entries(map.pathways)) {
    if (!Array.isArray(group && group.statements)) continue;
    group.statements.forEach((st, i) => {
      if (!valid.has(st.blockType)) {
        fail(failures, `blockType: pathways.${tag}.statements[${i}].blockType "${st.blockType}" is not one of BM-1's 15 (${blockTypes.join(', ')})`);
      }
    });
  }
}

// Check: every status is "proposed" or "confirmed".
function checkStatuses(map, failures) {
  const validStatus = new Set(['proposed', 'confirmed']);
  if (!isPlainObject(map.pathways)) return;
  for (const [tag, group] of Object.entries(map.pathways)) {
    if (isPlainObject(group.summary) && !validStatus.has(group.summary.status)) {
      fail(failures, `status: pathways.${tag}.summary.status "${group.summary.status}" is not "proposed" or "confirmed"`);
    }
    if (Array.isArray(group.statements)) {
      group.statements.forEach((st, i) => {
        if (!validStatus.has(st.status)) {
          fail(failures, `status: pathways.${tag}.statements[${i}].status "${st.status}" is not "proposed" or "confirmed"`);
        }
      });
    }
  }
}

// Check: every chunkId exists in the chunks file and is not excluded there;
// every extract/orientationExtract is 4 to 25 words and appears verbatim in
// its chunk's text (the source text sliced by the chunk's offsets), compared
// with runs of whitespace collapsed to one space on both sides and nothing
// else changed.
function checkChunksAndExtracts(map, mapDir, failures) {
  if (!isPlainObject(map.source) || !isPlainObject(map.source.chunksFile) || !isPlainObject(map.source.text)) {
    fail(failures, 'chunks: cannot check chunkIds or extracts, "source.chunksFile" or "source.text" missing or malformed');
    return;
  }
  const chunksPath = path.join(REPO_ROOT, map.source.chunksFile.file);
  const textPath = path.join(REPO_ROOT, map.source.text.file);
  let chunks, text;
  try {
    chunks = readJSON(chunksPath);
  } catch (e) {
    fail(failures, `chunks: cannot read chunks file "${map.source.chunksFile.file}" (${e.message})`);
    return;
  }
  try {
    text = fs.readFileSync(textPath, 'utf8');
  } catch (e) {
    fail(failures, `chunks: cannot read source text file "${map.source.text.file}" (${e.message})`);
    return;
  }
  const byId = new Map(chunks.map((c) => [c.chunkId, c]));

  if (!isPlainObject(map.pathways)) return;
  for (const [tag, group] of Object.entries(map.pathways)) {
    if (!Array.isArray(group.statements)) continue;
    group.statements.forEach((st, i) => {
      const loc = `pathways.${tag}.statements[${i}]`;
      const chunk = byId.get(st.chunkId);
      if (!chunk) {
        fail(failures, `chunkId: ${loc}.chunkId "${st.chunkId}" does not exist in the chunks file`);
        return;
      }
      if (chunk.excluded) {
        fail(failures, `chunkId: ${loc}.chunkId "${st.chunkId}" is excluded in the chunks file ("${chunk.excludedReason}")`);
        return;
      }
      const chunkText = text.slice(chunk.start, chunk.end);
      const normalizedChunk = collapseWhitespace(chunkText);
      for (const field of ['extract', 'orientationExtract']) {
        const value = st[field];
        if (typeof value !== 'string') continue;
        const wc = wordCount(value);
        if (wc < 4 || wc > 25) {
          fail(failures, `extract: ${loc}.${field} is ${wc} words, must be 4 to 25`);
        }
        const normalizedExtract = collapseWhitespace(value);
        if (!normalizedChunk.includes(normalizedExtract)) {
          fail(failures, `extract: ${loc}.${field} does not appear verbatim in chunk "${st.chunkId}"'s text`);
        }
      }
    });
  }
}

// Check (QV-TAG-2 part e, adp-0203 unit 5): a statement marked "direct"
// must have an "extract" that matches at least one of its pathway's
// patterns in pathway-term-lists.json. A miss is always recorded as a
// warning (chunkId, pathway, extract); in strict mode it is also added to
// failures, so it changes the exit code.
function checkStrength(map, termLists, strict, failures, warnings) {
  if (!isPlainObject(map.pathways)) return;
  const pathways = (termLists && isPlainObject(termLists.pathways)) ? termLists.pathways : {};
  for (const [tag, group] of Object.entries(map.pathways)) {
    if (!Array.isArray(group.statements)) continue;
    const pathwayId = tag.startsWith('adapt-') ? tag.slice('adapt-'.length) : tag;
    const patterns = Array.isArray(pathways[pathwayId]) ? pathways[pathwayId] : [];
    group.statements.forEach((st, i) => {
      if (st.strength !== 'direct') return;
      const extract = typeof st.extract === 'string' ? st.extract : '';
      const matched = patterns.some((entry) => {
        if (!isPlainObject(entry) || typeof entry.pattern !== 'string') return false;
        try {
          return new RegExp(entry.pattern, entry.flags || '').test(extract);
        } catch (e) {
          return false;
        }
      });
      if (!matched) {
        warnings.push({ chunkId: st.chunkId, tag, extract: st.extract });
        if (strict) {
          fail(failures, `strength: pathways.${tag}.statements[${i}] chunkId "${st.chunkId}" is "direct" but its extract matches no pathway-term-lists.json pattern for "${pathwayId}"`);
        }
      }
    });
  }
}

// Check: the text hash recorded in the map equals the index's sha256 for
// that source.
function checkTextHash(map, failures) {
  if (!isPlainObject(map.source) || !isPlainObject(map.source.text) || typeof map.source.id !== 'string') {
    fail(failures, 'hash: cannot check text hash, "source.id" or "source.text" missing or malformed');
    return;
  }
  const chunksFile = map.source.chunksFile && map.source.chunksFile.file;
  if (typeof chunksFile !== 'string') {
    fail(failures, 'hash: cannot find the index, "source.chunksFile.file" missing or malformed');
    return;
  }
  const indexPath = path.join(REPO_ROOT, path.dirname(chunksFile), 'index.json');
  let index;
  try {
    index = readJSON(indexPath);
  } catch (e) {
    fail(failures, `hash: cannot read index file "${path.dirname(chunksFile)}/index.json" (${e.message})`);
    return;
  }
  const slug = map.source.id.includes('/') ? map.source.id.split('/').slice(1).join('/') : map.source.id;
  const entry = Array.isArray(index) ? index.find((e) => e.slug === slug) : undefined;
  if (!entry) {
    fail(failures, `hash: no index entry for slug "${slug}" (derived from source.id "${map.source.id}")`);
    return;
  }
  if (entry.sha256 !== map.source.text.sha256) {
    fail(failures, `hash: source.text.sha256 "${map.source.text.sha256}" does not equal index's sha256 "${entry.sha256}" for "${slug}"`);
  }
}

// Check (RJ-0028, SRB-1): a pathway summary rests only on chunks that hold
// a statement in that same pathway. Every id in its "summary.basis", and
// every paragraph number cited in its "summary.text", must be the chunkId
// (or within the paragraphs) of a statement in that pathway. A pathway with
// no statements, an empty basis and no citations passes vacuously: this is
// the "no statement" case the mapping rules' step 4 writes as "none".

// Expands one chunk's `locator.paragraphs` string into the set of paragraph
// tokens it covers: a bare paragraph ("3.16") covers itself; a numeric
// range sharing one major number ("3.28-3.32") covers every paragraph in
// between; a repeated-paragraph suffix (DPN-1, for example "1.22-2") covers
// both its own id and the base paragraph it repeats; anything else is kept
// as its own single token.
function expandParagraphs(paragraphStr) {
  const result = new Set();
  if (!paragraphStr) return result;
  if (paragraphStr.includes('-')) {
    const dash = paragraphStr.indexOf('-');
    const start = paragraphStr.slice(0, dash);
    const end = paragraphStr.slice(dash + 1);
    if (/^\d+\.\d+$/.test(start) && /^\d+\.\d+$/.test(end)) {
      const [startMajor, startMinor] = start.split('.');
      const [endMajor, endMinor] = end.split('.');
      if (startMajor === endMajor) {
        for (let i = parseInt(startMinor, 10); i <= parseInt(endMinor, 10); i++) {
          result.add(`${startMajor}.${i}`);
        }
      } else {
        result.add(start);
        result.add(end);
      }
    } else if (/^\d+\.\d+$/.test(start)) {
      result.add(start);
      result.add(paragraphStr);
    } else {
      result.add(paragraphStr);
    }
  } else {
    result.add(paragraphStr);
  }
  return result;
}

// Builds a Map from chunkId to the Set of paragraph tokens that chunk's
// locator covers, from a parsed chunks-file array.
function buildParagraphsByChunkId(chunks) {
  const byId = new Map();
  for (const chunk of chunks) {
    const paragraphs = chunk.locator && chunk.locator.paragraphs;
    byId.set(chunk.chunkId, expandParagraphs(paragraphs));
  }
  return byId;
}

// Extracts every paragraph number a summary.text cites, from parenthetical
// groups. Accepts three forms inside parentheses, the three seen in the
// mapping rules' own example and in committed maps: a single paragraph
// ("3.16"), a comma-separated list ("4.9, 4.10"), and a numeric range
// ("3.28-3.32").
function extractCitedParagraphs(text) {
  const result = new Set();
  const groupRe = /\(([^)]*\d+\.\d+[^)]*)\)/g;
  let groupMatch;
  while ((groupMatch = groupRe.exec(text)) !== null) {
    const parts = groupMatch[1].split(',');
    for (let rawPart of parts) {
      const part = rawPart.trim();
      if (!part) continue;
      if (part.includes('-')) {
        const dash = part.indexOf('-');
        const start = part.slice(0, dash).trim();
        const end = part.slice(dash + 1).trim();
        if (/^\d+\.\d+$/.test(start) && /^\d+\.\d+$/.test(end)) {
          const [startMajor, startMinor] = start.split('.');
          const [endMajor, endMinor] = end.split('.');
          if (startMajor === endMajor) {
            for (let i = parseInt(startMinor, 10); i <= parseInt(endMinor, 10); i++) {
              result.add(`${startMajor}.${i}`);
            }
          } else {
            result.add(start);
            result.add(end);
          }
        } else if (/^\d+\.\d+$/.test(start)) {
          result.add(start);
        }
      } else if (/^\d+\.\d+$/.test(part)) {
        result.add(part);
      }
    }
  }
  return result;
}

// Loads the chunks file a map declares at "source.chunksFile.file",
// relative to the repo root. Returns null if it cannot be read or parsed,
// so the caller records its own failure rather than throwing.
function loadMapChunks(map) {
  if (!isPlainObject(map.source) || !isPlainObject(map.source.chunksFile) || typeof map.source.chunksFile.file !== 'string') {
    return null;
  }
  try {
    return readJSON(path.join(REPO_ROOT, map.source.chunksFile.file));
  } catch (e) {
    return null;
  }
}

function checkSummaryBasis(map, paragraphsByChunkId, failures) {
  if (!isPlainObject(map.pathways)) return;
  for (const [tag, group] of Object.entries(map.pathways)) {
    const statements = Array.isArray(group.statements) ? group.statements : [];
    const stmtChunkIds = new Set(statements.map((s) => s.chunkId));
    const pathwayParas = new Set();
    for (const cid of stmtChunkIds) {
      const paras = paragraphsByChunkId.get(cid);
      if (paras) for (const p of paras) pathwayParas.add(p);
    }
    const summary = isPlainObject(group.summary) ? group.summary : {};
    const basis = Array.isArray(summary.basis) ? summary.basis : [];
    for (const b of basis) {
      if (!stmtChunkIds.has(b)) {
        fail(failures, `summary: pathways.${tag}.summary.basis "${b}" is not the chunkId of a statement in pathway "${tag}"`);
      }
    }
    const text = typeof summary.text === 'string' ? summary.text : '';
    const cited = extractCitedParagraphs(text);
    for (const p of cited) {
      if (!pathwayParas.has(p)) {
        fail(failures, `summary: pathways.${tag}.summary.text cites paragraph "${p}" which no statement in pathway "${tag}" holds`);
      }
    }
  }
}

// Check: a map with no statements at all fails, whatever its coverage says.
function checkNotEmpty(map, failures) {
  if (!isPlainObject(map.pathways)) return;
  let total = 0;
  for (const group of Object.values(map.pathways)) {
    if (Array.isArray(group && group.statements)) total += group.statements.length;
  }
  if (total === 0) {
    fail(failures, 'empty: the map holds no statements at all');
  }
}

// Runs every check against one already-loaded map. Never reads argv, never
// calls process.exit: returns { failures, warnings } so both the single-file
// CLI path and the --index path can share exactly the same check sequence.
function validateLoadedMap(map, mapPath, strict) {
  const failures = [];
  checkShape(map, failures);

  let catalogueIds = [];
  try {
    catalogueIds = loadCatalogueIds();
  } catch (e) {
    fail(failures, `catalogue: cannot read catalogue/context/pathways.json (${e.message})`);
  }
  if (catalogueIds.length) checkTagsAndCoverage(map, catalogueIds, failures);

  checkCoverageCounts(map, failures);

  let blockTypes = [];
  try {
    blockTypes = loadBlockTypes();
  } catch (e) {
    fail(failures, `blockType: cannot read schemas/source-map.schema.json (${e.message})`);
  }
  if (blockTypes.length) checkBlockTypes(map, blockTypes, failures);

  checkStatuses(map, failures);
  checkChunksAndExtracts(map, path.dirname(mapPath), failures);

  const mapChunks = loadMapChunks(map);
  if (mapChunks) {
    checkSummaryBasis(map, buildParagraphsByChunkId(mapChunks), failures);
  } else {
    fail(failures, 'summary: cannot check summary basis/citations, chunks file missing or malformed');
  }

  checkTextHash(map, failures);
  checkNotEmpty(map, failures);

  const warnings = [];
  let termLists;
  try {
    termLists = loadPathwayTermLists();
  } catch (e) {
    fail(failures, `strength: cannot read pathway-term-lists.json (${e.message})`);
  }
  if (termLists) checkStrength(map, termLists, strict, failures, warnings);

  return { failures, warnings };
}

// Single-file CLI path: validate-map.js <map.json> [--strict]. Behaviour
// (messages, exit codes) is unchanged from before --index existed.
function runSingleFile(mapArg, strict) {
  const mapPath = path.resolve(mapArg);
  let map;
  try {
    map = readJSON(mapPath);
  } catch (e) {
    console.error(`FATAL: cannot read or parse "${mapArg}": ${e.message}`);
    process.exit(1);
  }

  const { failures, warnings } = validateLoadedMap(map, mapPath, strict);

  if (warnings.length > 0) {
    console.log(`WARN: ${warnings.length} strength warning(s) (a "direct" extract matches no pathway-term-lists.json pattern):`);
    for (const w of warnings) {
      console.log(`- chunkId="${w.chunkId}" pathway="${w.tag}" extract="${w.extract}"`);
    }
  }

  if (failures.length > 0) {
    console.error(`FAIL: ${failures.length} failure(s) in ${mapArg}\n`);
    for (const f of failures) console.error(`- ${f}`);
    process.exit(1);
  }

  console.log(`OK: ${mapArg} passes all checks.`);
  process.exit(0);
}

// --index [<index.json>] path: reads a map index (RJ-0046 point 2), skips
// every entry whose status is not "active", and runs the same checks as the
// single-file path against each active map in turn. A map index with zero
// active entries is a FAIL, never a silent pass: an empty or all-superseded
// index must not be reported as "every map passes" when no map was checked.
function runIndex(indexArg, strict) {
  const indexPath = indexArg ? path.resolve(indexArg) : MAP_INDEX_PATH;
  let entries;
  try {
    entries = readJSON(indexPath);
  } catch (e) {
    console.error(`FATAL: cannot read or parse map index "${indexArg || indexPath}": ${e.message}`);
    process.exit(1);
  }
  if (!Array.isArray(entries)) {
    console.error(`FATAL: map index "${indexArg || indexPath}" is not a JSON array`);
    process.exit(1);
  }

  const mapDir = path.dirname(indexPath);
  const active = entries.filter((e) => e.status === 'active');
  const skipped = entries.filter((e) => e.status !== 'active');

  if (active.length === 0) {
    console.error(
      `FAIL: 0 active maps in ${indexArg || indexPath} (${entries.length} total, ${skipped.length} not active); nothing was validated.`
    );
    for (const e of skipped) {
      console.error(`- skipped: slug="${e.slug}" status="${e.status}"`);
    }
    process.exit(1);
  }

  let totalFailures = 0;
  let totalWarnings = 0;
  for (const entry of active) {
    const mapPath = path.resolve(mapDir, entry.file);
    let map;
    try {
      map = readJSON(mapPath);
    } catch (e) {
      console.error(`FAIL: cannot read or parse "${entry.file}" (slug="${entry.slug}"): ${e.message}`);
      totalFailures += 1;
      continue;
    }
    const { failures, warnings } = validateLoadedMap(map, mapPath, strict);
    totalWarnings += warnings.length;
    if (warnings.length > 0) {
      console.log(`WARN: ${warnings.length} strength warning(s) in ${entry.file}:`);
      for (const w of warnings) {
        console.log(`- chunkId="${w.chunkId}" pathway="${w.tag}" extract="${w.extract}"`);
      }
    }
    if (failures.length > 0) {
      console.error(`FAIL: ${failures.length} failure(s) in ${entry.file}\n`);
      for (const f of failures) console.error(`- ${f}`);
      totalFailures += failures.length;
    } else {
      console.log(`OK: ${entry.file} passes all checks.`);
    }
  }

  if (skipped.length > 0) {
    console.log(`SKIPPED: ${skipped.length} non-active map(s) (not validated):`);
    for (const e of skipped) {
      console.log(`- slug="${e.slug}" status="${e.status}"`);
    }
  }

  if (totalFailures > 0) {
    console.error(`FAIL: ${totalFailures} failure(s) across ${active.length} active map(s).`);
    process.exit(1);
  }

  console.log(`OK: ${active.length} active map(s) pass all checks (${skipped.length} skipped).`);
  process.exit(0);
}

function main() {
  const args = process.argv.slice(2);
  const strict = args.includes('--strict');
  const indexFlagIndex = args.indexOf('--index');

  if (indexFlagIndex !== -1) {
    const next = args[indexFlagIndex + 1];
    const indexArg = next && next !== '--strict' ? next : null;
    runIndex(indexArg, strict);
    return;
  }

  const mapArg = args.find((a) => a !== '--strict');
  if (!mapArg) {
    console.error('Usage: validate-map.js <map.json> [--strict]');
    console.error('       validate-map.js --index [<index.json>] [--strict]');
    process.exit(2);
  }
  runSingleFile(mapArg, strict);
}

if (require.main === module) {
  main();
}

module.exports = {
  checkShape,
  checkTagsAndCoverage,
  checkCoverageCounts,
  checkBlockTypes,
  checkStatuses,
  checkChunksAndExtracts,
  checkStrength,
  checkTextHash,
  checkNotEmpty,
  expandParagraphs,
  buildParagraphsByChunkId,
  extractCitedParagraphs,
  loadMapChunks,
  checkSummaryBasis,
  validateLoadedMap,
  MAP_INDEX_PATH,
  loadCatalogueIds,
  loadBlockTypes,
  loadPathwayTermLists,
  collapseWhitespace,
  wordCount,
  REPO_ROOT,
};
