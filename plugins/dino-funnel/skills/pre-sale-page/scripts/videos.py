#!/usr/bin/env python3
"""Download + watch every review video and listing video of the product (and its twins).

  python3 videos.py <output/<sp>/1-pre-sale-page/research> [--no-whisper] [--model base|small]

Reads   research/reviews.json                  (the `videos` m3u8 URLs kept by amazon-reviews.js / merge_reviews.py)
        research/videos/listing-videos.json    (optional, from amazon-listing-videos.js)
Writes  research/videos/<review id>_<N>star_<ASIN>.mp4 and L<NN>_<ASIN>.mp4   (best rendition, -c copy, skips existing)
        research/videos/frames/<name>.jpg      (8 frames across the clip, one strip)
        research/videos/strips-<k>.jpg         (8 strips per sheet: listing videos first, then 5* -> 1*)
        research/videos/tx/<name>.txt          (transcript: Amazon's closed captions .vtt when the listing has one,
                                                else whisper "base" on the audio)
        research/videos/index.tsv              (name, source, stars, seconds, url)
Then LOOK at every strips-*.jpg, read every tx/*.txt and write research/videos.md (see SKILL.md step 2).
Needs ffmpeg + ffprobe; whisper (pip install openai-whisper) for clips without captions.
Whisper runs on CPU here (~1 min per min of audio with "small", 2026-10-26: 50 min of video took >30 min),
so "base" is the default; review clips are short and plain speech.
"""
import glob, json, os, re, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

research = sys.argv[1]
use_whisper = '--no-whisper' not in sys.argv and shutil.which('whisper')
model = sys.argv[sys.argv.index('--model') + 1] if '--model' in sys.argv else 'base'
vdir = os.path.join(research, 'videos')
for d in ('frames', 'audio', 'tx'):
    os.makedirs(os.path.join(vdir, d), exist_ok=True)


def load(path):
    raw = open(path).read()
    i = min(k for k in (raw.find('['), raw.find('{')) if k >= 0)
    return json.loads(raw[i:max(raw.rfind(']'), raw.rfind('}')) + 1])


jobs = []  # (name, source, stars, url)
vtts = {}  # name -> closed-captions url
for r in load(os.path.join(research, 'reviews.json')):
    for k, u in enumerate(r.get('videos') or []):
        src = (r.get('source') or '').split('-')[-1]
        jobs.append((f"{r['id'].split(':')[-1]}_{int(r.get('stars') or 0)}star_{src}" + (f'_{k}' if k else ''), src, int(r.get('stars') or 0), u))
lv = os.path.join(vdir, 'listing-videos.json')
if os.path.exists(lv):
    have = {m for j in jobs for m in re.findall(r'prod/([\w-]+)/', j[3])}
    n = 0
    for v in load(lv):
        uid = (re.findall(r'prod/([\w-]+)/', v['url']) or [''])[0]
        if uid in have:
            continue
        have.add(uid)
        url = re.sub(r'/default\.jobtemplate\.mp4$', '/default.jobtemplate.hls.m3u8', v['url'])  # the .mp4 often 404s
        jobs.append((f"L{n:02d}_{v['asin']}", v['asin'] + ' listing: ' + (v.get('title') or ''), 9, url))
        if v.get('vtt'):
            vtts[f"L{n:02d}_{v['asin']}"] = v['vtt']
        n += 1


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def fetch(job):
    name, _, _, url = job
    mp4 = os.path.join(vdir, name + '.mp4')
    if not os.path.exists(mp4) or os.path.getsize(mp4) < 1000:
        r = run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-i', url, '-c', 'copy', '-bsf:a', 'aac_adtstoasc', mp4])
        if not os.path.exists(mp4) or os.path.getsize(mp4) < 1000:
            run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-i', url, '-c', 'copy', mp4])
    if not os.path.exists(mp4) or os.path.getsize(mp4) < 1000:
        return name, None
    dur = float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4]).stdout.strip() or 0)
    run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-i', mp4, '-vf', f'fps=8/{max(dur, 1)},scale=-2:260,tile=8x1',
         '-frames:v', '1', os.path.join(vdir, 'frames', name + '.jpg')])
    run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-i', mp4, '-vn', '-ac', '1', '-ar', '16000', os.path.join(vdir, 'audio', name + '.wav')])
    return name, dur


with ThreadPoolExecutor(6) as ex:
    durs = dict(ex.map(fetch, jobs))
with open(os.path.join(vdir, 'index.tsv'), 'w') as f:
    f.write('name\tsource\tstars\tseconds\turl\n')
    for name, src, stars, url in jobs:
        f.write(f"{name}\t{src}\t{stars if stars != 9 else ''}\t{round(durs.get(name) or 0)}\t{url}\n")
print(f'{sum(1 for d in durs.values() if d)}/{len(jobs)} videos, {round(sum(d or 0 for d in durs.values()) / 60)} min')

try:
    from PIL import Image, ImageDraw
    order = sorted(glob.glob(os.path.join(vdir, 'frames', '*.jpg')),
                   key=lambda p: (0 if os.path.basename(p).startswith('L') else 1, -int((re.findall(r'_(\d)star', p) or ['9'])[0]), p))
    W = 1500
    for k in range(0, len(order), 8):
        ims = [(p, Image.open(p).convert('RGB')) for p in order[k:k + 8]]
        ims = [(p, i.resize((W, max(1, int(i.height * W / i.width))))) for p, i in ims]
        sheet = Image.new('RGB', (W, sum(i.height + 18 for _, i in ims)), 'white')
        d, y = ImageDraw.Draw(sheet), 0
        for p, i in ims:
            d.text((4, y + 2), os.path.basename(p)[:-4], fill='red'); sheet.paste(i, (0, y + 16)); y += i.height + 18
        sheet.save(os.path.join(vdir, f'strips-{k // 8}.jpg'), quality=85)
except ImportError:
    print('Pillow missing: no strip sheets')

import urllib.request
for name, url in vtts.items():
    txt = os.path.join(vdir, 'tx', name + '.txt')
    if os.path.exists(txt):
        continue
    try:
        raw = urllib.request.urlopen(url, timeout=30).read().decode('utf-8', 'ignore')
    except Exception as e:
        print('vtt failed', name, e); continue
    lines = [l.strip() for l in raw.splitlines() if l.strip() and l.strip() != 'WEBVTT' and '-->' not in l and not l.strip().isdigit()]
    open(txt, 'w').write(' '.join(dict.fromkeys(lines)) + '\n')
print(f'{len(vtts)} transcripts from closed captions')

if use_whisper:
    todo = [w for w in glob.glob(os.path.join(vdir, 'audio', '*.wav'))
            if not os.path.exists(os.path.join(vdir, 'tx', os.path.basename(w)[:-4] + '.txt'))]
    if todo:
        print(f'whisper {model} on {len(todo)} clips without captions...')
        run(['whisper', *todo, '--model', model, '--language', 'en', '--output_format', 'txt',
             '--output_dir', os.path.join(vdir, 'tx'), '--fp16', 'False'])
elif '--no-whisper' not in sys.argv:
    print('whisper not installed: pip install openai-whisper (transcripts skipped)')
