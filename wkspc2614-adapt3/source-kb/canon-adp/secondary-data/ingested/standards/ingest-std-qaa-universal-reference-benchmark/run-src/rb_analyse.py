import json,glob,collections,re,os
B='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/stan/core/qaa/benchmarks/'
exec(open('rf_bloom.py').read().split("R=json.load")[0])  # T, look, BR, SR
def sec4(f):
    c=json.load(open(f)); t=open(f.replace('.chunks.json','.norm.txt')).read()
    xs=[x for x in c if not x['excluded'] and (x.get('heading') or '').lower().startswith('benchmark standards')]
    return t[min(x['start'] for x in xs):max(x['end'] for x in xs)] if xs else ''
RUNG=re.compile(r'\b(threshold|typical|very good|excellent)( level| standards?| achievement)?\b',re.I)
docs={}
agg=collections.Counter(); verbs_by_rung=collections.defaultdict(collections.Counter); bloom_by_rung=collections.defaultdict(collections.Counter)
subheads=collections.Counter(); leadins=collections.Counter(); modal=collections.Counter()
for f in sorted(glob.glob(B+'*.chunks.json')):
    slug=os.path.basename(f).replace('.chunks.json',''); s=sec4(f); low=s.lower()
    d={'len':len(s),'rungs':[r for r in ('threshold','typical','very good','excellent') if re.search(r'\b'+r+r'\b',low)],
       'masters':bool(re.search(r"master'?s",low)),'annexD':'annex d' in low,
       'fourCategories':all(k in low for k in ('knowledge and understanding','cognitive skills','practical skills','transferable skills'))}
    cur='threshold'; items=collections.Counter()
    for line in s.split('\n'):
        m=None
        for m in RUNG.finditer(line):
            pass
        if not line.startswith('•') and m and len(line)<400 or (not line.startswith('•') and re.search(r'(Threshold|Typical|Excellent|Very good)\s*(level|standard)',line)):
            # last rung mention in a non-bullet line sets the current rung when it reads like a heading or a lead-in
            mm=list(re.finditer(r'(Threshold|Typical|Excellent|Very good)',line))
            if mm: cur=mm[-1].group(1).lower()
        if line.startswith('•'):
            items[cur]+=1
            w=re.findall(r"[A-Za-z\-']+",line[1:])
            if w:
                v=w[0].lower(); verbs_by_rung[cur][v]+=1
                k,dd=look(v)
                if dd.get('bloom'): bloom_by_rung[cur][max(BR.index(c) for c in dd['bloom'] if c in BR)]+=1
        lm=re.search(r'(graduates?|students?)\s+(will|should|are expected to|must)\s+(be able to|have)',line,re.I)
        if lm: modal[lm.group(2).lower()+' '+lm.group(3).lower()]+=1
        hm=re.search(r'(Subject[- ]specific [a-z ,]+|Generic skills|Transferable skills|Subject knowledge(, understanding)?( and skills)?|Generic( and transferable)? skills|Practical skills|Cognitive skills|Knowledge and understanding)',line)
        if hm and not line.startswith('•'): subheads[hm.group(1).strip().lower()]+=1
    d['items']=dict(items); docs[slug]=d
    agg['n']+=1
    for r in d['rungs']: agg['rung:'+r]+=1
    agg['masters']+=d['masters']; agg['annexD']+=d['annexD']; agg['fourCategories']+=d['fourCategories']
    agg['rungset:'+'+'.join(d['rungs'])]+=1
print(agg)
print('modal',modal.most_common(8))
print('subheads',subheads.most_common(15))
for r in ('threshold','typical','very good','excellent'):
    n=sum(verbs_by_rung[r].values()); bb=bloom_by_rung[r]; tot=sum(bb.values())
    mean=sum((k+1)*v for k,v in bb.items())/tot if tot else 0
    print(r,'items',n,'bloomplaced',tot,'mean',round(mean,2),{BR[k]:v for k,v in sorted(bb.items())},'top',verbs_by_rung[r].most_common(12))
json.dump({'docs':docs,'agg':agg,'modal':modal,'subheads':subheads,'verbs':{r:verbs_by_rung[r].most_common(40) for r in verbs_by_rung},'bloom':{r:{BR[k]:v for k,v in bloom_by_rung[r].items()} for r in bloom_by_rung}},open('rb_data.json','w'),indent=0)
