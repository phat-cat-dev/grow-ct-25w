import components from 'core/js/components';
import ConfidenceView from './ConfidenceView';
import ConfidenceModel from './ConfidenceModel';

export default components.register('growConfidence', {
  view: ConfidenceView,
  model: ConfidenceModel
});
