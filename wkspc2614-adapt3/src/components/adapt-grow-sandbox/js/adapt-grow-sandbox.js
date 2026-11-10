import components from 'core/js/components';
import SandboxView from './SandboxView';
import SandboxModel from './SandboxModel';

export default components.register('growSandbox', {
  model: SandboxModel,
  view: SandboxView
});
