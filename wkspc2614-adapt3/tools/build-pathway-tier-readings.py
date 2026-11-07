#!/usr/bin/env python3
"""build-pathway-tier-readings.py - fill the universal benchmark's nine tier
statement formulas with each pathway's own capability vocabulary and voice
band, producing catalogue/context/pathway-tier-readings/<pathway>.json (13
files, 9 statements each = 117 statements).

Deterministic and programmatic: the same inputs always give byte-identical
output. No hand-authoring, no generated prose. See
~/.claude/plans/abundant-discovering-tiger.md for the full design.

Run from the repo root:
    python3 tools/build-pathway-tier-readings.py --self-test
"""
import argparse, json, os, re, sys

import pathway_tiers as pt

REPO_ROOT = pt.REPO_ROOT
UNIVERSAL_PATH = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject',
                               'benchmarks', 'universal-reference.json')
OUT_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'pathway-tier-readings')
VOICE_SPEC = os.path.join(REPO_ROOT, 'reference', 'excelling-voice-specification.md')
TIER_MAPPING = os.path.join(REPO_ROOT, 'docs', 'curriculum', 'pathway-tier-mapping.md')

FIELDS = ('practice', 'knowledge', 'identity')
TIERS = pt.TIERS  # ('introductory', 'intermediate', 'advanced')

# ---------------------------------------------------------------------------
# VERB_SLOTS: every verb-role slot across the 9 universal formulas (23
# entries). 'policy' is 'band' (inflect a lemma taken from this pathway-tier's
# own section 16 voice band) or 'source' (keep the universal sourceFill
# verbatim - the slot is bound by the fixed template text around it: an
# idiom, a frame that needs a specific preposition, or an intransitive verb
# the band does not offer). 'form' is the surface form the template position
# demands, read off the universal sourceFill: bare | third | third-cap | past.
# ---------------------------------------------------------------------------
VERB_SLOTS = {
    ('u-intro', 'practice', 'verb_1'): ('source', 'bare',
        "bound: 'apply X to Y' frame"),
    ('u-intro', 'practice', 'verb_2'): ('source', 'third',
        "bound idiom: 'works with X'"),
    ('u-intro', 'practice', 'verb_3'): ('band', 'third',
        "free slot: '{verb} X' takes any transitive Beginner-band verb"),

    ('u-intro', 'knowledge', 'verb_1'): ('band', 'third-cap',
        "section 15.8 banned-vague opening verb 'Knows', sentence-initial"),
    ('u-intro', 'knowledge', 'verb_2'): ('source', 'bare',
        "bound idiom 'place them in X'; modal 'can' requires the bare form"),

    ('u-intro', 'identity', 'verb_1'): ('band', 'bare',
        "free slot after 'Begins to'; Beginner band already includes 'connect'"),

    ('u-int', 'practice', 'verb_1'): ('source', 'third-cap',
        "bound: 'Applies X to Y' frame, sentence-initial"),
    ('u-int', 'practice', 'verb_2'): ('source', 'third',
        "bound idiom: 'carries out supervised research'"),
    ('u-int', 'practice', 'verb_3'): ('source', 'third',
        "bound idiom: 'works with X'"),
    ('u-int', 'practice', 'verb_4'): ('source', 'third',
        "bound frame: 'communicates X to Y'"),

    ('u-int', 'knowledge', 'verb_1'): ('band', 'third-cap',
        "section 15.8 banned-vague opening verb 'Knows', sentence-initial"),
    ('u-int', 'knowledge', 'verb_2'): ('source', 'past',
        "bound intransitive past: 'the field developed'"),
    ('u-int', 'knowledge', 'verb_3'): ('source', 'third',
        "bound idiom: 'currently stands'"),

    ('u-int', 'identity', 'verb_1'): ('source', 'third-cap',
        "main-clause verb, structurally central to the sentence, sentence-initial"),

    ('u-adv', 'practice', 'verb_1'): ('source', 'third-cap',
        "bound pairing with verb_2: 'Designs and critiques X', sentence-initial"),
    ('u-adv', 'practice', 'verb_2'): ('band', 'third',
        "already an Advanced-band word ('critiques')"),
    ('u-adv', 'practice', 'verb_3'): ('band', 'third',
        "already an Advanced-band word ('evaluates')"),
    ('u-adv', 'practice', 'verb_4'): ('source', 'third',
        "bound frame: 'applies knowledge to problems' (knowledge is fixed text)"),

    ('u-adv', 'knowledge', 'verb_1'): ('band', 'third-cap',
        "banned authority-verb opening 'Commands', sentence-initial"),
    ('u-adv', 'knowledge', 'verb_2'): ('source', 'third',
        "bound idiom: 'sees where X runs out'"),

    ('u-adv', 'identity', 'verb_1'): ('band', 'third',
        "free slot: '{verb} how X shape Y' takes any transitive report-type verb"),
    ('u-adv', 'identity', 'verb_2'): ('source', 'third',
        "bound frame: 'weighs what this means'"),
    ('u-adv', 'identity', 'verb_3'): ('source', 'third',
        "bound frame: 'treats X as Y'"),
}

