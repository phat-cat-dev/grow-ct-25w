import ComponentView from 'core/js/views/componentView';

class SandboxView extends ComponentView {

  postRender() {
    this.setReadyStatus();
    this.setupInviewCompletion();
  }

}

SandboxView.template = 'sandbox.jsx';

export default SandboxView;
