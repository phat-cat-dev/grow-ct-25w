/**
 * WorkedExampleView
 *
 * View for the worked-example component: a collapsible accordion, cloned
 * from ChecklistView's toggle/region pattern. There are no items to tick -
 * opening the region is the whole completion gate, same as checklist's
 * "first open passes the trickle" rule.
 *
 * Design refs: mirrors adapt-abbott-checklist (CL-A accessibility model,
 * CB-4 view/template), stripped of the checkbox/fieldset/progress machinery
 * this component doesn't need.
 */

import ComponentView from 'core/js/views/componentView';

class WorkedExampleView extends ComponentView {

  /**
   * DOM events.
   */
  events() {
    return {
      'click .js-workedexample-toggle': 'onToggle'
    };
  }

  /**
   * Post-render setup.
   */
  postRender() {
    // No images to wait for; set ready immediately
    this.setReadyStatus();

    // Collapsed accordion: completion is on OPEN, same gate as checklist.
    // onToggle() calls setCompletionStatus() the first time the learner
    // opens the worked example, which passes the trickle.

    // Restore reduced motion preference
    this.setupReducedMotion();

    // Restore completion state visual
    if (this.model.get('_isComplete')) {
      this.$el.addClass('is-complete');
    }
  }

  /**
   * Setup reduced motion handling.
   */
  setupReducedMotion() {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.$el.toggleClass('reduce-motion', prefersReducedMotion);
  }

  /**
   * Toggle the accordion open/closed. The FIRST open completes the
   * component (setCompletionStatus), which passes the trickle. className()
   * is only evaluated once at render, so the is-complete class is added
   * here directly rather than relying on a re-render.
   *
   * @param {Event} event
   */
  onToggle(event) {
    const willOpen = !this.$el.hasClass('is-open');
    this.$el.toggleClass('is-open', willOpen);
    this.$(event.currentTarget).attr('aria-expanded', String(willOpen));
    if (willOpen && !this.model.get('_isComplete')) {
      this.setCompletionStatus();
      this.$el.addClass('is-complete');
    }
  }

}

WorkedExampleView.template = 'worked-example.jsx';

export default WorkedExampleView;
