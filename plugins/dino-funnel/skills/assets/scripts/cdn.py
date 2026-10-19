"""Upload local files to Dino Shopify Files and print their CDN URLs (needs the `shopify` CLI, logged in).
Flow: stagedUploadsCreate -> POST -> fileCreate -> poll until READY.

Usage: python3 cdn.py <file> [<file> ...] [--prefix bundle-catbed]
Prints `<file> <cdn url>` per line; the Shopify file name is `<prefix>-<file name>` (or the bare name).
Also imported by pre-sale-page/scripts/cdn_upload.py.
"""
import json, subprocess, sys, tempfile, time
from pathlib import Path

STORE = "dinosaurized-army-store.myshopify.com"
KIND = {".webp": ("IMAGE", "image/webp"), ".png": ("IMAGE", "image/png"), ".jpg": ("IMAGE", "image/jpeg"),
        ".jpeg": ("IMAGE", "image/jpeg"), ".gif": ("IMAGE", "image/gif"), ".mp4": ("VIDEO", "video/mp4"),
        ".woff2": ("FILE", "font/woff2")}


def gql(query, variables=None):
    with tempfile.TemporaryDirectory() as d:
        q, v, o = Path(d, "q.graphql"), Path(d, "v.json"), Path(d, "o.json")
        q.write_text(query); v.write_text(json.dumps(variables or {}))
        subprocess.run(["shopify", "store", "execute", "--store", STORE, "--query-file", str(q), "--variable-file", str(v),
                        "--allow-mutations", "--no-color", "--output-file", str(o)], check=True, capture_output=True, cwd=d)
        return json.loads(o.read_text())


def create(files):
    """files = [(Path, shopify file name)] -> Shopify file ids, same order. Batches of 20."""
    ids = []
    for i in range(0, len(files), 20):
        batch = files[i:i + 20]
        inp = [{"resource": KIND[f.suffix.lower()][0], "filename": name, "mimeType": KIND[f.suffix.lower()][1],
                "httpMethod": "POST", "fileSize": str(f.stat().st_size)} for f, name in batch]
        res = gql("""mutation($input:[StagedUploadInput!]!){stagedUploadsCreate(input:$input){
            stagedTargets{url resourceUrl parameters{name value}} userErrors{field message}}}""", {"input": inp})["stagedUploadsCreate"]
        assert not res["userErrors"], res["userErrors"]
        created = []
        for (f, _), t in zip(batch, res["stagedTargets"]):
            cmd = ["curl", "-sf", "-X", "POST", t["url"]]
            for p in t["parameters"]:
                cmd += ["-F", f"{p['name']}={p['value']}"]
            subprocess.run(cmd + ["-F", f"file=@{f}"], check=True, capture_output=True)
            created.append({"originalSource": t["resourceUrl"], "contentType": KIND[f.suffix.lower()][0]})
        fc = gql("""mutation($files:[FileCreateInput!]!){fileCreate(files:$files){files{id} userErrors{field message}}}""",
                 {"files": created})["fileCreate"]
        assert not fc["userErrors"], fc["userErrors"]
        ids += [n["id"] for n in fc["files"]]
    return ids


def wait_urls(ids, on_progress=None):
    """Poll until each file id is READY -> {id: url}; ids still pending after ~5 min are left out."""
    urls, pending = {}, list(ids)
    for _ in range(60):
        if not pending:
            break
        time.sleep(5)
        nodes = gql("""query($ids:[ID!]!){nodes(ids:$ids){id
            ... on MediaImage{fileStatus image{url}}
            ... on Video{fileStatus sources{url mimeType height}}
            ... on GenericFile{fileStatus url}}}""", {"ids": pending})["nodes"]
        for n in nodes:
            assert n.get("fileStatus") != "FAILED", f"{n['id']}: upload failed"
            url = (n.get("image") or {}).get("url") or n.get("url")
            mp4 = [s for s in n.get("sources") or [] if s["mimeType"] == "video/mp4"]
            url = url or (min([s for s in mp4 if s["height"] >= 480] or mp4, key=lambda s: s["height"])["url"] if mp4 else None)  # 480p is plenty for page slots
            if n.get("fileStatus") == "READY" and url:
                urls[n["id"]] = url
        pending = [i for i in pending if i not in urls]
        if on_progress:
            on_progress(urls)
    return urls


if __name__ == "__main__":
    args = sys.argv[1:]
    prefix = ""
    if "--prefix" in args:
        i = args.index("--prefix")
        prefix = args[i + 1] + "-"
        del args[i:i + 2]
    files = [Path(a) for a in args]
    assert files and all(f.is_file() and f.suffix.lower() in KIND for f in files), f"need files with one of {sorted(KIND)}"
    ids = create([(f, prefix + f.name) for f in files])
    urls = wait_urls(ids)
    for f, i in zip(files, ids):
        print(f, urls.get(i, "NOT READY"))
