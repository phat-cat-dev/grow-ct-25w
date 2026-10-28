/**
 * voice-lint.js
 *
 * Mechanical voice-compliance check (P9). Scans a course's JSON content
 * for hard-fail, pattern-matchable violations from
 * reference/excelling-voice-specification.md. Deliberately does NOT
 * check anything needing component-type/structural context (Oxford
 * comma, bold-in-running-prose, contractions-in-formal-content) or
 * whole-document statistics (sentence-length average, active/passive
 * ratio); those are out of scope for v1, not attempted even
 * approximately.
 *
 * Usage:
 *   node voice-lint.js --course=<course-slug>
 *   node voice-lint.js --file=<path>
 *
 * --course scans every *.json file under courses/<course-slug>/en/.
 * --file lints a single JSON file the same way: the file is parsed and
 * walked exactly as --course walks each of its files, and only the
 * authored-prose string leaves that survive are linted. Neither mode
 * ever lints raw JSON text directly (PR-S-32, fixed 18 Sep 2026,
 * Prompt 70) - doing so exposed rule checks to JSON syntax (a field's
 * own opening quote swallowing a sentence-initial "There is", and the
 * file's opening brace/first key being counted as prose) in both
 * directions on the same file. A run that matches no files, or that
 * matches files but extracts no prose from them, is a FAIL, not a PASS
 * (PR-S-30, fixed the same prompt) - the two are reported with
 * distinct messages so it's clear which condition produced the FAIL.
 *
 * Exits non-zero if any hard-fail violation is found, or if there was
 * nothing to check.
 */

const fs = require('fs-extra');
const path = require('path');
const { resolveCourse } = require('./tools/lib/course-resolve');

const ROOT = __dirname;

const acceptedArgs = ['course', 'file'];
const argumentValues = { course: null, file: null };

function parseArgs() {
  process.argv.slice(2).forEach(param => {
    const parts = param.replace(/^--/, '').split('=');
    if (!acceptedArgs.includes(parts[0])) {
      console.error(`Unrecognised argument: --${parts[0]}. Accepted: ${acceptedArgs.join(', ')}`);
      process.exit(1);
    }
    argumentValues[parts[0]] = parts[1];
  });
  if (!argumentValues.course && !argumentValues.file) {
    console.error('Usage: node voice-lint.js --course=<course-slug>');
    console.error('       node voice-lint.js --file=<path>');
    process.exit(1);
  }
  if (argumentValues.course && argumentValues.file) {
    console.error('Error: specify either --course or --file, not both.');
    process.exit(1);
  }
}

// --- Keys that are structural, not prose. Never checked. ---
const EXCLUDED_KEYS = new Set([
  '_id', '_parentId', '_type', '_component', '_classes', '_layout',
  'src', 'srcHover', 'srcVisited', '_graphic', '_pin', '_left', '_top',
  '_isEnabled', '_isOptional', '_setCompletionOn', 'context', 'lesson',
  'pathwayTier', '_templateFor',
  // '_flag' is a context-pack authoring/provenance note (e.g. "CONSTRUCTED
  // CONTENT - no book-sourced worked example exists..."), never delivered
  // to a student. Built course JSON never carries it, which is why this
  // wasn't already here; --file mode linting context packs directly
  // (PR-S-32 fix, Prompt 70) reaches it for the first time. Confirmed at
  // content/context-packs/baseline/academic-writing-introductory/
  // understanding-the-task.json:8.
  '_flag'
]);

// --- Rule data, from reference/excelling-voice-specification.md ---

const AMERICAN_TO_BRITISH = {
  'organized': 'organised', 'organize': 'organise', 'organizing': 'organising',
  'recognized': 'recognised', 'recognize': 'recognise', 'recognizing': 'recognising',
  'behavior': 'behaviour', 'behaviors': 'behaviours',
  'color': 'colour', 'colors': 'colours',
  'center': 'centre', 'centers': 'centres', 'centered': 'centred',
  'analyze': 'analyse', 'analyzing': 'analysing', 'analyzed': 'analysed',
  'utilize': 'utilise', 'utilizing': 'utilising', 'utilized': 'utilised',
  'favor': 'favour', 'favorite': 'favourite',
  'labor': 'labour', 'honor': 'honour',
  'defense': 'defence', 'offense': 'offence',
  'traveled': 'travelled', 'traveling': 'travelling',
  'modeling': 'modelling', 'modeled': 'modelled'
};

const BANNED_PHRASES = [
  'it is important to note that', 'it is worth remembering that',
  'as we can see', "in today's academic environment",
  'in this section, we will explore', "let's dive in", "let's unpack",
  'great work!', "you're doing brilliantly!", 'excellent job!',
  'moving on to', "now let's look at", 'last but not least',
  'to summarise the above', 'without further ado',
  'henceforth', 'notwithstanding', 'aforementioned',
  'students should', 'the learner', 'one might'
];

