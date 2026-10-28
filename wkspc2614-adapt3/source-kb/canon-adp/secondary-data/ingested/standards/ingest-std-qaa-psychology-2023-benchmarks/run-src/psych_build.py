#!/usr/bin/env python3
"""Build qaa-psychology-2023.md (run 0043) from the skeleton, the judgement fields and the S3 glosses."""
import json, sys
S = '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
skel = json.load(open(f'{S}/psych-skel.json'))
ns = {}; exec(open(f'{S}/psych_judgement.py', encoding='utf-8').read(), ns)
P, GRADE, WEAK, OUTCOMES = ns['P'], ns['GRADE'], ns['WEAK'], ns['OUTCOMES']
g = {}; exec(open(f'{S}/psych_s3.py', encoding='utf-8').read(), g); SUB, G = g['SUB'], g['G']
q = lambda s: json.dumps(s, ensure_ascii=False)
def key(n):
    try: return tuple(int(x) for x in n.split('.'))
    except ValueError: return None
def sub_for(n):
    k = key(n)
    for a, b, h in SUB:
        if k and key(a) <= k <= key(b): return h
    return None
spans = {c['id'].split('/')[-1]: c['span'] for c in skel['candidateStatements']}
comp = {c['number']: c for c in skel['components']}
for i in P:
    if i not in spans: spans[i] = {'start': comp[i]['start'], 'end': comp[i]['end']}
def order(i):
    base, _, b = i.partition('.b'); return key(base) + ((int(b),) if b else (0,))
IDS = sorted(P, key=order)
RV = {'4.8': 'threshold', '4.9': 'typical', '4.10': 'excellent'}
TH = {'1.18': 'theme:edi', '1.24': 'theme:accessibility'}  # only statements in a theme's own paragraphs: tags are what the source says

