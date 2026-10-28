import json,collections,re
exec(open('rf_bloom.py').read().split("R=json.load")[0])
S='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/'
G={}
for k,d,j in (('eee','ingest-std-qaa-enterprise-2018-guidance','eee_j.py'),('esd','ingest-std-qaa-advancehe-esd-2021-guidance','esdf_j.py')):
    ns={}; exec(open(f'{S}{d}/run-src/{j}').read(),ns); G[k]=ns['R']
def strand(r):
    t=(r['prac']+' '+' '.join(r['verbs'])).lower()
    if re.search(r'communicat|present|audience|stakeholder|listen|persuad|influenc|negotiat|mediat',t): return 'M'
    if re.search(r'reflect|own learning|lifelong|responsib|resilien|self|motivat|lead|initiative|autonom|independen|mindset|wellbeing|emotion',t): return 'R'
    if re.search(r'evaluat|analys|critical|judg|assess|weigh|question|argument|evidence|risk|decid|decision',t): return 'C'
    if re.search(r'appl|use|implement|plan|design|develop|creat|generat|solution|innovat|act|manage|research|tool',t): return 'A'
    return 'K'
out={}
for k,R in G.items():
    S_=[r for r in R if r['addr'] in ('student','graduate')]
    fam=collections.Counter(r['fam'] for r in R)
    st=collections.Counter(strand(r) for r in S_)
    emp=collections.Counter(r['emp'] for r in R)
    bl=collections.Counter()
    for r in S_:
        if r['verbs']:
            k2,d=look(r['verbs'][0])
            if d.get('bloom'): bl[BR[max(BR.index(c) for c in d['bloom'] if c in BR)]]+=1
    path=collections.Counter(p for r in R for p in r['path'])
    crit=collections.Counter(c for r in R for c in r['crit'])
    out[k]={'n':len(R),'student':len(S_),'fam':fam,'strand':st,'emp':emp,'bloom':bl,'path':path,'crit':crit}
    print(k,len(R),len(S_),dict(fam)); print('  strand',dict(st)); print('  bloom',dict(bl)); print('  emp',dict(emp))
    for r in S_: r['_strand']=strand(r)
json.dump({k:{a:dict(b) if hasattr(b,'items') else b for a,b in v.items()} for k,v in out.items()},open('rg_data.json','w'),indent=0)
json.dump({k:[{'id':r['id'],'fam':r['fam'],'strand':r.get('_strand'),'emp':r['emp'],'verbs':r['verbs'],'cat':r['cat']} for r in R] for k,R in G.items()},open('rg_recs.json','w'))
