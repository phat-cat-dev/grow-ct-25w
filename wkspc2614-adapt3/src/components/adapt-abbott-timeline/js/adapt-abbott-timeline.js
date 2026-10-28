/**
 * adapt-abbott-timeline
 *
 * A vertical ordered-process display: stages along a marked axis,
 * whole process visible at once, per-stage detail expanding in place.
 * Ordinal, not scalar — stages at equal spacing in authored order.
 *
 * Extends ItemsComponentModel for per-item visitation tracking.
 * NOT a question component — no marking, no _recordInteraction,
 * no response semantics. The base class's _userAnswer array is
 * legitimate persistence plumbing for visitation state only.
 *
 * See: docs/authoring/component-specs/timeline.md
 */

import components from 'core/js/components';
import TimelineView from './TimelineView';
import TimelineModel from './TimelineModel';

export default components.register('timeline', {
  view: TimelineView,
  model: TimelineModel
});
