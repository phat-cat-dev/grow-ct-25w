#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-subject-benchmark.py

Build a self-contained subject-benchmark authoring reference
(catalogue/context/subject/benchmarks/<id>.json) from two sources:

  1. The QAA Subject Benchmark Statement ingest markdown
     (source-kb/.../ingested/standards/ingest-std-qaa-<id>-benchmarks/...md),
     which carries YAML blocks per section (S1..S8, SB2..SB6, B1, B2a, S4,
     S4a, ...). This is where the statements, metadata, framework alignment
     and the practitioner/beneficiary rewrites come from.

  2. The subject's Adapt pathway map
     (tools/pathways/core/mapping/<id>.adapt-map.json), which carries the
     "spine": how this subject's benchmark relates to each of the 13 Adapt
     pathways. OPTIONAL: only `psychology-2023` has one today. When a subject
     has no map, `pathwayMapping` is written empty and the run report flags
     it. Re-running after a map is generated at the conventional path picks
     it up with no other change -- this is the plug-in point for a future
     map-generation stage.

The issuer's own text is copyright-held and never copied: the per-statement
`source` and `quote` fields are dropped; every statement carries only our
paraphrase and, where present, our practitioner/beneficiary rewrites.

Output is validated against schemas/catalogue.subject-benchmark.schema.json by
the repo's tools/validate-design-schemas.py (run separately, or with
--validate when available).

Usage:
  python3 tools/build-subject-benchmark.py --subject psychology-2023
  python3 tools/build-subject-benchmark.py --all
  python3 tools/build-subject-benchmark.py --all --dry-run
  python3 tools/build-subject-benchmark.py --subject law-2023 --no-index

