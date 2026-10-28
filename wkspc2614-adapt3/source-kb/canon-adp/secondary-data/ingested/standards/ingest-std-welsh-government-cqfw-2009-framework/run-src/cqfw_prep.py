import json, re, hashlib
H='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
norm=open(H+'/welsh-government-cqfw-level-descriptors-2009.norm.txt',encoding='utf-8').read()
COLS=[('Summary','summary'),('Knowledge and understanding','knowledge'),('Application and action','application'),('Autonomy and accountability','autonomy')]
LV=['Entry 1','Entry 2','Entry 3']+['Level %d'%i for i in range(1,9)]
def lid(l): return ('entry-'+l[-1]) if l.startswith('Entry') else 'l'+l.split()[1]
pos={}
for l in LV:
    i=norm.index(l+' Summary '); pos[l]=i
order=sorted(LV,key=lambda l:pos[l])
blocks=[]
for k,l in enumerate(order):
    s=pos[l]; e=pos[order[k+1]] if k+1<len(order) else len(norm)
    blocks.append((l,s,e))
stm=[]; comps=[]
for l,s,e in blocks:
    seg=norm[s:e]
    # column starts
    starts=[]
    for name,key in COLS:
        j=seg.find(name+' ' ) if name!='Summary' else seg.find('Summary ')
        if j>=0: starts.append((j,name,key))
    starts.sort()
    for n,(j,name,key) in enumerate(starts):
        a=s+j+len(name)+1; b=s+(starts[n+1][0] if n+1<len(starts) else len(seg.rstrip()))
        txt=norm[a:b].rstrip()
        b=a+len(txt)
        comps.append({'level':l,'id':lid(l),'column':key,'start':a,'end':b})
        # sentences
        for m_i,m in enumerate(re.finditer(r'[^.]+\.', txt),1):
            ss=a+m.start()+ (len(m.group(0))-len(m.group(0).lstrip())); se=a+m.end()
            stm.append({'id':f"{lid(l)}/{key}.{m_i}",'level':l,'column':key,'span':{'start':ss,'end':se},'text_words':len(norm[ss:se].split()),'lead':' '.join(norm[ss:se].split()[:3])})
json.dump({'components':comps,'statements':stm},open('/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad/cqfw-skel.json','w'),indent=1)
from collections import Counter
print(len(comps),'cells;',len(stm),'sentences;',Counter(x['column'] for x in stm))
for x in stm:
    if x['column']!='summary': print(x['id'],'|',x['lead'])
