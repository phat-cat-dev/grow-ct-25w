#!/usr/bin/env python3
"""model_build.py 0.2.0 (std, 4 October 2026; D-std-0018): builds a `standards/model` ingest document from its content
module (<library>/ingested/standards/<doc>/run-src/model_content.py) and the held text (<library>/txt/<name>.norm.txt),
on the model template 0.2.0-draft, and runs checks MD-1 to MD-11 with ST-5, ST-6 and ST-13 as they apply.
0.2.1: `labelPara` (was `para`, which clashed with the paraphrase); S7 targets quoted; PUBLISHED, REVISED and SUPERSEDES from the module; statement `readFrom`; groups' `ring` and per-axis counts; M5 `rel`; moods `function` and `noun-phrase`; conditionType `competency`; both checked. 0.2.0: everything specific to one model is in its content module (the content contract is below and in the template's
"Content module" section); axes (perspectives or facets), groups (an inner ring: stages or categories), labels the text
layer scrambles (`labelInText: False`), optional open segments and an optional PSF table.
Usage: model_build.py <doc folder> --stamp "<YYYY-MM-DD HH:MM>" [--version 0.1.0] [--check]
  --check   build in memory and report; write nothing

Content contract (names in the module; * optional):
  NAME DOC ID PFX TITLE SERIES PDF_SHA THEORY* EDITION DATES_OTHER MODEL_KIND FIGURE AXES GROUPS* USE S2
  COMPONENTS OPEN* OPEN_REASON* OPEN_INSTR* STEMS* STATEMENTS CONDS SECTOR_DEFAULT S6 S7 PSF* M5_INFERRED
  AGENTDEF SUMMARY S3 EXCLUDED BCONCEPTS B4 B5 PART_E D3 CHANGE"""
import os, sys, re, json, hashlib, importlib.util, argparse, shutil
import yaml

