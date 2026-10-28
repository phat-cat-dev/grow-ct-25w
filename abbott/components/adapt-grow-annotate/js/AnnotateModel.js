/**
 * AnnotateModel — model for the annotate component.
 *
 * Presentational / reflective, not a question: the learner marks author-defined
 * words in a passage with a chosen annotation "tool". No right/wrong. Extends
 * ComponentModel (like adapt-contrib-text), not ItemsComponentModel — the
 * "items" here are the passage targets and the tool palette, parsed from props
 * rather than Adapt child items.
 *
 * Interaction state is the map { targetKey -> toolId }. Completion is reached
 * when at least `_minAnnotations` targets are annotated (0 = complete on view).
 */

import ComponentModel from 'core/js/models/componentModel';
import {
  parsePassage, applyTool, isComplete, toUserAnswer, fromUserAnswer
} from './annotateLogic';

export default class AnnotateModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      passage: '',
      _tools: [],
      _minAnnotations: 1,
      _showLabels: true,
      _allowReset: true
    };
  }

  init() {
    super.init?.();

    // A usable default so a bare component still works: a single "Circle" tool.
    if (!(this.get('_tools') || []).length) {
      this.set('_tools', [{ _id: 'circle', label: 'Circle', _mark: 'oval', _color: 'accent' }]);
    }

    const { segments, keys } = parsePassage(this.get('passage'));
    this.set('_segments', segments);
    this.set('_targetKeys', keys);

    this._annotations = {};
  }

  getTool(toolId) {
    return (this.get('_tools') || []).find(t => t._id === toolId) || null;
  }

  getAnnotations() {
    return this._annotations;
  }

  /**
   * Apply (or toggle) a tool on a target. Persists and re-checks completion.
   * @returns {?string} the tool id now on the key, or undefined if cleared.
   */
  setAnnotation(key, toolId) {
    this._annotations = applyTool(this._annotations, key, toolId);
    this.storeUserAnswer();
    this.checkCompletion();
    return this._annotations[key];
  }

  clearAnnotations() {
    this._annotations = {};
    this.storeUserAnswer();
  }

  checkCompletion() {
    if (isComplete(this._annotations, this.get('_minAnnotations'))) {
      this.setCompletionStatus();
    }
  }

  storeUserAnswer() {
    this.set('_userAnswer', toUserAnswer(this._annotations, this.get('_targetKeys')));
  }

  restoreUserAnswers() {
    this._annotations = fromUserAnswer(this.get('_userAnswer'), this.get('_targetKeys'));
  }

}
