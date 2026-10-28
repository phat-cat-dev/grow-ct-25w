/*
 * adapt-gow-keyTerm
 * Static display component - ported from congen11's `key-term` component schema.
 * See ../README.md for the field-mapping rationale and the v5 (AMD) equivalent.
 */
import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class KeyTermView extends ComponentView {

  events() {
    return {
      'click .js-keyterm-reveal': 'onReveal'
    };
  }

  // When _reveal is set, the definition, example and related terms are hidden
  // behind one button that reveals the next section on each click, then hides
  // itself once everything is shown.
  onReveal(event) {
    const root = this.el;
    const hidden = root.querySelectorAll('.key-term__reveal-section[hidden]');
    if (!hidden.length) return;
    const next = hidden[0];
    next.removeAttribute('hidden');
    next.setAttribute('aria-hidden', 'false');

    const remaining = root.querySelectorAll('.key-term__reveal-section[hidden]');
    const button = event.currentTarget;
    if (!remaining.length) {
      button.setAttribute('hidden', '');
      return;
    }
    const label = button.querySelector('.js-keyterm-reveal-label');
    if (!label) return;
    const upcoming = remaining[0];
    label.textContent = upcoming.classList.contains('key-term__example')
      ? 'Show example'
      : upcoming.classList.contains('key-term__related-terms')
        ? 'Show related terms'
        : 'Show more';
  }

  // Purely presentational. ComponentView.postRender() is a no-op, so the
  // component must signal ready/completion itself or the page never fires
  // contentObjectView:ready and the loading screen never lifts.
  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__inner');
  }

}

export default Adapt.register('keyTerm', {
  view: KeyTermView,
  model: ComponentModel
});
