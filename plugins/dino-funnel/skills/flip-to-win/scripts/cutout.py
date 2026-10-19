"""White background -> transparent PNG for flip-to-win prize/card images.

Usage: python cutout.py <in> <out.png> [--seed x,y ...] [--max 400]
Flood-fills from the border, plus each --seed point for enclosed white holes
(e.g. inside a ribbon loop) that the border fill can't reach. A colour-key
("every near-white pixel") is not used on purpose: it punches holes in white
highlights inside the product.
Run with python3 (needs Pillow).
"""
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter


def cutout(src, dst, seeds=(), max_side=400, thresh=14):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    key = im.copy()
    border = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]
    for xy in border + list(seeds):
        ImageDraw.floodfill(key, xy, (255, 0, 255), thresh=thresh)
    r, g, b = key.split()
    bg = ImageChops.multiply(r.point(lambda v: 255 if v == 255 else 0),
                             ImageChops.multiply(g.point(lambda v: 255 if v == 0 else 0), b.point(lambda v: 255 if v == 255 else 0)))
    alpha = ImageChops.invert(bg).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    out = im.copy()
    out.putalpha(alpha)
    out = out.crop(alpha.getbbox())
    out.thumbnail((max_side, max_side))
    out.save(dst)
    return out.size


if __name__ == "__main__":
    a = sys.argv[1:]
    seeds, mx = [], 400
    if "--seed" in a:
        i = a.index("--seed") + 1
        while i < len(a) and not a[i].startswith("--"):
            seeds.append(tuple(int(v) for v in a[i].split(",")))
            i += 1
    if "--max" in a:
        mx = int(a[a.index("--max") + 1])
    print(cutout(a[0], a[1], seeds, mx))
