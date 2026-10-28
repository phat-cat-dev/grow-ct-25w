import json,re,collections,sys
sys.path.insert(0,'..')
RUNS='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/runs'
T=collections.defaultdict(dict)
for doc,short in (('ingest-theory-revised-bloom-taxonomy-anderson-krathwohl-2001.md','bloom'),('ingest-theory-solo-biggs-collis-1982.md','solo')):
    for line in open(f'{RUNS}/{doc}'):
        m=re.match(r'- \{ concept: ([^,]+), form: ([^,]+), frameworkBlocks: \[(.*)',line)
        if m: T[m.group(2).strip().lower()][short]=re.findall(r'component: ([a-z\-]+)',m.group(3))
BR=['remember','understand','apply','analyze','evaluate','create']
SR=['prestructural','unistructural','multistructural','relational','extended-abstract']
def look(v):
    v=v.lower()
    cands=[v,v.replace('ise','ize').replace('yse','yze'),re.sub(r's$','',v),re.sub(r'ing$','',v),re.sub(r'ing$','e',v),re.sub(r'ed$','',v),re.sub(r'ed$','e',v),re.sub(r'd$','',v)]
    out={}
    for c in cands:
        c2=c.replace('ise','ize').replace('yse','yze')
        for x in (c,c2):
            for k,val in T.get(x,{}).items(): out.setdefault(k,val)
    return v,out
R=json.load(open('rf_recs.json'))
DUB={'knowledge-and-understanding':'K','applying-knowledge':'A','making-judgements':'C','communication':'M','learning-skills':'R'}
for r in R:
    if r['src']=='dublin' and r['dim'] in DUB: r['strand']=DUB[r['dim']]
STEPS=['entry-2','entry-3','1','2','3','4','5','6','7','8']
placed=0; tot=0; unplaced=collections.Counter()
rows=collections.defaultdict(list); solo=collections.defaultdict(list)
for r in R:
    for v in r['verbs']:
        tot+=1; k,d=look(v)
        if 'bloom' in d and d['bloom']:
            placed+=1; rk=max(BR.index(c) for c in d['bloom'] if c in BR)+1; rows[(r['src'],r['step'])].append(rk)
        else: unplaced[v]+=1
        if 'solo' in d and d['solo']:
            sk=[SR.index(c) for c in d['solo'] if c in SR]
            if sk: solo[(r['src'],r['step'])].append(max(sk))
print('placed',placed,'of',tot); print('unplaced',unplaced.most_common(25))
res={}
for s in STEPS:
    line=[]
    for src in ('cqfw','fheq','fqheis','dublin'):
        x=rows.get((src,s))
        if x: line.append(f'{src}:{sum(x)/len(x):.1f}(n{len(x)})')
    res[s]={src:(round(sum(rows[(src,s)])/len(rows[(src,s)]),2),len(rows[(src,s)])) for src in ('cqfw','fheq','fqheis','dublin') if rows.get((src,s))}
    # top bloom level counts all srcs
    allx=[v for src in ('cqfw','fheq','fqheis','dublin') for v in rows.get((src,s),[])]
    dist=collections.Counter(allx)
    res[s]['dist']={BR[k-1]:dist.get(k,0) for k in range(1,7)}
    print(s,' '.join(line),dict(dist))
json.dump({'mean':res,'placed':placed,'total':tot,'unplaced':unplaced.most_common()},open('rf_bloom.json','w'),indent=0)
