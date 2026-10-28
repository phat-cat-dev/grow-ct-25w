#!/usr/bin/env python3
"""Checks for a standards/guidance document: usage gu_check.py <judge.py> <slug> [<built.md>]"""
import re, sys, yaml
G = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/guidance'
ns = {}; exec(open(sys.argv[1]).read(), ns); R = ns['R']
norm = open(f'{G}/{sys.argv[2]}.norm.txt', encoding='utf-8').read()
W = lambda s: re.findall(r"[a-z0-9']+", s.lower()); nw = W(norm); GR = {tuple(nw[i:i+9]) for i in range(len(nw)-8)}
cp = lambda t: [' '.join(W(t)[i:i+9]) for i in range(len(W(t))-8) if tuple(W(t)[i:i+9]) in GR]
BAN = ('qaa', 'advance he', 'unesco', 'guidance', 'graduates will', 'students should', 'educators', 'providers', 'benchmark')
F = []
for r in R:
    for k in ('prac', 'ben'):
        t = r.get(k)
        if t: c = cp(t); c and F.append(f"{r['id']}: {k} copies: {c[0]}")
    b = r.get('ben')
    if b:
        if not re.search(r'\byou(r)?\b', b, re.I): F.append(f"{r['id']}: ben not second person")
        for x in BAN:
            if re.search(r'\b' + re.escape(x) + r'\b', b.lower()): F.append(f"{r['id']}: ben banned: {x}")
if len(sys.argv) > 3:
    md = open(sys.argv[3], encoding='utf-8').read()
    for n, line in enumerate(md.split('\n'), 1):
        if 'heading: ' in line or line.startswith(('supersedes:', 'issuer:')) or line.startswith(('title:', '# ', 'title: ')) or 'title: "' in line: continue  # labels: titles and issuer headings
        c = cp(line); c and F.append(f'line {n}: copies: {c[0]}')
    fm = md.split('---\n')[1]; yaml.safe_load(fm)
    for i, blk in enumerate(re.findall(r'```yaml\n(.*?)```', md, re.S)):
        try: yaml.safe_load(blk)
        except Exception as e: F.append(f'yaml block {i}: {str(e)[:120]}')
print(len(R), 'records;', len(F), 'failures'); [print(' ', f) for f in F]
