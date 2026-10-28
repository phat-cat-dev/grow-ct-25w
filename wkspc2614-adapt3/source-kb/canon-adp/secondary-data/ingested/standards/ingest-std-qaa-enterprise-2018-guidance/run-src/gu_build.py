#!/usr/bin/env python3
"""Generic builder for `standards/guidance` documents (proposed variant; template 0.1.0-draft). std. Usage: gu_build.py <config.py> <out.md>"""
import json, re, sys, hashlib, collections
q = lambda s: json.dumps(s, ensure_ascii=False)
G = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/guidance'
cfg = {}; exec(open(sys.argv[1]).read(), cfg)
ns = {}; exec(open(cfg['JUDGE']).read(), ns); R, FAM = ns['R'], ns['FAM']
raw = open(f"{G}/{cfg['SLUG']}.txt", 'rb').read(); normb = open(f"{G}/{cfg['SLUG']}.norm.txt", 'rb').read(); norm = normb.decode('utf-8')
PW = ['reflective-practice', 'researching-and-research-methods', 'work-based-and-experiential-learning', 'finding-and-using-sources', 'criticality', 'academic-writing', 'referencing', 'understanding-learning-assessment-and-feedback', 'starting-progressing-and-succeeding', 'presenting', 'revising-and-exams', 'ai-and-technology', 'creativity']
# spans: unique start, or the next exact line after the cursor of the same family
cur = collections.defaultdict(int)
for r in R:
    st = r['start']; pre = ''
    if '|' in st: pre, st = st.split('|', 1)
    if pre: assert norm.count(pre + st) == 1, ('context start not unique', r['id']); s = norm.index(pre + st) + len(pre)
    elif norm.count(st) == 1: s = norm.index(st)
    else:
        assert norm.count('\n' + st + '\n') >= 1, ('start not unique and not a whole line', r['id'], norm.count(st))
        key = r['id'].rsplit('.', 1)[0]
        s = norm.index('\n' + st + '\n', cur[key]) + 1
    if st.startswith('• '): s += 2
    if r['end']: e = norm.index(r['end'], s) + len(r['end'])
    else: e = norm.index('\n', s) if '\n' in norm[s:] else len(norm)
    r['span'] = (s, e); cur[r['id'].rsplit('.', 1)[0]] = e
    for v in r['verbs']:
        assert re.search(r'\b' + re.escape(v) + r'\b', norm[s:e], re.I), (r['id'], v)
ID = lambda i: f"{cfg['PREFIX']}/{i}"
o = []; w = o.append
w(cfg['FRONT'].format(raw=hashlib.sha256(raw).hexdigest(), norm=hashlib.sha256(normb).hexdigest()))
w(cfg['HEAD'])
# S4
w('''### S4 Statements
<!-- label: both; status: drafted; basis: primary. One record per statement, cut at the issuer's own list items and sentences. Extra fields (guidance variant, proposed): `family` (GU1), `employability` (direct: names work, careers or ventures; bridge: a transferable capability employers value; academic: within study), `category` (behaviour, attribute, competency, literacy, awareness, mindset, capability, effectiveness, opportunity, assessment, educator, institution, aim, principle), `maps` (our reading: related framework statements, assessment criteria and academic practice pathways; all `inferred`). -->
```yaml''')
for r in R:
    s, e = r['span']
    maps = []
    if r['fheq']: maps.append('framework: [' + ', '.join(r['fheq']) + ']')
    if r['crit']: maps.append('criteria: [' + ', '.join(('bristol/generic-2024: ' if c.startswith('b:') else 'cardiffmet/generic-2020: ') + c[2:] for c in r['crit']) + ']')
    if r['path']: maps.append('pathways: [' + ', '.join(r['path']) + ']')
    w(f'''- id: {ID(r['id'])}
  family: {r['fam']}
  locator: {{ heading: {q(r['head'] if r.get('head') else FAM[r['fam']] if r['fam'] != 'outcome' and r['fam'] != 'delivery' else FAM[r['fam']] + ': ' + cfg.get('OUTTHEME', {}).get(r['id'].split('.')[1], ''))} }}
  span: {{ start: {s}, end: {e} }}
  statementType: {r['cat']}
  force: {r['force']}
  addressee: {r['addr']}
  employability: {r['emp']}
  verbs: [{', '.join(r['verbs'])}]
  maps: {{ {', '.join(maps + ['basis: inferred'])} }}
  audience: {'both' if r['ben'] else 'practitioner'}''' + (f"\n  basis: {q(r['basis'])}" if r.get('basis') else ''))
