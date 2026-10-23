---
name: flip-to-win
description: Build a Flip to Win / "Pick a Card" game step for a Dinosaurized Funnelish funnel (9 gift-box cards, visitor flips 4 prizes, Continue goes to the sale page). Use when the user asks for "flip to win", "pick a card", "trang lật thẻ", "game quà", "trang flip cho sp X", or sends a flip-to-win page (Gruns, Earth Breeze, Javvy) to copy for a product. Output is one Custom HTML file pasted into Funnelish.
---

# Flip to Win (Funnelish step)

One self-contained HTML file the user pastes into a Funnelish Custom HTML block, on a step placed directly before the product's sale page. Talk to the user in Vietnamese; the page copy is English.

Template: `templates/flip-to-win.html`. Layout is earthbreeze.com/pages/p/flipper-08-27-26, copy is gruns.co/pages/flip-to-win-v2, card face is a Javvy-style 3D gift box recolored Dino orange. First built for bug zapper: `output/2026-10-14-bug-zapper/flip-to-win/index.html`.

## Steps

1. **Read the offer.** `output/<sp>/0-brief/0-product-brief.md` if it exists, plus the sale page's `research.md` (offer, bonuses, free-shipping rule) and the checkout bundles. Done when you can name what the buyer actually gets on the next two steps.
2. **Pick 4 prizes**, in flip order. Every prize is something the sale page and checkout really deliver, worded the same way: a visitor who "won" Free Shipping and then sees "free shipping on 2+" feels cheated. Default slots: 1 = the hero (product image + "Get 1 Free" when there is a BOGO bundle, otherwise the discount), 2 = Free Shipping (fixed in the template), 3 and 4 = digital bonuses (ebook mockups) or a small physical gift. Send the list to the user and wait for an OK.
3. **Make the prize images**: transparent PNG/WebP, max 400px. Product: cut a white-background packshot with `scripts/cutout.py` (`--seed x,y` for white holes enclosed by the product), then composite it on a dark background and look at it. Ebooks: generate a mockup with Kie GPT Image 2.5 Flare (`python3 ${CLAUDE_PLUGIN_ROOT}/skills/product-truth-sheet/scripts/sheet.py <out.png> <prompt.txt> <ref url> --ratio 1:1`), then cut it out the same way.
4. **Upload every image to the Dino Shopify CDN** with `python3 ${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/cdn.py <file>... --prefix ftw-<sp>` (prints each CDN URL; needs the `shopify` CLI logged in to the Dino store). A fresh file can 404 on the CDN for a few seconds: re-check with curl before using it. Done when every `img` in the page is a `cdn.shopify.com/s/files/1/0267/4255/4668/` URL.
5. **Fill the template** into `output/<sp>/flip-to-win/index.html` (one file: it previews in a browser and is the paste). Replace every `{{...}}`; done when `grep '{{' index.html` prints nothing.
6. **Verify in Chrome** (chrome-devtools MCP, local `python3 -m http.server`) at 390px mobile and 1440px desktop: flip one card, press the button, counter reads 4/4, "Continue" appears, every prize image has `naturalWidth > 0`, tapping a card or Continue lands on `#next-step`.
7. **Hand off**: `pbcopy < index.html`, tell the user to paste it into one Custom HTML block. Launch checks for the user on Funnelish: the flip step sits directly before the sale page (`#next-step` follows step order), and the step's SEO title is updated (cloned steps keep the old page's title).

## What the template already handles

- **Full-bleed**: Funnelish wraps blocks in a 1170px `section_row`; `.ftw` escapes it with `width: 100vw; margin-left: calc(50% - 50vw)` plus `html, body { overflow-x: hidden }`.
- **Routing**: the Continue button is a static `<a href="#next-step">` (Funnelish intercepts it and sends the visitor to the next step); after the game, tapping any card clicks that link.
- **Fixed assets on the Dino CDN**: logo `dino-logo.webp`, card face `flip-giftbox.png` (orange box, cream ribbon), Free Shipping icon `flip-free-shipping.png`. Source files for the gift box: `output/2026-10-14-bug-zapper/flip-to-win/gen/`.
- **Palette**: navy `#0f2557` title and counter, Dino orange `#E75300` button and won-card border, cream `#FFF1E6` page wash and won-card fill.

Images taken from another brand's page (icons, reference shots) are re-hosted on the Dino CDN before they go into the page, so the live page never depends on a competitor's CDN.
