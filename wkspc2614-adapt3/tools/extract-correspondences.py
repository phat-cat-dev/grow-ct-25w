#!/usr/bin/env python3
"""
extract-correspondences.py

Extract the embedded `const DATA = {...}` correspondence matrix from the rendered
Pathway Table of Correspondences HTML into a structured, version-controlled store:
catalogue/context/correspondences.json — the "correspondences well".

The HTML (docs/curriculum/pathway-table-of-correspondences.html) renders its table
client-side from that JS blob, so the blob is the only structured home for the
FHEQ-grounded, per-card, per-pathway practice/knowledge/identity readings. This
tool lifts it into JSON so the well owns it; a generator (tools/render-
correspondences.*, to come) will later render the HTML back FROM this store.

Concept-ordered output (identity/provenance -> dimensions -> strands -> lenses ->
subjects -> the matrix body), per schemas/README.md. The DATA is emitted
faithfully; nothing is reworded here.

Usage:
  python3 tools/extract-correspondences.py \
      [--html docs/curriculum/pathway-table-of-correspondences.html] \
      [--out catalogue/context/correspondences.json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

DEF_HTML = "docs/curriculum/pathway-table-of-correspondences.html"
DEF_OUT = "catalogue/context/correspondences.json"
VERSION = "1.0.0"


def extract_data(html_text):
    """Pull the balanced `const DATA = {...}` object and parse it."""
    m = re.search(r"const DATA = (\{)", html_text)
    if not m:
        raise SystemExit("REFUSED: no `const DATA = {` found in the HTML.")
    start = m.start(1)
    depth = 0
    for i in range(start, len(html_text)):
        ch = html_text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(html_text[start:i + 1])
    raise SystemExit("REFUSED: DATA object braces never balanced.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", default=DEF_HTML)
    ap.add_argument("--out", default=DEF_OUT)
    args = ap.parse_args()

    html_path = Path(args.html)
    if not html_path.exists():
        raise SystemExit(f"REFUSED: HTML not found: {html_path}")

    data = extract_data(html_path.read_text(encoding="utf8"))

    # Concept-ordered store: provenance -> reading dimensions -> pathway strands
    # -> theme lenses -> subject benchmarks -> the card x pathway matrix (rows).
    store = {
        "correspondencesVersion": VERSION,
        "built": data.get("built"),
        "source": {
            "doc": "docs/curriculum/pathway-table-of-correspondences.html",
            "ref": f"Pathway Table of Correspondences, built {data.get('built')}",
            "note": "Extracted verbatim from the rendered table's embedded DATA by tools/extract-correspondences.py; readings are authored in the project's own words with FHEQ statement ids as grounding pointers."
        },
        "meta": data["meta"],            # the 6 reading dimensions (incl. dual axes)
        "pathways": data["pathways"],    # the 14 academic-practice strands
        "themes": data["themes"],        # development / metacog / professional / qual-framework / cross-cutting lenses
        "benchmarks": data["benchmarks"],  # the 54 subject benchmarks
        "rows": data["rows"]             # the card grid (F..L8); each row carries meta + per-pathway cells + per-theme + per-benchmark readings
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(store, indent=2, ensure_ascii=False) + "\n", encoding="utf8")

    print(f"Wrote {out_path}")
    print(f"  pathways:   {len(store['pathways'])}")
    print(f"  rows:       {len(store['rows'])}  ({', '.join(r['row'] for r in store['rows'])})")
    print(f"  themes:     {len(store['themes'])}")
    print(f"  benchmarks: {len(store['benchmarks'])}")
    print(f"  meta dims:  {store['meta']}")


if __name__ == "__main__":
    main()
