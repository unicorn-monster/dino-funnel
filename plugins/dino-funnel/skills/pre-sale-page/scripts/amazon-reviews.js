// Amazon review harvest, run with chrome-devtools `evaluate_script` on the
// listing tab (amazon.com/dp/<ASIN>, LOGGED IN in the user's Chrome).
// Paste each function body as the `function` arg, in order. Tested 2026-10-04
// on B0DQ6PQSL8: 250 gallery tiles (Amazon's cap) -> 172 reviews, 0 errors.
//
// Why the gallery: /product-reviews/ and /portal/customer-reviews/ only ever
// show 8 reviews now, filterByStar/sortBy/pageNumber are ignored even logged in.
// The "Customer photos and videos > See all" grid lazy-loads up to 250 tiles,
// each tile carries data-reviewid, and /gp/customer-reviews/<id> serves the
// full review (text, full-size images, video m3u8).

// ---- 1. aspects: Amazon's own mention counts over ALL ratings ------------
// For competitors also click each chip: the panel then reads
// "N customers mention X, P positive, Q negative" (Q = their real complaint count).
// Competitor 1-3★ text: in step 2 keep only tiles whose innerHTML matches /a-star-small-[123]\b/.
// -> [["Quality","955"],["Ease of cleaning","326"],...]  (the "Select to learn more" chips)
() => {
  const out = [], seen = new Set();
  document.querySelectorAll('#reviewsMedley button').forEach(e => {
    const m = (e.innerText || '').trim().match(/^([A-Za-z][A-Za-z \-&']{1,40})\s*\(([\d,.]+K?)\)$/);
    if (m && !seen.has(m[1])) { seen.add(m[1]); out.push([m[1].trim(), m[2]]); }
  });
  return out;
}

// ---- 2. open the gallery grid and scroll it until no new tiles ------------
// -> {tiles, images, videos, reviews}. Leaves window.__rids for step 3.
async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  // the review block lazy-loads: scroll to it first or the gallery link does not exist yet
  document.querySelector('#reviewsMedley')?.scrollIntoView();
  await sleep(2500);
  document.querySelector('#cm_cr_carousel_mixed_section a.a-link-emphasis')?.click();
  await sleep(3000);
  // the header button switches the modal back to the grid (after a tile was clicked)
  document.querySelector('.a-popover-modal button[data-seemore="true"]')?.click();
  await sleep(2000);
  const grid = document.querySelector('.a-popover-modal [class*="media-popover-gallery-container-grid"]');
  const tiles = () => [...grid.querySelectorAll('button[data-mediatype][data-reviewid]')];
  let stale = 0;
  while (stale < 6) {
    const before = tiles().length;
    grid.scrollTop = grid.scrollHeight;
    await sleep(1500);
    stale = tiles().length === before ? stale + 1 : 0;
  }
  const t = tiles();
  window.__types = {};
  t.forEach(e => (window.__types[e.dataset.reviewid] ??= []).push(e.dataset.mediatype));
  window.__rids = Object.keys(window.__types);
  window.__out = [];
  return { tiles: t.length, images: t.filter(e => e.dataset.mediatype === 'IMAGE').length,
           videos: t.filter(e => e.dataset.mediatype === 'VIDEO').length, reviews: window.__rids.length };
}

// ---- 3. fetch full reviews, 60 per call (one call ~60s, stays under the tool timeout) ----
// Repeat until done === total. On the LAST call pass filePath=<scratchpad>/reviews.json
// and change the return to `window.__out` to dump everything.
async () => {
  const txt = (r, s) => { const e = r.querySelector(s); return e ? e.textContent.replace(/[ \t]+/g, ' ').trim() : ''; };
  const one = async id => {
    const d = new DOMParser().parseFromString(await (await fetch('/gp/customer-reviews/' + id)).text(), 'text/html');
    const r = d.querySelector('[data-hook="review"]');
    if (!r) return { id, error: 'no review' };
    const star = txt(r, '[data-hook="review-star-rating"],[data-hook="cmps-review-star-rating"]');
    let body = txt(r, '[data-hook="reviewText"],[data-hook="review-body"]');
    if (body.includes('Full content visible')) body = body.split('Full content visible, double tap to read brief content.').pop();
    body = body.replace(/^Brief content visible, double tap to read full content\./, '').replace(/Read more\s*(Read less)?\s*$/, '').trim();
    return { id, stars: parseFloat(star), title: txt(r, '[data-hook="reviewTitle"],[data-hook="review-title"]').replace(star, '').trim(),
      name: txt(r, '.a-profile-name'), date: txt(r, '[data-hook="review-date"]'), variant: txt(r, '[data-hook="format-strip"]'),
      verified: !!r.querySelector('[data-hook="avp-badge"]'), helpful: txt(r, '[data-hook="helpful-vote-statement"]'), body,
      images: [...new Set([...r.querySelectorAll('[data-hook="review-image-tile"]')]
        .map(i => (i.src || i.querySelector('img')?.src || '').replace(/\._[^.]+_\./, '.')).filter(s => /images\/I\//.test(s)))],
      videos: [...new Set(r.outerHTML.match(/https:[^"'\s&]+?\.m3u8/g) || [])], gallery: window.__types[id] };
  };
  const end = Math.min(window.__out.length + 60, window.__rids.length);
  for (let i = window.__out.length; i < end; i++) {
    try { window.__out.push(await one(window.__rids[i])); } catch (e) { window.__out.push({ id: window.__rids[i], error: String(e) }); }
    await new Promise(r => setTimeout(r, 400 + Math.random() * 400));
  }
  return { done: window.__out.length, total: window.__rids.length, errors: window.__out.filter(r => r.error).length };
}
