/**
 * adapt-ab-theme
 *
 * Programme-wide custom styling. The CSS lives in less/; this module carries no
 * course behaviour — the extension's only job is to ship committed LESS that
 * compiles with every build while adapt-contrib-vanilla stays the base theme.
 *
 * The one exception is the dev/preview theme switcher below: a REMOVABLE overlay
 * for trying the colour packs and light/dark live. It is OFF unless the
 * `cm-theme-switch` flag is set (config _htmlClasses or ?cm-theme-switch), so
 * students never see it. To remove it entirely, delete the import line and
 * ab-theme-switcher.js — the extension goes back to being style-only.
 */
import initThemeSwitcher from './ab-theme-switcher';

initThemeSwitcher();

export default {};
