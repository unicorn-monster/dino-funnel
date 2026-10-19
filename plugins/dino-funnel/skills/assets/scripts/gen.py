"""Generate ad images with Kie GPT Image 2.5 Flare (Khang 2026-10-09; was GPT Image 2). Used for the 1:1 FB ad images and the 1200x628 Discover images.

Usage: python gen.py <prompts.md> [--only 1,3] [--dry]
Reads refs.json (same folder as prompts.md): {"1": [url, ...], ...}.
Writes NN.png next to prompts.md; an existing NN.png is kept as NN-vK.png.
Run with python3 (needs requests + Pillow) from the working folder root (key: KIE_API_KEY in .env).
"""
import json, re, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

MODEL = "gpt-image-2-5-flare-image-to-image"
sys.path.insert(0, str(Path(__file__).resolve().parent))


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    md = Path(args[0]).resolve()
    only = None
    if "--only" in sys.argv:
        only = {int(x) for x in sys.argv[sys.argv.index("--only") + 1].split(",")}
    prompts = [re.sub(r"^\d+\. ", "", p.strip()) for p in md.read_text(newline="").split("\r\n\r\n") if p.strip()]
    refs = json.loads((md.parent / "refs.json").read_text())
    jobs = [i for i in range(1, len(prompts) + 1) if only is None or i in only]
    assert all(str(i) in refs for i in jobs), "refs.json needs an entry per prompt"
    if "--dry" in sys.argv:
        for i in jobs:
            print(i, len(prompts[i - 1].split()), "words", refs[str(i)])
        return
    import kie as k
    key = k.api_key()

    def go(i):
        out = md.parent / f"{i:02d}.png"
        if out.exists():
            n = 1
            while (md.parent / f"{i:02d}-v{n}.png").exists():
                n += 1
            out.rename(md.parent / f"{i:02d}-v{n}.png")
        try:
            r = k.run_job(key, MODEL,
                          {"prompt": prompts[i - 1], "input_urls": refs[str(i)], "aspect_ratio": "auto", "resolution": "1K"},
                          out)
            from PIL import Image  # upload.py squashes to 1200x628, so the ratio must already be ~1.91
            w, h = Image.open(out).size
            return i, "ok", r["credits"], out.name, f"{w}x{h}", f"ratio {w / h:.2f}"
        except Exception as e:
            return i, "ERR", str(e)[:300], ""

    with ThreadPoolExecutor(5) as ex:
        for r in ex.map(go, jobs):
            print(*r)


if __name__ == "__main__":
    main()
