#!/usr/bin/env python3
"""check-pathway-tier-readings.py - validate
catalogue/context/pathway-tier-readings/<pathway>.json: the universal
benchmark's nine tier statement formulas, re-filled with each pathway's own
capability vocabulary and voice band (13 files, 9 statements each, 117
total). Built by tools/build-pathway-tier-readings.py.

All helper logic here (term_head/term_number/term_rejected/is_process_noun,
the section 16 band parser, the voice-band anchor parser, inflect()) is
duplicated from the builder, not imported: mirrors
tools/check-statement-formulas.py's own duplicated verb_bands() - a checker
that imports the thing it checks cannot catch that thing being wrong.

Checks, per file:
  - raw text, before parsing: no em dash, en dash, smart quote or tab; no
    "academic skills"; no ISO date/timestamp anywhere; valid UTF-8 JSON
  - shape: top-level keys exactly [pathway, status, note, tierReadings,
    source] in that order; pathway == filename stem == a real pathway;
    status == "generated"; note contains the script name, "deterministic",
    the known-limitation sentence and the override sentence, by substring;
    every source.inputs path exists
  - coverage: 3 tiers in order; universalRowId + fheqLevel match the
    universal row; 3 statements per tier keyed [practice, knowledge,
    identity] in order; capabilities[] == that tier's 3 own capability refs
    in rowId order; 9 statements per file, pairwise distinct
  - fidelity: template.format(**fill) == statement; universalTemplate and
    universalStatement byte-identical to the universal's; reversing
    subjectSubstitution on template yields universalTemplate exactly;
    closure both ways (template braces == fill keys == slotProvenance
    slots, in template order); roles match the universal's declared roles
    and are in the closed 8-role set; universalOutcomeRefs == the
    formula's outcome ids in order
  - policy honoured: every universalSourceFill slot value byte-identical
    to the universal sourceFill; every pitch role (condition, scope,
    qualifier, audience, stance) is universalSourceFill; <= 2
    capabilityVocabulary object fills per statement; identity object slots
    carry agentInstructionOverridden; termsUsed/capabilitiesUsed/
    pathwaySpecific exactly derivable from slotProvenance
  - verbs: section 16 parsed live (empty parse is a FAIL); verbBand ==
    the anchor parsed live from pathway-tier-mapping.md for this pathway's
    pathwayNumber; the three anchor bands are three consecutive section 16
    bands ascending; every lemma in BANDS[verbBand]; value ==
    independently re-run inflect(lemma, form); no banned vague verb in any
    verb slot; third-cap only where the slot is sentence-initial
  - terms: every term verbatim in the named capability's vocabulary.terms
    (tier matches); no term equal to the pathway's own label
    (self-referential); no term repeated within one statement; termNumber
    re-derived; the required grammatical number (where the template's own
    agreement demands one) is respected; the determiner context is
    re-derived from the template text immediately before the slot and the
    value's own "the " prefix follows from it; a slot sitting in "X of
    <label>" never takes a term containing " of "
  - tier climb: tier-discriminating pitch substrings present/absent per
    tier, so the hierarchy cannot collapse
  - surface quality: ends in exactly one full stop; no double space, no
    space before punctuation, no stray brace/bracket, initial capital, no
    "the the"/"a a"/"to to"/"and and"; word count within +-40% of the
    universal statement; no -ize/-ization (British English)
  - printed counts, not asserted: statements checked, object fills,
    pathwaySpecific:false count, termClass:fallback-any count,
    labelSource:slug count (expect 1, reflective-practice)

Run from the repo root:
    python3 tools/check-pathway-tier-readings.py                  # all 13
    python3 tools/check-pathway-tier-readings.py academic-writing  # one or more
"""
import glob, json, os, re, sys
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers as pt

REPO_ROOT = pt.REPO_ROOT
OUT_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'pathway-tier-readings')
UNIVERSAL_PATH = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject',
                               'benchmarks', 'universal-reference.json')
