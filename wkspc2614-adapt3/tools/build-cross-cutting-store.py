#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-cross-cutting-store.py

Build the shared cross-cutting store: the generic, pathway- and subject-
independent scaffolding that the per-subject and per-pathway tier readings
specialise. One file, concept-ordered so an agent reads it top to bottom:

  1. tierModel          - the tier<->level spine: our three tiers
                          (introductory/intermediate/advanced) with Abbott's
                          overlap formula, the edge rows (F, L8), and the full
                          row grid, each row carrying BOTH its tier and its
                          indicative FHEQ level.
  2. genericLadder      - the practitioner F->L8 readings (practice / knowledge
                          / identity), the generic spine the subject and
                          pathway readings specialise. Each row also carries
                          tier + fheqLevel (dual axes everywhere).
  3. frameworks         - FHEQ / CQFW / FQHEIS / QF-EHEA, each with its
                          dimensions and the per-row level alignment.
  4. crossCuttingThemes - enterprise / employability / ESD / Ofqual, each
                          mapped onto the row grid.
  5. developmentModels  - Barnett, SOLO, Dreyfus, Anderson & Krathwohl, Lave &
                          Wenger, etc., each placed against the rows.

Sources (clean YAML, in the old repo today):
  <wide>/cross-cutting-themes.yaml   (practitioner ladder, themes, frameworks)
  <wide>/models-of-development.yaml  (developmentModels)

A working compilation: every reading in the sources is the ing drafters' own
words, never issuer text. This tool restructures and concept-orders it; it
invents nothing. The per-pathway wide files (pathway-readings, fheq-readings)
are NOT read here - they belong to the pathway reference.

Usage:
  python3 tools/build-cross-cutting-store.py           # writes the store
  python3 tools/build-cross-cutting-store.py --dry-run # report only
