/**
 * adapt-abbott-branching
 *
 * A multi-step decision-scenario engine. The scenario (`_scenario`) is a graph
 * of nodes walked one choice at a time, to arbitrary depth, ending at an
 * outcome node (good / poor / neutral). After each choice the learner reads a
 * consequence before continuing, so the right and wrong routes stay non-obvious;
 * they can restart to try another path.
 *
 * Not graded in the Adapt question sense (no scoring/marking/_recordInteraction);
 * completion fires when the first outcome is reached. See branchingLogic.js for
 * the pure navigation functions and BranchingModel/BranchingView for the engine.
 */

import components from 'core/js/components';
import BranchingModel from './BranchingModel';
import BranchingView from './BranchingView';

export default components.register('branching', {
  model: BranchingModel,
  view: BranchingView
});
