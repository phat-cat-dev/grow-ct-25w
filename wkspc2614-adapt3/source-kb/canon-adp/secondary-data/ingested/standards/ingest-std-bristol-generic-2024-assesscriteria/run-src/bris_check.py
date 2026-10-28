import sys, re, json
sys.path.insert(0,'.')
from bris_common import *
norm=open('bris_hold/bristol-marking-criteria-2024.norm.txt').read()
W=lambda s: re.findall(r"[a-z0-9']+", s.lower().replace('’',"'")); nw=W(norm); G={tuple(nw[i:i+9]) for i in range(len(nw)-8)}
cp=lambda t:[' '.join(W(t)[i:i+9]) for i in range(len(W(t))-8) if tuple(W(t)[i:i+9]) in G]
ns={}
for f in ['bris_v4.py','bris_v5.py','bris_v67.py']: exec(open(f).read(),ns)
V={**ns['V'],**ns['V5'],**ns['V67']}
F=[]
for i,(p,b) in V.items():
    for k,t in (('prac',p),('ben',b)):
        c=cp(t); c and F.append(f'{i} {k} copies: {c[0]}')
    if not re.search(r'\byou(r)?\b',b,re.I): F.append(f'{i} ben not second person')
    for x in ('bristol','university','bsp','the student','marker'):
        if x in b.lower(): F.append(f'{i} ben banned {x}')
print(len(V),'versions;',len(F),'failures'); [print(' ',f) for f in F]