# ---------------------------------------------------------------------------
# FILLABLE: every object-role slot across the 9 universal formulas (23
# entries), (det, number, priority, rejectOfTerms, preference).
#   det            'supplied' = the template already supplies a determiner
#                  ("the X", "its X", "their own X") - insert nothing.
#                  'none' = bare NP - prefix "the " iff the chosen term is
#                  singular.
#   number         grammatical number the template's own verb/pronoun
#                  agreement REQUIRES: 'plural' | 'singular' | 'any'.
#   priority       fill order within one statement (1 = filled first).
#                  Combined with MAX_OBJECT_FILLS, this - not a separate
#                  eligibility flag - is what keeps grammatically awkward
#                  slots (an adjective wedged between the fixed text and the
#                  slot, or a slot bound inside a relative clause) rarely
#                  touched: they still partition into this table, they are
#                  just last in line.
#   rejectOfTerms  the slot already sits in "the X of <label>"; a term
#                  containing " of " would double the preposition.
#   preference     'process' = prefer a process/method/artefact noun from the
#                  pool before any other eligible term; None = no preference.
# ---------------------------------------------------------------------------
FILLABLE = {
    ('u-intro', 'practice', 'object_1'): ('supplied', 'any', 1, True, 'process'),
    ('u-intro', 'practice', 'object_2'): ('none', 'any', 3, False, None),
    ('u-intro', 'practice', 'object_3'): ('none', 'any', 2, False, None),

    ('u-intro', 'knowledge', 'object_1'): ('supplied', 'plural', 1, False, None),

    ('u-intro', 'identity', 'object_1'): ('none', 'any', 1, False, None),
    ('u-intro', 'identity', 'object_2'): ('none', 'any', 2, False, None),

    ('u-int', 'practice', 'object_1'): ('supplied', 'any', 1, True, 'process'),
    ('u-int', 'practice', 'object_2'): ('none', 'any', 2, False, None),
    ('u-int', 'practice', 'object_3'): ('none', 'any', 5, False, None),
    ('u-int', 'practice', 'object_4'): ('none', 'any', 3, False, None),
    ('u-int', 'practice', 'object_5'): ('none', 'any', 4, False, None),

    ('u-int', 'knowledge', 'object_1'): ('supplied', 'any', 1, True, None),

    ('u-int', 'identity', 'object_1'): ('none', 'any', 1, False, None),
    ('u-int', 'identity', 'object_2'): ('none', 'plural', 2, False, None),

    ('u-adv', 'practice', 'object_1'): ('none', 'any', 1, False, 'process'),
    ('u-adv', 'practice', 'object_2'): ('none', 'any', 2, False, None),

    ('u-adv', 'knowledge', 'object_1'): ('supplied', 'any', 1, True, None),
    ('u-adv', 'knowledge', 'object_2'): ('supplied', 'any', 2, False, None),
    ('u-adv', 'knowledge', 'object_3'): ('none', 'any', 3, False, None),
    ('u-adv', 'knowledge', 'object_4'): ('none', 'singular', 4, False, None),

    ('u-adv', 'identity', 'object_1'): ('supplied', 'plural', 1, False, None),
    ('u-adv', 'identity', 'object_2'): ('supplied', 'any', 2, False, None),
    ('u-adv', 'identity', 'object_3'): ('supplied', 'any', 3, False, None),
}

MAX_OBJECT_FILLS = 2

# Regex for a determiner immediately before a slot. 'own' may intervene
# between a possessive and the slot ("their own {object_1}") without
# changing the determiner context - no second article is needed either way.
_DET_BEFORE = re.compile(r"(?:the|its|their|a|an|'s)(?:\s+own)?\s*$")

# Last-word 's' endings that are grammatically singular, not plural markers:
# -is nouns, -ss nouns, the explicit mass noun 'ethics', and initial-capital
# proper nouns (checked separately, by case, not spelling).
_SINGULAR_S_EXCEPTIONS = {'analysis', 'synthesis', 'fairness', 'stress', 'ethics'}

_PROCESS_NOUN_HINTS = ('cycle', 'process', 'enquiry', 'inquiry', 'method',
                        'approach', 'procedure', 'practice', 'strategy',
                        'technique', 'workflow')


_HEAD_PREPOSITIONS = (' of ', ' with ', ' for ', ' to ', ' from ', ' on ', ' in ')


def term_head(term):
    """The head noun phrase before its first post-modifying preposition,
    e.g. 'breadth and depth of learning' -> 'breadth and depth', 'dialogue
    with tutors' -> 'dialogue'. Coordinating 'and' is never split on (it
    joins the head itself, e.g. 'costs and benefits' stays whole). Checked
    empirically against all 228 corpus terms: only 'dialogue with tutors'
    changes grammatical number under this rule (plural -> correctly
    singular; its one 's'-final word, 'tutors', is the object of 'with',
    not the head). Most corpus terms have none of these prepositions and
    are returned unchanged."""
    best = term
    for p in _HEAD_PREPOSITIONS:
        if p in best:
            best = best.split(p, 1)[0].strip()
    return best