VOICE_SPEC = os.path.join(REPO_ROOT, 'reference', 'excelling-voice-specification.md')
TIER_MAPPING = os.path.join(REPO_ROOT, 'docs', 'curriculum', 'pathway-tier-mapping.md')
BUILD_SCRIPT = 'tools/build-pathway-tier-readings.py'

FIELDS = ('practice', 'knowledge', 'identity')
TIERS = pt.TIERS
TOP_KEYS = ['pathway', 'status', 'note', 'tierReadings', 'source']
ROLES = {'verb', 'object', 'condition', 'field_content', 'scope', 'qualifier', 'audience', 'stance'}
PITCH_ROLES = {'condition', 'scope', 'qualifier', 'audience', 'stance'}
BANNED_VAGUE = {'understand', 'know', 'appreciate', 'be aware of', 'knows', 'understands', 'appreciates'}
MAX_OBJECT_FILLS = 2
RID_OF_TIER = {'introductory': 'u-intro', 'intermediate': 'u-int', 'advanced': 'u-adv'}

NOTE_SUBSTRINGS = (
    BUILD_SCRIPT,
    'deterministic',
    'the fill is grammatical by construction but not semantically curated',
    "overriding the universal formula's own agentInstruction guidance",
)

TIER_PITCH = {
    'introductory': {'must': ('with guidance', 'familiar, well-defined'),
                      'must_not': ('independently', 'originality', 'reflexive')},
    'intermediate': {'must': ('supervised', 'increasingly independently'), 'must_not': ()},
    'advanced': {'must': ('critically', 'with some originality', 'A reflexive practitioner'), 'must_not': ()},
}

# ---------------------------------------------------------------------------
# Duplicated from tools/build-pathway-tier-readings.py by design (see
# module docstring). ---------------------------------------------------------
_HEAD_PREPOSITIONS = (' of ', ' with ', ' for ', ' to ', ' from ', ' on ', ' in ')
_SINGULAR_S_EXCEPTIONS = {'analysis', 'synthesis', 'fairness', 'stress', 'ethics'}
_PROCESS_NOUN_HINTS = ('cycle', 'process', 'enquiry', 'inquiry', 'method', 'approach',
                        'procedure', 'practice', 'strategy', 'technique', 'workflow')
_DET_BEFORE = re.compile(r"(?:the|its|their|a|an|'s)(?:\s+own)?\s*$")


def term_head(term):
    best = term
    for p in _HEAD_PREPOSITIONS:
        if p in best:
            best = best.split(p, 1)[0].strip()
    return best


def term_number(term):
    head = term_head(term)
    parts = head.split()
    last = parts[-1] if parts else head
    if last[:1].isupper():
        return 'singular'
    bare = last.lower()
    if bare in _SINGULAR_S_EXCEPTIONS:
        return 'singular'
    return 'plural' if bare.endswith('s') else 'singular'


def term_rejected(term):
    head = term_head(term)
    parts = head.split()
    if not parts:
        return True
    if len(parts) == 1 and parts[0][:1].isupper():
        return True
    if parts[0].lower() == 'own':
        return True
    return False


def is_process_noun(term):
    head = term_head(term).lower()
    return any(h in head for h in _PROCESS_NOUN_HINTS)


def _third_person(lemma):
    parts = lemma.split()
    head = parts[-1]
    if head.endswith(('s', 'x', 'z', 'sh', 'ch')):
        infl = head + 'es'
    elif len(head) > 1 and head[-1] == 'y' and head[-2].lower() not in 'aeiou':
        infl = head[:-1] + 'ies'
    else:
        infl = head + 's'
    return ' '.join(parts[:-1] + [infl])


def inflect(lemma, form):
    if form == 'bare':
        return lemma
    if form == 'third':
        return _third_person(lemma)
    if form == 'third-cap':
        v = _third_person(lemma)
        return v[0].upper() + v[1:]
    return None


def verb_bands():
    bands = {}
    for line in open(VOICE_SPEC, encoding='utf-8'):
        m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|.*Outcome verbs:\s*([^|]+?)\.?\s*\|\s*$', line)
        if m:
            bands[m.group(1)] = [v.strip() for v in m.group(2).split(',') if v.strip()]
    return bands


