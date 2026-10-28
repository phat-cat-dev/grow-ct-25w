#!/usr/bin/env python3
"""Build welsh-government-cqfw-level-descriptors-2009.md (run 0045)."""
import json, sys, hashlib
S = '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
H = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
sk = json.load(open(f'{S}/cqfw-skel.json')); ns = {}; exec(open(f'{S}/cqfw_judgement.py', encoding='utf-8').read(), ns)
P, NAME, LEVELS, DEF, THREADS = ns['P'], ns['NAME'], ns['LEVELS'], ns['DEFINING'], ns['THREADS']
idx = {e['slug']: e for e in json.load(open(f'{H}/index.json'))}['welsh-government-cqfw-level-descriptors-2009']
raw = open(f'{H}/welsh-government-cqfw-level-descriptors-2009.txt', 'rb').read(); normb = open(f'{H}/welsh-government-cqfw-level-descriptors-2009.norm.txt', 'rb').read()
pdfh = '98e069d687e31ea74e8916aa2f3dfe9fa2436e1928638e595bcb76ba998a0a31'  # the PDF is not held (Abbott, 04:10: "Remove pdfs")
q = lambda s: json.dumps(s, ensure_ascii=False)
COLN = {'summary': 'Summary', 'knowledge': 'Knowledge and understanding', 'application': 'Application and action', 'autonomy': 'Autonomy and accountability'}
DOM = {'knowledge': 'knowledge-and-understanding', 'application': 'application-and-action', 'autonomy': 'autonomy-and-accountability'}
LID = lambda l: 'cqfw:' + (l if l.startswith('entry') else l[1:])
sp = {x['id']: x['span'] for x in sk['statements']}
ORDER = [x['id'] for x in sk['statements'] if x['column'] != 'summary']
o = []; w = o.append
w(f'''---
id: std:doc:welsh-government-cqfw-2009-framework
title: Level Descriptors
profile: standards/framework
profileVersion: 0.1.5-draft
issuer: Welsh Government (CQFW), as Abbott identifies it; the document itself names no issuer
kind: qualification-framework
jurisdiction: [Wales]
subjectScope: universal
subjects: []
edition: January 2009
published: 2009-01
status: unknown
supersedes: none
heldText: {{ method: sha256-bytes, raw: {hashlib.sha256(raw).hexdigest()}, normalised: {hashlib.sha256(normb).hexdigest()} }}
original: {{ method: sha256-bytes, pdf: {pdfh}, held: no }}   # supplied files stay out of UNI (nts N-1020)
frameworkKind: level-descriptors
nations: [Wales]
levels: [cqfw:entry-1, cqfw:entry-2, cqfw:entry-3, cqfw:1, cqfw:2, cqfw:3, cqfw:4, cqfw:5, cqfw:6, cqfw:7, cqfw:8]   # no cross-framework equivalents stated in this document
awards: none-stated
credit: none-stated
licence: none stated in the document (Part E)
parts:
  S: full
  B: "not-applicable: the document defines no terms"
  C: "not-applicable: the document sets out levels, not a procedure"
pins: {{ structure: 0.13.0-draft, template: 0.5.0-draft, runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0045
passes:
  P1: 2026-10-03, std (claude.ai, META Project)
  P2: "skipped: the text was read direct from the PDF; the issuer's identity rests on Abbott's word (Part E)"
  P3: open
version: 0.1.0
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.5.0-draft under the standards/framework variant (profile 0.1.5-draft; its template is to write), with the level-language section SL proposed for it (Abbott, 04:03; std N-0057) -->
# CQFW Level Descriptors (January 2009)

> Run 0045, P1 by std. The issuer's words are held in UNI only (`wkspc2601-library/txt/welsh-government-2009-cqfw-level-descriptors-standard.norm.txt`, extracted from the PDF table by table cell); every statement points into them by character span. Everything else is our words; in the level-language section, words in quotation marks are the issuer's, a few at a time. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The Credit and Qualifications Framework for Wales' generic level descriptors, from Entry 1 to Level 8, each described for knowledge and understanding, application and action, and autonomy and accountability. Reach for it to say what achievement at a level looks like in any subject or setting, or to write level-based progression. It is not a subject standard, a qualification descriptor or a credit specification.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
A short table, dated January 2009, describing eleven levels of achievement (Entry 1 to 3, then Levels 1 to 8) in a summary and three strands: knowledge and understanding; application and action; autonomy and accountability. Each strand is a few short imperative sentences ("Use...", "Address...", "Take responsibility..."). The levels climb by changing a small set of qualifiers: how defined and complex the problem is, what kind of knowledge is drawn on, what is done with it, how methods are chosen, how far enquiry and evaluation reach, and how much responsibility and autonomy the learner holds. The document names no issuer; Abbott identifies it as CQFW's.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: "unknown in the document; Abbott: CQFW's (Credit and Qualifications Framework for Wales, managed by the Welsh Government, as the Frameworks 2024 says at 2.23); PDF metadata author: Evans, Emma-Jane (DfES - QLD)"
title: Level Descriptors
edition: January 2009
dates:
  published: 2009-01
  other: []
kind: qualification-framework
jurisdiction: [Wales]
authority: reference   # the document states none; inferred from its use as CQFW's level descriptors (Part E)
licence: none stated
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: generic descriptions of achievement at eleven levels, Entry 1 to Level 8, in a summary and three strands (D1, the table)
appliesTo:
  awards: none-stated
  levels: [cqfw:entry-1, cqfw:entry-2, cqfw:entry-3, cqfw:1, cqfw:2, cqfw:3, cqfw:4, cqfw:5, cqfw:6, cqfw:7, cqfw:8]
  providers: none-stated
whoMustUse: none-stated
howUsed: [other: none stated in the document]
doesNot: none-stated
beneficiary: the learner
statedScope: none-stated   # the document is the table alone, with no introduction
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary. The issuer's own structure: levels in rows, the summary and three strands in columns; no numbering beyond the level names. Statement ids are level/strand.sentence in the issuer's order. -->
```yaml
components:''')
for c in sk['components']:
    w(f'  - {{ number: "{c["id"]}/{c["column"]}", componentType: {"level" if c["column"] == "summary" else "descriptor"}, parent: "{c["id"]}", heading: {q(c["level"] + ", " + COLN[c["column"]])} }}')
