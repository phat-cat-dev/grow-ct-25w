#!/usr/bin/env python3
"""Build the wide table of correspondences across the pathways (D-ing-0062).

Rows by card position: a foundation row (level 3 study before entry), i1 to e3, and a level 8 row.
Row-level columns are ing's readings: tier, indicative level, (until N-0161) dominant kind of knowledge (Anderson and
Krathwohl), metacognitive stance (the cores' A11 ladder), stage of participation (Lave and Wenger) and the
student life cycle stage, loosely. For each pathway, in the pathway model's order, three columns: the card
(or, for the foundation and level 8 rows, the core's A11 entry at level 3 or 8), its kind of knowledge, and
the qualification-framework statements by id.
Row readings also include practice, knowledge and practitioner self-identity (N-0149), and after the
pathways come the cross-cutting themes (N-0148): enterprise, employability and the Ofqual occupational
competence levels, both from `wide/cross-cutting-themes.yaml`.

Reads `plans/<pathway-id>.yaml` and the cores' A11. Writes, in `wide/`:
  ing-correspondence-wide.csv   one row per position, column groups per pathway
  ing-correspondence-long.csv   one row per position and pathway (for the database)
A working compilation for ing, never a record.

Usage: python3 build-wide-table.py
"""
import csv, os, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ING = os.path.dirname(os.path.dirname(HERE))
CORES = os.path.join(ING, 'pathways')
PLANS = os.path.join(HERE, 'plans')
OUT = os.path.join(HERE, 'wide')

ROWS = ['F', 'i1', 'i2', 'i3', 'd1', 'd2', 'd3', 'e1', 'e2', 'e3', 'L8']
ROWINFO = {
    # row: (tier, indicative level, dominant kind of knowledge, stance level, participation, life cycle)
    'F':  ('Foundation (before entry)', 'L3, with L2 beneath', 'factual and conceptual, with guided procedure', 3,
           'outside the community, preparing to join', 'pre-entry: A level, access, foundation year'),
    'i1': ('Introductory', 'L3', 'factual or conceptual', 3, 'legitimate peripheral participation: a newcomer at the edge', 'transition in: first year'),
    'i2': ('Introductory', 'L4', 'procedural, one set method', 4, 'legitimate peripheral participation: a newcomer at the edge', 'transition in: first year'),
    'i3': ('Introductory', 'L5', 'metacognitive, beginning', 5, 'legitimate peripheral participation: a newcomer at the edge', 'transition in: first year'),
    'd1': ('Intermediate', 'L4', 'conceptual', 4, 'increasing participation', 'progression: second year'),
    'd2': ('Intermediate', 'L5', 'procedural', 5, 'increasing participation', 'progression: second year'),
    'd3': ('Intermediate', 'L6', 'metacognitive, strategic', 6, 'increasing participation', 'progression: second year'),
    'e1': ('Advanced', 'L5', 'conceptual or procedural, criteria for choosing', 5, 'towards full participation', 'transition out: final year, graduate'),
    'e2': ('Advanced', 'L6', 'procedural with metacognitive', 6, 'towards full participation', 'transition out: final year, graduate'),
    'e3': ('Advanced', 'L7', 'metacognitive, self-knowledge', 7, 'towards full participation', 'transition out: final year, graduate'),
    'L8': ('Beyond (level 8)', 'L8', 'metacognitive and self-system: the knower examined', 8,
           'full participation that changes the community', 'postgraduate and professional practice'),
}
THEMES = yaml.safe_load(open(os.path.join(OUT, 'cross-cutting-themes.yaml'), encoding='utf-8'))
PRAC = THEMES['practitioner']
MODELS = yaml.safe_load(open(os.path.join(OUT, 'models-of-development.yaml'), encoding='utf-8'))['models']
EQUIV = yaml.safe_load(open(os.path.join(OUT, 'fheq-equivalences.yaml'), encoding='utf-8')) or {}


