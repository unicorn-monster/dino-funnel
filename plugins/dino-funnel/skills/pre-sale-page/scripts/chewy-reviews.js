// Chewy review harvest (no login needed). Tested 2026-10-22 on 2277694: 401 reviews in ~2 min.
// Open https://www.chewy.com/<slug>/product-reviews/<id> in a background tab, then run with
// chrome-devtools `evaluate_script`. The ?pageNumber= param is ignored (reviews render client-side),
// so step 1 clicks "Show More Reviews" until it disappears.

// ---- 1. load every review into the page -> {n, more}. Re-run if more === true (150 s cap per call).
async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const n = () => document.querySelectorAll('[class*="styles_review__"]').length;
  let stale = 0; const t0 = Date.now();
  while (stale < 4 && Date.now() - t0 < 150000) {
    const b = [...document.querySelectorAll('button')].find(e => /Show More Reviews/i.test(e.innerText));
    if (!b) { stale++; await sleep(1000); continue; }
    const before = n(); b.scrollIntoView(); b.click(); await sleep(1800);
    stale = n() === before ? stale + 1 : 0;
  }
  return { n: n(), more: !![...document.querySelectorAll('button')].find(e => /Show More Reviews/i.test(e.innerText)) };
}

// ---- 2. dump: pass filePath=<research>/chewy-<id>.json. Rows go straight into merge_reviews.py.
// Rating summary for research.md: the page header ("4.2 Rated ... 871 Ratings", star split, "401 Customer Reviews").
() => [...document.querySelectorAll('[class*="styles_review__"]')].map((r, k) => {
  const t = r.innerText.trim();
  const m = t.match(/^Rated (\d) out of 5 stars\s*By (.*?) on (\w{3} \d{1,2}, \d{4})\s*\n+([^\n]*)\n([\s\S]*?)(\n\d+\s*\nLikes|\nReport|$)/);
  return { id: 'chewy-' + (k + 1), stars: m ? +m[1] : null, name: m ? m[2] : '', date: m ? m[3] : '', title: m ? m[4].trim() : '',
    body: m ? m[5].trim() : t, helpful: (t.match(/\n(\d+)\s*\nLikes/) || [])[1] || '0',
    images: [...new Set([...r.querySelectorAll('img')].map(i => i.src).filter(s => /bazaarvoice|photos-us/.test(s)))] };
})
