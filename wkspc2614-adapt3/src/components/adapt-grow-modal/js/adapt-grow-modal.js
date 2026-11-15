/**
 * adapt-grow-modal
 *
 * Modal launcher: a trigger (button) that FOREGROUNDS authored content in the
 * Adapt notify popup — the same modal the hotgraphic hotspots and question
 * feedback use, themed light/dark by cm-notify.less. Use it to pull an activity,
 * worked example, definition or "try this" panel out of the page flow and into a
 * focused, dimmed-backdrop overlay (GROW, 10 Oct 2026: "get at the modal
 * process Adapt uses — they are great for foregrounding activities").
 *
 * Presentational launcher, NOT a graded question: no marking, no interaction
 * recording. The popup body is authored HTML. Completion fires on open by
 * default (engagement), configurable to on-view or none.
 */

import components from 'core/js/components';
import ModalModel from './ModalModel';
import ModalView from './ModalView';

export default components.register('growModal', {
  model: ModalModel,
  view: ModalView
});