const HARD_SENTENCE_WORD_LIMIT = 45;
const LONG_SENTENCE_THRESHOLD = 30;
const MAX_CONSECUTIVE_LONG_SENTENCES = 2;

// Openers permitted to begin with "There is/are". The spec at §15.3
// explicitly endorses "no right or wrong answers" for reflective prompts,
// so the one idiomatic construction the spec itself asks authors to write
// must not be flagged by the §15.1-derived "There is/are" opener rule
// (which spec §125 states only as "avoid where a more direct construction
// is available", not an outright ban). Added 4 October 2026, found via
// referencing-introductory components[6]'s false positive.
const THERE_IS_ARE_ALLOWED = [
  /^there (is|are) no right (or|and) wrong answers?\b/i
];

function stripHtml(str) {
  return str.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
}

function splitSentences(text) {
  return text.split(/(?<=[.!?;])\s+/).filter(s => s.trim().length > 0);
}

function splitBlockElements(html) {
  // Split on closing block-level tags so text from different HTML
  // elements (e.g. an intro <p> followed by a <blockquote>) is never
  // treated as one continuous sentence. Inline tags (em, strong) are
  // NOT split on, so text within one element still flows normally.
  // Confirmed 22 July 2026, found via component[39]'s false positive.
  return html
    .split(/<\/(p|blockquote|li|h[1-6])>/i)
    .filter((chunk, i) => i % 2 === 0)
    .map(chunk => chunk.trim())
    .filter(chunk => chunk.length > 0);
}

function checkText(text, location, violations) {
  const fragments = splitBlockElements(text);
  fragments.forEach((fragment, fragIndex) => {
    const plain = stripHtml(fragment);
    if (!plain) return;
    checkFragment(plain, fragIndex === 0 ? location : location + ' (fragment ' + (fragIndex + 1) + ')', violations);
  });
}

function checkFragment(plain, location, violations) {
  if (plain.includes('\u2014')) {
    violations.push({ location, rule: 'em-dash', detail: 'Contains an em dash' });
  }

  for (const [american, british] of Object.entries(AMERICAN_TO_BRITISH)) {
    const re = new RegExp(`\\b${american}\\b`, 'i');
    if (re.test(plain)) {
      violations.push({ location, rule: 'american-spelling', detail: `Found "${american}", expected British "${british}"` });
    }
  }

  const lower = plain.toLowerCase();
  for (const phrase of BANNED_PHRASES) {
    if (lower.includes(phrase)) {
      violations.push({ location, rule: 'banned-phrase', detail: `Found banned phrase: "${phrase}"` });
    }
  }

  const sentences = splitSentences(plain);
  let consecutiveLong = 0;
  sentences.forEach((s, i) => {
    const trimmed = s.trim();
    if (/^there (is|are)\b/i.test(trimmed) && !THERE_IS_ARE_ALLOWED.some(re => re.test(trimmed))) {
      violations.push({ location, rule: 'there-is-are-opener', detail: `Sentence ${i + 1} starts with "There is/are": "${trimmed.slice(0, 60)}..."` });
    }

    const wordCount = trimmed.split(/\s+/).length;
    if (wordCount > HARD_SENTENCE_WORD_LIMIT) {
      violations.push({ location, rule: 'sentence-too-long', detail: `Sentence ${i + 1} has ${wordCount} words (limit ${HARD_SENTENCE_WORD_LIMIT}): "${trimmed.slice(0, 60)}..."` });
    }
    if (wordCount >= LONG_SENTENCE_THRESHOLD) {
      consecutiveLong++;
      if (consecutiveLong > MAX_CONSECUTIVE_LONG_SENTENCES) {
        violations.push({ location, rule: 'consecutive-long-sentences', detail: `3+ consecutive sentences of ${LONG_SENTENCE_THRESHOLD}+ words each, ending at sentence ${i + 1}` });
      }
    } else {
      consecutiveLong = 0;
    }
  });
}

function walkJson(obj, pathParts, fileName, violations, stats) {
  if (typeof obj === 'string') {
    // Skip merge placeholders — these are replaced by pack content before packaging
    if (obj.startsWith('[UNMERGED:')) {
      stats.placeholdersSkipped++;
      return;
    }
    stats.fieldsChecked++;
    checkText(obj, fileName + ' > ' + pathParts.join(' > '), violations);
  } else if (Array.isArray(obj)) {
    obj.forEach((item, i) => walkJson(item, [...pathParts, '[' + i + ']'], fileName, violations, stats));
  } else if (obj && typeof obj === 'object') {
    const isIgnored = obj._voiceLintIgnore === true;
    if (isIgnored) {
      const reason = obj._voiceLintReason;
      if (!reason || typeof reason !== 'string' || reason.trim().length === 0) {
        violations.push({
          location: fileName + ' > ' + pathParts.join(' > '),
          rule: 'missing-ignore-reason',
          detail: '_voiceLintIgnore is true but _voiceLintReason is missing or empty'
        });
      }
    }
    for (const [key, value] of Object.entries(obj)) {
      if (EXCLUDED_KEYS.has(key)) continue;
      if (key === '_voiceLintIgnore' || key === '_voiceLintReason') continue;
      if (isIgnored && typeof value === 'string') continue;
      walkJson(value, [...pathParts, key], fileName, violations, stats);
    }
  }
}