A subject id is the ingest directory name with the `ingest-std-qaa-` prefix
and the `-benchmarks` suffix removed, e.g. `psychology-2023`, `law-2023`.
"""
import argparse
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("REFUSED: PyYAML is required (pip install pyyaml).")

# ---------------------------------------------------------------------------
# Defaults. Resolved relative to THIS repo (grow-course) so the ingest pipeline
# runs in place; override with the CLI flags if the inputs live elsewhere.
# REPO is the directory that holds tools/ (i.e. tools/..).
# ---------------------------------------------------------------------------
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INGEST_ROOT = os.path.join(
    REPO, "source-kb", "canon-adp", "secondary-data", "ingested", "standards")
DEFAULT_ADAPT_MAP_ROOT = os.path.join(
    REPO, "tools", "pathways", "core", "mapping")
DEFAULT_OUT_DIR = os.path.join(
    REPO, "catalogue", "context", "subject", "benchmarks")
DEFAULT_INDEX = os.path.join(
    REPO, "catalogue", "context", "subject", "benchmarks.json")
# The subject-benchmark cards: one <slug>.yaml per subject, carrying the
# per-tier practice/knowledge/identity readings.
DEFAULT_CARD_ROOT = os.path.join(
    REPO, "source-kb", "canon-adp", "secondary-data", "ingested",
    "themes", "pathways", "integrations", "cards", "wide", "benchmarks")

INGEST_PREFIX = "ingest-std-qaa-"
INGEST_SUFFIX = "-benchmarks"

# Copyright-held per-statement fields: never copied into our reference.
COPYRIGHT_FIELDS = {"source", "quote"}

# Repo-relative path templates recorded under `source` so a reader can trace
# provenance without the absolute environment paths leaking in.
INGEST_DOC_PATH_TMPL = (
    "source-kb/canon-adp/secondary-data/ingested/standards/"
    "ingest-std-qaa-{id}-benchmarks/ingest-std-qaa-{id}-benchmarks.md"
)
ADAPT_MAP_PATH_TMPL = "tools/pathways/core/mapping/{id}.adapt-map.json"
CARD_PATH_TMPL = (
    "source-kb/canon-adp/secondary-data/ingested/themes/pathways/"
    "integrations/cards/wide/benchmarks/{id}.yaml"
)

# The nine-card tier grid (build-card-file.py's own map): each card row carries
# BOTH a tier (from its letter) and an indicative FHEQ level (from the grid).
# Kept together per Abbott's dual-axis decision; the tier<->level overlap
# formula (Introductory L3->low-L5, Intermediate top-L4->low-L6, Advanced
# top-L5->L7) lives in the shared cross-cutting store, not per row.
ROW_ORDER = ["i1", "i2", "i3", "d1", "d2", "d3", "e1", "e2", "e3"]
ROW_TIER = {"i": "introductory", "d": "intermediate", "e": "advanced"}
ROW_FHEQ = {
    "i1": 3, "i2": 4, "i3": 5,
    "d1": 4, "d2": 5, "d3": 6,
    "e1": 5, "e2": 6, "e3": 7,
}

LICENCE = (
    "QAA copyright; held for study, never published. No issuer text (the "
    'per-statement "source" quote) is copied into this file; all statement '
    "text here is our own paraphrase or audience rewrite."
)

# An enumerated graduate-skill bullet: e.g. 3.16.b1, 3.17.b11. The rung field
# (threshold/typical/excellent) distinguishes these from the standards bullets
# that share the .bN shape; a skill bullet carries no rung.
SKILL_BULLET_RE = re.compile(r"^\d+\.\d+\.b\d+$")


# ---------------------------------------------------------------------------
# Ingest markdown parsing
# ---------------------------------------------------------------------------
def parse_ingest(md_path):
    """Return (front_matter, sections, raw) for an ingest markdown file.

    `sections` maps a section code (the first token of a 2-4 # heading, e.g.
    "S4", "SB3") to the list of YAML blocks parsed under that heading.
    """
    raw = open(md_path, encoding="utf-8").read()
    parts = raw.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{md_path}: no YAML front matter found")
    fm = yaml.safe_load(parts[1])

    sections = {}
    cur = None
    in_yaml = False
    buf = []
    heading_re = re.compile(r"^#{2,4}\s+(.*)$")
    for ln in raw.split("\n"):
        h = heading_re.match(ln)
        if h and not in_yaml:
            cur = h.group(1).strip()
            continue
        if ln.strip().startswith("```yaml"):
            in_yaml = True
            buf = []
            continue
        if in_yaml and ln.strip() == "```":
            in_yaml = False
            code = cur.split()[0] if cur else "?"
            try:
                parsed = yaml.safe_load("\n".join(buf))
            except yaml.YAMLError as e:
                parsed = {"_parse_error": str(e)}
            sections.setdefault(code, []).append(parsed)
            continue
        if in_yaml:
            buf.append(ln)
    return fm, sections, raw


def first(sections, code):
    """First YAML block under a section code, or None."""
    blocks = sections.get(code)
    return blocks[0] if blocks else None


def sb1_bullets(raw):
    """Distinctive-feature bullets under the prose SB1 heading.

    SB1 carries no YAML block (prose only), so it is read from the markdown
    directly: the bullets under the first `SB1` heading, up to the next
    heading. The trailing `(D1...)` provenance marker each bullet carries is
    stripped.
    """
    m = re.search(
        r"^#{2,4}\s+SB1\b.*?\n(.*?)(?=^#{2,4}\s)",
        raw,
        flags=re.S | re.M,
    )
    out = []
    if m:
        for b in re.findall(r"^- (.*)$", m.group(1), flags=re.M):
            out.append(re.sub(r"\s*\(D1[^)]*\)\.?$", "", b).strip())
    return out


# ---------------------------------------------------------------------------
# Field builders
# ---------------------------------------------------------------------------
def build_statements(sections):
    """S4 statements in full minus copyright fields, with S4a rewrites."""
    s4 = first(sections, "S4") or []
    s4a_block = first(sections, "S4a") or []
    s4a = {
        d["statement"]: d
        for d in s4a_block
        if isinstance(d, dict) and "statement" in d
    }
    statements = []
    for st in s4:
        if not isinstance(st, dict):
            continue
        entry = {k: v for k, v in st.items() if k not in COPYRIGHT_FIELDS}
        av = s4a.get(st.get("id"))
        if av:
            aud = {}
            for key in ("forPractitioner", "forBeneficiary"):
                v = av.get(key)
                if isinstance(v, dict) and v.get("text"):
                    aud[key] = {
                        kk: v.get(kk)
                        for kk in ("text", "rewrite", "force", "status")
                        if v.get(kk) is not None
                    }
            if aud:
                entry["audienceVersions"] = aud
        statements.append(entry)
    return statements


def build_skills(statements):
    """Graduate-skill digest, best-effort from the enumerated bullet outcomes.

    A skill bullet is an `outcome` statement with no rung whose id ends `.bN`
    (e.g. 3.16.b2). Split subject-specific vs transferable by `domain`:
    `generic-skill` -> transferable, everything else -> subject-specific. Each
    entry is the beneficiary-facing can-do rewrite.

    This reproduces the document's own skills lists where the ingest follows
    the enumerated-bullet convention (psychology: 15 + 11). Where it does not
    (some subjects number skills differently), the lists come back short or
    empty -- nothing is lost, since statements[] carries every statement's
    domain/rung/verbs/about for recovery by filter.
    """
    subject_specific, transferable = [], []
    for s in statements:
        sid = str(s.get("id", ""))
        tail = sid.split("/")[-1]
        if s.get("statementType") != "outcome":
            continue
        if s.get("rung") not in (None, "none"):
            continue
        if not SKILL_BULLET_RE.match(tail):
            continue
        ben = (s.get("audienceVersions", {}) or {}).get("forBeneficiary")
        if not (isinstance(ben, dict) and ben.get("text")):
            continue
        row = {"id": sid, "text": ben["text"]}
        if s.get("domain") == "generic-skill":
            transferable.append(row)
        else:
            subject_specific.append(row)
    return subject_specific, transferable


def build_pathway_mapping(adapt_map):
    """pathwayMapping + mapAgentInstructions from the adapt-map, or empty."""
    if not adapt_map:
        return {}, []
    pm = {}
    coverage = adapt_map.get("coverage", {}) or {}
    for pw, body in (adapt_map.get("pathways", {}) or {}).items():
        body = body or {}
        cov = coverage.get(pw)
        pm[pw] = {
            "coverage": cov if isinstance(cov, dict) else {"note": cov},
            "summary": body.get("summary") or {},
            "statements": body.get("statements") or [],
        }
    return pm, adapt_map.get("agentInstructions", []) or []


def build_tier_readings(card, statement_ids):
    """Per-tier readings from the subject-benchmark card, or None.

    Each populated card row (d3, e2, ...) becomes one reading carrying BOTH
    axes - our tier (from the row letter) and the indicative FHEQ level (from
    the grid) - plus the practice/knowledge/identity synthesis triad and the
    grounding statement ids. Rows are ordered introductory -> advanced. Returns
    (block, unresolved_ids): unresolved_ids are grounding ids not found in
    statement_ids (an integrity warning, surfaced in the run report).
    """
    if not card:
        return None, []
    rows_in = card.get("rows") or {}
    out_rows = []
    unresolved = []
    for key in ROW_ORDER:
        r = rows_in.get(key)
        if not isinstance(r, dict):
            continue
        ids = r.get("ids") or []
        for gid in ids:
            if gid not in statement_ids:
                unresolved.append((key, gid))
        out_rows.append({
            "rowId": key,
            "tier": ROW_TIER[key[0]],
            "fheqLevel": ROW_FHEQ[key],
            "practice": r.get("practice"),
            "knowledge": r.get("knowledge"),
            "identity": r.get("identity"),
            "groundingIds": ids,
        })
    if not out_rows:
        return None, unresolved
    block = {"rows": out_rows}
    if card.get("note"):
        block["note"] = card["note"]
    block["source"] = {
        "repo": "wkspc2614-adapt",
        "path": CARD_PATH_TMPL.format(id=card.get("slug", "")),
        "run": card.get("run"),
        "note": (
            "Subject-benchmark card readings: our own per-tier synthesis of "
            "the statements each row cites; no issuer text copied."
        ),
    }
    return block, unresolved


def subject_name(fm):
    """Human subject name from the ingest title, falling back to the label."""
    title = (fm.get("title") or "").strip()
    name = re.sub(
        r"^Subject Benchmark Statement(?:\s+for|\s*:)?\s*",
        "",
        title,
    ).strip()
    if name:
        return name
    subs = fm.get("subjects") or []
    if subs and isinstance(subs[0], dict) and subs[0].get("label"):
        return subs[0]["label"].title()
    return title or "(unknown)"


def subject_codes(fm):
    """scheme/code/label triples from the ingest front matter."""
    return [
        {"scheme": s["scheme"], "code": s["code"], "label": s["label"]}
        for s in (fm.get("subjects") or [])
        if isinstance(s, dict)
        and all(k in s for k in ("scheme", "code", "label"))
    ]


def headline_codes(codes):
    """Lightweight index codes: the first HECoS plus the CAH walk-up chain."""
    out = []
    seen_hecos = False
    for c in codes:
        if c["scheme"] == "hecos" and not seen_hecos:
            out.append(c)
            seen_hecos = True
        elif c["scheme"] == "cah":
            out.append(c)
    return out


# ---------------------------------------------------------------------------
# One subject
# ---------------------------------------------------------------------------
def build_subject(subject_id, args):
    """Build one subject's benchmark doc. Returns (doc, report)."""
    ingest_dir = os.path.join(
        args.ingest_root, f"{INGEST_PREFIX}{subject_id}{INGEST_SUFFIX}"
    )
    md_path = os.path.join(
        ingest_dir, f"{INGEST_PREFIX}{subject_id}{INGEST_SUFFIX}.md"
    )
    if not os.path.exists(md_path):
        raise FileNotFoundError(md_path)

    fm, sections, raw = parse_ingest(md_path)
    statements = build_statements(sections)
    subj_specific, transferable = build_skills(statements)
    sb1 = sb1_bullets(raw)

    adapt_map_path = os.path.join(
        args.adapt_map_root, f"{subject_id}.adapt-map.json"
    )
    adapt_map = None
    if os.path.exists(adapt_map_path):
        adapt_map = json.load(open(adapt_map_path, encoding="utf-8"))
    pathway_mapping, map_agent_instructions = build_pathway_mapping(adapt_map)

    card_path = os.path.join(args.card_root, f"{subject_id}.yaml")
    card = None
    if os.path.exists(card_path):
        card = yaml.safe_load(open(card_path, encoding="utf-8"))
    statement_ids = {s.get("id") for s in statements}
    tier_readings, unresolved_grounding = build_tier_readings(
        card, statement_ids
    )

    codes = subject_codes(fm)

    # Key order matches the hand-built reference: ingestId, ingestDoc,
    # adaptMap, licence.
    source = {
        "ingestId": fm.get("id"),
        "ingestDoc": {
            "repo": "wkspc2614-adapt",
            "path": INGEST_DOC_PATH_TMPL.format(id=subject_id),
            "note": (
                "QAA Subject Benchmark Statement, ingested. Issuer text is "
                "held, never copied; every statement here is our paraphrase "
                "or audience rewrite."
            ),
        },
    }
    if adapt_map is not None:
        source["adaptMap"] = {
            "repo": "wkspc2613-adapt2",
            "path": ADAPT_MAP_PATH_TMPL.format(id=subject_id),
            "note": (
                "Mapping of this benchmark to the 13 Adapt pathways; brought "
                "across into pathwayMapping below."
            ),
        }
    else:
        source["adaptMap"] = {
            "status": "pending",
            "expectedPath": ADAPT_MAP_PATH_TMPL.format(id=subject_id),
            "note": (
                "No adapt-map for this subject yet; pathwayMapping is empty "
                "until one is generated at expectedPath, after which this "
                "build picks it up on a re-run."
            ),
        }
    source["licence"] = LICENCE

    doc = {
        "subjectBenchmarkId": subject_id,
        "subject": {"name": subject_name(fm), "codes": codes},
        "issuer": fm.get("issuer"),
        "title": fm.get("title"),
        "edition": fm.get("edition"),
        "published": str(fm.get("published")),
        "status": fm.get("status"),
        "levelsCovered": fm.get("levelsCovered", []),
        "awardsCovered": fm.get("awardsCovered", []),
        "nations": fm.get("nations", []),
        "source": source,
        "identity": first(sections, "S1") or {},
        "purpose": first(sections, "S2") or {},
        "statedSubjects": (first(sections, "S2") or {}).get(
            "statedSubjects", []
        ),
        "structure": (first(sections, "S3") or {}).get("components", []),
        "frameworkAlignment": first(sections, "S5") or {},
        "tierReadings": tier_readings,
        "themes": first(sections, "S6") or [],
        "relations": first(sections, "S7") or [],
        "currency": first(sections, "S8") or {},
        "terminology": {
            "concepts": first(sections, "B1") or [],
            "terms": first(sections, "B2a") or [],
        },
        "digest": {
            "definition": sb1[0] if sb1 else None,
            "distinctiveFeatures": sb1,
            "themesInSubject": first(sections, "SB2") or [],
            "contentAndDelivery": first(sections, "SB3") or {},
            "standards": first(sections, "SB4") or {},
            "bodies": first(sections, "SB5") or [],
            "crossCuttingReferences": first(sections, "SB6") or {},
            "skills": {
                "subjectSpecific": subj_specific,
                "transferable": transferable,
            },
        },
        "statements": statements,
        "pathwayMapping": pathway_mapping,
        "mapAgentInstructions": map_agent_instructions,
    }

    report = {
        "id": subject_id,
        "name": doc["subject"]["name"],
        "codes": len(codes),
        "statements": len(statements),
        "withRewrites": sum(1 for s in statements if "audienceVersions" in s),
        "subjectSkills": len(subj_specific),
        "transferableSkills": len(transferable),
        "pathways": len(pathway_mapping),
        "hasMap": adapt_map is not None,
        "tierRows": len(tier_readings["rows"]) if tier_readings else 0,
        "hasCard": card is not None,
        "unresolvedGrounding": unresolved_grounding,
        "structureComps": len(doc["structure"]),
        "frameworkLevels": len(
            (doc["frameworkAlignment"] or {}).get("levels", [])
            if isinstance(doc["frameworkAlignment"], dict)
            else []
        ),
    }
    return doc, report


