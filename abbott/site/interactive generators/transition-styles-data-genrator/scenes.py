#!/usr/bin/env python3
"""scenes.py: make, prompt, check and render scroll-scenes content.

    python scenes.py new <topic_id> --topic "Evaluating a source" [options]
        Writes <topic_id>.yaml (blank content, topic filled in) and
        <topic_id>.prompt.md (paste this into any agent).

    python scenes.py revise <filled.yaml> --change "Make Set B shorter"
        Writes <name>.revise-prompt.md for an agent to apply the change.

    python scenes.py check <filled.yaml>
        Validates an agent's output. Exit code 0 means valid.

    python scenes.py render <filled.yaml> --set rec --preset calm
        Writes a finished HTML page. Standalone by default (one file).

    python scenes.py schema-prompts
        Prints the per-field prompts held in scene-content.schema.json.

Needs: pip install pyyaml jsonschema
Keep this file beside scene-content.template.yaml, scene-content.schema.json,
scroll-scenes.css, scroll-scenes.backgrounds.css and scroll-scenes.patched.js.
"""
import argparse
import copy
import html
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

HERE = Path(__file__).parent
TEMPLATE = HERE / "scene-content.template.yaml"
SCHEMA = HERE / "scene-content.schema.json"
FILLED_EXAMPLE = HERE / "scene-content.filled-example.yaml"


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def dump(obj):
    return yaml.dump(obj, Dumper=NoAliasDumper, allow_unicode=True, sort_keys=False, width=100)


def load_template():
    return yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))


def load_filled(path):
    """Load a filled file. Tolerates an agent wrapping its answer in a code fence."""
    text = Path(path).read_text(encoding="utf-8")
    fenced = re.search(r"```(?:ya?ml)?\s*\n(.*?)```", text, re.S)
    if fenced:
        text = fenced.group(1)
    doc = yaml.safe_load(text)
    if not isinstance(doc, dict):
        sys.exit(f"{path}: not a YAML mapping")
    return doc.get("content", doc)


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "topic"


def read(name):
    return (HERE / name).read_text(encoding="utf-8")


# ----------------------------------------------------------------------------
# check
# ----------------------------------------------------------------------------
def validate(content, schema_path=SCHEMA):
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    errors, warnings = [], []
    for e in sorted(Draft202012Validator(schema).iter_errors(content), key=lambda e: list(e.absolute_path)):
        path = ".".join(str(p) for p in e.absolute_path) or "(root)"
        msg = e.message if len(e.message) < 160 else e.message[:157] + "..."
        errors.append(f"{path}: {msg}")
    try:
        d00, sets = content["d00"], content["sets"]
        enabled = set(d00.get("layers_enabled", []))
        contexts = set(d00.get("contexts") or [])
        for name, s in sets.items():
            keys = [sc.get("key") for sc in s.get("d01", [])]
            if len(keys) != len(set(keys)):
                errors.append(f"sets.{name}: scene keys are not unique")
            for i, sc in enumerate(s.get("d01", [])):
                where = f"sets.{name}.d01[{i}]"
                lay = sc.get("layers", {})
                last = i == len(s["d01"]) - 1
                for lid in enabled:
                    if lid not in lay:
                        errors.append(f"{where}.layers.{lid}: enabled layer is missing")
                    elif lay[lid] is None and not (lid == "transition_cue" and last) and lid != "sources":
                        warnings.append(f"{where}.layers.{lid}: enabled layer is null")
                for lid in lay:
                    if lid not in enabled:
                        errors.append(f"{where}.layers.{lid}: layer is not in d00.layers_enabled")
                cv = lay.get("context_variants")
                if isinstance(cv, dict) and set(cv) != contexts:
                    errors.append(f"{where}.layers.context_variants: keys {sorted(cv)} do not match d00.contexts {sorted(contexts)}")
                rc = lay.get("retrieval_check")
                if rc and rc["answer_index"] >= len(rc["options"]):
                    errors.append(f"{where}.layers.retrieval_check: answer_index is outside the options")
                if last and lay.get("transition_cue"):
                    warnings.append(f"{where}.layers.transition_cue: last scene should have none")
        b_labels = {sc["stage_label"].lower() for sc in sets["B"]["d01"] if isinstance(sc.get("stage_label"), str)}
        if b_labels & {"trace", "test", "cross-check", "judge", "log"}:
            warnings.append("sets.B reuses stage names from the example. Check they fit this topic.")
        if b_labels == {"observe", "question", "explore", "act"}:
            errors.append("sets.B is the same model as Set A")
    except (KeyError, TypeError, AttributeError) as exc:
        errors.append(f"structure: could not run extra checks ({exc!r})")
    blob = json.dumps(content, ensure_ascii=False)
    for m in re.finditer(r"\b[\w-]+,\s+[\w-]+(?:\s[\w-]+)?,\s+(?:and|or)\s", dump(content)):
        warnings.append(f"possible Oxford comma near: {m.group(0)!r}")
    for w in re.findall(r"\b(color\w*|behavior\w*|organiz\w*|center\w*|analyz\w*|recogniz\w*|prioritiz\w*)\b", blob, re.I):
        warnings.append(f"US spelling: {w}")
    return errors, warnings


