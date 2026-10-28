# Held text for QAA and Advance HE ESD Guidance 2021 (full): pdftotext default per page, except pages with ruled tables,
# where text outside the tables comes from pdfplumber and each table is linearised row by row, cell by cell (std, run 0063).
import pdfplumber, subprocess, re
P='/root/.claude/uploads/378bff94-17ab-5a5d-8465-bd8449aca2a6/40ff5bf6-education-for-sustainable-development-guidance_1616774629.pdf'
TP={22,23,26,27,28,29,30,31,32,33,36,37,38,39,40}
B='\x83'
def cell(c):
    t=' '.join((c or '').split())
    return t[::-1] if ('syaW' in t or 'tcejbuS' in t) else t
def bullets(c):
    c=(c or '').replace('',B)
    parts=[p for p in c.split(B)]
    out=[]
    head=' '.join(parts[0].split())
    if head: out.append(head)
    out+=['• '+' '.join(p.split()) for p in parts[1:] if p.strip()]
    return out
def table_lines(rows):
    L=[]; hdr=None
    for r in rows:
        cs=[c for c in r]
        txt=[cell(c) for c in cs]
        if sum(1 for t in txt if t)==1 and not any(B in (c or '') for c in cs):
            L.append(''); L.append(next(t for t in txt if t)); continue
        if not any(B in (c or '') for c in cs) and all(len(t)<40 for t in txt if t):
            hdr=[t for t in txt]; L.append(''); L.append(' | '.join(t for t in txt if t)); continue
        for i,c in enumerate(cs):
            t=cell(c)
            if not t: continue
            if 'syaW' in (c or '') or 'tcejbuS' in (c or ''): L.append(''); L.append(t); continue
            if re.fullmatch(r'[a-z|]+', (c or '').replace('\n','|').replace(' ','')) and t[::-1].istitle()==False and ' ' not in t.strip() : pass
            L.append('')
            if t!=cell(c) or ('syaW' in (c or '') or 'tcejbuS' in (c or '')):
                L.append(t); continue
            if hdr and i<len(hdr) and hdr[i]: L.append(hdr[i])
            L+=bullets(c)
    return L
out=[]
with pdfplumber.open(P) as pdf:
    for n in range(1,len(pdf.pages)+1):
        if n not in TP:
            out.append(subprocess.run(['pdftotext','-f',str(n),'-l',str(n),P,'-'],capture_output=True,text=True).stdout.rstrip('\f')); continue
        pg=pdf.pages[n-1]
        ts=[t for t in pg.find_tables() if t.bbox[1]>1 and (t.bbox[2]-t.bbox[0])>300]
        rest=pg
        for t in ts: rest=rest.outside_bbox(t.bbox)
        txt=(rest.extract_text() or '')
        # drop mirrored vertical labels
        txt='\n'.join(l for l in txt.split('\n') if not re.fullmatch(r'[a-zA-Z ]{1,40}', l) or not any(w in l for w in ('gnik','fo','sGDS','tcej','noit','gni')))
        blocks=[txt]
        for t in sorted(ts,key=lambda t:t.bbox[1]):
            blocks.append('\n'.join(table_lines(t.extract())))
        out.append('\n\n'.join(blocks)+'\n')
raw='\n'.join(out)
raw=raw.replace('','•').replace('Subject knowledge of all knowledge SDGs and','Subject knowledge and knowledge of all SDGs')
open('esdfull_raw.txt','w').write(raw)
print(len(raw))
