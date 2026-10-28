import re, json
H='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
norm=open(H+'/qaa-frameworks-2024.norm.txt',encoding='utf-8').read()
A=norm.index('Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS', 5000)
E=norm.index('Published – 21 February 2024',A)
# paragraphs with spans
paras=[(m.start(),m.end(),m.group(0)) for m in re.finditer(r'[^\n]+(?:\n(?!\n)[^\n]+)*',norm[A:E])]
paras=[(A+s,A+e,t) for s,e,t in paras if not re.fullmatch(r'\s*\d+\s*',t) and t.strip()!='•']
BANDS=['ns','3rd','2.2','2.1','1st']
STR=[('knowledge','Knowledge and understanding A '),('cognitive','Cognitive skills A '),('practical','Practical skills An '),('transferable','Transferable skills Personal'),('professional','Professional competences (to the extent')]
cells=[]; comps=[]
# summary table: after the five lead cells
i=[k for k,(s,e,t) in enumerate(paras) if t.startswith('Did not achieve the required course learning outcomes and:')][0]
leads=paras[i:i+5]
for b,(s,e,t) in zip(BANDS,leads): comps.append({'id':f'annex-d/summary/lead/{b}','span':[s,e],'text':t})
rows=paras[i+5:i+25]
for r in range(4):
    for c in range(5):
        s,e,t=rows[r*5+c]; cells.append({'id':f'annex-d/summary/r{r+1}/{BANDS[c]}','strand':'summary','row':r+1,'band':BANDS[c],'span':[s,e]})
for k,(name,head) in enumerate(STR):
    hi=[j for j,(s,e,t) in enumerate(paras) if t.startswith(head)][0]
    s,e,t=paras[hi]
    # definition: heading text up to ' Not successful' if glued
    dend=t.find(' Not successful'); dtext=t if dend<0 else t[:dend]
    hlen=len(head.rsplit(' ',2)[0]) if name!='professional' else t.index(')')+1
    comps.append({'id':f'annex-d/{name}','span':[s,s+len(dtext)],'text':dtext})
    # cells start after the '1st' header paragraph
    j=hi+1
    while paras[j][2].strip()!='1st': j+=1
    j+=1
    nxt=[x for x in range(j,len(paras)) if k+1<len(STR) and paras[x][2].startswith(STR[k+1][1])]
    stop=nxt[0] if nxt else len(paras)
    body=[p for p in paras[j:stop] if not p[2].startswith('More detailed')]
    width=2 if name=='professional' else 5
    for r in range(len(body)//width):
        for c in range(width):
            s,e,t=body[r*width+c]
            band=BANDS[c] if width==5 else ['ns','3rd-1st'][c]
            cells.append({'id':f'annex-d/{name}/r{r+1}/{band}','strand':name,'row':r+1,'band':band,'span':[s,e]})
    assert len(body)%width==0,(name,len(body))
json.dump({'components':comps,'cells':cells},open('fheq2-annexd.json','w'),indent=1)
print(len(cells),'cells')
for c in comps: print(c['id'],'|',' '.join(c['text'].split())[:150])
for c in cells: print(c['id'],'|',' '.join(norm[c['span'][0]:c['span'][1]].split())[:110])
