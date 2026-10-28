// emit-json.js — a portable record of the theme (KEEP-DYNAMIC).
//
// Since nothing is flattened, this JSON captures the INGREDIENTS and the
// config that produced them, plus a note on where the derived tokens live.
// It is handy for diffing themes, feeding a docs page, or re-importing.

export function emitJson(tokens, cfg = {}) {
  return (
    JSON.stringify(
      {
        $meta: {
          name: cfg.name ?? 'untitled',
          generator: 'ab-theme-studio',
          mode: 'keep-dynamic',
          generatedAt: new Date().toISOString(),
        },
        config: cfg,
        ingredients: tokens,
        note:
          'Derived tokens (scales, accents, semantics, shadows, harmony siblings) ' +
          'are defined in theme.css and compute from these ingredients via var(). ' +
          'Nothing is flattened to hex in keep-dynamic mode.',
      },
      null,
      2
    ) + '\n'
  );
}
