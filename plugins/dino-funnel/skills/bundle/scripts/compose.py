"""Compose a checkout bundle image: N copies of one transparent cutout (+ optional gift), on white.

Usage: python3 compose.py <cutout.png> <out.jpg|png> --layout diag2 [--gift gift.png] [--size 500] [--margin 0.04]
       python3 compose.py --selftest
Layouts (positions in units of the cutout's own width/height, drawn back to front):
  one, row2, row3 (side by side: tall products), tri3 (2 back + 1 front),
  diag2 (back top-left, front bottom-right: flat/wide products), diamond4, stagger6 (2 offset columns),
  or a custom list "x,y;x,y;...".
--gift: products fill the left part, a red + in the gap, the gift on the right (the BOGO + gift look).
Cut the packshot first with flip-to-win/scripts/cutout.py <in> <cut.png> --max 1000.
"""
import sys
from PIL import Image, ImageDraw

LAYOUTS = {
    "one": [(0, 0)],
    "row2": [(0, 0), (1.02, 0)],
    "row3": [(0, 0), (1.02, 0), (2.04, 0)],
    "tri3": [(0, 0), (0.95, 0), (0.475, 0.15)],
    "diag2": [(0, 0), (0.5, 0.55)],
    "diamond4": [(0.55, 0), (0, 0.5), (1.1, 0.5), (0.55, 1.0)],
    "stagger6": [(i % 2 * 0.55, i * 0.9) for i in range(6)],
}
RED = (255, 0, 0)  # same + as the hummingbird bundles


def group(item, layout):
    """Paste copies of item at layout positions on a transparent canvas, cropped to content."""
    w, h = item.size
    pts = LAYOUTS.get(layout) or [tuple(float(v) for v in p.split(",")) for p in layout.split(";")]
    x0, y0 = min(p[0] for p in pts), min(p[1] for p in pts)
    W = int((max(p[0] for p in pts) - x0 + 1) * w) + 2
    H = int((max(p[1] for p in pts) - y0 + 1) * h) + 2
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for x, y in pts:
        canvas.alpha_composite(item, (int((x - x0) * w), int((y - y0) * h)))
    return canvas.crop(canvas.getbbox())


def fit(im, box_w, box_h):
    s = min(box_w / im.width, box_h / im.height)
    return im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)


def compose(cutout, layout, gift=None, size=500, margin=0.04):
    item = Image.open(cutout).convert("RGBA")
    item = item.crop(item.getbbox())
    g = group(item, layout)
    out = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    m = round(size * margin)
    inner = size - 2 * m
    if not gift:
        g = fit(g, inner, inner)
        out.alpha_composite(g, ((size - g.width) // 2, (size - g.height) // 2))
    else:
        gi = Image.open(gift).convert("RGBA")
        gi = fit(gi.crop(gi.getbbox()), round(inner * 0.30), round(inner * 0.60))
        g = fit(g, round(inner * 0.60), inner)
        out.alpha_composite(g, (m, (size - g.height) // 2))
        out.alpha_composite(gi, (size - m - gi.width, (size - gi.height) // 2))
        cx = (m + g.width + size - m - gi.width) // 2  # middle of the gap
        arm, t = round(size * 0.045), round(size * 0.013)
        d = ImageDraw.Draw(out)
        d.rectangle([cx - arm, size // 2 - t, cx + arm, size // 2 + t], fill=RED)
        d.rectangle([cx - t, size // 2 - arm, cx + t, size // 2 + arm], fill=RED)
    return out.convert("RGB")


def selftest():
    import tempfile, os
    d = tempfile.mkdtemp()
    item = Image.new("RGBA", (300, 200), (0, 0, 0, 0))
    ImageDraw.Draw(item).ellipse([10, 10, 290, 190], fill=(40, 120, 200, 255))
    item.save(os.path.join(d, "cut.png"))
    for lay in [*LAYOUTS, "0,0;1,0.5"]:
        for gift in (None, os.path.join(d, "cut.png")):
            im = compose(os.path.join(d, "cut.png"), lay, gift)
            assert im.size == (500, 500), lay
            box = im.convert("L").point(lambda v: 255 if v < 245 else 0).getbbox()
            assert box and box[0] >= 19 and box[2] <= 481 and box[1] >= 19 and box[3] <= 481, (lay, gift, box)
            if gift:
                assert RED in [px for _, px in im.getcolors(1 << 20)], "missing red +"
    print("selftest ok")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest()
        sys.exit()
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    im = compose(a[0], opt("--layout", "one"), opt("--gift"), int(opt("--size", 500)), float(opt("--margin", 0.04)))
    out = a[1]
    if out.lower().endswith((".jpg", ".jpeg")):
        im.save(out, quality=85, optimize=True, progressive=True)
    else:
        im.save(out, optimize=True)
    print(out, im.size)