BANDS = verb_bands()
BAND_ORDER = ('Foundation', 'Beginner', 'Intermediate', 'Advanced', 'Masters', 'Doctoral')

_ANCHOR_RE = re.compile(
    r'Introductory\s*\u2192\s*\xa7?16\s*(\w+),\s*'
    r'Intermediate\s*\u2192\s*\xa7?16\s*(\w+),\s*'
    r'Advanced\s*\u2192\s*\xa7?16\s*(\w+)')
_PATHWAY_HEADER_RE = re.compile(r'^##\s*Pathway\s+(\d+)\s*\u2014')


def voice_band_anchors():
    text = open(TIER_MAPPING, encoding='utf-8').read()
    anchors = {}
    current = None
    for line in text.split('\n'):
        m = _PATHWAY_HEADER_RE.match(line)
        if m:
            current = int(m.group(1))
            continue
        if current is not None and '**Voice-band anchor:**' in line:
            m2 = _ANCHOR_RE.search(line)
            if m2:
                anchors[current] = (m2.group(1), m2.group(2), m2.group(3))
            current = None
    return anchors


# Grammatical-number REQUIREMENT per object slot: independently declared
# here from the template's own verb/pronoun agreement, not imported from
# the builder's FILLABLE table (the two must independently agree).
REQUIRED_NUMBER = {
    ('u-intro', 'knowledge', 'object_1'): 'plural',
    ('u-int', 'identity', 'object_2'): 'plural',
    ('u-adv', 'knowledge', 'object_4'): 'singular',
    ('u-adv', 'identity', 'object_1'): 'plural',
}


def words(s):
    return len(re.findall(r"[A-Za-z0-9']+", s or ''))


def load_universal():
    return json.load(open(UNIVERSAL_PATH, encoding='utf-8'))


def universal_row(universal, rid):
    return next(r for r in universal['tierReadings']['rows'] if r['rowId'] == rid)


