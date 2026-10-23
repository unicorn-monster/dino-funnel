#!/usr/bin/env python3
"""Fill an OTO template with a step's content.json.

  python3 .claude/skills/upsell-downsell/scripts/fill.py output/<sp>/5-upsell-downsell/<step>/content.json [--template NAME]

Template defaults to the step folder: upsell-2 -> oto-crosssell, downsell-* -> oto-lastchance, anything else -> oto-classic.

Writes index.html next to content.json. {{KEY}} = string from content.json (HTML allowed),
{{#LIST}}...{{/LIST}} = repeat the block once per item of a list of objects (keys inside are the item's keys).
Exits 1 if any {{...}} is left unfilled.
"""
import json, re, sys
from pathlib import Path

TPL_DIR = Path(__file__).resolve().parent.parent / "templates"


def render(tpl: str, data: dict) -> str:
    def loop(m):
        return "".join(render(m.group(2), {**data, **item}) for item in data.get(m.group(1), []))
    tpl = re.sub(r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}", loop, tpl, flags=re.S)
    return re.sub(r"\{\{(\w+)\}\}", lambda m: str(data[m.group(1)]) if m.group(1) in data else m.group(0), tpl)


if __name__ == "__main__":
    src = Path(sys.argv[1])
    step = src.parent.name
    default = "oto-crosssell" if step == "upsell-2" else "oto-lastchance" if step.startswith("downsell") else "oto-classic"
    name = sys.argv[sys.argv.index("--template") + 1] if "--template" in sys.argv else default
    data = json.loads(src.read_text())
    out = render((TPL_DIR / f"{name}.html").read_text(), data)
    dst = src.parent / "index.html"
    dst.write_text(out)
    left = sorted(set(re.findall(r"\{\{[^}]+\}\}", out)))
    print(f"{dst} ({len(out)} bytes)" + (f" | UNFILLED: {', '.join(left)}" if left else ""))
    sys.exit(1 if left else 0)