w('''excluded:
  - { number: none, heading: "the repeated table header on each page", kind: "other: page furniture" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. 94 descriptor sentences, one record each; the level summaries are in SL1. Force `describes`: level descriptors state what achievement at a level reflects, without obliging. -->
```yaml''')
for i in ORDER:
    r = P[i]; lv, rest = i.split('/'); col = rest.split('.')[0]
    w(f'''- id: welsh-government/cqfw-2009/{i}
  locator: {{ number: "{i}", headingPath: [{q(NAME[lv])}, {q(COLN[col])}] }}
  span: {{ start: {sp[i]['start']}, end: {sp[i]['end']} }}
  stem: none
  statementType: descriptor
  force: describes
  level: {LID(lv)}
  dimension: {DOM[col]}
  appliesTo: "achievement at {NAME[lv]}"
  addressee: learner
  verbs: [{', '.join(r['verbs'])}]
  about: {q(r['about'])}
  themes: [none]
  paraphrase: {q(r['para'])}
  quote: none
  audience: both
  subjects: inherited''')
w('```\n\n### S4a Audience versions\n<!-- label: both; status: drafted; basis: primary -->\n```yaml')
for i in ORDER:
    r = P[i]
    w(f'''- statement: welsh-government/cqfw-2009/{i}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: describes, status: drafted }}
  forBeneficiary: {{ text: {q(r['ben'])}, rewrite: full, force: describes, status: drafted }}''')
w('''```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:''')
for l in LEVELS:
    w(f'  - {{ id: {LID(l)}, role: defines, locator: "D1, {NAME[l]}" }}')
