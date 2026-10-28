/**
 * adapt-grow-memory
 *
 * Memory match: a tile-flip pairs game. The author supplies an array of pairs
 * (each a Material Symbol icon and/or a short text); the component builds a deck
 * of two of each, shuffles it, and renders a responsive grid of tiles. Turning
 * two tiles over compares them: a match stays revealed, a mismatch turns both
 * back over after a short pause. The game is won when every pair has been found.
 *
 * Extends ComponentModel (NOT QuestionModel) — it stays entirely outside the
 * scoring machinery. There is no marking, no cmi.interactions and no score;
 * completion is formative and author-toggled (_isCompletionBearing).
 *
 * Mirrors the structure of adapt-abbott-opentext / adapt-abbott-flipcard
 * (components.register + Model/View split + .jsx template + schema globals) and
 * the GROW naming of adapt-grow-levels (_component: "growMemory").
 */

import components from 'core/js/components';
import MemoryView from './MemoryView';
import MemoryModel from './MemoryModel';

export default components.register('growMemory', {
  view: MemoryView,
  model: MemoryModel
});
