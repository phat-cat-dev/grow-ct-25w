import ComponentView from 'core/js/views/componentView';
import notify from 'core/js/notify';
import ScenarioPopupView from './ScenarioPopupView';

class ScenarioView extends ComponentView {

  preRender() {
    this.onLaunch = this.onLaunch.bind(this);
    this.model.set('onLaunch', this.onLaunch);
  }

  postRender() {
    // Reaching an ending completes the component. Viewing the launch card does not.
    this.setReadyStatus();
  }

  onLaunch() {
    notify.popup({
      _view: new ScenarioPopupView({ model: this.model }),
      _isCancellable: true,
      _showCloseButton: true,
      _classes: `grow-scenario is-component ${this.model.get('_classes') || ''}`
    });
  }
}

ScenarioView.template = 'growScenario.jsx';

export default ScenarioView;