w('''crosswalks: []   # this document states none; framework rule 2: an equivalence is recorded only with its source, never inferred. The Frameworks 2024 (2.23, 2.24) states the FHEQ's place in the CQFW: recorded there, at S-03
```

### S6 Themes
`not-applicable-by-design`: the document carries no cross-cutting themes.

### S7 Relations
```yaml
- { rel: partOf, target: "CQFW (Credit and Qualifications Framework for Wales)", note: "the framework's level descriptors (Abbott)" }
- { rel: alignsWith, target: "std:doc:qaa-fheq-2024-framework (S-03)", note: "the FHEQ is a constituent part of the CQFW (Frameworks 2024, 2.23)" }
```

### S8 Currency and review
```yaml
published: 2009-01
lastReviewed: none-stated
reviewCycle: none-stated
consultation: none-stated
replacedBy: unknown   # whether a later CQFW edition replaces these descriptors is to check (Part E)
```

### S9 Commentary (optional)
`unknown`: not researched.

### SL Level language
<!-- Proposed for the frameworks variant (Abbott, 04:03: "have a section in any um, level based framework, which is really what these are ... breaks down the language of them, looks at the verbs, looks at the um, the way they communicate uh, progression"; std N-0057). label: both; status: drafted; basis: primary. Our words, with the issuer's own verbs and short quoted phrases; the issuer's full wording, cell by cell, is in the held companion `wkspc2601-library/records/welsh-government-2009-cqfw-level-descriptors-standard.levels.held.md` (UNI only, never published). -->

#### SL1 What defines each level
<!-- Each level's defining step, in our words, for the practitioner and the learner. Read down the table to see the progression. -->

| Level | For the practitioner | For the learner |
|---|---|---|''')
for l in LEVELS:
    w(f'| {NAME[l]} | {DEF[l][0]} | {DEF[l][1]} |')
w('''
#### SL2 The level table, by strand
<!-- Each cell is our short gloss of the issuer's sentences at that level and strand (the S4 `about` fields); the issuer's sentences are the S4 spans. -->

| Level | Knowledge and understanding | Application and action | Autonomy and accountability |
|---|---|---|---|''')
for l in LEVELS:
    cells = []
    for col in ('knowledge', 'application', 'autonomy'):
        ab = [P[i]['about'] for i in ORDER if i.startswith(l + '/' + col + '.')]
        cells.append('; '.join(ab) if ab else '(summary only)')
    w(f'| {NAME[l]} | ' + ' | '.join(cells) + ' |')
w('''
#### SL3 Verbs by level
<!-- The issuer's own verbs, as given, in each strand at each level (from the S4 `verbs` fields, first occurrence kept). -->

| Level | Knowledge and understanding | Application and action | Autonomy and accountability |
|---|---|---|---|''')
for l in LEVELS:
    cells = []
    for col in ('knowledge', 'application', 'autonomy'):
        seen = []
        for i in ORDER:
            if i.startswith(l + '/' + col + '.'):
                for v in P[i]['verbs']:
                    if v.lower() not in [x.lower() for x in seen]: seen.append(v)
        cells.append(', '.join(x.lower() for x in seen) if seen else '')
    w(f'| {NAME[l]} | ' + ' | '.join(cells) + ' |')
w('''
#### SL4 How progression is communicated
<!-- Each thread follows one quality up the levels: where the issuer changes its wording, the level is listed with the new wording (the issuer's words in quotation marks, otherwise our short reading). A level not listed keeps the wording of the level below. -->
''')
for name, steps in THREADS:
    w(f'- **{name[0].upper() + name[1:]}:** ' + '; '.join(f'{NAME[l]}: {t}' for l, t in steps) + '.')
