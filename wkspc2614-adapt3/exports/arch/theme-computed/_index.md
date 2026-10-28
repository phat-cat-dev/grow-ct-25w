# Runtime (computed) theme styles

Every `--ab-*` token resolved to its real value by headless Chromium, per
colour theme pack x mode. Unlike `exports/theme-css/` (compiled but still
`var()`/`color-mix()`/`clamp()`), these are the values the browser actually
computes. **Viewport: 1280x800** (length/clamp values are viewport-specific).

Regenerate: `npm run theme-computed` (or `node tools/ab-theme-computed.js`).

| pack | mode | files |
|---|---|---|
| base | light | base-light.css / .json |
| base | dark | base-dark.css / .json |
| dark-blue | light | dark-blue-light.css / .json |
| dark-blue | dark | dark-blue-dark.css / .json |
| dark-grey | light | dark-grey-light.css / .json |
| dark-grey | dark | dark-grey-dark.css / .json |
| dark-blue-grey | light | dark-blue-grey-light.css / .json |
| dark-blue-grey | dark | dark-blue-grey-dark.css / .json |
