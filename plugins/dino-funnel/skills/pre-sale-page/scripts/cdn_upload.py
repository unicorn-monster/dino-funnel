"""Upload every /<slug>/assets/* file that <page_dir>/index.html references to Dino Shopify Files and
record its CDN URL in <page_dir>/cdn-map.json ({rel: {sha1, id, url}}); the page build swaps the paths.
Only new or changed files (by sha1) are uploaded. The Shopify flow lives in ../../assets/scripts/cdn.py.
Usage: python3 cdn_upload.py <page_dir> <slug> <file-prefix, e.g. bfr2>"""
import hashlib, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "assets/scripts"))
import cdn

OUT, SLUG, FPRE = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
PREFIX = f"/{SLUG}/assets/"
MAP = OUT / "cdn-map.json"

cmap = json.loads(MAP.read_text()) if MAP.exists() else {}
html = (OUT / "index.html").read_text()
files = sorted(set(re.findall(re.escape(PREFIX) + r'([^"\')\s]+)', html)))
todo = []
for rel in files:
    f = OUT / "assets" / rel
    sha = hashlib.sha1(f.read_bytes()).hexdigest()
    if cmap.get(rel, {}).get("sha1") != sha:
        todo.append((rel, f, sha))
print(f"{len(files)} referenced, {len(todo)} to upload")

ids = cdn.create([(f, f"{FPRE}-" + rel.replace("/", "-")) for rel, f, _ in todo])
for (rel, f, sha), i in zip(todo, ids):
    cmap[rel] = {"sha1": sha, "id": i, "url": None}
MAP.write_text(json.dumps(cmap, indent=1))

pending = {v["id"]: r for r, v in cmap.items() if not v.get("url")}


def save(urls):
    for i, url in urls.items():
        cmap[pending[i]]["url"] = url
    MAP.write_text(json.dumps(cmap, indent=1))


save(cdn.wait_urls(list(pending), on_progress=save))
print("not ready:", [r for r, v in cmap.items() if not v.get("url")] or "none")
