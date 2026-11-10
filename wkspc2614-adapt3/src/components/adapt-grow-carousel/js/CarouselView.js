/**
 * CarouselView
 *
 * View for the grow-carousel component. Extends ComponentView.
 *
 * Accessibility model:
 * - Container aria-roledescription="carousel" + aria-label (ariaRegion).
 * - Each slide role="group" aria-roledescription="slide", labelled "N of M";
 *   non-current slides are aria-hidden.
 * - Previous/next and indicators are native <button>s.
 * - .carousel-inner is aria-live="polite" while not auto-scrolling.
 * - Auto-rotate off by default; if enabled, consider a pause control.
 */

import ComponentView from 'core/js/views/componentView';

class CarouselView extends ComponentView {

  events() {
    return {
      'click .grow-carousel__prev': 'onPrev',
      'click .grow-carousel__next': 'onNext',
      'click .grow-carousel__indicator': 'onIndicator'
    };
  }

  preRender() {
    this.listenTo(this.model, 'change:_activeIndex', this.onActiveIndexChange);
  }

  postRender() {
    if (this.model.hasAnyGraphics()) {
      this.$('.carousel-inner').imageready(this.setReadyStatus.bind(this));
    } else {
      this.setReadyStatus();
    }
    this.setupInviewCompletion('.component__widget');
  }

  onPrev() { this.model.prev(); }

  onNext() { this.model.next(); }

  onIndicator(event) {
    const index = this.$(event.currentTarget).data('index');
    if (typeof index === 'number') this.model.goTo(index);
  }

  onActiveIndexChange() {
    this.changed();
  }

}

CarouselView.template = 'carousel.jsx';

export default CarouselView;
