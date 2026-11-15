/**
 * adapt-grow-accordion
 *
 * A Bootstrap-accordion-shaped component: a stack of header buttons that
 * expand/collapse panels. Single-open by default (opening one closes the
 * others); _isMultiSelect allows several open at once.
 *
 * Extends ItemsComponentModel for per-item visitation; completion is reached
 * when every panel has been opened at least once.
 *
 * See: docs/adapt-ab-components-sketch.md
 */

import components from 'core/js/components';
import AccordionView from './AccordionView';
import AccordionModel from './AccordionModel';

export default components.register('growAccordion', {
  view: AccordionView,
  model: AccordionModel
});
