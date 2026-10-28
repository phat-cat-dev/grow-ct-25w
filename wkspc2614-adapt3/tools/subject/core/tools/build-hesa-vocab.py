#!/usr/bin/env python3
"""
build-hesa-vocab.py — deterministic builder for tools/subject/core/vocab/cah.json
and tools/subject/core/vocab/hecos.json from HESA's own CSVs (HSV-1,
docs/project/open-decisions.md, landed 26 Sep 2026; moved under tools/subject/
by TLS-1 and HMD-1, adp-0204).

HESA's CSVs are never committed to this repo. This tool reads them from a
directory given on the command line, checks each against a hash held here as
a constant, and refuses to run if any differs — the vocabulary is built from
HESA's data, not typed or copied by hand, and a build against drifted or
substituted input is a build against the wrong input.

Inputs (all read with utf-8-sig, via the csv module):
    CAH_Groupings.csv        — every CAH1/CAH2/CAH3 code, its label, its
                                parent; one row per CAH3 leaf, plus one row
                                where all three codes are CAHZ5 ("Not
                                applicable"), HESA's own placeholder.
    HECoS_CAH_Mappings.csv   — every HECoS code's CAH3 classification.
    hecos_vocab.csv          — every HECoS code, term, definition, scope note.
    hecos_preferred.csv      — non-preferred terms per HECoS code.
    hecos_related.csv        — related-code pairs per HECoS code.

Outputs, written to the directory given on the command line as cah.json and
hecos.json: both with sorted object keys and arrays sorted by code, so two
runs against the same input are byte-identical.

cah.json's cah1/cah2/cah3 entries carry forward any field an existing entry
at the same code already has beyond code/label/parent, read from this repo's
current tools/subject/core/vocab/cah.json before it is overwritten (so a
field the CSVs do not themselves supply is never dropped, and never invented
for the codes that do not already have it).

cah.json's previousSource, cah3Note and cah3NoteSuperseded are frozen legacy
fields carried from the pre-HSV-1 store (git show 142298d:vocab-kb/cah.json),
held here as the LEGACY_CAH_SOURCE and LEGACY_CAH3_NOTE constants rather than
read from the live store: reading them from the store the tool is about to
overwrite let a second run promote that run's own (correct) "source" into
"previousSource", overwriting the true EPrints-era record it was meant to
preserve. Found and fixed by adp-0187.

Usage:
    python3 tools/subject/core/tools/build-hesa-vocab.py <csv-dir> <out-dir>

Landed: 26 Sep 2026, Prompt adp-0184 (HSV-1).
Legacy-field reproducibility fixed: 27 Sep 2026, adp-0187.
"""

import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
EXISTING_CAH_PATH = REPO_ROOT / "tools" / "subject" / "core" / "vocab" / "cah.json"

# Held as constants per HSV-1: a build refuses to run if any input's hash
# differs from the value verified against these CSVs on 26 Sep 2026.
EXPECTED_HASHES = {
    "HECoS_CAH_Mappings.csv": "26a047b119e5617ae8827b1fd03bad471c6fd1408317f99ecfe749eaf51c5ee0",
    "CAH_Groupings.csv": "f113839534b8f18696059feeaed78fe0f2e1211003171c3e4e05d3a373bd3d94",
    "hecos_vocab.csv": "38af934ed6ddfe7a914938d189d8f9d3b6c9d6f526d576602f652ead7e9fe6cc",
    "hecos_preferred.csv": "12c4de65b628fed7ff3527753ea69a2f885b50f7cddd07847af95a08f6bbe872",
    "hecos_related.csv": "ee9c60532d67b7bc5fe8d39521c8d2924b5bec4b4e374ae5ba98bcc7bec4efb5",
}

SOURCE_ISSUER = "HESA"
SOURCE_RETRIEVED = "2026-09-26"
SOURCE_PROVENANCE = "supplied by Abbott, downloaded from HESA"
SUPERSEDED_BY = "HSV-1"