def check(pid, universal, anchors):
    errs = []
    counts = {'statements': 0, 'object_fills': 0, 'nonspecific': 0, 'fallback_any': 0, 'slug_label': 0}
    path = os.path.join(OUT_DIR, pid + '.json')
    if not os.path.exists(path):
        return ['missing ' + os.path.relpath(path, REPO_ROOT)], counts
    raw = open(path, encoding='utf-8').read()

    # --- raw text, before parsing --------------------------------------
    if '\u2014' in raw:
        errs.append('em dash present')
    if '\u2013' in raw:
        errs.append('en dash present')
    if re.search(r'[\u2018\u2019\u201c\u201d]', raw):
        errs.append('smart quote present')
    if '\t' in raw:
        errs.append('tab present')
    if re.search(r'academic skills', raw, re.I):
        errs.append('"academic skills" present')
    if re.search(r'\b\d{4}-\d{2}-\d{2}\b', raw):
        errs.append('ISO date / timestamp present (determinism requires none)')
    try:
        doc = json.loads(raw, object_pairs_hook=OrderedDict)
    except Exception as e:
        errs.append('invalid JSON: %s' % e)
        return errs, counts

    # --- shape -----------------------------------------------------------
    top_keys = list(doc.keys())
    if top_keys != TOP_KEYS:
        errs.append('top-level keys %s != %s' % (top_keys, TOP_KEYS))
    if doc.get('pathway') != pid:
        errs.append('pathway field %r != filename stem %r' % (doc.get('pathway'), pid))
    if not os.path.exists(os.path.join(pt.PATHWAY_DIR, pid + '.json')):
        errs.append('pathway %r is not a real pathway' % pid)
    if doc.get('status') != 'generated':
        errs.append('status %r != "generated"' % doc.get('status'))
    note = doc.get('note') or ''
    for sub in NOTE_SUBSTRINGS:
        if sub not in note:
            errs.append('note missing required substring: %r' % sub)
    source = doc.get('source') or {}
    if source.get('script') != BUILD_SCRIPT:
        errs.append('source.script %r != %r' % (source.get('script'), BUILD_SCRIPT))
    for inp in source.get('inputs') or []:
        fp = inp.split(' (', 1)[0].strip()
        if not os.path.exists(os.path.join(REPO_ROOT, fp)):
            errs.append('source.inputs path does not exist: %r' % fp)

    # --- ground truth, independent of the builder -----------------------
    pdoc = json.load(open(os.path.join(pt.PATHWAY_DIR, pid + '.json'), encoding='utf-8'))
    pathway_number = (pdoc.get('identity') or {}).get('pathwayNumber')
    practice_noun = (pdoc.get('identity') or {}).get('practiceNoun')
    if practice_noun:
        label, label_source_expect = practice_noun, 'identity.practiceNoun'
    else:
        label, label_source_expect = pid.replace('-', ' '), 'slug'
        counts['slug_label'] += 1

    caps_by_tier, cap_by_ref = {}, {}
    for c in pdoc.get('capabilities') or []:
        ref = pt.cap_ref(c, pid)
        cap_by_ref[ref] = c
        caps_by_tier.setdefault(c.get('tier'), []).append(c)

    band_anchor = anchors.get(pathway_number)
    if band_anchor is None:
        errs.append('pathwayNumber %r has no parsed voice-band anchor' % pathway_number)
    else:
        idxs = [BAND_ORDER.index(b) for b in band_anchor if b in BAND_ORDER]
        if len(idxs) != 3 or idxs[1] != idxs[0] + 1 or idxs[2] != idxs[1] + 1:
            errs.append('voice-band anchor %r is not three consecutive section-16 bands ascending' % (band_anchor,))

    # --- coverage: tiers ---------------------------------------------------
    trs = doc.get('tierReadings') or []
    if [t.get('tier') for t in trs] != list(TIERS):
        errs.append('tierReadings tiers %s != %s' % ([t.get('tier') for t in trs], list(TIERS)))

    all_statement_texts = []

    for tier_idx, tr in enumerate(trs):
        tier = tr.get('tier')
        rid = RID_OF_TIER.get(tier)
        if rid is None:
            errs.append('unknown tier %r' % tier)
            continue
        row = universal_row(universal, rid)
        if tr.get('universalRowId') != rid:
            errs.append('%s: universalRowId %r != %r' % (tier, tr.get('universalRowId'), rid))
        if tr.get('fheqLevel') != row.get('fheqLevel'):
            errs.append('%s: fheqLevel %r != universal %r' % (tier, tr.get('fheqLevel'), row.get('fheqLevel')))

        verb_band = tr.get('verbBand')
        if band_anchor and verb_band != band_anchor[tier_idx]:
            errs.append('%s: verbBand %r != anchor %r' % (tier, verb_band, band_anchor[tier_idx]))
        if verb_band not in BANDS:
            errs.append('%s: verbBand %r has no parsed section-16 options' % (tier, verb_band))

        tier_caps = sorted(caps_by_tier.get(tier) or [], key=lambda c: c.get('rowId') or '')
        expect_refs = [pt.cap_ref(c, pid) for c in tier_caps]
        if tr.get('capabilities') != expect_refs:
            errs.append('%s: capabilities %s != expected %s' % (tier, tr.get('capabilities'), expect_refs))

        statements = tr.get('statements') or {}
        if list(statements.keys()) != list(FIELDS):
            errs.append('%s: statement fields %s != %s' % (tier, list(statements.keys()), list(FIELDS)))

        tier_statement_texts = []
        for field in FIELDS:
            s = statements.get(field)
            if s is None:
                errs.append('%s/%s: missing statement' % (tier, field))
                continue
            counts['statements'] += 1
            lbl = '%s/%s/%s' % (pid, tier, field)
            f = row['formulas'][field]
            sf = f.get('sourceFill') or {}

            if s.get('universalTemplate') != f.get('template'):
                errs.append('%s: universalTemplate != universal template' % lbl)
            if s.get('universalStatement') != row.get(field):
                errs.append('%s: universalStatement != universal live statement' % lbl)

            template = s.get('template', '')
            fill = s.get('fill') or {}
            try:
                rebuilt = template.format(**fill)
            except Exception as e:
                rebuilt = None
                errs.append('%s: template.format(**fill) raised %s' % (lbl, e))
            if rebuilt is not None and rebuilt != s.get('statement'):
                errs.append('%s: rebuilt statement != s.statement' % lbl)

            subst = s.get('subjectSubstitution')
            if subst:
                subst_from, subst_to = subst.get('from'), subst.get('to')
                if subst_to not in template:
                    errs.append('%s: subjectSubstitution.to %r not found in template' % (lbl, subst_to))
                else:
                    reversed_tmpl = template.replace(subst_to, subst_from, 1)
                    if reversed_tmpl != f.get('template'):
                        errs.append('%s: reversing subjectSubstitution != universalTemplate' % lbl)
                if subst.get('label') != label:
                    errs.append('%s: subjectSubstitution.label %r != pathway label %r' % (lbl, subst.get('label'), label))
                if subst.get('labelSource') != label_source_expect:
                    errs.append('%s: subjectSubstitution.labelSource %r != expected %r'
                                % (lbl, subst.get('labelSource'), label_source_expect))
            elif template != f.get('template'):
                errs.append('%s: no subjectSubstitution but template != universalTemplate' % lbl)

            used = re.findall(r'\{(\w+)\}', template)
            prov = s.get('slotProvenance') or []
            prov_keys = [p.get('slot') for p in prov]
            if used != prov_keys:
                errs.append('%s: slotProvenance order %s != template brace order %s' % (lbl, prov_keys, used))
            if set(fill.keys()) != set(used):
                errs.append('%s: fill keys %s != template braces %s' % (lbl, sorted(fill), sorted(set(used))))

            universal_slots_by_key = {sl['key']: sl for sl in f.get('slots') or []}
            outcome_refs_expect = [oc['id'] for oc in f.get('outcomes') or []]
            if s.get('universalOutcomeRefs') != outcome_refs_expect:
                errs.append('%s: universalOutcomeRefs != expected %s' % (lbl, outcome_refs_expect))

            statement_terms = []
            for p in prov:
                key, role, frm = p.get('slot'), p.get('role'), p.get('from')
                usl = universal_slots_by_key.get(key)
                if usl is None:
                    errs.append('%s/%s: no such slot in universal formula' % (lbl, key))
                    continue
                if role != usl.get('role'):
                    errs.append('%s/%s: role %r != universal role %r' % (lbl, key, role, usl.get('role')))
                if role not in ROLES:
                    errs.append('%s/%s: role %r not in closed role set' % (lbl, key, role))
                sf_val = sf.get(key)

                if role in PITCH_ROLES:
                    if frm != 'universalSourceFill' or p.get('value') != sf_val:
                        errs.append('%s/%s: pitch-bearing role must be untouched universalSourceFill' % (lbl, key))

                elif role == 'verb':
                    if frm == 'universalSourceFill':
                        if p.get('value') != sf_val:
                            errs.append('%s/%s: verb sourceFill value != universal' % (lbl, key))
                    elif frm == 'verbBand':
                        lemma, form, val = p.get('lemma'), p.get('form'), p.get('value')
                        if p.get('band') != verb_band:
                            errs.append('%s/%s: verb band %r != tier verbBand %r' % (lbl, key, p.get('band'), verb_band))
                        if verb_band in BANDS and lemma not in BANDS[verb_band]:
                            errs.append('%s/%s: lemma %r not in BANDS[%r]' % (lbl, key, lemma, verb_band))
                        expect_val = inflect(lemma, form) if lemma else None
                        if expect_val != val:
                            errs.append('%s/%s: inflect(%r,%r)=%r != value %r' % (lbl, key, lemma, form, expect_val, val))
                        if (lemma or '').lower() in BANNED_VAGUE or (val or '').lower() in BANNED_VAGUE:
                            errs.append('%s/%s: banned vague verb %r' % (lbl, key, lemma))
                        if form == 'third-cap' and not template.startswith('{%s}' % key):
                            errs.append('%s/%s: form third-cap but slot is not sentence-initial' % (lbl, key))
                    else:
                        errs.append('%s/%s: verb slot has unknown from=%r' % (lbl, key, frm))

                elif role == 'object':
                    if frm == 'universalSourceFill':
                        if p.get('value') != sf_val:
                            errs.append('%s/%s: object sourceFill value != universal' % (lbl, key))
                    elif frm == 'capabilityVocabulary':
                        counts['object_fills'] += 1
                        term, cap_ref_val, value = p.get('term'), p.get('capability'), p.get('value')
                        cap = cap_by_ref.get(cap_ref_val)
                        if cap is None:
                            errs.append('%s/%s: capability ref %r not found in pathway' % (lbl, key, cap_ref_val))
                        else:
                            if cap.get('tier') != tier:
                                errs.append('%s/%s: capability tier %r != statement tier %r' % (lbl, key, cap.get('tier'), tier))
                            vt = (cap.get('vocabulary') or {}).get('terms') or []
                            if term not in vt:
                                errs.append('%s/%s: term %r not verbatim in capability %r vocabulary.terms' % (lbl, key, term, cap_ref_val))
                        if term_rejected(term):
                            errs.append('%s/%s: term %r is a rejected term' % (lbl, key, term))
                        if term in statement_terms:
                            errs.append('%s/%s: term %r repeated within this statement' % (lbl, key, term))
                        statement_terms.append(term)
                        if (term or '').lower() == label.lower():
                            errs.append('%s/%s: term %r equals the pathway label (self-referential)' % (lbl, key, term))

                        exp_num = term_number(term)
                        if p.get('termNumber') != exp_num:
                            errs.append('%s/%s: termNumber %r != re-derived %r' % (lbl, key, p.get('termNumber'), exp_num))

                        req_num = REQUIRED_NUMBER.get((rid, field, key))
                        if req_num and exp_num != req_num:
                            errs.append('%s/%s: term %r is %s, slot requires %s' % (lbl, key, term, exp_num, req_num))

                        if p.get('termClass') not in ('preferred', 'fallback-any'):
                            errs.append('%s/%s: termClass %r not in (preferred, fallback-any)' % (lbl, key, p.get('termClass')))
                        if p.get('termClass') == 'fallback-any':
                            counts['fallback_any'] += 1

                        marker = '{%s}' % key
                        idx = template.find(marker)
                        det_supplied = bool(_DET_BEFORE.search(template[:idx])) if idx >= 0 else False
                        if det_supplied:
                            if value != term:
                                errs.append('%s/%s: determiner supplied by template but value %r != bare term %r' % (lbl, key, value, term))
                        elif exp_num == 'singular':
                            if value != 'the ' + term:
                                errs.append('%s/%s: no determiner + singular term but value %r != %r' % (lbl, key, value, 'the ' + term))
                        else:
                            if value != term:
                                errs.append('%s/%s: no determiner + plural term but value %r != bare term %r' % (lbl, key, value, term))

                        after = template[idx + len(marker):] if idx >= 0 else ''
                        if after.startswith(' of ') and term and ' of ' in term:
                            errs.append('%s/%s: slot sits in "X of <label>" but term %r itself contains " of "' % (lbl, key, term))

                        if field == 'identity' and not p.get('agentInstructionOverridden'):
                            errs.append('%s/%s: identity object slot missing agentInstructionOverridden flag' % (lbl, key))
                    else:
                        errs.append('%s/%s: object slot has unknown from=%r' % (lbl, key, frm))

            cap_vocab_fills = [p for p in prov if p.get('from') == 'capabilityVocabulary']
            if len(cap_vocab_fills) > MAX_OBJECT_FILLS:
                errs.append('%s: %d capabilityVocabulary object fills, max %d' % (lbl, len(cap_vocab_fills), MAX_OBJECT_FILLS))

            terms_used_expect = [p['term'] for p in cap_vocab_fills]
            caps_used_expect = sorted(set(p['capability'] for p in cap_vocab_fills))
            if s.get('termsUsed') != terms_used_expect:
                errs.append('%s: termsUsed != derivable from slotProvenance' % lbl)
            if s.get('capabilitiesUsed') != caps_used_expect:
                errs.append('%s: capabilitiesUsed != derivable from slotProvenance' % lbl)
            expect_specific = bool(subst) or bool(terms_used_expect)
            if s.get('pathwaySpecific') != expect_specific:
                errs.append('%s: pathwaySpecific %r != expected %r' % (lbl, s.get('pathwaySpecific'), expect_specific))
            if not expect_specific:
                counts['nonspecific'] += 1

            stmt = s.get('statement', '')
            if any(c in stmt for c in '{}<>'):
                errs.append('%s: stray brace/bracket in statement' % lbl)
            if not re.match(r'^[A-Z]', stmt):
                errs.append('%s: statement does not start with a capital' % lbl)
            if not stmt.strip().endswith('.') or stmt.strip().endswith('..'):
                errs.append('%s: statement does not end in exactly one full stop' % lbl)
            if '  ' in stmt:
                errs.append('%s: double space in statement' % lbl)
            if re.search(r'\s[.,;:]', stmt):
                errs.append('%s: space before punctuation in statement' % lbl)
            low = ' ' + stmt.lower() + ' '
            for dup in (' the the ', ' a a ', ' to to ', ' and and '):
                if dup in low:
                    errs.append('%s: repeated word %r in statement' % (lbl, dup.strip()))
            if re.search(r'\b\w*iz(e|es|ed|ing|ation)\b', stmt):
                errs.append('%s: American -ize/-ization spelling in statement' % lbl)
            uni_wc, gen_wc = words(row.get(field)), words(stmt)
            if uni_wc and not (0.6 * uni_wc <= gen_wc <= 1.4 * uni_wc):
                errs.append('%s: word count %d outside +-40%% of universal %d' % (lbl, gen_wc, uni_wc))

            tier_statement_texts.append(stmt)
            all_statement_texts.append(stmt)

        joined = ' '.join(tier_statement_texts)
        spec = TIER_PITCH.get(tier) or {}
        for must in spec.get('must', ()):
            if must not in joined:
                errs.append('%s: expected tier-pitch phrase %r not found' % (tier, must))
        for mustnot in spec.get('must_not', ()):
            if mustnot in joined:
                errs.append('%s: tier-discriminating phrase %r should not appear at this tier' % (tier, mustnot))
        if len(set(tier_statement_texts)) != len(tier_statement_texts):
            errs.append('%s: statements within tier are not pairwise distinct' % tier)

    if len(set(all_statement_texts)) != len(all_statement_texts):
        errs.append('statements across the file are not pairwise distinct')
    if counts['statements'] != 9:
        errs.append('expected 9 statements, got %d' % counts['statements'])

    return errs, counts


