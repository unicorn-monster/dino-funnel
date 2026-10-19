# Template: locket

Source: live page https://offer.dinosaurized.com/locket-chest-holster-1 (Locket Chest Holster, Dinosaurized).
A long-form direct-response product page pasted into a Funnelish **Custom HTML** block. Every button goes to the next funnel step (checkout).

The full page HTML is at the bottom of this file. To make a new page: copy it to `output/<slug>/index.html`, keep the `<head>` and `<style>` exactly as they are, and replace the content inside `<body>` section by section using the same classes. Don't restyle anything; the look comes from the CSS.

## Page structure (top to bottom)

| Part | Markup | What goes in it |
|---|---|---|
| Trust bar | `div.trustbar` | brand constant, keep |
| Hero | `div.hero` | `h1` with one `<em>` for the twist; rating row (brand constant); `img.hero-img` (product in use); `p.lede`; optional `div.builds` (2 variant cards); `ul.specs` (spec bullets, each with a bold lead-in); `a.cta` + `div.cta-sub` |
| As Seen In | `div.seen` | the logo is USCCA Concealed Carry magazine: keep it **only for holsters / carry gear**. For any other product delete the whole `div.seen` block (a press logo from the wrong field is off-topic and a false claim) |
| Body sections | `div.sec` / `div.sec tint` | `div.eyebrow` + `h2` + content blocks + optional `a.cta` + `div.cta-sub`. 5 to 9 sections, alternate white / tint |
| Offer | `div.offer#offer` | product name, sub line, `img.prod`, button, `div.bonus` rows, `div.stock` |
| Guarantee | `div.sec.tint > div.guar` | guarantee badge image (brand constant) + h2 + 3 paragraphs |
| FAQ | `div.sec.faq` | `details > summary + p`, 6 to 8 real objections |
| Reviews | `div.sec.tint` with `div.score` + `div.revs > div.rev` | score/count are brand constants |
| Footer | `div.foot` | brand constant, keep |
| Sticky bar | `div.sticky` (after `.wrap`) | product image, name, `price_line`, button |

## Content blocks (reuse inside hero and sections)

| Block | Markup | Use for |
|---|---|---|
| paragraph | `<p>` | body copy, inline `<b>` `<em>` |
| image | `<img class="full" src alt>` | full-width image |
| video | `<video class="full" src autoplay muted loop playsinline preload="metadata">` | short loop |
| arrow list | `ul.plain > li` | "what that means in practice" |
| numbered | `div.numbered > div.item > div.n (01) + div.t (<b>title.</b> text)` | 3-step how-it-works |
| variant cards | `div.builds > div.build` / `div.build field` (second color) | 2 builds, colors, sizes |
| table | `table.cmp`, header cells `th.c-classic` / `th.c-field` for variant columns | variant compare, size chart |
| cards | `div.cards > div.card > img + div.body > h4 + p` | "Who It's For", 3 cards |
| callout | `<p style="font-size:15px;color:var(--gray);border-left:3px solid var(--orange);padding-left:14px">` | the one honest limitation |
| missing image | `<div class="ph">IMAGE NEEDED: what it shows</div>` | slot with no image yet |

## Section playbook (what the live Dinosaurized pages share)

1. **The Real Problem** (tint, CTA): the pain the buyer already lives with, in their words, then how this product moves it. One image + an arrow list "what that means in practice".
2. **2 to 4 mechanism sections**: one per real feature that solves the problem. Eyebrow names the benefit, h2 is the claim, image, short paragraphs, a numbered list or arrow list when there are steps.
3. **Variants / fit / size** (only if the product has them): variant cards or a table.
4. **Straight Talk** (no CTA): the honest limitation as a callout + a paragraph handling the main objection. This is what makes the rest believable.
5. **Who It's For** (tint, no CTA): 3 cards, each a real buyer type with a real use case.

## Brand constants (keep exactly as in the HTML below)

Trust bar, CTA label `👉 Reveal Offer` + sub line, guarantee badge image, footer, hero rating `4.8/5` + `18,736`, reviews score `4.8` + `18,736` (store-wide numbers), 120-day guarantee, stock `15`.
Offer box when the user gives no offer: button "Get 50% Off Today Only!", bonus title "Plus $X Worth Of Free Gifts" (X ≈ sum of bonuses), bonus rows as in Locket (handbook, free shipping on 2+, multi-pack discount). The bonuses must match the real Funnelish checkout, so list them as "confirm" in research.md.

## Rules

