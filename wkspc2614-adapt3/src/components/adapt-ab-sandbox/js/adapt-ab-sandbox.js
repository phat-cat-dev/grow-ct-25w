import components from 'core/js/components';
import SandboxView from './SandboxView';
import SandboxModel from './SandboxModel';

export default components.register('ab-sandbox', {
  model: SandboxModel,
  view: SandboxView
});
