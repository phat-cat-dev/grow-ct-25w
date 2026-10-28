# Builds the two PSF 2023 framework documents (run 0068, std):
#   ingest-std-advancehe-psf-dimensions-2023-framework   (the Dimensions, with the common material)
#   ingest-std-advancehe-psf-descriptors-2023-framework  (the Descriptors D1 to D4)
# Usage: python3 psf_build.py <standards dir> <stamp>
import sys, os, json, hashlib, re
sys.path.insert(0, os.path.dirname(__file__))
from psf_data import *

STD = sys.argv[1]; STAMP = sys.argv[2]
HELD = os.path.join(os.path.dirname(os.path.dirname(STD)), 'txt/advance-he-2023-professional-standards-framework-standard')   # STD is the library's ingested/standards (std N-0119)
norm = open(HELD + '.norm.txt').read()
rawb = open(HELD + '.txt', 'rb').read()
RAW = hashlib.sha256(rawb).hexdigest()
NORM = hashlib.sha256(open(HELD + '.norm.txt', 'rb').read()).hexdigest()
PDF = '3b79bcff1e3ce2533ff2a6f6e74332b3dfcb95a483c718dace6580e976e0a396'
q = json.dumps

pos = [0]
def span(src, after=None):
    i = norm.find(src, after if after is not None else 0)
    assert i >= 0, src
    return i, i + len(src)

def chk_verbs(src, verbs):
    for v in verbs:
        assert re.search(r'\b' + re.escape(v) + r'\b', src), (v, src)

PERMISSION = ("Abbott (3 October 2026, 10:18): \"I have permissio I run the Fellowship scheme at CMet and am a former member of the Advance HE consultation team - extarct the original and rephrase as decided - it is the phrases that will be used by agents not the original\" (D-std-0013)")

def frontmatter(kind, title, levels, awards, version, parts_s, extra=''):
    return f'''---
id: std:doc:advancehe-psf-{kind}-2023-framework
title: {q(title)}
profile: standards/framework
profileVersion: 0.2.0-draft
issuer: Advance HE (copyright jointly Advance HE, GuildHE and Universities UK)
kind: professional-standards-framework   # proposed kind (Part E; for nts)
jurisdiction: [UK]   # the document states none; Advance HE recognition is UK-based and used internationally (inferred, Part E)
subjectScope: universal
subjects: []
edition: 2023
published: 2023
status: current   # as at the held text; not checked against Advance HE's site (Part E)
supersedes: "not stated in the document; known to replace the UK Professional Standards Framework (UKPSF) of 2011 (std's knowledge, P2 to confirm)"
heldText: {{ method: sha256-bytes, raw: {RAW}, normalised: {NORM} }}
original: {{ method: sha256-bytes, pdf: {PDF}, held: no }}   # supplied files stay out of UNI (nts N-1020)
frameworkKind: professional-standards   # proposed value (Part E)
nations: [UK]
levels: {levels}
awards: {awards}
credit: none-stated
knowledgePath: {{ practice: "01 education", stream: "01_03 learning and teaching", reference: "professional recognition (code to issue)", unit: "professional standards framework (ST code to issue)" }}   # Abbott, 09:49
licence: "All rights reserved (© Advance HE, GuildHE, Universities UK 2023); reproduction only with the copyright holders' permission. Held and rephrased on Abbott's permission (S1)"
agentUse: source-and-rephrased   # each record carries the issuer's statement (`source`) for language analysis and our rephrasings for agent phrasing; private, never published (Abbott, 10:18, 10:56; D-std-0014)
parts:
  S: {parts_s}
  B: full
  C: "not-applicable: the document sets out standards, not a procedure; the recognition route is summarised in S2"
pins: {{ structure: 0.13.0-draft, template: 0.6.1-draft, framework: 0.1.1-draft, runFrame: 0.1.1-draft, runLayer: 0.6.1-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.6.1-draft; std, run 0068
passes:
  P1: "{STAMP[:10]}, std (Claude Code, META Project)"
  P2: "skipped: read direct from the issuer's PDF; the 2011 predecessor and Advance HE's own guidance per Descriptor are wanted (D3)"
  P3: open
version: {version}
{extra}---
'''

def s1(scope):
    return f'''### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: "Advance HE, developed on behalf of the higher education sector; copyright jointly Advance HE, GuildHE and Universities UK (page 12)"
title: "Professional Standards Framework for teaching and supporting learning in higher education 2023"
shortTitle: PSF 2023
edition: 2023
dates:
  published: 2023
  other: []
kind: professional-standards-framework
jurisdiction: [UK]
authority: sector   # a sector framework for professional recognition; not regulatory
licence: "All rights reserved; redistribution or reproduction, in part or whole, only with the copyright holders' explicit permission (page 12)"
copyrightNotice: "© Advance HE, GuildHE, Universities UK 2023. All Rights Reserved."
permission:
  basis: "{PERMISSION.replace('"', "'")}"
  holder: "Abbott: runs the Cardiff Metropolitan University Fellowship scheme (an accredited route to Advance HE recognition) and is a former member of the Advance HE consultation team"
  use: "the issuer's statements are held in full, in the held text and in each S4 record's `source` field, for private language analysis; nothing is published; agents phrase from our rephrasings (paraphrase, S4a) (D-std-0014)"
scope: "{scope}"
```
'''

