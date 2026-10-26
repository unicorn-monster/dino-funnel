---
name: bundle
description: Make the bundle images for a Dinosaurized checkout's pack selector (1 pack, 2-3 packs, BOGO 1+1 / 2+2, pack + free gift), one set per color, 500x500 on white, uploaded to the Dino Shopify CDN. Use when the user asks for "bundle", "ảnh bundle", "ảnh gói", "ảnh BOGO", "bogo 1+1", "ảnh pack cho checkout", "bundle cho màu X", or the funnel reaches the bundle step after checkout. Not for ad images (fb-top5) or flip-to-win prize images.
---

# Bundle images (checkout pack selector)

Funnelish checkout shows one image per offer option. Each image = cutouts of the product composed on white, 500x500. Talk to the user in Vietnamese.

Done examples (look at one before starting): `output/2026-10-16-cat-bed/4-bundle/` (BOGO, 4 colors, JPG), `output/2026-10-14-bug-zapper/4-bundle/` (1-4 packs, tall product side by side), `output/2026-10-05-window-hummingbird-feeder/4-bundle/` (BOGO + gift with a red +).

## Steps

1. **Which images.** Read the offer: `output/<sp>/0-brief/0-product-brief.md` if present, the sale page offer box (`output/<sp>/2-sale-page/index.html`, `research.md`) and what the user says about the checkout. List one image per option × color, e.g. `bundle-1-<color>`, `bogo-1-1-<color>`, `bogo-2-2-<color>`, `bogo-3-3-gift`. Send the list, wait for an OK.
2. **Packshots per color.** One clean white-background photo per color, front-facing, no props, no text: the Amazon listing's variant images (`"hiRes"`, see pre-sale-page *Amazon research*), or the AliExpress / supplier variant photo. Save to `output/<sp>/4-bundle/src/<color>.jpg`. Gift images (ebook mockup, a small item) go in `src/` too.
3. **Cut out** each: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/flip-to-win/scripts/cutout.py src/<color>.jpg src/cut-<color>.png --max 1000` (`--seed x,y` for white holes inside the product). Composite one on a dark background and look at it: no white halo, no grey floor shadow left.
4. **Compose** with `python3 ${CLAUDE_PLUGIN_ROOT}/skills/bundle/scripts/compose.py src/cut-<color>.png <name>.jpg --layout <layout> [--gift src/cut-gift.png]`:

   | Option | Layout |
   |---|---|
   | 1 pack | `one` |
   | 2 packs / BOGO 1+1 | `row2` for tall products (lanterns, bottles), `diag2` for flat or wide ones (beds, feeders) |
   | 3 packs | `tri3` (tall) or `row3` |
   | 4 packs / BOGO 2+2 | `diamond4` |
   | 6 packs / BOGO 3+3 | `stagger6` |
   | + free gift | add `--gift` (products left, red + , gift right) |

   Doesn't look right (items too far apart, overlapping a key detail): pass a custom layout `"x,y;x,y"` in units of the item's own width/height, back to front. `python3 compose.py --selftest` checks the script.
5. **Approve one color first.** Make every option for one color, show them, wait for the user's OK, then run the same commands for the other colors.
6. **Funnel table**: write one row per option × color into the *Checkout bundles* table of `output/<sp>/0-funnel.md` (bundle name, color, price, price each, badge, image preview). No `0-funnel.md` yet: copy `${CLAUDE_PLUGIN_ROOT}/skills/funnel/templates/0-funnel.md` first (format rules in its comment).
7. **Upload**: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/cdn.py output/<sp>/4-bundle/*.jpg --prefix bundle-<sp>` and write the printed URLs into `output/<sp>/4-bundle/cdn-urls.md` (file → URL, per option and color).
8. **Hand over**: copy the final images to `~/Downloads/<product>-bundle-img/` (bundle images only there; Huy 2026-10-26: folder named `-bundle-img`, e.g. `grill-brush-bundle-img`), `open` that folder, run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/funnel/scripts/funnel_view.py <sp>`, and reply with a table: option, color, file, CDN URL.

## Rules

- JPG, 500x500, white background, ~40-50 KB. File names `<option>-<color>.jpg`, kebab-case, color names as the store spells them.
- Same layout for every color of an option, so the selector looks consistent when the buyer switches color.
- No text, badges or prices in the image: Funnelish shows those next to it.
- **Items never overlap** (Huy 2026-10-20: overlapped packs are hard to read/count). Use a spaced grid with a ~0.12 gap in item units: 2 = `0,0;1.12,0`, 4 = `0,0;1.12,0;0,1.12;1.12,1.12`, 6 = 3x2, 8 = 3-2-3 (`0,0;1.12,0;2.24,0;0.56,1.12;1.68,1.12;0,2.24;1.12,2.24;2.24,2.24`). The built-in `diag2` / `diamond4` / `stagger6` overlap: only use them if the user asks.
- The product in the image must be the color that option sells.
