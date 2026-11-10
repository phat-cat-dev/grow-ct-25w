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
  parsePassage, applyTool, isComplete, markAnswers,
  tokenizePassage, gradeFree
} from './annotateLogic';

export default class AnnotateModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      passage: '',
      _tools: [],
      _minAnnotations: 1,
      _showLabels: true,
      _allowReset: true,
      _isQuestion: false,
      _answers: [],
      _feedback: {},
      _freeSelect: false,
      _targets: []
    };
  }

  isFreeSelect() {
    return !!this.get('_freeSelect');
  }

  /**
   * Question mode: mark the current annotations against `_answers` (aligned to
   * target order). Returns per-target marks + totals; see annotateLogic.markAnswers.
   */
  checkAnswers() {
    if (this.isFreeSelect()) {
      return gradeFree(this._free, this.get('_tokens'), this.get('_targets'));
    }
    return markAnswers(this._annotations, this.get('_targetKeys'), this.get('_answers'));
  }

  init() {
    super.init?.();

    // A usable default so a bare component still works: a single "Circle" tool.
    if (!(this.get('_tools') || []).length) {
      this.set('_tools', [{ _id: 'circle', label: 'Circle', _mark: 'oval', _color: 'accent' }]);
    }

    if (this.isFreeSelect()) {
      // Free-selection: tokenise the plain passage into words; the learner's
      // marks are spans of word indices (not author targets).
      const { tokens, wordCount } = tokenizePassage(this.get('passage'));
      this.set('_tokens', tokens);
      this.set('_wordCount', wordCount);
      this._free = [];
      return;
    }

    const { segments, keys } = parsePassage(this.get('passage'));
    this.set('_segments', segments);
    this.set('_targetKeys', keys);

    this._annotations = {};
  }

  // ---- free-selection state (array of { id, a, b, tool }; a,b = word indices) --
  getFree() { return this._free || (this._free = []); }

  addFree({ id, a, b, tool }) {
    const newId = id || `f${(this._free || []).length}_${a}_${b}`;
    this._free = [...(this._free || []), { id: newId, a, b, tool }];
    this.storeUserAnswer();
    this.checkCompletion();
    return newId;
  }

  removeFree(id) {
    this._free = (this._free || []).filter(f => f.id !== id);
    this.storeUserAnswer();
  }

  clearFree() {
    this._free = [];
    this.storeUserAnswer();
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
    if (this.isFreeSelect()) {
      const min = Math.max(0, this.get('_minAnnotations') || 0);
      if ((this._free || []).length >= min) this.setCompletionStatus();
      return;
    }
    if (isComplete(this._annotations, this.get('_minAnnotations'))) {
      this.setCompletionStatus();
    }
  }

  // _userAnswer is a NUMERIC array - one tool index per target (-1 = unmarked)
  // - not the tool-id strings. Adapt-contrib-spoor serialises _userAnswer into
  // SCORM cmi.suspend_data via convertValuesToNumbers, which throws on
  // non-numeric strings; textTagging stores indices for the same reason.
  storeUserAnswer() {
    const tools = this.get('_tools') || [];
    if (this.isFreeSelect()) {
      // Flat numeric triples [a, b, toolIndex, …] so spoor's suspend_data
      // serialisation (numbers only) is happy.
      const flat = [];
      (this._free || []).forEach(f => {
        flat.push(f.a, f.b, tools.findIndex(t => t._id === f.tool));
      });
      this.set('_userAnswer', flat);
      return;
    }
    const keys = this.get('_targetKeys') || [];
    this.set('_userAnswer', keys.map(key => {
      const toolId = this._annotations[key];
      return toolId == null ? -1 : tools.findIndex(tool => tool._id === toolId);
    }));
  }

  restoreUserAnswers() {
    const tools = this.get('_tools') || [];
    if (this.isFreeSelect()) {
      const flat = this.get('_userAnswer') || [];
      this._free = [];
      for (let i = 0; i + 2 < flat.length; i += 3) {
        const a = flat[i], b = flat[i + 1], ti = flat[i + 2];
        if (tools[ti]) this._free.push({ id: `r${i}`, a, b, tool: tools[ti]._id });
      }
      return;
    }
    const keys = this.get('_targetKeys') || [];
    const answer = this.get('_userAnswer') || [];
    this._annotations = {};
    keys.forEach((key, i) => {
      const index = answer[i];
      if (typeof index === 'number' && index >= 0 && tools[index]) {
        this._annotations[key] = tools[index]._id;
      }
    });
  }

}
