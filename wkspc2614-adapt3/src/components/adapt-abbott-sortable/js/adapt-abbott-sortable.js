import components from 'core/js/components';
import SortableView from './SortableView';
import SortableModel from './SortableModel';

export default components.register('sortable', {
  view: SortableView,
  model: SortableModel
});
