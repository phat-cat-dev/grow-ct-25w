/**
 * collapseLogic — pure, DOM-free logic for the ab-collapse extension.
 * No Adapt/DOM dependencies; unit-testable in isolation.
 */

/**
 * Resolve a trigger's data-* attributes into collapse options.
 *
 *   data-ab-collapse="<selector>"         the target(s) to toggle
 *   data-ab-collapse-parent="<selector>"  optional: close sibling open
 *                                         collapses within this ancestor first
 *                                         (accordion-style, exclusive)
 *
 * @param {Object} dataset
 * @returns {{ selector: (string|null), parent: (string|null) }}
 */
export function resolveCollapse(dataset = {}) {
  const raw = dataset.abCollapse;
  const selector = (raw && raw !== 'true') ? String(raw).trim() : null;
  const parent = dataset.abCollapseParent ? String(dataset.abCollapseParent).trim() : null;
  return { selector: selector || null, parent: parent || null };
}

/**
 * The aria-expanded string for a state.
 * @param {boolean} isOpen
 * @returns {"true"|"false"}
 */
export function ariaExpanded(isOpen) {
  return isOpen ? 'true' : 'false';
}
