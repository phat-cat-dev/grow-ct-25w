export const DEFAULT_CARDS = { family: 'brand', fill: 'tinted', padding: 16, border: 1, tint: 12, elevation: 'soft', iconSize: 28, gap: 16 };
export function validateCards(value = DEFAULT_CARDS) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error('Invalid card settings. Expected an object.');
  const state = { ...DEFAULT_CARDS, ...value };
  const within = (key, min, max) => typeof state[key] === 'number' && Number.isFinite(state[key]) && state[key] >= min && state[key] <= max;
  if (!['brand', 'grey', 'gray'].includes(state.family) || !['tinted', 'soft', 'invert'].includes(state.fill) ||
      !['flat', 'soft', 'raised'].includes(state.elevation) || !within('padding', 8, 40) ||
      !within('border', 0, 6) || !within('tint', 0, 30) || !within('iconSize', 16, 56) || !within('gap', 8, 32)) {
    throw new Error('Invalid card settings. Check family, fill, depth and sizing limits.');
  }
  return state;
}
export function cardsCss(value) {
  const state = validateCards(value);
  const family = {
    brand: 'var(--accent)',
    grey: 'hsl(var(--brand-h) var(--grey-s) var(--acc-l))',
    gray: 'hsl(var(--brand-h) 0% var(--acc-l))',
  }[state.family];
  // XYZ Y is relative luminance; this is the black/white WCAG contrast crossover.
  const white = 'clamp(0, calc((0.1791287847 - y) * 1000000), 1)';
  const inverted = `--card-ink: #fff; --card-ink: color(from var(--ab-card-accent) xyz-d65 calc(.9504559271 * ${white}) ${white} calc(1.0890577508 * ${white})); --card-muted: var(--card-ink); --card-decoration: var(--card-ink);`;
  return `/* Theme-linked cards: one accent, shared geometry and semantic meaning. */
:root { --ab-card-spacer-x: ${state.padding}px; --ab-card-spacer-y: ${state.padding}px; --ab-card-border-width: ${state.border}px; --ab-card-group-gap: ${state.gap}px; --ab-card-tint: ${state.tint}%; --ab-card-icon-size: ${state.iconSize}px; --ab-card-shadow: ${state.elevation === 'flat' ? 'none' : state.elevation === 'raised' ? 'var(--shadow-3, 0 8px 24px var(--shadow))' : 'var(--shadow-1, 0 2px 6px var(--shadow))'}; }
:root .ab.card {
  --ab-card-accent: ${family};
  --card-fill: ${state.fill === 'invert' ? 'var(--ab-card-accent)' : state.fill === 'soft' ? 'color-mix(in srgb, var(--ab-card-accent) var(--ab-card-tint), var(--surface-1))' : 'var(--surface-1)'};
  --card-ink: var(--text, var(--ink)); --card-muted: var(--text-soft, var(--ink-soft)); --card-decoration: var(--ab-card-accent);
  ${state.fill === 'invert' ? inverted : ''}
  background: var(--card-fill); color: var(--card-ink);
  border: var(--ab-card-border-width) solid var(--ab-card-accent);
  border-radius: var(--radius); box-shadow: var(--ab-card-shadow);
}
:root .ab.card.primary { --ab-card-accent: var(--accent); }
:root .ab.card.secondary { --ab-card-accent: hsl(var(--brand-h) var(--grey-s) var(--acc-l)); }
${['positive', 'negative', 'comment', 'info'].map(role => `:root .ab.card.${role} { --ab-card-accent: var(--${role}); }`).join('\n')}
:root .ab.card:is(.warning, .amber, .neutral) { --ab-card-accent: var(--neutral); }
:root .ab.card.success, :root .ab.card:is(.advice, .do, .feedback-pos) { --ab-card-accent: var(--positive); }
:root .ab.card.danger, :root .ab.card:is(.dont, .feedback-neg) { --ab-card-accent: var(--negative); }
:root .ab.card.action { --ab-card-accent: var(--info); }
:root .ab.card.starting { --ab-card-accent: var(--comment); }
:root .ab.card.fam-brand { --ab-card-accent: var(--accent); }
:root .ab.card.fam-grey { --ab-card-accent: hsl(var(--brand-h) var(--grey-s) var(--acc-l)); }
:root .ab.card.fam-gray { --ab-card-accent: hsl(var(--brand-h) 0% var(--acc-l)); }
${[[50, 97], [100, 92], [200, 84], [300, 73], [400, 60], [500, 48], [600, 40], [700, 32], [800, 24], [900, 17], [950, 12]].map(([step, light]) => `:root .ab.card.sh-${step} { --ab-card-accent: hsl(var(--brand-h) var(--_cs, var(--brand-s)) ${light}%); }`).join('\n')}
:root .ab.card.tinted { --card-fill: var(--surface-1); }
:root .ab.card.soft { --card-fill: color-mix(in srgb, var(--ab-card-accent) var(--ab-card-tint), var(--surface-1)); }
:root .ab.card.elevated { --card-fill: var(--surface-2); }
:root .ab.card.invert { --card-fill: var(--ab-card-accent); }
:root .ab.card.invert { ${inverted} }
:root .ab.card:is(.tinted, .soft) { --card-ink: var(--text, var(--ink)); --card-muted: var(--text-soft, var(--ink-soft)); --card-decoration: var(--ab-card-accent); }
:root .ab.card .card-body { padding: var(--ab-card-spacer-y) var(--ab-card-spacer-x); color: var(--card-ink); }
:root .ab.card .card-title { color: var(--card-ink); font-size: 1.1rem; }
:root .ab.card :is(.card-text, .card-subtitle) { color: var(--card-muted); }
:root .ab.card :is(.card-header, .card-footer) {
  padding: calc(var(--ab-card-spacer-y) * .7) var(--ab-card-spacer-x);
  background: color-mix(in srgb, var(--ab-card-accent) var(--ab-card-tint), var(--card-fill));
  color: var(--card-ink); border-color: var(--ab-card-accent); border-width: var(--ab-card-border-width);
}
:root .ab.card .card-header { border-radius: max(0px, calc(var(--radius) - var(--ab-card-border-width))) max(0px, calc(var(--radius) - var(--ab-card-border-width))) 0 0; }
:root .ab.card .card-footer { border-radius: 0 0 max(0px, calc(var(--radius) - var(--ab-card-border-width))) max(0px, calc(var(--radius) - var(--ab-card-border-width))); }
:root .ab.card .card-link { color: var(--card-decoration); text-decoration: underline; }
:root .ab.card.with-icon .card-title { display: flex; align-items: center; gap: .65rem; }
:root .ab.card .card-icon { flex: none; color: var(--card-decoration); font-size: var(--ab-card-icon-size); }
:root .ab.card .card-icon svg { display: block; width: var(--ab-card-icon-size); height: var(--ab-card-icon-size); fill: currentColor; }
:root .ab.card.flat { box-shadow: none; }
:root .ab.card.raised { box-shadow: var(--shadow-3, 0 8px 24px var(--shadow)); }
:root .ab.card.square { border-radius: 0; }
:root .ab.card.hover-animate { cursor: auto; transition: box-shadow .2s ease; }
:root .ab.card.hover-animate:is(:hover, :focus-within) { transform: none; box-shadow: 0 0 0 2px var(--ab-card-accent), var(--ab-card-shadow); }
:root .ab.card-set { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr)); gap: var(--ab-card-group-gap); align-items: stretch; }
:root .ab.card-stack { display: grid; gap: var(--ab-card-group-gap); }
:root .ab.card .ab.card { margin-top: var(--ab-card-group-gap); }
:root .ab.card-group { display: flex; flex-direction: column; gap: var(--ab-card-group-gap); }
@media (min-width: 576px) {
  :root .ab.card-group { flex-direction: row; gap: 0; }
  :root .ab.card-group > .ab.card { flex: 1 1 0; }
  :root .ab.card-group > .ab.card:not(:last-child) { border-top-right-radius: 0; border-bottom-right-radius: 0; }
  :root .ab.card-group > .ab.card:not(:first-child) { border-top-left-radius: 0; border-bottom-left-radius: 0; border-left-width: 0; }
}
@media (prefers-reduced-motion: reduce) { :root .ab.card.hover-animate { transition: none; } }
@media (forced-colors: active) {
  :root .ab.card { --card-fill: Canvas !important; --card-ink: CanvasText !important; --card-muted: CanvasText !important; --card-decoration: CanvasText !important; --ab-card-accent: CanvasText !important; background: Canvas; color: CanvasText; border: 2px solid CanvasText; box-shadow: none; }
  :root .ab.card .card-link { color: LinkText; }
}
`;
}
