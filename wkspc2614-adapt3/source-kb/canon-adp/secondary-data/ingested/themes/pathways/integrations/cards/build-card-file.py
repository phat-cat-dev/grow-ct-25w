#!/usr/bin/env python3
"""Build a pathway's card integration file in the golden shape (D-ing-0061).

Reads a hand-written plan (`plans/<pathway-id>.yaml`: the nine cards, their order,
kinds of knowledge and framework picks, the readings of each benchmark extract, the
tier statements and review items) and fills the rest from the sources:
  - the pathway core's A10 cards (theory, professional frameworks) and front matter;
  - the card vocabulary (`ing-card-vocabulary.json`: verbs, measures, keywords);
  - adp-0212's capability cards and draft book map (META handover mta-nts-ho-adp-nts-0007);
  - the guide's Markdown copy, to check every quote and recompute its page;
  - META's INGEST theory runs (title, SHA-256 prefix, summary) and the FHEQ and CQFW runs;
  - the pathway model's tier map and catalogue (mirror).
Writes `ing-cards-<pathway-id>.md` and appends the pathway's verbs-in-context records to
`verbs-in-context.json`. A working tool for ing, never a record.

Usage: python3 build-card-file.py <pathway-id> [--write]
Without --write it prints the checks only.
"""
import hashlib, json, os, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ING = os.path.dirname(os.path.dirname(HERE))                      # sandboxes/ing
UNI = os.path.abspath(os.path.join(HERE, *(['..'] * 7)))          # wkspc2600-uni
CORES = os.path.join(ING, 'pathways')
VOCAB = os.path.join(HERE, 'ing-card-vocabulary.json')
VIC = os.path.join(HERE, 'verbs-in-context.json')
PLANS = os.path.join(HERE, 'plans')
HO = os.path.join(UNI, 'mta/claude/mta-relay/ho/mta-nts-ho-adp-nts-0007')
MIRROR = os.path.join(UNI, 'adp/adp-mirror')
BOOK = os.path.join(MIRROR, 'excelling-at-university.md')
THEORY = os.path.join(UNI, 'library/ingested/theory')
STD = os.path.join(UNI, 'library/ingested/standards')
FHEQ = os.path.join(STD, 'ingest-std-qaa-fheq-2024-framework/ingest-std-qaa-fheq-2024-framework.md')
CQFW = os.path.join(STD, 'ingest-std-welsh-government-cqfw-2009-framework/ingest-std-welsh-government-cqfw-2009-framework.md')

LEVEL = {'i1': 'L3', 'i2': 'L4', 'i3': 'L5', 'd1': 'L4', 'd2': 'L5', 'd3': 'L6', 'e1': 'L5', 'e2': 'L6', 'e3': 'L7'}
TIER = {'i': ('introduced', 'Introductory'), 'd': ('developed', 'Intermediate'), 'e': ('extended', 'Advanced')}
ORDER = ['i1', 'i2', 'i3', 'd1', 'd2', 'd3', 'e1', 'e2', 'e3']
PROBLEMS = []
NOTFOUND = []


def sha12(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:12]


# ---------- the guide ----------
BOOKTEXT = open(BOOK, encoding='utf-8').read()


def _norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('\\*', '').replace('*', '')
    return re.sub(r'\s+', ' ', s).strip()


# a normalised copy of the guide with a map back to page numbers
_NB, _PAGES = [], []
_page = None
for tok in re.split(r'(<!-- *pp?\.? *[^>]*?-->)', BOOKTEXT):
    m = re.match(r'<!-- *pp?\.? *([^ >]+?) *-->', tok)
    if m:
        _page = m.group(1)
        continue
    n = _norm(tok)
    if n:
        _NB.append(n + ' ')
        _PAGES.append((sum(len(x) for x in _NB) - len(n) - 1, _page))
NORMBOOK = ''.join(_NB).lower()


