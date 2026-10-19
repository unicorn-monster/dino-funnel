#!/usr/bin/env python3
"""Build output/<product>/funnel/: a flat, numbered copy of each funnel step, the way a user walks it.

  python3 .claude/skills/funnel/scripts/funnel_view.py            # every product in output/ (run from the working folder root)
  python3 .claude/skills/funnel/scripts/funnel_view.py cat-bed    # one product

funnel/ is a derived copy (originals stay where they are) and is rebuilt from scratch on every run:
  1-pre-sale.html  2-flip-to-win.html  3-sale-page.html  4-checkout-*.html
  5-bundle/  (bundle images)           6-ads/  (ad copy .md + ad images, prompts and old -vN versions skipped)
"""
import re, shutil, sys
from pathlib import Path

OUT = Path.cwd() / "output"
IMG = {".png", ".jpg", ".jpeg", ".webp"}


def build(p: Path) -> list[str]:
    dst = p / "funnel"
    shutil.rmtree(dst, ignore_errors=True)
    plan = []  # (source, name inside funnel/)
    pre = sorted(d for d in p.glob("1-pre-sale*") if (d / "index.html").exists())
    for d in pre:
        suffix = "" if len(pre) == 1 else "-" + d.name.removeprefix("1-pre-sale").strip("-")
        plan.append((d / "index.html", f"1-pre-sale{suffix}.html"))
    if (p / "flip-to-win/index.html").exists():
        plan.append((p / "flip-to-win/index.html", "2-flip-to-win.html"))
    if (p / "2-sale-page/index.html").exists():
        plan.append((p / "2-sale-page/index.html", "3-sale-page.html"))
    for f in sorted((p / "3-checkout").glob("*.html")):
        plan.append((f, f"4-checkout-{f.name}"))
    for f in sorted((p / "4-bundle").glob("*")):
        if f.suffix.lower() in IMG:
            plan.append((f, f"5-bundle/{f.name}"))
    for f in sorted(p.rglob("*")):
        rel = f.relative_to(p)
        if rel.parts[0] == "funnel" or not f.is_file() or not re.match(r"5-|6-ads", rel.parts[0]):
            continue
        if f.suffix == ".md" and re.search(r"fb-ads|demandgen", f.name):
            plan.append((f, f"6-ads/{f.name.removeprefix('5-')}"))
        elif f.suffix.lower() in IMG and len(rel.parts) > 1 and not re.search(r"-v\d+\.", f.name):
            plan.append((f, "6-ads/" + "-".join(x.removeprefix("5-") for x in rel.parts)))
    for src, name in plan:
        (dst / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst / name)
    return [name for _, name in plan]


if __name__ == "__main__":
    names = sys.argv[1:] or sorted(d.name for d in OUT.iterdir() if d.is_dir())
    for n in names:
        got = build(OUT / n)
        steps = [x for x in got if "/" not in x]
        print(f"{n}: {len(got)} files | {', '.join(steps) or '-'}"
              f" | bundle {sum(x.startswith('5-bundle/') for x in got)} | ads {sum(x.startswith('6-ads/') for x in got)}")
