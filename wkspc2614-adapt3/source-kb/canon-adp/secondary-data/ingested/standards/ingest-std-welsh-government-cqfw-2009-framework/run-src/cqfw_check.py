import json, re, sys
S='/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
H='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
norm=open(H+'/welsh-government-cqfw-level-descriptors-2009.norm.txt',encoding='utf-8').read()
sk=json.load(open(S+'/cqfw-skel.json')); ns={}; exec(open(sys.argv[1] if len(sys.argv)>1 else S+'/cqfw_judgement.py',encoding='utf-8').read(),ns); P=ns['P']
W=lambda s: re.findall(r"[a-z0-9']+", s.lower()); nw=W(norm); G={tuple(nw[i:i+9]) for i in range(len(nw)-8)}
cp=lambda t:[' '.join(W(t)[i:i+9]) for i in range(len(W(t))-8) if tuple(W(t)[i:i+9]) in G]
sp={x['id']:x['span'] for x in sk['statements']}
F=[]
want={x['id'] for x in sk['statements'] if x['column']!='summary'}
if set(P)!=want: F.append(f'coverage: missing {sorted(want-set(P))[:5]} extra {sorted(set(P)-want)[:5]}')
for i,r in P.items():
    seg=norm[sp[i]['start']:sp[i]['end']].lower()
    for v in r['verbs']:
        if not re.search(r'\b'+re.escape(v.lower())+r'\b',seg): F.append(f'{i}: ST-5 verb not in span: {v}')
    for k in ('para','prac','ben'):
        c=cp(r[k]); c and F.append(f'{i}: ST-12 {k} copies: {c[0]}')
    if not re.search(r'\byou(r)?\b',r['ben'],re.I): F.append(f'{i}: ST-13 not second person')
    for b in ('cqfw','credit and qualifications framework','level descriptor','welsh government','learners will'):
        if b in r['ben'].lower(): F.append(f'{i}: ST-13 banned: {b}')
for k,(p,b) in ns['DEFINING'].items():
    for x in (p,b):
        c=cp(x); c and F.append(f'DEFINING {k}: copies {c[0]}')
q=0
for name,steps in ns['THREADS']:
    for lv,txt in steps:
        for m in re.findall(r'"([^"]+)"',txt):
            q+=1
            if m.lower() not in norm.lower(): F.append(f'THREAD {name}/{lv}: not verbatim: {m}')
print(len(P),'statements;',q,'quoted thread phrases;',len(F),'failures'); [print(' ',f) for f in F]
