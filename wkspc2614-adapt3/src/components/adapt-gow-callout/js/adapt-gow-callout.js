/*
 * adapt-gow-callout
 * Static display component - ported from congen11's `callout` component schema.
 * See ../README.md for the field-mapping rationale and the v5 (AMD) equivalent.
 */
import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class CalloutView extends ComponentView {

  // Purely presentational. ComponentView.postRender() is a no-op, so the
  // component must signal ready/completion itself or the page never fires
  // contentObjectView:ready and the loading screen never lifts.
  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__inner');
  }

}

export default Adapt.register('callout', {
  view: CalloutView,
  model: ComponentModel
});
