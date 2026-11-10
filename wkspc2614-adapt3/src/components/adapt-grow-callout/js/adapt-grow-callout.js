/*
 * adapt-grow-callout
 * Static display component — a categorised message box (info / warning / tip /
 * example / note / definition). Ported to the 5.x React (.jsx) pipeline:
 * components.register + a React template (was Adapt.register + Handlebars).
 */
import components from 'core/js/components';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class CalloutView extends ComponentView {

  // Purely presentational. Signal ready + complete on inview, or the page never
  // fires contentObjectView:ready and the loading screen never lifts.
  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__inner');
  }

}

CalloutView.template = 'growCallout.jsx';

export default components.register('growCallout', {
  view: CalloutView,
  model: ComponentModel
});
