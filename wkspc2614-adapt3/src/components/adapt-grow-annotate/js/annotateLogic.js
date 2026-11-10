/**
 * annotateLogic.js — pure logic for the annotate component (no DOM/Backbone).
 *
 * Two jobs:
 *  1. Parse an author passage into renderable segments. Targets (the words the
 *     learner can annotate) are written in double brackets: `[[word]]`, or with
 *     an explicit stable key `[[word|key]]`. Everything else is plain text.
 *  2. Hold the annotation state — a map of target key -> tool id — with the
 *     apply/toggle rule, a completion predicate, and (de)serialisation for
 *     persistence.
 *
 * All unit-tested; the view and model stay thin wrappers over this.
 */

const TARGET_RE = /\[\[([^\]]*?)\]\]/g;

/**
 * Parse a passage string into segments.
 * @param {string} input
 * @returns {{segments: Array<{type:'text', text:string}|{type:'target', text:string, key:string}>, keys: string[]}}
 */
export function parsePassage(input) {
  const text = String(input == null ? '' : input);
  const segments = [];
  const keys = [];
  let targetIndex = 0;
  let last = 0;
  let match;

  TARGET_RE.lastIndex = 0;
  while ((match = TARGET_RE.exec(text)) !== null) {
    if (match.index > last) {
      segments.push({ type: 'text', text: text.slice(last, match.index) });
    }
    const [rawText, rawKey] = match[1].split('|');
    const label = (rawText || '').trim();
    if (!label) {
      // [[]] or [[|k]] with no text — keep the literal so nothing silently vanishes
      segments.push({ type: 'text', text: match[0] });
    } else {
      const key = rawKey && rawKey.trim() ? rawKey.trim() : `t${targetIndex}`;
      targetIndex++;
      segments.push({ type: 'target', text: label, key });
      keys.push(key);
    }
    last = TARGET_RE.lastIndex;
  }
  if (last < text.length) segments.push({ type: 'text', text: text.slice(last) });

  // Coalesce consecutive text segments (e.g. around a literal [[]]), so the
  // output is the minimal run of text + target segments.
  const merged = [];
  for (const seg of segments) {
    const prev = merged[merged.length - 1];
    if (seg.type === 'text' && prev && prev.type === 'text') prev.text += seg.text;
    else merged.push(seg);
  }
  return { segments: merged, keys };
}

/**
 * Apply a tool to a target key. Same tool again toggles it off; a null tool
 * clears it; a different tool replaces it. Returns a new state object.
 * @param {Object<string,string>} state
 * @param {string} key
 * @param {?string} toolId
 * @returns {Object<string,string>}
 */
export function applyTool(state, key, toolId) {
  const next = { ...state };
  if (toolId == null || toolId === '' || next[key] === toolId) delete next[key];
  else next[key] = toolId;
  return next;
}

/** How many targets currently carry an annotation. */
export function annotationCount(state) {
  return Object.values(state || {}).filter(v => v != null && v !== '').length;
}

/** Interaction-complete when at least `minAnnotations` targets are annotated. */
export function isComplete(state, minAnnotations = 1) {
  return annotationCount(state) >= Math.max(0, minAnnotations);
}

/** Serialise state to an array aligned to target order (for _userAnswer). */
export function toUserAnswer(state, keys) {
  return (keys || []).map(k => (state && state[k] != null ? String(state[k]) : ''));
}

/** Rebuild state from a serialised array and the current target keys. */
export function fromUserAnswer(arr, keys) {
  const state = {};
  if (!Array.isArray(arr) || !Array.isArray(keys)) return state;
  keys.forEach((k, i) => { if (arr[i]) state[k] = arr[i]; });
  return state;
}

/**
 * Mark a learner's annotations against an answer key (question mode).
 * `answers` is aligned to `keys` by position: answers[i] is the tool id the
 * target at keys[i] should carry. An empty/absent answer means that target is
 * not scored (free annotation). Only scored targets count toward the total.
 * @param {Object<string,string>} state  key -> applied tool id
 * @param {string[]} keys    ordered target keys (model._targetKeys)
 * @param {string[]} answers ordered correct tool ids
 * @returns {{marks: Array<{key:string, applied:string, correct:string, isScored:boolean, isCorrect:boolean}>, correctCount:number, total:number, allCorrect:boolean}}
 */
