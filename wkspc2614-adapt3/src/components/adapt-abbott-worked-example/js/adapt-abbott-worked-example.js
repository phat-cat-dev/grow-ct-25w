/**
 * adapt-abbott-worked-example
 *
 * Worked-example component: a collapsible accordion carrying the
 * weaker-then-stronger worked-example prose (merge-context.js's wrapProse()
 * applies the we-weaker/we-stronger cue classes to its paragraphs before
 * this component ever sees the body). Cloned from adapt-abbott-checklist's
 * toggle+region pattern, stripped of the checkbox/fieldset/progress
 * machinery this component doesn't need - there are no items, just one
 * prose body.
 *
 * Presentational, NOT graded: no marking, no _recordInteraction, no
 * response semantics. Completion fires on first open, same gate as
 * checklist, passing the trickle.
 */

import components from 'core/js/components';
import WorkedExampleModel from './WorkedExampleModel';
import WorkedExampleView from './WorkedExampleView';

export default components.register('workedExample', {
  model: WorkedExampleModel,
  view: WorkedExampleView
});
