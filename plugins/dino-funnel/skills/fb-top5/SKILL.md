---
name: fb-top5
description: Full Facebook ad kit for a Top 5 / buyer's-guide funnel from just the pre-sale page link: 5 ad combos (headline + primary text), 5 filled 1:1 image prompts from the T5 template library, and the 5 images generated with Kie GPT Image 2.5 Flare, all saved to output. Use when the user types "/fb-top5 <link>" (or the old "/fb-top5-hlpt"), or pastes a topreviewking / topreviewqueen / any top-5 pre-sale URL and asks for "fb ads", "hlpt", "headline primary text", "combo fb ads", "ảnh ads fb", "ads cho trang top 5", "viết ads khớp presale". Flow is ads > pre-sale > sale page > checkout, so every combo links to the pre-sale page and only uses claims both pages agree on. Not for ads that go straight to a sale page (that's hlpt-salepage).
---

# FB Top 5

Input: **one link, the pre-sale page.** Optional: "chỉ copy" (stop after Step 6), "chỉ ảnh" (skip Step 5-6), an image count or T5 IDs.

Output:
- 5 combos, one per template (T01, T02, T04, T09, T11), saved to `output/<product>/5-ads/meta/fb-ads-top5-<YYYY-MM-DD>.md` and shown in chat.
- 5 image prompts + images in `output/<product>/5-ads/meta/img-top5/` (Meta = 1:1 only; horizontal Google images live in `5-ads/google/`): `00-prompts-top5-<YYYY-MM-DD>-1x1.md`, `refs.json`, `01.png`..`05.png`.

Talk to the user in Vietnamese. Ad copy in plain American English. Ask zero questions unless a page won't load.

## Step 1: Read both pages (what the visitor actually sees)

The live pages are the source of truth. The ad must match what someone sees after clicking.

1. `WebFetch` the pre-sale URL. Ask for verbatim: H1, subheadline, opening paragraphs, every pain/scenario, the full No.1 section (name, pros, cons, bottom line), one line per loser and why it lost, testimonials with names, offer/guarantee/stock lines, and **the exact href of the No.1 CTA buttons**.
   For the images (Step 7) also pull: site name (TopReviewKing / TopReviewQueen), the N checks and the "only one passed" line, each rival's grade and main con, and the 5 product image URLs in rank order (`/<slug>/assets/photo-1..5.webp` or `sc-1..5.webp`; `curl -sI` each, must be 200).
2. If the summary misses the href: `curl -sL <url> | grep -oE 'href="https://[^"]+"' | sort | uniq -c | sort -rn` and take the offer link that repeats.
3. `WebFetch` that href (the sale page). Ask for verbatim: hero headline + sub, benefit claims, specs, price/offer/gifts/shipping, guarantee, rating + review count, every testimonial with the name as printed, personas, limitations, urgency/stock lines.

No browser needed. Only if WebFetch fails on a page, use Playwright/Chrome to read it.

## Step 2: Local research (extra facts and what NOT to claim)

Product folder = pre-sale slug minus `-review` / `-review-N` (e.g. `window-bird-feeder-review` → `window-bird-feeder`). If `output/<product>/` doesn't exist, `grep -rl <slug> output/*/1-pre-sale-page/research.md` to find it. Read when present:

- `output/<product>/1-pre-sale-page/research.md`
- `output/<product>/2-sale-page/research.md`

Use them for "won't do" limits and do-not-claim notes (e.g. "never claim never falls", "not squirrel-proof"). A fact that's only in research.md and not on either live page stays out of the ad. Nothing local? Fine, carry on with the live pages.

## Step 3: Congruency check (before writing)

Compare pre-sale vs sale page on: product name, offer (BOGO / % off / gifts / free shipping), guarantee length, rating + review count, stock/urgency line, and whether the sale page sells the same product (a reused Funnelish step can show another one).

- Ads use only claims **both pages agree on**, or claims on the pre-sale page that the sale page doesn't contradict.
- Offer mismatch: say "today's deal" / "today's offer" in the ads, never the specific deal, and report it at the top of the reply so the user fixes the pages.
- Sale page sells a different product: stop and tell the user.

## Step 4: Avatars (auto, no questions)

