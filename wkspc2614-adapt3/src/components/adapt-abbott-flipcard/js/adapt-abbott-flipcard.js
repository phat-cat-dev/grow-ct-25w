/**
 * adapt-abbott-flipcard
 *
 * A presentational card-set component with front and back faces.
 * Cards flip to reveal back content on selection. Supports text-front
 * and/or image-front. Completion by visiting all cards.
 *
 * Extends ItemsComponentModel for per-item visitation tracking.
 * NOT a question component — no marking, no _recordInteraction,
 * no response semantics. The base class's _userAnswer array is
 * legitimate persistence plumbing for visitation state only.
 *
 * See: docs/authoring/component-specs/flipcard.md
 */

import components from 'core/js/components';
import FlipcardView from './FlipcardView';
import FlipcardModel from './FlipcardModel';

export default components.register('flipcard', {
  view: FlipcardView,
  model: FlipcardModel
});
