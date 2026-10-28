/**
 * CalloutsView
 *
 * View for the ab-callouts component. Extends ComponentView.
 *
 * Presentational: no interaction handlers, no images to wait for. Marks ready
 * immediately, then sets up inview completion so a visible callout counts
 * toward page completion (the component contract - see
 * docs/adapt-extensibility-map.md section 8).
 */

import ComponentView from 'core/js/views/componentView';

class CalloutsView extends ComponentView {

  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__widget');
  }

}

CalloutsView.template = 'callouts.jsx';

export default CalloutsView;
