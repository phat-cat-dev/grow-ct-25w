/*
 * adapt-grow-stat-block
 * Static display component - ported from congen11's `grow-stat-block` component schema.
 * See ../README.md for the field-mapping rationale and the v5 (AMD) equivalent.
 */
import components from 'core/js/components';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class StatBlockView extends ComponentView {

  // Purely presentational. ComponentView.postRender() is a no-op, so the
  // component must signal ready/completion itself or the page never fires
  // contentObjectView:ready and the loading screen never lifts.
  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__inner');
  }

}

StatBlockView.template = 'growStatBlock';

export default components.register('growStatBlock', {
  view: StatBlockView,
  model: ComponentModel
});
