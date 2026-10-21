---
name: upsell-downsell
description: Build the top section of a Dinosaurized post-checkout OTO step (upsell-1, downsell-1, upsell-2, downsell-2) on Funnelish - logo + "STOP! YOUR ORDER IS NOT COMPLETED YET!" headline, hook + body copy, offer column (product name, "Only NOW" price, pill, hero photo) and "BONUS TODAY" list - as one Custom HTML block. Use when the user asks for "upsell", "downsell", "OTO", "oto1", "one time offer", "trang upsell cho sp X", "upsell-1", "downsell-1", or sends an offer.dinosaurized.com/...-oto link to copy for another product. The product list, YES button and "No thanks" link stay native Funnelish elements and are not coded.
---

# Upsell / downsell (Funnelish OTO steps)

Funnel order after checkout: `upsell-1 → downsell-1 → upsell-2 → downsell-2`. Each step = one Custom HTML block pasted at the top of the Funnelish OTO page; under it the user keeps the native **Product list** (radio + price) + **YES, ADD TO MY ORDER** button (`#yes-link`) + "No thanks" link. Talk to the user in Vietnamese; page copy is English.

| Step | Status | Template |
|---|---|---|
| upsell-1 | done | `templates/oto-classic.html` (clone of offer.dinosaurized.com/hummingbird-feeder-oto1-..., Funnelish page 5570689) |
| downsell-1 | done | `templates/oto-lastchance.html` (clone of offer.dinosaurized.com/hummingbird-feer-oto2-..., Funnelish page 5570690) |
| upsell-2 | done | `templates/oto-crosssell.html` (clone of offer.dinosaurized.com/hanging-bird-feeder-bath-tray-us2-..., a DIFFERENT product = cross-sell) |
| downsell-2 | done | `templates/oto-lastchance.html` again (offer.dinosaurized.com/hanging-bird-feeder-bath-tray-ds2-... has the same layout as downsell-1), with the upsell-2 product |

Demos: all 4 steps in `output/small-dog-bed/6-upsell-downsell/`. `fill.py` picks the template from the step folder (upsell-2 → oto-crosssell, downsell-* → oto-lastchance, else oto-classic).

**Step slug formula** (the user chốt 2026-10-19): `<product slug>-oto1`, `-ds1`, `-oto2`, `-ds2` for upsell-1, downsell-1, upsell-2, downsell-2. Product slug = the sale page slug without its template prefix (`offer.dinosaurized.com/10r-calming-dog-bed` → `calming-dog-bed-oto1`), same pattern as `hummingbird-feeder-oto1`. Funnelish appends its own numeric suffix. Give the user these slugs in the hand-off.

## Steps

1. **Read the offer.** `output/<sp>/0-product-brief.md` if it exists, plus `2-sale-page/research.md` (name on page, price, bonuses, guarantee, free-shipping rule) and `4-bundle/cdn-urls.md`. Ask the user for the OTO price and what the step sells (upsell-1 is usually "1 more of the same at a lower price") if he didn't say. Done when you know product name, OTO price, regular price, and which bonuses are really delivered.
2. **Write the copy** (invoke `copywriting`): `STOP_SUB` = "ADDITIONAL <PRODUCT NAME> ONE TIME OFFER"; `HOOK` = one orange line naming why a buyer wants another one; `BODY` = 2 short `<p>`, about 60 words total (longer pushes the price below the fold on mobile): who a second unit is for (second dog / second room / gift) + the product's real features, then the "this price on this page only" close. Use the sale page's product name and facts only.
3. **Pick images.** Hero = a UGC-style selfie of an owner with the product (the original uses one), from the sale page's CDN images (`2-sale-page/cdn.txt`). Bonus icons: reuse the URLs in the demo `content.json` (free shipping + money back on img.funnelish.com, special offers = `oto-oto-badge-special-offers.png` on the Dino CDN, re-cropped because the Funnelish original has ~15% white margin and looked smaller than the others). Every badge must fill its image edge to edge, or it renders smaller than its neighbours. A new image goes to the Dino CDN first: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/cdn.py <file> --prefix oto-<sp>`.
4. **Bonuses must match what the funnel delivers.** No gift on the sale page = no ebook here; the pill then names real perks ("PLUS FREE SHIPPING + 120-DAY GUARANTEE") instead of "$120 WORTH OF FREE GIFTS". Keep the Special Discount row's price = the OTO price.
5. **Fill**: write `output/<sp>/6-upsell-downsell/<step>/content.json` (keys = the `{{...}}` in the template; `BONUSES` = list of `{IMG, TALL ("" or " tall" for a 150px-high icon), TITLE, WAS, NOW}`), then `python3 ${CLAUDE_PLUGIN_ROOT}/skills/upsell-downsell/scripts/fill.py output/<sp>/6-upsell-downsell/<step>/content.json`. It writes `index.html` next to it and exits 1 if any `{{...}}` is left.
6. **Verify in Chrome** (chrome-devtools MCP, `python3 -m http.server` in `output/<sp>/6-upsell-downsell`) at desktop 1440 and mobile (<600px): two columns on desktop, stacked on mobile, no horizontal scroll, every `img` has `naturalWidth > 0`. Compare side by side with the reference OTO page.
7. **Hand off**: `pbcopy < index.html`, run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/funnel/scripts/funnel_view.py <sp>`, give the user the localhost link. Remind him: paste into one Custom HTML block at the top, keep the native Product list + YES button + No-thanks link under it, set the product/price in the Product list to the OTO price.
8. **Funnelish product setup for the user** (he fills the step's Product list by hand): write `output/<sp>/6-upsell-downsell/funnelish-products.md`, one row per step: slug, Product name (`1x <Product name>`), Price (number only, e.g. `34.95`), image file, Variant (`Color` + options, from the sale page research / bundle colors). Copy each step's product image (the 1-pack bundle image, 500x500 white: `output/<sp>/4-bundle/bundle-1-*.jpg`, or the cross-sell product's own `4-bundle/`) to `~/Downloads/<sp>-oto/` named `<N>-<step>-<product>.jpg`. Paste the table in the reply too.

## Template notes (`oto-classic`)

Layout = the hummingbird OTO1 (logo, STOP headline, hook + body, offer column | BONUS TODAY column). Design cleaned up 2026-10-19 at the user's request; keep these rules when editing it or adding a template:

- **One accent color**: Dino orange `#E75300` (`--acc`) only on the STOP word, the product-name bar, the price and the bonus "FREE TODAY" values. Everything else is ink `#252A32` / text `#3a3a3a`. No red.
- **Price is the loudest element**: 60px desktop / 46px mobile, orange; bigger than every heading on the page.
- **Above the fold on mobile (390x844)**: price + pill + top of the hero photo must show without scrolling (demo: price at ~600px). Check this with the chrome-devtools `emulate` viewport `390x844x2,mobile,touch`. Never `resize_page`: it shrinks the user's real Chrome window.
- Long copy left-aligned, max 760px wide, 12px between paragraphs; headlines centered. Pill = one inline-block chip (never an inline background that breaks across lines). BONUS TODAY heading smaller than the product name bar.
- **CSS reset must have zero specificity** (`:where(.oto) :where(p, h1, h2, h3) { margin: 0 }`). A plain `.oto h3 { margin: 0 }` beats `.oto-now { margin-top }` and every gap in the offer column silently collapses to 0. After any CSS change, measure the gaps (getBoundingClientRect) instead of trusting the stylesheet.
- Keys: `STOP_ACCENT`, `STOP_DARK`, `STOP_SUB`, `HOOK`, `BODY`, `PRODUCT_NAME`, `NOW_LABEL`, `PRICE`, `PRICE_UNIT`, `PILL`, `HERO_IMG`, `HERO_ALT`, `BONUS_HEADING`, `BONUSES`.
- The block carries its own `<meta name="viewport">` (needed for the local preview, ignored inside Funnelish) and loads Montserrat + Roboto from Google Fonts. Max width 1170px like a Funnelish `section_row`.
- Layout difference vs the original: there the Product list + button sit inside the right column under the bonuses; with one Custom HTML block they go full width below it. On mobile it's the same (everything stacks).

