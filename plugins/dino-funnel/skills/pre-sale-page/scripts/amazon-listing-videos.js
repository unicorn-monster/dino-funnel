// Listing videos (brand video, influencer "Videos for this product", "Related videos") of one or more ASINs.
// Run with chrome-devtools evaluate_script on any amazon.com tab, filePath=<research>/videos/listing-videos.json.
// Edit ASINS first. The page HTML holds them HTML-escaped: decode &quot; and \/ before matching.
// Main-video .mp4 links often 404: videos.py swaps them for the same uuid's default.jobtemplate.hls.m3u8.
// Each entry keeps the clip's closed-captions .vtt when Amazon has one (most listing videos do).
// Tested 2026-10-26 on B0C8613QJG (12 videos), B07YJ16RQG, B0GT51M6YT.
async () => {
  const ASINS = ['B0XXXXXXXX'];
  const out = [];
  for (const a of ASINS) {
    const h = (await (await fetch('/dp/' + a)).text()).replace(/&quot;/g, '"').replace(/\\\//g, '/').replace(/\\-/g, '-');
    const seen = new Set();
    // the closed-captions .vtt sits right after its videoURL: lets videos.py skip whisper for that clip
    const vtt = i => (h.slice(i, i + 600).match(/https:\/\/[^"]+?closedCaptions\/[\w-]+\.vtt/) || [''])[0];
    const add = (title, url, i) => { const uid = (url.match(/prod\/([\w-]+)\//) || [])[1] || url; if (!seen.has(uid)) { seen.add(uid); out.push({ asin: a, title, url, vtt: vtt(i) }); } };
    for (const m of h.matchAll(/"title":"([^"]{0,140})"[^{}]{0,3000}?"videoURL":"(https[^"]+?\.m3u8)"/g)) add(m[1], m[2], m.index + m[0].length);
    for (const m of h.matchAll(/https:\/\/m\.media-amazon\.com\/images\/S\/vse-vms-transcoding-artifact-us-east-1-prod\/[\w-]+\/default\.jobtemplate\.mp4/g)) add('main listing video', m[0], m.index);
    for (const m of h.matchAll(/"videoURL":"(https[^"]+?\.m3u8)"/g)) add('', m[1], m.index + m[0].length);
  }
  return out;
}