TOOLS = os.path.dirname(os.path.abspath(__file__))
UNI = os.path.abspath(os.path.join(TOOLS, '../../../../../../..'))
LIB = os.environ.get('LIBRARY') or os.path.join(os.path.dirname(UNI), 'wkspc2601-library')
STD = os.path.join(LIB, 'ingested/standards')
TEMPLATE_V = '0.3.0-draft'
BUILDER_V = '0.2.1'
ap = argparse.ArgumentParser(); ap.add_argument('doc'); ap.add_argument('--stamp', required=True)
ap.add_argument('--version', default='0.1.0'); ap.add_argument('--check', action='store_true')
a = ap.parse_args()
DOCDIR = os.path.join(STD, a.doc)
spec = importlib.util.spec_from_file_location('mc', os.path.join(DOCDIR, 'run-src', 'model_content.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
g = lambda k, d=None: getattr(C, k, d)
norm = open(os.path.join(LIB, 'txt', C.NAME + '.norm.txt'), encoding='utf-8').read()
RAW = hashlib.sha256(open(os.path.join(LIB, 'txt', C.NAME + '.txt'), 'rb').read()).hexdigest()
NORM = hashlib.sha256(norm.encode('utf-8')).hexdigest()
q = lambda s: json.dumps(s, ensure_ascii=False)
errors, notes = [], []
def err(m): errors.append(m)

# ---- spans
def find(src, after=0, para=False, what='text'):
    i = norm.find(src, after)
    if i < 0: err(f'MD-2 {what} not in held text: {src[:70]}'); return (0, 0)
    if para and not (norm[max(0, i - 2):i] in ('\n\n', '') or i == 0) :
        err(f'MD-2 label does not start a paragraph: {src}')
    if para and norm[i + len(src):i + len(src) + 2] not in ('\n\n', '\n'):
        err(f'MD-2 label does not end a paragraph: {src}')
    return (i, i + len(src))

# ---- our-words copy check (nine words)
def words(s): return re.findall(r"[a-z0-9']+", s.lower().replace('’', "'"))
NW = words(norm); GRAMS = {tuple(NW[i:i + 9]) for i in range(len(NW) - 8)}
def copycheck(where, s):
    if not s or s.startswith('not-applicable'): return
    w = words(s)
    for i in range(len(w) - 8):
        if tuple(w[i:i + 9]) in GRAMS: err(f'MD-8 nine-word copy in {where}: "{" ".join(w[i:i+9])}"'); return
BANNED = ['benchmark', 'degree programme', 'graduates will', 'guidance', 'educators', 'providers', 'students should',
          'framework', 'advance he', C.TITLE.lower()]
def bencheck(where, s):
    if s.startswith('not-applicable'): return
    if not re.search(r'\byou(r)?\b', s, re.I): err(f'MD-9 no second person in {where}')
    for b in BANNED:
        if b in s.lower(): err(f'MD-9 banned "{b}" in {where}')

# ---- axes and groups
AXES = C.AXES; AXIS_IDS = {x['id'] for x in AXES}
GROUPS = g('GROUPS', []) or []; GROUP_IDS = {x['id'] for x in GROUPS}
for x in AXES:
    if not re.match(r'^(perspective|facet):[a-z0-9-]+$', x['id']): err(f"MD-3 axis id {x['id']}")
slug = lambda i: i.split(':', 1)[1]

# ---- components
comps, labspans = [], []
for c in C.COMPONENTS:
    if c['axis'] not in AXIS_IDS: err(f"MD-3 axis {c['axis']} not in AXES ({c['slug']})")
    if c.get('group') and c['group'] not in GROUP_IDS: err(f"MD-3 group {c['group']} not in GROUPS ({c['slug']})")
    if c.get('labelInText', True):
        after = norm.find(c['anchor']) + len(c['anchor']) if c.get('anchor') else 0
        s, e = find(c['label'], after, para=c.get('labelPara', True), what='label')
        labspans.append((s, e, c['label'])); span = (s, e)
    else:
        span = None
        if not c.get('readFrom'): err(f"MD-2 label not in text needs readFrom: {c['slug']}")
    exp = []
    for src, link, page in c['explained']:
        es, ee = find(src, what='explainedBy')
        if link not in ('stated', 'inferred'): err(f'MD-4 link {link}')
        exp.append(dict(span=(es, ee), source=src, link=link, page=page))
    if not exp: err(f"MD-4 no explainedBy: {c['slug']}")
    if c['ctype'] not in ('culture', 'relationship', 'practice', 'structure', 'process', 'service', 'disposition', 'environment', 'competency'): err(f"conditionType {c['ctype']} ({c['slug']})")
    c['conds'] = list(dict.fromkeys(c['conds']))   # a merge may leave a theme twice
    cid = f"{C.PFX}/{slug(c['axis'])}.{c['slug']}"
    comps.append(dict(c, id=cid, span=span, exp=exp))
ls = sorted(labspans)
for i in range(1, len(ls)):
    if ls[i][0] < ls[i - 1][1]: err(f'MD-2 label spans overlap: {ls[i][2]}')
ids = [c['id'] for c in comps]
if len(set(ids)) != len(ids): err('duplicate component id')
for c in comps:
    if c.get('same') and f"{C.PFX}/{c['same']}" not in ids: err(f"sameLabelAs does not resolve: {c['same']}")

# ---- statements
STEMS = g('STEMS', {}) or {}
stem_at = {k: find(v, what='stem') for k, v in STEMS.items()}
stmts = []
for t in C.STATEMENTS:
    after = stem_at[t['stem']][0] if t.get('stem') else 0
    s, e = find(t['src'], after, what='statement')
    for v in t['verbs']:
        if not re.search(r'(?<![\w])' + re.escape(v) + r'(?![\w])', t['src']): err(f"verb {v} not in {t['n']}")
    lead = STEMS.get(t.get('stem'), '') if t.get('stem') else t.get('lead', '')
    if t['force'] == 'must' and not re.search(r'\brequires?\b|\bmust\b|\bneeds? to\b|\bnecessitates\b|\bessential\b|\brequired\b|\bresponsibility\b', t['src'] + ' ' + lead, re.I):
        err(f"ST-6 must without an obliging word: {t['n']}")
    if t['force'] == 'should' and 'should' not in t['src'] and not t.get('fnote'): err(f"ST-6 should unmarked: {t['n']}")
    if t['force'] == 'describes' and t.get('fnote') is None: t['fnote'] = 'states without obliging'
    if t.get('axis') and t['axis'] not in AXIS_IDS: err(f"statement axis {t['axis']} ({t['n']})")
    if t['mood'] not in ('declarative', 'imperative', 'entitlement', 'gerund', 'infinitive', 'function', 'noun-phrase'): err(f"mood {t['mood']} ({t['n']})")
    stmts.append(dict(t, id=f"{C.PFX}/{t['n']}", span=(s, e)))
if len({t['id'] for t in stmts}) != len(stmts): err('duplicate statement id')

OPEN = g('OPEN', []) or []
openrec = find(C.OPEN_REASON, what='open reason') if OPEN else None
PSF = g('PSF')
psf_lead = find(PSF['lead'], what='PSF lead') if PSF and PSF.get('lead') else None
psf_fel = find(PSF['fellowship'], what='fellowship') if PSF and PSF.get('fellowship') else None
S2 = C.S2
scope_s = find(S2['statedScope'], what='scope') if S2.get('statedScope') else None

# ---- PSF ids resolve (MD-7)
psfdoc = open(os.path.join(STD, 'ingest-std-advancehe-psf-dimensions-2023-framework', 'ingest-std-advancehe-psf-dimensions-2023-framework.md'), encoding='utf-8').read()
for code in (PSF or {}).get('codes', []):
    if f'- id: advancehe/psf-dimensions-2023/{code}\n' not in psfdoc: err(f'MD-7 PSF {code} does not resolve')

# ---- practice themes (MD-6)
carried = {}
for c in comps:
    if not c['conds']: err(f"MD-6 no practice theme: {c['id']}")
    for th in c['conds']:
        if th not in C.CONDS: err(f"MD-6 {th} not in M6 ({c['id']})")
        carried.setdefault(th, []).append(c['id'])
for th in C.CONDS:
    if th not in carried: err(f'MD-6 {th} carried by no component')
    if not re.match(r'^theme:[a-z0-9-]+$', th): err(f'MD-6 bad theme id {th}')
S6IDS = {x['id'] for x in C.S6}
for c in comps:
    for th in c.get('sector', C.SECTOR_DEFAULT):
        if th not in S6IDS: err(f"MD-6 sector theme {th} not in S6 ({c['id']})")

# ---- copy and beneficiary checks
for c in comps:
    for k in ('about', 'para', 'prac', 'ben', 'aaw', 'aad', 'holds', 'absent', 'steer'):
        if not c.get(k): err(f"MD-5 empty {k}: {c['id']}")
        copycheck(f"{c['id']}.{k}", c.get(k, ''))
    for x in c['signs']: copycheck(f"{c['id']}.signs", x)
    if not 2 <= len(c['signs']) <= 4: err(f"MD-5 signs count {c['id']}")
    bencheck(f"{c['id']} forBeneficiary", c['ben'])
for t in stmts:
    for k in ('about', 'para', 'prac', 'ben', 'aaw', 'aad'): copycheck(f"{t['id']}.{k}", t[k])
    bencheck(f"{t['id']} forBeneficiary", t['ben'])
for x in (C.AGENTDEF, C.SUMMARY): copycheck('Part 0', x)
for b in C.BCONCEPTS:
    copycheck(f"B1 {b['slug']}", b['defn'])
    if b['form'].lower() not in norm.lower(): err(f"B2a form not in text: {b['form']}")

# ================================================================ write
nseg = len(comps); nopen = len(OPEN)
segs = {x['id']: sum(1 for c in comps if c['axis'] == x['id']) for x in AXES}
opens = {x['id']: sum(1 for o in OPEN if o['axis'] == x['id']) for x in AXES}
nscr = sum(1 for c in comps if c["span"] is None)
nper = sum(1 for x in AXES if x['id'].startswith('perspective:')); nfac = len(AXES) - nper
out = []; w = out.append
E = g('EDITION', 'digital edition, 2024')
w(f'''---
id: {C.ID}
title: {q(C.TITLE)}
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: {C.MODEL_KIND}
series: {C.SERIES}
axes: {{ perspectives: {nper}, facets: {nfac}, groups: {len(GROUPS)}, segments: {nseg}, openSegments: {nopen}, labelsNotInText: {nscr} }}
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: {q(E)}
published: {g('PUBLISHED', 2024)}   # no date printed; from the PDF metadata (Part E)
revised: {q(g('REVISED', 'none-stated'))}   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: {q(g('SUPERSEDES', 'none-stated'))}
heldText: {{ method: sha256-bytes, raw: {RAW}, normalised: {NORM} }}
original: {{ method: sha256-bytes, pdf: {C.PDF_SHA}, held: "library pdf/{C.NAME}.pdf" }}
licence: "no licence or copyright notice printed; © Advance HE assumed. Held by Abbott's permission (4 October 2026, 05:03; D-std-0019)"
agentUse: source-and-rephrased   # `label` and `source` are the issuer's words for language analysis; private, never published (D-std-0014); agents phrase from our fields
parts:
  S: full
  M: full
  B: full
  C: "not-applicable: the model sets conditions, not a procedure"
pins: {{ structure: 0.13.0-draft, template: 0.8.0-draft, model: {TEMPLATE_V}, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; model template {TEMPLATE_V}; std (Claude Code, META Project); builder model_build.py {BUILDER_V}
passes:
  P1: "{a.stamp[:10]}, std"
  P2: "skipped: read direct from the issuer's PDF; the series page is wanted (D3)"
  P3: open
version: {a.version}
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards-model.md {TEMPLATE_V} on wpk-0016-ingest-pd-template-standards.md 0.8.0-draft; built by model_build.py {BUILDER_V} from run-src/model_content.py -->
# {C.TITLE}

> The issuer's text is held beside this document in the library (`txt/{C.NAME}.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
{C.AGENTDEF}

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
{C.SUMMARY}

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: {q(C.TITLE)}
series: "Advance HE Student Success Frameworks"
edition: {q(E)}
dates:
  published: {g('PUBLISHED', 2024)}   # not printed; PDF metadata
  other: {q(C.DATES_OTHER)}
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: {q(S2['governs'])}
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: {q(S2['providers'])}
whoMustUse: {q(S2['whoMustUse'])}
howUsed: {q(S2['howUsed'])}
doesNot: {q(S2.get('doesNot', 'none-stated'))}
beneficiary: the student
''')
if scope_s:
    w(f"statedScope: {q(S2['statedScope'])}\nstatedScopeLocator: {q('D1, p. ' + str(S2['scopePage']))}\nstatedScopeSpan: {{ start: {scope_s[0]}, end: {scope_s[1]} }}\n")
else:
    w('statedScope: none-stated\n')
w('''statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
''')
for num, order, ct, par, head, gloss, pg, rf in C.S3:
    w(f'  - {{ number: {q(num)}, order: {order}, componentType: {ct}, parent: {q(par)}, heading: {q(head)}, gloss: {q(gloss)}, pages: {q(pg)}, readFrom: {q(rf)} }}\n')
w('excluded:\n')
for num, head, kind, pg in C.EXCLUDED:
    w(f'  - {{ number: {q(num)}, heading: {q(head)}, kind: {q(kind)}, pages: {q(pg)} }}\n')
w('```\n\n### S4 Statements\n<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->\n```yaml\n')
if not stmts: w('[]   # no obliging or directing line in the held text\n')
for t in stmts:
    w(f'''- id: {t['id']}
  locator: {{ number: {q(t['n'])}, heading: {q(t.get('heading', ''))}, page: {t['page']} }}
  span: {{ start: {t['span'][0]}, end: {t['span'][1]} }}
  source: {q(t['src'])}
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: {t.get('stem') or 'none'}
  statementType: {t['stype']}
  force: {t['force']}   # {t['fnote']}
  level: none
  perspective: {t.get('axis') or 'none'}
  mood: {t['mood']}
  readFrom: {q(t.get('readFrom', 'text layer'))}
  appliesTo: {q(t.get('appliesTo', C.TITLE.lower()))}
  addressee: {t['addr']}
  verbs: {q(t['verbs'])}
  about: {q(t['about'])}
  themes: {q(t.get('themes', ['none']))}
  paraphrase: {q(t['para'])}
  audience: {'both' if not t['ben'].startswith('not-applicable') else 'practitioner'}
  subjects: inherited
''')
w('```\n\n### S4a Audience versions\n<!-- label: both; status: drafted; basis: primary -->\n```yaml\n')
if not stmts: w('[]\n')
for t in stmts:
    w(f'''- statement: {t['id']}
  forPractitioner: {{ text: {q(t['prac'])}, rewrite: full, force: {t['force']}, status: drafted }}
  forBeneficiary: {{ text: {q(t['ben'])}, rewrite: full, force: {t['force']}, status: drafted }}
  author-agent-written: {q(t['aaw'])}
  author-agent-dialogue: {q(t['aad'])}
''')
w('''```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels: []   # the model defines and cites no level
crosswalks: []   # its stated link to the PSF 2023, if any, is in M5
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary. Sector themes; the practice themes are in M6. -->
```yaml
''')
for x in C.S6:
    w(f"- {{ id: {x['id']}, role: {x['role']}, carriedIn: {q(x['carriedIn'])}, basis: {q(x['basis'])} }}\n")
w('```\n\n### S7 Relations\n<!-- label: both; status: drafted; basis: primary -->\n```yaml\n')
for x in C.S7:
    w(f"- {{ rel: {x['rel']}, target: {q(x['target'])}, note: {q(x['note'])} }}\n")
w('''```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: 2024
lastReviewed: none-stated
reviewCycle: none-stated
consultation: none-stated
replacedBy: none
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched (Part E).

## Part M Model

### M1 Model shape
<!-- label: source; status: drafted; basis: primary -->
```yaml
''')
F = C.FIGURE
w(f"figure: {{ form: {F['form']}, pages: {q(F['pages'])}, readFrom: {q(F['readFrom'])} }}\naxes:\n")
for x in AXES:
    extra = f", note: {q(x['note'])}" if x.get('note') else ''
    w(f"  - {{ id: {x['id']}, label: {q(x['label'])}, page: {x['page']}, segments: {segs[x['id']]}, openSegments: {opens[x['id']]}{extra} }}\n")
if GROUPS:
    w('groups:\n')
    for gr in GROUPS:
        gc = sum(1 for c in comps if c.get('group') == gr['id'])
        per = {x['id']: sum(1 for c in comps if c.get('group') == gr['id'] and c['axis'] == x['id']) for x in AXES}
        per = {k: v for k, v in per.items() if v}
        w(f"  - {{ id: {gr['id']}, kind: {gr['kind']}, label: {q(gr['label'])}, axis: {gr.get('axis') or 'all'}, ring: {gr.get('ring', 'inner')}, segments: {gc}, perAxis: {q(per)}, readFrom: {q(gr.get('readFrom', 'figure image'))} }}\n")
else:
    w('groups: none\n')
w(f"use: {q(C.USE)}\n```\n\n### M2 Components\n<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->\n```yaml\n")
order = {}
for c in comps:
    order[c['axis']] = order.get(c['axis'], 0) + 1
    sp = f"{{ start: {c['span'][0]}, end: {c['span'][1]} }}" if c['span'] else f"none   # {c.get('readFrom')}"
    w(f'''- id: {c['id']}
  label: {q(c['label'])}
  span: {sp}
  position: {{ axis: {c['axis']}, group: {c.get('group') or 'none'}, order: {order[c['axis']]}, page: {c['page']} }}
  explainedBy:
''')
    for x in c['exp']:
        w(f"    - {{ span: {{ start: {x['span'][0]}, end: {x['span'][1]} }}, source: {q(x['source'])}, link: {x['link']}, page: {x['page']} }}\n")
    w(f'''  conditionType: {c['ctype']}
  actor: {c['actor']}
  about: {q(c['about'])}
  paraphrase: {q(c['para'])}
  themes: {q(c['conds'] + c.get('sector', C.SECTOR_DEFAULT))}
  sameLabelAs: {(C.PFX + '/' + c['same']) if c.get('same') else 'none'}
''')
w('```\n\n### M2a Component audience versions\n<!-- label: both; status: drafted; basis: primary -->\n```yaml\n')
for c in comps:
    w(f'''- component: {c['id']}
  forPractitioner: {{ text: {q(c['prac'])}, rewrite: full, force: describes, status: drafted }}
  forBeneficiary: {{ text: {q(c['ben'])}, rewrite: full, force: describes, status: drafted }}
  author-agent-written: {q(c['aaw'])}
  author-agent-dialogue: {q(c['aad'])}
''')
w('```\n\n### M3 Conditions\n<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->\n```yaml\n')
for c in comps:
    w(f'''- component: {c['id']}
  theme: {c['conds'][0]}
  holdsWhen: {q(c['holds'])}
  signs: {q(c['signs'])}
  absentWhen: {q(c['absent'])}
  contextSteer: {q(c['steer'])}
  basis: ours
''')
w('```\n\n### M4 Open segments\n<!-- label: both; status: drafted; basis: primary -->\n```yaml\n')
if not OPEN: w('[]   # the figure leaves no segment blank on purpose\n')
for o in OPEN:
    w(f'''- id: {C.PFX}/{slug(o['axis'])}.open
  position: {{ axis: {o['axis']}, page: {o['page']} }}
  reason: {{ span: {{ start: {openrec[0]}, end: {openrec[1]} }}, source: {q(C.OPEN_REASON)}, page: {g('OPEN_REASON_PAGE', 12)} }}
  agentInstruction: {q(C.OPEN_INSTR[o['axis']])}
''')
w('```\n\n### M5 Crosswalks\n<!-- label: both; status: drafted; basis: primary -->\n```yaml\nstated:\n')
if PSF:
    if psf_lead: w(f"  lead: {{ span: {{ start: {psf_lead[0]}, end: {psf_lead[1]} }}, source: {q(PSF['lead'])}, page: {PSF['page']} }}\n")
    w('  codes:\n' if PSF.get('codes') else '  codes: []   # the table names no dimension\n')
    for code in PSF.get('codes', []):
        w(f"    - {{ to: advancehe/psf-dimensions-2023/{code}, code: {code}, page: {PSF['page']}, note: {q(PSF.get('codeNote', 'named in the PSF table'))} }}\n")
    if psf_fel: w(f"  fellowship: {{ span: {{ start: {psf_fel[0]}, end: {psf_fel[1]} }}, source: {q(PSF['fellowship'])}, page: {PSF['page']}, note: \"an invitation, not an obligation: not an S4 statement\" }}\n")
else:
    w('  []\n')
w('inferred:\n')
for x in C.M5_INFERRED:
    w(f"  - {{ from: {q(x['from'])}, to: {q(x['to'])}, rel: {x.get('rel', 'related')}, basis: inferred, note: {q(x['note'])} }}\n")
w('```\n\n### M6 Practice themes carried\n<!-- label: both; status: drafted; basis: discussion -->\n```yaml\n')
for th, wd in C.CONDS.items():
    w(f'- {{ id: {th}, tier: practice, working: {q(wd)}, carriedBy: {q(carried.get(th, []))}, status: provisional }}\n')
w('```\n\n## Part B Terminology\n\n### B1 Concepts\n<!-- label: both; status: drafted; basis: primary -->\n```yaml\n')
for b in C.BCONCEPTS:
    w(f"- {{ slug: {b['slug']}, definition: {q(b['defn'])}, scopeNote: {q(b['scope'])}, category: {b['cat']}, practices: [learning-and-teaching] }}\n")
w('```\n\n### B2a Terms as the issuer uses them\n<!-- label: source; status: drafted; basis: primary -->\n```yaml\n')
for b in C.BCONCEPTS:
    w(f"- {{ concept: {b['slug']}, form: {q(b['form'])}, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }}\n")
w('''```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
''')
for x in C.B4:
    w(f"- {{ rel: {x['rel']}, from: {x['from']}, to: {x['to']}, note: {q(x['note'])} }}\n")
w('```\n\n### B5 Rules\n')
for x in C.B5: w(f'- {x}\n')
w(f'''
## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: {q(C.TITLE)}
  edition: {q(E)}
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: {RAW}
  heldFiles: ["txt/{C.NAME}.txt", "txt/{C.NAME}.norm.txt", "records/{C.NAME}.held.json", "pdf/{C.NAME}.pdf"]
  citedIn: [0.2, S1, S2, S3, S4, M1, M2, M4, M5, B1]
```

### D2 Research log
```yaml
- {{ ref: D1, tier: primary, consulted: "{a.stamp[:10]}", pass: P1, outcome: "used for every section; figure pages read as images ({F['readFrom']})" }}
''')
if g('THEORY'):
    w(f"- {{ ref: \"{C.THEORY}\", tier: primary, consulted: \"{a.stamp[:10]}\", pass: P1, outcome: \"read for consistency of component names; not cited\" }}\n")
w('```\n\n### D3 Wanted sources\n```yaml\n')
for x in C.D3:
    w(f"- {{ citation: {q(x['citation'])}, settles: {q(x['settles'])}, asked: not yet, state: wanted }}\n")
w('```\n\n## Part E Gaps and questions\n')
for x in C.PART_E: w(f'- {x}\n')
if nscr: w(f'- M2: {nscr} label(s) not held in the text layer (read from the page image; `span: none`); MD-2 cannot check them by script.\n')
w(f'''
---

## Change notes
- {a.version}, {a.stamp}: {C.CHANGE} Model template {TEMPLATE_V}, builder {BUILDER_V}: {nseg} components, {nopen} open segments, {len(stmts)} statements, {len(C.CONDS)} practice themes.
''')
for x in (g('CHANGES_PRIOR', []) or []): w(f'- {x}\n')
doc = ''.join(out)

# ---- YAML parses
fm = doc.split('---\n')[1]
try: yaml.safe_load(fm)
except Exception as ex: err(f'front matter does not parse: {ex}')
for i, blk in enumerate(re.findall(r'```yaml\n(.*?)```', doc, re.S)):
    try: yaml.safe_load(blk)
    except Exception as ex: err(f'YAML block {i} does not parse: {str(ex)[:160]}')

print(f'{a.doc}: {nseg} components ({nscr} not in text), {nopen} open, {len(stmts)} statements, {len(C.CONDS)} practice themes; {len(errors)} error(s)')
for e_ in errors: print('  ERROR', e_)
if not a.check and not errors:
    open(os.path.join(DOCDIR, a.doc + '.md'), 'w', encoding='utf-8').write(doc)
    shutil.copy(__file__, os.path.join(DOCDIR, 'run-src', 'model_build.py'))
    print('  written', os.path.join(DOCDIR, a.doc + '.md'))
sys.exit(1 if errors else 0)