# Frozen legacy content, held as constants rather than read from the live
# store (see the module docstring). Character-for-character identical to
# git show 142298d:vocab-kb/cah.json's "source" object and "cah3Note" field;
# verified against that commit by adp-0187, never edited after.
LEGACY_CAH_SOURCE = {
    "issuer": "HESA",
    "vocabulary": "Common Aggregation Hierarchy (CAH)",
    "version": "1.3.4",
    "url": "https://files.eprints.org/2553/1/CAH-1_3_4-subjects.csv",
    "retrieved": "2026-09-18",
    "note": "HESA's own domain (hesa.ac.uk/collection/coding-manual-tools/hecoscahdata/cah and hesa.ac.uk/support/documentation/hecos/cah) returned HTTP 403 to automated fetch this sitting (curl and WebFetch both tried and both blocked). This file is the CAH-to-HECoS subjects CSV as archived by the University of Southampton EPrints file repository (eprints record 2553, titled 'The Higher Education Classification of Subjects (HECoS) Common Aggregation Hierarchy - v1.3.4'), which is a mirror of HESA's own published CAH v1.3.4 data, not a retyped or reconstructed list. Version and group counts (21 CAH1, 35 CAH2, 167 CAH3) were cross-checked against a web search of HESA's own support documentation before use and matched exactly.",
}

LEGACY_CAH3_NOTE = (
    "CAH3 (subject-level) landed only for disciplines named by this repo's existing content-pack directories (content/context-packs/: banking-and-finance, criminology, project-management, psychology, sports-journalism; baseline excluded, not a subject), per Prompt 67 ruling 3. Full CAH3 in v1.3.4 has 167 entries; this file carries only the four above. No CAH3 code named 'criminology' (or any crime/justice/policing term) exists anywhere in CAH v1.3.4 — checked directly against this file's own source CSV, grep for 'crim', 'justice', 'polic' under CAH15 (social sciences) and CAH16 (law) — so criminology is deliberately represented at CAH2 only (CAH15-01, sociology/social policy/anthropology, already present above as it is one of the complete CAH2 set) with no CAH3 leaf; inventing one would violate ruling 3's 'do not invent'. project-management has no CAH3 term of its own either (checked: CAH17-01's nine children are business and management (non-specific), accounting, tourism/transport/travel, marketing, human resource management, others in business and management, finance, business studies, management studies — no 'project management'); CAH17-01-01 (business and management, non-specific) is landed instead, matching the existing source-kb.json qaa/business-and-management-2023 entry's own collapsed classification, which the project-management context pack draws on."
)


def sha256_stripped(path: Path) -> str:
    """SHA-256 of a file's bytes with one trailing newline stripped."""
    return hashlib.sha256(path.read_bytes().rstrip(b"\n")).hexdigest()


def verify_hashes(csv_dir: Path) -> list:
    """Return a list of problems (empty if every file matches)."""
    problems = []
    for name, expected in EXPECTED_HASHES.items():
        path = csv_dir / name
        if not path.exists():
            problems.append(f"{name}: not found in {csv_dir}")
            continue
        actual = sha256_stripped(path)
        if actual != expected:
            problems.append(f"{name}: hash mismatch (expected {expected}, got {actual})")
    return problems


def read_rows(path: Path) -> list:
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def file_record(csv_dir: Path, name: str, row_count: int) -> dict:
    return {"name": name, "sha256": EXPECTED_HASHES[name], "dataRows": row_count}


