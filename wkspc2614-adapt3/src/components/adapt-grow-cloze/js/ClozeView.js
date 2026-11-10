/**
 * ClozeView
 *
 * View for the fill-the-blanks component. Extends ComponentView (NOT QuestionView)
 * to stay outside the scoring machinery.
 *
 * Behaviour (lifted from the gallery pattern, generalised to N blanks):
 * - On Check, each <select> is compared to its blank's correct answer in the model
 *   (answers are never put in the DOM), toggling a correct/incorrect state.
 * - State is conveyed NON-VISUALLY as well as by colour: a glyph mark (tick/cross),
 *   aria-invalid on wrong blanks, and a visually-hidden status word per blank that
 *   the select references with aria-describedby.
 * - An overall feedback message is written into a polite aria-live region.
 * - All learner-facing strings come from schema globals (_globals._growCloze).
 *
 * Like the other GROW components, ComponentView.postRender() is a no-op, so this
 * view calls setReadyStatus() itself or the page never fires
 * contentObjectView:ready and the loading curtain never lifts.
 */
import $ from 'jquery';
import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';

class ClozeView extends ComponentView {

  events() {
    return {
      'click .js-grow-cloze-check': 'onCheck',
      'change .grow-cloze__select': 'onChange'
    };
  }

  getData() {
    const data = super.getData();
    data._globals = this._getGlobals();
    data._segments = this.model.getSegments();
    data._blankCount = this.model.getBlankCount();
    return data;
  }

  /**
   * Component globals from course config. Keyed by component name (growCloze), so
   * the key is _growCloze. No fallback: schema defaults must resolve.
   * @private
   */
  _getGlobals() {
    return Adapt.course?.get('_globals')?._components?._growCloze || {};
  }

  /**
   * Interpolate {{name}} placeholders in a globals string.
   * @private
   */
  _interpolate(template, values) {
    if (!template) return '';
    return template.replace(/\{\{(\w+)\}\}/g, (match, key) =>
      (values[key] !== undefined ? values[key] : match)
    );
  }

  postRender() {
    this.$selects = this.$('.grow-cloze__select');
    this.$feedback = this.$('.grow-cloze__feedback');
    this._hasChecked = false;
    this.setReadyStatus();
  }

  /**
   * Editing a blank after a Check clears that blank's marking so stale feedback
   * never lingers on a changed answer.
   */
  onChange(e) {
    const select = e.currentTarget;
    const $blank = $(select).closest('.grow-cloze__blank');
    $blank.removeClass('is-correct is-incorrect');
    select.removeAttribute('aria-invalid');
    $blank.find('.grow-cloze__blank-status').text('');
  }

  /**
   * Mark every blank against its stored answer and announce overall feedback.
   */
  onCheck() {
    if (!this.model.get('_isEnabled')) return;

    const globals = this._getGlobals();
    let allCorrect = true;

    this.$selects.each((i, select) => {
      const index = parseInt(select.getAttribute('data-blank-index'), 10);
      const answer = this.model.getAnswer(index);
      const isCorrect = select.value !== '' && select.value === answer;
      const $blank = $(select).closest('.grow-cloze__blank');

      $blank.toggleClass('is-correct', isCorrect);
      $blank.toggleClass('is-incorrect', !isCorrect);

      // Non-visual state: aria-invalid + a visually-hidden status word that the
      // select references via aria-describedby (not colour alone).
      if (isCorrect) {
        select.removeAttribute('aria-invalid');
      } else {
        select.setAttribute('aria-invalid', 'true');
      }
      $blank.find('.grow-cloze__blank-status').text(isCorrect ? globals.blankCorrect : globals.blankIncorrect);

      if (!isCorrect) allCorrect = false;
    });

    const message = allCorrect ? globals.feedbackCorrect : globals.feedbackIncorrect;
    this.$feedback
      .removeClass('is-correct is-incorrect')
      .addClass(allCorrect ? 'is-correct' : 'is-incorrect')
      .text(message);

    // Formative completion: optional, on first Check, never a score.
    if (!this._hasChecked && this.model.isCompletionBearing() && !this.model.get('_isComplete')) {
      this.model.setCompletionStatus();
    }
    this._hasChecked = true;
  }

}

ClozeView.template = 'growCloze.jsx';

export default ClozeView;
