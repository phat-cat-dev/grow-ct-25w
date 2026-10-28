/**
 * TimelineView
 *
 * View for the timeline component. Extends ComponentView.
 *
 * Accessibility model (TL-6):
 * - <ol> with <li> per stage — sequence semantics in the list structure
 * - Each stage marker is a native <button>
 * - aria-expanded on button reflects expand state
 * - Button accessible name = label + title (static, never swapping)
 * - Detail region in flow after button, aria-hidden when collapsed
 * - ariaRegion introduces the interaction at component level
 * - Focus doesn't move on expand
 * - Native button keyboard semantics only (Tab / Enter / Space)
 *
 * Design refs: TB-4 (view/template), TB-5 (less)
 */

import ComponentView from 'core/js/views/componentView';

class TimelineView extends ComponentView {

  events() {
    return {
      'click .timeline__marker': 'onMarkerClick'
    };
  }

  preRender() {
    // Listen for item expanded state changes to re-render
    this.listenTo(this.model.getChildren(), 'change:_isExpanded', this.onItemExpandedChange);
  }

  postRender() {
    // Wait for detail images to load before marking ready
    if (this.model.hasAnyDetailGraphics()) {
      this.$('.timeline__stages').imageready(this.setReadyStatus.bind(this));
    } else {
      // No images — ready immediately
      this.setReadyStatus();
    }

    // Set up inview completion (component visible = counts toward page completion)
    this.setupInviewCompletion('.component__widget');
  }

  /**
   * Handle marker click — toggle expanded state via model.
   * @param {Event} event
   */
  onMarkerClick(event) {
    const $marker = this.$(event.currentTarget);
    const index = $marker.data('index');

    if (typeof index !== 'number') return;

    this.model.toggleItemExpanded(index);
  }

  /**
   * Re-render when an item's expanded state changes.
   * The JSX template reads _isExpanded from props, so we just trigger a re-render.
   */
  onItemExpandedChange() {
    // Trigger a re-render by calling changed() which re-renders the React component
    this.changed();
  }

}

TimelineView.template = 'timeline.jsx';

export default TimelineView;
