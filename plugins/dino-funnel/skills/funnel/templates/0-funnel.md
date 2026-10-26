# SteamJack Steam Grill Brush: funnel

<!-- Template for output/<sp>/0-funnel.md (filled example: SteamJack, 2026-10-26).
Copy it to output/<sp>/0-funnel.md and replace every value. Rules:
- Sections in this order: Funnel steps, Checkout bundles, Upsell / downsell products, Notes.
- Step numbers are fixed: 1 = pre-sale (1.1, 1.2 ... when several steps come before the sale page), 2 sale page, 3 checkout,
  4 upsell-1, 5 downsell-1, 6 upsell-2, 7 downsell-2, 8 thank you. Drop the rows of steps the funnel doesn't have, keep the numbers.
- Slugs: product slug = sale page slug without its template prefix; pre-sale `<product slug>-review`, checkout `-checkout`,
  upsells `-oto1` / `-ds1` / `-oto2` / `-ds2`, thank you `-thank-you`. Never add a number yourself.
- Bundle name = count + product noun, plural from 2 ("1 Brush", "2 Brushes", "3 Beds"), never "Pack 2".
  One row per bundle per color; Color = `-` when there is one color. Price = total, Price each = total / count.
  No compare-at column, no CDN links here (they go in 4-bundle/cdn-urls.md).
- Unknown value = `?`. Edit this file in place after every step; delete this comment. -->

## Funnel steps

| # | Step | Slug / URL |
|---|---|---|
| 1 | Pre-sale | `steam-grill-brush-review` |
| 2 | Sale page | `steamjack-grill-brush` |
| 3 | Checkout | `steamjack-grill-brush-checkout` |
| 4 | Upsell 1 | `steamjack-grill-brush-oto1` |
| 5 | Downsell 1 | `steamjack-grill-brush-ds1` |
| 8 | Thank you page | `steamjack-grill-brush-thank-you` |

## Checkout bundles (Funnelish product settings)

| Bundle | Color | Price | Price each | Badge | Image |
|---|---|---|---|---|---|
| **1 Brush** | - | $49.95 | $49.95/each | - | ![1 Brush](4-bundle/bundle-1.jpg) |
| **2 Brushes** | - | $79.90 | $39.95/each | MOST POPULAR | ![2 Brushes](4-bundle/bundle-2.jpg) |
| **3 Brushes** | - | $104.85 | $34.95/each | BEST VALUE | ![3 Brushes](4-bundle/bundle-3.jpg) |

## Upsell / downsell products

| Step | Slug | Product | Price | Variants |
|---|---|---|---|---|
| upsell-1 | `steamjack-grill-brush-oto1` | 1x SteamJack Steam Grill Brush | $29.95 | none |
| downsell-1 | `steamjack-grill-brush-ds1` | 1x SteamJack Steam Grill Brush | $24.95 | none |

Details: `5-upsell-downsell/funnelish-products.md`.

## Notes

Offer: Black Friday Early Access, up to 58% OFF + free gifts. Compare-at $83. Free gift = ebook, free shipping, 120-day guarantee. Bundle CDN URLs: `4-bundle/cdn-urls.md`.
