/**
 * adapt-abbott-tooltip — pure positioning logic (no DOM, unit-testable).
 *
 * Kept separate from the DOM behaviour so the geometry can be tested in node
 * without a browser (see test/unit/tooltipLogic.test.js), per the repo's
 * "prove, don't claim" discipline.
 *
 * @author Abbott
 * @license GPL-3.0
 */

/**
 * Decide where the tooltip bubble sits relative to its trigger.
 *
 * Coordinates are viewport-relative (as from getBoundingClientRect), so the
 * caller positions the bubble with `position: fixed`.
 *
 * Preference: above the trigger; flip below if there isn't room above.
 * Horizontally: centre on the trigger, then clamp inside the viewport so the
 * bubble never runs off either edge.
 *
 * @param {{top:number,left:number,width:number,height:number}} trigger
 * @param {{width:number,height:number}} bubble
 * @param {{width:number,height:number}} viewport
 * @param {number} [gap=8] gap in px between trigger and bubble, and min edge margin
 * @returns {{top:number,left:number,placement:'top'|'bottom'}}
 */
export function computePlacement(trigger, bubble, viewport, gap = 8) {
  const centreX = trigger.left + trigger.width / 2;

  // horizontal: centre then clamp within [gap, viewport.width - bubble.width - gap]
  let left = centreX - bubble.width / 2;
  const maxLeft = viewport.width - bubble.width - gap;
  // when the bubble is wider than the viewport, pin to the left gap
  left = maxLeft < gap ? gap : Math.max(gap, Math.min(left, maxLeft));

  // vertical: prefer above; flip below if it would clip the top
  let placement = 'top';
  let top = trigger.top - bubble.height - gap;
  if (top < gap) {
    placement = 'bottom';
    top = trigger.top + trigger.height + gap;
    // if below also overflows the bottom, clamp upward
    if (top + bubble.height + gap > viewport.height) {
      top = Math.max(gap, viewport.height - bubble.height - gap);
    }
  }

  return { top, left, placement };
}