def page_of(quote):
    """Return (first page, last page) of a quote in the guide, or None if not found.
    A quote is ended at the first page marker by the split above, so a quote
    across a page break is found only in part; try halves."""
    q = _norm(quote).lower()
    i = NORMBOOK.find(q)
    if i < 0:
        return None
    first = last = None
    for start, pg in _PAGES:
        if start <= i:
            first = pg
        if start <= i + len(q):
            last = pg
    # the page marker precedes the text it starts; a chunk's page is the last marker before it
    return first, last


def prev_page(p):
    """The book's markers open a page; text before the first marker in a chunk is on the earlier page."""
    return p


def quote_page(quote):
    r = page_of(quote)
    if r:
        return r
    # across a page break: split at each word boundary and look for both halves
    words = _norm(quote).split(' ')
    for k in range(3, len(words) - 2):
        a, b = ' '.join(words[:k]), ' '.join(words[k:])
        ra, rb = page_of(a), page_of(b)
        if ra and rb:
            return ra[0], rb[1]
    return None


def fmt_pages(a, b):
    return f'p. {a}' if a == b else f'pp. {a}-{b}'


def trim25(q):
    w = q.split()
    return q if len(w) <= 25 else ' '.join(w[:25]) + ' ...'


# ---------- sources ----------
def core_cards(pid):
    path = os.path.join(CORES, f'ingest-path-{pid}.md')
    if not os.path.exists(path):
        return {'version': 'not yet written', 'id': f'ing:doc:pathway-{pid}'}, {}
    text = open(path, encoding='utf-8').read()
    fm = yaml.safe_load(text.split('---')[1])
    a10 = re.search(r'### A10 Extension fields\n.*?```yaml\n(.*?)```', text, re.S).group(1)
    data = yaml.safe_load(a10)
    cards = {c['id']: c for c in data['pathway'].get('competencies', [])}
    return fm, cards


def runs_index():
    idx = {}
    for fn in os.listdir(THEORY):
        if not fn.endswith('.md'):
            continue
        p = os.path.join(THEORY, fn)
        t = open(p, encoding='utf-8').read()
        m = re.search(r'^id: (ing:doc:\S+)', t, re.M)
        if not m:
            continue
        title = re.search(r'^title: "?(.*?)"?$', t, re.M)
        summ = re.search(r'### 0\.1 Agent definition\n(?:<!--.*?-->\n)*(.+)', t)
        idx[m.group(1)] = {'title': title.group(1) if title else m.group(1), 'sha': sha12(p),
                           'summary': summ.group(1).strip() if summ else ''}
    return idx


RUNS = runs_index()


def qf_pool():
    pool = {}
    for path, fw in ((FHEQ, 'FHEQ'), (CQFW, 'CQFW')):
        t = open(path, encoding='utf-8').read()
        pre = 'qaa/fheq-2024/' if fw == 'FHEQ' else 'welsh-government/cqfw-2009/'
        for m in re.finditer(r'^- id: ' + re.escape(pre) + r'(\S+)\n((?:  .*\n)+)', t, re.M):
            body = m.group(2)
            src = re.search(r'^  source: "(.*)"', body, re.M)
            lv = re.search(r'^  level: \[?(?:fheq|cqfw):(\w+)', body, re.M)
            if src and lv:
                pool[m.group(1)] = {'fw': fw, 'level': lv.group(1), 'text': src.group(1)}
    return pool


POOL = qf_pool()


def bench_titles():
    out = {}
    for d in os.listdir(STD):
        m = re.match(r'ingest-std-qaa-(.+)-benchmarks$', d)
        if not m:
            continue
        for fn in os.listdir(os.path.join(STD, d)):
            if fn.endswith('.md'):
                t = open(os.path.join(STD, d, fn), encoding='utf-8').read(800)
                tt = re.search(r'^title: "?(.*?)"?$', t, re.M)
                if tt:
                    out[m.group(1)] = tt.group(1).replace('Subject Benchmark Statement', '').replace(':', '').strip()
    return out


