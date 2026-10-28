import sys, re
sys.path.insert(0,'.')
norm=open('cmet_hold/cardiffmet-generic-band-descriptors-2020.norm.txt').read()
W=lambda s: re.findall(r"[a-z0-9']+", s.lower().replace('’',"'")); nw=W(norm); G={tuple(nw[i:i+9]) for i in range(len(nw)-8)}
cp=lambda t:[' '.join(W(t)[i:i+9]) for i in range(len(W(t))-8) if tuple(W(t)[i:i+9]) in G]
ns={}
for f in ['cmet_v3.py','cmet_v45.py','cmet_v67.py']: exec(open(f).read(),ns)
V={**ns['V3'],**ns['V45'],**ns['V67']}
F=[]
for i,(p,b) in V.items():
    for k,t in (('prac',p),('ben',b)):
        c=cp(t); c and F.append(f'{i} {k} copies: {c[0]}')
    if not re.search(r'\byou(r)?\b',b,re.I): F.append(f'{i} ben not second person')
    for x in ('cardiff','university','the student','marker','gbd'):
        if x in b.lower(): F.append(f'{i} ben banned {x}')
print(len(V),'versions;',len(F),'failures'); [print(' ',f) for f in F]
