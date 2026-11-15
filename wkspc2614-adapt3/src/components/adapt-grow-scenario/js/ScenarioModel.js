import ComponentModel from 'core/js/models/componentModel';

export default class ScenarioModel extends ComponentModel {

  defaults() {
    return ComponentModel.resultExtend('defaults', {
      _completionOn: 'ending',
      _launch: {},
      _lastResult: null
    });
  }

  // _userAnswer holds a flat list of integers. It is stored only when the Spoor
  // tracking setting _shouldStoreResponses is on, and never includes private notes.
  saveState(flat) {
    this.set('_userAnswer', flat.slice());
  }

  getSavedState() {
    return this.get('_userAnswer');
  }

  hasStarted() {
    const saved = this.getSavedState();
    return Array.isArray(saved) && saved.length > 0;
  }

  onScenarioEnded({ result }) {
    this.set('_lastResult', result);
    const needsPass = this.get('_completionOn') === 'pass';
    if (!needsPass || result === 'pass') this.setCompletionStatus();
  }
}
