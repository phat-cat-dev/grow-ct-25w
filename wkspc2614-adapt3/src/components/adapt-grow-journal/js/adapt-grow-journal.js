/**
 * adapt-grow-journal
 *
 * A lined "notebook" text field for learner-authored writing (reflections,
 * private notes) that has no correct answer. Part of the GROW plugin set.
 *
 * Extends ComponentModel, NOT QuestionModel — stays outside the scoring
 * machinery entirely. Persists via offlineStorage custom keys into
 * cmi.suspend_data, not cmi.interactions (avoids 250-char truncation and
 * false result:incorrect).
 *
 * Same structure as adapt-abbott-opentext; the journal differs only in its
 * ruled, paper-like presentation.
 */

import components from 'core/js/components';
import JournalView from './JournalView';
import JournalModel from './JournalModel';

export default components.register('growJournal', {
  view: JournalView,
  model: JournalModel
});
