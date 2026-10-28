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
