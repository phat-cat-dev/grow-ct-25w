import sys, json, re, subprocess, hashlib, os
sys.path.insert(0, '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad')
from bris_common import *
HA = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/assessment-criteria'
MARKS = {'0-19': '0, 7, 15', '20-39': '22, 29, 35', '40-49': '42, 45, 48', '50-59': '52, 55, 58', '60-69': '62, 65, 68', '70-79': '72, 75, 78', '80-100': '83, 94, 100', '0-39': '0, 7, 15, 22, 29, 35'}
LH = {4: 'Level 4 (First-year undergraduate level)', 5: 'Level 5 (Second-year undergraduate level)', 6: 'Level 6 (Third-year undergraduate level)', 7: 'Level 7 (Masters level)'}
lay = open(HA + '/bristol-marking-criteria-level4.txt', encoding='utf-8').read().split('\n')
pre = '\n'.join(lay[1:47]).split('See section 15')[0].rstrip()
o = ['University of Bristol: University marking criteria, levels 4 to 7 (held text by std: the shared opening once, from the level 4 layout extract; then each level\'s grid cell by cell, from pdfplumber table extraction)', '', 'SHARED OPENING', pre, '', 'See section 15 in the Regulations and Code of Practice for Taught Programmes on the use of marking criteria.', '']
cur = None
for c in cells():
    if c['level'] != cur:
        cur = c['level']; o += [LH[cur], '']
    o += [f"L{c['level']} | {c['category']} | {c['criterion']} | {c['bsp']} | {c['band']} ({MARKS[c['band']]})", c['text'], '']
os.makedirs(S + '/bris_hold', exist_ok=True)
open(S + '/bris_hold/bristol-marking-criteria-2024.txt', 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print(subprocess.run(['node', '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/stan/core/tools/normalise.js', S + '/bris_hold'], capture_output=True, text=True))
