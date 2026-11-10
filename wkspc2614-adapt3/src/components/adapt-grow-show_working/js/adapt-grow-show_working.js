/**
 * adapt-grow-show_working
 *
 * "Show your working" — a step-by-step worked solution for the Adapt framework.
 * Each line arrives in turn with the move annotated, and the final answer is
 * checked by substitution with a tick that draws on. Part of the GROW plugin set.
 *
 * Presentation component: no learner input, no scoring. Uses the stock
 * ComponentModel; the view handles the inview-triggered reveal and completion.
 */

import components from 'core/js/components';
import ComponentModel from 'core/js/models/componentModel';
import ShowWorkingView from './ShowWorkingView';

export default components.register('growShowWorking', {
  model: ComponentModel,
  view: ShowWorkingView
});
