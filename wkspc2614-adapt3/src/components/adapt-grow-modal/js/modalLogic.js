/**
 * modalLogic — pure, DOM-free logic for the modal launcher.
 * No Adapt dependencies; unit-testable in isolation.
 */

export const COMPLETION = {
  TRIGGER: 'trigger',   // complete when the learner opens the popup (default)
  VIEW: 'view',         // complete when the component scrolls into view
  NONE: 'none'          // never auto-completes
};

/**
 * Resolve the configured completion mode to a known value.
 * Anything unrecognised (incl. undefined) falls back to TRIGGER.
 */
export function resolveCompletionMode(mode) {
  return (mode === COMPLETION.VIEW || mode === COMPLETION.NONE) ? mode : COMPLETION.TRIGGER;
}

/**
 * Build the options object passed to Adapt.notify.popup from the authored
 * `_popup` block. Always namespaces the popup with `cm-modal` (plus `cm-notify`
 * so the themed popup styles apply) ahead of any author `_classes`, and defaults
 * the popup to cancellable.
 */
export function buildPopupOptions(popup = {}, baseClasses = 'cm-notify cm-modal') {
  const classes = [baseClasses, popup._classes].filter(Boolean).join(' ');
  return {
    title: popup.title || '',
    body: popup.body || '',
    _classes: classes,
    _isCancellable: popup._isCancellable !== false
  };
}
