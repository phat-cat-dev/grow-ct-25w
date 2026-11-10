/**
 * PagefeedbackView
 *
 * View for the end-of-page feedback component. Extends ComponentView (NOT
 * QuestionView) — there is no scoring, just a two-choice self-report plus an
 * optional note.
 *
 * Re-renders (React diff via this.changed, matching adapt-grow-confidence's
 * radio pattern) on response/submitted/variant/save-status changes, since
 * those are discrete, action-driven transitions. Note text is NOT part of
 * that re-render loop — it is read/written directly via the textarea so
 * typing never disturbs focus or cursor position (matching
 * adapt-grow-opentext's rationale for keeping its textarea outside the
 * render loop).
 */

import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';

class PagefeedbackView extends ComponentView {

  events () {
    return {
      'click [data-grow-pagefeedback-choice]': 'onChoiceClick',
      'input .grow-pagefeedback__note': 'onNoteInput',
      'click .grow-pagefeedback__submit': 'onSubmitClick',
      'click .grow-pagefeedback__clear': 'onClearClick'
    };
  }

  preRender () {
    this.listenTo(this.model, 'change:_response change:_isSubmitted change:_variant change:_saveStatus', this.changed);
  }

  /**
   * Extend model data with computed properties for the template.
   */
  getData () {
    const data = super.getData();
    data._globals = this._getGlobals();
    data._choiceLabels = this.model.getChoiceLabels();
    data._statusKey = this.model.getStatusKey();
    data._initialNote = this.model.get('_note');
    return data;
  }

  /**
   * Get component globals from Adapt config.
   * @private
   */
  _getGlobals () {
    return Adapt.course?.get('_globals')?._components?._growPagefeedback || {};
  }

  postRender () {
    this.$note = this.$('.grow-pagefeedback__note');
    this.setReadyStatus();
  }

  /**
   * Handle a choice-button press. Just records the choice — saving happens
   * on an explicit Save press, matching the source demo's "choose, then
   * explicitly act" flow.
   */
  onChoiceClick (event) {
    const value = this.$(event.currentTarget).attr('data-grow-pagefeedback-choice');
    this.model.setResponse(value);
  }

  /**
   * Handle note typing. Deliberately does not trigger a re-render (see
   * class docblock) and does not persist — saved only on Save/Clear.
   */
  onNoteInput () {
    if (!this.$note.length) return;
    this.model.setNote(this.$note.val());
  }

  /**
   * Handle the Save response press.
   */
  onSubmitClick () {
    this.model.submitResponse();
  }

  /**
   * Handle the Clear response press.
   */
  onClearClick () {
    this.model.clearResponse();
    // Re-render has already cleared the form synchronously (Backbone's
    // .set() triggers change listeners before returning); move focus back
    // to the first choice, matching the source demo's reset behaviour.
    _.defer(() => this.$('[data-grow-pagefeedback-choice]').first().focus());
  }

}

PagefeedbackView.template = 'growPagefeedback.jsx';

export default PagefeedbackView;
