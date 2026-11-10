/**
 * AnnotatedView
 *
 * View for the annotated exemplar component. Renders the passage as
 * continuous prose with inline marker buttons for annotated segments.
 *
 * Accessibility: markers are native <button>s with aria-expanded and
 * aria-controls. Focus moves to the note region on expansion; a back
 * control returns focus to the marker.
 *
 * Design refs: AE-A (accessibility model), AB-4 (view/template)
 */

import ComponentView from 'core/js/views/componentView';

class AnnotatedView extends ComponentView {

  /**
   * DOM events.
   */
  events() {
    return {
      'click .js-grow-annotated-marker': 'onMarkerClick',
      'click .js-grow-annotated-back': 'onBackClick'
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

    // Toggle the note
    this.model.toggleNote(index);
  }

  /**
   * Handle back-to-passage button click.
   * @param {Event} event
   */
  onBackClick(event) {
    event.preventDefault();

    // Remember which marker to return to
    const returnIndex = this._lastClickedMarkerIndex;

    // Close the note
    this.model.closeNote();

    // Return focus to the marker
    if (returnIndex !== null) {
      const $marker = this.$(`.js-grow-annotated-marker[data-index="${returnIndex}"]`);
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
    this.$('.js-grow-annotated-marker').each((i, marker) => {
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

    // Update note region visibility
    const $noteRegion = this.$('.js-grow-annotated-note-region');

    if (expandedIndex !== null) {
      const notes = this.model.getNotes();
      const note = notes[expandedIndex];

      if (note) {
        // Update note content
        this.$('.js-grow-annotated-note-title').text(note.title);
        this.$('.js-grow-annotated-note-referent').text(`"${note.text}"`);
        this.$('.js-grow-annotated-note-body').html(note.body);

        // Show region
        $noteRegion
          .removeClass('u-display-none')
          .attr('aria-hidden', 'false');

        // Move focus to note region
        $noteRegion.focus();
      }
    } else {
      // Hide region
      $noteRegion
        .addClass('u-display-none')
        .attr('aria-hidden', 'true');
    }

    // Check completion
    if (this.model.areAllItemsCompleted()) {
      this.$el.addClass('is-complete');
    }
  }

}

AnnotatedView.template = 'growAnnotated.jsx';

export default AnnotatedView;
