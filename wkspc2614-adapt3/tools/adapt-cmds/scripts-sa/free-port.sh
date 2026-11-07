#!/usr/bin/env bash
# free-port.sh — kill whatever is listening on the dev-server port.
# Does nothing else: no fetch, no reset, no build, no launch. To free the port
# and then start the server, use kill-serve.sh.
#
# Replaces the older fuser-only kill-port-9001.sh.
#
# A pure port operation: it needs no repo root and no particular pwd, so it is
# safe to call from anywhere.
#
# THIS FILE OWNS THE PORT for the whole scripts-sa set. kill-serve.sh and
# pull-build-serve.sh ask it which port to use (--print-port) and pass that one
# port to both the kill and grunt's --port, so freeing and serving can never
# disagree. Change the port, or how the port is chosen, here and only here.
#
# Usage:
#   ./free-port.sh              free the port chosen by PORT_MODE below
#   ./free-port.sh 9002         free that port; never asks, whatever the mode
#   ./free-port.sh --print-port print the chosen port and exit, freeing nothing
#   PORT=9002 ./free-port.sh    env override, for scripts and CI
set -euo pipefail

# ===========================================================================
# CONFIGURATION — the two modes. Change PORT_MODE here.
#
#   fixed  always use DEFAULT_PORT and never ask. For when the port never
#          moves: run it and it works, nothing to answer.
#
#   ask    offer DEFAULT_PORT and let you accept it with Enter or type a
#          different one. For when you are juggling ports and the answer
#          changes run to run.
#
# Either way an explicit argument or a PORT env var wins and never prompts, so
# switching to `ask` cannot hang a script or a CI job that calls this.
# ===========================================================================
PORT_MODE="fixed"     # fixed | ask
DEFAULT_PORT=9000
# ===========================================================================

die() { printf '%s\n' "$*" >&2; exit 1; }

valid_port() {
  [[ "$1" =~ ^[0-9]+$ ]] && (( $1 >= 1 && $1 <= 65535 ))
}

# Decide the port, in precedence order: argument, env, mode, default.
# Everything here talks on stderr and reads from /dev/tty, so that
# `$(free-port.sh --print-port)` captures the port and nothing else.
resolve_port() {
  local arg="${1:-}"

  if [[ -n "$arg" ]]; then
    valid_port "$arg" || die "Not a usable port: '${arg}' (want 1-65535)"
    printf '%s\n' "$arg"
    return
  fi

  if [[ -n "${PORT:-}" ]]; then
    valid_port "$PORT" || die "Not a usable port in \$PORT: '${PORT}' (want 1-65535)"
    printf '%s\n' "$PORT"
    return
  fi

  if [[ "$PORT_MODE" == "ask" ]]; then
    # No terminal to ask on (piped, cron, CI): take the default rather than hang.
    if [[ ! -r /dev/tty ]]; then
      printf 'PORT_MODE=ask but there is no terminal to ask on; using %s\n' "$DEFAULT_PORT" >&2
      printf '%s\n' "$DEFAULT_PORT"
      return
    fi
    local reply
    while :; do
      printf 'Port? [%s] (Enter accepts, or type another): ' "$DEFAULT_PORT" >&2
      IFS= read -r reply < /dev/tty || reply=""
      reply="${reply//[[:space:]]/}"
      if [[ -z "$reply" ]]; then
        printf '%s\n' "$DEFAULT_PORT"
        return
      fi
      if valid_port "$reply"; then
        printf '%s\n' "$reply"
        return
      fi
      printf "  '%s' is not a port between 1 and 65535.\\n" "$reply" >&2
    done
  fi

  # fixed, or any unrecognised PORT_MODE: the default, no questions.
  if [[ "$PORT_MODE" != "fixed" ]]; then
    printf "PORT_MODE is '%s'; expected 'fixed' or 'ask'. Treating it as fixed.\\n" "$PORT_MODE" >&2
  fi
  printf '%s\n' "$DEFAULT_PORT"
}

listeners() {
  local port="$1"
  if command -v lsof >/dev/null 2>&1; then
    lsof -ti "tcp:${port}" || true
  elif command -v fuser >/dev/null 2>&1; then
    fuser -n tcp "${port}" 2>/dev/null || true
  else
    die "Need lsof or fuser to find listeners on :${port}"
  fi
}

# --- arguments -------------------------------------------------------------
PRINT_ONLY=false
WANTED=""
case "${1:-}" in
  --print-port) PRINT_ONLY=true; WANTED="${2:-}" ;;   # optional port after it
  -h|--help)    sed -n '2,20p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
  "")           ;;
  *)            WANTED="$1" ;;
esac

TARGET_PORT="$(resolve_port "$WANTED")"

if [[ "$PRINT_ONLY" == true ]]; then
  printf '%s\n' "$TARGET_PORT"
  exit 0
fi

# --- free it ---------------------------------------------------------------
PIDS="$(listeners "$TARGET_PORT")"

if [[ -z "${PIDS// /}" ]]; then
  echo "No process on :${TARGET_PORT}"
  exit 0
fi

echo "Killing PIDs on :${TARGET_PORT} -> ${PIDS}"
kill ${PIDS} 2>/dev/null || true
sleep 1

# Anything that ignored SIGTERM gets SIGKILL.
LEFT="$(listeners "$TARGET_PORT")"
if [[ -n "${LEFT// /}" ]]; then
  echo "Still alive, sending SIGKILL -> ${LEFT}"
  kill -9 ${LEFT} 2>/dev/null || true
fi

echo "Port ${TARGET_PORT} free."
