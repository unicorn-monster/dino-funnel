"""Fill the two checkout templates from one content.json.

usage: python3 fill.py output/<product>/3-checkout/content.json
writes fb-comments.html + reviews-trustpilot.html next to content.json (pure ASCII).

content.json:
{"comments": [{"name", "text", "avatar", "photo"|null, "photo_alt"?}] x3,
 "reviews":  [{"name", "text", "photo", "alt"?}] x6}
"""
import html, json, re, sys
from pathlib import Path

TPL = Path(__file__).resolve().parent.parent / 'templates'
WORDS = {'comments': (25, 55), 'reviews': (35, 70)}


def esc(s):
    return html.escape(s, quote=False).replace("'", '&rsquo;').replace('’', '&rsquo;')


def ascii_only(t):
    return t.encode('ascii', 'xmlcharrefreplace').decode()


def check(c):
    bad = []
    for key, (lo, hi) in WORDS.items():
        for x in c[key]:
            n = len(x['text'].split())
            if not lo <= n <= hi:
                bad.append(f"{key}: {x['name']} = {n} words (want {lo}-{hi})")
            if '—' in x['text']:
                bad.append(f"{key}: {x['name']} has an em dash")
    return bad


def fill_comments(c):
    t = (TPL / 'fb-comments.html').read_text()
    items = re.findall(r'<div class="fbc-item">.*?<div class="fbc-meta">', t, re.S)
    assert len(items) == len(c) == 3, 'template has 3 comments, content needs 3'
    for old, x in zip(items, c):
        new = re.sub(r'(<img class="fbc-av" src=")[^"]*(" alt=")[^"]*', rf'\g<1>{x["avatar"]}\g<2>{esc(x["name"])}', old)
        new = re.sub(r'(<span class="fbc-name">)[^<]*(</span><svg class="fbc-badge".*?</svg>).*?\n',
                     lambda m: f'{m[1]}{esc(x["name"])}{m[2]}{esc(x["text"])}\n', new, flags=re.S)
        if x.get('photo'):
            if 'fbc-photo-wrap' not in new:
                raise SystemExit(f'{x["name"]}: only comment 1 has a photo slot in the template')
            new = re.sub(r'(<img class="fbc-photo" src=")[^"]*(" alt=")[^"]*', rf'\g<1>{x["photo"]}\g<2>{esc(x.get("photo_alt", ""))}', new)
        elif 'fbc-photo-wrap' in new:
            raise SystemExit(f'{x["name"]}: comment 1 needs a photo')
        t = t.replace(old, new, 1)
    return t


def fill_reviews(r):
    t = (TPL / 'reviews-trustpilot.html').read_text()
    cards = re.findall(r'<div class="tprv-card">.*?</p>', t, re.S)
    assert len(cards) == len(r) == 6, 'template has 6 cards, content needs 6'
    for old, x in zip(cards, r):
        new = re.sub(r'(<img class="tprv-photo" src=")[^"]*(" alt=")[^"]*', rf'\g<1>{x["photo"]}\g<2>{esc(x.get("alt", "Customer photo"))}', old)
        new = re.sub(r'(<div class="tprv-name"><img [^>]+>)[^<]*', lambda m: m[1] + esc(x['name']), new)
        new = re.sub(r'(<p class="tprv-text">).*?</p>', lambda m: f'{m[1]}{esc(x["text"])}</p>', new, flags=re.S)
        t = t.replace(old, new, 1)
    return t


if __name__ == '__main__':
    src = Path(sys.argv[1])
    c = json.loads(src.read_text())
    for line in check(c):
        print('WARN', line)
    (src.parent / 'fb-comments.html').write_text(ascii_only(fill_comments(c['comments'])))
    (src.parent / 'reviews-trustpilot.html').write_text(ascii_only(fill_reviews(c['reviews'])))
    print('wrote', src.parent / 'fb-comments.html', src.parent / 'reviews-trustpilot.html')
