/**
 * pagefeedbackLogic
 *
 * Pure, framework-free functions for adapt-grow-pagefeedback. Kept separate
 * from PagefeedbackModel/View so the state-transition and persistence-shape
 * rules can be unit-tested with node:test, without Adapt/Backbone/jQuery.
 *
 * See: docs/authoring/component-specs/pagefeedback.md
 */

export const VALID_RESPONSES = ['helpful', 'needs-work'];
export const VALID_VARIANTS = ['conversation', 'growth', 'fieldnote'];

// Variant default choice labels — used only when the author leaves
// _choicePositiveLabel / _choiceNegativeLabel blank.
export const VARIANT_LABELS = {
  conversation: { positive: 'Yes, it helped', negative: 'Not quite' },
  growth: { positive: 'That made sense', negative: 'I need more clarity' },
  fieldnote: { positive: 'Found what I needed', negative: 'Something is missing' }
};

/**
 * Whether a response value is one of the two allowed choices.
 */
export function isValidResponse (value) {
  return VALID_RESPONSES.includes(value);
}

/**
 * Resolve the labels to show for the positive/negative choice buttons.
 * Author overrides win; otherwise fall back to the variant's defaults;
 * an unrecognised variant falls back to 'conversation'.
 */
export function resolveChoiceLabels (variant, positiveOverride, negativeOverride) {
  const defaults = VARIANT_LABELS[variant] || VARIANT_LABELS.conversation;
  return {
    positive: positiveOverride || defaults.positive,
    negative: negativeOverride || defaults.negative
  };
}

/**
 * Build the persisted payload shape for offlineStorage.
 * { v: variant, r: response, n: note }
 */
export function buildPayload (variant, response, note) {
  return { v: variant, r: response, n: note || '' };
}

// Valid transient save-status values. Never persisted — purely for driving
// which globals string the status line shows after the last action.
export const VALID_SAVE_STATUSES = ['idle', 'no-response', 'saved', 'failed', 'cleared'];

/**
 * Resolve which globals key the status line should read, given the last
 * save-action outcome and whether a response is currently chosen.
 * Pure function so the state table is unit-testable without a DOM/model.
 */
export function resolveStatusKey (saveStatus, hasResponse) {
  switch (saveStatus) {
    case 'saved': return 'statusSaved';
    case 'failed': return 'statusFailed';
    case 'cleared': return 'statusCleared';
    case 'no-response': return 'statusChooseFirst';
    default: return hasResponse ? 'statusChosen' : 'statusPrompt';
  }
}

/**
 * Defensively parse a value read back from offlineStorage.
 * Accepts the expected { v, r, n } object shape only — there is no legacy
 * bare-string shape for this component (unlike opentext). Returns null for
 * anything else so the caller can skip restoration without crashing.
 */
export function parsePayload (stored) {
  if (!stored || typeof stored !== 'object') return null;
  const response = isValidResponse(stored.r) ? stored.r : null;
  const note = typeof stored.n === 'string' ? stored.n : '';
  return { response, note };
}
