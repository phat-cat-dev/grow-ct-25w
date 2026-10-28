/**
 * ModalModel — model for the modal launcher.
 * Extends ComponentModel (NOT a question/items model): no marking, no response
 * semantics. Just resolves the completion mode and exposes the popup block.
 */

import ComponentModel from 'core/js/models/componentModel';
import { resolveCompletionMode } from './modalLogic';

export default class ModalModel extends ComponentModel {

  /** Resolved completion mode: 'trigger' (default) | 'view' | 'none'. */
  getCompletionMode() {
    return resolveCompletionMode(this.get('_completion'));
  }

  /** The authored popup block ({ title, body, _classes, _isCancellable }). */
  getPopup() {
    return this.get('_popup') || {};
  }

}
