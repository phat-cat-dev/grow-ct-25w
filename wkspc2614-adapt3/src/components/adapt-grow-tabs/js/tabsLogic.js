/**
 * tabsLogic.js
 *
 * Pure functions for tabs keyboard navigation logic.
 * No Backbone, no DOM — just data transformations for testability.
 *
 * Design ref: TC-3 (pure logic extraction)
 */

/**
 * Direction constants matching keyboard keys.
 */
export const Direction = {
  LEFT: 'Left',
  RIGHT: 'Right',
  HOME: 'Home',
  END: 'End'
};

/**
 * Compute the next active tab index based on keyboard direction.
 *
 * Follows WAI-ARIA tabs pattern:
 * - Left/Right move to adjacent tabs with wraparound
 * - Home goes to first tab
 * - End goes to last tab
 *
 * @param {number} currentIndex - Current active tab index (0-based)
 * @param {string} direction - One of Direction constants
 * @param {number} itemCount - Total number of tabs
 * @returns {number} The new active index
 */
export function computeNextIndex(currentIndex, direction, itemCount) {
  if (itemCount <= 0) return 0;
  if (itemCount === 1) return 0;

  switch (direction) {
    case Direction.HOME:
      return 0;

    case Direction.END:
      return itemCount - 1;

    case Direction.LEFT:
      // Wrap from first to last
      return currentIndex === 0 ? itemCount - 1 : currentIndex - 1;

    case Direction.RIGHT:
      // Wrap from last to first
      return currentIndex === itemCount - 1 ? 0 : currentIndex + 1;

    default:
      return currentIndex;
  }
}

/**
 * Compute the next visitation state after selecting a tab.
 *
 * When a tab is selected, mark it as visited (idempotent).
 *
 * @param {boolean[]} currentVisited - Array of visitation booleans per tab
 * @param {number} selectedIndex - The index being selected
 * @returns {boolean[]} Updated visitation array
 */
export function computeNextVisitation(currentVisited, selectedIndex) {
  const nextVisited = [...currentVisited];
  if (selectedIndex >= 0 && selectedIndex < nextVisited.length) {
    nextVisited[selectedIndex] = true;
  }
  return nextVisited;
}

/**
 * Map keyboard event key to Direction constant.
 *
 * @param {string} key - The KeyboardEvent.key value
 * @returns {string|null} Direction constant or null if not a navigation key
 */
export function keyToDirection(key) {
  switch (key) {
    case 'ArrowLeft':
      return Direction.LEFT;
    case 'ArrowRight':
      return Direction.RIGHT;
    case 'ArrowUp':
      // In vertical mode, up = left
      return Direction.LEFT;
    case 'ArrowDown':
      // In vertical mode, down = right
      return Direction.RIGHT;
    case 'Home':
      return Direction.HOME;
    case 'End':
      return Direction.END;
    default:
      return null;
  }
}
