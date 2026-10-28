/**
 * marksExtensionLogic.js — pure config logic for the grow-marks extension.
 *
 * No DOM, no Adapt. Decides whether the extension is on, whether a component
 * wants feedback marking, and which mark/colour a right or wrong answer gets.
 * Unit-tested; the main module stays a thin DOM/event wrapper over this.
 */

/** Defaults when a component enables feedback but doesn't override the marks. */
export const DEFAULT_FEEDBACK = {
  correct: { mark: 'tick', color: 'positive' },
  incorrect: { mark: 'cross', color: 'negative' }
};

/**
 * Globally on unless the course explicitly disables it.
 * @param {?{_isEnabled?:boolean}} courseConfig  course.get('_growMarks')
 */
export function isGloballyEnabled(courseConfig) {
  return !courseConfig || courseConfig._isEnabled !== false;
}

/**
 * Feedback marking is opt-in per component (off by default), so it never fights
 * a question's own tutor feedback unless the author asks for it.
 * @param {?object} componentConfig  model.get('_growMarks')
 */
export function isFeedbackEnabled(componentConfig) {
  if (!componentConfig || componentConfig._isEnabled === false) return false;
  const feedback = componentConfig._feedback;
  return !!(feedback && feedback._isEnabled);
}

/**
 * Resolve the mark + colour to play for a graded answer.
 * @param {boolean} isCorrect
 * @param {?object} componentConfig  model.get('_growMarks')
 * @returns {{mark:string, color:string}}
 */
export function resolveFeedbackMark(isCorrect, componentConfig) {
  const feedback = (componentConfig && componentConfig._feedback) || {};
  const slot = (isCorrect ? feedback._correct : feedback._incorrect) || {};
  const fallback = isCorrect ? DEFAULT_FEEDBACK.correct : DEFAULT_FEEDBACK.incorrect;
  return {
    mark: slot._mark || fallback.mark,
    color: slot._color || fallback.color
  };
}
