/**
 * ChecklistView
 *
 * View for the checklist component. Renders a set of native checkboxes
 * with properly associated labels.
 *
 * Accessibility: native <input type="checkbox"> with associated <label>
 * elements. The set is grouped with a programmatic label via fieldset/legend.
 * Focus stays on the ticked control (no movement). Native checkbox provides
 * keyboard operation and state announcement for free.
 *
 * Design refs: CL-A (accessibility model), CB-4 (view/template)
 */

import ComponentView from 'core/js/views/componentView';

class ChecklistView extends ComponentView {

  /**
   * DOM events.
   */
  events() {
    return {
      'change .js-grow-checklist-input': 'onCheckboxChange',
      'click .js-grow-checklist-toggle': 'onToggle'
    };
  }

  /**
   * Pre-render setup.
   */
  preRender() {
    this.listenTo(this.model, 'change:_checkedMap', this.onCheckedChange);
  }

  /**
   * Post-render setup.
   */
  postRender() {
    // No images to wait for; set ready immediately
    this.setReadyStatus();

    // Collapsed accordion: completion is on OPEN, not on view. onToggle() calls
    // setCompletionStatus() the first time the learner opens the checklist, which
    // passes the trickle. Ticking the items stays a self-assessment aid.

    // Restore reduced motion preference
    this.setupReducedMotion();

    // Restore completion state visual
    if (this.model.get('_isComplete')) {
      this.$el.addClass('is-complete');
    }

    // Reset checked state on re-visit (CL-2: ticks do not persist)
    // Note: completion status is already restored by framework
    this.model.resetCheckedState();

    // Update progress display
    this.updateProgress();
  }

  /**
   * Setup reduced motion handling.
   */
  setupReducedMotion() {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.$el.toggleClass('reduce-motion', prefersReducedMotion);
  }

  /**
   * Handle checkbox change.
   *
   * @param {Event} event
   */
  onCheckboxChange(event) {
    const $input = this.$(event.currentTarget);
    const index = parseInt($input.data('index'), 10);

    // Toggle the item
    this.model.toggleItem(index);

    // Focus stays on the checkbox (no movement per CL-A)
  }

  /**
   * Toggle the accordion open/closed. The FIRST open completes the component
   * (setCompletionStatus), which passes the trickle; ticking stays optional.
   *
   * @param {Event} event
   */
  onToggle(event) {
    const willOpen = !this.$el.hasClass('is-open');
    this.$el.toggleClass('is-open', willOpen);
    this.$(event.currentTarget).attr('aria-expanded', String(willOpen));
    if (willOpen && !this.model.get('_isComplete')) {
      this.setCompletionStatus();
    }
  }

  /**
   * Handle checked state change.
   */
  onCheckedChange() {
    const componentId = this.model.get('_id');
    const items = this.model.getChildren();

    // Update all checkboxes
    items.forEach((item, index) => {
      const isChecked = this.model.isItemChecked(index);
      const isVisited = item.get('_isVisited');
      const $input = this.$(`.js-grow-checklist-input[data-index="${index}"]`);
      const $item = $input.closest('.grow-checklist__item');

      // Update checkbox state
      $input.prop('checked', isChecked);

      // Update item classes
      $item.toggleClass('is-checked', isChecked);
      $item.toggleClass('is-visited', isVisited);
    });

    // Update progress
    this.updateProgress();

    // Check completion
    if (this.model.areAllItemsCompleted()) {
      this.$el.addClass('is-complete');
    }
  }

  /**
   * Update the progress count display.
   */
  updateProgress() {
    const checked = this.model.getCheckedCount();
    const total = this.model.getItemCount();
    const $progress = this.$('.js-grow-checklist-progress');

    if ($progress.length) {
      $progress.text(`${checked} of ${total} checked`);
    }
  }

}

ChecklistView.template = 'growChecklist.jsx';

export default ChecklistView;