out = []
w = out.append
w('---')
w(f'''id: std:doc:qaa-psychology-2023-benchmarks
title: Subject Benchmark Statement Psychology
profile: standards/subject-benchmark
profileVersion: 0.1.3-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - {{ scheme: hecos, code: "100497", label: psychology, basis: stated }}
  - {{ scheme: cah, code: CAH04-01-01, label: psychology (non-specific), basis: stated }}
  - {{ scheme: cah, code: CAH04-01, label: psychology, basis: stated }}
  - {{ scheme: cah, code: CAH04, label: psychology, basis: stated }}
  - {{ scheme: hecos, code: "100993", label: cognitive psychology, basis: stated }}
  - {{ scheme: hecos, code: "100952", label: developmental psychology, basis: stated }}
  - {{ scheme: hecos, code: "100498", label: social psychology, basis: stated }}
  - {{ scheme: hecos, code: "100959", label: research methods in psychology, basis: stated }}
  - {{ scheme: hecos, code: "101344", label: psychobiology, basis: inferred }}
edition: September 2023
published: 2023-09
status: current
supersedes: none
heldText: {{ method: sha256-bytes, raw: {skel['heldText']['raw']}, normalised: {skel['heldText']['normalised']} }}
heldTextStan: {{ method: sha256-stan, raw: {skel['heldTextStan']['raw']}, normalised: {skel['heldTextStan']['normalised']} }}
licence: QAA copyright; held for study, never published (re-use terms to check, Part E)
series: QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (2022 onward; recall, to check)
awardsCovered: ["bachelor's with honours", "master's conversion"]
levelsCovered: [fheq:6, fheq:7, fqheis:10, fqheis:11]
nations: [England, Wales, Scotland, Northern Ireland]
parts:
  S: full
  B: "partial: no glossary in the document; terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: {{ structure: 0.13.0-draft, template: 0.4.0-draft, benchmarkTemplate: 0.4.0-draft, runFrame: 0.1.1-draft, runLayer: 0.4.0-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.4.0-draft; std, run 0043
passes:
  P1: 2026-10-03, std (claude.ai, META Project)
  P2: "skipped: no trigger beyond the inferred codes and rung links, which P3 settles"
  P3: open
version: 0.1.0''')
w('---\n')
w('''<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.4.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.4.0-draft -->
# Subject Benchmark Statement: Psychology (QAA, September 2023)

> Run 0043, P1 by std. The issuer's words are held beside this document's collection (`wkspc2601-library/txt/qaa-2023-psychology-subject-benchmark-statement-standard.norm.txt`) and never copied here: every statement points into them by character span. Everything else is our words. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Psychology should know and be able to do at the end of an honours degree or a master's conversion course: the subject's outcome lists and its three rungs of achievement (threshold, typical, excellent). Reach for it when designing, reviewing or describing a psychology course or its outcomes. It is not a curriculum, not the professional body's accreditation standard and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in September 2023 for the sector, the statement describes the discipline, its purposes and distinctive features, the content, skills, teaching and assessment of a degree, and benchmark standards at threshold, typical and excellent levels for bachelor's degrees with honours and master's conversion courses. It adds the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship), points to QAA's degree classification descriptions (Annex D) for the generic skills each classification shows, and sets the subject beside its professional body (BPS) and regulator (HCPC). Providers, external examiners and PSRBs use it in design, approval and review; it replaced the previous Psychology statement (edition and date not given in the text: Part E).

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: Subject Benchmark Statement Psychology
edition: September 2023
dates:
  published: 2023-09
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: 'reference'   # a sector reference point, "not a regulatory requirement" (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation)
licence: 'QAA copyright; the document gives no re-use terms in its text (D1, front matter)'
copyrightNotice: { text: "''' + skel['copyrightNotice'] + '''", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: 'what a Psychology graduate can be expected to know, do and understand at the end of an honours degree or a master''s conversion course, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 1.16; 4.1)'
appliesTo:
  awards: ["bachelor's degrees with honours, BPS-accredited or not", "master's conversion courses", "integrated master's (described, 2.10)"]
  levels: [fheq:6, fheq:7, fqheis:10, fqheis:11]
  providers: [UK higher education providers]
whoMustUse: none-stated; it is a reference point, not a requirement (D1, front matter)
howUsed: [design, approval, review, other: external examining; PSRBs' reference for academic standards; information for prospective students and employers]
doesNot: it is not a national curriculum and does not prescribe teaching, learning or assessment; it does not interpret legislation or carry statutory or regulatory requirements (D1, front matter)
beneficiary: the student
statedScope: '"This Subject Benchmark Statement applies to conversion level as well as undergraduate courses." (D1, 1.16)'
statedSubjects:
  - { name: Psychology, locator: (D1, title; 1.1), kind: subject, codes: [{ scheme: hecos, code: "100497", label: psychology }, { scheme: cah, code: CAH04-01-01, label: psychology (non-specific) }] }
  - { name: "conversion degree at master's level", locator: (D1, 1.16; 2.8; 4.5), kind: programme title, codes: [{ scheme: hecos, code: "100497", label: psychology }] }
  - { name: "single honours ... joint honours ... combined joint or major/minor honours", locator: (D1, 1.13), kind: programme title, codes: [{ scheme: hecos, code: "100497", label: psychology }] }
  - { name: "Bachelor's degree in Science (BSc) or Arts (BA)", locator: (D1, 2.1), kind: programme title, codes: [{ scheme: hecos, code: "100497", label: psychology }] }
  - { name: Biological psychology, locator: (D1, 3.4), kind: specialism, codes: [] }
  - { name: Cognitive psychology, locator: (D1, 3.4), kind: specialism, codes: [{ scheme: hecos, code: "100993", label: cognitive psychology }] }
  - { name: Developmental psychology, locator: (D1, 3.4), kind: specialism, codes: [{ scheme: hecos, code: "100952", label: developmental psychology }] }
  - { name: Individual differences, locator: (D1, 3.4), kind: specialism, codes: [] }
  - { name: Social psychology, locator: (D1, 3.4), kind: specialism, codes: [{ scheme: hecos, code: "100498", label: social psychology }] }
  - { name: Methods of research and enquiry, locator: (D1, 3.6), kind: specialism, codes: [{ scheme: hecos, code: "100959", label: research methods in psychology }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
''')
w('```yaml\ncomponents:')
sections = {'1': 'Context and purposes of a Psychology Degree', '2': 'Distinctive features of a Psychology degree', '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
for c in skel['components']:
    n = c['number']
    if c['excluded']: continue
    par = n.split('.')[0]
    ct = 'stem' if c.get('componentType') == 'stem' and n not in ('2.8',) else 'section' if n in ('3.4', '3.25') and False else 'paragraph'
    if n in ('3.4', '3.25'): ct = 'stem'
    if n == '2.8': ct = 'paragraph'
    w(f'  - {{ number: "{n}", order: {c["order"]}, componentType: {"area" if n == "3.4" else "practice" if n == "3.25" else ct}, parent: "section {par}", heading: {q(sub_for(n) or c["heading"])}, gloss: {q(G.get(n, "unknown"))} }}')
for k, v in sections.items():
    w(f'  - {{ number: "{k}", componentType: section, parent: none, heading: {q(v)}, gloss: "section {k}" }}')
w('''excluded:
  - { number: none, heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: none, heading: Contents, kind: contents }
  - { number: "5", heading: List of references and further resources, kind: references }
  - { number: "6", heading: Membership of the Advisory Group, kind: acknowledgements }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 61 records. The issuer's words are each record's span; never copied here. -->
```yaml''')
for i in IDS:
    r = P[i]; sp = spans[i]; stem = i.rsplit('.b', 1)[0] if '.b' in i else None
    aw = r['award'] if isinstance(r['award'], list) else [r['award']]
    gr = GRADE.get(i)
    th = TH.get(i, 'none')
    w(f'''- id: qaa/psychology-2023/{i}
  locator: {{ number: "{i}", headingPath: [{q(sections[i.split('.')[0]])}, {q(sub_for(i.split('.b')[0]) or '')}] }}
  span: {{ start: {sp['start']}, end: {sp['end']} }}
  stem: {('"' + stem + '"') if stem else 'none'}
  statementType: {r['type']}
  rung: {r['rung']}
  force: {r['force']}
  level: {r['level']}
  appliesTo: {q(r['appliesTo'])}
  addressee: {r['addressee']}
  verbs: [{', '.join(r['verbs'])}]
  about: {q(r['about'])}
  themes: [{th}]
  domain: {r['domain']}
  award: [{', '.join(q(a) for a in aw)}]
  gradeOf: {('{ statement: qaa/psychology-2023/' + gr + ', basis: inferred }') if gr else 'none'}
  paraphrase: {q(r['para'])}
  quote: none
  audience: {'practitioner' if isinstance(r['ben'], tuple) else 'both'}
  subjects: inherited''')
w('```\n\n### S4a Audience versions\n<!-- label: both; status: drafted; basis: primary. Light rewrites keep the issuer\'s structure in our words; full rewrites recast it. -->\n```yaml')
nap = 0
for i in IDS:
    r = P[i]
    w(f'''- statement: qaa/psychology-2023/{i}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: {r['force']}, status: drafted }}''')
    if isinstance(r['ben'], tuple):
        nap += 1
        w(f'''  forBeneficiary: {{ text: "not-applicable: {r['ben'][1]}", rewrite: full, force: {r['force']}, status: drafted }}''')
    else:
        w(f'''  forBeneficiary: {{ text: {q(r['ben'])}, rewrite: full, force: {r['force']}, status: drafted }}''')
w('```')
w('''
### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: fheq:6, role: cites, locator: "D1, 2.7; 4.5" }
  - { id: fheq:7, role: cites, locator: "D1, 2.10; 4.5" }
  - { id: fqheis:10, role: cites, locator: "D1, 2.7; 4.2; 4.5" }
  - { id: fqheis:11, role: cites, locator: "D1, 2.10; 4.5" }
crosswalks:
  - { from: fheq:6, to: fqheis:10, relation: equivalent, basis: "stated (D1, 2.7; 4.5: honours at level 6 in England, Wales and Northern Ireland, level 10 in Scotland)" }
  - { from: fheq:7, to: fqheis:11, relation: equivalent, basis: "stated (D1, 2.10; 4.5)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: theme:edi, role: carries, carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "3.30"] }
- { id: theme:accessibility, role: carries, carriedIn: ["1.24", "1.25", "1.26", "1.27", "2.12", "2.20"] }
- { id: theme:esd, role: carries, carriedIn: ["1.12", "1.28", "1.29", "1.30", "1.31", "1.32"] }
- { id: theme:enterprise, role: carries, carriedIn: ["1.33", "1.34", "1.35", "2.16"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "collection: QAA Subject Benchmark Statements", note: one of 54 held by stan }
- { rel: supersedes, target: "std:doc:qaa-psychology-<previous year>-benchmarks (not yet ingested)", note: "the front matter names key changes from the previous statement but not its date: Part E" }
- { rel: refersTo, target: "std:doc:qaa-fheq-2024-framework (not yet ingested; run queue S-03), Annex D", note: "the degree classification descriptions for FHEQ level 6 and FQHEIS level 10, cited as QAA 2019 (4.2, 4.6, 4.7)" }
- { rel: refersTo, target: "std:doc:fheq (not yet ingested; S-03)", note: levels 6 and 7 }
- { rel: refersTo, target: "QAA Quality Code, Advice and Guidance", note: front matter }
- { rel: refersTo, target: "BPS accreditation standards (not yet ingested)", note: "1.4, 2.8, 2.21, 3.21" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: 2023-09
lastReviewed: none-stated
reviewCycle: none-stated
consultation: none-stated
replacedBy: none
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: S9 not researched in the pilot (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- A scientific and reflective discipline studying mind, brain, experience, behaviour and socio-cultural context in human and non-human animals, both theoretical and applied, with roots in philosophy, biology and physics (D1, 1.1).
- Its aim is psychological literacy: using disciplinary knowledge and insight on real problems, ethically and critically (D1, 1.2, 2.4).
- Ethics is at its core, in research, practice and conduct (D1, 2.5, 3.21).
- It is empirical: progressive laboratory and naturalistic work across quantitative, qualitative and mixed methods, culminating in an independent project (D1, 3.6, 3.7, 3.11).
- It is evolving and interdisciplinary, and critical of its own historical narrowness of populations and voices (D1, 1.19, 2.6, 3.3, 3.5).
- Professional routes run beyond the degree, through the BPS and the HCPC (D1, 1.4, 1.6).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the discipline names its own history of marginalising groups and of research on narrow populations; it asks for diverse curricula, inclusive environments, critique of dominant systems of thought and attention to the language of mental health (D1, 1.17 to 1.23)"
  statements: [qaa/psychology-2023/1.18]
- theme: theme:accessibility
  inThisSubject: "the Equality Act's anticipatory duty in course design, reasonable adjustments in every setting and flexible alternative assessment (D1, 1.24 to 1.27); digital and blended delivery to widen access (D1, 2.12)"
  statements: [qaa/psychology-2023/1.24]
- theme: theme:esd
  inThisSubject: "headed Sustainability in the text: psychology's part in the SDGs (naming SDGs 3 to 5, 8, 11 and 16), UNESCO's key competencies as core to the curriculum, behaviour change for climate action, transformative pedagogies (D1, 1.28 to 1.32)"
  statements: []
- theme: theme:enterprise
  inThisSubject: "acknowledged as under-used in the subject; enterprise skills for employability and venture creation, through partnerships and placements (D1, 1.33 to 1.35, 2.16)"
  statements: []
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.4", gloss: "five core areas, each with example topics: biological psychology; cognitive psychology; developmental psychology; individual differences; social psychology" }
  - { component: "3.5", gloss: conceptual and historical issues; interdisciplinarity }
  - { component: "3.6", gloss: methods of research and enquiry, quantitative, qualitative and mixed (3.6 to 3.11) }
practices:
  - { component: "3.25", kind: teaching, gloss: "lectures, laboratory classes, workshops, seminars, tutorials, independent study, collaborative work, project supervision" }
  - { component: "3.26", kind: learning, gloss: "problem-based, team-based, experiential, student-led and work-based learning" }
  - { component: "3.30", kind: assessment, gloss: "a range of methods for EDI, authentic and innovative tasks, assessment for non-academic audiences" }
  - { component: "3.31", kind: assessment, gloss: "clear criteria, co-developed assessment, integrity with AI" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: threshold, leadIn: "4.8", award: "bachelor's with honours", items: 9 }
  - { rung: typical, leadIn: "4.9", award: "bachelor's with honours", items: 9 }
  - { rung: excellent, leadIn: "4.10", award: "bachelor's with honours", items: 9 }
rungBases: "4.6: typical and excellent go beyond threshold on four bases: depth and breadth of knowledge; engagement in research and independent study; critical insight; advanced application of theory and method to current issues"
outcomeLists:
  - { leadIn: "3.16", gloss: subject-specific skills at graduation, items: 15, award: [honours, conversion] }
  - { leadIn: "3.17", gloss: transferable skills at graduation, items: 11, award: [honours, conversion] }
outcomes:''')
for k in range(1, 10):
    wk = ' (weaker content match: Part E)' if ('4.9.b%d' % k in WEAK or '4.10.b%d' % k in WEAK) else ''
    w(f'  - {{ outcome: {q(OUTCOMES[k-1])}, threshold: qaa/psychology-2023/4.8.b{k}, typical: qaa/psychology-2023/4.9.b{k}, excellent: qaa/psychology-2023/4.10.b{k}, basis: inferred, domain: {P["4.8.b%d" % k]["domain"]}, award: "bachelor\'s with honours" }}{("  # " + wk.strip()) if wk else ""}')
w('''```

### SB4a Student and practitioner versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
written: fresh from the held text; no consumer's statements read (benchmark variant rule 6)
fullRewrites: []
```

### SB5 Bodies
<!-- label: source; status: drafted; basis: primary -->
```yaml
- body: British Psychological Society (BPS)
  says: "accredits undergraduate and postgraduate study and training; chartered status needs an accredited route to the Graduate Basis for Chartered Membership (a second-class degree and a passed empirical project, or an accredited conversion course at 50%) and further training; reviews accredited courses cyclically; its ethics guidance underpins teaching (D1, 1.4, 2.8, 2.9, 2.17, 2.21, 3.21, 3.22)"
  requirements: not yet ingested (Part E)
- body: Health and Care Professions Council (HCPC)
  says: "regulator protecting the public; nine practitioner psychologist titles are protected by law and need HCPC registration and approved training; course titles must not borrow them (D1, 1.5, 1.6, 1.7, 2.17, 3.22, 4.13)"
  requirements: not yet ingested (Part E)
- body: Professional Standards Authority
  says: "registers wider psychological workforce roles, such as psychological wellbeing practitioners (D1, 1.7; 4.14 calls it the Professional Standards Association, Part E)"
  requirements: not-applicable-by-design
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: theme:edi, named: "Equality, diversity and inclusion", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "3.30"], statements: [qaa/psychology-2023/1.18] }
  - { id: theme:accessibility, named: Accessibility, carriedIn: ["1.24", "1.25", "1.26", "1.27", "2.12", "2.20"], statements: [qaa/psychology-2023/1.24] }
  - { id: theme:esd, named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.12", "1.28", "1.29", "1.30", "1.31", "1.32"], statements: [] }
  - { id: theme:enterprise, named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.33", "1.34", "1.35", "2.16"], statements: [] }
frameworks:
  - { framework: fheq, levels: [fheq:6, fheq:7], citedIn: ["2.7", "2.10", "4.5"] }
  - { framework: scqf, levels: [fqheis:10, fqheis:11], citedIn: ["2.7", "2.10", "4.2", "4.5"] }   # cited by its Scottish name, FQHEIS
bodies:
  - { body: British Psychological Society, citedIn: ["1.4", "2.8", "2.9", "2.17", "2.21", "3.21", "3.22"] }
  - { body: Health and Care Professions Council, citedIn: ["1.5", "1.6", "1.7", "2.17", "3.22", "4.13"] }
  - { body: Professional Standards Authority, citedIn: ["1.7", "4.14"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D (not yet ingested: S-03, W-std-0002)", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2", "4.6", "4.7"], role: "descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd); the statement says its subject criteria accompany the annex's more generic transferable skills (4.7)" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: Advice and Guidance, citedIn: [front matter], role: course design, teaching, external expertise, monitoring }
  - { document: "QAA Glossary (not ingested)", named: QAA's Glossary, citedIn: [front matter], role: explains unfamiliar terms }
  - { document: "UN Sustainable Development Goals (external)", named: Sustainable Development Goals, citedIn: ["1.12", "1.29"], role: the frame of the sustainability theme }
  - { document: "Equality Act 2010 (law)", named: Equality Act 2010, citedIn: ["1.17", "1.24", "1.25"], role: duties behind EDI and accessibility }
  - { document: "Health Professions Order 2001 (law)", named: Health Professions Order 2001, citedIn: ["1.6"], role: protected titles }
```

## Part B Terminology
<!-- The statement has no glossary of its own and sends readers to QAA's Glossary; these are the terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: psychological-literacy, definition: "the capability to use disciplinary knowledge, theory, principles and insight to respond to opportunities and challenges (D1, 1.2)", beneficiaryDefinition: "being able to use what you know about psychology to deal with real situations", scopeNote: "used throughout as the aim of the degree", category: unknown, practices: [education] }
- { slug: subject-specific-skills, definition: "skills that relate closely to subject knowledge or are integral to any Psychology degree (D1, 2.3)", scopeNote: "contrasted with transferable skills; the line is not clear-cut (3.14)", category: unknown, practices: [education] }
- { slug: transferable-skills, definition: "skills less tied to the subject matter of psychology (D1, 2.3, 3.14)", scopeNote: "listed in 3.17", category: unknown, practices: [education] }
- { slug: graduate-basis-for-chartered-membership, definition: "the BPS standing gained by completing an accredited degree or conversion course to the stated marks (D1, 1.4, 2.8)", scopeNote: "first step to chartered psychologist", category: unknown, practices: [education] }
- { slug: conversion-course, definition: "a master's-level course letting graduates of other disciplines study psychology, accredited by the BPS (D1, 1.4, 1.16)", scopeNote: "covered by the statement", category: unknown, practices: [education] }
- { slug: threshold-standard, definition: "the minimum a student will have demonstrated to be awarded the degree (D1, 4.1, 4.8)", scopeNote: "with typical and excellent above it (4.6, 4.9, 4.10)", category: unknown, practices: [education] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: psychological-literacy, form: psychological literacy, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: subject-specific-skills, form: subject-specific skills, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
- { concept: transferable-skills, form: transferable skills, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
- { concept: graduate-basis-for-chartered-membership, form: Graduate Basis for Chartered Member, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: graduate-basis-for-chartered-membership, form: GBC, lang: en, partOfSpeech: noun, termStatus: admitted, register: discipline-specific }
- { concept: conversion-course, form: conversion course, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
- { concept: threshold-standard, form: threshold level, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: formal }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: contrasts-with, from: subject-specific-skills, to: transferable-skills, note: "3.14: the distinction is not clear-cut" }
- { rel: related, from: conversion-course, to: graduate-basis-for-chartered-membership, note: "an accredited conversion course is a direct route (1.16)" }
```

### B5 Rules
<!-- label: editorial; status: drafted; basis: discussion -->
- conversion course: say "master's conversion course", because the statement covers it beside honours degrees and a bare "conversion course" is ambiguous across subjects.

## Part C Process

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: Subject Benchmark Statement Psychology
  edition: September 2023
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction, origin below)
  retrieved: "held from stan: ''' + skel['origin'] + '''; ADAPT a3c925b; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: ''' + skel['heldText']['raw'] + '''
  heldFiles: [''' + ', '.join(skel['heldFiles']) + ''']
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6, B1, B2a]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; every part" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (ADAPT 096e25b)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { citation: "QAA (2024) The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn, Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees (first published separately in 2019, as this statement cites it)", settles: [SB6, S7, S5], asked: 2026-10-03 (W-std-0002), state: wanted }
```

## Part E Gaps and questions
- S3: the held text runs 4.1, 4.2, 4.5: no 4.3 or 4.4. Settled: the gap is in the issuer's original, not an extraction loss (Abbott, 03:47: "They're not in the original"). Recorded as the issuer's numbering; nothing is missing.
- S3, std-prep: the script read 4.6's four bullets as threshold items because the lead-in names "threshold"; they are the bases on which typical and excellent go beyond threshold (SB4 `rungBases`). Lesson for the script: a rung lead-in is "has attained the <rung> level", not any mention of the word.
- S3: 2.8's line beginning "- for example" is a wrapped clause, not a list item (the script split it): 2.8 is one paragraph statement.
- S4, D-std-0002 (a) in practice: paragraphs carrying an expected outcome in "will" inside descriptive prose (1.18, 2.5, 3.11) were taken as statements; others with predictive "will" ("many graduates will pursue careers", 1.8) were not. The line is judgement: for Abbott at P3.
- S4, force: three paragraphs oblige in words outside the list: "need to demonstrate" (3.19, providers), "it is expected that" (3.27, staff development) and "it is important that" (4.13's first sentence). Not taken as statements; for Abbott: should "expected" and "need to" read as `should`?
- S4, 3.16.b10 begins "the ability to", not a verb, breaking its list's grammar; its verbs are taken from the clause.
- SB4: the three rung lists run outcome by outcome in position (nine each); each `gradeOf` link is inferred. Weaker content matches: typical 5 to threshold 5; excellent 5, 7 and 8 to typical 5, 7 and 8.
- SB4: 4.10's lead-in adds "consistently"; every excellent version keeps it.
- S2, statedSubjects: no HECoS term for "biological psychology" or "individual differences"; psychobiology (101344) is the nearest for the first, entered in front matter as inferred.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check (template open point 3).
- S7, S0.2: the previous Psychology statement's edition and date are not given in the text.
- SB5: 1.7 names the Professional Standards Authority, 4.14 the "Professional Standards Association": the issuer's inconsistency, kept; the body is the Authority.
- SB5: the BPS's and HCPC's own requirements are not yet ingested.
- S9: not researched in the pilot.
- S4, themes: list items that touch a theme without naming it (3.17.b2 and b9 on inclusion, 3.17.b11 on employability) are not tagged, since tags are what the source says; a consumer may map them.
- Levels: `fqheis:10` and `fqheis:11` used as shared ids for the Scottish framework's levels as this statement names them; not yet in a shared level list (template open point 2).
- ST-12: the length range for audience versions is still unset; versions here run 10 to 41 words.

---

## Change notes
- 0.1.0: 2026-10-03: researched by run frame 0.1.1-draft and standards run layer 0.4.0-draft, std, run 0043 (P1).''')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('statements', len(IDS), 'beneficiary n/a', nap)
