/**
 * adapt-grow-reflection-module
 *
 * A composed reflection activity for the Adapt framework: a lined "sketchbook"
 * journal where the learner develops a thought, paired with a "change the lens"
 * panel of reframing prompts. Part of the GROW plugin set.
 *
 * The writing half reuses the proven adapt-grow-journal behaviour (extends
 * ComponentModel, persists to suspend_data, never scored); the lens prompts are
 * static authored content.
 */

import components from 'core/js/components';
import ReflectionModuleView from './ReflectionModuleView';
import ReflectionModuleModel from './ReflectionModuleModel';

export default components.register('growReflectionModule', {
  view: ReflectionModuleView,
  model: ReflectionModuleModel
});
