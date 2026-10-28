/**
 * adapt-abbott-checklist
 *
 * Checklist component: a set of concrete, tickable actions the learner
 * works through before or after a task. A working aid, not an assessment.
 * Presentational, NOT graded: no marking, no _recordInteraction, no
 * response semantics.
 *
 * Design refs: CL-1 (plugin/schema), CB-1 (package)
 */

import components from 'core/js/components';
import ChecklistModel from './ChecklistModel';
import ChecklistView from './ChecklistView';

export default components.register('checklist', {
  model: ChecklistModel,
  view: ChecklistView
});
