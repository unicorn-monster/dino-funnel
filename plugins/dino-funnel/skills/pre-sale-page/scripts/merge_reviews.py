#!/usr/bin/env python3
"""Merge review dumps from several sources (same product, different sellers/sites) into one
reviews.json in the shape reviews_to_csv.py reads.

  python3 merge_reviews.py <out reviews.json> <source>=<dump.json> [<source>=<dump.json> ...]

<source> is a short label kept on every row (e.g. amz-B0DSBBLDJ5, chewy-2277694). Accepted dumps:
  - amazon-reviews.js step 3 (logged in): list of {id, stars, title, body, images, videos, ...}
  - amazon-gallery.js (logged out): list of {id, raw, images, thumbs, video}, `raw` = the gallery
    modal's review panel text ("\\tName\\nN Stars\\nVerified Purchase\\nTitle\\nBody")
  - chewy-reviews.js: list of {id, stars, name, date, title, body, helpful, images}
  - amazon-facts.js: one object with topReviews (" | "-joined text of the listing's top reviews)
Duplicates (same title + first 80 chars of body) are dropped, first source wins.
"""
import json, re, sys


def load(path):
    raw = open(path).read()
    i = min([k for k in (raw.find('['), raw.find('{')) if k >= 0])
    j = max(raw.rfind(']'), raw.rfind('}'))
    return json.loads(raw[i:j + 1])


def from_gallery(r):
    lines = [l.strip() for l in r['raw'].replace('\t', '').split('\n') if l.strip()]
    lines = [l for l in lines if not re.fullmatch(r'-?\d+:\d\d', l)]  # video timer
    k = next((n for n, l in enumerate(lines) if re.fullmatch(r'\d Stars?', l)), None)
    if k is None:
        return None
    rest = lines[k + 1:]
    verified = bool(rest) and rest[0] == 'Verified Purchase'
    if verified:
        rest = rest[1:]
    return {'id': r['id'], 'stars': float(lines[k][0]), 'name': lines[k - 1] if k else '', 'title': rest[0] if rest else '',
            'body': ' '.join(rest[1:]), 'verified': verified, 'images': r.get('images', []),
            'videos': [], 'gallery': ['VIDEO'] if r.get('video') else ['IMAGE'], 'video_thumbs': r.get('thumbs', [])}


def from_top(t, n):
    parts = [p.strip() for p in t.split(' | ')]
    s = next((i for i, p in enumerate(parts) if re.match(r'\d out of 5 stars', p)), None)
    if s is None:
        return None
    rest = [p for p in parts[s + 1:] if p not in ('Verified Purchase', 'Helpful', 'Report', 'Read more') and not re.match(r'(Reviewed in|Color:|Size:|Style:|\w+ (people|person) found)', p)]
    return {'id': f'top{n}', 'stars': float(parts[s][0]), 'name': parts[s - 1] if s else '', 'title': rest[0] if rest else '',
            'body': ' '.join(rest[1:]), 'images': [], 'videos': []}


out, seen = [], set()
for arg in sys.argv[2:]:
    src, path = arg.split('=', 1)
    data = load(path)
    rows = []
    if isinstance(data, dict):  # facts dump
        rows = [from_top(t, n) for n, t in enumerate(data.get('topReviews', []))]
    else:
        for r in data:
            if 'error' in r:
                continue
            rows.append(from_gallery(r) if 'raw' in r and 'body' not in r else r)
    added = 0
    for r in filter(None, rows):
        if not r.get('stars'):
            continue
        key = (r.get('title', '').lower()[:60], re.sub(r'\W', '', r.get('body', '').lower())[:80])
        if key in seen:
            continue
        seen.add(key)
        r.setdefault('date', ''); r.setdefault('variant', ''); r.setdefault('verified', False)
        r.setdefault('helpful', str(r.get('helpful', '0'))); r.setdefault('videos', []); r.setdefault('name', '')
        r['date'] = r['date'] or ''
        r['id'] = f"{src}:{r['id']}"
        r['source'] = src
        out.append(r)
        added += 1
    print(f'{src}: {added} reviews')
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
print(f'{len(out)} total -> {sys.argv[1]}')
