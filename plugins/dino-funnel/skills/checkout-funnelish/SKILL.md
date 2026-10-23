---
name: checkout-funnelish
description: Fill the two social-proof blocks that go on a Dinosaurized Funnelish checkout page, a Facebook-style comments block (3 comments) and a Trustpilot-style review grid "Don't Take Our Word For It!" (6 cards), using the product's Amazon review photos and review text. Use whenever the user asks for "checkout", "trang checkout", "fb comments", "comment facebook", "review grid", "trustpilot reviews", "điền template checkout", "làm 2 template checkout", "review cho checkout" for a product, or once a sale page is done and the funnel's next step (checkout) needs its proof blocks. Not for the sale page reviews (that's sale-page) or the top-5 pre-sale page (pre-sale-page).
---

# Checkout proof blocks (Funnelish)

Two Custom HTML blocks the user pastes into the Funnelish checkout step. Talk to the user in Vietnamese; the block copy is plain American English.

| Template | What it is |
|---|---|
| `templates/fb-comments.html` | 3 Facebook comments, 480px wide. Comment 1 has a 3:2 photo under the bubble, 2 and 3 are text only. Avatar 40px circle. |
| `templates/reviews-trustpilot.html` | orange header, 5 stars + "4.8/5 Based on 18,736+ reviews" (brand constants, keep), 6 cards in a 3-column grid (1 column on mobile): square photo, stars + name, text, "Posted on Trustpilot". |

Don't edit the templates. Everything product-specific lives in one `content.json`, and `scripts/fill.py` writes both files from it.

## Output

`output/<product>/3-checkout/`:

```
content.json             names, texts, photos, avatars (the only file you write by hand)
fb-comments.html         generated
reviews-trustpilot.html  generated
```

## Workflow

### 1. Source material

The review harvest from the pre-sale step: `output/<product>/1-pre-sale-page/research/reviews.json` (id, name, stars, title, body, images = Amazon URLs) and the downloaded photos in `research/amazon-review-images/<N>star_<id>_<k>.jpg` (`_k` = position in `images`). No harvest yet: scrape the listing's reviews first the way the pre-sale-page skill does.

Also read `output/<product>/2-sale-page/index.html` so you don't reuse the reviewers already shown there.

### 2. Pick the reviews

Build a contact sheet of the 4-5 star photos (ffmpeg crop to square, `tile=`) and look at it before choosing:

- **Photos first.** A hummingbird (or the product) in real use beats the product on a kitchen counter. Cards with the best photos go first in the grid.
- **Check the photo shows THIS product.** Amazon merges variants into one review gallery. A review can be for a sister variant (a seed feeder under a hummingbird feeder listing). Drop it even if the text is great.
- Comment 1 needs a photo that still reads at 3:2. Comments 2 and 3 can be photo-less reviews with a strong line (emotional story, objection handled).
- No reviewer appears twice across the sale page, the comments and the grid.
- Keep real names exactly as written, any format ("Jen Murdock", "Amanda", "Sydney W."): the mix of formats is what makes it look real. Replace only names that don't read as a person: handles, usernames, initials-only, "Amazon Customer" (CC → "Christina C.", SL1026 → "Sarah L.", spychic → "Stephanie P."), keeping the original initials where they fit. Also replace a name whose gender clashes with the text or the comment avatar ("Alex P" writing "my husband's car" → "Alexis P.").

### 3. Even out the length

the user's rule: the Trustpilot cards must read about the same length. One 250-word wall next to an 11-word line looks fake and breaks the grid.
Comments are the opposite (Huy 2026-10-23): three comments of the same length look scripted. Mix them: one short (10-20 words, a quick reaction, an emoji is fine), one long (55-75, a little story), one in between (25-40). The photo comment can be the short one.

| Block | Words per item |
|---|---|
| Trustpilot cards | 35-70, aim 45-65 |
| FB comments | one 10-20, one 25-40, one 55-75 (`fill.py` warns when the shortest and longest are under 30 words apart) |

- **Too long:** keep the reviewer's opening line and voice, keep the 2-3 strongest specifics (what problem it fixed, the feature they loved, a tip), cut the rest.
- **Too short:** keep their words and add 1-3 sentences in the same voice. Take the additions from what other buyers of the same listing say (voice of customer in `reviews.json` and the research aspect counts), and only claim what the listing supports. Small human details (where it hangs, coffee, the grandkids) are fine.
- Keep a small honest gripe if the review has one. It's what makes the block believable.
- Fix typos, no em dashes, contractions welcome.

### 4. Avatars

Comments need 3 avatars. Pick from `../assets/avatars/index.md` (who each one is + its Shopify CDN URL), matching the name, and not the one used as the sale page hero avatar. Put the CDN URL straight into `content.json`, no copying or upload.

### 5. Fill

Write `content.json`:

```json
{"comments": [{"name": "J.D.", "avatar": "https://cdn.shopify.com/.../dino-avatar-NN.webp", "photo": "<amazon url>", "photo_alt": "...", "text": "..."},
              {"name": "...", "avatar": "...", "photo": null, "text": "..."}, {...}],
 "reviews":  [{"name": "...", "photo": "<amazon url>", "alt": "...", "text": "..."}, ... 6 items]}
```

Run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/checkout-funnelish/scripts/fill.py output/<product>/3-checkout/content.json`. It prints `WARN` for any text outside the word ranges or containing an em dash. Fix those and rerun. Output is pure ASCII so emoji survive the Funnelish paste.

### 6. Check

`curl` every Amazon photo URL (expect 200), serve the folder with `python3 -m http.server` on a free port, and look at both files in Playwright: grid at 1280px, comments at 480px. No broken images, card lengths look even. Then `open` both files for the user.

### 7. Hand over

Reply in Vietnamese: the two file paths, a table of who's in each block (name, one-line gist, photo), word counts, and the reminder that Amazon photo links must be uploaded to Shopify and swapped before pasting into Funnelish.