export function markAnswers(state, keys, answers) {
  const ks = Array.isArray(keys) ? keys : [];
  const ans = Array.isArray(answers) ? answers : [];
  let correctCount = 0;
  let total = 0;
  const marks = ks.map((key, i) => {
    const correct = ans[i] || '';
    const applied = (state && state[key] != null) ? String(state[key]) : '';
    const isScored = !!correct;
    const isCorrect = isScored ? applied === correct : true;
    if (isScored) { total++; if (isCorrect) correctCount++; }
    return { key, applied, correct, isScored, isCorrect };
  });
  return { marks, correctCount, total, allCorrect: total > 0 && correctCount === total };
}

// ===========================================================================
// FREE-SELECTION MODE
// No author [[targets]]: the passage is tokenised into words, the learner
// selects any run of words and marks it, and (question mode) each mark is graded
// against `_targets` (expected { text, tool }) by the "covers the word" rule.
// ===========================================================================

const WORD_RE = /\S+/g; // a word = a run of non-whitespace (punctuation stays attached)

/**
 * Split a passage into tokens: words (indexed) and the gaps between them.
 * @returns {{tokens: Array<{type:'word', text:string, index:number}|{type:'gap', text:string}>, wordCount:number}}
 */
export function tokenizePassage(input) {
  const text = String(input == null ? '' : input);
  const tokens = [];
  let wordIndex = 0, last = 0, m;
  WORD_RE.lastIndex = 0;
  while ((m = WORD_RE.exec(text)) !== null) {
    if (m.index > last) tokens.push({ type: 'gap', text: text.slice(last, m.index) });
    tokens.push({ type: 'word', text: m[0], index: wordIndex++ });
    last = WORD_RE.lastIndex;
  }
  if (last < text.length) tokens.push({ type: 'gap', text: text.slice(last) });
  return { tokens, wordCount: wordIndex };
}

/** Lowercase + strip punctuation for tolerant matching. */
export function normaliseWord(s) {
  return String(s == null ? '' : s).toLowerCase()
    .replace(/[^\p{L}\p{N}\s]/gu, '').replace(/\s+/g, ' ').trim();
}

/**
 * Locate each expected target's word-index span in the tokenised passage
 * (first occurrence). Returns targets as { text, tool, a, b } with a=-1 when not
 * found (an author typo in `_targets.text`).
 */
export function locateTargets(tokens, targets) {
  const words = (tokens || []).filter(t => t.type === 'word');
  const normWords = words.map(w => normaliseWord(w.text));
  return (targets || []).map(t => {
    const tw = normaliseWord(t && t.text).split(' ').filter(Boolean);
    let a = -1, b = -1;
    if (tw.length) {
      for (let i = 0; i + tw.length <= normWords.length; i++) {
        let hit = true;
        for (let j = 0; j < tw.length; j++) if (normWords[i + j] !== tw[j]) { hit = false; break; }
        if (hit) { a = words[i].index; b = words[i + tw.length - 1].index; break; }
      }
    }
    return { text: (t && t.text) || '', tool: (t && t.tool) || '', a, b };
  });
}

/**
 * Grade free-selection annotations with the "covers the word" rule: a target is
 * found when some annotation of the matching tool spans across it (ann.a <= tg.a
 * && ann.b >= tg.b). Extra words in the selection are tolerated. An annotation
 * that covers no expected target (or covers with the wrong tool) is incorrect.
 * @param {Array<{id:string,a:number,b:number,tool:string}>} annotations
 * @param {Array} tokens  tokenizePassage output
 * @param {Array<{text:string,tool:string}>} targets
 */
export function gradeFree(annotations, tokens, targets) {
  const located = locateTargets(tokens, targets);
  const anns = (annotations || []).map(an => ({ ...an, isCorrect: false }));
  let found = 0;
  const targetMarks = located.map(tg => {
    if (tg.a < 0) return { ...tg, isFound: false };
    const hit = anns.find(an => an.tool === tg.tool && an.a <= tg.a && an.b >= tg.b);
    if (hit) { hit.isCorrect = true; found++; return { ...tg, isFound: true }; }
    return { ...tg, isFound: false };
  });
  const total = located.length;
  return { annotations: anns, targets: targetMarks, found, total, allCorrect: total > 0 && found === total };
}
