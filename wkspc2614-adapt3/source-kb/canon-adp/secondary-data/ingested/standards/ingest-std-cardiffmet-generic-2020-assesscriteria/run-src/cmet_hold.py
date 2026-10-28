import sys, json, re, subprocess, hashlib, os
sys.path.insert(0, '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad')
from cmet_common import *
import docx
from docx.oxml.ns import qn
DX = '/root/.claude/uploads/378bff94-17ab-5a5d-8465-bd8449aca2a6/a5baa12d-AH1_04_03.docx'
d = docx.Document(DX)
o = ['Cardiff Metropolitan University: Academic Handbook AH1 4.3, Guidance on Assessment Marking, with the Generic Band Descriptors, levels 3 to 7 (held text by std: key details, the guidance paragraphs in order, then each level grid cell by cell, from the .docx with python-docx)', '']
o.append('KEY DETAILS')
for r in d.tables[0].rows: o.append(' | '.join(' '.join(c.text.split()) for c in r.cells))
o += ['', 'GUIDANCE']
on = False
for el in d.element.body.iterchildren():
    if el.tag == qn('w:p'):
        t = ' '.join(''.join(x.text or '' for x in el.iter(qn('w:t'))).split())
        if t == 'Guidance on Assessment Marking': on = True
        if t.startswith('TABLE A'): break
        if on and t: o += [t, '']
LH = {L: f'GENERIC LEVEL {L} BAND DESCRIPTORS' for L in '34567'}
cur = None
for c in cells():
    if c['level'] != cur:
        cur = c['level']; o += [LH[str(cur)], '']
    o += [f"L{c['level']} | {c['criterion']} | {c['label']}", c['text'] or '(empty cell: the band-wide descriptor is in the Knowledge & Understanding row)', '']
H = S + '/cmet_hold'; os.makedirs(H, exist_ok=True)
slug = 'cardiffmet-generic-band-descriptors-2020'
open(f'{H}/{slug}.txt', 'w', encoding='utf-8').write('\n'.join(o) + '\n')
b = open(f'{H}/{slug}.txt', 'rb').read().rstrip(b'\n')
json.dump([{'slug': slug, 'sha256': hashlib.sha256(b).hexdigest()}], open(f'{H}/index.json', 'w'))
print(subprocess.run(['node', '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/stan/core/tools/normalise.js', H], capture_output=True, text=True).stdout[-200:])