def rec_yaml(rid, src, a, b, stem, typ, force, level, part, verbs, about, para, aud, extra=None, applies="the individual's practice", addressee='practitioner'):
    chk_verbs(src, verbs)
    out = [f'- id: {rid}',
           f'  locator: {{ number: {q(rid.split("/", 2)[-1])}, headingPath: {q(part)} }}',
           f'  span: {{ start: {a}, end: {b} }}',
           f'  stem: {stem}',
           f'  statementType: {typ}',
           f'  force: {force}',
           f'  level: {level}',
           f'  dimension: {part[-1].lower().replace(" ", "-").replace("?", "")}',
           f'  appliesTo: {q(applies)}',
           f'  addressee: {addressee}',
           f'  verbs: {q(verbs)}',
           f'  about: {q(about)}',
           '  themes: [none]',
           f'  paraphrase: {q(para)}',
           f'  source: {q(src)}',
           '  quote: full   # the issuer statement, held for analysis (D-std-0014)',
           f'  audience: {aud}',
           '  subjects: inherited']
    if extra:
        out.insert(7, f'  requires: {json.dumps(extra)}')
    return '\n'.join(out)

def a4(rid, prac, ben, force):
    s = f'- statement: {rid}\n  forPractitioner: {{ text: {q(prac)}, rewrite: full, force: {force}, status: drafted }}'
    if ben:
        s += f'\n  forBeneficiary: {{ text: {q(ben)}, rewrite: full, force: {force}, status: drafted }}'
    else:
        s += '\n  forBeneficiary: none   # practitioner-only record'
    return s

# ---------------------------------------------------------------- Dimensions document
DIMID = 'advancehe/psf-dimensions-2023'
recs, vers = [], []
for k, src, verbs, about, para, prac, ben in PURPOSE:
    a, b = span(src)
    recs.append(rec_yaml(f'{DIMID}/{k}', src, a, b, 'none', 'purpose', 'describes', 'none', ['Purpose'], verbs, about, para, 'both', applies='the framework', addressee='none'))
    vers.append(a4(f'{DIMID}/{k}', prac, ben, 'describes'))
dstart = norm.find('What are Dimensions?')
for k, src, verbs, about, para, prac, ben in ABOUT_DIMS:
    a, b = span(src, dstart)
    recs.append(rec_yaml(f'{DIMID}/{k}', src, a, b, 'none', 'definition', 'describes', 'none', ['Dimensions', 'What are Dimensions?'], verbs, about, para, 'both', applies='the Dimensions', addressee='none'))
    vers.append(a4(f'{DIMID}/{k}', prac, ben, 'describes'))
setpos = {}
for code, _, src, verbs, about, para, prac, ben in STEMS:
    head = SETS[code][0]
    hp = norm.find(head + ' ' + src)
    a, b = span(src, hp)
    setpos[code] = b
    recs.append(rec_yaml(f'{DIMID}/{code}/stem', src, a, b, 'none', 'stem', 'describes', 'none', ['Dimensions', head], verbs, about, para, 'both'))
    vers.append(a4(f'{DIMID}/{code}/stem', prac, ben, 'describes'))
for code, src, verbs, about, para, prac, ben in DIMS:
    a, b = span(code + ' ' + src, setpos[code[0]])
    a += len(code) + 1
    recs.append(rec_yaml(f'{DIMID}/{code}', src, a, b, f'{DIMID}/{code[0]}/stem', 'dimension', 'describes', 'none', ['Dimensions', SETS[code[0]][0]], verbs, about, para, 'both'))
    vers.append(a4(f'{DIMID}/{code}', prac, ben, 'describes'))
n_dim = len(recs)


