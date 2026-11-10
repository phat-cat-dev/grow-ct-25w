/**
 * FlipcardView
 *
 * View for the flipcard component. Extends ComponentView.
 *
 * Accessibility model (FB-3):
 * - Each card is a native <button> containing both faces
 * - Both faces always in DOM; non-current face has aria-hidden="true"
 * - aria-expanded on button reflects flip state
 * - Button accessible name = front title (stable, doesn't swap on flip)
 * - ariaRegion introduces the interaction at component level
 * - Focus doesn't move on flip
 * - Native button keyboard semantics only (Tab / Enter / Space)
 *
 * Design refs: FB-3 (view/template), FB-4 (less)
 */

import ComponentView from 'core/js/views/componentView';

class FlipcardView extends ComponentView {

  events() {
    return {
      'click .grow-flipcard__card': 'onCardClick'
    };
  }

  preRender() {
    // Listen for item flipped state changes to re-render
    this.listenTo(this.model.getChildren(), 'change:_isFlipped', this.onItemFlippedChange);
  }

  postRender() {
    // Wait for front images to load before marking ready
    if (this.model.hasAnyFrontGraphics()) {
      this.$('.grow-flipcard__cards').imageready(this.setReadyStatus.bind(this));
    } else {
      // No images — ready immediately
      this.setReadyStatus();
    }

    // Set up inview completion (component visible = counts toward page completion)
    this.setupInviewCompletion('.component__widget');
  }

  /**
   * Handle card click — toggle flip state via model.
   * @param {Event} event
   */
  onCardClick(event) {
    const $card = this.$(event.currentTarget);
    const index = $card.data('index');

    if (typeof index !== 'number') return;

    this.model.toggleItemFlipped(index);
  }

  /**
   * Re-render when an item's flipped state changes.
   * The JSX template reads _isFlipped from props, so we just trigger a re-render.
   */
  onItemFlippedChange() {
    // Trigger a re-render by calling changed() which re-renders the React component
    this.changed();
  }

}

FlipcardView.template = 'growFlipcard.jsx';

export default FlipcardView;