def term_number(term):
    """'plural' if the term's head's last word ends in a bare pluralising
    's' not covered by a known singular exception; 'singular' otherwise.
    Checked empirically against all 228 distinct corpus terms: the only
    's'-final heads that are grammatically singular are analysis/synthesis
    (-is), fairness/stress (-ss), ethics (explicit), and initial-capital
    proper nouns (Gibbs, Johns) - there a trailing 's' is part of the name."""
    head = term_head(term)
    words = head.split()
    last = words[-1] if words else head
    if last[:1].isupper():
        return 'singular'
    bare = last.lower()
    if bare in _SINGULAR_S_EXCEPTIONS:
        return 'singular'
    return 'plural' if bare.endswith('s') else 'singular'


def term_rejected(term):
    """Bare proper nouns (the whole head is one capitalised word: 'Gibbs',
    'Kolb', 'GenAI') and leading possessive fragments ('own point', 'own
    work') are rejected: either would produce broken text in a slot. A
    multi-word head that merely starts with a capital ('AI literacy',
    'Boolean operators') is a normal noun phrase and is not rejected."""
    head = term_head(term)
    words = head.split()
    if not words:
        return True
    if len(words) == 1 and words[0][:1].isupper():
        return True
    if words[0].lower() == 'own':
        return True
    return False


def is_process_noun(term):
    head = term_head(term).lower()
    return any(h in head for h in _PROCESS_NOUN_HINTS)


def verb_bands():
    """Section 16 of the voice specification: band name -> outcome verbs.
    Mirrors tools/check-statement-formulas.py's verb_bands() and
    tools/build-universal-benchmark.py's verb_bands() (tier-specification.md
    §110 forbids a second hand-typed list, so this is the live parser, not a
    third copy of the data)."""
    bands = {}
    for line in open(VOICE_SPEC, encoding='utf-8'):
        m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|.*Outcome verbs:\s*([^|]+?)\.?\s*\|\s*$', line)
        if m:
            bands[m.group(1)] = [v.strip() for v in m.group(2).split(',') if v.strip()]
    return bands


BANDS = verb_bands()

# Section-16 bands in ascending rigour order, for the "three consecutive
# bands ascending" check and for the default (non-up-skewed) anchor.
BAND_ORDER = ('Foundation', 'Beginner', 'Intermediate', 'Advanced', 'Masters', 'Doctoral')

_ANCHOR_RE = re.compile(
    r'Introductory\s*\u2192\s*\xa7?16\s*(\w+),\s*'
    r'Intermediate\s*\u2192\s*\xa7?16\s*(\w+),\s*'
    r'Advanced\s*\u2192\s*\xa7?16\s*(\w+)')
_PATHWAY_HEADER_RE = re.compile(r'^##\s*Pathway\s+(\d+)\s*\u2014')


def voice_band_anchors():
    """pathwayNumber (int) -> {'introductory': band, 'intermediate': band,
    'advanced': band} parsed live from docs/curriculum/pathway-tier-mapping.md.
    Each pathway's own '## Pathway N - ...' section is searched for its
    '**Voice-band anchor:** Introductory->SS16 X, Intermediate->SS16 Y,
    Advanced->SS16 Z' line. Unparsable is the caller's problem (no silent
    default): a pathway with no parsed anchor is simply absent from the
    returned dict."""
    text = open(TIER_MAPPING, encoding='utf-8').read()
    lines = text.split('\n')
    anchors = {}
    current = None
    for line in lines:
        m = _PATHWAY_HEADER_RE.match(line)
        if m:
            current = int(m.group(1))
            continue
        if current is not None and '**Voice-band anchor:**' in line:
            m2 = _ANCHOR_RE.search(line)
            if m2:
                anchors[current] = {
                    'introductory': m2.group(1),
                    'intermediate': m2.group(2),
                    'advanced': m2.group(3),
                }
            current = None  # one anchor per pathway section
    return anchors


def voice_band_anchor(pathway_number):
    """This pathway's (introductory, intermediate, advanced) band names, as a
    tuple in TIERS order. Raises if unparsable - a hard fail, not a silent
    default, per the plan."""
    anchors = voice_band_anchors()
    if pathway_number not in anchors:
        raise ValueError('no voice-band anchor parsed for pathway %r' % pathway_number)
    a = anchors[pathway_number]
    return tuple(a[t] for t in TIERS)


def load_universal():
    return json.load(open(UNIVERSAL_PATH, encoding='utf-8'))


