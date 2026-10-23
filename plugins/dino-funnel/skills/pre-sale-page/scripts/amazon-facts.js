// Amazon listing facts WITHOUT login (title, bullets, spec rows, hi-res images, "Customers say" summary,
// star split, aspect chips with positive/negative counts, the listing's top reviews).
// Run with chrome-devtools evaluate_script on amazon.com/dp/<ASIN>, filePath=<research>/facts-<ASIN>.json.
// Tested 2026-10-22 (the old #reviewsMedley selector is gone; chips are matched by their "Name(123)" text).
async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const t = s => (document.querySelector(s)?.innerText || '').trim();
  const facts = {
    asin: (location.pathname.match(/dp\/(\w{10})/) || [])[1], title: t('#productTitle'), by: t('#bylineInfo'),
    price: t('#corePrice_feature_div .a-offscreen') || t('.a-price .a-offscreen'), rating: t('#acrPopover'), count: t('#acrCustomerReviewText'),
    bought: t('#social-proofing-faceout-title-tk_bought'), bullets: t('#feature-bullets'),
    rows: [...document.querySelectorAll('table tr')].map(r => r.innerText.replace(/\s+/g, ' ').trim()).filter(x => x.length < 200).slice(0, 60),
    hi: [...new Set((document.documentElement.innerHTML.match(/"hiRes":"(https:[^"]+)"/g) || []).map(x => x.slice(9, -1)))],
  };
  window.scrollTo(0, document.body.scrollHeight * 0.6); await sleep(3000);
  const bt = document.body.innerText; const i = bt.indexOf('Customers say'); facts.customersSay = i >= 0 ? bt.slice(i, i + 700) : '';
  facts.hist = [...document.querySelectorAll('#histogramTable tr, #histogramTable li')].map(e => e.innerText.replace(/\s+/g, ' ')).join(' | ');
  const btns = [...document.querySelectorAll('button, [role=button], a, span')].filter(e => /^[A-Z][A-Za-z \-&']{1,40}\(\d[\d,]*\)$/.test((e.innerText || '').trim()) && e.children.length < 4);
  const seen = new Set(); facts.aspects = [];
  for (const b of btns) { const k = b.innerText.trim(); if (seen.has(k)) continue; seen.add(k); b.click(); await sleep(1300);
    const m = [...document.body.innerText.matchAll(/\d[\d,]* customers? mentions? [^"\n]{1,40}, \d[\d,]* positive, \d[\d,]* negative/gi)].map(x => x[0]); facts.aspects.push(m.slice(-1)[0] || k); }
  facts.topReviews = [...document.querySelectorAll('[data-hook="review"]')].map(r => r.innerText.replace(/\n+/g, ' | '));
  return facts;
}