## Template notes (`oto-lastchance`, downsell-1)

- Layout = the hummingbird OTO2: headline "LAST CHANCE! SAVE $X" + gray sub-line, then one card: product photo (left on desktop, top on mobile) | cart-reserved countdown, product name, "Only NOW:", price + "each" + struck regular price, "Act Now and You'll Get:" checklist. Same design rules as oto-classic (one orange accent, price loudest, price above the fold on mobile: demo at ~550px).
- **Price rule (the user chốt 2026-10-19): each downsell = the upsell right before it − $5** (downsell-1 = upsell-1 − $5, downsell-2 = upsell-2 − $5). Demo: upsell-1 $34.95 → downsell-1 $29.95. `HEAD_ACCENT` saving = regular price − downsell price, exact (no rounding). Checklist = only what the funnel really delivers (no ebook if the sale page has no gift).
- Hero photo: a product-in-scene shot different from the upsell-1 photo (demo: `lapnest-gallery-1-hero`).
- Countdown is a small inline script (`data-otl-timer` = minutes, default 15), kept per tab in sessionStorage. Discount and check icons are inline SVG, no external images besides the photo.
- The original page also repeats the Product list + YES button at the very top on mobile. That's native Funnelish (mobile-only elements), not part of this block: The user keeps or removes it in the editor.
- Keys: `HEAD_DARK`, `HEAD_ACCENT`, `SUB`, `HERO_IMG`, `HERO_ALT`, `TIMER_LABEL`, `TIMER_TEXT`, `TIMER_MINUTES`, `PRODUCT_NAME`, `NOW_LABEL`, `PRICE`, `PRICE_UNIT`, `WAS`, `GET_HEADING`, `ITEMS` (list of `{TEXT}`, HTML allowed).

## Template notes (`oto-crosssell`, upsell-2)

- Upsell-2 sells **another product** that goes with the main one (hummingbird feeder → bird feeder & bath tray). Ask the user which product if he didn't say; pull its name, price, photo and one real review from that product's own `output/<other-sp>/2-sale-page/`.
- Layout = oto-classic with a different header and no hook/body: logo, "Wait… Your Order is Not Complete!" (`STOP_ACCENT` + `STOP_DARK`), `QUALIFIED` line ("Congratulations! You've qualified for a <u>special offer!</u>"), `OFFER_LINE` ("Get the <b>X</b> for only <b>$P</b> <s>$R</s>"), then offer column (name bar, Only NOW, price, pill, photo, **5-star customer quote** `QUOTE` + `QUOTE_NAME`) | BONUS TODAY column. Same design rules (price above the fold on mobile: demo at ~340px).
- Bonuses = what the funnel really delivers; Special Discount row = regular price → upsell-2 price.
- Every template starts with `<meta charset="utf-8">`: without it the local preview turns "…" and curly quotes into "â€¦".