def universal_slots(doc):
    """(rowId, field, key) -> slot dict, for every slot in every tierReadings
    statement formula. Used by --self-test to prove VERB_SLOTS/FILLABLE
    partition exactly the verb/object slots that actually exist."""
    out = {}
    for row in doc['tierReadings']['rows']:
        rid = row['rowId']
        for field in FIELDS:
            f = row['formulas'][field]
            for s in f.get('slots') or []:
                out[(rid, field, s['key'])] = s
    return out


# ---------------------------------------------------------------------------
# Subject substitution: 6 of 9 templates carry literal "the subject" text.
# 'possessive' rewrites "the subject's {object_1}" -> "the {object_1} of
# <label>" (a bare possessive reads badly for long labels). 'plain' replaces
# the literal substring "the subject" with <label> directly. The other 3
# templates (u-intro/identity, u-adv/practice, u-adv/identity) contain no
# "the subject" text at all and take no substitution.
# ---------------------------------------------------------------------------
SUBJECT_SUBSTITUTION = {
    ('u-intro', 'practice'): ('possessive', "the subject's {object_1}",
                              lambda label: "the {object_1} of " + label),
    ('u-intro', 'knowledge'): ('plain', "the subject", lambda label: label),
    ('u-int', 'practice'): ('possessive', "the subject's {object_1}",
                            lambda label: "the {object_1} of " + label),
    ('u-int', 'knowledge'): ('plain', "the subject", lambda label: label),
    ('u-int', 'identity'): ('plain', "the subject", lambda label: label),
    ('u-adv', 'knowledge'): ('plain', "the subject", lambda label: label),
}

PREFERRED_STRAND = {'practice': 'procedural', 'knowledge': 'conceptual', 'identity': 'metacognitive'}
STRANDS = ('conceptual', 'procedural', 'metacognitive')


def pathway_label(pdoc, pid):
    """identity.practiceNoun is the clean lowercase noun phrase. Missing on
    reflective-practice (1 of 13): fall back to the humanised slug and report
    the fallback. identity.title is never used: all 13 contain the banned
    phrase "academic skills"."""
    pn = (pdoc.get('identity') or {}).get('practiceNoun')
    if pn:
        return pn, 'identity.practiceNoun'
    return pid.replace('-', ' '), 'slug'


def strand(c):
    """conceptual | procedural | metacognitive, read from knowledgeKind by
    whichever of the three words appears earliest in the text (compound
    descriptions lead with the primary strand: 'procedural with conceptual'
    is primarily procedural). Falls back to the rowId index (i/d/e N -> N)
    when knowledgeKind is null (the 31 capabilities with everything null) -
    moot in practice since those capabilities have no vocabulary.terms
    either, so they never contribute to a pool regardless of strand label."""
    kk = (c.get('knowledgeKind') or '').lower()
    hits = [(kk.index(w), w) for w in STRANDS if w in kk]
    if hits:
        return min(hits)[1]
    idx = {'1': 'conceptual', '2': 'procedural', '3': 'metacognitive'}
    rid = c.get('rowId') or ''
    return idx.get(rid[1:2], 'conceptual')


def build_pool(pid, tier, field):
    """This (pathway, tier, field)'s term pool: the tier's 3 capabilities
    ranked (strand matching this field's preferred strand first, then the
    other two strands in a fixed canonical order, then rowId), their
    vocabulary.terms flattened in that order, duplicates dropped. Returns
    (pool, capability_refs_in_rowid_order) - the pool for filling, and the
    tier's capability refs in rowId order for the tierReadings entry."""
    preferred = PREFERRED_STRAND[field]
    chain = [preferred] + [s for s in STRANDS if s != preferred]
    caps = [c for c in pt.raw_capabilities(pid) if c.get('tier') == tier]
    caps_by_rowid = sorted(caps, key=lambda c: c.get('rowId') or '')
    cap_refs_rowid_order = [pt.cap_ref(c, pid) for c in caps_by_rowid]

    def rank(c):
        s = strand(c)
        return (chain.index(s) if s in chain else len(chain), c.get('rowId') or '')

    pool = []
    seen = set()
    for c in sorted(caps, key=rank):
        ref = pt.cap_ref(c, pid)
        s = strand(c)
        for t in (c.get('vocabulary') or {}).get('terms') or []:
            if t in seen:
                continue
            seen.add(t)
            pool.append({'term': t, 'capability': ref, 'rowId': c.get('rowId'), 'strand': s})
    return pool, cap_refs_rowid_order


def _third_person(lemma):
    """Inflect a band lemma's last word to third-person-singular present.
    Handles the two irregularities the five bands actually contain: a
    trailing sibilant takes -es (none in these bands, kept for safety) and a
    consonant+y takes -ies ('apply' -> 'applies', 'justify' -> 'justifies');
    a multi-word lemma inflects only its last word ('critically evaluate' ->
    'critically evaluates')."""
    words = lemma.split()
    head = words[-1]
    if head.endswith(('s', 'x', 'z', 'sh', 'ch')):
        infl = head + 'es'
    elif len(head) > 1 and head[-1] == 'y' and head[-2].lower() not in 'aeiou':
        infl = head[:-1] + 'ies'
    else:
        infl = head + 's'
    return ' '.join(words[:-1] + [infl])


