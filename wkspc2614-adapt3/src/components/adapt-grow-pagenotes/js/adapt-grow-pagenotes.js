import components from 'core/js/components';
import ComponentModel from 'core/js/models/componentModel';
import PageNotesView from './PageNotesView';

export default components.register('growPageNotes', {
  model: ComponentModel,
  view: PageNotesView
});
