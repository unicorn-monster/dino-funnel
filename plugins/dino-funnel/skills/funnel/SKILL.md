---
name: funnel
description: Run the whole Dinosaurized funnel for one product, step by step, from an Amazon link: pre-sale top 5 page → flip to win → sale page → checkout proof blocks → bundle images → FB ads for the top 5 page. Use when the user types "/funnel <amazon link> [offer link]", asks to "làm funnel", "làm trọn bộ", "làm từ đầu tới cuối cho sp này", "tiếp tục funnel sp X", "funnel tới bước nào rồi", or asks what the next step is for a product.
---

# Funnel (the whole chain for one product)

`ads → pre-sale (top 5) → flip to win → sale page → checkout`. Each step is its own skill; this one runs them in order, stops for the user's approval between steps, and picks up where a product left off. Talk to the user in Vietnamese, short.

## Inputs

- **Amazon link** of the product we sell (white-label source). Required.
- **Offer link**: the Funnelish sale page URL (offer.dinosaurized.com/...). Ask once if missing; the pre-sale page can be built with a `{{KHANG: offer link}}` placeholder meanwhile.
- **Where the pre-sale page goes**: topreviewking.com, topreviewqueen.com or Funnelish. Ask once.
- Colors sold, offer (BOGO, % off, gifts): read them from the offer page, ask only what isn't there.

## Where things live

All paths are relative to the working folder root (run everything from there). `output/<sp>/` per product. `<sp>` = the product folder, named `<YYYY-MM-DD>-<product>` with the date the product was started (`2026-10-23-oriole-feeder`, Huy 2026-10-23: dated so they sort oldest → newest). A new product: create it with today's date; never rename an existing one. `<product>` (short kebab-case: `cat-bed`, `oriole-feeder`) without the date is what goes into `~/Downloads/<product>-…/` folders, file names and slugs. `funnel_view.py` accepts either name:

```
0-funnel.md          funnel map (slug of every step) + Funnelish product settings (bundles, price, price each, compare at, badge, variants, upsell/downsell products): the ONLY copy, edit it in place after each step. Sits at the product root so Huy can take it out (2026-10-23); bundle previews link `4-bundle/<file>`
0-brief/0-product-brief.md   claims, USP, offer, colors, links, names chosen: read first, update after each step
0-brief/truth-sheet/<key>/   product-truth-sheet kit (truth.md + sheet.png), one folder per product incl. rivals (was 0-truth-sheet/, merged into 0-brief/ 2026-10-23)
1-pre-sale-page/     pre-sale-page
flip-to-win/         flip-to-win
2-sale-page/         sale-page
3-checkout/          checkout-funnelish
4-bundle/            bundle
6-ads/meta/          fb-top5
funnel/              flat copy to review in order: python3 ${CLAUDE_PLUGIN_ROOT}/skills/funnel/scripts/funnel_view.py <sp>
funnel/0-funnel.md   older products only (no root 0-funnel.md yet): their original funnel map, funnel_view.py keeps it
```

