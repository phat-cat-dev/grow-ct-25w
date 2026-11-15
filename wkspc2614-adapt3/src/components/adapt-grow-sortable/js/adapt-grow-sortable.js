import components from 'core/js/components';
import SortableView from './SortableView';
import SortableModel from './SortableModel';

export default components.register('growSortable', {
  view: SortableView,
  model: SortableModel
});
