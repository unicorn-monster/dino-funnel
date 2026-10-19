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

All paths are relative to the working folder root (run everything from there). `output/<sp>/` per product, `<sp>` = short kebab-case product name (`cat-bed`, `bug-zapper`):

```
0-product-brief.md   claims, USP, offer, colors, links, names chosen: read first, update after each step
1-pre-sale-page/     pre-sale-page
flip-to-win/         flip-to-win
2-sale-page/         sale-page
3-checkout/          checkout-funnelish
4-bundle/            bundle
5-ads/meta/          fb-top5
funnel/              flat copy to review in order: python3 ${CLAUDE_PLUGIN_ROOT}/skills/funnel/scripts/funnel_view.py <sp>
```

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

Invoke each step's skill and follow it fully: its checks are part of the step. After each step: update `0-product-brief.md` (what was decided: name, offer, gifts, links), run `funnel_view.py <sp>`, give the user the result + what they must do (column above), and ask before starting the next step. The user can skip or reorder steps (flip to win is optional; ads can wait for the page to be live).

## Rules for every step

- Images: Kie GPT Image 2.5 Flare only (`${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/gen.py` for prompt files, `product-truth-sheet/scripts/sheet.py` for a single image), 1K, ad images 1:1 unless told otherwise; a ratio the model lacks → `auto`. Key = `KIE_API_KEY` in `.env` at the working folder root.
- Images that end up on a Funnelish page go to the Dino Shopify CDN: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/cdn.py <file>...`.
- Don't comment on claims, compliance, review counts or ratings: a lawyer reviews everything before it's published, and numbers the user gives are real.
- `~/Downloads/<sp>-images/` holds bundle images only; other uploads stay in `output/`.
- Python scripts run with `python3` (needs `requests` + `Pillow`). A tool is missing (`shopify`, `cwebp`, `ffmpeg`, Chrome MCP): the plugin user runs `/dino-funnel:funnel-setup`.