**Step numbers** (`0-funnel.md` and the files in `funnel/`, Huy 2026-10-20): step 1 = everything before the sale page, numbered 1.1, 1.2 ... in the order a visitor walks them when there is more than one (several pre-sales, then flip to win); the sale page is always 2, checkout 3, upsell-1 4, downsell-1 5, upsell-2 6, downsell-2 7, thank you page 8 (Funnelish TYP, Huy 2026-10-23). `0-funnel.md` sections, in this order (Huy 2026-10-23: funnel steps first): *Funnel steps* (# / step / slug or URL only, no where/status columns: Huy 2026-10-23), *Checkout bundles* (one row per checkout bundle per color: name = count + the product noun, plural from 2 (`1 Feeder`, `2 Feeders`, `3 Beds`, `2 Traps`; never `Pack 2`, Huy 2026-10-23), color (Huy 2026-10-22; `-` when there is one color), price, price each like `$14.98/each`, badge (no compare-at column, Huy 2026-10-23), image preview `![](4-bundle/<file>)`) (no Variants line, no CDN link list: those live in `4-bundle/cdn-urls.md`, Huy 2026-10-23), then *Upsell / downsell products* (slug, product, price, variants; no image column, Huy 2026-10-23). Unknown = `?`. **Template + filled example: `${CLAUDE_PLUGIN_ROOT}/skills/funnel/templates/0-funnel.md`**: copy it to `output/<sp>/0-funnel.md` when the product has none, then replace every value. Asked for the table alone ("làm 0-funnel.md cho sp X"): fill what the product folder already has (slugs from the pages, bundles from `4-bundle/` + the sale page offer, OTO prices from `5-upsell-downsell/`), `?` for the rest.

**Slugs:** the sale page slug is Huy's (template prefix allowed, e.g. `10r-calming-dog-bed`); product slug = it without the prefix. Pre-sale `<product slug>-review`, checkout `<product slug>-checkout`, upsells per `upsell-downsell` (`<product slug>-oto1` / `-ds1` / `-oto2` / `-ds2`), thank you page `<product slug>-thank-you`. Never add a number yourself: the `-1` / `-2` on live slugs is Funnelish's own suffix. Until Huy creates the sale page, write the proposed product slug (e.g. `gourdian-fruit-fly-trap`) and replace it with the real one once it exists.

## Steps

Start by listing `output/<sp>/` and telling the user which steps exist and which is next. Then, for each missing step:

| # | Skill | Needs | The user does after |
|---|---|---|---|
| 1 | `pre-sale-page` | Amazon link, offer link, site | picks product name + hero image; TRK/TRQ: sends the page folder to Huy to deploy (or deploys via `topreviewking/` if that folder exists); Funnelish: pastes `index.html` |
| 2 | `flip-to-win` | offer + gifts from the sale page | pastes into a Funnelish step placed right before the sale page |
| 3 | `sale-page` | Amazon link, offer | pastes `index.html` into Funnelish; sends generated images back for `IMAGE NEEDED` slots |
| 4 | `checkout-funnelish` | review harvest from step 1 | pastes the 2 blocks into the Funnelish checkout |
| 5 | `bundle` | offer options, colors | puts the CDN URLs on the checkout options |
| 6 | `fb-top5` | the LIVE pre-sale URL | uploads the 5 combos + images to Meta |

Invoke each step's skill and follow it fully: its checks are part of the step. After each step: update `0-brief/0-product-brief.md` (what was decided: name, offer, gifts, links) and `0-funnel.md` (slugs, bundles, prices), run `funnel_view.py <sp>`, give the user the result + what they must do (column above), and ask before starting the next step. The user can skip or reorder steps (flip to win is optional; ads can wait for the page to be live).

## Rules for every step

- **Ads link to the pre-sale page** whenever the funnel has one (`<product slug>-review`), never straight to the sale page, whatever template library the images come from (SP or T5) (Huy 2026-10-23, repeated: "không thì làm pre-sale page để chơi à"). Only a funnel with no pre-sale links ads to the sale page.
- **Truth sheet first:** `output/<sp>/0-brief/truth-sheet/<product-key>/sheet.png` must exist before any step generates an image (`product-truth-sheet` skill); no sheet yet → make it before going on, whatever step you're in.
- Images: Kie GPT Image 2.5 Flare only (`${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/gen.py` for prompt files, `product-truth-sheet/scripts/sheet.py` for a single image), 1K, ad images 1:1 unless told otherwise; a ratio the model lacks → `auto`. Key = `KIE_API_KEY` in `.env` at the working folder root.
- Images that end up on a Funnelish page go to the Dino Shopify CDN: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/cdn.py <file>...`.
- Don't comment on claims, compliance, review counts or ratings: a lawyer reviews everything before it's published, and numbers the user gives are real.
- `~/Downloads/<product>-bundle-img/` holds bundle images only; other uploads stay in `output/`.
- Python scripts run with `python3` (needs `requests` + `Pillow`). A tool is missing (`shopify`, `cwebp`, `ffmpeg`, Chrome MCP): the plugin user runs `/dino-funnel:funnel-setup`.
