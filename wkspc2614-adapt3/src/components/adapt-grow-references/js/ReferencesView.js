import ComponentView from 'core/js/views/componentView';

class ReferencesView extends ComponentView {

  postRender() {
    this.setReadyStatus();
    // Lesson Sources has nothing to interact with, so complete it on view —
    // otherwise it stays incomplete and blocks page/trickle completion
    // (Abbott, 10 Oct 2026). setupInviewCompletion is core ComponentView's
    // standard inview-completion helper (as used by contrib text/graphic).
    this.setupInviewCompletion('.grow-references__widget');
  }

}

ReferencesView.template = 'growReferences.jsx';

export default ReferencesView;
