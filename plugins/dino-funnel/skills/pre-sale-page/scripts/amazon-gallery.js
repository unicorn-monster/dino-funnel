// Amazon review gallery harvest WITHOUT login. Use this when /gp/customer-reviews/<id> redirects to
// Sign-In (amazon-reviews.js step 3 needs a logged-in Chrome). Opens "Customer photos and videos > See all",
// clicks each tile and reads the review panel. Resumable: each call reads 20 more tiles into window.__g;
// repeat until {done: true}, then dump: () => Object.values(window.__g) with filePath=<research>/gal-<ASIN>.json.
// Tested 2026-10-22: 210 tiles -> 136 reviews on B0DLRH694Y. Videos come back as video:true + thumbs only:
// for the files, see SKILL.md *Review videos*.
async () => {
  // Resumable: each call reads up to 20 more gallery tiles into window.__g. Call until done.
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const m = () => document.querySelector('.a-popover-modal');
  const grid = () => m()?.querySelector('[class*="media-popover-gallery-container-grid"]');
  const back = async () => { (m().querySelector('[class*=media-popover-see-all-container]') || m().querySelector('button[data-seemore="true"]'))?.click(); await sleep(1500); };
  const tiles = () => [...grid().querySelectorAll('button[data-mediatype][data-reviewid]')];
  window.__g ??= {}; window.__gk ??= 0;
  if (!m() || !m().offsetParent) {
    document.querySelector('#cm_cr_carousel_mixed_section a.a-link-emphasis')?.click() ||
      [...document.querySelectorAll('a,button,span')].find(e => (e.innerText || '').trim() === 'See all' && e.closest('[id*=customer-reviews], [id*=cm_cr], [data-hook]'))?.click();
    await sleep(3500);
  }
  if (!grid() || !grid().offsetParent) await back();
  const end = window.__gk + 20; const t0 = Date.now();
  for (; window.__gk < end && Date.now() - t0 < 80000; window.__gk++) {
    const k = window.__gk;
    if (!grid() || !grid().offsetParent) await back();
    let tl = tiles(), tries = 0; while (tl.length <= k && tries < 6) { grid().scrollTop = grid().scrollHeight; await sleep(1200); tl = tiles(); tries++; }
    if (tl.length <= k) return { done: true, tiles: tl.length, reviews: Object.keys(window.__g).length };
    const b = tl[k]; const id = b.dataset.reviewid, type = b.dataset.mediatype; const thumb = b.querySelector('img')?.src || '';
    b.click(); await sleep(1600);
    const p = m().querySelector('[class*=single-review-media-popover-container]'); const tx = p ? p.innerText : '';
    const media = [...m().querySelectorAll('img')].filter(e => e.clientWidth > 150).map(e => e.currentSrc || e.src);
    const r = window.__g[id] || (window.__g[id] = { id, raw: tx, images: [], thumbs: [], video: false }); if (tx.length > r.raw.length) r.raw = tx;
    if (type === 'VIDEO') { r.video = true; r.thumbs.push(thumb); } else r.images.push(...media.filter(s => /images\/I\//.test(s)).map(s => s.replace(/\._[^.]+_\./, '.')));
    await back();
  }
  return { done: false, at: window.__gk, tiles: tiles().length, reviews: Object.keys(window.__g).length };
}
