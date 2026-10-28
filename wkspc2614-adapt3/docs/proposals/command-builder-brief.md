# Build brief — "Command Deck": a templated web-based command builder

*A ready-to-paste prompt for a fresh thread. Everything it needs is below; it does
not need the conversation this came from.*

---

## PROMPT (paste from here down)

You are building a small, self-contained **web-based command builder** — a local
dev tool that turns a project's everyday CLI commands (npm scripts, grunt tasks,
long-running dev servers, custom node tools) into a point-and-click web panel on
the local network. Think "control deck for a repo's commands". Working name:
**command-deck** (change if you prefer).

### Where this comes from (the seed to generalise)

A working CLI prototype already exists at `_workspace/grunt-menu/viewer.js` in the repo
`workspace26u/wkspc2613-adapt2` (an Adapt e-learning build system). READ IT
FIRST — it is the design seed. It is a dependency-free Node CLI "control panel"
with:

- a **declarative command model**: a `GROUPS` array of panels, each with
  commands `{ alias, name, desc, base | fn, pick?, flags? }`;
- **short patterned aliases** (`<panel><action>`: `bb` build, `cr` rebuild, `ne`
  course-export, …);
- **live discovery** of selectable targets (it scans the filesystem for courses
  and context packs);
- a **guided command-builder**: when a command needs completing, it prompts for
  a *project/target* (from the live list) and lets you *toggle flags* (with
  descriptions, e.g. `--force`), previews the assembled command, then runs it;
- a `help` and an `aliases` view (the latter emits a paste-ready shell-alias
  snippet);
- runs interactively or non-interactively (`node _workspace/grunt-menu/viewer.js <alias> [args]`).

Your job is to **generalise this into a templated npm module with a web UI** that
runs as a local server. The CLI concepts map directly onto the web app.

### Goal

An installable npm package that a user runs in any project:

```
npx command-deck --project . --port 4321
```

…which starts an HTTP server, binds to the local network, and serves a web page
that:

1. **Loads a declarative command dataset** for the project (a `commandset.json`
   or `.yaml` at the project root — see schema below) **plus auto-discovered
   commands**: parse `package.json` `scripts`, and detect grunt tasks
   (`grunt --help` or parsing `Gruntfile.js` / `grunt/tasks/*`).
2. **Groups commands into panels** and shows each with its name, description and
   a short alias (mirroring `viewer.js`).
3. **Reads project-specific variables / targets** (e.g. "which course", "which
   context pack") by running a declared discovery command or glob, and offers
   them as a pick list when a command needs one.
4. **Surfaces available flags**, highlighting the common ones, as toggles; plus
   a free-text field for anything else.
5. **Previews the assembled command** before running.
6. **Runs the command on the server host and streams stdout/stderr live** to the
   page (WebSocket or SSE). Long-running commands (watch, dev server) show a live
   log with a **Stop** control.
7. Is **templated/reusable** — no project specifics baked into the app; a project
   describes itself entirely through its `commandset` + auto-discovery, so the
   same tool serves any repo.

### `commandset` schema (starting point — refine as needed)

```jsonc
{
  "name": "My project",
  "discovery": {
    // named target lists the UI can offer for a command's "pick"
    "course":  { "glob": "courses/*", "exclude": ["_generated"] },
    "context": { "glob": "content/context-packs/*" }
  },
  "groups": [
    {
      "title": "Build & preview",
      "commands": [
        { "alias": "bb", "name": "Build", "desc": "production build",
          "exec": "npx grunt build",
          "flags": [{ "flag": "--force", "desc": "build past check-json", "common": true }] },
        { "alias": "cr", "name": "Rebuild", "desc": "merge a context then build",
          "exec": "node merge-context.js --context={context} --tier={course} && npx grunt build",
          "pick": ["context", "course"],
          "flags": [{ "flag": "--force", "desc": "", "common": true }],
          "longRunning": false }
      ]
    }
  ]
}
```

- `{context}` / `{course}` are substituted from the user's picks (from
  `discovery`).
- Auto-discovered npm scripts and grunt tasks are merged in as an extra panel so
  nothing has to be hand-listed; the `commandset` is for curated/alias'd/templated
  commands and discovery rules.

### Stretch goals ("perfect world")

- **Terminal view/editor in the browser** — an actual terminal in the page via
  **xterm.js + node-pty**, so the user gets a real interactive shell alongside the
  builder (this is the closest practical answer to "inject into my workspace
  terminal": a browser page cannot write into a separate OS terminal, but it *can*
  host its own full terminal). Note `node-pty` is a native dependency (needs a
  build toolchain) — keep it an **optional mode** so the core stays light.
- **"Copy command" button** as the simplest injection path (assemble the command,
  copy to clipboard, paste into whatever terminal).
- **Favourites / recent**, and persisting the user's common flag choices per
  command (localStorage).

### Architecture suggestions (your call)

- Node server: built-in `http` or a light framework; **WebSocket** (`ws`) or SSE
  for live output; `child_process.spawn` for exec (or `node-pty` for the terminal
  mode). Keep the dependency footprint small; make the terminal an opt-in extra.
- Front-end: vanilla + a tiny bit of structure is fine (match `viewer.js`'s
  restraint); a framework only if it clearly earns its place.
- Package layout: a `bin` CLI entry, a `server/`, a `web/` (static assets), a
  `commandset` loader + JSON-schema validation, and a sample `commandset.json`.

### Hard constraints / cautions

- **It executes arbitrary commands on the host over the LAN.** Default-bind to
  `127.0.0.1`; require an explicit `--host 0.0.0.0` (or `--lan`) to expose on the
  network, and when exposed, gate with a token/PIN and print a clear warning. This
  is a trusted-dev-network tool, never for untrusted networks.
- Must run on macOS and Windows (spawn with `shell: true`; handle path quirks).
- Cross-platform process stop (kill the child/tree) for long-running commands.

### Deliverables

1. The npm package (CLI + server + web UI + commandset loader/validator + sample).
2. A real `commandset.json` for `workspace26u/wkspc2613-adapt2` ported from
   `_workspace/grunt-menu/viewer.js`'s `GROUPS` (build/preview, course workflow, npm scripts),
   as the first proving dataset.
3. README: install, run, write a `commandset`, security notes.
4. Optional: the xterm/node-pty terminal mode behind a flag.

### First, put these decisions to the user before building

- Standalone repo, or live in the `wkspc2600-uni` "viewer tooling"?
- Front-end: vanilla vs a framework?
- Terminal mode (xterm + node-pty native dep) in v1, or copy-command only?
- Auth model when LAN-exposed (token? PIN? none for localhost-only)?
- Package name.

Start by reading `_workspace/grunt-menu/viewer.js`, then propose the package skeleton + the
`commandset` schema for sign-off before writing the server.

## (end of prompt)
