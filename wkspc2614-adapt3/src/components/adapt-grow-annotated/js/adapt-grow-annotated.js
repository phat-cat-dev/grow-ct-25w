/**
 * adapt-grow-annotated
 *
 * Annotated exemplar component: a passage of sample text where marked
 * spans carry explanatory notes. Presentational, NOT graded.
 *
 * Design refs: AE-1 (plugin/schema), AB-1 (package)
 */

import components from 'core/js/components';
import AnnotatedModel from './AnnotatedModel';
import AnnotatedView from './AnnotatedView';

export default components.register('growAnnotated', {
  model: AnnotatedModel,
  view: AnnotatedView
});
