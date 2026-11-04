/**
 * WorkedExampleModel
 *
 * Model for the worked-example component. Extends the plain ComponentModel
 * (not ItemsComponentModel, as checklist does) - there are no items, just a
 * single prose body carrying the weaker-then-stronger contrast.
 *
 * No custom state: completion is driven entirely by the view's open/close
 * toggle (see WorkedExampleView#onToggle), the same accordion gate as
 * checklist, so the base class's _isComplete handling is sufficient.
 */

import ComponentModel from 'core/js/models/componentModel';

export default class WorkedExampleModel extends ComponentModel {}
