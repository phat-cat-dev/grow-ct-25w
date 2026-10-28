export const COLOR_SYSTEMS = ['hsl', 'brand', 'harmony', 'semantics'];
export const COLOR_HARMONIES = {
  complementary: [180, 180, 180], analogous: [30, -30, 60], triadic: [120, 240, 120],
  split: [150, 210, 180], tetradic: [60, 180, 240], square: [90, 180, 270], monochrome: [0, 0, 0],
  'accented-analogous': [30, -30, 180], 'double-complementary': [30, 180, 210],
  'mono-tints': [0, 0, 0], 'mono-shades': [0, 0, 0], 'mono-muted': [0, 0, 0],
  'mono-pastel': [0, 0, 0], 'mono-contrast': [0, 0, 0], 'mono-ink-wash': [0, 0, 0],
  'analogous-tight': [15, -15, 30], 'analogous-wide': [60, -60, 120],
  'split-wide': [135, 225, 180], rectangle: [45, 180, 225],
  pentadic: [72, 144, 216, 288], hexadic: [60, 120, 180, 240, 300],
  spectrum: [90, 180, 270],
  'golden-angle': Array.from({ length: 9 }, (_, i) => Math.round(((i + 1) * (180 * (3 - Math.sqrt(5))) % 360) * 1000) / 1000),
};
export function harmonyPalette(state) {
  const anchors = [0, ...COLOR_HARMONIES[state.harmony]];
  const occurrences = new Map();
  return Array.from({ length: state.harmonyCount ?? 4 }, (_, i) => {
    const t = i / ((state.harmonyCount ?? 4) - 1);
    const profiles = {
      'mono-tints': { absoluteLightness: 42 + 48 * t, saturation: 1 },
      'mono-shades': { absoluteLightness: 68 - 58 * t, saturation: 1 },
      'mono-muted': { absoluteLightness: 48, saturation: 1 - .9 * t },
      'mono-pastel': { absoluteLightness: 72 + 18 * t, saturation: .65 - .4 * t },
      'mono-contrast': { absoluteLightness: i % 2 ? 90 - 15 * t : 10 + 20 * t, saturation: 1 },
      'mono-ink-wash': { absoluteLightness: i === 0 ? 20 : 76 + 14 * t, saturation: i === 0 ? 1 : .5 - .35 * t },
    };
    if (Object.hasOwn(profiles, state.harmony)) {
      const profile = profiles[state.harmony];
      return { offset: 0, lightness: 0, ...profile, absoluteLightness: Math.round(profile.absoluteLightness * 10) / 10 };
    }
    const offset = state.harmony === 'spectrum' ? Math.round(i * 360 / (state.harmonyCount ?? 4) * 1000) / 1000 : anchors[i % anchors.length];
    const seen = occurrences.get(offset) || 0;
    occurrences.set(offset, seen + 1);
    return { offset, lightness: [0, 15, -15, 30, -25, 22, -8, 38, -32, 8][seen] };
  });
}
export const SEMANTIC_BANDS = { negative: [-10, 15], positive: [125, 165], neutral: [30, 55], comment: [255, 285], info: [195, 225] };
export const SEMANTIC_HUES = { negative: 0, positive: 145, neutral: 42, comment: 270, info: 210 };
export const SEMANTIC_PRESETS = {
  default: { saturation: 1, light: [0, 0], dark: [0, 0] },
  muted: { saturation: .55, light: [0, 0], dark: [0, 0] },
  vivid: { saturation: 1.3, light: [-4, 0], dark: [4, 0] },
  pastel: { saturation: .65, light: [18, 3], dark: [10, 8] },
  'high-contrast': { saturation: 1.1, light: [-14, 5], dark: [18, -8] },
};
export const SEMANTIC_APPEARANCES = ['default', 'solid', 'soft', 'outline', 'inverted'];
export function semanticSettings(state) {
  const shade = state.main === 'semantics' ? undefined : state.mainShade;
  const source = state.baseColor ?? (shade ? { ...(state.main === 'hsl' ? state.source : state.brand), ...shade } : state.main === 'hsl' ? state.source : state.brand);
  const variation = !state.baseColor && state.main === 'harmony' ? harmonyPalette(state)[state.harmonyHue - 1].lightness : 0;
  const clamp = value => Math.round(Math.max(0, Math.min(100, value)) * 10) / 10;
  const harmonyEntry = !state.baseColor && state.main === 'harmony' && !state.mainShade ? harmonyPalette(state)[state.harmonyHue - 1] : null;
  const base = { s: clamp(source.s * (harmonyEntry?.saturation ?? 1)), weakS: clamp(source.s * (harmonyEntry?.saturation ?? 1)) };
  for (const [mode, strong, weak] of [['light', 42, 92], ['dark', 64, 18]]) {
    base[mode] = { strong: state.baseColor || shade ? source.l : harmonyEntry?.absoluteLightness ?? clamp(paletteLightness(source, strong) + variation), weak: clamp(paletteLightness(source, weak)) };
  }
  const preset = SEMANTIC_PRESETS[state.semanticPreset ?? 'default'];
  base.s = clamp(base.s * preset.saturation);
  base.weakS = clamp(base.weakS * preset.saturation);
  for (const mode of ['light', 'dark']) {
    base[mode].strong = clamp(base[mode].strong + preset[mode][0]);
    base[mode].weak = clamp(base[mode].weak + preset[mode][1]);
  }
  const adjustments = state.semanticAdjustments;
  if (!adjustments) return {
    base, s: clamp(state.semanticS * preset.saturation), weakS: clamp(state.semanticWeakS * preset.saturation),
    light: { strong: clamp(state.light.strong + preset.light[0]), weak: clamp(state.light.weak + preset.light[1]) },
    dark: { strong: clamp(state.dark.strong + preset.dark[0]), weak: clamp(state.dark.weak + preset.dark[1]) },
  };
  return {
    base, s: clamp(base.s + adjustments.s), weakS: clamp(base.weakS + adjustments.weakS),
    light: { strong: clamp(base.light.strong + adjustments.light.strong), weak: clamp(base.light.weak + adjustments.light.weak) },
    dark: { strong: clamp(base.dark.strong + adjustments.dark.strong), weak: clamp(base.dark.weak + adjustments.dark.weak) },
  };
}
export const COLOR_STOPS = [[50, 97], [100, 92], [200, 84], [300, 73], [400, 60], [500, 48], [600, 40], [700, 32], [800, 24], [900, 17], [950, 12]];
export function paletteLightness(palette, light) {
  return Math.round((light + (palette.tone ?? 0) * 4 * light / 100 * (1 - light / 100)) * 10) / 10;
}
function accentForeground(h, s, l) {
  const a = s / 100 * Math.min(l / 100, 1 - l / 100);
  const luminance = [0, 8, 4].reduce((sum, n, i) => {
    const k = (n + h / 30) % 12;
    const c = l / 100 - a * Math.max(-1, Math.min(k - 3, 9 - k, 1));
    const linear = c <= .04045 ? c / 12.92 : ((c + .055) / 1.055) ** 2.4;
    return sum + linear * [.2126, .7152, .0722][i];
  }, 0);
  return (luminance + .05) / .05 >= 1.05 / (luminance + .05) ? '#000' : '#fff';
}
export function remixBrand(source, previous, random = Math.random) {
  const profiles = [[0.45, 0.5, 12], [1.2, 1.3, -10], [0.7, 1.5, -6], [1.1, 0.4, 8], [0.55, 1.1, 5]];
  const candidates = profiles.map(([s, gs, tone]) => ({
    h: source.h, s: Math.max(0, Math.min(100, Math.round(source.s * s))),
    gs: Math.max(0, Math.min(40, Math.round(source.gs * gs))), tone,
  })).filter(p => p.s !== previous.s || p.gs !== previous.gs || p.tone !== (previous.tone ?? 0));
  return candidates[Math.floor(random() * candidates.length)];
}
export function randomizeColorSystem(state, random = Math.random) {
  validateColorSystem(state);
  if (state.baseColor) return state;
  const integer = (min, max) => min + Math.floor(random() * (max - min + 1));
  const source = { h: (mainColor(state).h + integer(1, 359)) % 360, s: integer(20, 90), gs: integer(0, 40) };
  const harmonies = Object.keys(COLOR_HARMONIES);
  const next = {
    ...state, source, brand: { ...source, tone: integer(-12, 12) },
    main: 'brand', harmony: harmonies[integer(0, harmonies.length - 1)],
    harmonyCount: integer(3, 10), harmonyHue: 1,
    semanticAdjustments: { s: 0, weakS: 0, light: { strong: 0, weak: 0 }, dark: { strong: 0, weak: 0 } },
    included: [...new Set([...state.included, 'brand'])],
  };
  delete next.mainShade;
  delete next.locked;
  return validateColorSystem(next);
}
export function defaultColorSystem(cfg = {}) {
  const source = { h: cfg.brandH ?? 202, s: cfg.brandS ?? 72, gs: cfg.greyS ?? 12 };
  return {
    source, brand: { ...source }, harmony: cfg.harmony || 'complementary', harmonyCount: 4,
    main: 'brand', included: ['hsl', 'brand', 'harmony', 'semantics'], harmonyHue: 1, semanticRole: 'info',
    semanticS: cfg.semanticS ?? 55, semanticWeakS: cfg.semanticS ?? 55,
    semanticPreset: 'default', semanticAppearance: 'default',
    semanticAdjustments: { s: 0, weakS: 0, light: { strong: 0, weak: 0 }, dark: { strong: 0, weak: 0 } },
    light: { strong: 38, weak: 92 }, dark: { strong: 64, weak: 18 },
  };
}
export function validateColorSystem(state) {
  const number = (value, min, max) => typeof value === 'number' && Number.isFinite(value) && value >= min && value <= max;
  const adjustments = state?.semanticAdjustments;
  const shade = state?.mainShade;
  if ((state?.semanticPreset !== undefined && !Object.hasOwn(SEMANTIC_PRESETS, state.semanticPreset)) ||
      (state?.semanticAppearance !== undefined && !SEMANTIC_APPEARANCES.includes(state.semanticAppearance))) {
    throw new Error('Invalid semantic preset or appearance modifier.');
  }
  if (state?.baseColor !== undefined && (!state.baseColor ||
      !number(state.baseColor.h, 0, 360) || !number(state.baseColor.s, 0, 100) ||
      !number(state.baseColor.l, 0, 100) || !number(state.baseColor.gs, 0, 40))) {
    throw new Error('Invalid fixed base colour.');
  }
  if (shade !== undefined && (!shade ||
      !(state.main === 'semantics'
        ? Object.hasOwn(SEMANTIC_HUES, shade.family) && ['strong', 'weak'].includes(shade.step)
        : state.main === 'harmony'
        ? shade.family === 'harmony' && Number.isInteger(shade.step) && number(shade.step, 1, state.harmonyCount ?? 4) && shade.step === state.harmonyHue
        : ['hsl', 'brand'].includes(state.main) && ['brand', 'grey', 'gray'].includes(shade.family) && (shade.step === 'custom' || COLOR_STOPS.some(([step]) => step === shade.step))) ||
      !number(shade.h, 0, 360) || !number(shade.s, 0, 100) || !number(shade.l, 0, 100))) {
    throw new Error('Invalid selected main shade.');
  }
  if (adjustments !== undefined && (!adjustments || ![adjustments.s, adjustments.weakS, adjustments.light?.strong, adjustments.light?.weak, adjustments.dark?.strong, adjustments.dark?.weak].every(v => number(v, -100, 100)))) {
    throw new Error('Invalid semantic adjustment offsets.');
  }
  if (!state || ![state.source, state.brand].every(p => p && number(p.h, 0, 360) && number(p.s, 0, 100) && number(p.gs, 0, 40) && number(p.tone ?? 0, -12, 12)) ||
      (state.locked !== undefined && typeof state.locked !== 'boolean') ||
      !Object.hasOwn(COLOR_HARMONIES, state.harmony) || !COLOR_SYSTEMS.includes(state.main) ||
      !Array.isArray(state.included) || !state.included.every(s => COLOR_SYSTEMS.includes(s)) || !state.included.includes(state.main) ||
      !Number.isInteger(state.harmonyCount ?? 4) || !number(state.harmonyCount ?? 4, 3, 10) ||
      !Number.isInteger(state.harmonyHue) || !number(state.harmonyHue, 1, state.harmonyCount ?? 4) || !Object.hasOwn(SEMANTIC_BANDS, state.semanticRole) ||
      !number(state.semanticS, 20, 90) || !number(state.semanticWeakS, 20, 90) ||
      ![state.light, state.dark].every(p => p && number(p.strong, 20, 80) && number(p.weak, 0, 97))) {
    throw new Error('Invalid colour theme settings. Check palettes, selected systems and semantic limits.');
  }
  return state;
}
export function semanticHue(role) {
  return SEMANTIC_HUES[role];
}
export function mainColor(state) {
  validateColorSystem(state);
  if (state.baseColor) return { ...state.baseColor };
  if (state.mainShade) return { ...(state.main === 'hsl' ? state.source : state.brand), h: state.mainShade.h, s: state.mainShade.s, l: state.mainShade.l };
  if (state.main === 'hsl') return state.source;
  if (state.main === 'semantics') return { h: semanticHue(state.semanticRole), s: semanticSettings(state).s, gs: state.brand.gs };
  const entry = state.main === 'harmony' ? harmonyPalette(state)[state.harmonyHue - 1] : null;
  return { ...state.brand, h: (state.brand.h + (entry?.offset ?? 0) + 360) % 360, s: Math.round(state.brand.s * (entry?.saturation ?? 1) * 10) / 10 };
}
export function colorTokens(state) {
  const main = mainColor(state);
  const tokens = { '--brand-h': String(main.h), '--brand-s': main.s + '%', '--grey-s': main.gs + '%' };
  if (state.included.includes('harmony')) harmonyPalette(state).slice(1).forEach(({ offset }, i) => { tokens['--harm-' + (i + 2)] = String(offset); });
  return tokens;
}
export function colorSystemCss(state) {
  validateColorSystem(state);
  const declarations = Object.entries(colorTokens(state)).map(([key, value]) => `  ${key}: ${value};`);
  for (const system of ['hsl', 'brand']) {
    if (!state.included.includes(system)) continue;
    const palette = system === 'hsl' ? state.source : state.brand;
    declarations.push(`  --theme-${system}-h: ${palette.h};`, `  --theme-${system}-s: ${palette.s}%;`, `  --theme-${system}-grey-s: ${palette.gs}%;`);
    COLOR_STOPS.forEach(([step, stopLight]) => {
      const light = paletteLightness(palette, stopLight);
      declarations.push(
      `  --theme-${system}-${step}: hsl(var(--theme-${system}-h) var(--theme-${system}-s) ${light}%);`,
      `  --theme-${system}-grey-${step}: hsl(var(--theme-${system}-h) var(--theme-${system}-grey-s) ${light}%);`,
      `  --theme-${system}-gray-${step}: hsl(0 0% ${light}%);`
      );
    });
  }
  if (!state.baseColor && state.main === 'brand' && state.brand.tone) {
    COLOR_STOPS.forEach(([step, light]) => {
      const value = paletteLightness(state.brand, light);
      declarations.push(`  --blue-${step}: hsl(var(--brand-h) var(--brand-s) ${value}%);`,
        `  --grey-${step}: hsl(var(--brand-h) var(--grey-s) ${value}%);`,
        `  --gray-${step}: hsl(0 0% ${value}%);`);
    });
  }
  if (state.included.includes('harmony')) {
    const foundation = state.baseColor ?? state.brand;
    declarations.push(`  --theme-harmony-h: ${foundation.h};`, `  --theme-harmony-s: ${foundation.s}%;`);
    harmonyPalette(state).forEach(({ offset, lightness, saturation = 1, absoluteLightness }, i) => {
      declarations.push(`  --hue-${i + 1}: calc(var(--theme-harmony-h) + ${offset});`);
      declarations.push(`  --theme-harmony-s-${i + 1}: ${Math.round(foundation.s * saturation * 10) / 10}%;`);
      declarations.push(`  --theme-harmony-l-${i + 1}: ${absoluteLightness !== undefined ? absoluteLightness + '%' : `clamp(10%, calc(var(--acc-l, 40%) + ${lightness}%), 90%)`};`);
      declarations.push(`  --theme-harmony-${i + 1}: hsl(var(--hue-${i + 1}) var(--theme-harmony-s-${i + 1}) var(--theme-harmony-l-${i + 1}));`);
      if (i) declarations.push(`  --accent-${i + 1}: var(--theme-harmony-${i + 1});`);
    });
  }
  let dark = '';
  let semanticStyles = '';
  if (state.included.includes('semantics')) {
    const settings = semanticSettings(state);
    declarations.push(`  --sem-s: ${settings.s}%;`, `  --sem-weak-s: ${settings.weakS}%;`, `  --sem-l: ${settings.light.strong}%;`, `  --sem-weak-l: ${settings.light.weak}%;`);
    Object.entries(SEMANTIC_HUES).forEach(([role, hue]) => {
      declarations.push(`  --${role}-h: ${hue};`);
      declarations.push(`  --${role}: hsl(${hue} var(--sem-s) var(--sem-l));`, `  --${role}-weak: hsl(${hue} var(--sem-weak-s) var(--sem-weak-l));`);
      declarations.push(`  --c-${role}: var(--${role});`, `  --c-${role}-weak: var(--${role}-weak);`);
      declarations.push(`  --${role}-foreground: ${accentForeground(hue, settings.s, settings.light.strong)};`, `  --${role}-weak-foreground: ${accentForeground(hue, settings.weakS, settings.light.weak)};`);
    });
    const values = `--sem-l: ${settings.dark.strong}%; --sem-weak-l: ${settings.dark.weak}%;\n` +
      Object.entries(SEMANTIC_HUES).map(([role, hue]) => `--${role}-foreground: ${accentForeground(hue, settings.s, settings.dark.strong)}; --${role}-weak-foreground: ${accentForeground(hue, settings.weakS, settings.dark.weak)};`).join('\n');
    dark = `\n@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { ${values} } }\n:root[data-theme="dark"] { ${values} }\n`;
    const appearance = state.semanticAppearance ?? 'default';
    Object.keys(SEMANTIC_HUES).forEach(role => {
      const names = role === 'neutral' ? ['neutral', 'warning', 'amber'] : [role];
      const targets = names.flatMap(name => [`.ab.btn.${name}`, `.badge-${name}`]);
      targets.push(`.ab.btn[data-semantic-role="${role}"]`);
      const selector = `:root :is(${targets.join(', ')})`;
      semanticStyles += `
${selector} {
  --semantic-colour: var(--${role});
  --semantic-weak: var(--${role}-weak);
  --semantic-foreground: var(--${role}-foreground);
  --_c: var(--semantic-colour);
  --_fg: var(--semantic-foreground);
}
${selector}:is([data-semantic-strength="weak"], .weak) {
  --semantic-colour: var(--${role}-weak);
  --semantic-foreground: var(--${role}-weak-foreground);
}
`;
      if (appearance === 'default') {
        semanticStyles += `:root :is(${names.map(name => '.badge-' + name).join(', ')}) { background: var(--semantic-weak); color: var(--semantic-colour); }\n`;
        return;
      }
      const element = `:is(${targets.join(', ')}):not(.outline):not(.soft):not(.link)`;
      const target = `:root ${element}`;
      const styles = {
        solid: 'background: var(--semantic-colour); color: var(--semantic-foreground);',
        soft: 'background: color-mix(in srgb, var(--semantic-colour) 16%, var(--surface-1, #fff)); color: var(--semantic-ink);',
        outline: 'background: transparent; color: var(--semantic-ink);',
        inverted: 'background: var(--semantic-foreground); color: var(--semantic-colour);',
      };
      semanticStyles += `
${target} {
  --semantic-ink: hsl(var(--${role}-h) var(--sem-s) ${Math.min(30, settings.light.strong)}%);
  border: 1px solid var(--semantic-colour);
  ${styles[appearance]}
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) ${element} { --semantic-ink: hsl(var(--${role}-h) var(--sem-s) ${Math.max(78, settings.dark.strong)}%); }
}
:root[data-theme="dark"] ${element} { --semantic-ink: hsl(var(--${role}-h) var(--sem-s) ${Math.max(78, settings.dark.strong)}%); }
${target}.btn:is(:hover, :focus-visible) {
  background: ${appearance === 'solid' ? 'transparent' : 'var(--semantic-colour)'};
  color: ${appearance === 'solid' ? 'var(--semantic-ink)' : 'var(--semantic-foreground)'};
}
${target}.btn:focus-visible { outline: 2px solid var(--semantic-ink); outline-offset: 3px; }
@media (forced-colors: active) {
  ${target} { background: Canvas; color: CanvasText; border-color: ButtonText; }
  ${target}.btn:is(:hover, :focus-visible) { background: Highlight; color: HighlightText; }
}
`;
    });
  }
  const schemes = state.included.includes('harmony') ? harmonyPalette(state).map((_, i) => `
.hue-${i + 1} {
  --accent: var(--theme-harmony-${i + 1});
  --accent-hover: hsl(var(--hue-${i + 1}) var(--theme-harmony-s-${i + 1}) var(--acc-hover-l, 32%));
  --accent-weak: hsl(var(--hue-${i + 1}) var(--theme-harmony-s-${i + 1}) var(--acc-weak-l, 92%));
  --ab-btn-primary: var(--accent);
}
.ab.btn.fam-h${i + 1} { --_c: var(--theme-harmony-${i + 1}); --_fg: #fff; }
:root .ab.card.fam-h${i + 1} { --ab-card-accent: var(--theme-harmony-${i + 1}); }
.ab.callout.fam-h${i + 1} { --ab-callout-accent: var(--theme-harmony-${i + 1}); }`).join('\n') : '';
  let roles = '';
  if (!state.baseColor && state.main === 'harmony' && !state.mainShade) {
    const count = state.harmonyCount ?? 4;
    const border = Math.min(4, count);
    roles = `
/* Harmony role mapping: surfaces, headings, actions and borders. */
:root, :root[data-theme], :root:not([data-theme]) {
  --h: var(--theme-harmony-h);
  --accent: var(--theme-harmony-3);
  --line: var(--theme-harmony-${border});
  --border: var(--line);
  --accent-hover: hsl(var(--hue-3) var(--theme-harmony-s-3) var(--acc-hover-l, 32%));
  --accent-weak: hsl(var(--hue-3) var(--theme-harmony-s-3) var(--acc-weak-l, 92%));
}
:root a { color: var(--accent); }
:root .ab.btn:is(.primary,.secondary) { --_c: var(--accent); }
`;
    for (let i = 1; i <= 6; i++) {
      const sibling = i === 1 || count <= 4 ? 2 : 5 + ((i - 2) % (count - 4));
      roles += `:root { --theme-heading-h-${i}: var(--hue-${sibling}); }\n`;
      roles += `:root h${i}:not(.sec):not(.card-title):not(.accordion-header) { color: hsl(var(--theme-heading-h-${i}) var(--theme-harmony-s-${sibling}) var(--acc-l, 42%)); }\n`;
    }
    roles += ':root .harm-demo a { color: var(--accent); }\n';
  }
  if (state.baseColor || state.mainShade) {
    const { h, s, l } = state.baseColor ?? state.mainShade;
    const accent = `hsl(${h} ${s}% ${l}%)`;
    const foreground = accentForeground(h, s, l);
    roles += `
/* Exact selected shade; keep it unchanged in light and dark mode. */
:root, :root[data-theme], :root:not([data-theme]) {
  --accent: ${accent};
  ${!state.baseColor && state.main === 'harmony' ? '' : `--acc-l: ${l}%;`}
  --on-accent: ${foreground};
  --ab-btn-primary: ${accent};
  --accent-hover: hsl(${h} ${s}% ${Math.max(0, l - 8)}%);
  --accent-weak: hsl(${h} ${s}% var(--acc-weak-l, 92%));
}
:root .ab.btn.primary { --_c: var(--accent); --_fg: var(--on-accent); }
`;
  } else if (state.main === 'semantics') {
    const settings = semanticSettings(state);
    const foreground = mode => accentForeground(semanticHue(state.semanticRole), settings.s, settings[mode].strong);
    roles += `
/* Automatic semantic main follows its independent light/dark settings. */
:root, :root[data-theme], :root:not([data-theme]) {
  --accent: var(--${state.semanticRole});
  --acc-l: var(--sem-l);
  --on-accent: ${foreground('light')};
  --ab-btn-primary: var(--accent);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { --on-accent: ${foreground('dark')}; }
}
:root[data-theme="dark"] { --on-accent: ${foreground('dark')}; }
:root .ab.btn.primary { --_c: var(--accent); --_fg: var(--on-accent); }
`;
  }
  return `/* Selected colour systems: ${state.included.join(', ')}. Main: ${state.main}. */\n:root {\n${declarations.join('\n')}\n  --h: var(--brand-h);\n  --s: var(--brand-s);\n  --gs: var(--grey-s);\n}\n${dark}${schemes}\n${roles}\n${semanticStyles}`;
}
