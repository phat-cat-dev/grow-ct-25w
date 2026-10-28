/*
 * adapt-gow-textTagging
 * Entry point - registers the component with Adapt.
 *
 * Behaviour ported from pw02's text-tagging activity; data model ported from
 * congen11's text-tagging activity schema. See TextTaggingModel.js,
 * TextTaggingView.js and ../README.md for full detail on both sources and the
 * bugs fixed (not ported) along the way.
 */
import Adapt from 'core/js/adapt';
import TextTaggingModel from './TextTaggingModel';
import TextTaggingView from './TextTaggingView';

export default Adapt.register('textTagging', {
  model: TextTaggingModel,
  view: TextTaggingView
});