- **Landing-page CTA contract:** every CTA anchor uses the exact `href="#next-step"`. Funnelish resolves it to the immediate next step in funnel order, so the Sale Page step must be followed by Checkout.
- **Navigation only:** `#next-step` only navigates; it does not submit forms or add products. Checkout form submission stays a native Funnelish Submit step action. Post-purchase acceptance uses Funnelish's `#yes-link` action.
- **Anchor ownership:** the offer box is `id="offer"`. Keep `next-step` exclusively for CTA `href` values: no element uses `id="next-step"`, and no custom JavaScript intercepts these clicks.
- **Funnelish references:** [CTA actions](https://community.funnelish.com/t/ctas-buttons-and-links/10225) and [Custom HTML navigation](https://community.funnelish.com/t/custom-html-oto-tracking-in-funnelish-important-setup/9859).
- **No em dash** (`—`, `&mdash;`). Use a comma or a period.
- **No price** (`$` followed by a digit) anywhere except the offer bonus title and the struck-through `was` values in bonus rows. The sticky bar says "50% OFF", not a dollar amount.
- **Reviews:** only real Dinosaurized customer reviews. Amazon reviews of the white-label listing belong to another seller. With none provided, keep 4 `div.rev` cards with `IMAGE NEEDED` boxes, who = `[REVIEWER NAME]`, text = `[PLACEHOLDER: paste a real Dinosaurized customer review here]`.
- **Facts:** every spec and claim traces to the listing. Anything uncertain goes into research.md as "confirm", not onto the page.
- **Name:** the product name is ours (Locket, Mamasaurus, Clear View...), never the Amazon title. Propose one and flag it.

## Finish (run from `output/<slug>/`)

```bash
grep -nE '—|&mdash;' index.html                    # must be empty
grep -noE '\$[0-9][^<]{0,40}' index.html            # only the offer bonus title and bonus "was" values
grep -c 'href="#next-step"' index.html              # = number of CTAs + offer button + sticky
grep -c 'id="next-step"' index.html                 # must be 0
python3 -c "import pathlib as p; f=p.Path('index.html'); f.write_text(f.read_text().encode('ascii','xmlcharrefreplace').decode())"   # pure ASCII so the Funnelish paste can't garble ★ and emoji
```

The ASCII step is safe to run more than once. It turns ★ into `&#9733;`; inside `<style>`, any non-ASCII character (the CSS uses ✓ in `content:`) must be a CSS escape instead (`\2713 `), which the template's CSS already is. Check: `python3 -c "print(open('index.html','rb').read().isascii())"` prints `True`.

## Template HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Locket Chest Holster: Classic &amp; Field | Dinosaurized</title>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  :root{
    --orange:#e75201;--orange-dark:#c84500;--navy:#1c2233;--cream:#f9f6f1;
    --gray:#6b7280;--gray-light:#f3f4f6;--border:#e5e0d8;
    --field:#4a3b2a;--classic:#2d3b4a;
  }
  body{font-family:'DM Sans',sans-serif;font-size:17px;line-height:1.65;color:var(--navy);background:var(--cream)}
  .wrap{max-width:780px;width:100%;margin:0 auto;background:#fff}
  /* --- \e9 p r\1ed9 ng khi nh\fa ng v\e0 o Funnelish/Shopify (container cha h\1eb9 p) --- */
  .wrap,.wrap *{max-width:100%;box-sizing:border-box}
  .wrap{max-width:780px!important}
  .sec img.full,.hero-img,.offer img.prod,.card img,.rev img,.guar img,.seen img{
    width:100%!important;height:auto!important;max-width:100%!important}
  .offer img.prod{max-width:320px!important}
  .guar img{max-width:110px!important;width:110px!important}
  .card img{height:auto!important;aspect-ratio:1/1;object-fit:cover}
  .rev img{height:auto!important;aspect-ratio:1/1;object-fit:cover}
  img{max-width:100%;display:block}

  /* TRUST BAR */
  .trustbar{background:var(--navy);color:#fff;display:flex;flex-wrap:wrap;justify-content:center;gap:4px 26px;padding:10px 14px;font-size:11px;letter-spacing:1px;text-transform:uppercase;font-weight:700}
  .trustbar span{white-space:nowrap}
  .trustbar .star{color:var(--orange)}

  /* HERO */
  .hero{padding:26px 22px 8px}
  .hero h1{font-family:'Oswald',sans-serif;font-weight:700;font-size:33px;line-height:1.12;letter-spacing:-0.4px;margin-bottom:12px}
  .hero h1 em{color:var(--orange);font-style:normal}
  .rating-row{display:flex;align-items:center;gap:9px;margin-bottom:18px;font-size:13px;color:var(--gray)}
  .rating-row .stars{color:var(--orange);font-size:15px;letter-spacing:1px}
  .rating-row strong{color:var(--navy)}
  .hero-img{border-radius:6px;margin-bottom:20px;border:1px solid var(--border)}
  .hero p.lede{font-size:17px;margin-bottom:20px;line-height:1.6}

  /* BUILD PICKER */
  .builds{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:22px 0}
  .build{border:2px solid var(--border);border-radius:8px;padding:16px 14px;background:#fff}
  .build.field{border-color:var(--field)}
  .build .tag{display:inline-block;font-family:'Oswald',sans-serif;font-weight:700;font-size:11px;letter-spacing:1.6px;text-transform:uppercase;padding:3px 9px;border-radius:3px;margin-bottom:9px;color:#fff;background:var(--classic)}
  .build.field .tag{background:var(--field)}
  .build h4{font-family:'Oswald',sans-serif;font-size:17px;font-weight:600;margin-bottom:6px;line-height:1.2}
  .build p{font-size:13.5px;line-height:1.5;color:var(--gray)}
  .build p b{color:var(--navy)}

  /* SPEC LIST */
  .specs{list-style:none;margin:20px 0}
  .specs li{padding:8px 0 8px 27px;position:relative;font-size:15.5px;line-height:1.5;border-bottom:1px solid var(--gray-light)}
  .specs li:last-child{border-bottom:none}
  .specs li:before{content:"\2713 ";position:absolute;left:2px;top:8px;color:var(--orange);font-weight:700}
  .specs li b{font-weight:700}

  /* CTA */
  .cta{display:block;background:var(--orange);color:#fff;text-decoration:none;text-align:center;font-family:'Oswald',sans-serif;font-weight:700;font-size:19px;letter-spacing:1.2px;text-transform:uppercase;padding:17px 20px;border-radius:5px;margin:22px 0 8px;box-shadow:0 3px 0 var(--orange-dark)}
  .cta:active{transform:translateY(2px);box-shadow:0 1px 0 var(--orange-dark)}
  .cta-sub{text-align:center;font-size:12.5px;color:var(--gray);margin-bottom:26px}

  /* SECTION */
  .sec{padding:34px 22px;border-top:1px solid var(--border)}
  .sec.tint{background:var(--cream)}
  .sec.dark{background:var(--navy);color:#fff;border-top:none}
  .sec.dark h2,.sec.dark h3{color:#fff}
  .sec.dark p{color:#cfd3da}
  .eyebrow{font-family:'Oswald',sans-serif;font-size:12px;font-weight:700;letter-spacing:2.2px;text-transform:uppercase;color:var(--orange);margin-bottom:7px}
  .sec h2{font-family:'Oswald',sans-serif;font-weight:700;font-size:27px;line-height:1.16;letter-spacing:-0.3px;margin-bottom:14px}
  .sec p{margin-bottom:15px;font-size:16.5px;line-height:1.65}
  .sec img.full,.sec video.full{border-radius:6px;margin:20px 0;border:1px solid var(--border)}
  .sec video.full{display:block;width:100%;height:auto;background:#000}
  .sec ul.plain{list-style:none;margin:14px 0 18px}
  .sec ul.plain li{padding:7px 0 7px 26px;position:relative;font-size:16px;line-height:1.5}
  .sec ul.plain li:before{content:"\2192 ";position:absolute;left:0;color:var(--orange);font-weight:700}

  /* NUMBERED */
  .numbered{margin:18px 0}
  .numbered .item{display:flex;gap:14px;margin-bottom:16px}
  .numbered .n{font-family:'Oswald',sans-serif;font-weight:700;font-size:26px;color:var(--orange);line-height:1;flex-shrink:0;width:34px}
  .numbered .t{font-size:15.5px;line-height:1.55}
  .numbered .t b{display:block;margin-bottom:2px}

  /* COMPARE TABLE */
  .cmp{width:100%;border-collapse:collapse;margin:20px 0;font-size:14.5px}
  .cmp th,.cmp td{padding:11px 10px;text-align:left;border-bottom:1px solid var(--border);vertical-align:top}
  .cmp th{font-family:'Oswald',sans-serif;font-size:13px;letter-spacing:1px;text-transform:uppercase;background:var(--gray-light)}
  .cmp th.c-classic{color:#fff;background:var(--classic)}
  .cmp th.c-field{color:#fff;background:var(--field)}
  .cmp td:first-child{font-weight:700;width:33%}

  /* USE CARDS */
  .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}
  .card{border:1px solid var(--border);border-radius:6px;overflow:hidden;background:#fff}
  .card img{width:100%;aspect-ratio:1/1;object-fit:cover}
  .card .body{padding:13px 12px}
  .card h4{font-family:'Oswald',sans-serif;font-size:16px;margin-bottom:6px}
  .card p{font-size:13.5px;line-height:1.5;color:var(--gray);margin:0}

  /* OFFER */
  .offer{background:var(--navy);color:#fff;padding:34px 22px;text-align:center}
  .offer h2{font-family:'Oswald',sans-serif;font-size:29px;line-height:1.12;margin-bottom:8px;color:#fff}
  .offer .sub{color:#cfd3da;font-size:15px;margin-bottom:20px}
  .offer img.prod{max-width:300px;margin:0 auto 20px;border-radius:6px;background:#fff}
  .bonus{background:rgba(255,255,255,0.07);border-radius:6px;padding:16px;margin:18px 0;text-align:left}
  .bonus .bh{font-family:'Oswald',sans-serif;font-size:14px;letter-spacing:1.6px;text-transform:uppercase;color:var(--orange);text-align:center;margin-bottom:12px}
  .bonus .row{display:flex;align-items:center;gap:10px;padding:9px 0;border-top:1px solid rgba(255,255,255,0.12);font-size:14.5px}
  .bonus .row:first-of-type{border-top:none}
  .bonus .row .nm{flex:1;color:#fff}
  .bonus .row s{color:#8a919c;font-size:13px;margin-right:6px}
  .bonus .row .free{color:var(--orange);font-weight:700;font-size:13px}
  .stock{font-size:13px;color:#cfd3da;margin-top:12px}
  .stock b{color:var(--orange)}

  /* GUARANTEE */
  .guar{display:flex;gap:18px;align-items:flex-start}
  .guar img{width:110px;flex-shrink:0}

  /* FAQ */
  .faq details{border-bottom:1px solid var(--border);padding:14px 0}
  .faq summary{font-family:'Oswald',sans-serif;font-size:17px;font-weight:600;cursor:pointer;list-style:none;position:relative;padding-right:28px;line-height:1.35}
  .faq summary::-webkit-details-marker{display:none}
  .faq summary:after{content:"+";position:absolute;right:4px;top:-2px;color:var(--orange);font-size:24px;font-weight:700}
  .faq details[open] summary:after{content:"\2013 "}
  .faq p{margin:11px 0 0;font-size:15.5px;color:#444}

  /* REVIEWS */
  .revs{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px}
  .rev{border:1px solid var(--border);border-radius:6px;overflow:hidden;background:#fff}
  .rev img{width:100%;aspect-ratio:1/1;object-fit:cover}
  .rev .body{padding:14px 13px}
  .rev .stars{color:var(--orange);font-size:13px;letter-spacing:1px;margin-bottom:5px}
  .rev .who{font-weight:700;font-size:14.5px;margin-bottom:2px}
  .rev .buildtag{display:inline-block;font-size:10px;font-family:'Oswald',sans-serif;letter-spacing:1.2px;text-transform:uppercase;padding:2px 7px;border-radius:3px;color:#fff;background:var(--classic);margin-bottom:8px}
  .rev .buildtag.field{background:var(--field)}
  .rev p{font-size:13.5px;line-height:1.55;color:#444;margin:0}

  .score{text-align:center;margin-bottom:6px}
  .score .big{font-family:'Oswald',sans-serif;font-size:40px;font-weight:700;color:var(--orange);line-height:1}
  .score .st{color:var(--orange);font-size:17px;letter-spacing:2px;margin:4px 0}
  .score .cnt{font-size:13px;color:var(--gray)}

  /* SEEN IN */
  .seen{text-align:center;padding:26px 22px;border-top:1px solid var(--border)}
  .seen .lbl{font-family:'Oswald',sans-serif;font-size:12px;letter-spacing:2.4px;text-transform:uppercase;color:var(--gray);margin-bottom:14px}
  .seen img{max-width:100%}

  /* STICKY */
  .sticky{position:fixed;bottom:0;left:0;right:0;background:var(--navy);border-top:3px solid var(--orange);padding:10px 14px;display:flex;align-items:center;gap:10px;z-index:9999;box-shadow:0 -4px 14px rgba(0,0,0,.25)}
  .sticky img{width:44px;height:44px;border-radius:4px;object-fit:cover;background:#fff;flex-shrink:0}
  .sticky .info{flex:1;min-width:0;line-height:1.25}
  .sticky .nm{color:#fff;font-weight:700;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .sticky .pr{font-size:12px;color:#cfd3da}
  .sticky .pr b{color:var(--orange);font-family:'Oswald',sans-serif;font-size:13px}
  .sticky a{background:var(--orange);color:#fff;text-decoration:none;padding:12px 17px;font-family:'Oswald',sans-serif;font-weight:700;font-size:15px;letter-spacing:.8px;text-transform:uppercase;border-radius:4px;white-space:nowrap;flex-shrink:0;animation:pl 2s infinite}
  @keyframes pl{0%{box-shadow:0 0 0 0 rgba(231,82,1,.6)}70%{box-shadow:0 0 0 12px rgba(231,82,1,0)}100%{box-shadow:0 0 0 0 rgba(231,82,1,0)}}

  .foot{padding:26px 22px 96px;text-align:center;font-size:12.5px;color:var(--gray);border-top:1px solid var(--border);line-height:1.8}
  .foot a{color:var(--gray);text-decoration:none;margin:0 7px}

  @media(max-width:620px){
    .hero{padding:22px 17px 6px}
    .hero h1{font-size:27px}
    .sec{padding:28px 17px}
    .sec h2{font-size:23px}
    .builds{grid-template-columns:1fr}
    .cards{grid-template-columns:1fr}
    .revs{grid-template-columns:1fr}
    .offer{padding:28px 17px}
    .offer h2{font-size:24px}
    .guar{flex-direction:column;align-items:center;text-align:center}
    .sticky .info{display:none}
    .sticky a{flex:1;text-align:center}
  }

:root{--classic:#2d3b4a;--field:#4a3b2a}
.ph{background:#e5e7eb;color:#6b7280;display:flex;align-items:center;justify-content:center;min-height:180px;border-radius:6px;margin:20px 0;padding:12px;font-size:13px;text-align:center}.sticky .ph{min-height:44px;width:44px;margin:0;padding:0;font-size:0;flex-shrink:0}.guar .ph{width:110px;min-height:110px;margin:0;flex-shrink:0}
</style>
</head>
<body>
<div class="wrap">
<div class="trustbar"><span>Free Shipping</span><span class="star">★★★★★</span><span>Trusted By Thousands</span><span>120-Day Returns</span><span>Secured Checkout</span></div>
<div class="hero">
<h1>The Chest Holster That Actually Fits The Guys <em>Belt Holsters Give Up On</em></h1>
<div class="rating-row"><span class="stars">★★★★★</span><span><strong>4.8/5</strong>, rated by 18,736 happy customers</span></div><img class="hero-img" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/ad_9_bccb0e0b-26a2-489d-acda-873e511f4071.png?v=1790579942" alt="Locket Field chest holster worn on a mountain ridge"><p class="lede">Single-shoulder chest rig built around a quick-release buckle. Goes on in seconds, comes off just as fast, and stays put all day once it's on. Engineered for the one thing most shoulder rigs get wrong: making the straps genuinely fit both smaller frames <b>and</b> guys past a 50" chest.</p>
<div class="builds">
<div class="build"><span class="tag">Classic</span><h4>Soft Neoprene</h4><p>Thinnest profile under a dress shirt. Soft straight against skin. <b>For town carry and compact pistols.</b></p></div>
<div class="build field"><span class="tag">Field</span><h4>Canvas &amp; Leather</h4><p>Heavy canvas, leather retention strap, solid brass hardware. <b>For hunting, hauling, and full-size pistols.</b></p></div></div>
<ul class="specs">
<li><b>Fits:</b> Glock 17/19/26/43 · M&amp;P 9/40/Shield · P365 · SIG P320 · 1911s · revolvers up to 4" barrel</li>
<li><b>Single-shoulder design:</b> one padded strap + chest anchor, no bulky X-harness</li>
<li><b>Quick-release buckle:</b> on in 10 seconds, off in 2</li>
<li><b>Three sizes, fits 31" to 58" chests:</b> tested on frames past 6'0" / 280 lbs</li>
<li><b>Wears two ways:</b> chest-front, or rotated to under-arm shoulder position</li>
<li><b>Right-hand draw from left chest:</b> natural cross-body reach</li>
<li><b>Universal holster pod:</b> subcompact through full-size</li></ul><a class="cta" href="#next-step">👉 Reveal Offer</a>
<div class="cta-sub">Try It Risk Free • 120-Day Money Back Guarantee</div></div>
<div class="seen">
<div class="lbl">As Seen In</div><img src="https://img.funnelish.com/8133/110371/1689575767-Untitled%20design%20-%202023-07-17T133602.492.png" alt="As seen in"></div>
<div class="sec tint">
<div class="eyebrow">The Real Problem</div>
<h2>If Your Waistband Carry Quit Working, Start Here</h2><p>Here's the problem with IWB carry most guys don't say out loud:</p><p>The gun ends up exactly where your body already hurts. Your hip. Your gut. Your lower back. Four, six, ten hours. That's where the pistol lives, pressing into the same spots you already fight with.</p><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/ad_6_d33e3afc-b915-4ebc-9cf6-0aea6da1c9b4.png?v=1790579942" alt="Drawing from chest holster while seated with seatbelt on"><p>The Locket moves the weight up and out of that zone entirely. Chest placement. Distributed across the shoulder and ribcage. Completely off your waistband.</p><p><b>What that means in practice:</b></p>
<ul class="plain">
<li>Nothing digging into your hip when you sit in a truck</li>
<li>No printing through your shirt at 3 o'clock</li>
<li>Seatbelt crosses below the pistol, not through the draw path</li>
<li>Works the same with a belly as without one, the rig doesn't care</li></ul><p>The shoulder strap is wide and padded enough to spread weight across the trap instead of cutting into it. And the quick-release buckle means you can take the whole thing off at the end of the day without wrestling with it for five minutes.</p><a class="cta" href="#next-step">👉 Reveal Offer</a>
<div class="cta-sub">Try It Risk Free • 120-Day Money Back Guarantee</div></div>
<div class="sec">
<div class="eyebrow">Why Guys Keep Wearing It</div>
<h2>The Buckle Is The Whole Point</h2><p>Most shoulder holsters take 3-5 minutes to get on right. You pull it over your head, fight with the straps, realize it's twisted, start over. By the third time that week, you're not wearing it anymore.</p><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/1773760786-imageye___-_imgi_17_EgGP81n5KPvieHL._AC_SL1500.webp?v=1790581679" alt="Quick release buckle detail"><p>The Locket uses a single quick-release buckle at the chest strap. <b>Snap it on in about 10 seconds. Pull it off in 2.</b> That's the difference between a rig you wear every day and one that stays in the drawer.</p>
<div class="numbered">
<div class="item">
<div class="n">01</div>
<div class="t"><b>Setup speed.</b> Put on your shirt, snap the Locket over it (or under, your call), adjust once, go.</div></div>
<div class="item">
<div class="n">02</div>
<div class="t"><b>Same fit every time.</b> Adjust the straps one time to your body. After that the buckle releases and reclips to the same position. No re-calibrating every morning.</div></div>
<div class="item">
<div class="n">03</div>
<div class="t"><b>Off in 2 seconds.</b> Bathroom break, range trip, gym: unclip, step out of it, clip back in when you're done. Not a process.</div></div></div><p>Sounds like a small thing. It isn't. It's the difference between a holster you own and a holster you actually wear.</p><a class="cta" href="#next-step">👉 Reveal Offer</a>
<div class="cta-sub">Try It Risk Free • 120-Day Money Back Guarantee</div></div>
<div class="sec tint">
<div class="eyebrow">Classic Or Field</div>
<h2>Same Position On Your Body. Two Different Jobs.</h2><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/4_1.png?v=1790583089" alt="Locket Classic versus Field build comparison"><p><b>Pick CLASSIC</b> if you carry in town. Office, church, errands, restaurants. Compact or subcompact pistol. You want the thinnest thing that disappears under a dress shirt, and you want it soft against your skin without an undershirt.</p><p><b>Pick FIELD</b> if your gear takes abuse. Hunting season, the ATV, the farm, a loaded pack on your back. Full-size pistol or a revolver. Canvas doesn't pack down the way foam does. It breaks in and stays that way for years, and the leather strap holds the same tension on day 400 as it did on day one.</p>
<table class="cmp">
<tr><th></th><th class="c-classic">Classic</th><th class="c-field">Field</th></tr>
<tr><td>Material</td><td>Perforated neoprene</td><td>Heavy canvas + genuine leather</td></tr>
<tr><td>Retention</td><td>Elastic band + snap</td><td>Leather strap + brass snap</td></tr>
<tr><td>Hardware</td><td>Polymer buckle</td><td>Brass roller buckles</td></tr>
<tr><td>Thinnest under a suit</td><td>✓ Best</td><td>Very good</td></tr>
<tr><td>Heavy full-size &amp; revolvers</td><td>Good</td><td>✓ Best</td></tr>
<tr><td>Rain, brush, pack straps</td><td>Good</td><td>✓ Best</td></tr>
<tr><td>Soft on bare skin</td><td>✓ Best</td><td>Wear over a shirt</td></tr></table><p>Most guys who buy one end up with both. One lives in the closet. One lives in the truck.</p><a class="cta" href="#next-step">👉 Reveal Offer</a>
<div class="cta-sub">Try It Risk Free • 120-Day Money Back Guarantee</div></div>
<div class="sec">
<div class="eyebrow">One Rig, Any Sidearm</div>
<h2>One Holster, Whatever You're Carrying Today</h2><p>Most of us don't carry the same pistol every day. Compact at the office. Full-size on the weekend. The wife's .38 revolver walking the dog. The Locket's holster pod adjusts across the range. Not "technically compatible," actually fits.</p><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/ad_8_81684048-83a3-4d86-bae2-e3a31505f014.png?v=1790579942" alt="Locket holster fits multiple pistol sizes"><p><b>Confirmed fit across:</b></p>
<ul class="plain">
<li><b>Subcompact:</b> Glock 43x · P365 · Shield · Ruger LCP · Beretta Nano</li>
<li><b>Compact:</b> Glock 19/26 · M&amp;P 9 · SIG P320 Compact · Beretta PX4 Compact</li>
<li><b>Full-size:</b> Glock 17 · Glock 21 · 1911 Government · Beretta 92 · SIG P226</li>
<li><b>Revolvers:</b> J-frame · SP101 · LCR · GP100 (up to 4" barrel)</li>
<li><b>With optics:</b> 507C · RMR · 407K · Holosun · Trijicon all clear</li></ul><p>Retention adjusts to the pistol's profile: tight enough to hold through movement, loose enough to draw clean. The pod flips from right to left carry in under a minute.</p><p style="font-size:15px;color:var(--gray);border-left:3px solid var(--orange);padding-left:14px"><b>One thing it won't take:</b> a pistol with a weapon light mounted. Red dots clear fine. Lights add too much width for the pod.</p><a class="cta" href="#next-step">👉 Reveal Offer</a>
<div class="cta-sub">Try It Risk Free • 120-Day Money Back Guarantee</div></div>
<div class="sec tint">
<div class="eyebrow">Two Carry Positions</div>
<h2>It Wears Two Completely Different Ways</h2><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/vv_2_9ec86c85-a4b8-45b6-8b6d-eac158136874.png?v=1790580397" alt="Chest position versus under-arm shoulder position"><p>Rotate the whole rig around your torso (no unbuckling, no re-threading straps) and the pod drops from center chest down under your arm. Now it's a classic shoulder holster. Drop your arm and it vanishes completely.</p><p><b>Chest-front</b> for outdoors: hunting, the ATV, working the property, anywhere you've got a pack or a jacket and you want the grip where both hands can reach it.</p><p><b>Under-arm</b> when you're dressed up: the pod sits behind the lapel line of a suit jacket and there's nothing to see, even leaning forward at a table.</p><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/1773760781-imageye___-_imgi_7_YxPY91tqDcTTJ2L._AC_SL1500_480x480_f0d8ca6d-3d86-4bc5-a8ec-760ecf576049.webp?v=1790581656" alt="Another way to wear it"><p>Same holster. Two carry philosophies. Takes about four seconds to switch.</p></div>
<div class="sec">
<div class="eyebrow">The One Belt Carry Can't Do</div>
<h2>It's The Only Rig That Survives A Backpack</h2><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/vv_1_b6d5b351-ceee-4aea-b801-fc7d52fa9cb9.png?v=1790580397" alt="Hiking with a loaded pack and a chest holster"><p>Anybody who hunts, hikes, or hauls a pack already knows this problem and has probably just accepted it.</p><p>A loaded pack's hip belt sits at exactly the same height as your holster. There's no sharing that real estate. So you either cinch the hip belt over your gun (miserable and slow) or you loosen the belt and let forty pounds hang off your shoulders all day, which is worse.</p><p>Most guys solve it by leaving the gun in the truck. Which is a hell of a solution when you're the one walking into the treeline alone.</p><p>Chest carry doesn't compete with the hip belt. Pack straps run over your shoulders, the holster strap runs under them, and the pod sits in the open space on your sternum. Nothing stacked, nothing pinched.</p><a class="cta" href="#next-step">👉 Reveal Offer</a>
<div class="cta-sub">Try It Risk Free • 120-Day Money Back Guarantee</div></div>
<div class="sec tint">
<div class="eyebrow">Rain, Sweat, Hard Days</div>
<h2>Canvas Sheds It. Foam Soaks It Up.</h2><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/4_2.png?v=1790583089" alt="Canvas chest holster shedding rain"><p>Here's what nobody tells you about soft holsters: foam and elastic have a shelf life. Months of body heat and sweat and they pack down flat. Retention goes loose. The strap stretches and stops holding your adjustment. You don't notice it happening. You just notice one day that the gun moves more than it used to.</p><p>Canvas doesn't pack down. It breaks in. Same way a good work jacket does: stiff for the first week, then it molds to you and stays that way for years. It sheds rain instead of soaking it up, and dries fast when it does get wet.</p><p>A guy we know ran his through a full week of backcountry with a 50-pound pack: sweat, rain, brushing pines every twenty feet. It came out looking broken in, not beat up.</p><p>And the leather retention strap does something elastic never does: it holds the same tension on day 400 that it held on day one. One thumb to open. One press to close.</p><a class="cta" href="#next-step">👉 Reveal Offer</a>
<div class="cta-sub">Try It Risk Free • 120-Day Money Back Guarantee</div></div>
<div class="sec tint">
<div class="eyebrow">Who It's For</div>
<h2>Locket Chest Holsters Are Perfect For</h2>
<div class="cards">
<div class="card"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/vv_1_b6d5b351-ceee-4aea-b801-fc7d52fa9cb9.png?v=1790580397" alt="Outdoor Enthusiasts">
<div class="body"><h4>Outdoor Enthusiasts</h4><p>Hikers, hunters, ATV riders, motorcyclists, farmers. IWB fights body movement: rotates, shifts, leans into the hip. Chest carry stays put through climbing, riding, crouching, and clears a pack hip belt. <b>The Field build is made for exactly this.</b></p></div></div>
<div class="card"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/ad_10_32fc0238-47d0-47b6-89dd-5c12dd3c6ed4.png?v=1790579941" alt="People In Suits">
<div class="body"><h4>People In Suits</h4><p>Under a suit jacket or blazer the Locket disappears. No belt required, no waistband bulge, no printing at the hip when you sit at a reception. Weddings, funerals, graduations, business meetings.</p></div></div>
<div class="card"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/ad_6_d33e3afc-b915-4ebc-9cf6-0aea6da1c9b4.png?v=1790579942" alt="Drivers">
<div class="body"><h4>Drivers</h4><p>Uber drivers, truckers, dispatchers, desk workers, anyone spending 6+ hours a day in a seat. IWB folds under the waistband and gets trapped against the seat. Chest carry sits above the seatbelt, accessible seated or standing.</p></div></div></div></div>
<div class="sec">
<div class="eyebrow">Get The Size Right</div>
<h2>Three Sizes. 31" To 58" Chests.</h2><p>Measure around the widest part of your chest, over the shirt you'd normally wear it with. If you're between sizes, go up, every size has adjustment range on both straps.</p><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/4_4.png?v=1790583089" alt="Locket chest holster on a bigger build"><p>That's an XL on a 280-pound frame, and there's still strap left over. Most shoulder rigs tap out around 48". This one doesn't.</p><img class="full" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/4_3.png?v=1790583089" alt="Locket size chart">
<table class="cmp">
<tr><th>Size</th><th>Chest</th><th>Typical build</th></tr>
<tr><td>M</td><td>31" – 40"</td><td>Slim to average</td></tr>
<tr><td>L</td><td>41" – 50"</td><td>Average to broad</td></tr>
<tr><td>XL</td><td>51" – 58"</td><td>Big and tall</td></tr></table></div>
<div class="offer" id="offer">
<h2>Locket Chest Holster</h2>
<div class="sub">Classic &amp; Field builds. Pick yours on the next page.</div><img class="prod" src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/ad_11_a2e2d40d-c84e-4d4a-bf9a-f8a8c51662d4.png?v=1790579941" alt="Locket Chest Holster"><a class="cta" href="#next-step" style="margin-top:0">Get 50% Off Today Only!</a>
<div class="bonus">
<div class="bh">Plus $120 Worth Of Free Gifts</div>
<div class="row">
<div class="nm">🎁 The Travel Safety Handbook</div>
<div><s>$29.97</s><span class="free">FREE</span></div></div>
<div class="row">
<div class="nm">🚚 Free Shipping On Packs Of 2+</div>
<div><s>$9.97</s><span class="free">FREE</span></div></div>
<div class="row">
<div class="nm">💰 Special Multi-Pack Discount</div>
<div><s>$89.97</s><span class="free">FREE</span></div></div></div>
<div class="stock">Order now, only <b>15</b> left in stock</div></div>
<div class="sec tint">
<div class="guar"><img src="https://img.funnelish.com/15168/120537/1713329736-120%20days%20guarantee.png" alt="Guarantee">
<div>
<h2 style="font-size:24px">Our Rig, Your Confidence. Guaranteed.</h2><p>When your gear arrives, put it to the test for a full 120 days. Wear it to work, to church, into the woods. Sweat in it. Soak it. Sleep in it if you want.</p><p>If it doesn't earn a permanent spot in your everyday carry, email us at <b>support@dinosaurized.com</b> for a full refund. No hoops. No headaches. No questions asked.</p><p>We stand behind our gear, because anything less isn't worth carrying.</p></div></div></div>
<div class="sec faq">
<div class="eyebrow">Ready To Order, But Have Questions?</div>
<h2>We Got You Covered</h2>
<details><summary>What's the difference between Classic and Field?</summary><p>Classic is soft perforated neoprene: thinnest under a dress shirt, soft enough to wear against bare skin. Field is heavy canvas with a genuine leather retention strap and solid brass hardware, built for outdoor abuse, heavier pistols, and years of hard use. Same carry position, same buckle, same sizing.</p></details>
<details><summary>Will it fit my pistol with a weapon light?</summary><p>No. Both builds are sized for bare pistols and red dots. 507C, RMR, 407K, Holosun and Trijicon all clear fine. Weapon lights add too much width for the pod. If you run a light on your carry gun, this isn't the right rig for you.</p></details>
<details><summary>Will this holster fit my revolver?</summary><p>Yes. The pod takes most compact and mid-size revolvers (J-frame, SP101, LCR, GP100) with a barrel up to 4". Full-size or long-barrel revolvers (6"+) don't sit well.</p></details>
<details><summary>Can it really be concealed under clothing?</summary><p>Yes. The low profile disappears under an untucked button-down, hoodie, flannel, light jacket or suit coat. Under a fitted t-shirt only, you'll see some outline. That's true of every chest rig on the market.</p></details>
<details><summary>What size should I order?</summary><p>Three sizes: M fits 31"–40", L fits 41"–50", XL fits 51"–58". Measure the widest part of your chest over the shirt you'd wear it with. Between sizes? Go up, every size adjusts on both straps.</p></details>
<details><summary>Is it suitable for both men and women?</summary><p>Yes. The straps adjust on two axes, and size M starts at a 31" chest. Plenty of women run it for hiking and trail carry where a waistband rig won't work with a pack.</p></details>
<details><summary>What if I don't like it?</summary><p>Contact our support team at support@dinosaurized.com within 120 days and we'll refund you in full. Send the product back to our warehouse and that's it. No questions asked.</p></details></div>
<div class="sec tint">
<div class="score">
<div class="big">4.8</div>
<div class="st">★★★★★</div>
<div class="cnt">Based on 18,736 reviews</div></div>
<h2 style="text-align:center;margin-top:14px">Everyone Loves The Locket</h2>
<div class="revs">
<div class="rev"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/rv_locket_field.jpg?v=1790581372" alt="Mitchell G., Wilderness Guide review">
<div class="body">
<div class="stars">★★★★★</div>
<div class="who">Mitchell G., Wilderness Guide</div><span class="buildtag field">Field Build</span><p>I've had mine six months now and it's the most reliable piece of gear I own. Snug, doesn't shift, comfortable enough for all-day wear. Daily carry is a compact Glock 26 and it fits like a glove. Went canvas and leather because I'm in the woods most weekends. The brass snap is the same tension it was a year ago.</p></div></div>
<div class="rev"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/rv_locket_classic.webp?v=1790581372" alt="Peter S. review">
<div class="body">
<div class="stars">★★★★★</div>
<div class="who">Peter S.</div><span class="buildtag">Classic Build</span><p>This holster is a game-changer. I've struggled to find something that fits my body type and my S&amp;W M&amp;P Shield, and this fits both perfectly. Discreet enough under a light jacket without printing. Really impressed with the quality. It's held up through hiking, running, and everyday use.</p></div></div>
<div class="rev"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/rv_locket_field.png?v=1790581372" alt="James B. review">
<div class="body">
<div class="stars">★★★★★</div>
<div class="who">James B.</div><span class="buildtag field">Field Build</span><p>Bought it for professional use as a private security contractor. Being able to switch between a Sig P320 and a Beretta 92 is a huge plus. The canvas has held up through everything and the leather strap hasn't stretched out, which matters when you're wearing it 12+ hours. I've recommended it to all my colleagues.</p></div></div>
<div class="rev"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/rv_locket_classic_1.jpg?v=1790581372" alt="Emily K. review">
<div class="body">
<div class="stars">★★★★★</div>
<div class="who">Emily K.</div><span class="buildtag">Classic Build</span><p>Works great. Fits my 9mm well and is comfortable to wear. The straps adjust easily and keep everything secure. I also like the extra pocket for the magazine. Good quality and does exactly what it's supposed to do. Definitely a good buy.</p></div></div>
<div class="rev"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/rv_locket_classic_2.jpg?v=1790581372" alt="Christopher J. Moore review">
<div class="body">
<div class="stars">★★★★★</div>
<div class="who">Christopher J. Moore</div><span class="buildtag">Classic Build</span><p>Nice comfortable holster. Tried a little Beretta APX A1 with a red dot and it fit fine. Also a full size 9mm and a .45 1911, both fine. Very pliable, conforms to the body. Sits high and doesn't weigh down the waist, which is nice. I can see fishermen or hunters using it. You can wade pretty deep without worrying about your weapon. Nothing snags as you're moving.</p></div></div>
<div class="rev"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/1773760782-imageye___-_imgi_6_P34481d7cKdjd-L._AC_SL1500_480x480_414ea636-aedb-45a2-88ea-d1ea41afb1ed.webp?v=1790581701" alt="Rebecca S. Anderson review">
<div class="body">
<div class="stars">★★★★★</div>
<div class="who">Rebecca S. Anderson</div><span class="buildtag">Classic Build</span><p>I have a Glock 17 and was looking for a good concealed holster after getting my permit. I'd tried a few waistbands and holsters and they all felt uncomfortable during the day. So glad I found this one. Comfortable for extended wear and holds my pistol secure while still being easy to access. Setup took a couple of minutes. Feels much more natural than the waist holsters I tried.</p></div></div></div></div>
<div class="foot">Dinosaurized LLC<br><a href="https://dinosaurized.com/pages/contact">Privacy Policy</a> · <a href="https://dinosaurized.com/policies/refund-policy">Refund Policy</a> · <a href="https://dinosaurized.com/policies/terms-of-service">Terms Of Service</a> · <a href="https://dinosaurized.com/pages/shipping-handling">Shipping Policy</a><br><br>support@dinosaurized.com</div>
</div>
<div class="sticky"><img src="https://cdn.shopify.com/s/files/1/0267/4255/4668/files/ad_11_a2e2d40d-c84e-4d4a-bf9a-f8a8c51662d4.png?v=1790579941" alt="Locket Chest Holster">
<div class="info">
<div class="nm">Locket Chest Holster</div>
<div class="pr"><b>50% OFF</b> · Classic &amp; Field</div></div><a href="#next-step">Reveal Offer →</a></div>
</body>
</html>
```
