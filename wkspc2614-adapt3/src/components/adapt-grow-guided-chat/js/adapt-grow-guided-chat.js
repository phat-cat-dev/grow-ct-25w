import components from 'core/js/components';
import ComponentModel from 'core/js/models/componentModel';
import GuidedChatView from './GuidedChatView';

export default components.register('growGuidedChat', {
  model: ComponentModel,
  view: GuidedChatView
});
