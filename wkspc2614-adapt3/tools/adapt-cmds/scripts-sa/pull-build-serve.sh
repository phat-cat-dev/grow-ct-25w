#!/usr/bin/env bash
# pull-build-serve.sh — safely push + pull latest, build, free the dev-server
# port, then launch grunt server-scorm on it.
#
# Push/merge policy matches gm-up (gits-mgmt): fetch + merge --no-edit, never
# force, never rebase. A conflict pauses here rather than guessing. Unlike
# gm-up, this never auto-commits a dirty tree — commit your own work (or run
# gm-up) first; pub aborts rather than clobbering uncommitted changes.
#
# The port is free-port.sh's business: resolved once here, then passed to both
# the kill and grunt's --port. Set it, or switch to being asked each run
# (PORT_MODE), in free-port.sh.
#
# Usage, from anywhere:
#   ./_workspace/scripts-sa/pull-build-serve.sh        port per free-port.sh
#   ./_workspace/scripts-sa/pull-build-serve.sh 9002   this port, no questions
#
# Lives in _workspace/scripts-sa/ (project-management tooling, not part of the
# Adapt build chain), so it anchors itself to the repo root two levels up and
# runs there whatever pwd you invoke it from.
set -euo pipefail

# Resolved absolutely, and before the cd: a relative BASH_SOURCE would
# otherwise resolve against the repo root and miss its own sibling script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

echo "== pwd: $(pwd)"

echo "== git sync: push + pull (safe: only if working tree is clean) =="
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Working tree has uncommitted changes. Aborting. Commit first (or run gm-up)." >&2
  git status --short
  exit 1
fi

branch="$(git branch --show-current)"
if [[ -z "${branch}" ]]; then
  echo "Detached HEAD, no branch to sync." >&2
  exit 1
fi

if ! git ls-remote --exit-code --heads origin "${branch}" >/dev/null 2>&1; then
  echo "'${branch}' is not on origin yet; pushing it for the first time."
  git push -u origin "${branch}"
else
  git fetch --quiet origin "${branch}"
  if ! git merge --no-edit "origin/${branch}"; then
    echo "Merge stopped on a conflict. Resolve the listed files, then:" >&2
    echo "       git add <files> && git commit && git push origin ${branch}" >&2
    echo "   or back out with:  git merge --abort" >&2
    exit 1
  fi
  git push origin "${branch}"
fi
echo "EXIT: $?"

echo "== grunt build =="
npx grunt build
echo "EXIT: $?"

# Asked for once (in an `ask` mode this is the prompt), then reused.
SERVE_PORT="$("$SCRIPT_DIR/free-port.sh" --print-port "$@")"

echo "== freeing port ${SERVE_PORT} =="
"$SCRIPT_DIR/free-port.sh" "$SERVE_PORT"

echo "== launching grunt server-scorm on ${SERVE_PORT} =="
npx grunt server-scorm --port "$SERVE_PORT"
