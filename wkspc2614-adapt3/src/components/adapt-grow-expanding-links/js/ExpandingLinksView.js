/**
 * ExpandingLinksView
 *
 * View for the expanding-links learning-sequence component. Extends
 * ComponentView (NOT QuestionView) to stay outside the scoring machinery.
 *
 * Ports the study's learning-sequence.js player into the Adapt View lifecycle:
 *   - go(index, focus): navigate, show only the current step, move focus to the
 *     step panel, announce via the status live region, fire a change event.
 *   - mark(index): mark a step complete, update progress, fire a progress event,
 *     and apply the component's completion rule (model owns the rule).
 *   - reset(): clear the "done" set and return to step 1.
 *   - get(): snapshot { index, total, completed } (completed = indices).
 *
 * Accessibility and motion are preserved from the study: aria-current="step"
 * on the active button (which also expands its label), a polite role="status"
 * live region, keyboard focus moved to the panel on Back/Next, and reduced-motion
 * handled in LESS. All fixed learner-facing strings come from schema globals.
 *
 * ComponentView.postRender() is a no-op and does not call setReadyStatus(), so
 * (like the sibling GROW components) this view calls it itself or the page never
 * fires contentObjectView:ready and the loading curtain never lifts.
 */

import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';

class ExpandingLinksView extends ComponentView {

  events() {
    return {
      'click .js-grow-el-step': 'onStep',
      'click .js-grow-el-back': 'onBack',
      'click .js-grow-el-next': 'onNext',
      'click .js-grow-el-complete': 'onMark'
    };
  }

  /**
   * Extend model data for the template: resolved globals, normalised steps
   * (each tagged _iconIsSvg for icon rendering), and config flags.
   */
  getData() {
    const data = super.getData();
    data._globals = this._getGlobals();
    data._stepsResolved = this.model.getSteps().map((step, i) => ({
      ...step,
      _index: i,
      _number: i + 1,
      _iconIsSvg: this._isInlineSvg(step._icon)
    }));
    return data;
  }

  /**
   * Component globals, keyed by registered component name (spec: single source
   * of truth, no fallback strings in code).
   * @private
   */
  _getGlobals() {
    return Adapt.course?.get('_globals')?._components?._growExpandingLinks || {};
  }

  /**
   * An icon value is treated as inline SVG when it begins with an <svg tag;
   * otherwise it is a Material Symbols ligature name.
   * @private
   */
  _isInlineSvg(icon) {
    return typeof icon === 'string' && /^\s*<svg[\s>]/i.test(icon);
  }

  /**
   * Interpolate {{name}} placeholders. Numbers are localised; strings pass
   * through. Ported from the opentext view.
   * @private
   */
  _interpolate(template, values) {
    if (!template) return '';
    return template.replace(/\{\{(\w+)\}\}/g, (match, key) => {
      const value = values[key];
      if (value === undefined) return match;
      return typeof value === 'number' ? value.toLocaleString() : value;
    });
  }

  // Adapt's JSX path builds props from the view's OWN properties + model json
  // (it does NOT call getData), so expose the derived steps and component globals
  // as own props before the first render()/changed() (FB-6).
  preRender() {
    this._stepsResolved = this.model.getSteps().map((step, i) => ({
      ...step, _index: i, _number: i + 1, _iconIsSvg: this._isInlineSvg(step._icon)
    }));
    this._elGlobals = this._getGlobals();
  }

  postRender() {
    // Cache DOM
    this.$nav = this.$('.js-grow-el-nav');
    this.$buttons = this.$('.js-grow-el-step');
    this.$panels = this.$('.js-grow-el-panel');
    this.$status = this.$('.js-grow-el-status');
    this.$back = this.$('.js-grow-el-back');
    this.$next = this.$('.js-grow-el-next');
    this.$complete = this.$('.js-grow-el-complete');

    this.total = this.$panels.length;
    this.index = 0;
    this.done = new Set();

    // Restore a completed state (Adapt persists _isComplete; step progress is not
    // persisted). For allStepsComplete, reflect it by marking every step done.
    if (this.model.get('_isComplete') &&
        this.model.isCompletionBearing() &&
        this.model.getCompletionCriterion() === 'allStepsComplete') {
      for (let i = 0; i < this.total; i++) this.done.add(i);
    }

    this._refresh();

    // Evaluate completion once at mount so a completion-bearing 'finalStep'
    // sequence whose final step is already the current one (for example a
    // single-step sequence) is not left unable to complete. No-ops otherwise.
    this._applyCompletionRule();

    // Formative, not completion-bearing: complete simply on being seen so the
    // component never silently blocks page completion. setupInviewCompletion is
    // the standard ComponentView mechanism (seen = done), not a score.
    if (!this.model.isCompletionBearing() && !this.model.get('_isComplete')) {
      this.setupInviewCompletion();
    }

    this.setReadyStatus();
  }

