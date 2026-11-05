/**
 * flipbuttonLogic — pure, DOM-free logic for the ab-flipbutton extension.
 * No Adapt/DOM dependencies; unit-testable in isolation.
 */

/**
 * Compute the next flipped state from the current one.
 * @param {boolean} isFlipped
 * @returns {boolean}
 */
export function nextFlipped(isFlipped) {
  return !isFlipped;
}

/**
 * The aria-pressed string for a state.
 * @param {boolean} isFlipped
 * @returns {"true"|"false"}
 */
export function ariaPressed(isFlipped) {
  return isFlipped ? 'true' : 'false';
}
