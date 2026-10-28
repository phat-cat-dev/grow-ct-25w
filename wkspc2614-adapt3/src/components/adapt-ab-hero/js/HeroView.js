/**
 * HeroView
 *
 * View for the ab-hero component. Extends ComponentView.
 *
 * Presentational: no interaction handlers. Waits for a hero image to load
 * (if any), then marks ready; sets up inview completion so a visible hero
 * counts toward page completion (the component contract - see
 * docs/adapt-extensibility-map.md section 8).
 */

import ComponentView from 'core/js/views/componentView';

class HeroView extends ComponentView {

  postRender() {
    if (this.model.hasImage()) {
      this.$('.ab-hero__widget').imageready(this.setReadyStatus.bind(this));
    } else {
      this.setReadyStatus();
    }

    this.setupInviewCompletion('.component__widget');
  }

}

HeroView.template = 'hero.jsx';

export default HeroView;
