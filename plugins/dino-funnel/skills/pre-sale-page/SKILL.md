---
name: pre-sale-page
description: Use when the user asks for a pre-sale page built from a saved template ("pre-sale page", "template top5 king", "pre-sale page theo khung top5-king", "clone trang topreviewking.com/hummingbird-feeder-review cho sp X", "lam presale top 5 theo template ...", "review page", "buyer's guide", "comparison lander", "trang review", "trang như topreviewking", "template top5-02", "khung trustedconsumerreview") for any product, wants to add a new page as a template, or just pastes an Amazon listing link (+ offer link) and wants the whole top 5 page done A to Z (research, review + photo harvest, things-that-matter, copy).
---

# Template Top5 King (pre-sale page)

Funnel: **ads → pre-sale page (this skill) → sale page on offer.dinosaurized.com (Funnelish) → checkout.** Pages are plain HTML + CSS, deployed through `topreviewking/`.

Each template is one file, `templates/template-<name>.html`: the frozen HTML of a winning live page, with a notes comment right after `<!DOCTYPE html>` (what to replace block by block, template-specific traps).

A new page = **copy the template HTML, keep every byte of `<head>` CSS and end-of-body scripts, swap only content** per that file's slot map.
Never rebuild the layout from scratch, never "improve" the CSS.

**REQUIRED BACKGROUND:** read *Strategy* below before writing copy. Copy itself: `copywriting` skill (invoke it every time, before writing any line).

Talk to the user in Vietnamese. Page copy in plain American English.

## Templates

