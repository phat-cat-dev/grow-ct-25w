#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-pathway-reference.py

Build a per-pathway authoring reference, concept-ordered so an agent reads it
top to bottom, aggregating the many per-pathway sources into one place:

  identity         - what the pathway is (core Part 0 + front matter + the
                     card plan's number/practice noun + catalogue placement)
  capabilities     - the nine cards (3 tiers x 3), each merging the card plan
                     (statement, knowledge kind, QF extracts, book quotes), the
                     core A10 competency (academic + professional framings,
                     theory ids), and the card vocabulary (verbs/terms/keywords)
  tierProgression  - all tier content together: core A11 levels (3-8, with the
                     metacognition ladder), the plan's tier statements + mastery
                     prose, the per-row practice/knowledge/identity readings,
                     and the FHEQ descriptor readings
  theorySpine      - the core A1 overview + the theory ids the pathway rests on
  crossCutting     - the plan's cross-cutting analysis, benchmark evidence
                     (readings + verbs-in-context), and framework readings
  gaps             - core open questions + the plan's review items
  provenance

Every tiered item carries BOTH axes (tier + FHEQ level), per the shared
cross-cutting store's tier model. Content is our own words; no issuer text.

v1 scope: the clean-YAML and core-YAML sources above. Two markdown-prose
sources fold in next (v2), both flagged null here:
  - the book->pathway source map (per-capability book pages/teaching/gaps)
  - the ADAPT consumer integration (voice band, scope/signpost routing)

Usage:
  python3 tools/build-pathway-reference.py --pathway understanding-learning-assessment-feedback
  python3 tools/build-pathway-reference.py --all [--dry-run]
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

OLD = "/home/user/wkspc2614-adapt"
THEMES = (
    f"{OLD}/source-kb/canon-adp/secondary-data/ingested/themes/pathways"
)
DEFAULT_CORE_ROOT = f"{THEMES}/pathways"
DEFAULT_PLAN_ROOT = f"{THEMES}/integrations/cards/plans"
DEFAULT_WIDE_ROOT = f"{THEMES}/integrations/cards/wide"
DEFAULT_VOCAB = f"{THEMES}/integrations/cards/ing-card-vocabulary.json"
DEFAULT_EAU_ROOT = f"{THEMES}/source-maps/excelling-at-university"
DEFAULT_ADAPT_ROOT = f"{THEMES}/integrations/adapt"
DEFAULT_CATALOGUE = "/home/user/wkspc2613-adapt2/catalogue/context/pathways.json"
DEFAULT_OUT_DIR = "/home/user/wkspc2613-adapt2/catalogue/context/pathway"

CORE_TMPL = "ingest-path-{slug}.md"
PLAN_TMPL = "{slug}.yaml"
EAU_TMPL = "ingest-path-{slug}-eau.md"
ADAPT_TMPL = "ingest-path-{slug}-adapt.md"

ROW_TIER = {"i": "introductory", "d": "intermediate", "e": "advanced"}
ROW_FHEQ = {
    "F": 3, "i1": 3, "i2": 4, "i3": 5, "d1": 4, "d2": 5, "d3": 6,
    "e1": 5, "e2": 6, "e3": 7, "L8": 8,
}
ROW_ORDER = ["F", "i1", "i2", "i3", "d1", "d2", "d3", "e1", "e2", "e3", "L8"]


def row_tier(r):
    if r == "F":
        return "foundation"
    if r == "L8":
        return "beyond"
    return ROW_TIER[r[0]]


# ---------------------------------------------------------------------------
# Core markdown parsing (front matter + fenced yaml per heading + prose)
# ---------------------------------------------------------------------------
def parse_core(md_path):
    raw = open(md_path, encoding="utf-8").read()
    fm = yaml.safe_load(raw.split("---", 2)[1])
    fenced = {}
    cur = None
    in_yaml = False
    buf = []
    hre = re.compile(r"^#{2,4}\s+(.*)$")
    for ln in raw.split("\n"):
        h = hre.match(ln)
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
                fenced.setdefault(code, []).append(yaml.safe_load("\n".join(buf)))
            except yaml.YAMLError:
                pass
            continue
        if in_yaml:
            buf.append(ln)
    return fm, fenced, raw


def prose_under(raw, heading_re):
    """Prose text under the first heading matching heading_re, to next heading,
    with HTML comments and blank padding stripped."""
    m = re.search(
        rf"^#{{2,4}}\s+{heading_re}.*?\n(.*?)(?=^#{{2,4}}\s)",
        raw, flags=re.S | re.M,
    )
    if not m:
        return None
    text = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # drop any fenced block
    text = "\n".join(l.rstrip() for l in text.splitlines())
    return text.strip() or None


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------
def build_identity(fm, raw, plan, cat_entry):
    return {
        "id": fm.get("id"),
        "slug": None,  # set by caller
        "title": fm.get("title"),
        "aliases": fm.get("aliases", []),
        "practices": fm.get("practices", []),
        "pathwayNumber": (cat_entry or {}).get("number") or plan.get("pathwayNo"),
        "chapters": (cat_entry or {}).get("chapters"),
        "practiceNoun": plan.get("practiceNoun"),
        "agentDefinition": prose_under(raw, r"0\.1\s+Agent definition"),
        "summary": prose_under(raw, r"0\.2\s+Summary"),
        "status": fm.get("status"),
        "catalogueEntry": cat_entry,
    }


def build_capabilities(plan, a10, vocab_by_id):
    """Merge card plan cards + core A10 competencies + vocabulary, by id."""
    comp_by_id = {}
    if a10:
        for c in (a10.get("pathway", {}) or {}).get("competencies", []) or []:
            comp_by_id[c.get("id")] = c
    out = []
    for card in plan.get("cards", []) or []:
        row = card.get("new")
        cid = card.get("old")
        comp = comp_by_id.get(cid, {})
        voc = vocab_by_id.get(cid, {})
        out.append({
            "rowId": row,
            "capabilityId": cid,
            "tier": row_tier(row) if row else None,
            "fheqLevel": ROW_FHEQ.get(row),
            "statement": card.get("short"),
            "knowledgeKind": card.get("knowledge"),
            "qf": card.get("qf", []),
            "book": card.get("book", []),
            "competency": {
                "academicStatement": comp.get("statement"),
                "verbs": comp.get("verbs", []),
                "theory": comp.get("theory", []),
                "process": comp.get("process", []),
                "professional": comp.get("professional", []),
            } if comp else None,
            "vocabulary": {
                "verbs": voc.get("verbs", []),
                "measures": voc.get("measures", []),
                "terms": voc.get("terms", []),
                "keywords": voc.get("keywords", []),
                "bookTopics": voc.get("bookTopics", []),
                "benchmarkHits": voc.get("benchmarkHits"),
            } if voc else None,
        })
    return out


def build_tier_progression(plan, a11, readings, fheq):
    levels = (a11 or {}).get("progression", {}).get("levels", []) if a11 else []
    ladder = []
    for r in ROW_ORDER:
        triad = (readings or {}).get(r)
        if not triad:
            continue
        ladder.append({
            "rowId": r, "tier": row_tier(r), "fheqLevel": ROW_FHEQ[r],
            "practice": triad[0] if len(triad) > 0 else None,
            "knowledge": triad[1] if len(triad) > 1 else None,
            "identity": triad[2] if len(triad) > 2 else None,
        })
    framework = []
    for r in ROW_ORDER:
        rows = (fheq or {}).get(r)
        if not rows:
            continue
        entry = {"rowId": r, "tier": row_tier(r), "fheqLevel": ROW_FHEQ[r]}
        for axis in ("practice", "knowledge", "identity"):
            entry[axis] = rows.get(axis, []) if isinstance(rows, dict) else []
        framework.append(entry)
    return {
        "levels": levels,
        "tierStatements": plan.get("tierStatements", []),
        "masteryNote": plan.get("mastery"),
        "ladderReadings": ladder,
        "frameworkReadings": framework,
    }


def build_theory_spine(raw, a10, a11):
    theories = set()
    if a10:
        for c in (a10.get("pathway", {}) or {}).get("competencies", []) or []:
            for t in c.get("theory", []) or []:
                if isinstance(t, str):
                    theories.add(t)
    return {
        "overview": prose_under(raw, r"A1\s+Overview"),
        "corePrinciples": prose_under(raw, r"A2\s+Core principles"),
        "selection": prose_under(raw, r"A8\s+Selection"),
        "theories": sorted(theories),
    }


def build_cross_cutting(plan):
    readings = []
    vic = plan.get("vic", {}) or {}
    for sid, kind in (plan.get("readings", {}) or {}).items():
        v = vic.get(sid, {})
        readings.append({
            "benchmarkId": sid,
            "kind": kind,
            "verbs": v.get("verbs", []),
            "relation": v.get("relation"),
        })
    return {
        "analysis": plan.get("across", []),
        "benchmarkReadings": readings,
        "benchmarkReadingsSummary": plan.get("vicSummary"),
        "frameworkReadings": {
            "intro": plan.get("qfIntro"),
            "items": plan.get("qf", []),
            "notes": plan.get("qfAdd"),
        },
    }


def build_gaps(raw, plan):
    return {
        "coreOpenQuestions": prose_under(raw, r"Part E\s+Gaps and questions")
        or prose_under(raw, r"E\b"),
        "reviewItems": plan.get("review", []),
        "differsFromTierMapping": plan.get("differ"),
    }


# ---------------------------------------------------------------------------
# Markdown table / section helpers (for the eau + adapt integration docs, v2)
# ---------------------------------------------------------------------------
def md_sections(raw):
    """Map each '## <heading>' line to its body text (### subheadings ignored)."""
    out = {}
    parts = re.split(r"^##\s+(.*)$", raw, flags=re.M)
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def md_table(text):
    """Parse the first pipe table in text -> list of row dicts keyed by header."""
    rows = [l for l in text.splitlines() if l.strip().startswith("|")]
    if len(rows) < 2:
        return []
    headers = _cells(rows[0])
    out = []
    for line in rows[2:]:  # skip header row + separator row
        c = _cells(line)
        out.append({headers[i]: (c[i] if i < len(c) else "")
                    for i in range(len(headers))})
    return out


def _clean(v):
    """Empty / placeholder dash -> None."""
    if v is None:
        return None
    v = str(v).strip()
    return None if v in ("", "-", "--") else v


def numbered_points(text):
    """'N. text' items; splits a bold lead 'N. **Label.** rest' into label+text."""
    out = []
    for m in re.finditer(r"^\d+\.\s+(.*)$", text, flags=re.M):
        body = m.group(1).strip()
        lab = re.match(r"\*\*(.+?)\.?\*\*\s*(.*)$", body)
        if lab:
            out.append({"label": lab.group(1).strip(),
                        "text": lab.group(2).strip()})
        else:
            out.append({"label": None, "text": body})
    return out


def code_block_lines(text):
    m = re.search(r"```\n?(.*?)```", text, flags=re.S)
    return [l.strip() for l in m.group(1).splitlines() if l.strip()] if m else []


def build_book_grounding(eau_path):
    """Per-capability book grounding from the book->pathway source map."""
    if not os.path.exists(eau_path):
        return None, {}
    raw = open(eau_path, encoding="utf-8").read()
    secs = md_sections(raw)
    chapters = None
    m = re.search(r"\*\*Chapters:\*\*\s*(.+)", raw)
    if m:
        chapters = m.group(1).strip()
    sections, cap_rows, not_covered = [], [], None
    for head, body in secs.items():
        if head.startswith("1."):
            for r in md_table(body):
                sections.append({
                    "pages": _clean(r.get("Pages")),
                    "teaches": _clean(r.get("What the guide teaches there")
                                      or r.get("What the guide teaches")),
                })
        elif head.startswith("2."):
            for r in md_table(body):
                capcell = r.get("Capability", "")
                cid = re.search(r"`([^`]+)`", capcell)
                tier = re.search(r"\((\w+)\)", capcell)
                cap_rows.append({
                    "capabilityId": cid.group(1) if cid else None,
                    "tierNote": tier.group(1) if tier else None,
                    "pages": _clean(r.get("Pages")),
                    "teaches": _clean(r.get("What the guide teaches")),
                    "workedExamples": _clean(r.get("Worked examples and tasks")),
                    "notes": _clean(r.get("Notes and gaps")),
                })
        elif head.startswith("3."):
            txt = re.sub(r"<!--.*?-->", "", body, flags=re.S)
            not_covered = re.sub(r"\s+", " ", txt).strip() or None
    block = {
        "chapters": chapters,
        "sections": sections,
        "byCapability": cap_rows,
        "notCovered": not_covered,
    }
    by_id = {r["capabilityId"]: r for r in cap_rows if r["capabilityId"]}
    return block, by_id


def build_adapt_integration(adapt_path):
    """ADAPT consumer view: placement, usage (voice band + routing), open points."""
    if not os.path.exists(adapt_path):
        return None
    raw = open(adapt_path, encoding="utf-8").read()
    secs = md_sections(raw)
    placement, usage, open_points, patterns = [], [], [], []
    for head, body in secs.items():
        if head.startswith("1."):
            for r in md_table(body):
                placement.append({
                    "what": _clean(r.get("What")),
                    "where": _clean(r.get("Where")),
                    "state": _clean(r.get("State")),
                })
        elif head.startswith("2."):
            usage = numbered_points(body)
        elif head.startswith("3."):
            open_points = [p["text"] for p in numbered_points(body)]
        elif head.startswith("4."):
            patterns = code_block_lines(body)

    def find(labels):
        for u in usage:
            if u["label"] and any(k in u["label"].lower() for k in labels):
                return u["text"]
        return None

    return {
        "placement": placement,
        "usage": usage,
        "voiceBand": find(["voice band"]),
        "routing": find(["scope and signpost", "signpost", "cross-link",
                         "scope"]),
        "openPoints": open_points,
        "benchmarkPatterns": patterns,
    }


def build_pathway(slug, args, catalogue, vocab_cards):
    core_path = os.path.join(args.core_root, CORE_TMPL.format(slug=slug))
    plan_path = os.path.join(args.plan_root, PLAN_TMPL.format(slug=slug))
    for p in (core_path, plan_path):
        if not os.path.exists(p):
            raise FileNotFoundError(p)
    fm, fenced, raw = parse_core(core_path)
    plan = yaml.safe_load(open(plan_path, encoding="utf-8"))
    a10 = (fenced.get("A10") or [None])[0]
    a11 = (fenced.get("A11") or [None])[0]

    readings_all = yaml.safe_load(
        open(os.path.join(args.wide_root, "pathway-readings.yaml"),
             encoding="utf-8")
    )
    fheq_all = yaml.safe_load(
        open(os.path.join(args.wide_root, "fheq-readings.yaml"),
             encoding="utf-8")
    )
    readings = (readings_all or {}).get(slug)
    fheq = (fheq_all or {}).get(slug)

    vocab_by_id = {c["id"]: c for c in vocab_cards if c.get("pathway") == slug}
    cat_entry = next(
        (p for p in (catalogue.get("pathways", []) or [])
         if p.get("id") == slug), None
    )

    eau_path = os.path.join(args.eau_root, EAU_TMPL.format(slug=slug))
    adapt_path = os.path.join(args.adapt_root, ADAPT_TMPL.format(slug=slug))
    book_grounding, book_by_id = build_book_grounding(eau_path)
    adapt_integration = build_adapt_integration(adapt_path)

    identity = build_identity(fm, raw, plan, cat_entry)
    identity["slug"] = slug
    capabilities = build_capabilities(plan, a10, vocab_by_id)
    for cap in capabilities:
        cap["bookGrounding"] = book_by_id.get(cap["capabilityId"])
    doc = {
        "pathwayReferenceId": slug,
        "identity": identity,
        "capabilities": capabilities,
        "tierProgression": build_tier_progression(plan, a11, readings, fheq),
        "theorySpine": build_theory_spine(raw, a10, a11),
        "crossCutting": build_cross_cutting(plan),
        "gaps": build_gaps(raw, plan),
        "adaptIntegration": adapt_integration,
        "bookGrounding": book_grounding,
        "source": {
            "repo": "wkspc2614-adapt",
            "core": f"...themes/pathways/pathways/{CORE_TMPL.format(slug=slug)}",
            "plan": f"...integrations/cards/plans/{PLAN_TMPL.format(slug=slug)}",
            "wide": "...integrations/cards/wide/{pathway-readings,fheq-readings}.yaml",
            "vocab": "...integrations/cards/ing-card-vocabulary.json",
            "eau": f"...source-maps/excelling-at-university/{EAU_TMPL.format(slug=slug)}",
            "adapt": f"...integrations/adapt/{ADAPT_TMPL.format(slug=slug)}",
            "note": (
                "Our own words; no issuer or book text beyond short checked "
                "quotes. bookGrounding is the book->pathway source map; "
                "adaptIntegration is the ADAPT consumer view (voice band + "
                "scope/signpost routing)."
            ),
        },
    }
    report = {
        "slug": slug,
        "capabilities": len(doc["capabilities"]),
        "a11Levels": len(doc["tierProgression"]["levels"]),
        "ladderRows": len(doc["tierProgression"]["ladderReadings"]),
        "fheqRows": len(doc["tierProgression"]["frameworkReadings"]),
        "benchmarkReadings": len(doc["crossCutting"]["benchmarkReadings"]),
        "theories": len(doc["theorySpine"]["theories"]),
        "bookCaps": len(book_by_id),
        "hasAdapt": adapt_integration is not None,
        "inCatalogue": cat_entry is not None,
    }
    return doc, report


def discover(plan_root):
    return sorted(
        f[:-5] for f in os.listdir(plan_root) if f.endswith(".yaml")
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pathway")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--core-root", default=DEFAULT_CORE_ROOT)
    ap.add_argument("--plan-root", default=DEFAULT_PLAN_ROOT)
    ap.add_argument("--wide-root", default=DEFAULT_WIDE_ROOT)
    ap.add_argument("--vocab", default=DEFAULT_VOCAB)
    ap.add_argument("--eau-root", default=DEFAULT_EAU_ROOT)
    ap.add_argument("--adapt-root", default=DEFAULT_ADAPT_ROOT)
    ap.add_argument("--catalogue", default=DEFAULT_CATALOGUE)
    ap.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    catalogue = json.load(open(args.catalogue, encoding="utf-8"))
    vocab_cards = json.load(open(args.vocab, encoding="utf-8")).get("cards", [])
    slugs = [args.pathway] if args.pathway else discover(args.plan_root)
    if not args.dry_run:
        os.makedirs(args.out_dir, exist_ok=True)

    reports, failures = [], []
    for slug in slugs:
        try:
            doc, report = build_pathway(slug, args, catalogue, vocab_cards)
        except Exception as e:  # noqa: BLE001
            failures.append((slug, f"{type(e).__name__}: {e}"))
            continue
        if not args.dry_run:
            with open(os.path.join(args.out_dir, f"{slug}.json"), "w",
                      encoding="utf-8") as f:
                json.dump(doc, f, indent=2, ensure_ascii=False)
        reports.append(report)

    print(f"{'pathway':<42} {'caps':>4} {'A11':>4} {'ladR':>5} {'fheqR':>6} "
          f"{'bmR':>4} {'thy':>4} {'book':>4} {'adapt':>5} cat")
    print("-" * 90)
    for r in reports:
        print(f"{r['slug']:<42} {r['capabilities']:>4} {r['a11Levels']:>4} "
              f"{r['ladderRows']:>5} {r['fheqRows']:>6} "
              f"{r['benchmarkReadings']:>4} {r['theories']:>4} "
              f"{r['bookCaps']:>4} {'yes' if r['hasAdapt'] else 'no':>5} "
              f"{'yes' if r['inCatalogue'] else 'NO'}")
    print("-" * 80)
    not_in_cat = [r["slug"] for r in reports if not r["inCatalogue"]]
    print(f"built: {len(reports)} | not in catalogue: "
          f"{', '.join(not_in_cat) or 'none'}")
    if failures:
        print("FAILURES:")
        for slug, why in failures:
            print(f"  {slug}: {why}")
    if args.dry_run:
        print("DRY RUN: no files written.")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
