#!/usr/bin/env bash
# workspace-build-sync.sh — pick a build-test dir + branch(es), sync it to
# match origin, then optionally build or preview it.
#
# Role: Build & Preview Manager / read-only consumer of content.
# This script NEVER commits, NEVER pushes to a real branch. It only fetches,
# hard-resets a build-test checkout to match a branch on origin (optionally
# merging in further branches on top, for testing several together), then
# (optionally) runs a build target.
#
# Scans workspace-26u-build for dirs matching the
# wkspc26<xx>-<project-name>-build naming formula and offers it as a pick.
# If the chosen one isn't a git checkout yet (e.g. a placeholder dir, or one
# freshly created by workspace-build-create.sh without cloning), it's cloned
# in place first, using the matching source project's 'origin' remote under
# workspace-26u.
#
# Usage — any argument you omit is prompted for interactively, so you can run
# it bare and build the command step by step, or pass some/all of it directly.
# Passing <branch> explicitly keeps the old single-branch behavior (for
# scripting); omitting it drops you into the interactive base-branch +
# optional-merge-more-branches picker instead:
#   workspace-build-sync.sh                                  fully interactive
#   workspace-build-sync.sh <project>                        pick branch/target
#   workspace-build-sync.sh <project> <branch>                pick target
#   workspace-build-sync.sh <project> <branch> sync
#   workspace-build-sync.sh <project> <branch> build [context]
#   workspace-build-sync.sh <project> <branch> preview <context>
#
# NOTE on `build` vs `preview`: a fresh sync hard-resets then `git clean -fdx`s,
# which wipes courses/_generated/ (gitignored, rebuilt) and so leaves the tracked
# src/course symlink dangling. grunt's own check-build-target task then refuses.
# `preview <context>` runs `viewer.js cr` (merge context -> link -> grunt build),
# which regenerates + relinks first. `build` now does the same setup on demand:
# if nothing is linked it generates+links the chosen context (viewer.js cg) before
# `grunt build`, so `build` is self-sufficient on a freshly-synced checkout too.
#
# Lives OUTSIDE any content repo on purpose (this is build tooling, not
# content; it must never appear as an untracked file inside a content/claude
# branch's working tree).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib-build-common.sh
source "$SCRIPT_DIR/lib-build-common.sh"
WORKSPACE_ROOT="$BUILD_ROOT"

# --- helpers: numbered picks, bash `select` already re-prompts on a bad
#     choice without re-printing the whole list, so no extra validation
#     loop is needed here. ---