  /**
   * Snapshot of player state. completed is the sorted list of completed indices,
   * matching the study's event detail shape.
   */
  get() {
    return {
      index: this.index,
      total: this.total,
      completed: [...this.done].sort((a, b) => a - b)
    };
  }

  /**
   * Reflect current state into the DOM. Shows only the current step's panel,
   * sets aria-current on the active button, updates completion marks, disables
   * Back/Next at the ends, toggles the mark-complete control, and writes the
   * status live region.
   */
  // Reflect state into the DOM. Renamed from render() so it no longer clobbers
  // the inherited lifecycle render() (template + postRender); that override made
  // Backbone initialize() call this with $panels undefined -> crash (FB-6).
  _refresh() {
    const globals = this._getGlobals();
    const steps = this.model.getSteps();

    this.$panels.each((i, el) => { el.hidden = i !== this.index; });

    this.$buttons.each((i, el) => {
      const isDone = this.done.has(i);
      const label = (steps[i] && steps[i].label) || '';
      if (i === this.index) el.setAttribute('aria-current', 'step');
      else el.removeAttribute('aria-current');
      el.dataset.complete = String(isDone);
      el.setAttribute('aria-label', this._interpolate(
        isDone ? globals.stepLabelCompleted : globals.stepLabel,
        { number: i + 1, label }
      ));
    });

    this.$back.prop('disabled', this.index === 0);
    this.$next.prop('disabled', this.index === this.total - 1);

    const currentDone = this.done.has(this.index);
    this.$complete.prop('disabled', currentDone);
    this.$complete.text(currentDone ? globals.stepCompletedButton : globals.markStepButton);

    const allDone = this.done.size === this.total && this.total > 0;
    let status = this._interpolate(globals.statusText, {
      current: this.index + 1,
      total: this.total,
      completed: this.done.size
    });
    if (allDone && globals.sequenceCompleteText) status += ' ' + globals.sequenceCompleteText;
    this.$status.text(status);
  }

  /**
   * Navigate to a zero-based step. Optionally move focus to the panel (used by
   * Back/Next); step buttons keep their own focus, matching the study.
   */
  go(index, focus = false) {
    if (!Number.isInteger(index) || index < 0 || index >= this.total) return;
    this.index = index;
    this._refresh();

    if (focus) {
      const panel = this.$panels[this.index];
      if (panel) panel.focus({ preventScroll: true });
    }

    this._dispatch('change');
    this._applyCompletionRule();
  }

  /**
   * Mark the current step complete. Formative self-marking (the study's
   * signature behaviour); then apply the component completion rule.
   */
  mark(index = this.index) {
    if (this.done.has(index)) return;
    this.done.add(index);
    this._refresh();

    // Focus handling mirrors the study: move to Next, else Back, else the button.
    if (!this.$next.prop('disabled')) this.$next.focus();
    else if (!this.$back.prop('disabled')) this.$back.focus();
    else if (this.$buttons[index]) this.$buttons[index].focus();

    this._dispatch('progress');
    this._applyCompletionRule();
  }

  /**
   * Clear completion marks and return to step 1. Preserved from the study API
   * (player.reset). Does not touch Adapt's own _isComplete.
   */
  reset() {
    this.done.clear();
    this.go(0);
  }

  /**
   * Ask the model whether the current progress satisfies completion, and set it
   * if so. The model owns the rule; the view only reports progress.
   * @private
   */
  _applyCompletionRule() {
    if (!this.model.isCompletionBearing()) return;
    if (this.model.get('_isComplete')) return;
    const complete = this.model.isSequenceComplete({
      index: this.index,
      total: this.total,
      completed: this.done.size
    });
    if (complete) this.model.markComplete();
  }

  /**
   * Fire a bubbling DOM CustomEvent on the component element, preserving the
   * study's event API (change / progress) with { index, total, completed }.
   * @private
   */
  _dispatch(name) {
    if (!this.el) return;
    this.el.dispatchEvent(new CustomEvent(`growExpandingLinks:${name}`, {
      bubbles: true,
      detail: this.get()
    }));
  }

  onStep(e) {
    const i = this.$buttons.index(e.currentTarget);
    this.go(i, false);
  }

  onBack() {
    this.go(this.index - 1, true);
  }

  onNext() {
    this.go(this.index + 1, true);
  }

  onMark() {
    this.mark(this.index);
  }

}

ExpandingLinksView.template = 'expandingLinks.jsx';

export default ExpandingLinksView;