async function lintJsonFile(filePath) {
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    process.exit(1);
  }

  const content = await fs.readFile(filePath, 'utf8');
  const fileName = path.basename(filePath);

  let json;
  try {
    json = JSON.parse(content);
  } catch (err) {
    // PR-S-32: --file mode lints authored prose extracted from parsed
    // JSON, never raw file text. A file that doesn't parse has nothing
    // to extract from, so this is reported directly rather than falling
    // back to linting the unparsed text (which is the exact fault fixed
    // here).
    console.error(`voice-lint: FAIL. ${fileName} is not valid JSON: ${err.message}`);
    console.error('--file mode extracts authored prose from parsed JSON and cannot lint a file it cannot parse.');
    process.exit(1);
  }

  const violations = [];
  const stats = { placeholdersSkipped: 0, fieldsChecked: 0 };
  walkJson(json, [], fileName, violations, stats);

  return { violations, stats, fileName };
}

async function main() {
  parseArgs();
  const { course, file } = argumentValues;

  // --file mode: parse a single JSON file and lint the authored prose
  // extracted from it (PR-S-32 - never the raw file text).
  if (file) {
    const { violations, stats, fileName } = await lintJsonFile(file);

    // PR-S-30: a file that parsed but yielded no authored-prose string
    // leaves to check is a FAIL, distinct from "file not found" (handled
    // in lintJsonFile) and distinct from a real pass below.
    if (stats.fieldsChecked === 0) {
      console.error(`voice-lint: FAIL. ${fileName} matched but contained 0 authored-prose fields to check after exclusion/placeholder filtering. Nothing was checked; this is not a pass.`);
      process.exit(1);
    }

    if (violations.length === 0) {
      console.log(`voice-lint: PASS. No hard-fail violations found in ${fileName} (${stats.fieldsChecked} field${stats.fieldsChecked === 1 ? '' : 's'} checked).`);
      process.exit(0);
    }

    console.error(`voice-lint: FAIL. ${violations.length} violation(s) found:\n`);
    violations.forEach(v => {
      console.error(`  [${v.rule}] ${v.location}\n    ${v.detail}\n`);
    });
    process.exit(1);
  }

  // --course mode: lint all JSON files in a course
  // Try shell course first, then generated output
  const resolved = resolveCourse(course, ['courses', 'courses/_generated']);
  resolved.warnings.forEach(w => console.error(`WARNING: ${w}`));

  const enDir = resolved.enDir;
  if (!enDir) {
    console.error(`No course content found at either:`);
    resolved.checked.forEach(d => console.error(`  ${path.join(d, 'en')}`));
    process.exit(1);
  }

  const files = (await fs.readdir(enDir)).filter(f => f.endsWith('.json'));

  // PR-S-30: zero matched files is a FAIL, never the PASS it used to be.
  // Reported before the (necessarily empty) violations loop runs, with a
  // message distinct from the "matched files, extracted nothing" case
  // below, so the two zero-subject conditions aren't conflated.
  if (files.length === 0) {
    console.error(`voice-lint: FAIL. No .json files found under ${enDir}. 0 files matched; nothing was checked. This is not a pass.`);
    process.exit(1);
  }

  const violations = [];
  const stats = { placeholdersSkipped: 0, fieldsChecked: 0 };

  for (const f of files) {
    const json = await fs.readJson(path.join(enDir, f));
    walkJson(json, [], f, violations, stats);
  }

  // PR-S-30: files matched, but nothing survived exclusion/placeholder
  // filtering to actually check. Also a FAIL, and also distinct from the
  // zero-files case above.
  if (stats.fieldsChecked === 0) {
    console.error(`voice-lint: FAIL. ${files.length} file(s) matched under ${enDir} but contained 0 authored-prose fields to check after exclusion/placeholder filtering. Nothing was checked; this is not a pass.`);
    process.exit(1);
  }

  const skipNote = stats.placeholdersSkipped > 0
    ? ` (${stats.placeholdersSkipped} merge placeholder${stats.placeholdersSkipped === 1 ? '' : 's'} skipped)`
    : '';

  if (violations.length === 0) {
    console.log(`voice-lint: PASS. No hard-fail violations found across ${files.length} files (${stats.fieldsChecked} fields checked).${skipNote}`);
    process.exit(0);
  }

  console.error(`voice-lint: FAIL. ${violations.length} violation(s) found:\n`);
  violations.forEach(v => {
    console.error(`  [${v.rule}] ${v.location}\n    ${v.detail}\n`);
  });
  process.exit(1);
}

main().catch(err => {
  console.error('voice-lint.js failed:', err);
  process.exit(1);
});
