---
name: sale-page
description: Build a complete Dinosaurized product sale page (the long offer page that sends buyers to checkout, pasted into a Funnelish Custom HTML block) from just an Amazon product link, using a saved template. Use this whenever the user gives an Amazon link and asks for a "sale page", "trang bán hàng", "offer page", "làm sale page cho sp này", or wants a page like offer.dinosaurized.com/matt-6-26-bird-feeder-2 for a new product, even if he doesn't name the template. Also use it to add a new sale-page template. Not for top-5 / buyer's-guide pre-sale pages (that's pre-sale-page).
---

# Sale page

Turns one Amazon link into a finished sale page: researched facts, direct-response copy, a content JSON, and a built HTML file ready to paste into Funnelish. Talk to the user in Vietnamese; the page copy is plain American English for older blue-collar US men (and their wives, depending on the product).

## Templates

Each template is one file in `templates/`: the full page HTML to copy, with notes on how it's filled.

| Name | Source | What it is |
|---|---|---|
| `origin` (`templates/template-origin.html`) | offer.dinosaurized.com/matt-6-26-bird-feeder-2-1791173375647585 | pixel clone of the Funnelish bird-feeder page: top bar + logo, gallery hero + bullets + testimonial + accordions, 3 alternating feature rows, 3 "perfect for" cards, offer + 3 bonus rows, guarantee, FAQ, 3 reviews, sticky bar. Plain HTML file, every image is a `div.m` placeholder (drop an `<img>` inside it) |

Default = `origin` (the user 2026-10-07; the old `locket` template was removed 2026-10-19): use it unless the user names another template, don't pick one yourself. For `origin`, the finished `output/window-hummingbird-feeder/2-sale-page/index.html` shows the filled shared slots (logo, rating bar, payment icons, stars, Trustpilot, 120-day badge, bonus badges) to reuse. **Read the whole template file before writing anything**: its copy is also the reference for tone and length.

## Output

Output is grouped by product: `output/<product>/` (relative to the working folder root) (kebab-case, e.g. `window-bird-feeder/`) holds `1-pre-sale-page/`, `2-sale-page/`, `3-checkout/` (pages get a folder) and all ads in `5-ads/`: `meta/` (1:1 only: copy `fb-ads-*.md` + image folders `img-<sp|top5>/` with their `00-prompts-*.md`) and `google/` (horizontal images + Demand Gen asset sheets). Everything for this page goes in `output/<product>/2-sale-page/`. Below, `<slug>` means `<product>/2-sale-page`:

```
index.html          the page: what the user pastes into Funnelish
research.md         facts, sources, open questions, what to confirm before going live
image-prompts.md    one prompt per missing image
assets/             generated images the user sends back (<product-short>-<slot>.webp)
```

Nothing is deployed. The user pastes `index.html` into Funnelish himself.

## Workflow

### 1. Check it isn't done already

`grep -rl <ASIN> output` and check `output/` for the same product. If a page exists, ask the user: rebuild or update?

### 2. Research the Amazon listing

The listing is the white-label source of the product we sell. It's the only input, so read it thoroughly in a real browser (Playwright; WebFetch only sees Amazon's JS):

