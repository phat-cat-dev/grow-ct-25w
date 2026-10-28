// emit-css.js — compose the final theme.css (KEEP-DYNAMIC).
//
// Output = the full theme.css system VERBATIM + a trailing, UNLAYERED :root
// block that sets the ingredients. Unlayered declarations beat everything in
// @layer, so these ingredients win; and because they are the hue/saturation
// knobs the whole system derives from, overriding them re-themes every scale,
// accent, semantic and shadow — in light AND dark — with zero flattening.
//
// We only append ingredients that are safe to force globally (see tokens.js).

import { connectorAssets, connectorImports } from '../public/site/connectors.js';
import { colorSystemCss } from '../public/site/color-system.js';
import { typographyCss } from '../public/site/typography-system.js';
import { spacingCss } from '../public/site/spacing-system.js';
import { layoutCss } from '../public/site/layout-system.js';
import { cardsCss } from '../public/site/card-system.js';

export function emitCss(tokens, template, customCss = '', connectors, colorSystem, typography, spacing, layout, cards) {
  if (typeof customCss !== 'string') throw new TypeError('Scheme CSS must be a string');
  const decls = Object.entries(tokens)
    .map(([k, v]) => `  ${k}: ${v};`)
    .join('\n');

  const override = `

/* ==========================================================================
   theme.config — generated ingredient overrides (KEEP-DYNAMIC, do not hand-edit)
   --------------------------------------------------------------------------
   Unlayered so they win over the @layer tokens defaults above. Every derived
   token in theme.css recomputes from these via var(). Change the config and
   rebuild; never edit this block directly.
   ========================================================================== */
:root {
${decls}
}
`;

  const assets = connectors ? connectorAssets(connectors) : null;
  return (assets ? connectorImports(assets.urls) : '') +
    template.replace(/\s*$/, '\n') + override +
    (assets ? '\n/* Google Fonts and Material Symbols */\n' + assets.css + '\n' : '') +
    (colorSystem ? '\n' + colorSystemCss(colorSystem) : '') +
    (typography ? '\n' + typographyCss(typography) : '') +
    (spacing ? '\n' + spacingCss(spacing) : '') +
    (layout ? '\n' + layoutCss(layout) : '') +
    (cards !== undefined ? '\n' + cardsCss(cards) : '') +
    (customCss ? '\n/* Custom scheme CSS */\n' + customCss + '\n' : '');
}
