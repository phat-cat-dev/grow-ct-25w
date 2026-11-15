import components from 'core/js/components';
import CorkboardModel from './CorkboardModel';
import CorkboardView from './CorkboardView';

export default components.register('growCorkboard', {
  model: CorkboardModel,
  view: CorkboardView
});