def inflect(lemma, form):
    if form == 'bare':
        return lemma
    if form == 'third':
        return _third_person(lemma)
    if form == 'third-cap':
        v = _third_person(lemma)
        return v[0].upper() + v[1:]
    raise ValueError('band verb slots only use bare/third/third-cap, got %r' % form)


def build_statement(rid, field, row, tier, band, pool, cap_refs_rowid_order, label, label_source):
    """Fill one of the 9 universal statement formulas for one pathway tier.
    Returns the full statement dict for the output JSON."""
    f = row['formulas'][field]
    universal_template = f['template']
    universal_statement = row[field]
    source_fill = f['sourceFill']
    slots = f['slots']

    template = universal_template
    subject_substitution = None
    subst = SUBJECT_SUBSTITUTION.get((rid, field))
    if subst:
        kind, old, make_new = subst
        new = make_new(label)
        assert old in template, '%s/%s: %r not found in template %r' % (rid, field, old, template)
        template = template.replace(old, new, 1)
        subject_substitution = {
            'form': 'possessive-of-rewrite' if kind == 'possessive' else 'plain-substitution',
            'from': old, 'to': new, 'label': label, 'labelSource': label_source,
        }

    # Object slots: decide which get a capability term, up to MAX_OBJECT_FILLS,
    # in priority order, before the single template-order render pass below.
    obj_slots = [s for s in slots if s['role'] == 'object']
    obj_decisions = {}
    used_terms = []
    fills_used = 0
    for s in sorted(obj_slots, key=lambda s: FILLABLE[(rid, field, s['key'])][2]):
        key = s['key']
        det, number, _priority, reject_of, pref = FILLABLE[(rid, field, key)]
        if fills_used >= MAX_OBJECT_FILLS:
            obj_decisions[key] = None
            continue
        # A term equal to the pathway's own label is excluded everywhere, not
        # just in "X of <label>" slots: filling any slot with the pathway's
        # own name reads as circular ("critiques the creativity", "its
        # creativity") regardless of surrounding grammar. 3 of 13 pathways
        # have a vocabulary term matching their own label (academic-writing/
        # 'academic writing', ai-technology/'AI literacy', creativity/
        # 'creativity').
        candidates = [e for e in pool if e['term'] not in used_terms
                      and not term_rejected(e['term'])
                      and e['term'].lower() != label.lower()]
        if reject_of:
            # The slot already sits in "the X of <label>"; a term containing
            # " of " would double the preposition.
            candidates = [e for e in candidates if ' of ' not in e['term']]
        if number != 'any':
            candidates = [e for e in candidates if term_number(e['term']) == number]
        chosen = None
        term_class = None
        if pref == 'process':
            preferred_hits = [e for e in candidates if is_process_noun(e['term'])]
            if preferred_hits:
                chosen, term_class = preferred_hits[0], 'preferred'
            elif candidates:
                chosen, term_class = candidates[0], 'fallback-any'
        elif candidates:
            chosen, term_class = candidates[0], 'preferred'
        if chosen:
            used_terms.append(chosen['term'])
            fills_used += 1
            value = chosen['term']
            if det == 'none' and term_number(chosen['term']) == 'singular':
                value = 'the ' + value
            obj_decisions[key] = {
                'det': det, 'value': value, 'term': chosen['term'], 'capability': chosen['capability'],
                'rowId': chosen['rowId'], 'strand': chosen['strand'],
                'termNumber': term_number(chosen['term']), 'termClass': term_class,
            }
        else:
            obj_decisions[key] = None

    # Single template-order pass: verb slots, object slots, pitch slots.
    fill = {}
    slot_provenance = []
    verb_i = 0
    for s in slots:
        key, role = s['key'], s['role']
        if role == 'verb':
            policy, form, why = VERB_SLOTS[(rid, field, key)]
            sf_val = source_fill[key]
            if policy == 'source':
                fill[key] = sf_val
                slot_provenance.append({'slot': key, 'role': 'verb', 'from': 'universalSourceFill',
                                         'value': sf_val, 'reason': why})
            else:
                lemma = BANDS[band][verb_i % len(BANDS[band])]
                verb_i += 1
                value = inflect(lemma, form)
                fill[key] = value
                slot_provenance.append({'slot': key, 'role': 'verb', 'from': 'verbBand', 'band': band,
                                         'lemma': lemma, 'form': form, 'value': value})
        elif role == 'object':
            d = obj_decisions.get(key)
            sf_val = source_fill[key]
            if d is None:
                fill[key] = sf_val
                slot_provenance.append({'slot': key, 'role': 'object', 'from': 'universalSourceFill',
                                         'value': sf_val})
            else:
                entry = {'slot': key, 'role': 'object', 'from': 'capabilityVocabulary',
                          'capability': d['capability'], 'rowId': d['rowId'],
                          'strand': d['strand'], 'term': d['term'],
                          'termNumber': d['termNumber'], 'termClass': d['termClass'],
                          'value': d['value']}
                if field == 'identity':
                    # Decision 5 overrides the universal formula's own
                    # agentInstruction, which explicitly pins these object
                    # slots to their universal wording (quoted verbatim
                    # below). Recorded here, not hidden, per the plan's
                    # "Owner override to record, not hide".
                    entry['agentInstructionOverridden'] = True
                    entry['overriddenInstruction'] = f.get('agentInstruction')
                fill[key] = d['value']
                slot_provenance.append(entry)
        else:
            sf_val = source_fill[key]
            fill[key] = sf_val
            slot_provenance.append({'slot': key, 'role': role, 'from': 'universalSourceFill', 'value': sf_val})

    statement = template.format(**fill)
    assert '{' not in statement and '}' not in statement, 'stray brace: %r' % statement
    assert statement.strip().endswith('.') and not statement.strip().endswith('..'), \
        'not a single full stop: %r' % statement
    assert '  ' not in statement, 'double space: %r' % statement
    assert ' the the ' not in statement.lower(), '"the the": %r' % statement
    assert statement[:1].isupper(), 'does not start with a capital: %r' % statement

    terms_used = [p['term'] for p in slot_provenance if p.get('from') == 'capabilityVocabulary']
    capabilities_used = sorted(set(p['capability'] for p in slot_provenance if p.get('from') == 'capabilityVocabulary'))
    pathway_specific = bool(subject_substitution) or bool(terms_used)
    outcome_refs = [oc['id'] for oc in f.get('outcomes') or []]

    out = {
        'statement': statement,
        'universalStatement': universal_statement,
        'template': template,
        'universalTemplate': universal_template,
        'fill': fill,
        'slotProvenance': slot_provenance,
        'termsUsed': terms_used,
        'capabilitiesUsed': capabilities_used,
        'pathwaySpecific': pathway_specific,
        'universalOutcomeRefs': outcome_refs,
    }
    if subject_substitution:
        out['subjectSubstitution'] = subject_substitution
    return out