def load_existing_cah_extras() -> dict:
    """
    code -> {extra field: value, ...} for every field an existing cah1/cah2/cah3
    entry carries beyond code/label/parent. Empty dict per code where there is
    nothing extra. Empty overall if the existing store is absent or unreadable.
    """
    extras = {}
    if not EXISTING_CAH_PATH.exists():
        return extras
    try:
        existing = json.loads(EXISTING_CAH_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return extras
    for level in ("cah1", "cah2", "cah3"):
        for row in existing.get(level, []) or []:
            if not isinstance(row, dict) or "code" not in row:
                continue
            extra = {k: v for k, v in row.items() if k not in ("code", "label", "parent")}
            if extra:
                extras[row["code"]] = extra
    return extras


def build_cah_store(csv_dir: Path) -> dict:
    grouping_rows = read_rows(csv_dir / "CAH_Groupings.csv")

    placeholder_rows = [r for r in grouping_rows if r["CAH3_Code"] == "CAHZ5"]
    real_rows = [r for r in grouping_rows if r["CAH3_Code"] != "CAHZ5"]

    # A row using the CAHZ5 placeholder must use it at all three levels, or
    # the data means something this tool has not been told about.
    for r in grouping_rows:
        codes = {r["CAH1_Code"], r["CAH2_Code"], r["CAH3_Code"]}
        if "CAHZ5" in codes and codes != {"CAHZ5"}:
            raise SystemExit(f"CAHZ5 appears at only some levels of one row: {r}")
    if len(placeholder_rows) != 1:
        raise SystemExit(f"expected exactly one CAHZ5 row, found {len(placeholder_rows)}")

    extras = load_existing_cah_extras()

    def dedup(rows, code_key, label_key, parent_key=None):
        by_code = {}
        for r in rows:
            code = r[code_key]
            label = r[label_key]
            parent = r[parent_key] if parent_key else None
            if code in by_code:
                prior = by_code[code]
                if prior["label"] != label or prior.get("parent") != parent:
                    raise SystemExit(
                        f"code {code} appears twice with different label/parent: "
                        f"{prior} vs label={label!r} parent={parent!r}"
                    )
                continue
            entry = {"code": code, "label": label}
            if parent_key:
                entry["parent"] = parent
            entry.update(extras.get(code, {}))
            by_code[code] = entry
        return sorted(by_code.values(), key=lambda e: e["code"])

    cah1 = dedup(real_rows, "CAH1_Code", "CAH1_Label")
    cah2 = dedup(real_rows, "CAH2_Code", "CAH2_Label", "CAH1_Code")
    cah3 = dedup(real_rows, "CAH3_Code", "CAH3_Label", "CAH2_Code")

    placeholder_row = placeholder_rows[0]
    placeholders = [
        {
            "code": "CAHZ5",
            "label": placeholder_row["CAH3_Label"],
            "levels": ["cah1", "cah2", "cah3"],
            "selectable": False,
        }
    ]

    previous_source = dict(LEGACY_CAH_SOURCE)
    previous_source["supersededBy"] = SUPERSEDED_BY

    store = {
        "source": {
            "issuer": SOURCE_ISSUER,
            "vocabulary": "Common Aggregation Hierarchy (CAH)",
            "version": "1.3.4",
            "url": "https://www.hesa.ac.uk/support/documentation/hecos/cah",
            "retrieved": SOURCE_RETRIEVED,
            "licence": {
                "value": None,
                "url": "https://www.hesa.ac.uk/support/documentation/hecos/cah",
                "note": "HESA's CAH page states no licence.",
            },
            "provenance": SOURCE_PROVENANCE,
            "files": [file_record(csv_dir, "CAH_Groupings.csv", len(grouping_rows))],
        },
        "cah1": cah1,
        "cah2": cah2,
        "cah3": cah3,
        "placeholders": placeholders,
    }
    store["previousSource"] = previous_source
    store["cah3Note"] = LEGACY_CAH3_NOTE
    store["cah3NoteSuperseded"] = {"by": SUPERSEDED_BY, "date": SOURCE_RETRIEVED}
    return store


def build_hecos_store(csv_dir: Path) -> dict:
    vocab_rows = read_rows(csv_dir / "hecos_vocab.csv")
    mapping_rows = read_rows(csv_dir / "HECoS_CAH_Mappings.csv")
    preferred_rows = read_rows(csv_dir / "hecos_preferred.csv")
    related_rows = read_rows(csv_dir / "hecos_related.csv")

    vocab_by_code = {r["HECOS_subject_code"]: r for r in vocab_rows}
    mapping_cah3_by_code = {r["HECoS_Code"]: r["CAH3_Code"] for r in mapping_rows}
    mapping_label_by_code = {r["HECoS_Code"]: r["HECoS_Label"] for r in mapping_rows}

    non_preferred = defaultdict(set)
    for r in preferred_rows:
        non_preferred[r["Subject_code"]].add(r["Non_preferred_term"])

    related = defaultdict(set)
    for r in related_rows:
        a, b = r["HECOS_subject_code"], r["Related_HECOS_subject_code"]
        related[a].add(b)
        related[b].add(a)

    missing_cah3 = [code for code in vocab_by_code if code not in mapping_cah3_by_code]
    if missing_cah3:
        raise SystemExit(f"{len(missing_cah3)} vocabulary code(s) have no CAH3 mapping: {sorted(missing_cah3)[:5]}...")

    terms = []
    for code, row in vocab_by_code.items():
        scope_note = row["Scope_note"] or None
        terms.append(
            {
                "code": code,
                "term": row["Term"],
                "definition": row["Definition"],
                "scopeNote": scope_note,
                "cah3": mapping_cah3_by_code[code],
                "nonPreferredTerms": sorted(non_preferred.get(code, [])),
                "relatedCodes": sorted(c for c in related.get(code, []) if c != code),
            }
        )
    terms.sort(key=lambda t: t["code"])

    non_vocab_codes = sorted(set(mapping_cah3_by_code) - set(vocab_by_code))
    non_vocabulary_mappings = [
        {
            "code": code,
            "label": mapping_label_by_code[code],
            "cah3": mapping_cah3_by_code[code],
            "selectable": False,
        }
        for code in non_vocab_codes
    ]

    store = {
        "source": {
            "issuer": SOURCE_ISSUER,
            "vocabulary": "Higher Education Classification of Subjects (HECoS)",
            "release": None,
            "retrieved": SOURCE_RETRIEVED,
            "licence": {
                "value": "CC-BY-4.0",
                "url": "https://www.hesa.ac.uk/innovation/hecos",
                "note": None,
            },
            "provenance": SOURCE_PROVENANCE,
            "note": "HESA's pages give no HECoS version or release date.",
            "files": [
                file_record(csv_dir, "hecos_vocab.csv", len(vocab_rows)),
                file_record(csv_dir, "HECoS_CAH_Mappings.csv", len(mapping_rows)),
                file_record(csv_dir, "hecos_preferred.csv", len(preferred_rows)),
                file_record(csv_dir, "hecos_related.csv", len(related_rows)),
            ],
        },
        "terms": terms,
        "nonVocabularyMappings": non_vocabulary_mappings,
    }
    return store


def write_json(obj: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <csv-dir> <out-dir>", file=sys.stderr)
        return 2

    csv_dir = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])

    problems = verify_hashes(csv_dir)
    if problems:
        print("REFUSED — input hash check failed:", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1

    cah_store = build_cah_store(csv_dir)
    hecos_store = build_hecos_store(csv_dir)

    write_json(cah_store, out_dir / "cah.json")
    write_json(hecos_store, out_dir / "hecos.json")

    print(f"cah.json: {len(cah_store['cah1'])} cah1, {len(cah_store['cah2'])} cah2, "
          f"{len(cah_store['cah3'])} cah3, {len(cah_store['placeholders'])} placeholder(s)")
    print(f"hecos.json: {len(hecos_store['terms'])} terms, "
          f"{len(hecos_store['nonVocabularyMappings'])} non-vocabulary mapping(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
