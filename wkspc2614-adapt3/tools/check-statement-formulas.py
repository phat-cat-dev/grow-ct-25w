#!/usr/bin/env python3
"""check-statement-formulas.py - validate the tokenised formula layer on
catalogue/context/subject/benchmarks/universal-reference.json: a statement
formula (template + sourceFill, reproduces the live statement byte-for-byte)
plus atomic AL-2 outcome formulas, per tierReadings row/field and per
graduate_competency item (both registers: forPractitioner, forBeneficiary).

Checks:
  - fidelity: template.format(**sourceFill) == the live statement text, for
    every statement-level formula. This is the load-bearing check: it proves
    the tokenisation lost nothing.
  - closure, both ways: every {slot} in a template is declared (sourceFill
    keys for statement formulas; slot keys for outcome formulas), and every
    declared key is used. No orphans in either direction.
  - role within the closed 8-role set (verb, object, condition, field_content,
    scope, qualifier, audience, stance); every outcome formula has exactly
    one verb, one object and one condition slot (section 15.8 + rule AL-2).
  - AL-2: no literal "and" in an outcome template's own fixed text (slot
    options may bundle "and" inside one noun phrase; that is one object, not
    two tasks).
  - every verb slot's options are a non-empty subset of the section 16 band
    it names, and the band name is real, so drift from section 16 fails the
    build rather than passing silently. Bands are parsed live from the voice
    specification here (never a second hand-typed list) - mirrors
    tools/build-prompt-sets.py's verb_bands(); the parser is duplicated by
    design, the data is not.
  - no verb option is in the section 15.8 banned-vague set.
  - rebuild demo: filling every template with each slot's first option yields
    a non-empty sentence ending in a full stop, with no leftover braces.
  - subjectSupplied slots carry a floor; non-subjectSupplied slots do not.
  - agentInstruction present on every formula and every outcome, 15-60 words.
  - house rules on raw file text: no em dash (U+2014), never "academic
    skills".

Run from the repo root:
    python tools/check-statement-formulas.py
"""
import json, os, re, sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC_PATH = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.json')
VOICE_SPEC = os.path.join(REPO_ROOT, 'reference', 'excelling-voice-specification.md')

ROLES = {'verb', 'object', 'condition', 'field_content', 'scope', 'qualifier', 'audience', 'stance'}
BANNED_VAGUE = {'understand', 'know', 'appreciate', 'be aware of', 'knows', 'understands', 'appreciates'}
REGISTERS = (('forPractitioner', 'graduateStatement'), ('forBeneficiary', 'studentStatement'))


def verb_bands():
    """Section 16 of the voice specification: band name -> outcome verbs.
    Mirrors tools/build-prompt-sets.py's verb_bands(); the parser is
    duplicated by design (section 16 is the one authoritative list), the
    data is not."""
    bands = {}
    for line in open(VOICE_SPEC, encoding='utf-8'):
        m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|.*Outcome verbs:\s*([^|]+?)\.?\s*\|\s*$', line)
        if m:
            bands[m.group(1)] = [v.strip() for v in m.group(2).split(',') if v.strip()]
    return bands


def words(s):
    return len(re.findall(r"[A-Za-z0-9']+", s or ''))


