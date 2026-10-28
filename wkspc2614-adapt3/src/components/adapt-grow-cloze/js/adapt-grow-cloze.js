/**
 * adapt-grow-cloze
 *
 * Fill-the-blanks (cloze) formative activity. The learner chooses a word from a
 * dropdown for each inline blank in a sentence, then selects Check. Each blank is
 * marked correct/incorrect (non-visually as well as by colour) and an overall
 * feedback message is announced politely.
 *
 * Matured from the "Fill the blanks" gallery pattern (abbott/assets/gallery/
 * patterns-3.html) and generalised to any number of blanks.
 *
 * FORMATIVE, NOT ASSESSED: extends ComponentModel (NOT QuestionModel). It records
 * no cmi.interactions and produces no score. It may optionally complete on the
 * first Check when _isCompletionBearing is true; that completion is informational.
 */
import components from 'core/js/components';
import ClozeView from './ClozeView';
import ClozeModel from './ClozeModel';

export default components.register('growCloze', {
  view: ClozeView,
  model: ClozeModel
});
