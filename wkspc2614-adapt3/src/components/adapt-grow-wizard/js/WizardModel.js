/**
 * WizardModel
 *
 * Model for the step wizard. Extends ComponentModel (NOT QuestionModel) to stay
 * outside the scoring machinery: no _userAnswer, no interactions, no marking.
 *
 * Owns the step data and the maths derived from the current index (clamping,
 * progress percentage, "is this the final step?"), plus the completion rule
 * (completes on reaching the final step only when _isCompletionBearing is true).
 * The view owns the DOM and the affordances.
 */

import ComponentModel from 'core/js/models/componentModel';
import logging from 'core/js/logging';

const LOG_PREFIX = '[growWizard]';

export default class WizardModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _steps: [],
      _isCompletionBearing: false
    };
  }

  init() {
    super.init();
    this._validateSteps();
  }

  /**
   * Warn (do not throw) if there are no steps; the component still renders
   * an empty, harmless shell.
   * @private
   */
  _validateSteps() {
    if (!this.getStepCount()) {
      logging.warn(`${LOG_PREFIX} ${this.get('_id')}: no _steps authored; the wizard will render empty.`);
    }
  }

  /**
   * The authored steps as an array (defensive: always returns an array).
   */
  getSteps() {
    const steps = this.get('_steps');
    return Array.isArray(steps) ? steps : [];
  }

  getStepCount() {
    return this.getSteps().length;
  }

  /**
   * Which step opens first. The flow always starts at the beginning, matching
   * the source pattern.
   */
  getStartIndex() {
    return 0;
  }

  /**
   * Clamp an index to the valid [0, count - 1] range (the Back/Next clamp).
   */
  clampIndex(index) {
    const last = Math.max(0, this.getStepCount() - 1);
    const n = Number(index);
    if (Number.isNaN(n)) return 0;
    return Math.max(0, Math.min(last, n));
  }

  /**
   * Whether an index is the final step.
   */
  isFinalIndex(index) {
    const count = this.getStepCount();
    return count > 0 && this.clampIndex(index) >= count - 1;
  }

  /**
   * Progress as a whole-number percentage for the 1-based "current of total"
   * reading, matching the source ((index + 1) / total * 100).
   */
  getProgressPercent(index) {
    const count = this.getStepCount();
    if (!count) return 0;
    return Math.round(((this.clampIndex(index) + 1) / count) * 100);
  }

  /**
   * Completion rule: only a completion-bearing wizard completes on reaching the
   * final step. A non-bearing wizard is presentational (view completes on view).
   */
  shouldCompleteOnFinalStep() {
    return this.get('_isCompletionBearing') === true;
  }

  /**
   * Mark complete. Formative completion only, never a score or interaction.
   */
  markComplete() {
    this.setCompletionStatus();
  }

  /**
   * Completion is sticky: a hard reset on revisit must not silently wipe it.
   * Mirrors the opentext pattern.
   */
  reset(type = 'hard', canReset = this.get('_canReset')) {
    const wasComplete = this.get('_isComplete');
    const didReset = super.reset(type, canReset);
    if (didReset && wasComplete) {
      this.set('_isComplete', true);
    }
    return didReset;
  }

}
