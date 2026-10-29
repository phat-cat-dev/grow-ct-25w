# VM setup — grow-course workspace

This repo (`grow-ct-25w`) is a **flat snapshot** of the whole `grow-course` workspace,
taken for transfer to a VM. Everything you need to build and continue the work is here,
but a few things are deliberately left out of git and must be recreated on first clone
(they're all one command each). The original nested sub-repo histories travel separately
as **git bundles** under [`_histories/`](_histories/) — see *Restoring full history* below.

The Adapt engine lives in [`wkspc2614-adapt3/`](wkspc2614-adapt3/); most commands run from
there.

---

## 1. Quick start (Linux VM)

```bash
git clone https://github.com/phat-cat-dev/grow-ct-25w.git
cd grow-ct-25w/wkspc2614-adapt3

# a) node_modules is gitignored — reinstall
npm ci                      # or: npm install

# b) src/extensions and src/components are gitignored EXCEPT the custom
#    adapt-ab-*/adapt-abbott-*/adapt-grow-* plugins — the 23 stock
#    adapt-contrib-* plugins (incl. adapt-contrib-spoor, which generates
#    imsmanifest.xml at build time) never travel. Without this step, grunt
#    build succeeds but produces a web-only bundle with NO imsmanifest.xml —
#    the zip will upload to an LMS but fail as "missing imsmanifest.xml".
#    Never run raw `adapt install`: it wipes the local patches in src/ — use
#    this npm script, which reinstalls them then reapplies patches/.
npm run adapt-install

# c) the src/course symlink doesn't travel (Adapt ignores it) — recreate it,
#    pointing at a COMMITTED course (not a _generated one; see §2)
#    NB: the target is relative to src/, not the repo root — needs ../
ln -s ../courses/ai-technology-introductory src/course

# d) build
npx grunt build

# e) serve build/ over HTTP (it AJAX-loads JSON, so file:// will NOT work)
cd build && python3 -m http.server 8080
# → open http://localhost:8080
```

Node **≥ 18** is required (see `package.json` → engines). On Node 18 only, if the build
errors on `crypto`, run `export NODE_OPTIONS=--experimental-global-webcrypto` first.

---

## 2. What doesn't travel in the snapshot (by design)

| Missing on clone | Why | How to restore |
|---|---|---|
| `wkspc2614-adapt3/node_modules/` | gitignored | `npm ci` |
| `wkspc2614-adapt3/src/extensions/adapt-contrib-*`, `src/components/adapt-contrib-*` (incl. `adapt-contrib-spoor`) | gitignored — only the custom `adapt-ab-*`/`adapt-abbott-*`/`adapt-grow-*` plugins are whitelisted in `.gitignore` | `npm run adapt-install` (never raw `adapt install` — it wipes the local patches in `src/`) |
| `wkspc2614-adapt3/src/course` symlink | Adapt ignores it; old target was a Windows absolute path | `ln -s ../courses/<slug> src/course` |
| `wkspc2614-adapt3/build/` | gitignored build output | `npx grunt build` |
| `wkspc2614-adapt3/courses/_generated/` | gitignored; regenerated per context/tier | run `merge-context.js --context <ctx> --tier <tier>` |

**About `adapt-contrib-spoor`:** this is the plugin that writes `imsmanifest.xml`
into `build/` from each course's `config.json` `_spoor` block. If it's missing,
`grunt build` still succeeds and produces a web-only bundle with no error — the
zip looks fine until an LMS rejects it for lacking `imsmanifest.xml`/AICC
structure. Always run `npm run adapt-install` before the first `grunt build` on
a fresh clone.

**About `src/course`:** on the source machine it pointed at a `_generated/` course, but
`_generated/` is gitignored and won't exist until you regenerate it. Easiest path is to
symlink one of the committed authored courses:

- `courses/ai-technology-introductory` (or any `<pathway>-<tier>` under `courses/`)
- `courses/_component-gallery` (the all-components test bed)

To build a **merged / contextualised** variant, run the merge step first, then point the
symlink at the resulting `courses/_generated/<slug>-<ctx>/` dir, then `grunt build`.

---

## 3. Restoring full git history (optional)

The snapshot's own history is a single commit. The real per-repo development histories are
preserved as bundles in [`_histories/`](_histories/):

| Bundle | Contents | Tip |
|---|---|---|
| `wkspc2614-adapt3-history.bundle` | the engine — **96 commits, all 7 branches** (`vm-transfer-prep`, `gate-system-review`, `adab-styles-mapper`, `adopt-grow-theme`, two `backup/*`, the fork worktree) | `vm-transfer-prep` |
| `grow-ct-history.bundle` | the theme repo — `main` + tag `v1.0.1` | `main` |

**To inspect a history** (clone the bundle into a scratch dir):

```bash
git clone _histories/wkspc2614-adapt3-history.bundle /tmp/engine-history
cd /tmp/engine-history
git log --oneline --all
```

**To revive it as a real repo with a new remote** (e.g. push the engine history to a fresh
GitHub repo so it lives as normal git again):

```bash
git clone _histories/wkspc2614-adapt3-history.bundle engine-history
cd engine-history
git checkout vm-transfer-prep
git remote set-url origin <your-new-github-url>
git push --all && git push --tags
```

> The bundles are a one-time transfer artifact. Once you've restored what you need on the
> VM, you can delete `_histories/` from your working copy (and, if you want to slim the
> remote, remove it in a follow-up commit).

### `src/core` history (not bundled)

`wkspc2614-adapt3/src/core` is the public **Adapt framework core**
(`adaptlearning/adapt-contrib-core`, 2073 commits). Its files are in the snapshot, but its
history is just upstream — re-fetch it only if you need it:

```bash
cd /tmp
git clone https://github.com/adaptlearning/adapt-contrib-core
```

---

## 4. Linux vs the old Windows machine

Things that were Windows-only headaches and simply **don't apply** on a Linux VM:

- **No `python3` shim needed** — the VM has a real `python3`, so the PATH workaround is gone.
- **`.sh` scripts just run** — `.gitattributes` checks them out with LF line endings.
- **No MAX_PATH / `core.longpaths` issue** — that was a Windows filename-length limit.

---

## 5. Caveat

This is a flat snapshot (one commit, `ebcf1ef`). The nested sub-repos' `.git` dirs were
backed up on the source machine as `.git_wks_bak` and are **not** in this repo — their
histories live only in the bundles above. Restore from a bundle if you need per-repo
history on the VM.