def cmd_check(args):
    errors, warnings = validate(load_filled(args.file), args.schema or SCHEMA)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


# ----------------------------------------------------------------------------
# prompts
# ----------------------------------------------------------------------------
def schema_prompts():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    defs = schema.get("$defs", {})
    out = []

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if "$ref" in node:
            walk(defs[node["$ref"].split("/")[-1]], path)
        if "x-agent-prompt" in node and path:
            out.append((path, node["x-agent-prompt"]))
        for k, v in node.get("properties", {}).items():
            walk(v, f"{path}.{k}" if path else k)
        if "prefixItems" in node:
            walk(node["prefixItems"][0], path + "[]")
        if isinstance(node.get("items"), dict):
            walk(node["items"], path + "[]")
        if isinstance(node.get("additionalProperties"), dict):
            walk(node["additionalProperties"], path + ".<key>")

    walk(schema, "")
    seen, rows = set(), []
    for path, text in out:
        path = re.sub(r"sets\.[AB]\.d01\[\]", "sets.<A|B>.d01[]", path)
        if (path, text) not in seen:
            seen.add((path, text))
            rows.append((path, text))
    return rows


def layer_block(tpl, enabled):
    reg = {l["id"]: l for l in tpl["layers_registry"]}
    lines = []
    for lid in enabled:
        l = reg[lid]
        lines.append(f"- {lid}\n    shape: {l['shape']}\n    limits: {l['limits']}\n    do: {' '.join(str(l['agent_instruction']).split())}")
    return "\n".join(lines)


def models_block(tpl):
    m = tpl["models"]
    stages = "\n".join(f"- {s['label']}: {s['purpose']}" for s in m["oqea"]["stages"])
    rules = "\n".join(f"- {r}" for r in m["custom"]["rules"])
    return f"Set A is the fixed OQEA model:\n{stages}\n\nRules for Set B, your own model:\n{rules}"


def common_rules(tpl, enabled):
    fields = "\n".join(f"- {p}: {t}" for p, t in schema_prompts())
    return (
        "FIELD PROMPTS (one per field in the file)\n" + fields +
        "\n\nLAYERS TO FILL (d00.layers_enabled)\n" + layer_block(tpl, enabled) +
        "\n\nMODELS\n" + models_block(tpl)
    )


OUTPUT_RULES = (
    "OUTPUT FORMAT\n"
    "Return the `content` block only, as one YAML document that starts with `d00:`. "
    "Keep every key. Fill every null that the instructions above ask you to fill. "
    "Put the YAML in a single code block and write nothing else."
)