- First load can be a "Continue shopping" interstitial: click `button[alt="Continue shopping"]`, then reload.
- `#productTitle`, `#feature-bullets` (clothing listings have no such block: use `#productFactsDesktopExpander`), the spec rows in `table tr` (dimensions, material, capacity, what's included).
- "Customers say" aspect chips: click each and read `N customers mention X, P positive, Q negative`. Positives tell you what buyers love (headline material). Negatives tell you the objections to answer and the honest limitation for the Straight Talk callout. These are other sellers' customers: use them for insight, never quote them as our reviews.
- Images: `fetch('/dp/<ASIN>')` and regex `"hiRes":"(https:[^"]+)"`. Look at every image (contact sheet) to see features the bullets don't mention and to assign images to slots. Download them into `output/<slug>/_listing/`, never a shared folder like `/tmp` (another run can overwrite the files and you end up judging the wrong product). Delete `_listing/` when done.

Write `research.md`: product facts table, what it will NOT do, aspect counts, proposed product name, open questions.

### 3. Write the copy

Invoke the `copywriting` skill (or `direct-response-copy` if that's the one listed) before drafting. Copy the template HTML to `output/<slug>/index.html` and replace the content inside `<body>` block by block, following the template's section playbook. Keep `<head>` and `<style>` untouched. Problem first, concrete specs, one honest limitation, short sentences.

Why the facts discipline matters: this goes on a real brand page that takes money. A claim the product can't back is a refund and a chargeback. So every spec and feature comes from the listing; anything uncertain goes to research.md as "confirm", not onto the page.

### 4. Images

Use the listing's hi-res Amazon URLs directly in `index.html` so the page is complete when the user opens it. Assign by what each image shows (hero = product in use, sections = the feature they discuss). Images with another brand's logo or text baked in: still usable for preview, but list them in research.md as "replace before live". Slots no listing image fits: the template's `IMAGE NEEDED` box, and a prompt for each in `image-prompts.md` (one fenced code block per prompt, one paragraph, 1:1, bright background, literal text only, no borders), labelled with where it goes on the page.

In research.md, remind the user: Amazon image links can break, re-upload them to Shopify before the page goes live.

**Review photos (Trustpilot cards) = real customer photos.** Ours from the white-label Amazon listing or AliExpress reviews. If our product differs from the Amazon reference (no real photo of ours exists), take the reference product's review photos and gen-swap our product in (same method and files as the PDP mosaic, see `pdp-carousel` Rules), never a fully generated scene.

**Testimonial avatars:** pick one from `../assets/avatars/index.md` (who each one is + its Shopify CDN URL; match the reviewer and the buyer) and use the CDN URL directly as the `src`. Already on Shopify, so it stays out of the upload pack.

**Image file names.** Every image file Claude saves or hands over is named `<product-short>-<slot>.<ext>`, kebab-case, describing where it sits on the page: `window-feeder-hero-woodpeckers.jpg`, `window-feeder-dimensions.jpg`, `window-feeder-who-retired-man.webp`, `window-feeder-review-1.jpg` (reviews numbered in page order). Never `who-1.webp`, never an Amazon ID like `71gUrhqayQL._AC_SL1500_.jpg`. These names end up in Shopify Files, so they have to be readable there.

**When the user sends generated images** for an `IMAGE NEEDED` slot: `cwebp -quiet -q 82 -resize 800 0` into `output/<slug>/assets/<product-short>-<slot>.webp`, swap the box for `<img src="assets/..." alt="..." loading="lazy">`, and update the missing-images note in research.md. A relative `src` won't load once the page is pasted into Funnelish, so it gets swapped for the Shopify URL along with the rest.

**Upload pack** (when the user asks for the images to upload to Shopify): download every distinct `src` in `index.html`, plus the files in `assets/`, into `~/Downloads/<slug>-images/`, rename each one as above, `open` the folder, and reply with a table: file → where it's used on the page. When he sends back the Shopify URLs, replace every `src` (Amazon and `assets/`) with them.

### 5. Check

Check: every CTA is `href="#next-step"` (`grep -c 'href="#next-step"' index.html`), no `div.m` placeholder text left, no `—`/`&mdash;` in new copy. Then open `index.html` in the user's browser (`open`) and look at it yourself at 375px and 1280px (Playwright via a local `python3 -m http.server`): no broken images, no layout overflow, and every CTA goes to `#next-step`.

For a live Funnelish funnel, confirm the immediate next Funnelish step is Checkout. `#next-step` follows funnel order, so the HTML can be correct while a misplaced step still sends buyers to the wrong page. If the funnel is unavailable, add this as a launch check in `research.md` instead of claiming the routing is verified.

### 6. Hand over

Reply in Vietnamese: the `index.html` path, the proposed product name, what needs confirming (offer bonuses, name, any "confirm" facts), how many images are still missing.

## Adding a new template

1. Get the page's clean HTML (the source the user pasted, or `curl -sL <url>`; Funnelish serves it minified with unquoted attributes, so prefer the original source).
2. Write `templates/template-<name>.html` in the same shape as `template-origin.html`: the full page HTML, a notes comment at the top, every image a `div.m` placeholder. Non-ASCII characters inside `<style>` become CSS escapes (`\2713 `).
3. Add a row to the Templates table above.