BENCH = bench_titles()
VOC = {c['id']: c for c in json.load(open(VOCAB, encoding='utf-8'))['cards']}
CAPS = {c['id']: c for c in json.load(open(os.path.join(HO, 'adp-0212-capability-cards.json'), encoding='utf-8'))['cards']}
BMAP = {e['id']: e for e in json.load(open(os.path.join(HO, 'adp-0212-book-map-draft.json'), encoding='utf-8'))['entries']}


def statement_type(chunk):
    sec = chunk.rsplit('/', 1)[1].split('.')[0]
    return {'1': 'context', '2': 'nature and extent', '3': 'teaching, learning and assessment',
            '4': 'benchmark standard', '5': 'other'}.get(sec, 'other')


def subject(chunk):
    slug = chunk.split('/')[1]
    return BENCH.get(slug) or slug


def short_chunk(chunk):
    _, slug, para = chunk.split('/')
    m = re.match(r'(.+)-(\d{4})$', slug)
    name = (BENCH.get(slug) or m.group(1)) if m else slug
    return f'{name} {m.group(2) if m else ""}, {para}'.replace(' ,', ',')


# ---------- rows ----------
def theory_ref(t):
    if isinstance(t, dict):
        return '; '.join(f'{v}' for v in t.values())
    r = RUNS.get(t)
    if not r:
        PROBLEMS.append(f'theory run not found: {t}')
        return f'`{t}` (run not found)'
    return f"{r['title']} (`{t}`, {r['sha']})"


def frameworks_row(card):
    out = []
    for pf in card.get('professional', []) or []:
        for fw in pf.get('frameworks', []) or []:
            out.append(f"{fw} ({pf.get('equivalence', 'unrated')})")
    return '; '.join(out) or 'none recorded'


def book_row(oldids, extra=None):
    parts, notes = [], []
    for bx in extra or []:
        r = quote_page(bx['quote'])
        if not r:
            PROBLEMS.append(f"plan quote not in the guide: {bx['quote'][:60]}")
            continue
        if len(bx['quote'].split()) > 25:
            PROBLEMS.append(f"plan quote over 25 words: {bx['quote'][:60]}")
        parts.append(f"{bx['element']} ({fmt_pages(*r)}): \"{bx['quote']}\"")
    for oid in oldids:
        e = BMAP.get(oid)
        if not e:
            continue
        for bt in e.get('bookTopics', []):
            s = bt.get('source', {})
            q = s.get('quote')
            if not q:
                parts.append(bt.get('element', ''))
                continue
            r = quote_page(q)
            if not r:
                if ';' in q and len(q.split(';')) >= 3:
                    parts.append(f"{bt.get('element')} (draft map p. {s.get('page')}, among the chapter's keywords)")
                else:
                    notes.append(f"the draft map's quote for {bt.get('element')} (p. {s.get('page')}) is not in the guide's copy and is left out")
                    NOTFOUND.append(f'{oid}: {q[:70]}')
                continue
            pages = fmt_pages(*r)
            if ';' in q and len(q.split(';')) >= 3:
                parts.append(f"{bt.get('element')} ({pages}, among the chapter's keywords)")
                continue
            if str(s.get('page')) not in (r[0], r[1]):
                notes.append(f"{bt.get('element')}: draft map's p. {s.get('page')} corrected to {pages}")
            parts.append(f"{bt.get('element')} ({pages}): \"{trim25(q).replace('|', chr(92) + '|')}\"")
    text = '; '.join(parts) if parts else 'none in the draft book map'
    if notes:
        text += ' [' + '; '.join(notes) + '.]'
    return text, len(notes)