def cmd_new(args):
    tpl = load_template()
    content = copy.deepcopy(tpl["content"])
    all_layers = [l["id"] for l in tpl["layers_registry"]]
    enabled = all_layers if args.layers == "all" else (args.layers.split(",") if args.layers else content["d00"]["layers_enabled"])
    bad = [l for l in enabled if l not in all_layers]
    if bad:
        sys.exit(f"Unknown layer id(s): {', '.join(bad)}. Choose from: {', '.join(all_layers)}")
    d00 = content["d00"]
    d00.update(topic_id=slugify(args.topic_id), topic=args.topic, title=args.title,
               audience=args.audience, learning_aim=args.aim, layers_enabled=enabled)
    if args.contexts:
        d00["contexts"] = args.contexts.split(",")
    if args.preset:
        preset = next((p for p in tpl["style_presets"] if p["id"] == args.preset), None)
        if not preset:
            sys.exit(f"Unknown preset. Choose from: {', '.join(p['id'] for p in tpl['style_presets'])}")
        d00["presentation"].update(preset=preset["id"], scheme=preset["scheme"], background=preset["background"],
                                   transition=preset["transition"], effect=preset["effect"])
    for key in ("A", "B"):
        for sc in content["sets"][key]["d01"]:
            sc["layers"] = {lid: None for lid in enabled}
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = d00["topic_id"]
    blank = dump({"content": content})
    (out_dir / f"{stem}.yaml").write_text(f"# Blank content for: {args.topic}\n# Give {stem}.prompt.md to an agent, save its answer as {stem}.filled.yaml, then run:\n#   python scenes.py check {stem}.filled.yaml\n" + blank, encoding="utf-8")
    example = FILLED_EXAMPLE.read_text(encoding="utf-8") if FILLED_EXAMPLE.exists() else ""
    prompt = (
        tpl["agent_author_prompt"].rstrip() + "\n\n" + OUTPUT_RULES + "\n\n" + common_rules(tpl, enabled) +
        ("\n\nSHAPE EXAMPLE (a different topic: copy the structure, never the words)\n```yaml\n" + example.rstrip() + "\n```" if example else "") +
        f"\n\nTOPIC: {args.topic}\n\nFILE TO FILL\n```yaml\n" + blank.rstrip() + "\n```\n"
    )
    (out_dir / f"{stem}.prompt.md").write_text(prompt, encoding="utf-8")
    print(f"wrote {out_dir / (stem + '.yaml')}\nwrote {out_dir / (stem + '.prompt.md')}  ({len(prompt.split())} words)")
    return 0


def cmd_revise(args):
    tpl = load_template()
    content = load_filled(args.file)
    enabled = content["d00"]["layers_enabled"]
    prompt = (
        "You are revising an existing scroll-scenes content file. Apply the change request below and "
        "change nothing else. Keep every rule from the brief.\n\n"
        "BRIEF\n" + tpl["agent_author_prompt"].rstrip() + "\n\n"
        "CHANGE REQUEST\n" + args.change.strip() + "\n\n" + OUTPUT_RULES.replace("Fill every null that the instructions above ask you to fill.", "Return the whole updated block.") +
        "\n\n" + common_rules(tpl, enabled) + "\n\nCURRENT FILE\n```yaml\n" + dump({"content": content}).rstrip() + "\n```\n"
    )
    out = Path(args.file).with_suffix("").with_suffix(".revise-prompt.md") if Path(args.file).suffix else Path(args.file + ".revise-prompt.md")
    out.write_text(prompt, encoding="utf-8")
    print(f"wrote {out}  ({len(prompt.split())} words)")
    return 0


def cmd_schema_prompts(_):
    for path, text in schema_prompts():
        print(f"{path}\n    {text}")
    return 0


# ----------------------------------------------------------------------------
# render
# ----------------------------------------------------------------------------
EXTRA_CSS = """
.scroll-scenes .scene-extra { max-inline-size: 46ch; margin-block: .6rem 0; font-size: .95rem; }
.scroll-scenes .scene-extra strong { color: var(--scene-accent); }
.scroll-scenes .scene-cue { font-style: italic; opacity: .85; }
"""


def esc(text):
    return html.escape(str(text), quote=True)


