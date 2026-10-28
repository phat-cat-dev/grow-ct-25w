/**
 * ModalView — view for the modal launcher.
 * Extends ComponentView. Renders a trigger button; on click, opens the authored
 * content in the Adapt notify popup (themed by cm-notify.less). Handles
 * completion per the resolved mode.
 */

import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';
import { buildPopupOptions, COMPLETION } from './modalLogic';

class ModalView extends ComponentView {

  events() {
    return {
      'click .js-modal-trigger': 'onTriggerClick'
    };
  }

  postRender() {
    this.setReadyStatus();

    // On-view completion only when configured; TRIGGER completes on open, NONE
    // never auto-completes.
    if (this.model.getCompletionMode() === COMPLETION.VIEW) {
      this.setupInviewCompletion('.component__widget');
    }

    if (this.model.get('_isComplete')) {
      this.$el.addClass('is-complete');
    }
  }

  onTriggerClick(event) {
    if (event) event.preventDefault();

    const options = buildPopupOptions(this.model.getPopup());
    // Adapt.notify is always present; .popup opens the focused, dimmed-backdrop
    // modal and traps focus until dismissed.
    Adapt.notify.popup(options);

    if (this.model.getCompletionMode() === COMPLETION.TRIGGER && !this.model.get('_isComplete')) {
      this.setCompletionStatus();
    }
  }

}

ModalView.template = 'modal.jsx';

export default ModalView;
