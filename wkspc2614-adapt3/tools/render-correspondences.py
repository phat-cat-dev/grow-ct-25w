#!/usr/bin/env python3
"""
render-correspondences.py

(b) of the correspondences build: render the Pathway Table of Correspondences
HTML FROM the well (catalogue/context/correspondences.json), so the store is the
single source of truth and the HTML is a generated view. Inverse of
tools/extract-correspondences.py.

The HTML already carries all the presentation (CSS + the client-side table
renderer). This tool only replaces its embedded `const DATA = {...};` blob with
the store's render keys (pathways, meta, benchmarks, themes, rows, built) in the
order the renderer expects, emitted compact to keep the artifact diff minimal.
Store-only provenance keys (correspondencesVersion, source) are not published
into the artifact.

Workflow: edit the well -> run this -> commit the regenerated HTML.

Usage:
  python3 tools/render-correspondences.py \
      [--store catalogue/context/correspondences.json] \
      [--html docs/curriculum/pathway-table-of-correspondences.html] \
      [--check]   # verify the HTML already matches the store; non-zero if drifted
"""
import argparse
import json
import re
import sys
from pathlib import Path

DEF_STORE = "catalogue/context/correspondences.json"
DEF_HTML = "docs/curriculum/pathway-table-of-correspondences.html"
RENDER_KEYS = ["pathways", "meta", "benchmarks", "themes", "rows", "built"]


def data_blob(store):
    """The render object, in the renderer's key order, compact."""
    data = {k: store.get(k) for k in RENDER_KEYS}
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if "</script" in js.lower():
        raise SystemExit("REFUSED: store content contains a </script> sequence.")
    return js


def swap_data(html_text, js):
    """Replace the balanced `const DATA = {...};` with the new blob."""
    m = re.search(r"const DATA = (\{)", html_text)
    if not m:
        raise SystemExit("REFUSED: no `const DATA = {` in the HTML shell.")
    start = m.start(1)
    depth = 0
    for i in range(start, len(html_text)):
        if html_text[i] == "{":
            depth += 1
        elif html_text[i] == "}":
            depth -= 1
            if depth == 0:
                obj_end = i + 1
                break
    else:
        raise SystemExit("REFUSED: DATA braces never balanced.")
    # include a trailing semicolon if present
    tail = obj_end
    if tail < len(html_text) and html_text[tail] == ";":
        tail += 1
    return html_text[:start] + js + ";" + html_text[tail:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default=DEF_STORE)
    ap.add_argument("--html", default=DEF_HTML)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    store = json.loads(Path(args.store).read_text(encoding="utf8"))
    html_path = Path(args.html)
    if not html_path.exists():
        raise SystemExit(f"REFUSED: HTML shell not found: {html_path}")

    html = html_path.read_text(encoding="utf8")
    rendered = swap_data(html, data_blob(store))

    if args.check:
        if rendered == html:
            print("OK: HTML matches the store (no drift).")
            return
        print("DRIFT: HTML does not match the store — run without --check to regenerate.")
        sys.exit(1)

    if rendered == html:
        print(f"No change: {html_path} already matches the store.")
        return
    html_path.write_text(rendered, encoding="utf8")
    print(f"Rendered {html_path} from {args.store}")
    print(f"  pathways {len(store['pathways'])}, rows {len(store['rows'])}, "
          f"themes {len(store['themes'])}, benchmarks {len(store['benchmarks'])}")


if __name__ == "__main__":
    main()