w('```\n\n### S4a Audience versions\n<!-- label: both; status: drafted; basis: primary. Student versions in the second person, naming no issuer; force kept. -->\n```yaml')
for r in R:
    ben = f"{{ text: {q(r['ben'])}, rewrite: full, force: {r['force']}, status: drafted }}" if r['ben'] else q('not-applicable: addressed to ' + ('educators' if r['addr'] == 'educator' else 'providers') + ' alone')
    w(f'''- statement: {ID(r['id'])}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: {r['force']}, status: drafted }}
  forBeneficiary: {ben}''')
w('```')
w(cfg['MID'])
# GU1 families
w('''## Part GU Guidance analysis

### GU1 Statement families
<!-- The kinds of standards assertion the guidance makes, by family: who it addresses, its usual force, and how many records. -->

| Family | Heading | Records | Addressee | Force | Student versions |
|---|---|---|---|---|---|''')
for f, h in FAM.items():
    rs = [r for r in R if r['fam'] == f]
    if not rs: continue
    w(f"| {f} | {h} | {len(rs)} | {', '.join(sorted(set(r['addr'] for r in rs)))} | {', '.join(sorted(set(r['force'] for r in rs)))} | {sum(1 for r in rs if r['ben'])} |")
w(cfg['GU2'])
# GU3 employability
E = collections.Counter(r['emp'] for r in R); EC = collections.Counter((r['emp'], r['cat']) for r in R)
w(f'''
### GU3 Employability
<!-- Each record tagged: `direct` names work, careers, employers or ventures; `bridge` is a capability that study and work share; `academic` stays within study. Our reading. -->

| Tag | Records | Categories |
|---|---|---|''')
for t in ('direct', 'bridge', 'academic'):
    w(f"| {t} | {E.get(t, 0)} | {', '.join(f'{c} {n}' for (e, c), n in EC.most_common() if e == t)} |")
w('\n**Direct statements:** ' + '; '.join(f"`{r['id']}`" for r in R if r['emp'] == 'direct') + '.')
w(cfg['GU3'])
# GU4 frameworks and criteria
FC = collections.Counter(x for r in R for x in r['fheq']); CC = collections.Counter(x for r in R for x in r['crit'])
w('''
### GU4 Links to framework levels and assessment criteria
<!-- Counts of records linked, our reading (`inferred`). Framework statements are std:doc:qaa-fheq-2024-framework's; criteria are Bristol's (b:) and Cardiff Met's (c:) generic marking criteria. -->

| Framework statement | Records |
|---|---|''')
for k, n in FC.most_common(): w(f'| {k} | {n} |')
w('\n| Assessment criterion | Records |\n|---|---|')
for k, n in CC.most_common(): w(f"| {('Bristol: ' if k.startswith('b:') else 'Cardiff Met: ') + k[2:]} | {n} |")
w(cfg['GU4'])
# GU5 pathways
PC = collections.Counter(p for r in R for p in r['path'])
w('''
### GU5 Academic practice pathways
<!-- Records per pathway (ACPRAC-DAT's thirteen, used loosely as categories), our reading. -->

| Pathway | Records | Families |
|---|---|---|''')
for p in PW:
    rs = [r for r in R if p in r['path']]
    w(f"| {p} | {len(rs)} | {', '.join(f'{f} {n}' for f, n in collections.Counter(r['fam'] for r in rs).most_common()) or '(none)'} |")
w(cfg['GU5'])
w(cfg['TAIL'])
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
json.dump([{k: r[k] for k in ('id', 'fam', 'span', 'emp', 'cat', 'path', 'fheq', 'crit')} for r in R], open(sys.argv[2].replace('.md', '.records.json'), 'w'), indent=1)
print(len(R), 'records')
