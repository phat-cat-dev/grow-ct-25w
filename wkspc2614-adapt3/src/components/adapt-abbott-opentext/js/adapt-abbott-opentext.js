/**
 * adapt-abbott-opentext
 *
 * A general-purpose open-text component for learner-authored writing
 * (reflective prompts, notes) that has no correct answer.
 *
 * Extends ComponentModel, NOT QuestionModel — stays outside the scoring
 * machinery entirely. Persists via offlineStorage custom keys into
 * cmi.suspend_data, not cmi.interactions (avoids 250-char truncation
 * and false result:incorrect).
 *
 * See: docs/authoring/component-specs/opentext.md
 */

import components from 'core/js/components';
import OpenTextView from './OpenTextView';
import OpenTextModel from './OpenTextModel';

export default components.register('opentext', {
  view: OpenTextView,
  model: OpenTextModel
});