w('''
#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **The form is fixed.** Every level uses the same three strands and the same sentence shape: an imperative verb, an object, and a qualifier of context or degree. Progression is carried almost wholly by the qualifiers and a few verbs, not by new kinds of sentence.
- **Verbs climb in a small ladder.** Thinking verbs go know, be aware, interpret, evaluate, analyse, critically analyse, then "produce modified conceptions" (Level 7) and "new knowledge and theories" (Level 8). Method verbs go use, select, identify, adapt, determine, refine, then "formulate" (Level 8).
- **Context does the most work.** The problem moves from "simple, familiar" through "well-defined, routine" and "complex and non-routine" to "limited definition", "problematic situations" and finally contexts that "lack definition". Each step loosens how much is given.
- **Responsibility and autonomy rise together but separately.** Responsibility widens in scope (outcomes, tasks, courses of action, change, the field); autonomy widens in limits (guidance, direction, limited, broad, across an area, leadership).
- **Some steps are small.** Levels 4 and 5, and 6 and 7, share most of their wording; the differences sit in one or two qualifiers per strand ("well-defined" to "broadly-defined"; "refine" to "reformulate"). These are the steps a progression model has to make most visible.
- **Higher education levels.** Levels 4 to 8 are the higher education levels the FHEQ shares (Frameworks 2024, 2.24); the comparison of the two sets of wording is the second layer Abbott asks for (std N-0058), after S-03.

## Part B Terminology
`not-applicable-by-design`: the document defines no terms.

## Part C Process

### C0 Formality
`not-applicable`: the document sets out levels, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: "unknown in the document (Abbott: CQFW)"
  title: Level Descriptors
  edition: January 2009
  year: 2009
  url: unknown
  retrieved: "PDF attached by Abbott, 2026-10-03, 03:47"
  licence: none stated
  tier: primary
  readVia: direct
  held: ''' + hashlib.sha256(raw).hexdigest() + '''
  heldFiles: [wkspc2601-library/txt/welsh-government-2009-cqfw-level-descriptors-standard.txt, wkspc2601-library/txt/welsh-government-2009-cqfw-level-descriptors-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, SL]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct; extracted by table cell with pdfplumber, normalised with stan's tool (word sequence equal)" }
- { ref: "std:doc:qaa-fheq-2024-framework, 2.23 and 2.24 (held, read for S-03)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "the CQFW's managing body and its relation to the FHEQ, for S1, S5 and S7" }
```

### D3 Wanted sources
```yaml
- { citation: "the CQFW's own publication of these level descriptors, with its issuer, date, status and re-use terms, and any later edition", settles: [S1, S8], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- S1: the document names no issuer, framework or nation; CQFW rests on Abbott's word (03:47 and 04:03) and the PDF's metadata author (DfES - QLD, read as the Welsh Government's education department: inference). Its status (current or superseded), licence and any later edition are unknown (D3).
- S1: the same three strands and Entry 1 to Level 8 were used by England's Qualifications and Credit Framework; this text is taken as CQFW's on Abbott's word, not compared with the QCF's.
- S3, extraction: the PDF is a table; the text was taken cell by cell (pdfplumber), so the held text's line order is ours: level, strand heading, cell. pdftotext's reading order interleaved the columns and was not used.
- S4: statements are cut at sentences, the issuer giving no numbers within a cell; ids are ours (level/strand.n).
- S4: the source writes "well defined" and "well-defined", "non- routine" (a broken hyphen), "broadly- defined"; the held text keeps them as extracted.
- S4, force: `describes` for every descriptor; the imperative form ("Use...", "Take responsibility...") describes what achievement reflects and obliges no one.
- S5: no crosswalk: this document states none, and the framework variant records an equivalence only from its source (profile 0.1.5-draft, P5); the CQFW-FHEQ relation is the Frameworks 2024's to state (S-03).
- S4, the cut: the framework variant says a descriptor is cut "at its own headings" (P5, rule 3); this run cuts one step finer, one record per sentence within each heading, the sentences being separate descriptors and the unit the verb analysis needs. For Abbott (D-std-0005).
- SL: the section is proposed for the frameworks variant; its tables are built from S4 and need P3 like the rest.
- ST-12: versions here run short (7 to 37 words); the formulaic wording of level descriptors made close paraphrase copy nine-word runs (31 found and reworded).

---

## Change notes
- 0.1.0: 2026-10-03: researched by run frame 0.1.1-draft and standards run layer 0.5.0-draft, std, run 0045 (P1).''')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
# held companion: the issuer's words cell by cell (UNI only)
norm = normb.decode('utf-8')
hc = ['# CQFW Level Descriptors (January 2009): the issuer\'s wording, by level and strand', '', '> HELD. UNI only: never in the Project, a mirror, an artifact or a store. Rendered from the held text by span, for practitioner reference and analysis; the ingestion document carries our words.', '']
for c in sk['components']:
    hc.append(f'## {c["level"]}: {COLN[c["column"]]}'); hc.append(norm[c['start']:c['end']]); hc.append('')
open(f'{H}/welsh-government-cqfw-level-descriptors-2009.levels.held.md', 'w', encoding='utf-8').write('\n'.join(hc))
print('S4', len(ORDER))
