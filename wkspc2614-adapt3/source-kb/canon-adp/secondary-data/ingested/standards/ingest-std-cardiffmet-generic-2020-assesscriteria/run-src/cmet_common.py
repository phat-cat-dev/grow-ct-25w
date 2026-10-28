import json, re
S='/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
G=json.load(open(S+'/cmet-grid.json'))
SLUG={'Overall summary':'overall','Knowledge & Understanding':'knowledge','Presentation and communication':'presentation','Analysis & discussion':'analysis','Research / scholarship':'research','Structured argument and critical evaluation':'argument'}
def rng(b): return re.match(r'(\d+)%?-(\d+)%', b).group(0).replace('%','')
def key(t): return ' '.join(re.sub(r'level [3-7]','level N',re.sub(r'[^a-z0-9 ]',' ',t.lower())).split())
def cells():
    out=[]
    for L in ['3','4','5','6','7']:
        v=G[L]
        for c in v['criteria']:
            for k,x in enumerate(c['cells']):
                b=v['bands'][k]
                out.append(dict(id=f'l{L}/{SLUG[c["criterion"]]}/{rng(b)}',level=int(L),criterion=c['criterion'],crit=SLUG[c['criterion']],band=rng(b),label=b,bi=k,text=x,key=key(x)))
    first={}
    for c in out: first.setdefault(c['key'],c['id']); c['first']=first[c['key']]
    return out
import difflib
def sim(a, b):
    return difflib.SequenceMatcher(None, a.split(), b.split()).ratio()
def resolve(th=0.85):
    """each cell's version source: itself, an identical earlier cell (sameAs), or a near-identical cell at an earlier level, same criterion and band (like)."""
    C = cells(); byid = {c['id']: c for c in C}
    for c in C:
        c['src'] = c['first']; c['rel'] = 'self' if c['first'] == c['id'] else 'sameAs'; c['sim'] = 1.0
        if c['rel'] == 'self':
            prev = [p for p in C if p['crit'] == c['crit'] and p['band'] == c['band'] and p['level'] < c['level'] and p['src'] == p['id']]
            best = max(prev, key=lambda p: sim(p['key'], c['key']), default=None)
            if best is not None and sim(best['key'], c['key']) >= th:
                c['src'] = best['id']; c['rel'] = 'like'; c['sim'] = round(sim(best['key'], c['key']), 2)
    return C
def resolved(th=0.95):
    C = resolve(th); by = {c['id']: c for c in C}
    for c in C:
        s = c['src']
        while by[s]['src'] != s: s = by[s]['src']
        c['src'] = s
    return C
def split(t):
    t = ' '.join(t.split())
    return [x for x in re.split(r'(?<=[.])\s+(?=[A-Z])', t) if x.strip()]
def sentences(th=0.95):
    """sentence records: id <cell>.s<n>; version source: own, sameAs (identical sentence anywhere earlier) or like (>= th, same criterion and band, earlier level)."""
    C = resolved(th); out = []
    for c in C:
        if not c['text']: continue
        for n, x in enumerate(split(c['text']), 1):
            out.append(dict(c, id=f"{c['id']}.s{n}", cell=c['id'], n=n, text=x, key=key(x)))
    first = {}
    for s in out:
        first.setdefault(s['key'], s['id']); s['src'] = first[s['key']]; s['rel'] = 'self' if s['src'] == s['id'] else 'sameAs'; s['sim'] = 1.0
    own = []
    for s in out:
        if s['rel'] == 'self':
            cand = [p for p in own if p['crit'] == s['crit'] and p['band'] == s['band'] and p['level'] < s['level']]
            best = max(cand, key=lambda p: sim(p['key'], s['key']), default=None)
            if best is not None and sim(best['key'], s['key']) >= th:
                s['src'] = best['id']; s['rel'] = 'like'; s['sim'] = round(sim(best['key'], s['key']), 2)
            else: own.append(s)
    by = {s['id']: s for s in out}
    for s in out:
        x = s['src']
        while by[x]['src'] != x: x = by[x]['src']
        s['src'] = x
    return out
