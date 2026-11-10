/**
 * WizardView
 *
 * View for the step wizard. Extends ComponentView (NOT QuestionView) to stay
 * outside the scoring machinery.
 *
 * Behaviour (from the gallery pattern):
 * - a progress bar whose width tracks the current step via --p
 * - a row of step labels with the current one highlighted (.is-current)
 * - a content panel that fades in per step
 * - Back and Next move through the steps, clamped at the ends
 *
 * Accessibility:
 * - the progress bar is a role="progressbar" with an accessible value
 * - the active step label carries aria-current="step"
 * - only the current panel is in the accessibility tree and tab order
 * - step changes are announced politely via a live region
 * - all learner-facing strings come from schema globals
 * - the progress-width and panel-fade transitions are disabled under reduced
 *   motion (handled in LESS)
 *
 * Note: in this fork ComponentView.postRender() is a no-op, so this view calls
 * setReadyStatus() itself or the page never fires contentObjectView:ready and
 * the loading curtain never lifts (as with the other GROW components).
 */

import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';

class WizardView extends ComponentView {

  events() {
    return {
      'click .js-grow-wizard-back': 'onBack',
      'click .js-grow-wizard-next': 'onNext'
    };
  }

  getData() {
    const data = super.getData();
    const start = this.model.getStartIndex();
    data._globals = this._getGlobals();
    data._startIndex = start;
    data._stepCount = this.model.getStepCount();
    data._startPercent = this.model.getProgressPercent(start);
    data._valueText = this._interpolate(this._getGlobals().progressValueText, {
      current: start + 1,
      total: this.model.getStepCount()
    });
    return data;
  }

  /** @private */
  _getGlobals() {
    return Adapt.course?.get('_globals')?._components?._growWizard || {};
  }

  /**
   * Interpolate {{name}} placeholders. Numbers are localised; strings pass
   * through. Mirrors the opentext/confidence pattern.
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

  postRender() {
    this.$bar = this.$('.js-grow-wizard-bar');
    this.$fill = this.$('.js-grow-wizard-fill');
    this.$steps = this.$('.js-grow-wizard-step');
    this.$panels = this.$('.js-grow-wizard-panel');
    this.$back = this.$('.js-grow-wizard-back');
    this.$next = this.$('.js-grow-wizard-next');
    this.$live = this.$('.js-grow-wizard-live');

    this.stepCount = this.model.getStepCount();
    this.index = this.model.clampIndex(this.model.getStartIndex());

    // Initial paint, no announcement.
    this._render(false);

    // A non-completion-bearing wizard is presentational: complete on view so it
    // never blocks page or trickle completion. A completion-bearing wizard
    // completes when the learner reaches the final step (see _render).
    if (!this.model.shouldCompleteOnFinalStep()) {
      this.setupInviewCompletion('.component__widget');
    }

    this.setReadyStatus();
  }

  onBack() {
    this._goTo(this.index - 1);
    // Keep keyboard focus usable if Back has just become disabled.
    if (this.$back.prop('disabled') && this.$next.length) this.$next.focus();
  }

  onNext() {
    this._goTo(this.index + 1);
    // Keep keyboard focus usable if Next has just become disabled.
    if (this.$next.prop('disabled') && this.$back.length) this.$back.focus();
  }

  /**
   * Move to an index, clamped. No-op if already there (clamped at an end).
   * @private
   */
  _goTo(index) {
    const next = this.model.clampIndex(index);
    if (next === this.index) return;
    this.index = next;
    this._render(true);
  }

  /**
   * Reflect the current index across the UI: progress width + ARIA value, the
   * active label, the visible panel, the Back/Next disabled states, completion,
   * and (optionally) a polite announcement.
   * @private
   */
  _render(announce) {
    const count = this.stepCount;
    const current = this.index;      // 0-based
    const human = current + 1;       // 1-based (learner-facing)
    const globals = this._getGlobals();

    // Progress bar: width via --p, plus accessible value.
    if (this.$fill.length) {
      this.$fill[0].style.setProperty('--p', this.model.getProgressPercent(current) + '%');
    }
    if (this.$bar.length) {
      this.$bar.attr('aria-valuenow', human);
      this.$bar.attr('aria-valuetext', this._interpolate(globals.progressValueText, { current: human, total: count }));
    }

    // Step labels: highlight and mark the current one.
    this.$steps.each((i, el) => {
      const on = i === current;
      el.classList.toggle('is-current', on);
      if (on) el.setAttribute('aria-current', 'step');
      else el.removeAttribute('aria-current');
    });

    // Panels: only the current one is visible, in the a11y tree and tab order.
    // Adding is-current to a newly current panel re-triggers the fade naturally.
    this.$panels.each((i, el) => {
      const on = i === current;
      el.classList.toggle('is-current', on);
      if (on) el.removeAttribute('hidden');
      else el.setAttribute('hidden', 'hidden');
      el.setAttribute('aria-hidden', String(!on));
    });

    // Back/Next clamp at the ends.
    this._setDisabled(this.$back, current <= 0);
    this._setDisabled(this.$next, current >= count - 1);

    // Completion on reaching the final step (bearing wizards only; sticky).
    if (this.model.shouldCompleteOnFinalStep() && this.model.isFinalIndex(current) && !this.model.get('_isComplete')) {
      this.setCompletionStatus();
    }

    // Announce the step change politely.
    if (announce) {
      const label = this._stripTags(this.model.getSteps()[current]?.label || '');
      this._announce(this._interpolate(globals.stepAnnouncement, { current: human, total: count, label }));
    }
  }

  /** @private */
  _setDisabled($btn, disabled) {
    if (!$btn.length) return;
    $btn.prop('disabled', disabled);
    $btn.attr('aria-disabled', String(disabled));
  }

  /** @private */
  _stripTags(html) {
    return String(html).replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();
  }

  /**
   * Announce via the polite live region. Clear then set so the same text can be
   * re-announced.
   * @private
   */
  _announce(message) {
    if (!this.$live.length || !message) return;
    this.$live.text('');
    setTimeout(() => this.$live.text(message), 50);
  }

}

WizardView.template = 'growWizard.jsx';

export default WizardView;
