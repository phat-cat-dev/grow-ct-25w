import re, json
H='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
norm=open(H+'/qaa-frameworks-2024.norm.txt',encoding='utf-8').read()
L=[m for m in re.finditer(r'Qualifications that signify completion of the [^:]*:',norm)]
end=norm.index('From first cycle (bachelor)')
C=['short','1','2','3']; out=[]
for k,m in enumerate(L):
    s=m.end(); e=L[k+1].start() if k+1<len(L) else end
    seg=norm[s:e]
    for n,b in enumerate(re.finditer(r'•\n+(.+?)(?=\n+•\n|\n\n\d+\n|\n\d+ [A-Z]|\Z)',seg,re.S),1):
        t=b.group(1); t=re.split(r'\n\n\d+\n',t)[0].rstrip()
        out.append({'id':f'annex-b/{C[k]}/b{n}','cycle':C[k],'lead':[m.start(),m.end()],'span':[s+b.start(1),s+b.start(1)+len(t)]})
json.dump(out,open('fheq2-dublin.json','w'),indent=1)
for o in out: print(o['id'],'|',' '.join(norm[o['span'][0]:o['span'][1]].split()))