def bench_row(oldids, readings):
    out = []
    for oid in oldids:
        c = CAPS.get(oid)
        if not c:
            continue
        be = c.get('benchmarkEvidence', {})
        cands = be.get('candidates', [])
        if not cands:
            out.append(f"none found by adp-0212 ({be.get('status', 'no status')})")
            continue
        bits = []
        for cd in cands:
            rd = readings.get(f"{cd['chunkId']}@{oid.split('/')[1]}", readings.get(cd['chunkId']))
            if rd is None:
                PROBLEMS.append(f'no reading for {cd["chunkId"]}')
                rd = 'unread'
            bits.append(f"**{rd}**: {short_chunk(cd['chunkId'])}")
        out.append(f"{be.get('distinctChunkCount')} / {be.get('distinctTextCount')}. " + '; '.join(bits))
    return ' '.join(out) if out else 'not searched (no adp-0212 card).'


def other_authors(theory, seen):
    out = []
    for t in theory or []:
        if isinstance(t, dict):
            continue
        r = RUNS.get(t)
        if not r:
            continue
        if t in seen:
            out.append(f"{r['title']} (run above)")
            continue
        seen.add(t)
        s = re.sub(r'\s*\[D:[^\]]*\]', '', r['summary'])
        first = re.split(r'(?<=\.)\s', s, maxsplit=1)[0]
        out.append(f"{r['title']}: {first} (`{t}`, {r['sha']}, from the run's agent definition)")
    return ' '.join(out) or 'none held yet'


