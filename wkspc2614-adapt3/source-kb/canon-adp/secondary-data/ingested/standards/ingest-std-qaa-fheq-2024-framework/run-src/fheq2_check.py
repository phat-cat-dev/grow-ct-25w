import json, re
S='/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
H='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
norm=open(H+'/qaa-frameworks-2024.norm.txt',encoding='utf-8').read()
W=lambda s: re.findall(r"[a-z0-9']+", s.lower()); nw=W(norm); G={tuple(nw[i:i+9]) for i in range(len(nw)-8)}
cp=lambda t:[' '.join(W(t)[i:i+9]) for i in range(len(W(t))-8) if tuple(W(t)[i:i+9]) in G]
ad={};exec(open(S+'/fheq2_annexd.py').read(),ad); db={};exec(open(S+'/fheq2_dublin.py').read(),db); pv={};exec(open(S+'/fheq2_provider.py').read(),pv)
AD=json.load(open(S+'/fheq2-annexd.json')); DB=json.load(open(S+'/fheq2-dublin.json'))
recs=[]
for c in AD['cells']: r=ad['D'][c['id']]; recs.append((c['id'],c['span'],r['verbs'],{'prac':r['prac'],'ben':r['ben']}))
for c in DB: r=db['B'][c['id']]; recs.append((c['id'],c['span'],r['verbs'],{'para':r['para'],'prac':r['prac'],'ben':r['ben']}))
for i,r in pv['R'].items():
    a,b=r['se']; s=norm.index(a); e=norm.index(b,s)+len(b)
    if norm.count(a)!=1: print('WARN start not unique',i)
    recs.append((i,[s,e],r['verbs'],{} if r['para']=='stem' else {'para':r['para'],'prac':r['prac'],'ben':r['ben']}))
F=[]
BAN=('fheq','fqheis','scqf','qaa','qualification descriptor','degree-awarding bod','the student has','students who','dublin','qf-ehea','bologna','annex')
for i,sp,verbs,txt in recs:
    seg=' '.join(norm[sp[0]:sp[1]].lower().replace('degreeawarding','degree-awarding').split())
    for v in verbs:
        if not re.search(r'\b'+re.escape(v.lower())+r'\b',seg): F.append(f'{i}: verb not in span: {v}')
    for k,t in txt.items():
        if t is None: continue
        c=cp(t); c and F.append(f'{i}: {k} copies: {c[0]}')
    b=txt.get('ben')
    if b:
        if not re.search(r'\byou(r)?\b',b,re.I): F.append(f'{i}: ben not second person')
        for x in BAN:
            if x in b.lower(): F.append(f'{i}: ben banned: {x}')
for k,t in ad['DEFS'].items():
    c=cp(t); c and F.append(f'DEF {k} copies {c[0]}')
for k,t in pv['TERMS']:
    c=cp(t); c and F.append(f'TERM {k} copies {c[0]}')
print(len(recs),'records;',len(F),'failures'); [print(' ',f) for f in F]