discover_packs() {
  local d
  for d in "$REPO_DIR"/content/context-packs/*/; do
    [ -d "$d" ] && basename "$d"
  done
}

# The viewer/menu moved from tools/ to _workspace/grunt-menu/ in some projects
# and not others, and this script runs against whichever checkout you picked.
# Resolve it per project rather than hardcoding either location.
viewer_path() {
  local p
  for p in "_workspace/grunt-menu/viewer.js" "tools/viewer.js"; do
    [ -f "$REPO_DIR/$p" ] && { echo "$p"; return 0; }
  done
  echo "No viewer.js found in $PROJECT (looked in _workspace/grunt-menu/ and tools/)" >&2
  return 1
}

# Sets the global CONTEXT: leaves a non-empty CONTEXT untouched, otherwise
# prompts from the discovered context packs. Shared by `build` and `preview`.
pick_context() {
  if [ -n "${CONTEXT:-}" ]; then
    return
  fi
  mapfile -t PACKS < <(discover_packs)
  if [ "${#PACKS[@]}" -eq 0 ]; then
    echo "No context packs found under $REPO_DIR/content/context-packs" >&2
    exit 1
  fi
  echo "== Context packs available ($PROJECT) =="
  PS3="Context pack #? "
  select CONTEXT in "${PACKS[@]}"; do
    [ -n "$CONTEXT" ] && break
  done
}

# --- 1. project ---
PROJECT="${1:-}"
if [ -n "$PROJECT" ]; then
  shift
else
  mapfile -t PROJECTS < <(discover_build_dirs)
  if [ "${#PROJECTS[@]}" -eq 0 ]; then
    echo "No directories found under $WORKSPACE_ROOT" >&2
    exit 1
  fi
  echo "== Directories available under $WORKSPACE_ROOT =="
  PS3="Project #? "
  select PROJECT in "${PROJECTS[@]}"; do
    [ -n "$PROJECT" ] && break
  done
fi

REPO_DIR="$WORKSPACE_ROOT/$PROJECT"
if [ ! -d "$REPO_DIR" ]; then
  echo "No such directory: $REPO_DIR" >&2
  exit 1
fi
ensure_git_checkout "$REPO_DIR"

cd "$REPO_DIR"

# Some projects' `build` task (e.g. course-script-md sub-tasks) overwrites a
# tracked file under exports/ and writes a new timestamped export on every
# run, by that project's own design for its authors. Not something this
# read-only build surface should ever leave behind. Revert any tracked-content
# drift the build introduced, whether it succeeded or failed partway through,
# while preserving the real exit code.
cleanup() {
  local rc=$?
  DIRTY="$(git status --porcelain)"
  if [ -n "$DIRTY" ]; then
    echo "== workspace-build-sync: discarding tracked-content drift introduced by the build =="
    echo "$DIRTY"
    git checkout -- .
    git clean -fd -- exports 2>/dev/null || true
  fi
  exit "$rc"
}
trap cleanup EXIT

echo "== workspace-build-sync: fetching origin ($PROJECT) =="
git fetch origin

# --- 2. branch(es) ---
BRANCH="${1:-}"
if [ -n "$BRANCH" ]; then
  shift
  echo "== workspace-build-sync: hard-reset to origin/${BRANCH} =="
  git reset --hard "origin/${BRANCH}"
  git clean -fdx -e node_modules -e build -e 'build-*'
  MERGED_BRANCHES=("$BRANCH")
else
  select_and_merge_branches "$PROJECT"
fi

echo "== Now at: $(git rev-parse --short HEAD)  ($(git log -1 --pretty=%s)); branches: ${MERGED_BRANCHES[*]} =="

# --- 3. target ---
TARGET="${1:-}"
if [ -n "$TARGET" ]; then
  shift
else
  echo "== Build target ($PROJECT) =="
  PS3="Target #? "
  select TARGET in "sync" "build" "preview"; do
    [ -n "$TARGET" ] && break
  done
fi
[ "$TARGET" = "sync" ] && TARGET=""

case "$TARGET" in
  "")
    echo "Sync only; no build target requested."
    ;;
  build)
    # A fresh sync wipes courses/_generated (gitignored), leaving src/course
    # dangling so grunt's check-build-target refuses. If nothing is currently
    # linked, generate + link the chosen context first (viewer.js cg), then build.
    if node tools/check-build-target.js >/dev/null 2>&1; then
      echo "== A course is already linked; building it as-is =="
    else
      echo "== No course linked (the sync wiped the generated one); generating + linking first =="
      CONTEXT="${1:-}"
      pick_context
      VIEWER="$(viewer_path)"
      echo "== Running: node ${VIEWER} cg ${CONTEXT} =="
      node "${VIEWER}" cg "${CONTEXT}"
    fi
    echo "== Running: npx grunt build =="
    npx grunt build
    ;;
  preview)
    CONTEXT="${1:-}"
    pick_context
    VIEWER="$(viewer_path)"
    echo "== Running: node ${VIEWER} cr ${CONTEXT} =="
    node "${VIEWER}" cr "${CONTEXT}"
    ;;
  *)
    echo "Unknown build target: '${TARGET}' (expected: sync|build|preview)" >&2
    exit 1
    ;;
esac