def build_pathway(pid):
    """The full catalogue/context/pathway-tier-readings/<pid>.json payload."""
    universal = load_universal()
    pdoc = json.load(open(os.path.join(pt.PATHWAY_DIR, pid + '.json'), encoding='utf-8'))
    label, label_source = pathway_label(pdoc, pid)
    pathway_number = (pdoc.get('identity') or {}).get('pathwayNumber')
    anchor = voice_band_anchor(pathway_number)  # (introBand, interBand, advBand)

    tier_readings = []
    for tier_idx, tier in enumerate(TIERS):
        rid = {'introductory': 'u-intro', 'intermediate': 'u-int', 'advanced': 'u-adv'}[tier]
        row = next(r for r in universal['tierReadings']['rows'] if r['rowId'] == rid)
        band = anchor[tier_idx]
        statements = {}
        all_cap_refs = None
        for field in FIELDS:
            pool, cap_refs_rowid_order = build_pool(pid, tier, field)
            if all_cap_refs is None:
                all_cap_refs = cap_refs_rowid_order
            statements[field] = build_statement(rid, field, row, tier, band, pool,
                                                 cap_refs_rowid_order, label, label_source)
        tier_readings.append({
            'tier': tier,
            'fheqLevel': row.get('fheqLevel'),
            'universalRowId': rid,
            'verbBand': band,
            'verbBandBasis': {'doc': 'docs/curriculum/pathway-tier-mapping.md',
                               'ref': 'Pathway %d voice-band anchor' % pathway_number},
            'capabilities': all_cap_refs,
            'statements': statements,
        })

    note = (
        "Pathway tier readings: the universal benchmark's three tier readings "
        "(practice, knowledge, identity, per tier) re-filled with this pathway's "
        "own capability vocabulary and voice band. Generated deterministically "
        "and mechanically by tools/build-pathway-tier-readings.py; no "
        "hand-authoring and no generated prose. Every slot is either a verb "
        "inflected from this "
        "pathway's own section 16 voice band, a noun phrase taken verbatim "
        "from a capability's vocabulary.terms, or the universal wording kept "
        "unchanged. Known limitation: the fill is grammatical by construction "
        "but not semantically curated; a harvested term can land in a slot it "
        "does not suit. Every fill is traceable in slotProvenance. The "
        "identity object slots are filled by owner decision, overriding the "
        "universal formula's own agentInstruction guidance to keep them. "
        "Draft for review, not finished copy."
    )

    return {
        'pathway': pid,
        'status': 'generated',
        'note': note,
        'tierReadings': tier_readings,
        'source': {
            'script': 'tools/build-pathway-tier-readings.py',
            'inputs': [
                'catalogue/context/subject/benchmarks/universal-reference.json (tierReadings.rows[].formulas)',
                'catalogue/context/pathway/%s.json (capabilities[].vocabulary.terms, knowledgeKind, identity.practiceNoun)' % pid,
                'reference/excelling-voice-specification.md (section 16 verb bands)',
                'docs/curriculum/pathway-tier-mapping.md (per-pathway voice-band anchor)',
            ],
            'note': ('Deterministic: the same inputs always give byte-identical output, '
                     'so a rebuild is a no-op and determinism is itself checkable. No '
                     'timestamp is recorded. Our words, no issuer or book text.'),
        },
    }


