/**
 * navigationLogic — pure, DOM-free helpers for the ab-navigation adapter.
 * No Adapt/DOM dependencies; unit-testable in isolation.
 */

/**
 * Normalise author-configured custom nav items into a clean spec list.
 * Keeps only items that have something to show (label or icon) AND an action
 * (a url, a core data-event, or an ab-modal id).
 *
 * @param {Array<Object>} items - from _abNavigation._items
 * @returns {Array<{label:string,icon:string,order:number,url:string,event:string,abModal:string,classes:string}>}
 */
export function normaliseItems(items) {
  return (items || []).map((it, i) => {
    const rawOrder = (it && (it._order !== undefined ? it._order : it.order));
    const order = Number.isFinite(Number(rawOrder)) ? Number(rawOrder) : (50 + i);
    return {
      label: (it && (it.label || it.title)) || '',
      icon: (it && (it._icon || it.icon)) || '',
      order,
      url: (it && (it._url || it.url)) || '',
      event: (it && (it._event || it.event)) || '',
      abModal: (it && (it._abModal || it.abModal)) || '',
      classes: (it && it._classes) || ''
    };
  }).filter(it => (it.label || it.icon) && (it.url || it.event || it.abModal));
}

/**
 * Index at which to insert a new item (by data-order) among existing items,
 * so the nav stays ordered: before the first existing order greater than the
 * new one, else at the end.
 *
 * @param {number[]} existingOrders - existing items' data-order, in DOM order
 * @param {number} order
 * @returns {number}
 */
export function insertionIndex(existingOrders, order) {
  for (let i = 0; i < existingOrders.length; i++) {
    if (existingOrders[i] > order) return i;
  }
  return existingOrders.length;
}
