/**
 * BranchingView
 *
 * View for the branching scenario engine. The JSX template renders whatever the
 * model's current node is; this view only wires the clicks (choose a choice,
 * continue past a consequence, restart) and re-renders the React template when
 * the model's navigation state changes. Event handlers are delegated from the
 * component root, so they survive each ReactDOM re-render.
 */

import ComponentView from 'core/js/views/componentView';

class BranchingView extends ComponentView {

  events() {
    return {
      'click .js-grow-branching-choice': 'onChoice',
      'click .js-grow-branching-continue': 'onContinue',
      'click .js-grow-branching-restart': 'onRestart'
    };
  }

  preRender() {
    // Re-render the JSX whenever the learner moves through the scenario.
    this.listenTo(this.model, 'change:_currentNode change:_pendingChoice', this.onStateChange);
  }

  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion('.component__widget');
  }

  onStateChange() {
    this.changed();
    // Move focus to the newly revealed region so keyboard/screen-reader users
    // land on the new content rather than staying on a now-replaced button.
    requestAnimationFrame(() => {
      const target = this.$('.grow-branching__consequence, .grow-branching__outcome')[0];
      if (target) target.focus();
    });
  }

  onChoice(event) {
    const index = parseInt(event.currentTarget.getAttribute('data-index'), 10);
    if (Number.isNaN(index)) return;
    this.model.choose(index);
  }

  onContinue() {
    this.model.advance();
  }

  onRestart() {
    this.model.restart();
  }

}

BranchingView.template = 'growBranching.jsx';

export default BranchingView;