# no longer shown on the page since N-0176 (the FHEQ entries now sit under each reading); kept for the data
def equiv_cell(pid, r, cited=()):
    """The FHEQ equivalence for a practice's row: ids per reading, then the relation (N-0174)."""
    e = EQUIV.get(pid, {}).get(r)
    if not e:
        return 'the FHEQ starts at level 4' if r in ('F', 'i1') else ''
    short = lambda ids: ', '.join(i.split('/', 1)[1] for i in ids) or 'none at this level'
    # new: statements the card does not yet cite, worked out from the plan at each build (N-0175)
    new = sorted({i for k in ('practice', 'knowledge', 'identity') for i in e[k]} - {'fheq-2024/' + c for c in cited})
    return (f"practice: {short(e['practice'])}\nknowledge: {short(e['knowledge'])}\nself-identity: {short(e['identity'])}"
            f"\n{e['relation']}" + (f"\nnew to the card: {short(new)}" if new else ''))


FXR = yaml.safe_load(open(os.path.join(OUT, 'fheq-readings.yaml'), encoding='utf-8')) or {}


def with_fheq(pid, r, readings):
    """Each reading followed by its FHEQ entries: what the descriptor looks like here and its evidence (N-0176)."""
    out = []
    for k, text in zip(('practice', 'knowledge', 'identity'), readings):
        ents = (FXR.get(pid, {}).get(r) or {}).get(k) or []
        out.append(text + ''.join(f"\n\nFHEQ {e['id'].split('/', 1)[1]}: {e['here']}. Evidenced as {e['evidence']}." for e in ents))
    return out


READ = yaml.safe_load(open(os.path.join(OUT, 'pathway-readings.yaml'), encoding='utf-8')) or {}
STD = os.path.normpath(os.path.join(HERE, '../../../../../../../library/ingested/standards'))


def qf_levels(q):
    """Statements of one framework by level: {level: [(short id, label, paraphrase)]}, from the runs."""
    out = {}
    dirs = q['dir'] if isinstance(q['dir'], list) else [q['dir']]
    for d in dirs:
        md = os.path.join(STD, d, d + '.md')
        text = open(md, encoding='utf-8').read()
        for rid, body in re.findall(r'\n- id: (\S+)\n(.*?)(?=\n- id: |\n```)', text, re.S):
            lv = re.search(r'\n\s+level: (.*)', body)
            dim = re.search(r'\n\s+dimension: (\S+)', body)
            par = re.search(r'\n\s+paraphrase: "(.*)"', body)
            hp = re.search(r'headingPath: \["(.*?)"', body)
            if not (lv and dim and dim.group(1) in q['dims']):
                continue
            for m in re.finditer(q['scheme'] + r':(\w+)', lv.group(1)):
                if not par:
                    sys.exit(f'FAIL: {rid} has no paraphrase')
                short = rid.split('/', 1)[1]
                key = int(m.group(1)) if m.group(1).isdigit() else m.group(1)
                out.setdefault(key, []).append((short, hp.group(1) if hp else '', par.group(1)))
    return out

# 'Dominant kind of knowledge' left the row readings at N-0161: Anderson and Krathwohl, a model of knowledge, carries it formally
# 'Participation (Lave and Wenger)' and 'Student life cycle (loosely)' moved to the models of development at N-0164
HEAD = ['Row', 'Tier', 'Indicative level'] + PRAC['heads'] + ['Metacognitive stance (A11)']


def a11(pid):
    path = os.path.join(CORES, f'ingest-path-{pid}.md')
    if not os.path.exists(path):
        return {}
    text = open(path, encoding='utf-8').read()
    m = re.search(r'### A11 Progression by level\n.*?```yaml\n(.*?)```', text, re.S)
    if not m:
        return {}
    data = yaml.safe_load(m.group(1))
    return {int(l['level']): l for l in data['progression']['levels'] if str(l.get('level')).isdigit()}