if __name__ == '__main__':
    pids = sys.argv[1:] or sorted(os.path.splitext(os.path.basename(p))[0]
                                  for p in glob.glob(os.path.join(pt.PATHWAY_DIR, '*.json')))
    universal = load_universal()
    anchors = voice_band_anchors()
    if not BANDS:
        print('FATAL: no section 16 bands parsed from ' + os.path.relpath(VOICE_SPEC, REPO_ROOT))
        sys.exit(1)

    bad = 0
    totals = {'statements': 0, 'object_fills': 0, 'nonspecific': 0, 'fallback_any': 0, 'slug_label': 0}
    for pid in pids:
        errs, counts = check(pid, universal, anchors)
        print('%-46s %s' % (pid, 'PASS' if not errs else 'FAIL (%d)' % len(errs)))
        for e in errs:
            print('    - ' + e)
        bad += bool(errs)
        for k in totals:
            totals[k] += counts.get(k, 0)

    print()
    print('pathways checked:', len(pids))
    print('statements checked:', totals['statements'])
    print('capabilityVocabulary object fills:', totals['object_fills'])
    print('pathwaySpecific=false statements:', totals['nonspecific'])
    print('termClass=fallback-any fills:', totals['fallback_any'])
    print('labelSource=slug pathways:', totals['slug_label'], '(expect 1, reflective-practice)')
    sys.exit(1 if bad else 0)
