# Stage 2 sections for the FHEQ document (run 0047). Imported by fheq_build.py.
import json, re, collections
S = '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
H = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
norm = open(H + '/qaa-frameworks-2024.norm.txt', encoding='utf-8').read()
q = lambda s: json.dumps(s, ensure_ascii=False)
ad = {}; exec(open(S + '/fheq2_annexd.py').read(), ad); db = {}; exec(open(S + '/fheq2_dublin.py').read(), db); pv = {}; exec(open(S + '/fheq2_provider.py').read(), pv); tb = {}; exec(open(S + '/fheq2_tables.py').read(), tb)
AD = json.load(open(S + '/fheq2-annexd.json')); DB = json.load(open(S + '/fheq2-dublin.json'))
ID = lambda i: f'qaa/fheq-2024/{i}'
BANDL = {'ns': 'Not successful', '3rd': 'Third-class honours (3rd, pass or threshold)', '2.2': 'Lower second-class honours (2.2)', '2.1': 'Upper second-class honours (2.1)', '1st': 'First-class honours (1st)', '3rd-1st': '3rd to 1st (one cell across all four classifications)'}
STRL = {'summary': 'Summary table', 'knowledge': 'Knowledge and understanding', 'cognitive': 'Cognitive skills', 'practical': 'Practical skills', 'transferable': 'Transferable skills', 'professional': 'Professional competences'}
def span_of(r):
    a, b = r['se']; s = norm.index(a); return s, norm.index(b, s) + len(b)

def s3():
    o = []
    for c in AD['components']:
        if '/lead/' in c['id']:
            b = c['id'].rsplit('/', 1)[1]
            o.append(f'  - {{ number: "{c["id"]}", componentType: stem, parent: "annex-d/summary", heading: {q("the lead of the " + BANDL[b] + " column: " + ("course outcomes not achieved" if b == "ns" else "all course outcomes achieved, and"))} }}')
        else:
            k = c['id'].split('/')[1]
            o.append(f'  - {{ number: "{c["id"]}", componentType: strand, parent: "Annex D", heading: {q(STRL[k])}, gloss: {q(ad["DEFS"][k])} }}')
    o.append(f'  - {{ number: "annex-d/summary", componentType: strand, parent: "Annex D", heading: "Summary table (four rows)", gloss: {q(ad["DEFS"]["summary"])} }}')
    for cy, (lid, name, short) in db['CY'].items():
        o.append(f'  - {{ number: "annex-b/{cy}", componentType: stem, parent: "Annex B", heading: {q("the " + short + ": qualifications marking its completion are awarded to students who (list)")}, level: {lid} }}')
    for i, r in pv['R'].items():
        if r['para'] == 'stem':
            o.append(f'  - {{ number: "{i}", componentType: stem, parent: "{r["loc"]}", heading: {q(r["about"])} }}')
    return '\n'.join(o)

def s4():
    o = []
    for i, r in pv['R'].items():
        if r['para'] == 'stem': continue
        s, e = span_of(r); stem = ID(i.rsplit('.', 1)[0]) if re.search(r'\.b\d+$', i) and i.rsplit('.', 1)[0] in pv['R'] else 'none'
        o.append(f'''- id: {ID(i)}
  locator: {{ number: "{i}", headingPath: [{q(r['loc'])}] }}
  span: {{ start: {s}, end: {e} }}
  stem: {stem}
  statementType: provider-requirement
  force: {r['force']}
  forceBasis: {r['basis']}
  level: none
  addressee: {q(r['addr'])}
  verbs: [{', '.join(r['verbs'])}]
  about: {q(r['about'])}
  themes: [none]
  paraphrase: {q(r['para'])}
  quote: none
  audience: {'both' if r['ben'] else 'practitioner'}
  subjects: inherited''')
    for c in DB:
        r = db['B'][c['id']]; lid = db['CY'][c['cycle']][0]
        o.append(f'''- id: {ID(c['id'])}
  locator: {{ number: "{c['id']}", headingPath: ["Annex B: Dublin descriptors", {q(db['CY'][c['cycle']][2])}] }}
  span: {{ start: {c['span'][0]}, end: {c['span'][1]} }}
  stem: {ID('annex-b/' + c['cycle'])}
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: {lid}
  dimension: {['knowledge-and-understanding', 'applying-knowledge', 'making-judgements', 'communication', 'learning-skills', 'wider-contribution'][int(c['id'][-1]) - 1]}
  addressee: student
  verbs: [{', '.join(r['verbs'])}]
  about: {q(r['about'])}
  themes: [none]
  paraphrase: {q(r['para'])}
  quote: none
  audience: both
  subjects: inherited''')
    for c in AD['cells']:
        r = ad['D'][c['id']]
        o.append(f'''- id: {ID(c['id'])}
  locator: {{ number: "{c['id']}", headingPath: ["Annex D", {q(STRL[c['strand']])}, {q(BANDL[c['band']])}] }}
  span: {{ start: {c['span'][0]}, end: {c['span'][1]} }}
  stem: {ID('annex-d/summary/lead/' + c['band']) if c['strand'] == 'summary' else 'none'}
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: {c['strand']}
  band: {q(c['band'])}
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [{', '.join(r['verbs'])}]
  about: {q(r['about'])}
  themes: [none]
  paraphrase: {q(r['prac'])}   # for grid cells the paraphrase is the practitioner version
  quote: none
  audience: {'both' if r['ben'] else 'practitioner'}
  subjects: inherited''')
    return '\n'.join(o)

