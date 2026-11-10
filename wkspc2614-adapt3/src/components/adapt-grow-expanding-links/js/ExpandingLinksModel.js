/**
 * ExpandingLinksModel
 *
 * Model for the expanding-links learning-sequence component. Extends
 * ComponentModel (NOT QuestionModel) to stay outside the scoring machinery.
 *
 * The model owns the completion rule; the view owns navigation, the "done" set
 * and the affordances. Completion is formative:
 *   - _isCompletionBearing false: the component completes on inview (seen = done),
 *     contributing no deliberate signal. The view sets this up.
 *   - _isCompletionBearing true: completion is an explicit learner action,
 *     governed by _completionCriteria ('allStepsComplete' or 'finalStep').
 *
 * Nothing here writes cmi.interactions or a score. Step progress ("done" set,
 * current index) is ephemeral per the study and is not persisted; only Adapt's
 * own _isComplete persists and is restored on revisit.
 */

import ComponentModel from 'core/js/models/componentModel';
import logging from 'core/js/logging';

const LOG_PREFIX = '[growExpandingLinks]';
const VALID_CRITERIA = ['allStepsComplete', 'finalStep'];
const VALID_LABEL_DISPLAY = ['expandOnActive', 'always'];

export default class ExpandingLinksModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _steps: [],
      _isCompletionBearing: false,
      _completionCriteria: 'allStepsComplete',
      _labelDisplay: 'expandOnActive'
    };
  }

  init() {
    super.init();
    this._validateEnums();
  }

  /**
   * Validate the two enum properties. Warn and fall back on an unknown value
   * rather than render something broken.
   * @private
   */
  _validateEnums() {
    const id = this.get('_id');

    const criteria = this.get('_completionCriteria');
    if (criteria && !VALID_CRITERIA.includes(criteria)) {
      logging.warn(`${LOG_PREFIX} ${id}: Invalid _completionCriteria "${criteria}". Falling back to "allStepsComplete".`);
      this.set('_completionCriteria', 'allStepsComplete');
    }

    const labelDisplay = this.get('_labelDisplay');
    if (labelDisplay && !VALID_LABEL_DISPLAY.includes(labelDisplay)) {
      logging.warn(`${LOG_PREFIX} ${id}: Invalid _labelDisplay "${labelDisplay}". Falling back to "expandOnActive".`);
      this.set('_labelDisplay', 'expandOnActive');
    }
  }

  /**
   * Authored steps as a safe array.
   */
  getSteps() {
    return this.get('_steps') || [];
  }

  getStepCount() {
    return this.getSteps().length;
  }

  /**
   * Whether completion is a deliberate learner action (true) or just inview (false).
   */
  isCompletionBearing() {
    return this.get('_isCompletionBearing') === true;
  }

  getCompletionCriterion() {
    return this.get('_completionCriteria') || 'allStepsComplete';
  }

  /**
   * Decide, for a completion-bearing component, whether the current progress
   * satisfies the configured criterion.
   * @param {Object} progress { index, total, completed } where completed is a count.
   * @returns {boolean}
   */
  isSequenceComplete({ index, total, completed }) {
    if (!this.isCompletionBearing()) return false;
    if (this.getCompletionCriterion() === 'finalStep') {
      return total > 0 && index >= total - 1;
    }
    // allStepsComplete
    return total > 0 && completed >= total;
  }

  /**
   * Mark the Adapt component complete. Explicit, non-scored.
   */
  markComplete() {
    if (this.get('_isComplete')) return;
    this.setCompletionStatus();
  }

  /**
   * Protect completion on revisit. Completion here is a deliberate act (or a
   * seen-state) and must not be wiped by _isResetOnRevisit. Mirrors the
   * opentext "sticky completion" pattern: AdaptModel.reset(type='hard') clears
   * _isComplete, so restore it after super.reset().
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