def check_formula(f, bands, is_statement, live_text=None):
    errs = []
    tmpl = f.get('template', '')
    used = set(re.findall(r'\{(\w+)\}', tmpl))
    slots = f.get('slots') or []
    slot_keys = {s.get('key') for s in slots}

    if is_statement:
        fill = f.get('sourceFill') or {}
        declared = set(fill.keys())
        if used != declared:
            errs.append('closure mismatch (template vs sourceFill): template=%s sourceFill=%s'
                        % (sorted(used), sorted(declared)))
        elif live_text is not None:
            rebuilt = tmpl.format(**fill)
            if rebuilt != live_text:
                errs.append('fidelity mismatch: rebuilt=%r live=%r' % (rebuilt, live_text))
        if used != slot_keys:
            errs.append('closure mismatch (template vs slots): template=%s slots=%s'
                        % (sorted(used), sorted(slot_keys)))
    else:
        if used != slot_keys:
            errs.append('closure mismatch (template vs slots): template=%s slots=%s'
                        % (sorted(used), sorted(slot_keys)))
        roles = [s.get('role') for s in slots]
        for req in ('verb', 'object', 'condition'):
            c = roles.count(req)
            if c != 1:
                errs.append('needs exactly one %s slot, has %d' % (req, c))
        if re.search(r'\band\b', tmpl):
            errs.append('AL-2: literal "and" in outcome template (risks joining two tasks): %r' % tmpl)

    n = words(f.get('agentInstruction', ''))
    if not (15 <= n <= 60):
        errs.append('agentInstruction %d words (want 15-60): %r' % (n, f.get('agentInstruction')))

    for s in slots:
        key = s.get('key', '?')
        role = s.get('role')
        if role not in ROLES:
            errs.append('slot %s: bad role %r' % (key, role))
        if s.get('subjectSupplied'):
            if 'floor' not in s:
                errs.append('slot %s: subjectSupplied but missing floor' % key)
        elif 'floor' in s:
            errs.append('slot %s: has floor but not subjectSupplied' % key)
        opts = s.get('options') or []
        if not opts:
            errs.append('slot %s: no options' % key)
        if role == 'verb':
            band = s.get('verbBand')
            if band not in bands:
                errs.append('slot %s: bad verbBand %r (not a real section 16 band)' % (key, band))
            else:
                bad = [o for o in opts if o not in bands[band]]
                if bad:
                    errs.append('slot %s: verb options not subset of %s band: %s' % (key, band, bad))
            bad_vague = [o for o in opts if o.lower() in BANNED_VAGUE]
            if bad_vague:
                errs.append('slot %s: banned vague verb (section 15.8) in options: %s' % (key, bad_vague))

    demo_fill = {}
    ok_for_demo = True
    for key in used:
        matches = [s for s in slots if s.get('key') == key and s.get('options')]
        if matches:
            demo_fill[key] = matches[0]['options'][0]
        else:
            ok_for_demo = False
            errs.append('template key %r has no matching slot with options' % key)
    if ok_for_demo:
        try:
            demo = tmpl.format(**demo_fill)
            if not demo.strip().endswith('.') or '{' in demo or '}' in demo or not demo.strip():
                errs.append('rebuild demo malformed: %r' % demo)
        except Exception as e:
            errs.append('rebuild demo exception: %s' % e)

    return errs


def check():
    errs = []
    if not os.path.exists(DOC_PATH):
        return ['missing ' + os.path.relpath(DOC_PATH, REPO_ROOT)], 0, 0
    raw = open(DOC_PATH, encoding='utf-8').read()
    if '\u2014' in raw:
        errs.append('em dash present')
    for m in re.finditer(r'academic skills', raw, re.I):
        # the house rule note itself names the banned term in quotes
        # (...never \"academic skills\".) - that sanctioned self-reference is
        # not a violation; anything else matching is.
        before, after = raw[max(0, m.start() - 2):m.start()], raw[m.end():m.end() + 2]
        if before.endswith('\\"') and after.startswith('\\"'):
            continue
        errs.append('"academic skills" present')
        break
    doc = json.loads(raw)
    bands = verb_bands()
    if not bands:
        errs.append('no section 16 bands parsed from ' + os.path.relpath(VOICE_SPEC, REPO_ROOT))

    seen_stmt = 0
    seen_outcomes = 0

    rows = (doc.get('tierReadings') or {}).get('rows') or []
    for row in rows:
        row_id = row.get('rowId', '?')
        formulas = row.get('formulas') or {}
        for field in ('practice', 'knowledge', 'identity'):
            f = formulas.get(field)
            label = row_id + '/' + field
            if f is None:
                errs.append(label + ': missing formula')
                continue
            seen_stmt += 1
            ferrs = check_formula(f, bands, True, row.get(field))
            errs.extend(label + ': ' + e for e in ferrs)
            for oc in f.get('outcomes') or []:
                seen_outcomes += 1
                oid = oc.get('id', label + '/o?')
                errs.extend(oid + ': ' + e for e in check_formula(oc, bands, False))

    items = (doc.get('graduate_competency') or {}).get('items') or []
    for item in items:
        iid = item.get('id', '?')
        f = item.get('formula')
        if f is None:
            errs.append(iid + ': missing formula')
            continue
        regs = f.get('registers') or {}
        for reg, live_key in REGISTERS:
            rf = regs.get(reg)
            label = iid + '/' + reg
            if rf is None:
                errs.append(label + ': missing register formula')
                continue
            seen_stmt += 1
            ferrs = check_formula(rf, bands, True, item.get(live_key))
            errs.extend(label + ': ' + e for e in ferrs)
            for oc in rf.get('outcomes') or []:
                seen_outcomes += 1
                oid = oc.get('id', label + '/o?')
                errs.extend(oid + ': ' + e for e in check_formula(oc, bands, False))

    if doc.get('statementFormulas') is None:
        errs.append('missing top-level statementFormulas')

    return errs, seen_stmt, seen_outcomes


if __name__ == '__main__':
    errs, seen_stmt, seen_outcomes = check()
    print('%-46s %s' % ('universal-reference.json', 'PASS' if not errs else 'FAIL (%d)' % len(errs)))
    for e in errs:
        print('    - ' + e)
    print()
    print('statement formulas checked:', seen_stmt)
    print('outcome formulas checked:', seen_outcomes)
    sys.exit(1 if errs else 0)
