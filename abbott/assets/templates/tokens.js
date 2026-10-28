// tokens.js — turn a theme config into the small set of INGREDIENT overrides.
//
// KEEP-DYNAMIC MODE: we never flatten colours to hex. A theme is defined by a
// handful of root custom properties; every scale / accent / semantic token in
// theme.css re-derives from them in the browser via var(). So all we emit is
// the ingredients — the rest of the system does the work.
//
// Only SAFE-to-override-globally props are emitted here: the ones that are the
// same in light AND dark (hue, saturations, harmony angles). The theme-flipped
// lightness tokens (--sem-l, --acc-l, surfaces) are left to theme.css so dark
// mode keeps working. Anything you really want to pin can go in `overrides`.

import { HARMONY } from './harmony.js';
import { colorTokens } from '../public/site/color-system.js';

const pct = (v) => (typeof v === 'number' ? v + '%' : String(v));

export function buildTokens(cfg = {}) {
  if (cfg.colorSystem) {
    const tokens = {};
    for (const [key, value] of Object.entries(cfg.overrides ?? {})) {
      tokens[key.startsWith('--') ? key : '--' + key] = value;
    }
    return Object.assign(tokens, colorTokens(cfg.colorSystem));
  }
  const h  = cfg.brandH ?? 202;
  const s  = cfg.brandS ?? 72;
  const gs = cfg.greyS ?? 12;
  const [h2, h3, h4] = HARMONY[cfg.harmony] ?? HARMONY.complementary;

  const t = {
    '--brand-h': String(h),
    '--brand-s': pct(s),
    '--grey-s':  pct(gs),
    // colour-harmony angle offsets (sibling hues fall out by calc in theme.css)
    '--harm-2': String(h2),
    '--harm-3': String(h3),
    '--harm-4': String(h4),
  };

  // Semantic SATURATION is not theme-flipped, so it is safe to override.
  // (Semantic LIGHTNESS flips in dark — tune it in theme.css, not here.)
  if (cfg.semanticS != null) {
    t['--sem-s'] = pct(cfg.semanticS);
    t['--sem-weak-s'] = pct(cfg.semanticS);
  }

  // Free-form pinned overrides — your responsibility re: dark mode.
  for (const [k, v] of Object.entries(cfg.overrides ?? {})) {
    t[k.startsWith('--') ? k : '--' + k] = v;
  }

  return t;
}