# ---------- build ----------
def build(pid, write):
    plan = yaml.safe_load(open(os.path.join(PLANS, f'{pid}.yaml'), encoding='utf-8'))
    if plan.get('dataOnly'):
        sys.exit(f'{pid}: a data-only plan; its card file is hand-written and is not built')
    fm, ccards = core_cards(pid)
    name = plan['name']
    seen = set()
    vic_records = []
    corrections = 0
    lines = []
    A = lines.append
    newids = [c['new'] for c in plan['cards']]
    assert newids == ORDER, newids
    for c in plan['cards']:
        assert c['new'] in LEVEL
    crosswalk = []
    for c in plan['cards']:
        olds = ([c['old']] if c.get('old') else []) + (c.get('merged') or [])
        crosswalk.append(f"{', '.join(o.split('/')[1] for o in olds) or 'new'} to {c['new']}")

    # front matter
    A('---')
    A(f'document:  card integration: {name}')
    A(f"core:      `pathways/ingest-path-{pid}.md` {fm['version']} (`{fm['id']}`), A10 `competencies`, joined by card id")
    A('owner:     adp ing (drafts); `path` holds the cards (nts); the model\'s author rules them (D-0058)')
    revs = plan.get('revisions', [])
    vline = ''.join(f"{r['version']}, {r['date']}, {r['time']}, {r['what']} (ing {r['note']}); " for r in reversed(revs))
    A(f"version:   {vline}0.1.0, {plan['date']}, {plan['time']}, created from the golden template (D-ing-0061; ing {plan['note']})")
    A('status:    working draft; not ingested; not a record')
    A('---')
    A('')
    A(f'# {name}: the cards in context')
    A('')
    A(f"D-ing-0055 keeps each card in the core as the pathway template defines it and puts here what lies beyond the template: each card's vocabulary, the book topics under it, the benchmark evidence, the crosswalk to other frameworks, the pedagogy beneath it and how other authors describe it, then the vocabulary across the cards, the tiers from two directions and a table of correspondences. This file speaks to the core; it is not part of it. Its shape is the golden template (`ing-cards-template.md`, D-ing-0061).")
    A('')
    A("Sources: the cards and their theory and frameworks from the core's A10; vocabulary from `ing-card-vocabulary.json`; book topics from adp-0212's draft book map (`mta-nts-ho-adp-nts-0007`), every quote found in the guide's Markdown copy by script and its page recomputed from the copy's page markers; benchmark evidence from adp-0212's card drafts (counts are passages / texts, of 54), each extract read by ing; other authors from META's INGEST runs in UNI's `library/ingested/theory/`, each with its SHA-256 prefix, given from the run's agent definition, never quoting the author. Quotations from the guide stay within 25 words.")
    A('')
    A('How the benchmark evidence is read: **skill** where the passage describes the learner doing the capability; **theme** where the practice appears only as an item in a list of attributes, methods or assessment types.')
    A('')
    A('## 1. The cards')
    A('')
    A("Nine cards, three at each tier, ordered within each tier and across the tiers from the concrete towards the metacognitive (D-ing-0060). The letter is the tier note: **i**, introduced, the Introductory course; **d**, developed, the Intermediate course; **e**, extended, the Advanced course. Section 5 gives each card's kind of knowledge and indicative level.")
    A('')
    unsearched = []
    for c in plan['cards']:
        tierword = TIER[c['new'][0]][0]
        olds = ([c['old']] if c.get('old') else []) + (c.get('merged') or [])
        base = ccards.get(c['old']) if c.get('old') else None
        if c.get('old') and not base:
            PROBLEMS.append(f"old card not in core A10: {c['old']}")
        stmt = c.get('statement') or (base or {}).get('statement') or VOC.get(c.get('old'), {}).get('statement')
        A(f"### `{pid}/{c['new']}` ({tierword}) {stmt}")
        A('')
        A('| | |')
        A('|---|---|')
        rows = c.get('rows') or {}
        v = {}
        for o in olds:
            vc = VOC.get(o, {})
            for k in ('verbs', 'measures', 'keywords'):
                v.setdefault(k, [])
                v[k] += [x for x in vc.get(k, []) if x not in v[k]]
        A(f"| Verbs | {rows.get('Verbs') or ', '.join(v.get('verbs', [])) or 'none'} |")
        A(f"| Measures | {rows.get('Measures') or ', '.join(v.get('measures', [])) or 'none'} |")
        A(f"| Keywords | {rows.get('Keywords') or '; '.join(v.get('keywords', [])) or 'none'} |")
        if rows.get('Book topics'):
            bt = rows['Book topics']
        else:
            bt, n = book_row(olds, c.get('book'))
            corrections += n
        A(f'| Book topics | {bt} |')
        if rows.get('Benchmark evidence'):
            be = rows['Benchmark evidence']
        else:
            be = bench_row(olds, plan.get('readings', {}))
        if be.startswith('not searched'):
            unsearched.append(c['new'])
        A(f'| Benchmark evidence | {be} |')
        theory = []
        for o in olds:
            for t in (ccards.get(o) or {}).get('theory', []) or []:
                if t not in theory:
                    theory.append(t)
        A(f"| Pedagogy | {rows.get('Pedagogy') or '; '.join(theory_ref(t) for t in theory) or 'none recorded'} |")
        fws = '; '.join(frameworks_row(ccards[o]) for o in olds if o in ccards)
        A(f"| Frameworks | {rows.get('Frameworks') or fws or 'none recorded'} |")
        A(f"| Other authors | {rows.get('Other authors') or other_authors(theory, seen)} |")
        if c.get('note'):
            A(f"| Note | {c['note']} |")
        A('')

    A('## 2. Vocabulary')
    A('')
    A("Each card's own verbs, measures and keywords are in its table (section 1). This section reads the vocabulary across the cards, in the statements other sources use it in, and in the national level descriptors.")
    A('')
    A('### 2a. Across the cards')
    A('')
    for b in plan['across']:
        A(f'- {b}')
    A('')
    A('### 2b. Verbs in context (D-ing-0058)')
    A('')
    A("Every verb is captured with the statement it is used in, and with how that statement relates the pathway to the subject, discipline or vocational area the source describes. The cards' own verbs sit in their capability statements, generic to any subject (section 1). The benchmark verbs are below, from the extracts adp-0212 chose; statement type is inferred from the chunk's section number, the subject is the benchmark's, HECoS codes wait for the benchmarks' subject tags, and the verbs, reading and relation are ing's. Data: `verbs-in-context.json`.")
    A('')
    A('| Card | Verbs | Statement | Statement type | Subject | Read as | How it relates the pathway to the subject |')
    A('|---|---|---|---|---|---|---|')
    old2new = {}
    for c in plan['cards']:
        for o in ([c['old']] if c.get('old') else []) + (c.get('merged') or []):
            old2new[o] = c['new']
    nrows = 0
    for c in plan['cards']:
        for o in ([c['old']] if c.get('old') else []) + (c.get('merged') or []):
            for cd in CAPS.get(o, {}).get('benchmarkEvidence', {}).get('candidates', []):
                vv = plan.get('vic', {}).get(f"{cd['chunkId']}@{o.split('/')[1]}") or plan.get('vic', {}).get(cd['chunkId'])
                if not vv:
                    PROBLEMS.append(f'no verbs-in-context for {cd["chunkId"]}')
                    continue
                st = statement_type(cd['chunkId'])
                sb = subject(cd['chunkId'])
                rd = plan['readings'].get(f"{cd['chunkId']}@{o.split('/')[1]}", plan['readings'].get(cd['chunkId'], 'unread'))
                A(f"| {c['new']} | {', '.join(vv['verbs']) or '(none)'} | \"{cd['extract'].replace('|', chr(92) + '|')}\" | {st} | {sb} | {rd} | {vv['relation']} |")
                nrows += 1
                vic_records.append({'pathway': pid, 'card': f"{pid}/{c['new']}", 'formerCard': o, 'source': cd['chunkId'],
                                    'statementType': st, 'statement': cd['extract'], 'verbs': vv['verbs'], 'subject': sb,
                                    'hecos': None, 'readAs': rd, 'relation': vv['relation']})
    if nrows == 0:
        A('| | | none: no card here has adp-0212 extracts | | | | |')
    A('')
    A(plan['vicSummary'])
    A('')
    A('### 2c. qualification-frameworks')
    A('')
    A(f"The national level descriptors, recorded beside the cards, never as their anchor: a card belongs to a course tier, not a qualification level (Abbott, 10:31). The statements below are those that speak to {plan['practiceNoun']}, quoted from META's runs of the FHEQ (`std:doc:qaa-fheq-2024-framework`, SHA-256 prefix {sha12(FHEQ)}) and the CQFW (`std:doc:welsh-government-cqfw-2009-framework`, {sha12(CQFW)}), each with its verbs and how it relates to the practice (D-ing-0058). {plan['qfIntro']} The loose fit of tiers to levels is ing's reading.")
    A('')
    A(f"| Level | Framework and statement | Verbs | How it relates to {plan['practiceNoun']} | Loosely, the tier |")
    A('|---|---|---|---|---|')
    for r in plan['qf']:
        s = POOL.get(r['id'])
        if not s:
            PROBLEMS.append(f"qf id not in pool: {r['id']}")
            continue
        A(f"| {s['fw']} {s['level']} | `{r['id']}` \"{s['text']}\" | {r['verbs']} | {r['relation']} | {r['tier']} |")
    A('')
    A("The core's A11 carries the full ladder, levels 3 to 8, with the metacognitive stance at each.")
    A('')
    A('## 3a. Tier statements and the kinds of knowledge')
    A('')
    A("A loosely level-based set of statements about the practice at each tier, read through Anderson and Krathwohl's knowledge dimension (`ing:doc:bloom-anderson-krathwohl-2001`, " + RUNS.get('ing:doc:bloom-anderson-krathwohl-2001', {}).get('sha', '?') + "): factual knowledge (the terms and details), conceptual knowledge (how they fit together: models, principles), procedural knowledge (how to do it, and the criteria for choosing which method) and metacognitive knowledge (knowledge of cognition and of one's own), on a continuum from concrete to abstract. Factual and conceptual together are what Biggs and Marzano call declarative knowledge, knowing that; Biggs calls knowledge put to work functioning knowledge (`ing:doc:constructive-alignment-biggs-1996`); Marzano and Kendall place metacognition and the self-system above the cognitive system (`ing:doc:new-taxonomy-marzano-kendall-2007`, " + RUNS.get('ing:doc:new-taxonomy-marzano-kendall-2007', {}).get('sha', '?') + "). The statements are ing's, built up from the cards and the knowledge models; the classification is ing's reading. Section 4a gives the pathway model's own tier text, from the other direction (D-ing-0059).")
    A('')
    A('| Tier | Statement about the practice | Knowledge type | Cognitive process | What changes |')
    A('|---|---|---|---|---|')
    for r in plan['tierStatements']:
        A(f"| {r['tier']} | {r['statement']} | {r['type']} | {r['process']} | {r.get('change', '')} |")
    A('')
    A(f"**How the learner moves to mastery.** {plan['mastery']}")
    A('')
    # 4a
    A('## 4a. The tier map: the pathway model as used')
    A('')
    if not plan.get('tierMapDraft'):
        A("The tier map of the pathway model as used, imported here so the tiers sit in one place with the cards (D-ing-0059). It comes from a different direction from section 3a: section 3a is ing's, built up from the cards and the knowledge models; this is the model's design as used, built down from the guide. The two are kept side by side and not merged for now.")
        A('')
    A('This file is the first of three parts: the Introductory course comes first, with Intermediate and Advanced to follow (ing N-0117, N-0122).')
    A('')
    if plan.get('tierMapDraft'):
        d = plan['tierMapDraft']
        A("The pathway model has no tier map entry or catalogue file for this pathway yet. The text below is ing's draft in the map's own shape, for the model's author to rule; it is not the model as used.")
        A('')
        A("**Draft tier focus**")
        A('')
        A('| Tier | Focus | Course | Status |')
        A('|---|---|---|---|')
        for tier in ('Introductory', 'Intermediate', 'Advanced'):
            A(f"| {tier} | {d['focus'][tier]} | not yet set | drafted |")
        A('')
        A("**Draft tier text**")
        A('')
        A('\n'.join('> ' + l if l else '>' for l in d['text'].strip().split('\n')))
        A('')
    else:
        ptm = open(os.path.join(MIRROR, 'pathway-tier-mapping.md'), encoding='utf-8').read()
        commit = re.search(r'Generated from commit: `(\w+)`', ptm).group(1)
        A(f"Sources: `pathway-tier-mapping.md` (canonical `docs/curriculum/pathway-tier-mapping.md`, Draft v3, \"for SME review\") and `catalogue_pathways_{pid}.json`, both read from the mirror of commit {commit}, which is a copy and not evidence for the repo. The map's text is quoted as it stands, its dashes and arrows included.")
        A('')
        A("**The catalogue's tier focus**")
        A('')
        A('| Tier | Focus | Course | Status |')
        A('|---|---|---|---|')
        cat = json.load(open(os.path.join(MIRROR, f'catalogue_pathways_{pid}.json'), encoding='utf-8'))
        for t in cat['tiers']:
            A(f"| {t['displayName']} | {t.get('focus')} | {t.get('courseSlug') or 'not yet set'} | {t.get('status')} |")
        A('')
        sec = re.search(r'^## (Pathway (\d+) — [^\n]+)\n(.*?)(?=^---\n|^## Pathway )', ptm[ptm.index(f"## Pathway {plan['pathwayNo']} "):], re.S | re.M)
        A(f"**The map's text ({sec.group(1).replace(' — ', ', ')})**")
        A('')
        body = sec.group(3).strip('\n')
        body = '\n'.join(l for l in body.split('\n') if not l.startswith('**Voice-band anchor:**'))
        body = re.sub(r'\n{2,}', '\n\n', body).strip()
        A('\n'.join('> ' + l if l else '>' for l in body.split('\n')))
        A('')
        A("The map's voice-band anchor governs the lesson register and is left out here.")
        A('')
    A(f"**Where the two directions differ** (ing's reading, recorded, not resolved): {plan['differ']}")
    A('')
    # 5
    A('## 5. Table of correspondences')
    A('')
    A("Each card with its tier, its kind of knowledge (Anderson and Krathwohl, section 3a) and a loose indicative level, the tiers overlapping like competency bands: card 1 of a tier at the lowest level of its band, card 3 at the highest (Abbott, 12:05). The level is an indication, never the card's anchor: a card belongs to its tier (N-0117). Beside it, the qualification-framework statements at that level, by id and a short extract.")
    A('')
    A('| Card | Tier | Statement | Kind of knowledge | Indicative level | Qualification frameworks at that level |')
    A('|---|---|---|---|---|---|')
    for c in plan['cards']:
        qs = []
        for q in c.get('qf', []):
            s = POOL.get(q['id'])
            if not s:
                PROBLEMS.append(f"qf id not in pool: {q['id']}")
                continue
            if _norm(q['extract']) not in _norm(s['text']):
                PROBLEMS.append(f"extract not in statement {q['id']}: {q['extract']}")
            lvl = 'L' + s['level']
            if lvl != LEVEL[c['new']] and not q.get('beyond'):
                PROBLEMS.append(f"{c['new']}: {q['id']} is {lvl}, card is {LEVEL[c['new']]}")
            pre = 'beyond the band, ' if q.get('beyond') else ''
            qs.append(f"{pre}{s['fw']} {s['level']} `{q['id']}`: \"{q['extract']}\"")
        A(f"| {c['new']} | {TIER[c['new'][0]][1]} | {c['short']} | {c['knowledge']} | {LEVEL[c['new']]} | {'; '.join(qs) or 'none at that level'} |")
    A('')
    A(f"What the frameworks add (ing's reading): {plan['qfAdd']}")
    A('')
    A('## 6. For review')
    A('')
    items = list(plan.get('review', []))
    if unsearched:
        items.append(f"Benchmark evidence not yet searched for {', '.join(unsearched)}: the practice searcher could do it once found (J-ing-0003, RJ-0111).")
    if corrections:
        items.append(f"{corrections} page corrections to adp-0212's draft book map are recorded in the card tables, for `path`'s guide map, which nts holds.")
    items.append('The core, the card vocabulary and the database still carry the old ids until the core is renumbered (D-ing-0060); the crosswalk is in the change notes.')
    for i, it in enumerate(items, 1):
        A(f'{i}. {it}')
    A('')
    A('---')
    A('')
    A('## Change notes')
    for r in reversed(plan.get('revisions', [])):
        A(f"- {r['version']}: {r['date']}, {r['time']}: {r['what']} (ing {r['note']}).")
    A(f"- 0.1.0: {plan['date']}, {plan['time']}: created from the golden template (D-ing-0061; ing {plan['note']}). Crosswalk from the core's ids (D-ing-0060): " + '; '.join(crosswalk) + '.')
    out = '\n'.join(lines) + '\n'
    print(f'{pid}: {len(out)} chars, {nrows} verbs-in-context rows, {corrections} page corrections, unsearched {unsearched}')
    for p in PROBLEMS:
        print('PROBLEM:', p)
    for p in NOTFOUND:
        print('quote not found (left out):', p)
    if write:
        if PROBLEMS:
            print('not written: problems above')
            sys.exit(1)
        open(os.path.join(HERE, f'ing-cards-{pid}.md'), 'w', encoding='utf-8').write(out)
        vic = json.load(open(VIC, encoding='utf-8'))
        vic['records'] = [r for r in vic['records'] if r['pathway'] != pid] + vic_records
        json.dump(vic, open(VIC, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('written')


if __name__ == '__main__':
    build(sys.argv[1], '--write' in sys.argv)
