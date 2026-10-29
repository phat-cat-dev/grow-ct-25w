#!/usr/bin/env python3
"""apply-house-rules.py - apply the content house rules to a built course folder.

Two rules, both idempotent, so the tool can be re-run after merge-context.js
regenerates a course:

  1. Worked examples are collapsed panels. A worked-example block's `text`
     component becomes a one-item accordion with _classes
     "worked-example-panel" (styled as the checklist in the grow-ct theme).
     Opening it completes the component, so the trickle waits on it.

  2. Fictional students take Welsh first names from
     design-kb/design-kb.name-bank.json. In each worked example the weaker
     student (first name in the we-weaker paragraph) and the stronger one (in
     we-stronger) are renamed to a female + male pair from the bank. The weaker
     role alternates by lesson (male in odd lessons, female in even), every pair
     is new within the course, and the choice is deterministic per course slug.
     Names already in the bank are left alone.

Run from the repo root:
    python tools/apply-house-rules.py courses/_generated/ai-technology-introductory-school-of-sport
    python tools/apply-house-rules.py <course-dir> --check     # report only
"""
import argparse, hashlib, json, os, re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME_BANK = os.path.join(REPO_ROOT, 'design-kb', 'design-kb.name-bank.json')
PANEL_CLASS = 'worked-example-panel'


def load(path):
    return json.load(open(path, encoding='utf-8'))


def save(path, doc):
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(doc, ensure_ascii=False, indent=2) + '\n')


def lead_name(html, cls):
    """The first word of the paragraph with class `cls`, taken as its student's name."""
    m = re.search(r'<p class="%s">\s*([A-Z][\wÀ-ſ]+)' % cls, html or '')
    return m.group(1) if m else None


def to_panel(c):
    """A worked-example text component -> a one-item collapsed accordion."""
    new = {k: c[k] for k in ('_id', '_parentId', '_type') if k in c}
    new.update({
        '_component': 'accordion',
        '_classes': ((c.get('_classes') or '') + ' ' + PANEL_CLASS).strip(),
        '_layout': c.get('_layout', 'full'),
        'title': c.get('title') or 'Worked example',
        'displayTitle': '',
        'body': '',
        'instruction': 'Select the heading to open the worked example.',
        '_shouldCollapseItems': True,
        '_shouldExpandFirstItem': False,
        '_items': [{'title': c.get('displayTitle') or 'Worked example', 'body': c.get('body') or ''}],
    })
    for k in ('_pageLevelProgress', '_trackingId', '_isOptional', '_isAvailable'):
        if k in c:
            new[k] = c[k]
    return new


def body_of(c):
    return c['_items'][0]['body'] if c.get('_component') == 'accordion' else c.get('body') or ''


def set_body(c, html):
    if c.get('_component') == 'accordion':
        c['_items'][0]['body'] = html
    else:
        c['body'] = html


def picker(slug, bank, used):
    """Deterministic walk through the bank for this course, skipping used names."""
    start = int(hashlib.sha1(slug.encode('utf-8')).hexdigest(), 16)
    pos = {'female': start % len(bank['female']), 'male': (start // 7) % len(bank['male'])}

    def take(gender):
        names = bank[gender]
        for _ in range(len(names)):
            n = names[pos[gender] % len(names)]
            pos[gender] += 3
            if n not in used:
                used.add(n)
                return n
        raise SystemExit('name bank exhausted for ' + gender)
    return take


def main():
    ap = argparse.ArgumentParser(description='Apply the content house rules to a course folder.')
    ap.add_argument('course_dir')
    ap.add_argument('--check', action='store_true', help='report only, write nothing')
    args = ap.parse_args()

    en = os.path.join(args.course_dir, 'en')
    slug = os.path.basename(os.path.normpath(args.course_dir))
    bank = load(NAME_BANK)
    in_bank = set(bank['female']) | set(bank['male'])
    blocks = {b['_id']: b for b in load(os.path.join(en, 'blocks.json'))}
    comps = load(os.path.join(en, 'components.json'))

    worked = [i for i, c in enumerate(comps)
              if blocks.get(c['_parentId'], {}).get('_skeletonKey') == 'worked-example']
    used = set()
    for i in worked:
        b = body_of(comps[i])
        used |= {n for n in (lead_name(b, 'we-weaker'), lead_name(b, 'we-stronger')) if n in in_bank}
    take = picker(slug, bank, used)

    panels, renames = [], []
    for i in worked:
        c = comps[i]
        if c['_component'] == 'text':
            comps[i] = c = to_panel(c)
            panels.append(c['_id'])
        html = body_of(c)
        weak, strong = lead_name(html, 'we-weaker'), lead_name(html, 'we-stronger')
        if not weak or not strong or (weak in in_bank and strong in in_bank):
            continue
        lesson = int(re.match(r'L(\d+)', c['_id']).group(1)) if re.match(r'L(\d+)', c['_id']) else 1
        weak_gender = 'male' if lesson % 2 else 'female'
        new_weak = take(weak_gender)
        new_strong = take('female' if weak_gender == 'male' else 'male')
        # swap via placeholders so a new name can never be caught by the next pass
        html = re.sub(r'\b%s\b' % re.escape(weak), '\x00W\x00', html)
        html = re.sub(r'\b%s\b' % re.escape(strong), '\x00S\x00', html)
        set_body(c, html.replace('\x00W\x00', new_weak).replace('\x00S\x00', new_strong))
        renames.append('%s: %s -> %s (weaker), %s -> %s' % (c['_id'], weak, new_weak, strong, new_strong))

    # the old names must not survive anywhere else in the course
    old = {r.split(': ')[1].split(' -> ')[0] for r in renames} | {r.split(', ')[1].split(' -> ')[0] for r in renames}
    stray = []
    for name in ('course.json', 'contentObjects.json', 'articles.json', 'blocks.json'):
        text = open(os.path.join(en, name), encoding='utf-8').read()
        stray += ['%s in %s' % (n, name) for n in old if re.search(r'\b%s\b' % re.escape(n), text)]
    comp_text = json.dumps(comps, ensure_ascii=False)
    stray += ['%s in components.json' % n for n in old if re.search(r'\b%s\b' % re.escape(n), comp_text)]

    print('%s: %d worked example(s); panels %s; renamed %d' % (slug, len(worked), panels or 'none', len(renames)))
    for r in renames:
        print('  ' + r)
    if stray:
        print('  WARNING old names still present: ' + ', '.join(stray))
    if not args.check:
        save(os.path.join(en, 'components.json'), comps)


if __name__ == '__main__':
    main()
