/*
 * adapt-grow-text-tagging
 * Entry point - registers the component with Adapt.
 *
 * Ported to the 5.x React (.jsx) pipeline: components.register + a React
 * template (was Adapt.register + Handlebars). This is a QUESTION component,
 * so the View extends QuestionView and the Model extends QuestionModel -
 * marking, buttons and feedback are managed by QuestionView.
 *
 * Behaviour ported from pw02's grow-text-tagging activity; data model ported from
 * congen11's grow-text-tagging activity schema. See TextTaggingModel.js,
 * TextTaggingView.js and ../README.md for full detail on both sources and the
 * bugs fixed (not ported) along the way.
 */
import components from 'core/js/components';
import TextTaggingModel from './TextTaggingModel';
import TextTaggingView from './TextTaggingView';

TextTaggingView.template = 'growTextTagging.jsx';

export default components.register('growTextTagging', {
  model: TextTaggingModel,
  view: TextTaggingView
});
