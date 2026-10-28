#!/usr/bin/env bash
# kill-serve.sh — free the dev-server port, then launch grunt server on it.
#
# Was workspace-build-server.sh. Does no git work and no build: for the
# push + pull + build + serve sequence use pull-build-serve.sh, and to only
# free the port without starting anything use free-port.sh.
#
# The port is free-port.sh's business, not this script's. It is resolved once
# here and passed to both the kill and grunt's --port, so the port freed and
# the port served are always the same one. Set the port, or switch to being
# asked each run (PORT_MODE), in free-port.sh.
#
# Lives in _workspace/scripts-sa/ (project-management tooling, not part of the
# Adapt build chain), so it anchors itself to the repo root two levels up and
# runs there whatever pwd you invoke it from.
#
# Usage, from anywhere:
#   ./_workspace/scripts-sa/kill-serve.sh         port per free-port.sh
#   ./_workspace/scripts-sa/kill-serve.sh 9002    this port, no questions
#   PORT=9002 ./_workspace/scripts-sa/kill-serve.sh
set -euo pipefail

# Resolved absolutely, and before the cd: a relative BASH_SOURCE would
# otherwise resolve against the repo root and miss its own sibling script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"
echo "== repo root: $REPO_ROOT"

# Ask once (this is where an `ask` mode prompts), then reuse the answer: the
# second call is given the port explicitly, so it cannot prompt again.
SERVE_PORT="$("$SCRIPT_DIR/free-port.sh" --print-port "$@")"

echo "== freeing port ${SERVE_PORT} =="
"$SCRIPT_DIR/free-port.sh" "$SERVE_PORT"

echo "== launching grunt server on ${SERVE_PORT} =="
npx grunt server --port "$SERVE_PORT"
