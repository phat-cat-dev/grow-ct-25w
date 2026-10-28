/**
 * adapt-abbott-glossary
 *
 * Glossary passage component: a passage of teaching prose where marked
 * terms reveal their definitions in place. Presentational, NOT graded.
 *
 * Design refs: GL-1 (plugin/schema), GB-1 (package)
 */

import components from 'core/js/components';
import GlossaryModel from './GlossaryModel';
import GlossaryView from './GlossaryView';

export default components.register('glossary', {
  model: GlossaryModel,
  view: GlossaryView
});
