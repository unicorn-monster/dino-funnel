"""Generate one product truth sheet (or any reference-driven image) on Kie and save it with its URL.
Usage: python3 sheet.py <out.png> <prompt.txt> <ref_url> [<ref_url> ...] [--model nano-banana-2] [--ratio 16:9]
Writes <out.png> and <out>.url.txt (the Kie result URL, reusable as a reference in later jobs).
Run with python3 (needs requests) from the working folder root (key: KIE_API_KEY in .env)."""
import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "assets/scripts"))
import kie

ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("prompt"); ap.add_argument("refs", nargs="+")
ap.add_argument("--model", default="gpt-image-2-5-flare-image-to-image")
ap.add_argument("--ratio", default="16:9")
a = ap.parse_args()

key = kie.api_key()
inp = {"prompt": Path(a.prompt).read_text(), "aspect_ratio": a.ratio, "resolution": "1K"}
if a.model.startswith("nano-banana"):  # NB2 takes image_input + output_format, no 8:9 etc. (use "auto")
    inp |= {"image_input": a.refs, "output_format": "png"}
else:
    inp["input_urls"] = a.refs
r = kie.run_job(key, a.model, inp, Path(a.out), timeout=300)
Path(a.out).with_suffix(".url.txt").write_text(r["result_url"])
print(r["credits"], r["result_url"])