"""
import argparse
import json
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("REFUSED: PyYAML is required (pip install pyyaml).")

DEFAULT_WIDE_ROOT = (
    "/home/user/wkspc2614-adapt/source-kb/canon-adp/secondary-data/"
    "ingested/themes/pathways/integrations/cards/wide"
)
DEFAULT_OUT = (
    "/home/user/wkspc2613-adapt2/catalogue/context/shared/cross-cutting.json"
)
WIDE_REPO_PATH = (
    "source-kb/canon-adp/secondary-data/ingested/themes/pathways/"
    "integrations/cards/wide"
)

# The row grid. F = foundation / pre-entry, L8 = beyond the degree; i/d/e are
# the three tiers, three rows each.
ROW_ORDER = ["F", "i1", "i2", "i3", "d1", "d2", "d3", "e1", "e2", "e3", "L8"]
ROW_TIER = {"i": "introductory", "d": "intermediate", "e": "advanced"}
ROW_FHEQ = {
    "F": 3,
    "i1": 3, "i2": 4, "i3": 5,
    "d1": 4, "d2": 5, "d3": 6,
    "e1": 5, "e2": 6, "e3": 7,
    "L8": 8,
}

# Abbott's tier<->level overlap formula (9 October 2026). The tiers are loosely
# based on FHEQ levels and deliberately overlap; both axes are kept because
# both get called upon.
OVERLAP_NOTE = (
    "Our tiers are loosely based on FHEQ levels and overlap on purpose. "
    "Introductory runs L3 to the lower end of L5; Intermediate runs the top "
    "of L4 to the bottom of L6; Advanced runs the top of L5 to L7. Both axes "
    "are kept on every tiered item because both can be useful; the per-row "
    "fheqLevel is the single indicative level, the fheqRange is the tier's "
    "loose span."
)
TIER_RANGES = {
    "introductory": {"min": 3, "max": 5,
                     "note": "L3 to the lower end of L5"},
    "intermediate": {"min": 4, "max": 6,
                     "note": "top of L4 to the bottom of L6"},
    "advanced": {"min": 5, "max": 7,
                 "note": "top of L5 to L7"},
}


def row_tier(row_id):
    if row_id == "F":
        return "foundation"
    if row_id == "L8":
        return "beyond"
    return ROW_TIER[row_id[0]]


def build_tier_model():
    tiers = []
    for tier, rng in TIER_RANGES.items():
        rows = [r for r in ROW_ORDER if row_tier(r) == tier]
        tiers.append({
            "tier": tier,
            "rows": rows,
            "fheqRange": {"min": rng["min"], "max": rng["max"]},
            "note": rng["note"],
        })
    edge_rows = [
        {"rowId": "F", "role": "foundation / pre-entry (level 3 study)",
         "fheqLevel": ROW_FHEQ["F"]},
        {"rowId": "L8", "role": "beyond the taught degree (doctoral)",
         "fheqLevel": ROW_FHEQ["L8"]},
    ]
    rows = [
        {"rowId": r, "tier": row_tier(r), "fheqLevel": ROW_FHEQ[r]}
        for r in ROW_ORDER
    ]
    return {
        "note": OVERLAP_NOTE,
        "tiers": tiers,
        "edgeRows": edge_rows,
        "rows": rows,
    }


def build_generic_ladder(cct):
    pr = cct.get("practitioner", {}) or {}
    heads = pr.get("heads", [])
    src_rows = pr.get("rows", {}) or {}
    rows = []
    for r in ROW_ORDER:
        triad = src_rows.get(r)
        if not triad:
            continue
        practice = triad[0] if len(triad) > 0 else None
        knowledge = triad[1] if len(triad) > 1 else None
        identity = triad[2] if len(triad) > 2 else None
        rows.append({
            "rowId": r,
            "tier": row_tier(r),
            "fheqLevel": ROW_FHEQ[r],
            "practice": practice,
            "knowledge": knowledge,
            "identity": identity,
        })
    return {"heads": heads, "rows": rows}


def split_ids(cell):
    """A theme/framework id cell may hold comma-separated ids or be empty."""
    if not cell:
        return []
    return [p.strip() for p in str(cell).split(",") if p.strip()]


def build_themes(cct):
    out = []
    for t in cct.get("themes", []) or []:
        entry = {
            "key": t.get("key"),
            "name": t.get("name"),
            "run": t.get("run"),
            "note": t.get("note"),
        }
        if t.get("byLevel"):
            entry["byLevel"] = True
            entry["levels"] = t.get("levels", {})
            entry["rowLevel"] = t.get("rowLevel", {})
        else:
            rows = []
            src = t.get("rows", {}) or {}
            for r in ROW_ORDER:
                cell = src.get(r)
                if cell is None:
                    continue
                ids = split_ids(cell[0]) if len(cell) > 0 else []
                reading = cell[1] if len(cell) > 1 else None
                rows.append({
                    "rowId": r,
                    "tier": row_tier(r),
                    "ids": ids,
                    "reading": reading,
                })
            entry["rows"] = rows
        out.append(entry)
    return out


def build_frameworks(cct):
    out = []
    for q in cct.get("qualifications", []) or []:
        entry = {
            "key": q.get("key"),
            "name": q.get("name"),
            "run": q.get("run"),
            "note": q.get("note"),
            "scheme": q.get("scheme"),
            "dims": q.get("dims", []),
            "rowLevel": q.get("rowLevel", {}),
        }
        if q.get("labels"):
            entry["labels"] = q["labels"]
        out.append(entry)
    return out


def build_models(mod):
    out = []
    for m in mod.get("models", []) or []:
        subs = m.get("subs", [])
        rows = []
        src = m.get("rows", {}) or {}
        for r in ROW_ORDER:
            cells = src.get(r)
            if cells is None:
                continue
            rows.append({
                "rowId": r,
                "tier": row_tier(r),
                "cells": cells,
            })
        out.append({
            "key": m.get("key"),
            "name": m.get("name"),
            "ref": m.get("ref"),
            "note": m.get("note"),
            "subs": subs,
            "rows": rows,
        })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wide-root", default=DEFAULT_WIDE_ROOT)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cct_path = os.path.join(args.wide_root, "cross-cutting-themes.yaml")
    mod_path = os.path.join(args.wide_root, "models-of-development.yaml")
    for p in (cct_path, mod_path):
        if not os.path.exists(p):
            sys.exit(f"REFUSED: source not found: {p}")

    cct = yaml.safe_load(open(cct_path, encoding="utf-8"))
    mod = yaml.safe_load(open(mod_path, encoding="utf-8"))

    store = {
        "crossCuttingVersion": "1.0.0",
        "tierModel": build_tier_model(),
        "genericLadder": build_generic_ladder(cct),
        "frameworks": build_frameworks(cct),
        "crossCuttingThemes": build_themes(cct),
        "developmentModels": build_models(mod),
        "source": {
            "repo": "wkspc2614-adapt",
            "files": [
                f"{WIDE_REPO_PATH}/cross-cutting-themes.yaml",
                f"{WIDE_REPO_PATH}/models-of-development.yaml",
            ],
            "note": (
                "ing's own readings, restructured and concept-ordered. No "
                "issuer text copied; theme/framework id cells are traceability "
                "pointers into the standards runs."
            ),
        },
    }

    # Report
    print(f"tierModel rows: {len(store['tierModel']['rows'])} "
          f"(tiers {len(store['tierModel']['tiers'])}, "
          f"edge {len(store['tierModel']['edgeRows'])})")
    print(f"genericLadder rows: {len(store['genericLadder']['rows'])}")
    print(f"frameworks: {len(store['frameworks'])} "
          f"({', '.join(f['key'] for f in store['frameworks'])})")
    print(f"crossCuttingThemes: {len(store['crossCuttingThemes'])} "
          f"({', '.join(t['key'] for t in store['crossCuttingThemes'])})")
    print(f"developmentModels: {len(store['developmentModels'])} "
          f"({', '.join(m['key'] for m in store['developmentModels'])})")

    if args.dry_run:
        print("DRY RUN: no file written.")
        return

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(store, f, indent=2, ensure_ascii=False)
    print(f"wrote {args.out} ({os.path.getsize(args.out)} bytes)")


if __name__ == "__main__":
    main()
