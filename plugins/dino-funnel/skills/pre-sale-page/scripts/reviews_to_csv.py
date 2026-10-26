#!/usr/bin/env python3
"""reviews.json (dump of amazon-reviews.js step 3) -> CSV + review photos + theme counts.

  python3 reviews_to_csv.py <reviews.json> <output/<sp>/1-pre-sale-page/research> <ASIN> [themes.json] [--all-stars]

Writes  <sp>/amazon-reviews-<ASIN>.csv            (sorted by helpful votes)
        <sp>/amazon-review-images/<N>star_<id>_<k>.jpg   (4-5* photos only; 1-3* photos and all videos stay as URLs
                                                          in the CSV, --all-stars downloads every photo)
Prints  per theme: total / positive (4-5*) / negative (1-2*) mentions.

themes.json = {"theme label": "regex", ...}, written per product, e.g.
  {"easy to clean": "clean|apart|wash", "no leak": "leak|drip|spill", "ants / moat": "\\\\bants?\\\\b|moat"}
"""
import csv, json, os, re, subprocess, sys

args = [a for a in sys.argv[1:] if not a.startswith('--')]
src, out, asin = args[0], args[1], args[2]
# 1-3* photos were never used (slots reject defect shots; text + videos show the failures better) and were
# 74% of the download on a complaint-heavy gallery (2026-10-26): skip them unless asked
min_stars = 1 if '--all-stars' in sys.argv else 4
raw = open(src).read()
rows = [r for r in json.loads(raw[raw.find('['):raw.rfind(']') + 1]) if 'error' not in r]

for r in rows:
    m = re.match(r'Reviewed in (?:the )?(.*?) on (.*)', r['date'])
    r['country'], r['date'] = (m.group(1), m.group(2)) if m else ('', r['date'])
    r['has_video'] = bool(r['videos']) or 'VIDEO' in (r.get('gallery') or [])
helpful = lambda r: int(re.sub(r'\D', '', r['helpful'].replace('One', '1')) or 0)
rows.sort(key=lambda r: (-helpful(r), -r['stars']))

cols = ['id', 'stars', 'title', 'body', 'name', 'date', 'country', 'variant', 'verified', 'helpful', 'has_video', 'images', 'videos']
with open(os.path.join(out, f'amazon-reviews-{asin}.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
    w.writeheader()
    for r in rows:
        w.writerow({**r, 'images': ' '.join(r['images']), 'videos': ' '.join(r['videos'])})

img_dir = os.path.join(out, 'amazon-review-images')
os.makedirs(img_dir, exist_ok=True)
jobs = [(u, f"{int(r['stars'])}star_{r['id']}_{k}.jpg") for r in rows if r['stars'] >= min_stars for k, u in enumerate(r['images'], 1)]
for u, name in jobs:  # ponytail: sequential curl, ~200 photos in a few minutes; parallelize if it gets slow
    dest = os.path.join(img_dir, name)
    if not os.path.exists(dest):
        subprocess.run(['curl', '-sSf', '-A', 'Mozilla/5.0', '-o', dest, u], check=False)
print(f'{len(rows)} reviews, {len(jobs)} photos ({min_stars}-5*) -> {out}')

if len(args) > 3:
    themes = json.load(open(args[3]))
    print(f"{'total':>5} {'pos':>4} {'neg':>4}  theme")
    for label, rx in sorted(themes.items(), key=lambda kv: -sum(bool(re.search(kv[1], (r['title'] + ' ' + r['body']).lower())) for r in rows)):
        hit = [r for r in rows if re.search(rx, (r['title'] + ' ' + r['body']).lower())]
        print(f"{len(hit):5d} {sum(r['stars'] >= 4 for r in hit):4d} {sum(r['stars'] <= 2 for r in hit):4d}  {label}")