def s4a():
    o = []
    NAB = 'not-applicable: addressed to providers alone'
    for i, r in pv['R'].items():
        if r['para'] == 'stem': continue
        ben = f'{{ text: {q(r["ben"])}, rewrite: full, force: {r["force"]}, status: drafted }}' if r['ben'] else q(NAB)
        o.append(f'''- statement: {ID(i)}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: {r['force']}, status: drafted }}
  forBeneficiary: {ben}''')
    for c in DB:
        r = db['B'][c['id']]
        o.append(f'''- statement: {ID(c['id'])}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: describes, status: drafted }}
  forBeneficiary: {{ text: {q(r['ben'])}, rewrite: full, force: describes, status: drafted }}''')
    for c in AD['cells']:
        r = ad['D'][c['id']]
        ben = f'{{ text: {q(r["ben"])}, rewrite: full, force: describes, status: drafted }}' if r['ben'] else '"not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"'
        o.append(f'''- statement: {ID(c['id'])}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: describes, status: drafted }}
  forBeneficiary: {ben}''')
    return '\n'.join(o)

def s5():
    o = ['  # Table 1 (read from the page image, printed page 12): the qualification-level crosswalk. Equivalence holds per qualification, not per level: FHEQ 6 sits beside SCQF 10 for honours and SCQF 9 for other bachelor\'s and graduate awards.']
    for name, f, s, cy in tb['T1']:
        o.append(f'  - {{ qualification: {q(name)}, fheq: {f}, fqheis: {q(s) if s == "NA" else s}, qfehea: {q(cy) if cy else q("none (shaded: short of the cycle's expectations, 3.7)")}, source: "Table 1" }}')
    o.append('  - { from: "qfehea:3, qfehea:2, qfehea:1, qfehea:short", to: "fheq and fqheis, by qualification as above", relation: corresponds, source: "Table 1; 2.20; Annex B" }')
    cr = ['credit:   # Annex C, read from the page images (printed pages 40 to 43); values exactly as printed, typical minimum credit per qualification, with any minimum or maximum at a stated level in brackets; qualification names and values are data, copied exactly']
    for name, f, s, en, sc, wa, ec in tb['AC']:
        cr.append(f'  - {{ qualification: {q(name)}, fheq: {f}, scqf: {q(s) if s == "NA" else s}, englandNI: {q(en)}, scotland: {q(sc)}, wales: {q(wa)}, ects: {q(ec) if ec else "shaded"} }}')
    return '\n'.join(o), '\n'.join(cr)

