#!/usr/bin/env python3
"""Check the subject benchmark readings (ing N-0154): every file present and parsing, ids in the run at the row's level,
10 to 35 words (8 to 40 tolerated), no dashes, semicolons or second person, no nine words of issuer text, no seven words of a paraphrase."""
import re,glob,yaml,os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); STD=os.path.normpath(os.path.join(HERE,'../../../../../../../library/ingested/standards')); BM=os.path.join(HERE,'wide','benchmarks')
ROWLV={'d2':'5','d3':'6','e2':'6','e3':'7'}
def words(s): return re.findall(r"[a-z0-9']+",s.lower())
def grams(s,n): w=words(s); return {' '.join(w[i:i+n]) for i in range(len(w)-n+1)}
probs=[]; nfiles=0; ncells=0
for d in sorted(glob.glob(f'{STD}/ingest-std-qaa-*-benchmarks')):
    slug=os.path.basename(d)[len('ingest-std-qaa-'):-len('-benchmarks')]
    f=f'{BM}/{slug}.yaml'
    if not os.path.exists(f): probs.append(f'{slug}: no file'); continue
    nfiles+=1
    y=yaml.safe_load(open(f))
    t=open(f'{d}/{os.path.basename(d)}.md').read()
    recs={}; src9=set(); par7=set()
    for i,b in re.findall(r'\n- id: (\S+)\n(.*?)(?=\n- id: |\n```)',t,re.S):
        lv=re.search(r'\n\s+level: (.*)',b); recs[i]=set(re.findall(r'fheq:(\d)',lv.group(1))) if lv else set()
        s=re.search(r'\n\s+source: "(.*)"',b); p=re.search(r'\n\s+paraphrase: "(.*)"',b)
        if s: src9|=grams(s.group(1),9)
        if p: par7|=grams(p.group(1),7)
    for k in ('slug','name','run','subject','rows'):
        if not y.get(k): probs.append(f'{slug}: missing {k}')
    for i in y.get('subjectIds') or []:
        if i not in recs: probs.append(f'{slug}: subjectId {i} not in run')
    texts=[('subject',y.get('subject',''))]
    for r,c in (y.get('rows') or {}).items():
        if r not in ROWLV: probs.append(f'{slug}: unknown row {r}'); continue
        for k in ('practice','knowledge','identity'):
            v=c.get(k,''); texts.append((f'{r}.{k}',v)); ncells+=1
            n=len(v.replace(" (ing's reading)",'').split())
            if not 8<=n<=40: probs.append(f'{slug} {r}.{k}: {n} words')
        ids=c.get('ids') or []
        if not ids: probs.append(f'{slug} {r}: no ids')
        for i in ids:
            if i not in recs: probs.append(f'{slug} {r}: id {i} not in run')
            elif ROWLV[r] not in recs[i]: probs.append(f'{slug} {r}: id {i} at level {recs[i] or "none"}')
    for k,v in texts:
        if '—' in v or '–' in v: probs.append(f'{slug} {k}: dash')
        if ';' in v: probs.append(f'{slug} {k}: semicolon')
        if grams(v,9)&src9: probs.append(f'{slug} {k}: nine words of issuer text')
        if grams(v,7)&par7: probs.append(f'{slug} {k}: seven words of a paraphrase')
        if re.search(r'\b(you|your)\b',v,re.I): probs.append(f'{slug} {k}: second person')
        if re.search(r', (and|or) [\w-]+[.]?$',v) and v.count(',')>=2: probs.append(f'{slug} {k}: possible Oxford comma: ...{v[-60:]}')
print(nfiles,'files',ncells,'cells',len(probs),'problems')
for p in probs: print(p)
sys.exit(1 if probs or nfiles < 54 else 0)