dimdoc = frontmatter('dimensions', 'Professional Standards Framework 2023: the Dimensions of practice, with the framework\'s purpose', '[]   # level-free: the levels are the Descriptors, std:doc:advancehe-psf-descriptors-2023-framework', 'none-stated   # the Fellowship categories belong to the Descriptors document', '0.1.1', '"full for the purpose and the Dimensions (pages 2, 4, 5); the Descriptors (pages 6 to 11) are std:doc:advancehe-psf-descriptors-2023-framework"', 'dimensionIds: [psf:V1, psf:V2, psf:V3, psf:V4, psf:V5, psf:K1, psf:K2, psf:K3, psf:K4, psf:K5, psf:A1, psf:A2, psf:A3, psf:A4, psf:A5]   # defined here (S5); the Descriptors document cites them\n') + f'''
<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the standards/framework variant (framework template 0.1.1-draft; profile 0.2.0-draft). One of two documents for the PSF 2023, split by Abbott (10:20): this one holds the Dimensions and the material common to both (D-std-0013, framework rule 4) -->
# Professional Standards Framework 2023: the Dimensions of practice

> Run 0068, P1 by std. Held by permission (S1). Private to the project, never published. Each S4 record carries the issuer's statement in full (`source`) for language analysis, with its character span in the held text (`wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.norm.txt`), and our rephrasings (`paraphrase`, S4a), which are what agents phrase from (Abbott, 10:18 and 10:56; D-std-0014). Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The fifteen Dimensions of practice in Advance HE's Professional Standards Framework 2023, in three sets of five (Professional Values, Core Knowledge, Areas of Activity), each set with its lead-in. Reach for it to name what teaching and supporting learning in higher education involves, to frame staff development, mentoring or a recognition claim, or to tag practice against V1 to A5. For how much of the Dimensions each Fellowship category asks for, use the Descriptors document, `std:doc:advancehe-psf-descriptors-2023-framework`. It describes staff practice, not student achievement: it does not sit on the qualification level spine.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
A short sector framework for the professional practice of people who teach or support learning in higher education. Its purpose page gives eight aims, from making professionalism visible to offering a route to recognition. Its core is fifteen Dimensions in three linked sets of five. Each set has its own lead-in, which every statement completes: values are shown in the person's own setting, knowledge is applied in it, and activity is demonstrated in it. The values are the base; the knowledge serves the activities; the activities combine both. The four Descriptors, held in the companion document, say how much of the Dimensions each category of recognition requires.

## Part S Standard

{s1("the purpose (page 2) and the Dimensions (pages 4 and 5) of the PSF 2023; the Descriptors (pages 6 to 11) are in std:doc:advancehe-psf-descriptors-2023-framework")}
### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the fifteen Dimensions of professional practice in teaching and supporting learning in higher education (pages 4, 5), with the framework's purpose (page 2)"
appliesTo:
  awards: none-stated   # Fellowship categories: the Descriptors document
  levels: none   # level-free
  providers: none-stated
whoMustUse: none-stated   # voluntary; used for recognition, development and accreditation
howUsed: [professional recognition, initial and continuing professional development, review of practice, institutional accreditation of development programmes]
doesNot: "state levels; the Descriptors do (companion document)"
beneficiary: "staff who teach or support learning in higher education; through them, learners"
statedScope: "teaching and supporting learning in higher education, in diverse academic or professional settings (purpose.5)"
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary. The issuer numbers the Dimensions V1 to V5, K1 to K5, A1 to A5; the purpose bullets and the explanatory bullets are unnumbered and numbered here in order. -->
```yaml
components:
  - {{ number: purpose, componentType: section, parent: none, heading: "Purpose", items: 8 }}
  - {{ number: about, componentType: section, parent: none, heading: "Dimensions: What are Dimensions?", items: 7 }}
  - {{ number: V, componentType: set, parent: none, heading: "Professional Values", stem: V/stem, items: [V1, V2, V3, V4, V5] }}
  - {{ number: K, componentType: set, parent: none, heading: "Core Knowledge", stem: K/stem, items: [K1, K2, K3, K4, K5] }}
  - {{ number: A, componentType: set, parent: none, heading: "Areas of Activity", stem: A/stem, items: [A1, A2, A3, A4, A5] }}
companions:
  - {{ id: std:doc:advancehe-psf-descriptors-2023-framework, holds: "Descriptors D1 to D4 (pages 6 to 10) and the recognition page (page 11)" }}
statements: {n_dim}
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. {n_dim} records: 8 purpose, 7 about the Dimensions, 3 stems, 15 Dimensions. Force `describes`: the Dimensions describe practice; they bind only through a Descriptor's criteria (companion document). Verbs are the issuer's, each present in its span; the K items are noun phrases completing the stem "apply knowledge of", so carry no verb of their own. `paraphrase` is ours. -->
```yaml
{chr(10).join(recs)}
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for those who lead, mentor, review or design recognition and development (scheme leads, mentors, reviewers, developers). forBeneficiary: for the person evidencing their own practice, in the second person. These are the phrases agents use (Abbott, 10:18). -->
```yaml
{chr(10).join(vers)}
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels: []   # level-free; the levels (psf:d1 to psf:d4) are defined in std:doc:advancehe-psf-descriptors-2023-framework
dimensions:   # defined here, the only place; the Descriptors document cites them
''' + '\n'.join(f'  - {{ id: psf:{c}, role: defines, set: {SETS[c[0]][1]}, record: {DIMID}/{c} }}' for c, *_ in DIMS) + f'''
crosswalks: []   # the document states none to other frameworks
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- {{ theme: "sustainability", where: "{DIMID}/purpose.7", note: "the UN Sustainable Development Goals named as one example of evolving needs" }}
- {{ theme: "inclusion and equity", where: "{DIMID}/V1, {DIMID}/V2", note: "inclusive practice is also a quality every Descriptor's activity criterion asks for (companion document)" }}
```

### S7 Relations
```yaml
- {{ rel: companionOf, target: std:doc:advancehe-psf-descriptors-2023-framework, note: "one framework, two documents (Abbott, 10:20; D-std-0013); the purpose and terms are held here once" }}
- {{ rel: describedBy, target: ing:doc:professional-standards-framework-advance-he-2023, note: "ing's theory-side document on the same PDF (run 0053): the PSF as a framework of ideas, with its history and criticisms; this document holds the statements" }}
- {{ rel: supersedes, target: "UKPSF 2011", note: "not stated in the document; std's knowledge, P2 to confirm (W-std-0022)" }}
- {{ rel: relatesTo, target: std:ref:uk-framework, note: "none stated; the PSF describes staff practice and sits beside the qualification spine, not on it (S9)" }}
```

### S8 Currency and review
```yaml
published: 2023
lastReviewed: none-stated
reviewCycle: none-stated
consultation: "none stated in the document; Abbott reports he was a member of Advance HE's consultation team (S1)"
replacedBy: none known
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: inferred. Our reading; nothing here is the issuer's. -->
- **Not on the spine.** The reference framework's spine (`spine:entry-1` to `spine:8`) steps student achievement. The Dimensions describe the practice of staff, so they sit beside it. Where a Dimension names the work a level descriptor assumes, the link is to the theory side, not the spine (inferred).
- **Proposed theory links** (associations, for ing; inferred): V3 and K3 with reflective practice (`src-schon-1983`, `src-johns-2000`); A1 and K2 with constructive alignment (`src-biggs-and-tang-2011`); A3 with assessment for learning; K1 with learning theory generally; A5 with continuing professional development.
- **Proposed links to the shared strands** (inferred): the Areas of Activity are the `strand:application` of teaching practice; V4 and K5 carry `strand:autonomy` in the sense of reading one's context and answering to it.

### SL Level language
<!-- label: both; status: drafted; basis: primary. The Dimensions are level-free (framework template 0.1.1-draft, rule 6 as amended: a level-free companion points to the document that holds the levels). SL1, SL2 and SL4 are in std:doc:advancehe-psf-descriptors-2023-framework; this document keeps the verbs by set and the observations. -->

#### SL1, SL2, SL4
`see std:doc:advancehe-psf-descriptors-2023-framework`, whose SL2 shows how much of each set each Descriptor asks for.

#### SL3 Verbs by set
| Set | Lead-in verb | Statement verbs (the issuer's, first occurrence kept) |
|---|---|---|
| Professional Values | show how you | respect; promote; use; respond; collaborate |
| Core Knowledge | apply knowledge of | none: noun phrases (how learners learn; approaches; critical evaluation; use of technologies; requirements for quality) |
| Areas of Activity | demonstrate that you | design, plan; teach, support; assess, give; support, guide; enhance |

#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **Three grammars.** Values are stances (verb phrases of attitude: respect, promote, respond); knowledge is a list of topics (noun phrases); activities are actions (design, teach, assess, guide, enhance). The lead-ins carry the evidence verb for each: show how, apply, demonstrate.
- **"In your context" carries the scope.** Every lead-in starts with the person's own setting, which is how one framework covers lecturers, librarians, technicians, learning developers and others. Agents writing for a role should keep that move: name the setting, then the Dimension.
- **"And/or" widens every activity.** Teaching and supporting learning are held as equal routes throughout ("teach and/or support"), so A2 and K2 never assume a lecturing role.
- **No levels inside a Dimension.** The Dimensions do not step; the Descriptors carry progression by how many Dimensions, how integrated, and whose practice (companion SL4).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary. Our definitions, from the document's use; held once here for both PSF documents (framework rule 4). -->
```yaml
- {{ term: Dimensions, sense: "the fifteen statements of what professional practice in teaching and supporting learning involves, in three sets", source: "about.1, about.2" }}
- {{ term: Professional Values, sense: "the five values (V1 to V5) on which the knowledge and activities rest", source: about.values }}
- {{ term: Core Knowledge, sense: "the five forms of knowledge (K1 to K5) the activities need, shaped by the values", source: about.knowledge }}
- {{ term: Areas of Activity, sense: "the five core activities (A1 to A5) in which values and knowledge combine", source: about.activity }}
- {{ term: stem statement, sense: "the lead-in each set's statements complete", source: about.3 }}
- {{ term: Descriptor, sense: "one of four statements (D1 to D4) of a broad category of practice, with an introduction and three criteria", source: "std:doc:advancehe-psf-descriptors-2023-framework, about.1" }}
- {{ term: criteria statement, sense: "one of the three things a Descriptor asks a person to evidence", source: "the Descriptors document" }}
- {{ term: Fellowship, sense: "Advance HE's recognition of an individual who meets a Descriptor, in four categories: Associate Fellow, Fellow, Senior Fellow, Principal Fellow", source: "the Descriptors document, recognition.1" }}
- {{ term: institutional accreditation, sense: "Advance HE's confirmation that an institution's development programme is aligned with the PSF, so completing it brings recognition", source: "the Descriptors document, recognition.2" }}
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the document sets out standards; the recognition route is summarised in the Descriptors document's S2.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE (copyright Advance HE, GuildHE, Universities UK)
  title: "Professional Standards Framework for teaching and supporting learning in higher education 2023"
  edition: 2023 (screen-reader compatible version)
  year: 2023
  url: unknown   # www.advance-he.ac.uk named on page 11
  retrieved: "PDF attached by Abbott, 2026-10-03, 09:49"
  licence: "all rights reserved; held by permission (S1)"
  tier: primary
  readVia: direct
  held: {RAW}
  heldFiles: [wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.txt, wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, SL, B]
```

### D2 Research log
```yaml
- {{ ref: D1, tier: primary, consulted: {STAMP[:10]}, pass: P1, outcome: "read whole, direct (12 pages); pdftotext default mode; page 5's graphic linearised by hand in reading order (each set's heading, lead-in, then code and statement), words checked equal to the extraction; normalised with stan's normalise.js 1.0 (words equal)" }}
- {{ ref: "ing:doc:professional-standards-framework-advance-he-2023 (run 0053)", tier: secondary, consulted: {STAMP[:10]}, pass: P1, outcome: "front matter read for the relation in S7; its statements not used (untainted)" }}
- {{ ref: "run-src/psf_data.py, psf_build.py", tier: method, consulted: {STAMP[:10]}, pass: P1, outcome: "records and both documents built by script; spans checked against the normalised text; verbs checked present in each span; the issuer's statements in `source`; our rephrasings checked for no nine-word run of the held text" }}
```

### D3 Wanted sources
```yaml
- {{ w: W-std-0021, citation: "Advance HE's guidance notes for the PSF 2023, one per Descriptor, and its glossary", settles: [B, S9], asked: not yet, state: wanted }}
- {{ w: W-std-0022, citation: "the UK Professional Standards Framework (UKPSF) 2011, the predecessor, and Advance HE's account of the 2023 review", settles: [S1, S7, S8], asked: not yet, state: wanted }}
```

## Part E Gaps and questions
- S1, licence: the PSF's notice reserves reproduction to the copyright holders. Abbott has permission (10:18) and directs that the source statements are held in full for analysis (10:56); the documents are private to the project and never published (D-std-0014).
- Split (Abbott, 10:20): one PSF, two documents. The purpose page and the terms are held here once (framework rule 4); the Descriptors document points here.
- Names: `ingest-std-advancehe-psf-dimensions-2023-framework` and `-descriptors-`, the framework name with the part after the initials (D-std-0013, std's reading; Abbott may overrule).
- Kind: `professional-standards-framework` and `frameworkKind: professional-standards` are new values, not yet in the profile (P2). For nts.
- knowledgePath: Abbott gave education > learning and teaching > professional recognition > professional standards framework (09:49). Both documents sit at the last node; the reference code for "professional recognition" and the ST codes are not yet issued. For nts and pmg.
- Page 5: a circular graphic; the text extraction scatters its labels. The held text gives the three sets in reading order and leaves out the graphic's ring labels ("Dimensions of the framework" and set names repeated). Read from the page and the extraction; words checked.
- jurisdiction and supersedes are not stated in the document; both are std's knowledge, marked, for P2.
- ST-12: the versions here are short (4 to 35 words): the Dimensions are short phrases, and A4 and V5 cannot be put more briefly than the issuer does without losing sense; these few close echoes stay well under the nine-word limit.

---

## Change notes
- 0.1.1, 3 October 2026, 10:56: each S4 record now carries the issuer's statement in full (`source`, `quote: full`) for language analysis, beside our rephrasings (Abbott, 10:56; D-std-0014).
- 0.1.0, 3 October 2026, 10:28: researched by run frame 0.1.1-draft and standards run layer 0.6.1-draft, std, run 0068 (P1); held and rephrased on Abbott's permission (D-std-0013).
'''