def extras_html(layers, show):
    parts = []
    for lid in show:
        v = layers.get(lid)
        if not v:
            continue
        if lid == "question_prompt":
            parts.append(f'<p class="scene-extra"><strong>Ask yourself:</strong> {esc(v)}</p>')
        elif lid == "micro_task":
            parts.append(f'<p class="scene-extra"><strong>Try this ({esc(v["minutes"])} min):</strong> {esc(v["instruction"])}</p>')
        elif lid == "evidence_cue":
            parts.append(f'<p class="scene-extra"><strong>You will know it worked when:</strong> {esc(v)}</p>')
        elif lid == "transition_cue":
            parts.append(f'<p class="scene-extra scene-cue">{esc(v)}</p>')
        elif lid == "reflection_note":
            parts.append(f'<p class="scene-extra"><strong>In your notes:</strong> {esc(v)}</p>')
        else:
            sys.exit(f"--show-layers: layer '{lid}' has no visual form. Use: question_prompt, micro_task, evidence_cue, transition_cue, reflection_note")
    return "\n        ".join(parts)


def render_page(content, set_key, tpl, args):
    d00 = content["d00"]
    pres = dict(d00.get("presentation") or {})
    if args.preset:
        preset = next((p for p in tpl["style_presets"] if p["id"] == args.preset), None)
        if not preset:
            sys.exit(f"Unknown preset. Choose from: {', '.join(p['id'] for p in tpl['style_presets'])}")
        pres.update({k: preset[k] for k in ("scheme", "background", "transition", "effect")})
    for key, val in (("scheme", args.scheme), ("background", args.background), ("transition", args.transition), ("effect", args.effect)):
        if val:
            pres[key] = None if val == "none-value" else val
    scenes = content["sets"][set_key]["d01"]
    title = d00["title"]
    attrs = []
    if pres.get("scheme") and pres["scheme"] != "default":
        attrs.append(f'data-scheme="{esc(pres["scheme"])}"')
    if pres.get("background"):
        attrs.append(f'data-scene-bg="{esc(pres["background"])}"')
    if pres.get("transition"):
        attrs.append(f'data-scene-transition="{esc(pres["transition"])}"')
    show = [s for s in (args.show_layers.split(",") if args.show_layers else []) if s]
    nav, secs = [], []
    for i, sc in enumerate(scenes):
        nn, label = f"{i + 1:02d}", sc["stage_label"]
        nav.append(f'<button type="button" data-scroll-to="{i}">{nn} {esc(label)}</button>')
        sattr = ""
        if sc.get("background"):
            sattr += f' data-scene-bg="{esc(sc["background"])}"'
        if sc.get("colour_slot"):
            sattr += f' data-scene-colour="{int(sc["colour_slot"])}"'
        extra = extras_html(sc.get("layers", {}), show)
        secs.append(
            f'<section data-scroll-scene aria-label="{esc(label)}"{sattr}><div data-scene-content>\n'
            f'        <p class="scene-number">{nn} / {esc(label.upper())}</p>\n'
            f'        <h2>{"<br>".join(esc(l) for l in sc["heading_lines"])}</h2>\n'
            f'        <p class="scene-copy">{esc(sc["body"])}</p>'
            + (f"\n        {extra}" if extra else "") + "\n      </div></section>"
        )
    css = read("scroll-scenes.css") + "\n" + read("scroll-scenes.backgrounds.css") + EXTRA_CSS
    js = read("scroll-scenes.patched.js")
    if "</script" in js:
        sys.exit("scroll-scenes.patched.js contains </script; cannot inline")
    effect = pres.get("effect") or "zoom"
    mount = (
        "if (typeof ScrollScenes === 'undefined') { document.body.insertAdjacentHTML('afterbegin', "
        "'<p style=\"padding:1rem;background:#fde8e8;color:#600\">The scroll scenes script did not load. Check the browser console.</p>'); } "
        f"else {{ ScrollScenes.mount(document.querySelector('.scroll-scenes'), {{ effect: '{esc(effect)}', snap: {'true' if pres.get('snap', True) else 'false'} }}); }}"
    )
    if args.linked:
        head_assets = '<link rel="stylesheet" href="scroll-scenes.css">\n  <link rel="stylesheet" href="scroll-scenes.backgrounds.css">\n  <style>' + EXTRA_CSS + "</style>"
        script = '<script src="scroll-scenes.patched.js"></script>\n  <script>\n    ' + mount + "\n  </script>"
    else:
        head_assets = "<style>\n" + css + "\n  </style>"
        script = "<script>\n" + js + "\n\n    " + mount + "\n  </script>"
    vp_label = "Scrollable " + title[:1].lower() + title[1:]
    return (
        '<!doctype html>\n<html lang="en-GB">\n<head>\n  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{esc(title)}</title>\n  {head_assets}\n  <style>body {{ margin: 0; padding: 1rem; }}</style>\n</head>\n<body>\n"
        f'  <main class="scroll-scenes" aria-label="{esc(title)}" {" ".join(attrs)}>\n'
        '    <nav class="scene-nav" aria-label="Choose a scene">\n      ' + "\n      ".join(nav) + "\n"
        '      <progress data-scroll-progress max="1" value="0" aria-label="Scroll progress"></progress>\n'
        '      <span class="scene-status" data-scroll-status aria-live="polite"></span>\n    </nav>\n'
        f'    <div data-scroll-viewport tabindex="0" role="region" aria-label="{esc(vp_label)}">\n      '
        + "\n      ".join(secs) + "\n    </div>\n  </main>\n  " + script + "\n</body>\n</html>\n"
    )


