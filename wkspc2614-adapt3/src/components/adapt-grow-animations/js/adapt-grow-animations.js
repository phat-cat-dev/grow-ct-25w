import components from 'core/js/components';
import ComponentModel from 'core/js/models/componentModel';
import AnimationsView from './AnimationsView';

export default components.register('growAnimations', {
  model: ComponentModel,
  view: AnimationsView
});