# ---------------------------------------------------------------- Descriptors document
DESID = 'advancehe/psf-descriptors-2023'
recs, vers = [], []
dstart = norm.find('What are Descriptors?')
for k, src, verbs, about, para, prac, ben in ABOUT_DESC:
    a, b = span(src, dstart)
    recs.append(rec_yaml(f'{DESID}/{k}', src, a, b, 'none', 'definition', 'describes', 'none', ['Descriptors', 'What are Descriptors?'], verbs, about, para, 'both', applies='the Descriptors', addressee='none'))
    vers.append(a4(f'{DESID}/{k}', prac, ben, 'describes'))
cur = 0; n_crit = 0
for key, part, src, typ, force, verbs, about, para, prac, ben, req in DESC:
    d = key.split('/')[0]
    base = norm.find(f'Descriptor {d[1]} {d}') if part != 'recognition' else norm.find(src)
    if key.endswith('/stem') or key.endswith('intro.2'):
        base = cur
    if part == 'criteria':
        num = f'{d}.{key[-1]}'
        a, b = span(num + ' ' + src, cur); a += len(num) + 1
        n_crit += 1
    else:
        a, b = span(src, base)
    cur = b
    stem = f'{DESID}/{d}/stem' if part == 'criteria' else 'none'
    level = f'psf:{d.lower()}'
    recs.append(rec_yaml(f'{DESID}/{key}', src, a, b, stem, typ, force, level, [f'Descriptor {d[1]}', part.capitalize()], verbs, about, para, 'both', extra=req, applies=f'recognition at {d}'))
    vers.append(a4(f'{DESID}/{key}', prac, ben, force))