def cmd_render(args):
    tpl = load_template()
    content = load_filled(args.file)
    errors, warnings = validate(content)
    if errors and not args.force:
        for e in errors[:10]:
            print("ERROR", e)
        sys.exit(f"{len(errors)} error(s). Fix the file or use --force to render anyway.")
    which = ["A", "B"] if args.set == "both" else [content["recommendation"]["set"] if args.set == "rec" else args.set]
    base = Path(args.out) if args.out else Path(args.file).with_suffix("")
    for key in which:
        out = base.with_name(f"{base.stem}.{key}.html") if len(which) > 1 else (Path(args.out) if args.out else base.with_name(base.stem + ".html"))
        out.write_text(render_page(content, key, tpl, args), encoding="utf-8")
        print(f"wrote {out}  (Set {key}, {len(content['sets'][key]['d01'])} scenes)")
    return 0


# ----------------------------------------------------------------------------
def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("new", help="start a new topic and write its agent prompt")
    n.add_argument("topic_id")
    n.add_argument("--topic", required=True)
    n.add_argument("--title")
    n.add_argument("--audience")
    n.add_argument("--aim")
    n.add_argument("--contexts", help="comma separated ids, for the context_variants layer")
    n.add_argument("--layers", help="comma separated layer ids, or 'all'")
    n.add_argument("--preset")
    n.add_argument("--out-dir", default=".")
    n.set_defaults(fn=cmd_new)

    r = sub.add_parser("revise", help="write a prompt that changes an existing filled file")
    r.add_argument("file")
    r.add_argument("--change", required=True)
    r.set_defaults(fn=cmd_revise)

    c = sub.add_parser("check", help="validate an agent's output")
    c.add_argument("file")
    c.add_argument("--schema")
    c.set_defaults(fn=cmd_check)

    g = sub.add_parser("render", help="write the finished HTML page")
    g.add_argument("file")
    g.add_argument("--set", choices=["A", "B", "rec", "both"], default="rec")
    g.add_argument("--preset")
    g.add_argument("--scheme")
    g.add_argument("--background")
    g.add_argument("--transition")
    g.add_argument("--effect")
    g.add_argument("--show-layers", help="comma separated: question_prompt,micro_task,evidence_cue,transition_cue,reflection_note")
    g.add_argument("--linked", action="store_true", help="link the CSS and JS files instead of inlining them")
    g.add_argument("--out")
    g.add_argument("--force", action="store_true")
    g.set_defaults(fn=cmd_render)

    s = sub.add_parser("schema-prompts", help="print the per-field prompts")
    s.set_defaults(fn=cmd_schema_prompts)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
