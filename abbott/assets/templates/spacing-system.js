import { FLUID_CORE_CSS } from './fluid-core.js';

export const DEFAULT_SPACING = Object.freeze({
  viewportMin: 20, viewportMax: 45,
  textMin: .75, textMax: 1,
  spaceMin: .75, spaceMax: 1,
  layoutMin: .75, layoutMax: 1,
  iconMin: 1.5, iconMax: 2.5,
});
export const SPACING_PROFILES = Object.freeze({
  default: DEFAULT_SPACING,
  compact: Object.freeze({ ...DEFAULT_SPACING, spaceMin: .5, spaceMax: .75, layoutMin: .5, layoutMax: .75 }),
  roomy: Object.freeze({ ...DEFAULT_SPACING, viewportMax: 80, spaceMin: 1, spaceMax: 1.5, layoutMin: 1, layoutMax: 1.5 }),
});
const settings = {
  viewportMin: '--ab-fluid-vp-min', viewportMax: '--ab-fluid-vp-max',
  textMin: '--ab-fluid-text-min', textMax: '--ab-fluid-text-max',
  spaceMin: '--ab-fluid-space-min', spaceMax: '--ab-fluid-space-max',
  layoutMin: '--ab-fluid-layout-min', layoutMax: '--ab-fluid-layout-max',
  iconMin: '--ab-fluid-icon-min', iconMax: '--ab-fluid-icon-max',
};

export function validateSpacing(value = {}) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new TypeError('Spacing settings must be an object');
  const state = { ...DEFAULT_SPACING, ...value };
  for (const key of Object.keys(settings)) {
    const max = key.startsWith('viewport') ? 120 : key.startsWith('icon') ? 6 : 3;
    const min = key.startsWith('viewport') ? 10 : .5;
    if (typeof state[key] !== 'number' || !Number.isFinite(state[key]) || state[key] < min || state[key] > max) {
      throw new RangeError(`Spacing ${key} must be between ${min} and ${max}`);
    }
  }
  if (state.viewportMin >= state.viewportMax) throw new RangeError('The maximum viewport must exceed the minimum');
  for (const scale of ['text', 'space', 'layout', 'icon']) {
    if (state[scale + 'Min'] > state[scale + 'Max']) throw new RangeError(`${scale}: maximum size must be at least the minimum`);
  }
  return Object.fromEntries(Object.keys(settings).map(key => [key, state[key]]));
}

export function spacingCss(value) {
  const declarations = state => Object.entries(settings).map(([key, token]) => `  ${token}: ${state[key]};`).join('\n');
  const state = validateSpacing(value);
  return FLUID_CORE_CSS + '\n/* Live fluid settings and scoped comparison profiles */\n' +
    `:root {\n${declarations(state)}\n}\n` +
    `:root, :where([data-ab-profile]) {
  --ab-fluid-icon-slope: calc((var(--ab-fluid-icon-max) - var(--ab-fluid-icon-min)) / (var(--ab-fluid-vp-max) - var(--ab-fluid-vp-min)));
  --ab-fluid-icon: clamp(calc(var(--ab-fluid-icon-min) * 1rem), calc((var(--ab-fluid-icon-min) - var(--ab-fluid-icon-slope) * var(--ab-fluid-vp-min)) * 1rem + var(--ab-fluid-icon-slope) * 100vw), calc(var(--ab-fluid-icon-max) * 1rem));
  --ab-icon-size: var(--ab-fluid-icon);
}
.fluid-card .fluid-icon { display: block; inline-size: var(--ab-icon-size); block-size: var(--ab-icon-size); fill: currentColor; color: var(--accent); flex: none; }
` +
    Object.entries(SPACING_PROFILES).map(([name, profile]) =>
      `[data-ab-profile="${name}"] {\n${declarations(profile)}\n}`).join('\n') + '\n';
}