def sl():
    C = {b: collections.Counter() for b in ['ns', '3rd', '2.2', '2.1', '1st']}
    WL = ['not', 'inadequate', 'insufficient', 'limited', 'little', 'lack', 'weak', 'some', 'general', 'sound', 'strong', 'good', 'consistently', 'thorough', 'thoroughly', 'well-developed', 'sophisticated', 'critical', 'critically', 'advanced', 'exceptional', 'independent', 'independently', 'autonomously', 'autonomy', 'beyond', 'perceptively', 'accomplished', 'high', 'wide', 'extensive', 'innovative', 'originality', 'flair']
    for c in AD['cells']:
        if c['band'] not in C: continue
        t = ' '.join(norm[c['span'][0]:c['span'][1]].lower().split())
        for w_ in WL: C[c['band']][w_] += len(re.findall(r'\b' + re.escape(w_) + r'\b', t))
    o = ['''
#### SL6 The classification bands (Annex D)
<!-- How the four classes and the not-successful column are told apart: our reading, with a count of the issuer's degree words per band across all 104 cells (the issuer's single words, counted from the held text). -->

| Band | What marks it | Degree words, counted |
|---|---|---|''']
    MARK = {'ns': 'Absence and inconsistency: outcomes not achieved; the skill is "not" shown, "little or no", "inadequate", or not "consistently".', '3rd': 'Presence: the skill is shown, mostly with no qualifier at all; "some" and "general" where one is used. All course outcomes achieved: the threshold.', '2.2': 'Consistency: the commonest qualifier by far; "strong" and "sound" for quality; at times going past the set range.', '2.1': 'Thoroughness and criticality: "thorough", "critically", "wide"; first autonomy in decisions; going past the set range usually.', '1st': 'Exception and independence: "exceptional" dominates; "beyond" the threshold and the taught; independence, autonomy, originality, flair.'}
    for b in ['ns', '3rd', '2.2', '2.1', '1st']:
        cnt = ', '.join(f'{k} {v}' for k, v in C[b].most_common() if v)
        o.append(f'| {BANDL[b]} | {MARK[b]} | {cnt} |')
    o.append('''
#### SL7 The Dublin step changes (Annex B)
<!-- The annex's own comparison of the cycles, element by element (the Joint Quality Initiative's), in our short reading with the issuer's words in quotation marks a few at a time. -->
''')
    T = [('Knowledge and understanding', 'short cycle: at the level of "advanced textbooks"; first: some of it "informed by knowledge at the forefront"; second: a "basis or opportunity for originality", often in research; doctorate: "systematic understanding" and "mastery of the methods of research"'),
         ('Applying knowledge', 'short cycle: in "occupational context"; first: by "devising and sustaining arguments"; second: problem-solving in "new or unfamiliar environments"; doctorate: a "substantial process of research" that "extends the frontier of knowledge"'),
         ('Making judgements', 'short cycle: data for "well-defined concrete and abstract problems"; first: "gathering and interpreting relevant data"; second: "handle complexity", judging "with incomplete data"; doctorate: "critical analysis, evaluation and synthesis"'),
         ('Communication', 'short cycle: with "peers, supervisors and clients"; first: "information, ideas, problems and solutions"; second: conclusions and their rationale to "specialist and non-specialist audiences"; doctorate: with peers, scholars and "society in general"'),
         ('Learning skills', 'short cycle: "with some autonomy"; first: "a high level of autonomy"; second: "largely self-directed or autonomous"; doctorate: promoting "technological, social or cultural advancement"')]
    for a, b in T: o.append(f'- **{a}:** {b}.')
    o.append('''
#### SL8 Observations on stage 2
<!-- label: editorial; status: drafted; basis: primary -->
- **Annex D is a marking scale for one level.** It holds the honours threshold (3rd) fixed and grades upwards by a small ladder of qualifiers, the same in every strand: shown, then consistently, then thoroughly and critically, then exceptionally and independently. It is the pattern Bristol's and Cardiff Met's criteria follow within each level (the assessment-criteria variant, next).
- **The third is the threshold.** The annex says so ("3rd (pass or threshold)"), and the 3rd column's wording is the descriptor's wording almost unqualified. A pathway's pass statement and an honours descriptor are the same thing said twice.
- **Failure is described as absence or inconsistency, not as a lower level.** "Did not consistently demonstrate" is the summary's failure form: the same skill, shown unreliably.
- **The Dublin descriptors climb by autonomy and by reach.** Their learning-skills line is the clearest single progression in the document: "some autonomy", "a high level", "largely self-directed", then promoting advancement in society.
- **The provider statements are mostly present-tense rules** ("degree-awarding bodies ensure"), not "must"; their force is inferred as `must` where the sentence states a condition of award or title (`forceBasis: inferred`).''')
    return '\n'.join(o)

def partB():
    o = ['```yaml']
    for k, g in pv['TERMS']:
        o.append(f'- {{ term: {q(k)}, gloss: {q(g)}, locator: "Definitions", basis: paraphrase }}')
    o.append('- { term: "Abbreviations", gloss: "CQFW, EQF, FHEQ, FQHEIS, OfS, PSRBs and QF-EHEA are expanded in the Definitions; recorded in S1, S5 and S7 where used", locator: "Definitions", basis: paraphrase }')
    o.append('```')
    return '\n'.join(o)

def partC():
    return '''### C0 Formality
`described`: section 6 sets out what degree-awarding bodies do; the steps are its, the order ours.

### C1 Steps
```yaml
- { step: 1, name: position the qualification, does: "set its framework level by the level most of its outcomes match (6.1)", statements: [6.1.a, 6.1.b] }
- { step: 2, name: approve the course, does: "course approval checks the threshold standard and the awarding body's own standards (6.2); design and review weigh alignment, volume, opportunity and PSRB requirements (6.3)", statements: [6.3.b1, 6.3.b2, 6.3.b3, 6.3.b4] }
- { step: 3, name: assess, does: "judge performance against the standards set (6.5)", statements: [6.5] }
- { step: 4, name: award, does: "award only when outcomes are shown in full; fall-back awards only on their own outcomes; compensation and condonement never replace achievement (6.4, 6.6, 6.7)", statements: [6.4, 6.6, 6.6.b1, 6.6.b2, 6.7.b1, 6.7.b2, 6.7.b3] }
- { step: 5, name: classify (honours), does: "place the honours award in a class by Annex D (2.8)", statements: ["annex-d/*"] }
- { step: 6, name: title, does: "title the award by level, volume, nature and field (6.8 to 6.19)", statements: [6.9, 6.10.b1, 6.10.b2, 6.10.b3, 6.11.a, 6.11.b, 6.13.b2, 6.13.b3, 6.14.b1, 6.14.b2, 6.14.b3, 6.14.b4, 6.14.b5, 6.15, 6.16, 6.17, 6.18.b1, 6.18.b2, 6.19] }
- { step: 7, name: record, does: "give the student a record of study: transcript, Diploma Supplement or HEAR (5.7)", statements: [] }
```'''
