/**
 * CardView
 *
 * View for the grow-card component. Extends ComponentView.
 *
 * Presentational: no interaction handlers. Waits for any card images to load,
 * then marks ready; sets up inview completion so a visible card counts toward
 * page completion (the component contract - see docs/adapt-extensibility-map.md
 * section 8).
 */

import ComponentView from 'core/js/views/componentView';

class CardView extends ComponentView {

  postRender() {
    if (this.model.hasAnyGraphics()) {
      this.$('.grow-card__group').imageready(this.setReadyStatus.bind(this));
    } else {
      this.setReadyStatus();
    }

    this.setupInviewCompletion('.component__widget');
  }

}

CardView.template = 'card.jsx';

export default CardView;