| Name | Source | Format |
|---|---|---|
| `top5-king-1` (`templates/template-top5-king-1.html`) | topreviewking.com/hummingbird-feeder-review/ | Best X buyer's guide, 5 products, ours #1, sticky offer bar |
| `listical&quiz` (`templates/template-listical&quiz.html`) | offers.hike-footwear.com/l/li12 | First-person quiz listicle "I tried N X, only one worked": 11 steps shown one at a time (Next/Back bar, progress + counter), 4 competitors fail, ours wins, result page with offer. Media are `.ph` placeholders showing the original hotlinked as a reference (never ship it), fonts self-hosted (curl list in the notes) |
| `top5-personal-review` (`templates/template-top5-personal-review.html`) | thereviewboard.co (protein powders review) | First-person editor review "Best (and Worst) [X]": author box, photo strip, ranking list with stars, "How I Tested", one long card per product (specs table, verdict, pros/cons, What I Love / What Could Be Better). Source has 9 products (cut to 5 per the notes). Media keep the original `<img>` hotlinked + `data-ph` labels drawn by a template-only script |
| `top5-02` (`templates/template-top5-02.html`) | trustedconsumerreview.com (shared template of all its `/top-*`, `/top5-*` pages; frozen copy = top5-dash-cams) | "Top 5 [X] In [Year] Based On ...": scored top 5 table (#1 sale bubble + VISIT SITE, #2-#5 VIEW ON AMAZON, #4-#5 behind "See the rest"), BEST OVERALL box, then ONE long first-person review of #1 only (story, features, testing, verdict, scarcity, how to order, Q&A, price, IMPORTANT box), expert bio, sale popup. No competitor cards. Optional accordion + testimonial slider blocks. Its own copy rules are in the notes |

The user names the template. If he doesn't, ask which one. **Route by template:** each template's own rules (format, copy voice, slot map, assets, traps) live in its file's notes comment, and they win over anything below. The *Strategy*, *Comparison table* and *Cards* sections below are written for `top5-king-1` only; for `listical&quiz`, `top5-personal-review` and `top5-02` follow that file's notes and keep only the shared parts here (research, copywriting, hub copy checks, output, deploy/Funnelish).

**Reference pages (style to imitate, not templates to clone):** `refs/top5-choices/seamossreview.md` and `magnesiumreview.md`, text of top5-choices.com, the benchmark for top 5 pages (table that leaves one obvious choice, short competitor cards, tone, how #1's Bottom Line closes). Read both before writing any copy.

## Strategy

the user's proven winning format (live: topreviewking.com/hummingbird-feeder-review/, runs on Google Ads + FB). A third-party-voice buyer's guide: it teaches the reader the buying criteria, compares 5 real products against them, and ranks ours #1 because it is the only one that meets all of them.

### Why it wins (keep all of these)

1. **Opens on the problem, not the product.** The biggest pain from the reviews (*The pain points*), explained so the reader learns something by paragraph two (hummingbird: ports sit under the nectar, gravity makes it weep, the sticky film is the ant trail). The reader learns, so they trust the writer.
2. **Stakes beyond annoyance.** A section on what the problem actually costs (hummingbird: mold in the ports can give a bird a tongue infection and it starves at a full feeder). Emotional, specific, attributed to a credible group ("bird rehabilitators warn"). Verify the fact is real before using it.
3. **Rigged-but-true criteria.** Every factor is a real, defensible buying criterion, and ours is the only product that ticks all of them. If ours doesn't actually have a feature, it isn't a factor. The reader writes the verdict before the table.
4. **Honest cons for every competitor**, from public specs and their recurring complaints. Competitors get real pros too. This is what makes #1 believable.
5. **Our "cons" are scarcity in disguise:** "Only sold on the official site", "Sells out fast".
6. **Competitors link out to Amazon with BUY NOW** (real ASINs). Ours gets LEARN MORE → the offer page. Looks independent.
7. **Reader-only offer** on the final card and sticky bar ("For Readers of TopReviewKing Only"), deal taken from the offer page.

### Page blueprint (content order; the template HTML holds the layout)

- **H1:** `The Best [Category]: A Buyer's Guide`. **Dek:** one line naming the two biggest pains ("Which feeder the ants can't get into, and which one you end up scrubbing.").
- **IMPORTANT callout:** "If you're looking for a [category] that [solves the core pain], look no further. We compared five of the most popular [category] on the same N checks: [check 1] ... [check N]." + the hero image (generated real photo with a person, see *Steps* 2).
- **`#dangers`, why they fail:** pain one told step by step, then pain two. End on why people quit the category ("Not because it broke. Because it became a chore. That's exactly why we wrote this guide.").
- **What a bad one actually does:** 4 short sub-heads from annoying to dangerous. The last one is the design point that causes the others ("A feeder you can't open is a feeder you stop cleaning").
- **`#matters`:** see *Things that matter*. Each card ends with why the built-in/included version beats the add-on.
- **`#compare`:** see *Comparison table and ranking*.
- **Cards #1–#5:** see *Cards*. Each competitor opens on one identity line ("The best looking one here", "If cleaning is all you care about, this wins outright", "The one most likely to end up in the garage").
- **Final section "The #1 [Category]":** one-paragraph recap of the N checks, then the product card.

### Copy rules

- Third-person reviewer voice ("we", "most people"). Never "you should buy".
- Short sentences. Concrete verbs.
- Competitor claims: specs and recurring complaints first. Anything beyond that per copywriting Draft mode, tagged.
- Our quotes verbatim, names shortened.
- **Competitor prices on the page (any template): never the real Amazon price** (the user: Amazon = floor price, too low). Write a high but believable price, above ours.
- No health claims for people. Animal-welfare stakes are fine if attributable.
- No weapons in any image for outdoor products.

## Amazon link only → finished page (A to Z)

The user often gives just the Amazon listing (our white-label source) + the offer URL. Run the whole flow without asking step by step. Research files go in `output/<sp>/1-pre-sale-page/research/`.

1. **Listing facts** (logged-in Chrome, see *Amazon research*): title, brand, bullets, spec table, hi-res images → `research.md`.
2. **Review harvest** with `scripts/amazon-reviews.js` (aspects → gallery → full reviews, paste each function into chrome-devtools `evaluate_script`), dump to `research/reviews.json`, then `python3 scripts/reviews_to_csv.py research/reviews.json research <ASIN> research/themes.json`. Output: `amazon-reviews-<ASIN>.csv` + `amazon-review-images/` (photos only, never download videos, keep their m3u8 URLs in the CSV). Both stay local (gitignored: customer names, tens of MB); `research.md` records the counts and the path.
   Then **pick the reference photos**: PIL contact sheets (5×4, numbered, 5★ first) → look at every sheet → open the candidates large → write `research/review-image-picks.md` (grade A/B, what each is for, the `m.media-amazon.com` URL) and copy them to `amazon-review-images/_picks/`. Reject: defect shots, other products mixed into the gallery, visible white-label box/brand, images under ~800px, product too small in frame. The best A pick becomes `shot-1` (#1's in-use image).
3. **Things that matter** (rules below) from the theme counts + Amazon aspect counts.
4. **Competitors**: 4 organic Amazon best sellers, their specs + recurring complaints (aspect chips' negative counts + their ≤3★ gallery tiles).
5. **Copy**: invoke `copywriting`, read the two refs, then fill the template. Table + ranking per *Comparison table and ranking*.
6. **Build, check**, report what is still a placeholder.

Anything missing that doesn't block the page (rating/review count, coupon) → **don't stop**: put a visible placeholder `{{KHANG: <what>}}` (links: `href="#"`) and list every placeholder in the final message. Ask only when the answer changes the whole page (offer link missing, offer page sells another product).

## Things that matter (the `#matters` section)

The factors come from what **owners actually talk about**, not from what we guess:

1. Amazon's aspect chips ("Select to learn more": `Quality (955)`, `Ease of cleaning (326)`...) = mention counts over ALL ratings. Step 1 of `amazon-reviews.js`.
2. Theme counts on the harvested reviews (`themes.json`): one regex per theme for the category (clean, leak, sturdy, easy to fill, birds love it, ants...).
3. **Rank factors by mention count**, highest first, and say so in the section intro ("we counted what owners praised and complained about most, in order").
4. **One factor = one thing.** Never bundle two (no leak and ant moat are two factors). The count is whatever the data gives (5, 6, 7): add or remove `.need-item` blocks to match. The heading and every "N checks" mention on the page (IMPORTANT box, intro, conclusion) follow that number.
5. Drop factors owners barely mention, even if the template had them.
6. A claim on our listing can stay a factor and a #1 benefit even if some 1-2★ reviews disagree. Don't lecture about it.
7. Evergreen copy: never tie a factor to a season ("survives a summer" → "high-quality material that lasts").

## The pain points (`#dangers` / the intro story)

- Source = **4-5★ reviews, the sentences about their OLD product** ("my old one", "previous", "I've tried", "finally", "unlike my $20 one", "threw it out"). That is why people quit the category. 1-2★ reviews only tell what's wrong with *this* product, never use them as the category pain.
- Rank those pains by count, open the intro with the biggest one. Every pain sentence traces to real review lines; never keep the template's mechanism/story if reviews don't say it (hummingbird: the template said "it is almost never the birds", reviews said the #1 pain IS the birds not coming).
- **Keep the stakes section** ("What a bad [X] actually does…") even when reviews barely mention it: it is the deepest emotional lever.
- **The story carries through:** once the intro changes, re-align the dek under the H1, the IMPORTANT box and every competitor identity line to the same pains, and grep out the old story's words.

## Comparison table and ranking

- Rows = the factors (same order as `#matters`), plus value rows (capacity, size...). Columns in rank order. Unknown facts = `<td>N/A</td>`.
- **The table must leave ONE obvious choice** (ref seamossreview). A reader who only glances at it must not hesitate between #1 and #2:
  - #1 = ours, every ✓.
  - **At least 2 rows only #1 wins** (every competitor ✗). Build them from our real edge: a feature only we have, the guarantee, the bundle.
  - **#2 loses clearly:** at least 3 ✗. No close runner-up.
  - ✓ count strictly drops rank by rank; only #4 and #5 may tie.
  - **Not rigged-looking:** #4 and #5 keep at least 2 ✓ each (one ✓ looks biased).
  - **Every ✓/✗ row has at least 2 ✗** among the competitors. Never an all-✓ row.
  - These rules fight each other with few rows. If they can't all hold, **add a factual row** (a spec where weaker products legitimately win) first. Still short: set the ✗ needed per copywriting Draft mode and list each one in research.md as `[FABRICATED]`.
- **Rank strictly by ✓ count.** Ties: say so and let the user pick. When the order changes, move the whole card (`<section id="rank-N">`), renumber, keep grades by position (A+, B+, B, C+, C), reorder table columns, fix any sentence that names a position.
- Only **#1** keeps the in-use image (`.rc-shot`). Cards #2-#5: none.

## Cards

- **Competitor cards** (nobody scrolls to #2-#5 and re-checks the table), style = the refs: PROS 3 short labels (2-4 words), CONS 3-4 short labels, The Bottom Line 3-4 short paragraphs, **~80-100 words total**: one line of honest praise → "the main drawback is…" in plain words → why it sits at this rank ("we couldn't place it any higher than #2", "a decent pick at #3", "better than nothing"). Cons are informed by that competitor's own 1-3★ reviews; a small wording stretch so the card matches its ✗ is fine.
- **Never quote review stats or counts** in cards ("333 of 518 owners complain"): reviews are research, the card speaks in general terms ("the rubber parts tend to break down within a season").
- **#1 card:** PROS = longer benefit lines. The Bottom Line ~150 words, last paragraph = "Tap the LEARN MORE button below to see today's promo pricing" + the guarantee ("It comes with a 120-day money-back guarantee, so you have nothing to worry about"). Dinosaurized guarantee is ALWAYS 120 days (the user, 2026-10-05), never a placeholder.
- **Conclusion bullets = short labels** (2-5 words, Title Case: "Comes Fully Apart to Clean", "Leak-Free Seal", "120-Day Money-Back Guarantee"), one per table row the #1 wins, guarantee included.

## Inputs

| Field | How Claude gets it |
|---|---|
| Template | only one exists → use it, else ask |
| Product specs | the Amazon listing (real browser, `document.body.innerText`; WebFetch only sees Amazon's JS) |
| Product name | **propose 3 names, the user picks** (see *Product name* below). The offer page title is only for specs, not the name |
| Brand | Dinosaurized unless the offer domain says otherwise (the `by …` line) |
| Offer line for the sticky bar | the deal on the offer page (BOGO, % off) |
| Slug | `<category>-review`, e.g. `window-bird-feeder-review` |
| 4 competitors | Amazon search: top organic best sellers (skip sponsored, skip white-label twins of ours) |
| Rating / review count | **never from the Amazon listing** (those reviews are the white-label seller's). Omit `.rc-rev` and the star count line unless the user gives a real number |
| Hands-on testing | The user tests for real (2026-10-05): write it as hands-on ("we tested five ... on the same N checks", table note "our own testing"). Don't argue it |
| Site | `topreviewking.com` (`public/`), `topreviewqueen.com` (`public-queen/`) or **Funnelish** (offer.dinosaurized.com, Custom HTML block): The user says which, ask if he doesn't (it changes links, assets and the publication name). Queen = swap every `TopReviewKing`/`TopReview<b>King</b>` for Queen (logo, seal, spo-line), deploy per `CLONE-RUNBOOK.md` *Deploy len topreviewqueen.com*. Funnelish = see *Hosting on Funnelish* |

### Product name

After research, before building, give the user **3 names in one table**, ranked, #1 recommended, and wait for his pick (the user 2026-10-07). Columns: `# | Name | Meaning | Why it stands out | Risk`. No intro line before the table.

- **A coined word, not a description.** Wordplay or a picture tied to where it's used or the #1 win: `Pawsenger` (paw + passenger, front seat cover), `Shotgun` ("riding shotgun"), `Barnacle` (grips like one, no slide). Plain names ("StayPut Seat Cover", "Quilted Waterproof Cover", "PawGuard") are too ordinary: The user rejected them.
- **No "Dino" prefix.** Full name = `<Name> <Category>` ("Pawsenger Front Seat Cover"); the table column and concl-lead use the bare `<Name>`.
- **Risk column:** words Meta/Google ads may flag (gun, kill, drug…), names likely taken on Amazon/USPTO, odd connotations.

Stop and ask only for what blocks the page: offer link missing, or the offer page is down **or sells a different product** (open it and read the title; a reused Funnelish step can show another product). If the user says "dùng tạm", build with it and flag it in research.md.

**First, check this product isn't already done:** `grep -rl <ASIN> output` (plus `topreviewking/docs topreviewking/public` when that folder exists). A hit means a research doc or page exists; ask the user whether to rebuild or update it.

## Output

Output is grouped by product: everything for one page goes in **`output/<product>/1-pre-sale-page/`** (paths are relative to the working folder root); the same product's sale page lives in `<product>/2-sale-page/` and single-file outputs (image prompts, ad copy) sit straight in `<product>/`. A second pre-sale page for the same product gets its own folder named by template, e.g. `1-pre-sale-top5-king-1/`.
The **deploy slug** is the public URL, so it never says "presale". Put it in the HTML asset paths (`/<slug>/assets/...`) and at the top of research.md.

```
index.html          the page
assets/             fonts/ (curl from the live page, URL in the template), photo-1..5, shot-1, lineup, spo-prod (.webp)
research.md         spec table, aspect + theme counts, sources, ✗ per column, placeholders
research/           reviews.json, themes.json, amazon-reviews-<ASIN>.csv, amazon-review-images/, review-image-picks.md (local only)
image-prompts.md    the hero (lineup) prompt + Image Input table; the image itself is generated, see *Steps* 2
```

Deploying (copy to `topreviewking/public/<slug>/` without `research/`, PR to `main` per `CLONE-RUNBOOK.md`) is a separate step, only when the user asks. No `topreviewking/` folder in the working folder: zip the page folder without `research/` and tell the user to send it to Huy, who deploys it.

### Hosting on Funnelish (Custom HTML block)

The user pastes the whole `index.html` into a Funnelish Custom HTML block (same as `sale-page`). Learned on bird-feeder-review-2 (2026-10-09):

- **Every CTA = `href="#next-step"`, never a bare offer URL** (the user). Funnelish routes it to the next funnel step and keeps the URL params, so the click-ID script has nothing to do.
- **Publication name is not TopReviewKing/Queen** on a dinosaurized page: use a niche name (e.g. `We Love Birds`).
- **All media + fonts on the Dino Shopify CDN** (relative `/<slug>/assets/...` paths 404 there): upload with `stagedUploadsCreate` → POST → `fileCreate`, swap paths for the CDN URLs. Script: `scripts/cdn_upload.py <page_dir> <slug> <file-prefix>` (only re-uploads changed files, writes `<page_dir>/cdn-map.json`; build the page with local paths first, then swap each `/<slug>/assets/<rel>` for its `url` when the file's sha1 still matches).
- **Drop `/tags.js` and the favicon links** from `<head>` (topreviewking-only; Funnelish has its own pixels/favicon).
- **Class clash:** Funnelish's `core.min.css` styles `.main-wrapper` as a centered flex column with `min-height:100vh`, and its row is capped at 1170px. Templates that use `.main-wrapper` (listical&quiz) shrink the header to its text. Append inside the page's `<style>`: `.section_row:has(.page-wrapper){max-width:none!important}` and `.page-wrapper>.main-wrapper.publisher{display:block;min-height:0}`. Check other templates for the same class names before pasting.
- **Sticky footer spacing (listical&quiz):** the user settled on `.page-wrapper .af-section{padding-bottom:70px}` (64 too tight, 76/88 too tall).
- Verify on the live URL in a background tab (inject CSS there to test a fix) before telling the user to re-paste.
- **Speed (listical&quiz, one step visible at a time):** steps 2-11 get `style="display:none"` in the HTML (the quiz script reveals them; without it every lazy image sits near the fold and loads at once); only step-1 avatar + hero are `loading="eager"` (hero `fetchpriority="high"` + `srcset` 720/800/1080 via Shopify `&width=`), every other `<img>` `loading="lazy"`, warmed 1.5 s after `load`; pair-slot images `&width=700`; videos `preload="none"` + `data-poster`, played by an IntersectionObserver, Shopify 480p rendition. bird-feeder-review-2: 3.9 MB → ~0.75 MB at open. When measuring, use never-loaded URLs: memory-cached images ignore `loading="lazy"` and look like eager loads.
- **Colors = the checkout's colors** (the user 2026-10-09, full congruency, not just the buttons): curl the next step's checkout, take its button orange / dark (bird feeder: `#E75201` + `#252A32`) and apply them to header bar, progress segments, sticky footer buttons, every CTA, sale badge, headline accents. Override with `!important` rules appended to `<style>`.
- **Brand names in Title Case** in copy (Sweetfull, not SWEETFULL), even when the Amazon listing shouts.

## Amazon research (logged-in Chrome)

- Use the **chrome-devtools MCP** (user scope). It drives the user's real Chrome, already logged in to Amazon. If it says *Could not find DevToolsActivePort*: open `chrome://inspect/#remote-debugging` (`osascript -e 'tell application "Google Chrome" to open location "chrome://inspect/#remote-debugging"'`), ask him to flip the switch, and wait on `~/Library/Application Support/Google/Chrome/DevToolsActivePort` instead of asking him to report back.
- Work in a new background tab (`new_page` with `background: true`). Never touch his other tabs.
- **Reviews: don't bother with `/product-reviews/` or `/portal/customer-reviews/`**, both stop at 8 and ignore every filter. Use `scripts/amazon-reviews.js` (photo/video gallery, up to 250 tiles ≈ 170 reviews with full text).
- First hit can be a "Continue shopping" interstitial: click `button[alt="Continue shopping"]`, then reload the listing.
- Specs: `#productTitle`, `#bylineInfo` (brand), `#feature-bullets`, rows of `table tr` (dimensions, material, capacity).
- **Complaints with counts:** click each "Customers say" aspect chip and read `N customers mention X, P positive, Q negative` from `document.body.innerText`. Loop all chips in one `evaluate_script`.
- Hi-res images: `fetch('/dp/<ASIN>')` from an amazon.com tab and regex `"hiRes":"(https:[^"]+)"`. The `#altImages` thumbnails are only ~500px.
- No good review photo for `shot-1`? Fall back to the "Videos for this product" strip: `#vftphero img.bpy-rv-panel-img` srcs, strip the `._CR..._SR..._` suffix, pick a customer-shot frame (skip added text, influencer faces, other products).
- Competitors: search `amazon.com/s?k=<category>`, rank organic results (no `[Sponsored]`) by review count and "bought in past month". Skip twins of ours (same design, different brand).
- Look at each listing's images (contact sheet) before writing ✓/✗: many specs are only visible in photos.

## Steps

1. Read `templates/template-<name>.html`. Research (above) → `research.md`.
2. Images: main listing image → `photo-N` 720x720 on white; `shot-1` 900x720 (5:4) from the review pick, cropped without other products; `cwebp -quiet -q 80`.
   **Hero image under IMPORTANT (`lineup.webp`, 1440x810) = a REAL-looking photo, GENERATED, never a placeholder and never a collage of listing images** (the user has said this many times). Every page ships with it:
   - **Always generate TWO options and let the user pick** (the user 2026-10-07). Don't ship either until he chooses; show both with their paths.
     - **A. Comparison** (`research/lineup-gen.png`): rules from `refs/hero-lineup-prompt.md`: one candid phone photo, 5 products staggered in depth, ours center and only slightly forward, a "proof" item in front of each, setting fits the category, 5500K daylight, no text. A person in the shot (friendly owner framed waist-up behind the products, smiling at camera, natural skin; for pet products their pet on/with ours). `refs/hero-lineup-ref.webp` = the no-person look, for products-only only if the user asks. Input = the 5 hi-res listing URLs.
     - **B. Outcome** (`research/outcome-gen.png`): only ours, in use in the real place it's used (car seat cover → fitted on a car's front seat; feeder → hanging in a yard with birds), the user (and pet) visibly happy with it, ours clearly readable in frame. Same candid-phone-photo, 5500K, no-text rules. Input = ours' hi-res listing image + 1-2 real customer review photos of it fitted/in use (from `research/review-image-picks.md` / `amazon-review-images/`, same color as the offer, no other brands visible), so the fit looks real.
   - In `image-prompts.md`: both prompts, each with its **Image Input table** (rank/role, product, hi-res URL, local file) in the order the prompt references them. Each prompt = **one paragraph in one fenced code block**.
   - Generate both: Kie.ai `gpt-image-2-5-flare-image-to-image` (GPT Image 2.5 Flare, hub default), `input_urls` = the URLs from that option's table, `aspect_ratio` `16:9`, `resolution` `1K`, key `KIE_API_KEY` from `.env` at the working folder root: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/product-truth-sheet/scripts/sheet.py <out.png> <prompt.txt> <url1> <url2> ... --ratio 16:9` (client `${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/kie.py`, python3 needs `requests`). Save to the option's PNG path and look at each (A: 5 products recognizable, ours center; B: ours fitted right and readable, happy faces; both: no text/garbled logos). Bad result → fix that prompt and regenerate. Show the user both; the one he picks gets center-cropped to 16:9, `cwebp -q 80` → `assets/lineup.webp`.
3. Build `index.html` from the template file with a script: drop the notes comment after `<!DOCTYPE html>`, keep everything else before `<body>` (only the path prefix and `<title>` change) and everything from the sticky-bar script comment on, byte for byte; generate the body between them. Reuse the template's svg snippets (PROS/CONS icons, ✓/✗ cells, checklist circles) by regex. Assert in the script that head and tail are unchanged.
4. Fill every slot per the template's slot map. Competitors: `BUY NOW` → Amazon with `target="_blank" rel="sponsored nofollow noopener"`. Ours: `LEARN MORE` → offer.
5. Run the checks.

## Checks before calling it done

- The template's leftover grep returns nothing, offer-link count matches.
- `grep -nE '—|–|&mdash;|&ndash;' index.html` is empty.
- `grep -n '{{KHANG:' index.html` → every hit is listed in the final message.
- Table: count ✓/✗ per column and per row against *Comparison table and ranking*.
- **Voice = contractions everywhere** (it's, don't, can't), like the refs. Never mix both voices on one page. American spelling (`mould→mold`, `colour→color`, `neighbour→neighbor`, `centre→center`).
- **Say each list once.** The N checks appear in the IMPORTANT box and the conclusion only; the intro just says "five [X], N checks, only one passed all N".
- **Short paragraphs:** body copy (intro, `.bc-card`, The Bottom Line, competitor cards) = 1-2 sentences, ≤ ~40 words per `<p>`. Exceptions kept as one block: each `#matters` item, centered section intros, a single list sentence.
- **Copy self-check:** run `copywriting`'s *The test* on every new sentence (would a person say this to a friend?). Banned: reviewer bios, "one owner…" / "owners report…" / "owners routinely…", sentences about reviews instead of the product, clichés, anything that sends the reader off the page ("search the reviews", "check Amazon"). `grep -niE "one owner\b|owners report|routinely|out of the air|search the reviews|test lab|complaining|owners who" index.html` must be empty.
- `assets/lineup.webp` is the generated photo the user picked (A `research/lineup-gen.png` or B `research/outcome-gen.png`), not a packshot row.
- Preview: asset paths are `/<slug>/assets/...` but the local folder is `<product>/1-pre-sale-page`, so serve a temp root: `mkdir -p /tmp/pv && ln -sfn "$PWD/output/<product>/1-pre-sale-page" /tmp/pv/<slug> && python3 -m http.server -d /tmp/pv <free port>`, open `/<slug>/?gclid=test`. At 375px and 1280px: no horizontal scroll, no broken images, offer links carry `gclid`. Sticky bar: test with `scrollTo({top, behavior:'instant'})`, it must be off at the top, on after `#rank-1`, off at `#winner`. 404s for `/tags.js` and favicons are expected locally. **Leave the server running and put the clickable `http://127.0.0.1:<port>/<slug>/?gclid=test` link at the top of the final message** so the user can check it himself.

## Adding a new template

1. Get the live page's HTML (`curl -sL <url>`). No product images, no fonts in the skill: fonts are curled from the live page at use time.
2. Write `templates/template-<name>.html` in the same shape as `template-top5-king-1.html`: the full page HTML, with a notes comment right after `<!DOCTYPE html>` holding global replaces, slot map with original sizes, do-not-touch, assets, leftover grep, traps.
3. Add a row to the Templates table above.
