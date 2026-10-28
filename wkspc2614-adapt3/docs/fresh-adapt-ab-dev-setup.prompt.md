# Prompt — stand up a fresh Adapt component/extension dev sandbox

Paste the block below to a Claude Code agent running on the machine that has
`/home/abbottdev/workspace-26u/`. It builds a clean vanilla Adapt install with a
dev server, an `--ab-base` token foundation, and a sandbox test page — ready for
developing `adapt-ab-*` components/extensions and for importing the components
branch later.

The token defaults in Step 3 are chosen to match exactly the `--ab-*` tokens the
existing `adapt-ab-card` / `-accordion` / `-carousel` consume, so those render
with no theme present.

---

```
You are setting up a fresh Adapt Framework development sandbox for building and
testing custom components and extensions, with a token-based styling foundation.

TARGET FOLDER (create if missing, work entirely inside it):
  /home/abbottdev/workspace-26u/wkpsc2611-adapt-ab

GOALS
  A. A plain vanilla Adapt install that builds and serves via a dev server, so I
     can develop/test components and extensions by placing instances on a test page.
  B. An `--ab-base` CSS-custom-property foundation wired in, so component LESS can
     consume `--ab-base-*` / `--ab-*` tokens that are populated by base defaults
     and optionally overridden by a theme layer.

Work in small steps, run each command, and SHOW the real output + exit code of the
key ones (append `; echo "EXIT: $?"`). Do not claim success you have not seen.

=== STEP 0 — environment check ===
- Confirm node >= 18 and git: `node -v; git --version`.
- Install the Adapt CLI if absent: `npm install -g adapt-cli` then `adapt --version`.

=== STEP 1 — scaffold a vanilla Adapt framework ===
- Create and enter the target folder.
- Scaffold the framework + default course. Prefer the CLI:
    adapt create course .        (or `adapt create course wkpsc2611-adapt-ab` one level up)
  If the CLI misbehaves, fall back to:
    git clone https://github.com/adaptlearning/adapt_framework.git .
    npm install
    npx adapt install            (installs the default contrib plugins)
- Result must include: src/course/ (the default vanilla course), src/components/,
  src/extensions/, src/theme/adapt-contrib-vanilla, Gruntfile.js, grunt/.

=== STEP 2 — prove the build + dev server ===
- `npx grunt build` and confirm build/index.html exists.
- Start the dev server (whichever the framework exposes): `npx grunt server`
  (and note the localhost URL/port). Confirm the default course loads.
- Also confirm the watch/dev task: `npx grunt dev` (build + watch) rebuilds on edit.
- Report: adapt_framework version (package.json), adapt-contrib-core version, the
  server URL, and the build exit code.

=== STEP 3 — the --ab-base token foundation (a style-only extension) ===
Create a style-only extension that ships default token values globally. This is the
BASE layer; components consume these with fallbacks so they render unthemed.

Create src/extensions/adapt-ab-base/ with:

  bower.json:
    {
      "name": "adapt-ab-base",
      "version": "1.0.0",
      "framework": ">=5.19.1",
      "extension": "abBase",
      "targetAttribute": "_abBase",
      "displayName": "AB Base Tokens",
      "main": "/js/adapt-ab-base.js",
      "keywords": ["adapt-plugin", "adapt-extension"],
      "license": "GPL-3.0",
      "private": true
    }

  js/adapt-ab-base.js:
    // style-only: ships the base token LESS; no runtime behaviour
    export default {};

  less/ab-base.less  —  define :root defaults for the token spine. Include AT LEAST
  these (components already reference them), with sensible neutral defaults:

    :root {
      /* ink + surfaces */
      --ab-base-ink: #1a1a1a;
      --ab-base-ink-muted: #6d6d6d;
      --ab-base-surface: #ffffff;
      --ab-base-surface-sunken: #f3f3f3;
      --ab-base-hairline: rgba(0,0,0,0.125);
      --ab-base-border-width: 0.1rem;

      /* accent (overridable by a theme) */
      --ab-accent: #2a5db0;
      --ab-accent-rgb: 42,93,176;
      --ab-on-accent: #ffffff;

      /* shape */
      --ab-border-radius: 0.375rem;

      /* spacing scale */
      --ab-space-050: 0.5rem;
      --ab-space-075: 0.75rem;
      --ab-space-100: 1rem;
      --ab-space-125: 1.25rem;
      --ab-space-200: 2rem;
    }

Rules to document in a short README in that folder:
  - Component LESS must CONSUME tokens (`var(--ab-base-surface, #fff)`), never
    hardcode a palette.
  - A theme layer overrides by REDEFINING these same custom properties (globally,
    or under a scope class) — it does not touch component files.

=== STEP 4 — a demo theme-override layer (prove the cascade) ===
Create a tiny second style-only extension src/extensions/adapt-ab-theme-demo/ (same
bower shape, extension name "abThemeDemo") whose less/ab-theme-demo.less REDEFINES a
few base tokens under a scope class so the override is switchable:

    .ab-theme-demo {
      --ab-accent: #6b0f1a;
      --ab-accent-rgb: 107,15,26;
      --ab-base-surface-sunken: #f6eeea;
    }

Enable the scope by adding the class via the course config. In src/course/config.json
add (or extend) "_htmlClasses": "ab-theme-demo". Toggling that string on/off must
visibly reskin anything consuming the tokens — this is the base-vs-theme seam.

=== STEP 5 — a sandbox component to prove the component pipeline ===
Create ONE minimal custom component src/components/adapt-ab-sandbox/ (register name
"ab-sandbox") that renders a box using ONLY base tokens, e.g.:

  .ab-sandbox__box { background: var(--ab-base-surface-sunken); color: var(--ab-base-ink);
    border: var(--ab-base-border-width) solid var(--ab-base-hairline);
    border-radius: var(--ab-border-radius); padding: var(--ab-space-100); }

Use the standard component shape (bower.json with "component":"ab-sandbox" +
"targetAttribute":"_abSandbox", properties.schema, js/adapt-ab-sandbox.js registering
view+model, js Model extends ComponentModel, View extends ComponentView with
setupInviewCompletion, templates/sandbox.jsx via core/js/reactHelpers rendering
<templates.header/> + the box). Mirror an existing contrib component's file layout.

=== STEP 6 — wire a TEST PAGE ===
In src/course/en/ add, to the default course, one article + block + a component with
"_component": "ab-sandbox" (give it a unique _id and correct _parentId), so the
sandbox renders on a page. Keep the default vanilla theme as the base theme.

=== STEP 7 — build, serve, verify (SHOW output) ===
- `npx grunt build; echo "EXIT: $?"` — must pass.
- Serve and load the course; confirm the ab-sandbox box renders.
- Toggle "_htmlClasses": "ab-theme-demo" in config.json, rebuild, and confirm the
  box's accent/surface changes — proving base defaults + theme override both work.
- If git is initialised here, add a .gitignore rule so custom plugins are tracked:
    !src/components/adapt-ab-*/
    !src/extensions/adapt-ab-*/
  (placed after the framework's `src/components/*` / `src/extensions/*` ignores).

DELIVERABLES / REPORT BACK
  - The dev server URL and how to start it (the exact grunt task).
  - Framework + core versions.
  - Confirmation screenshots or console output of: default course building, the
    ab-sandbox rendering, and the theme-demo override visibly changing it.
  - The final folder tree of src/components, src/extensions, and src/course/en.

DO NOT
  - Do not add a brand theme or any Cardiff-Met styling — keep base neutral.
  - Do not hardcode colours in component LESS — tokens only.
  - Do not import the existing adapt-ab components yet; this is the bare sandbox.
```

---

## After the sandbox exists — importing this branch's components

When the sandbox builds and the token cascade is proven, bring the components across
from the `wkspc2613-adapt2` repo, branch `claude/peaceful-sagan-d7e4ue`:

1. From inside the new install, add the source repo as a remote and fetch:
   `git remote add compsrc <url-of-wkspc2613-adapt2>` ; `git fetch compsrc claude/peaceful-sagan-d7e4ue`
2. Check out only the component dirs:
   `git checkout compsrc/claude/peaceful-sagan-d7e4ue -- src/components/adapt-ab-card src/components/adapt-ab-accordion src/components/adapt-ab-carousel`
3. The `--ab-base` foundation from Step 3 already supplies every token those
   components reference, so they render with no theme. For the card, also copy the
   `.cm.card` system (`ab-cards.less`) from the theme if you want the full card
   visuals; otherwise add a minimal `.cm.card` to ab-base.
4. Add one instance of each to the test page and rebuild.

(Only the component files move; the real `--ab-*` theme stays on its own branch and
is layered in later as an override, exactly as the base-vs-theme seam intends.)