def discover_subjects(ingest_root):
    """All QAA benchmark subject ids under the ingest root, sorted."""
    out = []
    for name in sorted(os.listdir(ingest_root)):
        if name.startswith(INGEST_PREFIX) and name.endswith(INGEST_SUFFIX):
            out.append(name[len(INGEST_PREFIX) : -len(INGEST_SUFFIX)])
    return out


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def rebuild_index(out_dir, index_path):
    """Rebuild the collection index from every benchmark file present."""
    entries = []
    for name in sorted(os.listdir(out_dir)):
        if not name.endswith(".json"):
            continue
        d = json.load(open(os.path.join(out_dir, name), encoding="utf-8"))
        # Skip anything that is not a single-benchmark file (e.g. an index
        # written into the same directory).
        if "subjectBenchmarkId" not in d or "subject" not in d:
            continue
        entries.append(
            {
                "id": d["subjectBenchmarkId"],
                "subject": d["subject"]["name"],
                "issuer": d.get("issuer"),
                "edition": d.get("edition"),
                "codes": headline_codes(d["subject"]["codes"]),
                "file": (
                    f"catalogue/context/subject/benchmarks/"
                    f"{d['subjectBenchmarkId']}.json"
                ),
            }
        )
    index = {"subjectBenchmarksVersion": "1.0.0", "benchmarks": entries}
    write_json(index_path, index)
    return len(entries)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--subject", help="one subject id, e.g. psychology-2023")
    g.add_argument(
        "--all", action="store_true", help="build every discoverable subject"
    )
    ap.add_argument("--ingest-root", default=DEFAULT_INGEST_ROOT)
    ap.add_argument("--adapt-map-root", default=DEFAULT_ADAPT_MAP_ROOT)
    ap.add_argument("--card-root", default=DEFAULT_CARD_ROOT)
    ap.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    ap.add_argument("--index", default=DEFAULT_INDEX)
    ap.add_argument(
        "--no-index", action="store_true", help="do not rebuild the index"
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="parse and report; write nothing",
    )
    args = ap.parse_args()

    if not os.path.isdir(args.ingest_root):
        sys.exit(f"REFUSED: ingest root not found: {args.ingest_root}")

    if args.all:
        subjects = discover_subjects(args.ingest_root)
    else:
        subjects = [args.subject]

    if not args.dry_run:
        os.makedirs(args.out_dir, exist_ok=True)

    reports, failures = [], []
    for sid in subjects:
        try:
            doc, report = build_subject(sid, args)
        except FileNotFoundError as e:
            failures.append((sid, f"ingest not found: {e}"))
            continue
        except Exception as e:  # noqa: BLE001 - report, don't abort the run
            failures.append((sid, f"{type(e).__name__}: {e}"))
            continue
        out_path = os.path.join(args.out_dir, f"{sid}.json")
        if not args.dry_run:
            write_json(out_path, doc)
        reports.append((report, os.path.getsize(out_path) if (not args.dry_run and os.path.exists(out_path)) else None))

    # Run report
    print(f"{'subject':<40} {'stmts':>6} {'rw':>4} {'subjSk':>7} "
          f"{'tranSk':>7} {'paths':>6} {'tiers':>6} map")
    print("-" * 90)
    for report, _size in reports:
        flag = "yes" if report["hasMap"] else "NO MAP"
        tiers = report["tierRows"] if report["hasCard"] else "NO CARD"
        print(f"{report['id']:<40} {report['statements']:>6} "
              f"{report['withRewrites']:>4} {report['subjectSkills']:>7} "
              f"{report['transferableSkills']:>7} {report['pathways']:>6} "
              f"{str(tiers):>6} {flag}")
    print("-" * 90)
    built = len(reports)
    with_map = sum(1 for r, _ in reports if r["hasMap"])
    with_card = sum(1 for r, _ in reports if r["hasCard"])
    zero_skills = [r["id"] for r, _ in reports
                   if r["subjectSkills"] == 0 and r["transferableSkills"] == 0]
    unresolved = [(r["id"], r["unresolvedGrounding"]) for r, _ in reports
                  if r["unresolvedGrounding"]]
    print(f"built: {built} | with adapt-map: {with_map} | "
          f"no map: {built - with_map} | with tier card: {with_card} | "
          f"no card: {built - with_card}")
    if unresolved:
        print("UNRESOLVED grounding ids (not in statements[]):")
        for sid, pairs in unresolved:
            shown = ", ".join(f"{k}:{g}" for k, g in pairs[:6])
            print(f"  {sid}: {len(pairs)} -> {shown}")
    if zero_skills:
        print(f"zero skills digest (statements[] still complete): "
              f"{', '.join(zero_skills)}")
    if failures:
        print("FAILURES:")
        for sid, why in failures:
            print(f"  {sid}: {why}")

    if not args.dry_run and not args.no_index:
        n = rebuild_index(args.out_dir, args.index)
        print(f"index rebuilt: {n} entr{'y' if n == 1 else 'ies'} "
              f"-> {args.index}")

    if args.dry_run:
        print("DRY RUN: no files written.")

    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