def self_test():
    errs = []
    doc = load_universal()
    slots = universal_slots(doc)

    verb_keys = {k for k, s in slots.items() if s['role'] == 'verb'}
    object_keys = {k for k, s in slots.items() if s['role'] == 'object'}

    # --- partition: VERB_SLOTS == every verb slot, FILLABLE == every object
    # slot, no overlap, no gap, nothing extra.
    if set(VERB_SLOTS) != verb_keys:
        missing = verb_keys - set(VERB_SLOTS)
        extra = set(VERB_SLOTS) - verb_keys
        if missing:
            errs.append('VERB_SLOTS missing verb slots: %s' % sorted(missing))
        if extra:
            errs.append('VERB_SLOTS has non-verb/unknown keys: %s' % sorted(extra))
    if set(FILLABLE) != object_keys:
        missing = object_keys - set(FILLABLE)
        extra = set(FILLABLE) - object_keys
        if missing:
            errs.append('FILLABLE missing object slots: %s' % sorted(missing))
        if extra:
            errs.append('FILLABLE has non-object/unknown keys: %s' % sorted(extra))
    overlap = set(VERB_SLOTS) & set(FILLABLE)
    if overlap:
        errs.append('VERB_SLOTS and FILLABLE overlap: %s' % sorted(overlap))
    if len(VERB_SLOTS) + len(FILLABLE) != 46:
        errs.append('expected 46 verb+object slots total, got %d'
                     % (len(VERB_SLOTS) + len(FILLABLE)))

    # --- VERB_SLOTS form must match how sourceFill is actually surfaced.
    for key, (policy, form, why) in VERB_SLOTS.items():
        if key not in slots:
            continue
        rid, field, _ = key
        row = next(r for r in doc['tierReadings']['rows'] if r['rowId'] == rid)
        sf = row['formulas'][field]['sourceFill'][key[2]]
        label = '%s/%s/%s' % key
        if form == 'third-cap':
            if not sf[:1].isupper():
                errs.append('%s: form third-cap but sourceFill %r is not capitalised' % (label, sf))
        elif form == 'past':
            if not (sf.endswith('ed') or sf in ('stood', 'sat', 'ran')):
                errs.append('%s: form past but sourceFill %r does not look past-tense' % (label, sf))
        elif form == 'third':
            head = sf.split()[0]
            if not (sf[:1].islower() and head.endswith('s')):
                errs.append('%s: form third but sourceFill %r does not look third-person' % (label, sf))
        elif form == 'bare':
            head = sf.split()[0]
            if not (sf[:1].islower() and not head.endswith('s')):
                errs.append('%s: form bare but sourceFill %r looks inflected' % (label, sf))
        else:
            errs.append('%s: unknown form %r' % (label, form))
        if policy not in ('band', 'source'):
            errs.append('%s: unknown policy %r' % (label, policy))

    # --- FILLABLE determiner context must match the template's own fixed
    # text immediately before the slot (allowing 'own' to intervene after a
    # possessive: 'their own {object_1}').
    for key, (det, number, priority, reject, pref) in FILLABLE.items():
        if key not in slots:
            continue
        rid, field, slot_key = key
        row = next(r for r in doc['tierReadings']['rows'] if r['rowId'] == rid)
        tmpl = row['formulas'][field]['template']
        marker = '{%s}' % slot_key
        idx = tmpl.index(marker)
        before = tmpl[:idx]
        matched = bool(_DET_BEFORE.search(before))
        label = '%s/%s/%s' % key
        if det == 'supplied' and not matched:
            errs.append('%s: det=supplied but no determiner immediately precedes the slot in %r' % (label, tmpl))
        if det == 'none' and matched:
            errs.append('%s: det=none but a determiner immediately precedes the slot in %r' % (label, tmpl))
        if det not in ('supplied', 'none'):
            errs.append('%s: unknown det %r' % (label, det))
        if number not in ('any', 'plural', 'singular'):
            errs.append('%s: unknown number %r' % (label, number))
        if pref not in (None, 'process'):
            errs.append('%s: unknown preference %r' % (label, pref))

    # --- number heuristic validated over every distinct term in the corpus:
    # the stated exceptions must classify singular, and a sample of plain
    # plurals must classify plural.
    import glob as _glob
    terms = set()
    for p in _glob.glob(os.path.join(pt.PATHWAY_DIR, '*.json')):
        pdoc = json.load(open(p, encoding='utf-8'))
        for c in pdoc.get('capabilities') or []:
            for t in (c.get('vocabulary') or {}).get('terms') or []:
                terms.add(t)
    if len(terms) < 100:
        errs.append('corpus term census looks too small (%d terms) - check PATHWAY_DIR glob' % len(terms))
    known_singular = {'analysis', 'synthesis', 'fairness', 'stress', 'research ethics', 'Gibbs', 'Johns', 'Kolb'}
    for t in known_singular:
        if t in terms and term_number(t) != 'singular':
            errs.append('term_number(%r) == %r, want singular' % (t, term_number(t)))
    known_plural = {'assumptions', 'sources', 'methods', 'judgements', 'values', 'keywords'}
    for t in known_plural:
        if t in terms and term_number(t) != 'plural':
            errs.append('term_number(%r) == %r, want plural' % (t, term_number(t)))
    rejected = [t for t in terms if term_rejected(t)]
    expect_rejected = {'Gibbs', 'Johns', 'Kolb', 'GenAI', 'own performance', 'own point', 'own work'}
    missing_reject = expect_rejected & terms - set(rejected)
    if missing_reject:
        errs.append('expected rejected but not: %s' % sorted(missing_reject))
    wrongly_rejected = {t for t in rejected if t in {'AI literacy', 'AI use', 'Boolean operators', 'GenAI outputs'}}
    if wrongly_rejected:
        errs.append('wrongly rejected multi-word capitalised terms: %s' % sorted(wrongly_rejected))

    # --- section 16 bands and per-pathway anchors, parsed live.
    if not BANDS:
        errs.append('no section 16 bands parsed from ' + os.path.relpath(VOICE_SPEC, REPO_ROOT))
    anchors = voice_band_anchors()
    pathway_files = sorted(f for f in os.listdir(pt.PATHWAY_DIR) if f.endswith('.json'))
    if len(pathway_files) != 13:
        errs.append('expected 13 pathway files, found %d' % len(pathway_files))
    for fn in pathway_files:
        pdoc = json.load(open(os.path.join(pt.PATHWAY_DIR, fn), encoding='utf-8'))
        pn = (pdoc.get('identity') or {}).get('pathwayNumber')
        if pn not in anchors:
            errs.append('%s: pathwayNumber %r has no parsed voice-band anchor' % (fn, pn))
            continue
        bands3 = voice_band_anchor(pn)
        for b in bands3:
            if b not in BAND_ORDER:
                errs.append('%s: anchor band %r is not a real section 16 band' % (fn, b))
        idxs = [BAND_ORDER.index(b) for b in bands3 if b in BAND_ORDER]
        if len(idxs) == 3 and (idxs[1] != idxs[0] + 1 or idxs[2] != idxs[1] + 1):
            errs.append('%s: anchor bands %r are not three consecutive section 16 bands ascending'
                         % (fn, bands3))
        for b in bands3:
            if b in BAND_ORDER and b not in BANDS:
                errs.append('%s: anchor band %r has no verb options parsed' % (fn, b))
    if len(anchors) != 13:
        errs.append('expected 13 parsed voice-band anchors, got %d' % len(anchors))
    researching_pn = 9
    if researching_pn in anchors and voice_band_anchor(researching_pn) != ('Intermediate', 'Advanced', 'Masters'):
        errs.append('pathway 9 (Researching) anchor == %r, want up-skewed (Intermediate, Advanced, Masters)'
                     % (voice_band_anchor(researching_pn),))

    print('build-pathway-tier-readings.py --self-test:', 'PASS' if not errs else 'FAIL (%d)' % len(errs))
    for e in errs:
        print('    - ' + e)
    print()
    print('verb slots:', len(VERB_SLOTS), '| object slots:', len(FILLABLE),
          '| band policy:', sum(1 for v in VERB_SLOTS.values() if v[0] == 'band'),
          '| source policy:', sum(1 for v in VERB_SLOTS.values() if v[0] == 'source'))
    print('corpus terms censused:', len(terms), '| rejected:', len(rejected))
    print('section 16 bands parsed:', sorted(BANDS))
    print('voice-band anchors parsed:', len(anchors), 'of 13')
    for pn in sorted(anchors):
        print('    pathway %2d: %s' % (pn, voice_band_anchor(pn)))
    return errs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('pathway', nargs='?', help='pathway key, e.g. academic-writing')
    ap.add_argument('--dry-run', action='store_true', help='print, do not write')
    ap.add_argument('--report', action='store_true', help='read-through report')
    ap.add_argument('--self-test', action='store_true', help='validate VERB_SLOTS/FILLABLE')
    args = ap.parse_args()

    if args.self_test:
        errs = self_test()
        sys.exit(1 if errs else 0)

    if not args.pathway:
        ap.error('a pathway key is required unless --self-test is given')

    payload = build_pathway(args.pathway)

    if args.dry_run or args.report:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, args.pathway + '.json')
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False, sort_keys=False)
        fh.write('\n')
    print('wrote', os.path.relpath(out_path, REPO_ROOT))


if __name__ == '__main__':
    main()