def main():
    plans = []
    for fn in os.listdir(PLANS):
        if fn.endswith('.yaml'):
            p = yaml.safe_load(open(os.path.join(PLANS, fn), encoding='utf-8'))
            p['pid'] = fn[:-5]
            plans.append(p)
    plans.sort(key=lambda p: p['pathwayNo'])
    if len(plans) < 13:
        sys.exit(f'FAIL: {len(plans)} plans, expected at least 13')
    stances = {}
    problems = []
    long_rows, wide = [], []
    head = list(HEAD)
    for p in plans:
        head += [f"{p['pathwayNo']}. {p['name']}: card", f"{p['pathwayNo']}. {p['name']}: kind of knowledge", f"{p['pathwayNo']}. {p['name']}: frameworks"]
        if p['pid'] in READ:
            head += [f"{p['pathwayNo']}. {p['name']}: {x}" for x in ('practice', 'knowledge', 'practitioner self-identity')]
    levels = {p['pid']: a11(p['pid']) for p in plans}
    NM = len(HEAD)
    pcells = {}
    for r in ROWS:
        tier, lvl, kind, stl, part, life = ROWINFO[r]
        st = set()
        for p in plans:
            lv = levels[p['pid']].get(stl)
            if lv:
                st.add(lv.get('metacognition', {}).get('stance'))
        stance = '; '.join(sorted(s for s in st if s)) or 'not stated'
        row = [r, tier, lvl] + PRAC['rows'][r] + [stance]
        for p in plans:
            if r in ('F', 'L8'):
                lv = levels[p['pid']].get(3 if r == 'F' else 8)
                fb = p.get('foundation' if r == 'F' else 'level8')
                if not lv and fb:
                    cells = [fb['cell'], '(ing\'s draft)', fb.get('sources', '')]
                elif not lv:
                    problems.append(f"{p['pid']}: no A11 level {3 if r == 'F' else 8}")
                    cells = ['', '', '']
                else:
                    comp = '; '.join(lv.get('competencies', []) or [])
                    meta = lv.get('metacognition', {}).get('statement', '')
                    cells = [f"{comp} ({meta})" if meta else comp, '(A11 level %d)' % (3 if r == 'F' else 8), ', '.join(lv.get('sources', []) or [])]
            else:
                c = next((c for c in p['cards'] if c['new'] == r), None)
                if not c:
                    problems.append(f"{p['pid']}: no card {r}")
                    cells = ['', '', '']
                else:
                    qf = ', '.join(('beyond: ' if q.get('beyond') else '') + q['id'] for q in c.get('qf', []))
                    cells = [c['short'], c['knowledge'], qf]
            ext = READ.get(p['pid'], {}).get(r)
            if p['pid'] in READ and not ext:
                problems.append(f"{p['pid']}: no readings for {r}")
            if p['pid'] in READ:
                card = next((c for c in p.get('cards', []) if c['new'] == r), {})
                cells = cells + with_fheq(p['pid'], r, ext or ['', '', ''])
            row += cells
            pcells.setdefault(r, {})[p['pathwayNo']] = cells
            long_rows.append([r, tier, lvl, p['pathwayNo'], p['pid'], p['name']] + cells[:3] + (cells[3:6] or ['', '', '']))
        wide.append(row)
    # the cross-cutting themes (N-0148), after the pathways
    tcells = {}
    for th in THEMES['themes']:
        head += [f"{th['name']}: id", f"{th['name']}: reading"]
    for i, r in enumerate(ROWS):
        tcells[r] = {}
        for th in THEMES['themes']:
            if th.get('byLevel'):
                lv = th['rowLevel'][r]
                lv = lv if isinstance(lv, list) else [lv]
                c = ['; '.join(th['levels'][x][0] for x in lv), ' / '.join(th['levels'][x][1] for x in lv)]
            else:
                c = th['rows'][r]
            assert len(c) == 2, (th['key'], r)
            tcells[r][th['key']] = c
            wide[i] += c
    # the models of development (N-0159)
    mcells = {r: {} for r in ROWS}
    for m in MODELS:
        head += [f"{m['name']}: {s}" for s in m['subs']]
        for i, r in enumerate(ROWS):
            c = m['rows'][r]
            if len(c) != len(m['subs']):
                problems.append(f"{m['key']} {r}: {len(c)} cells for {len(m['subs'])} columns")
            mcells[r][m['key']] = c
            wide[i] += c
    # the qualification frameworks (N-0151), placed before the themes
    qcells = {r: {} for r in ROWS}
    for q in THEMES['qualifications']:
        lv = qf_levels(q)
        head += [f"{q['name']}: id", f"{q['name']}: reading"]
        for i, r in enumerate(ROWS):
            ids, reads = [], []
            for n in q['rowLevel'][r]:
                st = lv.get(n)
                if not st:
                    problems.append(f"{q['key']}: no statements at level {n}")
                    continue
                labels = []
                for s in st:
                    if s[1] not in labels:
                        labels.append(s[1])
                ids.append(q['labels'][n] if q.get('labels') else ' / '.join(labels))
                for s in st:
                    reads.append(s[0].split('/', 1)[1] + ': ' + s[2])
            # the level in the first column; each statement keeps its id beside its paraphrase
            c = ['\n'.join(ids), '\n\n'.join(reads) or 'no level here']
            qcells[r][q['key']] = c
            wide[i] += c
    # the subject benchmarks (N-0154): practice, knowledge and practitioner self-identity where each speaks
    bms = []
    for fn in sorted(os.listdir(os.path.join(OUT, 'benchmarks'))):
        if fn.endswith('.yaml'):
            bms.append(yaml.safe_load(open(os.path.join(OUT, 'benchmarks', fn), encoding='utf-8')))
    if len(bms) < 54:
        problems.append(f'{len(bms)} benchmark files, expected 54')
    bcells = {r: {} for r in ROWS}
    for b in bms:
        head += [f"{b['name']}: practice", f"{b['name']}: knowledge", f"{b['name']}: practitioner self-identity", f"{b['name']}: ids"]
        for i, r in enumerate(ROWS):
            c = (b.get('rows') or {}).get(r)
            cells = [c['practice'], c['knowledge'], c['identity'], ', '.join(c['ids'])] if c else ['', '', '', '']
            bcells[r][b['slug']] = cells
            wide[i] += cells
    for x in problems:
        print('PROBLEM:', x)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'ing-correspondence-wide.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(head)
        w.writerows(wide)
    with open(os.path.join(OUT, 'ing-correspondence-long.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['row', 'tier', 'indicative_level', 'pathway_no', 'pathway', 'pathway_name', 'cell', 'knowledge', 'frameworks', 'practice', 'knows', 'self_identity'])
        w.writerows(long_rows)
    print(f'{len(wide)} rows, {len(head)} columns; {len(long_rows)} long rows; {len(problems)} problems')
    # the page: the template with the data injected
    import json, datetime
    data = {'pathways': [{'no': p['pathwayNo'], 'name': p['name'], 'readings': p['pid'] in READ} for p in plans],
            'meta': HEAD[1:],
            'benchmarks': [{'slug': b['slug'], 'name': b['name'], 'run': b['run'], 'subject': b['subject'],
                            'subjectIds': b.get('subjectIds') or [], 'note': b.get('note', '')} for b in bms],
            'themes': [{'key': m['key'], 'name': m['name'], 'run': m['ref'], 'note': m['note'], 'group': {'metacognition': 'metacog', 'professional': 'prof'}.get(m.get('group'), 'model'), 'subs': m['subs']} for m in MODELS]
                      + [{'key': q['key'], 'name': q['name'], 'run': q['run'], 'note': q['note'], 'group': 'qf'} for q in THEMES['qualifications']]
                      + [{'key': th['key'], 'name': th['name'], 'run': th['run'], 'note': th['note'], 'group': 'theme'} for th in THEMES['themes']],
            'rows': [], 'built': datetime.date.today().strftime('%d %B %Y')}
    for row in wide:
        cells = {}
        for k, p in enumerate(plans):
            cells[p['pathwayNo']] = pcells[row[0]][p['pathwayNo']]
        data['rows'].append({'row': row[0], 'meta': row[1:NM], 'cells': cells, 'themes': {**mcells[row[0]], **qcells[row[0]], **tcells[row[0]]}, 'bm': bcells[row[0]]})
    tpl = open(os.path.join(OUT, 'table-template.html'), encoding='utf-8').read()
    assert tpl.count('__DATA__') == 1
    open(os.path.join(OUT, 'pathway-table-of-correspondences.html'), 'w', encoding='utf-8').write(
        tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False)))
    if problems:
        sys.exit(1)


if __name__ == '__main__':
    main()
