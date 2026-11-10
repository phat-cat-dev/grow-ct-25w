import Adapt from 'core/js/adapt';
import { mountPlayer } from './player';

// The modal itself comes from Adapt's notify popup, which handles the backdrop, the
// focus trap, Escape and returning focus. This view only supplies the content.
export default class ScenarioPopupView extends Backbone.View {

  className() {
    return 'grow-scenario__popup';
  }

  initialize() {
    this.listenToOnce(Adapt, 'notify:opened', this.onOpened);
    this.listenToOnce(Adapt, 'notify:closed', this.remove);
  }

  render() {
    return this;
  }

  onOpened() {
    const { model } = this;
    const close = () => Adapt.trigger('notify:close');
    this.player = mountPlayer(this.el, model.get('_scenario'), {
      saved: model.getSavedState(),
      headingLevel: 2,
      onChange: flat => model.saveState(flat),
      onComplete: details => model.onScenarioEnded(details),
      onClose: close
    });
    this.player.focus();
  }

  remove() {
    this.player?.destroy();
    this.player = null;
    super.remove();
  }
}