rstart = norm.find('Relationship to Advance HE')
for k, src, verbs, about, para, prac, ben, aud in RECOG:
    a, b = span(src, rstart)
    recs.append(rec_yaml(f'{DESID}/{k}', src, a, b, 'none', 'context', 'describes', 'none', ['Relationship to Advance HE individual professional recognition and institutional accreditation'], verbs, about, para, aud, applies='recognition and accreditation', addressee='none'))
    vers.append(a4(f'{DESID}/{k}', prac, ben, 'describes'))
n_des = len(recs)

def lvl_rows(col):
    rows = {}
    for key, part, src, typ, force, verbs, about, para, prac, ben, req in DESC:
        if key.endswith('intro.1'):
            rows[key[:2]] = (prac, ben)
    return rows
L = lvl_rows(None)
CAT = {'D1': 'Associate Fellow', 'D2': 'Fellow', 'D3': 'Senior Fellow', 'D4': 'Principal Fellow'}
sl1 = '\n'.join(f'| `psf:{d.lower()}` ({CAT[d]}) | {L[d][0]} | {L[d][1]} |' for d in ['D1', 'D2', 'D3', 'D4'])

desdoc = frontmatter('descriptors', 'Professional Standards Framework 2023: the Descriptors D1 to D4 and the recognition they lead to', '[psf:d1, psf:d2, psf:d3, psf:d4]   # staff categories of practice; not on the qualification spine (S9)', '[Associate Fellow, Fellow, Senior Fellow, Principal Fellow]   # Advance HE recognition, as each Descriptor states', '0.1.1', '"full for the Descriptors and the recognition page (pages 6 to 11); the purpose, the Dimensions and the terms are held once in std:doc:advancehe-psf-dimensions-2023-framework"', 'usesIds: "psf:V1 to psf:A5, defined in std:doc:advancehe-psf-dimensions-2023-framework"\n') + f'''
<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the standards/framework variant (framework template 0.1.1-draft; profile 0.2.0-draft). One of two documents for the PSF 2023, split by Abbott (10:20): this one holds the Descriptors; the purpose, Dimensions and terms are in the companion (D-std-0013, framework rule 4) -->
# Professional Standards Framework 2023: the Descriptors D1 to D4

> Run 0068, P1 by std. Held by permission (S1). Private to the project, never published. Each S4 record carries the issuer's statement in full (`source`) for language analysis, with its character span in the held text (`wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.norm.txt`), and our rephrasings (`paraphrase`, S4a), which are what agents phrase from (Abbott, 10:18 and 10:56; D-std-0014). Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The four Descriptors of Advance HE's Professional Standards Framework 2023, each an introduction and three criteria, with the Fellowship category each leads to: D1 Associate Fellow, D2 Fellow, D3 Senior Fellow, D4 Principal Fellow. Reach for it to say what a recognition claim at a category must evidence, to place a role or a colleague's practice at a category, to plan development towards the next one, or to write mentoring and review prompts. The Dimensions it cites (V1 to A5) are defined in `std:doc:advancehe-psf-dimensions-2023-framework`.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Four broad categories of practice for people who teach or support learning in higher education. D1 and D2 are about the person's own practice: D1 asks for some of the Dimensions (at least V1 and V3, K1 to K3, and two Areas of Activity), D2 for all fifteen. D3 and D4 are about influence and leadership: D3 asks for a sustained record of leading or influencing others' practice and practice reaching beyond direct teaching; D4 asks for sustained strategic leadership with wide impact, effective and inclusive strategies or policies, and all the Dimensions built into that leadership. Every category asks for practice that is effective and inclusive. Each Descriptor leads to an Advance HE Fellowship category, directly or through an accredited institutional programme.

## Part S Standard

{s1("the Descriptors (pages 6 to 10) and the recognition page (page 11) of the PSF 2023; the purpose and the Dimensions are in std:doc:advancehe-psf-dimensions-2023-framework")}
### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "four Descriptors of broad categories of practice in teaching and supporting learning in higher education, each with three criteria (pages 6 to 10), and how they lead to recognition (page 11)"
appliesTo:
  awards: [Associate Fellow, Fellow, Senior Fellow, Principal Fellow]
  levels: [psf:d1, psf:d2, psf:d3, psf:d4]
  providers: "institutions with accredited development programmes (recognition.2)"
whoMustUse: none-stated   # voluntary
howUsed: [individual claims for recognition, development planning, institutional development and recognition programmes, career and progression pathways, professional bodies' recognition frameworks]
recognitionRoute: "a person who meets a Descriptor is recognised by Advance HE with the matching Fellowship category, directly or by completing an accredited institutional programme (recognition.1, recognition.2)"
doesNot: "define the Dimensions (companion document) or say how evidence is judged (Advance HE's own guidance, W-std-0021)"
beneficiary: "staff who teach or support learning in higher education"
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary. The issuer numbers the Descriptors D1 to D4 and their criteria D1.1 to D4.3; the explanatory bullets, introductions and lead-ins are unnumbered and named here. -->
```yaml
components:
  - {{ number: about, componentType: section, parent: none, heading: "Descriptors: What are Descriptors?", items: 6 }}
''' + '\n'.join(f'  - {{ number: {d}, componentType: level, parent: none, heading: "Descriptor {d[1]}", items: [{d}/intro, {d}/stem, {d}.1, {d}.2, {d}.3, {d}/aligns] }}' for d in ['D1', 'D2', 'D3', 'D4']) + f'''
  - {{ number: recognition, componentType: section, parent: none, heading: "Relationship to Advance HE individual professional recognition and institutional accreditation", items: 3 }}
companions:
  - {{ id: std:doc:advancehe-psf-dimensions-2023-framework, holds: "the purpose (page 2), the Dimensions (pages 4, 5) and the terms (Part B)" }}
statements: {n_des}
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. {n_des} records: 6 about the Descriptors, 4 introductions (D4's in two sentences), 4 lead-ins, {n_crit} criteria, 4 recognition alignments, 3 on recognition and accreditation. Force: the criteria and their lead-ins are `threshold`, the conditions a claim must evidence (D-std-0004); the rest `describes`. The criteria are noun phrases completing their lead-in, so most carry no verb of their own; `requires` gives, in our terms, which Dimensions each criterion names. -->
```yaml
{chr(10).join(recs)}
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for those who lead, mentor, review or design recognition and development. forBeneficiary: for the person making a claim, in the second person. These are the phrases agents use (Abbott, 10:18). -->
```yaml
{chr(10).join(vers)}
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - {{ id: psf:d1, role: defines, locator: "Descriptor 1 (page 7)", typical: Associate Fellow }}
  - {{ id: psf:d2, role: defines, locator: "Descriptor 2 (page 8)", typical: Fellow }}
  - {{ id: psf:d3, role: defines, locator: "Descriptor 3 (page 9)", typical: Senior Fellow }}
  - {{ id: psf:d4, role: defines, locator: "Descriptor 4 (page 10)", typical: Principal Fellow }}
dimensionsUsed: {{ ids: "psf:V1 to psf:A5", definedIn: std:doc:advancehe-psf-dimensions-2023-framework }}
crosswalks:
  - {{ from: psf:d1, to: "Advance HE Associate Fellow", relation: equivalent, source: "D1/aligns: the issuer's 'aligns with'" }}
  - {{ from: psf:d2, to: "Advance HE Fellow", relation: equivalent, source: "D2/aligns" }}
  - {{ from: psf:d3, to: "Advance HE Senior Fellow", relation: equivalent, source: "D3/aligns" }}
  - {{ from: psf:d4, to: "Advance HE Principal Fellow", relation: equivalent, source: "D4/aligns" }}
  # no crosswalk to any qualification framework is stated, and none is inferred here (framework rule 2)
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- {{ theme: "inclusion", where: "D1/3, D2/3, D3/2, D4/2", note: "every category asks for inclusive practice" }}
- {{ theme: "leadership", where: "D3/1, D4/1, D4/2, D4/3", note: "influence at D3, strategic leadership at D4" }}
```

### S7 Relations
```yaml
- {{ rel: companionOf, target: std:doc:advancehe-psf-dimensions-2023-framework, note: "one framework, two documents (Abbott, 10:20; D-std-0013); the criteria cite its Dimension ids" }}
- {{ rel: describedBy, target: ing:doc:professional-standards-framework-advance-he-2023, note: "ing's theory-side document on the same PDF (run 0053)" }}
- {{ rel: supersedes, target: "UKPSF 2011 descriptors D1 to D4", note: "not stated in the document; std's knowledge, P2 to confirm (W-std-0022)" }}
```

### S8 Currency and review
```yaml
published: 2023
lastReviewed: none-stated
reviewCycle: none-stated
consultation: "none stated in the document; Abbott reports he was a member of Advance HE's consultation team (S1)"
replacedBy: none known
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: inferred. Our reading; nothing here is the issuer's. -->
- **A staff ladder beside the student spine.** D1 to D4 step professional practice, not qualification level. They do not map to `spine:4` to `spine:8`, and no crosswalk is stated. A Fellowship scheme often sits beside a postgraduate certificate at FHEQ 7; that is a programme's choice, not the framework's.
- **Two kinds of step.** D1 to D2 is a step in coverage (some to all Dimensions, in one's own practice). D2 to D3 changes whose practice counts (one's own to others'). D3 to D4 changes the scale (influence to strategic leadership with wide impact).
- **For writers of mentoring and review prompts:** the criteria name what to evidence, not how much; Advance HE's guidance per Descriptor (W-std-0021) and a scheme's own criteria set the judgement.

### SL Level language
<!-- label: both; status: drafted; basis: primary. Our words, built from S4 and S4a; the issuer's words appear only as single terms in quotation marks. -->

#### SL1 What defines each level
| Level | For the practitioner | For the applicant |
|---|---|---|
{sl1}

#### SL2 The level table, by part
| Level | Professional Values | Core Knowledge | Areas of Activity | Beyond the Dimensions |
|---|---|---|---|---|
| `psf:d1` | those that fit the role; V1 and V3 at least | those that fit the role; K1, K2 and K3 at least | two or more, effective and inclusive | none |
| `psf:d2` | all five | all five | all five, effective and inclusive | none |
| `psf:d3` | all, integrated | all, integrated | all, integrated; effective and inclusive | a sustained record of leading or influencing others; practice well beyond direct teaching or support |
| `psf:d4` | all, built into strategic leadership | all, built into strategic leadership | all, built into strategic leadership | sustained, effective strategic leadership with wide impact; effective, inclusive strategies, policies, procedures or initiatives |

#### SL3 Verbs by level
| Level | Lead-in | Criteria (the issuer's head words, first occurrence kept) |
|---|---|---|
| `psf:d1` | demonstrated through evidence of | use; application; practice |
| `psf:d2` | demonstrated through evidence of | use; application; practice |
| `psf:d3` | able to evidence | leading, influencing; integrates; extends |
| `psf:d4` | able to evidence | leadership; development, implementation; commitment, integration |

#### SL4 How progression is communicated
<!-- Each thread follows one quality up the Descriptors; the issuer's single words in quotation marks, otherwise our short reading. -->
- **Coverage of the Dimensions:** D1: "some", with named minimums; D2: "all"; D3: all, "integrates"; D4: all, "integration" within strategic leadership.
- **Whose practice:** D1 and D2: the person's own, with learners; D3: others who teach or support learning; D4: an institution, beyond it, a discipline or a profession.
- **Reach:** D3: "beyond" direct teaching; D4: "extensive" impact, "strategic".
- **Time:** D1 and D2: none stated; D3 and D4: "sustained" record.
- **Experience:** D2: "breadth and depth"; D3: "comprehensive" understanding; D4: "highly experienced".
- **Quality words:** "effective" and "inclusive" at every level; "high-quality" learning from D2 up.
- **What is evidenced:** D1 and D2: practice, through evidence of the criteria; D3 and D4: the person is "able to evidence" a record.

#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **Noun-phrase criteria.** Every criterion is a noun phrase completing its lead-in ("use of", "application of", "a sustained record of"), so verbs carry little; the step sits in quantifiers (some, at least, all), in whose practice, and in reach.
- **Named minimums at D1 only.** D1 is the only Descriptor that names Dimensions (V1, V3, K1 to K3) and a count (two Areas of Activity); higher Descriptors take all fifteen as given.
- **Integration as the step to D3.** "All" (D2) becomes "integrates all" (D3): from covering the Dimensions to joining them up.
- **Agent use.** For a claim, name the category, then evidence each criterion in the person's own setting (the Dimensions' lead-ins), using the forBeneficiary versions as prompts.

#### SL6 Recognition categories
| Level | Category (as each Descriptor states) | Route |
|---|---|---|
| `psf:d1` | Associate Fellow | direct claim or accredited programme (recognition.1, recognition.2) |
| `psf:d2` | Fellow | as above |
| `psf:d3` | Senior Fellow | as above |
| `psf:d4` | Principal Fellow | as above |

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
`see std:doc:advancehe-psf-dimensions-2023-framework`, Part B: the terms for both PSF documents are held there once (framework rule 4).

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`described`: S2 gives the recognition route in brief; the procedure itself is Advance HE's and an accredited institution's (W-std-0021).

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE (copyright Advance HE, GuildHE, Universities UK)
  title: "Professional Standards Framework for teaching and supporting learning in higher education 2023"
  edition: 2023 (screen-reader compatible version)
  year: 2023
  url: unknown   # www.advance-he.ac.uk named on page 11
  retrieved: "PDF attached by Abbott, 2026-10-03, 09:49"
  licence: "all rights reserved; held by permission (S1)"
  tier: primary
  readVia: direct
  held: {RAW}
  heldFiles: [wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.txt, wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, SL]
```

### D2 Research log
```yaml
- {{ ref: D1, tier: primary, consulted: {STAMP[:10]}, pass: P1, outcome: "read whole, direct; as the Dimensions document's D2 (one held text for both)" }}
- {{ ref: "run-src (in the Dimensions document's folder): psf_data.py, psf_build.py", tier: method, consulted: {STAMP[:10]}, pass: P1, outcome: "built by script with the Dimensions document; spans and verbs checked; `source` holds the issuer's statements; rephrasings checked for no nine-word run of the held text" }}
```

### D3 Wanted sources
```yaml
- {{ w: W-std-0021, citation: "Advance HE's guidance notes for the PSF 2023, one per Descriptor, and its glossary", settles: [S2, S9, C0], asked: not yet, state: wanted }}
- {{ w: W-std-0022, citation: "the UK Professional Standards Framework (UKPSF) 2011, the predecessor, and Advance HE's account of the 2023 review", settles: [S7, S8], asked: not yet, state: wanted }}
```

## Part E Gaps and questions
- S1, licence: as the Dimensions document's Part E: source statements held in full on Abbott's permission and direction (10:18, 10:56; D-std-0014).
- S4: the issuer's page for D2 runs "high-" and "quality" across a line; the extraction joins them as one word, kept in the held text as extracted.
- S4, force: the criteria are `threshold`: a claim at a category must evidence all three. The introductions say who a Descriptor suits and are `describes`.
- S4, `requires`: our reading of which Dimensions a criterion names; "appropriate" at D1 is left to the role (`plus: the others that fit the role`).
- S5: the recognition categories are recorded as stated ("aligns with"); no link to the qualification spine is stated or inferred.
- Names, kind and knowledgePath: as the Dimensions document's Part E.

---

## Change notes
- 0.1.1, 3 October 2026, 10:56: each S4 record now carries the issuer's statement in full (`source`, `quote: full`) for language analysis, beside our rephrasings (Abbott, 10:56; D-std-0014).
- 0.1.0, 3 October 2026, 10:28: researched by run frame 0.1.1-draft and standards run layer 0.6.1-draft, std, run 0068 (P1), with the Dimensions document; held and rephrased on Abbott's permission (D-std-0013).
'''

for name, doc in [('ingest-std-advancehe-psf-dimensions-2023-framework', dimdoc), ('ingest-std-advancehe-psf-descriptors-2023-framework', desdoc)]:
    p = os.path.join(STD, name, name + '.md')
    open(p, 'w').write(doc)
    print(p, doc.count('\n'), 'lines')
print('dimensions records', n_dim, 'descriptors records', n_des)
