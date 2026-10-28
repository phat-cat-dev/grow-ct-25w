import re, json
H='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
norm=open(H+'/qaa-frameworks-2024.norm.txt',encoding='utf-8').read()
DS=['4.10','4.11','4.12','4.13','4.14','4.15','4.16','4.17','4.18']
starts=[norm.index(d+' Descriptor for a higher education qualification') for d in DS]
end=norm.index('Using UK qualification descriptors', starts[-1])
LEAD=[('demonstrated',re.compile(r'awarded to students who have demonstrated:')),('typical',re.compile(r'Typically, holders of the [^:]*? will be able to:')),('holders',re.compile(r'And holders will have:'))]
recs=[]; comps=[]
for k,d in enumerate(DS):
    s=starts[k]; e=starts[k+1] if k+1<len(DS) else end
    blk=norm[s:e]
    head=re.match(r'(4\.\d+) Descriptor for a higher education qualification at (.*?) on the (FHEQ and SCQF Level \d+ on the FQHEIS|FHEQ|FQHEIS) (.*?) (The |Certificates)',blk)
    notes=re.search(r'\na\)\n',blk); nend=s+(notes.start() if notes else len(blk))
    leads=[]
    for kind,rx in LEAD:
        m=rx.search(blk)
        if m: leads.append((s+m.start(),s+m.end(),kind))
    leads.sort()
    comps.append({'number':d,'start':s,'end':e,'introEnd':leads[0][0],'notesStart':nend,'title':blk[:blk.index(' The ') if ' The ' in blk[:300] else 150]})
    b=0
    for li,(ls,le,kind) in enumerate(leads):
        lend=leads[li+1][0] if li+1<len(leads) else nend
        seg=norm[le:lend]
        # items: split on bullet markers
        parts=[]; 
        for m in re.finditer(r'(?:^|\n)([•o])\n\n(.*?)(?=\n\n?[•o]\n|\n\n(?:Typically|And holders)|\Z)',seg,re.S):
            parts.append((le+m.start(2),le+m.end(2),m.group(2),m.group(1)))
        sub_parent=None
        # an "o" marker left at the end of a stem's own line (": o\n\n") opens a sub-list: split it there
        fixed=[]
        for ps,pe,txt,mark in parts:
            k2=txt.find(': o\n\n')
            if k2>=0:
                fixed.append((ps,ps+k2+1,txt[:k2+1],mark)); fixed.append((ps+k2+5,pe,txt[k2+5:],'o'))
            else: fixed.append((ps,pe,txt,mark))
        parts=fixed
        for ps,pe,txt,mark in parts:
            txt_s=re.sub(r'\n\n\d+\s*$','',txt.rstrip()).rstrip()
            if txt_s.endswith(': o'): txt_s=txt_s[:-2].rstrip()
            pe=ps+len(txt_s)
            if mark=='o' and recs and (recs[-1].get('stem') or recs[-1].get('parent')):
                par=recs[-1]['id'] if recs[-1].get('stem') else recs[-1]['parent']
                n=sum(1 for r in recs if r.get('parent')==par)+1
                recs.append({'id':f'{par}.{n}','descriptor':d,'list':kind,'parent':par,'span':{'start':ps,'end':pe}}); sub_parent=None; continue
            if txt_s.endswith(':') and mark=='•' and not sub_parent:
                b+=1; r={'id':f'{d}.b{b}','descriptor':d,'list':kind,'stem':True,'span':{'start':ps,'end':pe}}; recs.append(r)
                sub_parent={'id':r['id'],'n':0}; continue
            # inline sub-bullets " o "
            inl=re.split(r' o (?=[a-z])',txt_s)
            if len(inl)>1 and txt_s.split(' o ')[0].rstrip().endswith(':'):
                b+=1; base=f'{d}.b{b}'; off=ps
                recs.append({'id':base,'descriptor':d,'list':kind,'stem':True,'span':{'start':ps,'end':ps+len(inl[0])}})
                cur=ps+len(inl[0])+3
                for m_i,sub in enumerate(inl[1:],1):
                    recs.append({'id':f'{base}.{m_i}','descriptor':d,'list':kind,'parent':base,'span':{'start':cur,'end':cur+len(sub.rstrip())}})
                    cur+=len(sub)+3
                sub_parent=None; continue
            if sub_parent and not txt_s.endswith(':'):
                sub_parent['n']+=1
                recs.append({'id':f"{sub_parent['id']}.{sub_parent['n']}",'descriptor':d,'list':kind,'parent':sub_parent['id'],'span':{'start':ps,'end':pe}})
                continue
            b+=1
            r={'id':f'{d}.b{b}','descriptor':d,'list':kind,'span':{'start':ps,'end':pe}}
            if txt_s.endswith(':'): r['stem']=True; sub_parent={'id':r['id'],'n':0}
            else: sub_parent=None
            recs.append(r)
json.dump({'descriptors':comps,'items':recs},open('/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad/fheq-skel.json','w'),indent=1)
from collections import Counter
print(len(recs),'records', Counter(r['list'] for r in recs), sum(1 for r in recs if r.get('stem')),'stems')
for r in recs: print(r['id'], r['list'], ('STEM ' if r.get('stem') else '')+' '.join(norm[r['span']['start']:r['span']['end']].split()[:7]))
