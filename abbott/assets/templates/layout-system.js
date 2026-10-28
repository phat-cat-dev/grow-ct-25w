export const DEFAULT_LAYOUT = { radius: 16 };
export function validateLayout(value = DEFAULT_LAYOUT) {
  const state = { ...DEFAULT_LAYOUT, ...value };
  if (typeof state.radius !== 'number' || !Number.isFinite(state.radius) || state.radius < 0 || state.radius > 48) {
    throw new Error('Invalid layout corner radius. Use a number from 0 to 48 pixels.');
  }
  return state;
}
export function layoutCss(value) {
  const { radius } = validateLayout(value);
  return `/* Layout corner radius */
:root { --radius-sm: ${radius / 2}px; --radius: ${radius}px; --radius-lg: ${radius * 1.5}px; --ab-btn-radius: ${radius}px; --ab-btn-radius-sm: ${radius / 2}px; --ab-btn-radius-lg: ${radius}px; --ab-card-radius: ${radius}px; --ab-callout-radius: ${radius}px; --ab-acc-radius: ${radius}px; }
.rail, .site-area, .card-doc, .connector-panel, .harmony-demo-panel, .harm-card, .motion-sample, .fluid-card, .ab.accordion .accordion-item { border-radius: var(--radius); }
#base-colour-lock, #scheme-open, .stage-theme-actions button, .theme-toggle button, .harm-swatches button.hsw, .layout-preview-button { border-radius: var(--radius); }
.ab.btn:not(.square):not(.pill) { border-radius: var(--radius); }
:root :is(.active-source-chip, .rail, .site-area, .card-doc, .connector-panel, .harmony-preset-panel, .harmony-demo-panel, .harm-card, .motion-sample, .fluid-card, .fluid-stage, .fluid-type-scale, .fluid-settings fieldset, .color-selection, .placeholder, .structure-notice, .panel, .scale, pre, .area-number) { border-radius: var(--radius); }
:root :is(#base-colour-lock, #scheme-open, #scheme-tools button, .connector-panel button, .connector-controls button, .stage-theme-actions button, .theme-toggle button, .harm-card .demobtn, .harm-swatches button.hsw, .hovmodes label) { border-radius: var(--radius); }
:root :is(.connector-panel input:not([type="range"]):not([type="checkbox"]):not([type="radio"]), .connector-panel select, .color-selection select, #scheme-tools input, #scheme-tools select, #scheme-tools textarea, code, kbd, .connector-badge) { border-radius: var(--radius-sm); }
:root .area-trigger:focus-visible { border-radius: var(--radius); }
:root .ab.accordion:not(.intext) .accordion-item { border-radius: var(--radius); }
`;
}
