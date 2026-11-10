import components from 'core/js/components';
import ScenarioModel from './ScenarioModel';
import ScenarioView from './ScenarioView';

export default components.register('growScenario', {
  model: ScenarioModel,
  view: ScenarioView
});