Pick the top 2 avatars from: pre-sale opening and scenarios, sale-page persona list (first listed = main), testimonial contexts, the hero's pain. Give each a weight with 1-2 lines of evidence. Split combos ~3/2. Combo 5 bridges both.

## Step 5: Write the 5 combos

Invoke `copywriting` (or `direct-response-copy` if that's the one listed) first.

**Pull before writing:**
- Pre-sale H1 verbatim plus its frame phrase (the part naming the audience or promise). If the H1 is generic ("The Best X: A Buyer's Guide"), take the frame from the subheadline (e.g. "stays on the glass through a cold snap").
- The sale-page hero promise. At least one headline should echo it, so the promise carries through all three steps.

| Combo | Template | Shape | Headline pattern |
|---|---|---|---|
| 1 | T01 Testimonial → Benefit stack → Offer | Real quote, the pre-sale mechanism in 2-3 lines, 5 ✅ benefits, "not a gadget" positioning, guarantee | [Core benefit] that echoes the frame phrase |
| 2 | T02 Star review → Feature stack → Action CTA | ⭐⭐⭐⭐⭐ quote, sensory scene, "🔥 LIMITED:" line, 5 emoji features, seasonal hook | [Benefit outcome], [time/context] |
| 3 | T04 Problem callout → Solution → Effortless promise | 🚨 ALL CAPS pain line, empathy, the pre-sale failure mechanism, the fix, "literally never been easier" | Say Goodbye To [Problem 1] & [Problem 2]! |
| 4 | T09 Sensory → Social proof number → Feature stack | "Experience the..." scene, real review count, limited line, 3 emoji benefits, "you deserve..." | Top Rated [Category] [Year]! |
| 5 | T11 Personal story → Benefit stack → Trust | "After [X], I thought [belief]." / "The No.1 pick from [comparison] [reignited/brought back]..." / 3 outcomes / 5 emoji bullets, last one ends "Where A Meets B!" / 2 ✓ trust lines / soft CTA / "Try the No.1 pick risk-free today ([N]-day guarantee)!" | **No.1 [Category from pre-sale H1] [Year]** (mandatory) |

Every combo ends with a short CTA line + 👇, then the **pre-sale URL** bare on its own line. Use a different CTA per combo ("See which feeder ranked No.1", "See the full comparison", "Find which one passed all 4 checks"...).

## Hard rules

- **Link = the pre-sale URL**, never the sale page.
- **`No.1`, never `#1`** (markdown turns `#1` into a link).
- **No brand or product name** in headline or body. Category only ("the No.1 pick", "the feeder that ranked No.1").
- **Testimonials:** real ones from the live pages first, word for word, name exactly as printed (`— Hillary H.`). Need more? Write them per copywriting Draft mode, tagged `[FABRICATED]`. Never add "verified buyer", "happy customer", "real user" or "5-star reviewer".
- **Numbers:** page numbers first (review count, rating, guarantee days, number of products compared, number of checks). Anything else per copywriting Draft mode, tagged.
- Plain text only, no markdown links. Primary text 150-300 words, headline 5-8 words. Max 2 em dashes per combo (use periods).
- Pain-first tone in all 5. Don't name the pre-sale author.

## Step 6: Self-check, save, reply

Run on the draft before saving:

```bash
grep -nE '#[0-9]|verified buyer|happy customer|real user|5-star reviewer|\]\(http' <file>
grep -ni '<brand>\|<product name>' <file>        # must be empty
grep -c 'https://' <file>                         # = 5, all the pre-sale URL
```

Save to `output/<product>/5-ads/meta/fb-ads-top5-<YYYY-MM-DD>.md` (add `-2`, `-3` if it exists). In the file, each combo is `### Combo N — TXX: <name>`, then `**Primary Text:**` and `**Headline:**`, each followed by its copy inside a ```` ```text ```` fenced block (the user copies from the rendered preview, where plain lines merge: the ✅ list and the CTA line glue onto one line), then `**Notes:**` (1-2 lines: avatar + test role).

Show the combos in chat now (format in Step 9), then go straight on to the images. No waiting for approval.

## Step 7: Image prompts (5, 1:1)

Library: `${CLAUDE_PLUGIN_ROOT}/skills/assets/img-templates/top5-presale.md`. Read its rules (Luật dùng, esp. rule 8 Image Input), slot glossary, the "Tấm vẽ hàng hỏng" notes and the pre-post checklist before writing. Templates are drawn at 1:1, so use their layout as written.

Look at the 5 product images and write the lock lines first: one `[HERO]` sentence for ours (repeated verbatim in every prompt), one short physical line per rival, each rival a visibly different shape.

Default set:

| # | T5 | Mechanic |
|---|---|---|
| 1 | T5-5 | Same test on all 5, the visible **proof** shows the difference |
| 2 | T5-2 | 5 phone photos, grade sticky notes = the page's grades |
| 3 | T5-13 | Creator thumbnail, outcome hidden, "ONLY ONE PASSED ALL N CHECKS" |
| 4 | T5-18 | Person holds ours + the #2 |
| 5 | T5-31 | Dry-erase board "Ranked Best to Worst!", ? over each |

More images or named IDs: add from the library. A template that shows a failing product: lock who fails per the library's "Tấm vẽ hàng hỏng" notes.

- Truth sheet first (Huy 2026-10-20): before writing any prompt, our product needs `output/<product>/truth-sheet/<key>/sheet.png`; missing → make it with `product-truth-sheet` and get Huy's ok. Upload it with `cdn.py` (Kie result URLs expire) and put that CDN URL right before our real photo in every refs list (after the avatar if any). Each prompt names it: "The [Nth] attached image is a product truth sheet of our [CATEGORY SINGULAR] from several views; reproduce that exact product: [locked details]", where locked details = the counts and shapes from the sheet's identity paragraph.

Image Input = the library's rule 8: every prompt attaches all 5 product images (ours first, then the 4 rivals), plus the avatar first when a person is in the frame (the person on the destination page, e.g. the article author); `refs.json` is the same list for every prompt, with or without the avatar.

- Fill every slot, nothing in brackets left. Image copy comes from the pre-sale page only (its checks, its grades, its claims), plain American English, no em/en dashes.
- No brand, product name or our wordmark on any product. Rivals plain and unmarked, plus `each rival turned so that any printed lettering or brand name on its body is rotated fully away from the camera and is not visible`. The site name (TopReviewKing / TopReviewQueen) is allowed.
- Proof template (#1): state the difference as "the whole point of the photo and must be obvious", with ours' good state spelled out.
- Name the ratio in the `Create:` sentence ("Create: a 1:1 ...") and end every prompt with exactly `1:1 aspect ratio.`
- Prompt file: CRLF, prompts separated by a blank line, each starting `1. `, nothing else in the file. `refs.json` = `{"1": [urls...], ...}` per rule 8. Folder exists with older images → keep them, the gen script versions them.

## Step 8: Generate (Kie GPT Image 2.5 Flare)

```
python3 ${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/gen.py output/<product>/5-ads/meta/img-top5/00-prompts-top5-<YYYY-MM-DD>-1x1.md
```

Kie `gpt-image-2-5-flare-image-to-image`, 1K, `aspect_ratio: auto` (the prompt's 1:1 sets the frame), key `KIE_API_KEY` from `.env` at the working folder root, ~6 credits each, all 5 in parallel. Run `--dry` first to check prompt count vs refs. Each printed ratio must be ~1.00; a line with `ERR` or a ratio off 1:1 → fix that prompt and rerun it alone with `--only N` (the old file is kept as `NN-vK.png`).

Look at every image against the library checklist (exactly 5 products, distinct shapes, every character of copy correct, no brand/logo, fingers). A broken one → fix the prompt and `--only N` once; still broken → report it, don't loop.

The user asks for a redo later ("làm lại tấm 2, ..."): edit that prompt per his note, `--only 2`.

## Step 9: Reply

Reply in chat, in this order:
1. Mismatches from Step 3 (if any), one line each.
2. H1 / frame phrase / No.1 pick / 2 avatars, a few lines.
3. The 5 combos (copy-ready).
4. The images: one line each (`01.png` T5-5, ratio, ok / issue), total credits.
5. The saved paths: combos file, prompts file, image folder.
