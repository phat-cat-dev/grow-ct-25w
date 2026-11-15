/**
 * AccordionView
 *
 * View for the grow-accordion component. Extends ComponentView.
 *
 * Accessibility model:
 * - Each header is a native <button> inside an element with role (heading level
 *   from the block level), carrying aria-expanded and aria-controls.
 * - Each panel is role="region" + aria-labelledby its header button.
 * - Toggling does not move focus; native button keyboard semantics only.
 */

import ComponentView from 'core/js/views/componentView';

class AccordionView extends ComponentView {

  events() {
    return {
      'click .grow-accordion__header-btn': 'onHeaderClick'
    };
  }

  preRender() {
    this.listenTo(this.model.getChildren(), 'change:_isOpen', this.onOpenChange);
  }

  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__widget');
  }

  onHeaderClick(event) {
    const index = parseInt(this.$(event.currentTarget).data('index'), 10);
    if (!Number.isNaN(index)) this.model.toggleItem(index);
  }

  onOpenChange() {
    this.changed();
  }

}

AccordionView.template = 'grow-accordion.jsx';

export default AccordionView;
