/**
 * confidenceLogic — pure, DOM-free logic for the confidence component.
 * No Adapt dependencies; unit-testable in isolation.
 * Implements CD-3 (five-pattern classification) and CD-4 (summary selection).
 */

export const PATTERNS = {
  ROSE: 'rose',
  STAYED_HIGH: 'stayedHigh',
  STAYED_LOW: 'stayedLow',
  NO_MOVEMENT: 'noMovement',
  DROPPED: 'dropped'
};

export const SUMMARY = {
  UP: '_predominantlyUp',
  MIXED: '_mixed',
  FLAT_OR_LOW: '_flatOrLow'
};

// CD-3 bands: Low = 1-2, Mid = 3, High = 4-5
function band(value) {
  if (value <= 2) return 'low';
  if (value === 3) return 'mid';
  return 'high';
}

/**
 * CD-3 — classify one item's (pre, post) rating pair into one of the five patterns.
 * First match wins, in this order. "Dropped" is checked FIRST so any downward
 * revision (even 5->4) is honoured and never masked. "Rose" is band-agnostic
 * (1->2 and 2->5 are both "rose"); finishing-band nuance lives in the summary.
 * The three "stayed" cases are separated by absolute band, not direction.
 * Both ratings must be integers 1-5 (BS-4: all items required within a paired instance).
 */
export function classifyItem(pre, post) {
  if (!Number.isInteger(pre) || !Number.isInteger(post) ||
      pre < 1 || pre > 5 || post < 1 || post > 5) {
    throw new Error(`classifyItem: ratings must be integers 1-5 (got pre=${pre}, post=${post})`);
  }
  if (post < pre) return PATTERNS.DROPPED;   // any downward move (checked first)
  if (post > pre) return PATTERNS.ROSE;      // any upward move
  const b = band(post);                       // post === pre — read absolute band
  if (b === 'high') return PATTERNS.STAYED_HIGH;
  if (b === 'low') return PATTERNS.STAYED_LOW;
  return PATTERNS.NO_MOVEMENT;                 // mid
}

/**
 * CD-4 — select the whole-instrument summary variant from the per-item patterns.
 * Never an aggregate score — a simple count of "positive" vs "attention" items.
 *   positive  = rose + stayedHigh
 *   attention = dropped + stayedLow
 *   (noMovement is neutral)
 * Rules:
 *   no attention and >=1 positive -> UP
 *   all neutral (no attention, no positive) -> FLAT_OR_LOW
 *   attention > positive -> FLAT_OR_LOW
 *   otherwise (attention >=1 and attention <= positive) -> MIXED
 * So "mostly up but one/two dropped" -> MIXED, which normalises the drops (SA-6).
 */
export function selectSummary(patterns) {
  const positive = patterns.filter(p => p === PATTERNS.ROSE || p === PATTERNS.STAYED_HIGH).length;
  const attention = patterns.filter(p => p === PATTERNS.DROPPED || p === PATTERNS.STAYED_LOW).length;
  if (attention === 0) return positive >= 1 ? SUMMARY.UP : SUMMARY.FLAT_OR_LOW;
  return attention > positive ? SUMMARY.FLAT_OR_LOW : SUMMARY.MIXED;
}
