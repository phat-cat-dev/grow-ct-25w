/**
 * GlossaryView
 *
 * View for the glossary passage component. Renders the passage as
 * continuous prose with inline marker buttons for term segments.
 *
 * Accessibility: markers are native <button>s with aria-expanded and
 * aria-controls. Focus moves to the definition region on expansion; a back
 * control returns focus to the marker.
 *
 * Design refs: GL-A (accessibility model), GB-4 (view/template)
 */

import ComponentView from 'core/js/views/componentView';

class GlossaryView extends ComponentView {

  /**
   * DOM events.
   */
  events() {
    return {
      'click .js-grow-glossary-marker': 'onMarkerClick',
      'click .js-grow-glossary-back': 'onBackClick'
    };
  }

  /**
   * Initialize the view.
   */
  initialize(...args) {
    super.initialize(...args);

    // Track which marker to return focus to
    this._lastClickedMarkerIndex = null;
  }

  /**
   * Pre-render setup.
   */
  preRender() {
    this.listenTo(this.model, 'change:_expandedIndex', this.onExpandedChange);
  }

  /**
   * Post-render setup.
   */
  postRender() {
    // No images to wait for; set ready immediately
    this.setReadyStatus();

    // Restore reduced motion preference
    this.setupReducedMotion();
  }

  /**
   * Setup reduced motion handling.
   */
  setupReducedMotion() {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.$el.toggleClass('reduce-motion', prefersReducedMotion);
  }

  /**
   * Handle marker button click.
   * @param {Event} event
   */
  onMarkerClick(event) {
    event.preventDefault();
    const $marker = this.$(event.currentTarget);
    const index = parseInt($marker.data('index'), 10);

    // Track for back-navigation
    this._lastClickedMarkerIndex = index;

    // Toggle the term
    this.model.toggleTerm(index);
  }

  /**
   * Handle back-to-passage button click.
   * @param {Event} event
   */
  onBackClick(event) {
    event.preventDefault();

    // Remember which marker to return to
    const returnIndex = this._lastClickedMarkerIndex;

    // Close the term
    this.model.closeTerm();

    // Return focus to the marker
    if (returnIndex !== null) {
      const $marker = this.$(`.js-grow-glossary-marker[data-index="${returnIndex}"]`);
      if ($marker.length) {
        $marker.focus();
      }
    }
  }

  /**
   * Handle expansion state change.
   */
  onExpandedChange() {
    const expandedIndex = this.model.getExpandedIndex();
    const componentId = this.model.get('_id');

    // Update all markers' aria-expanded state
    this.$('.js-grow-glossary-marker').each((i, marker) => {
      const $marker = this.$(marker);
      const index = parseInt($marker.data('index'), 10);
      const isExpanded = (index === expandedIndex);
      $marker.attr('aria-expanded', isExpanded ? 'true' : 'false');

      // Update visited class
      const item = this.model.getItem(index);
      if (item && item.get('_isVisited')) {
        $marker.addClass('is-visited');
      }
    });

    // Update definition region visibility
    const $defRegion = this.$('.js-grow-glossary-definition-region');

    if (expandedIndex !== null) {
      const terms = this.model.getTerms();
      const term = terms[expandedIndex];

      if (term) {
        // Update definition content
        this.$('.js-grow-glossary-term-heading').text(term.term);
        this.$('.js-grow-glossary-definition-body').html(term.definition);
        this.$('.js-grow-glossary-back').attr(
          'aria-label',
          `Back to passage, after the term ${term.term}`
        );

        // Show region
        $defRegion
          .removeClass('u-display-none')
          .attr('aria-hidden', 'false');

        // Move focus to definition region
        $defRegion.focus();
      }
    } else {
      // Hide region
      $defRegion
        .addClass('u-display-none')
        .attr('aria-hidden', 'true');
    }

    // Check completion
    if (this.model.areAllItemsCompleted()) {
      this.$el.addClass('is-complete');
    }
  }

}

GlossaryView.template = 'growGlossary.jsx';

export default GlossaryView;
