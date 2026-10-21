---
name: img-to-template
description: Reverse-engineer any image into a reusable text-to-image template prompt AND save it to one of two growing, numbered libraries: SALE PAGE ads (Alex Cooper 40, SP-41+ added) or TOP 5 PRE-SALE PAGE ads (40 Top 5 templates, T5-41+ added). Use whenever the user provides an image (file path, attachment, or URL) and asks for a "prompt", "template prompt", "prompt for this image", "recreate this", "add this to the templates", "làm template từ ảnh này", "viết prompt cho hình này", "thêm vào bộ template", or wants to clone / adapt the image's style for different content. Also use when they ask to see, pick from, or reuse the saved templates. The output is a single self-contained prompt with positional layout in %, [PLACEHOLDER like example] slots for any swappable element (copy, colors, products, subjects), camera/lighting spec where photographic, and aspect ratio at the end. Tool-agnostic (works in any modern text-to-image model) and product-category agnostic: one template must work for any product range, followed by a per-category fill table.
---

# img-to-template

Takes one image and produces ONE template prompt: a reusable blueprint anyone can fill with their own copy / colors / product / subject. Then saves it to the right library under the next free number, so both libraries keep growing.

## Two libraries — never mix them

| Library | File | For | IDs |
|---|---|---|---|
| **Sale page** (Alex Cooper 40) | `../assets/img-templates/sale-page.md` | Ads for ONE product, driving to its sale page | SP-01..SP-40, new: SP-41+ |
| **Top 5 pre-sale page** (40 Top 5) | `../assets/img-templates/top5-presale.md` | Ads driving to a Top 5 / buyer's-guide page: the frame shows several products and the "compare before you choose" mechanic | T5-01..T5-40, new: T5-41+ |

Always say the ID with its prefix (SP-13, T5-13) so the two #13s never get confused. Don't pull templates from both libraries into one campaign.

Which library a new image goes into:
- **Top 5** = several *different* products (different brands/makers) placed together to be compared: lineups, rankings, grids, report cards, "I tested them all".
- **Sale page** = one product is the subject. Several units of the *same* product (colorways, bundle, multi-pack) is still sale page; so is one product vs a single generic "them".
- Not sure which → ask the user ("Ảnh này làm template cho sale page hay top 5?") before writing. Don't guess.

You are NOT writing a description of the image. You are writing a **production blueprint**. The source image's copy and brand must NOT be baked in; they become slots.

**Category-agnostic (load-bearing).** One template must work across any product range (hats, flashlights, dog food, supplements, ...). The template copies the ad's **mechanic** (the persuasion device), never the source's product type. If the source shows supplement bottles, the words "bottle", "cap", "capsule", "label" must not appear outside a slot. A template that only works for the source's category has failed.

## Files

| File | Read when |
|---|---|
| `../assets/img-templates/sale-page.md` | Sale-page images. Index (number, name, stage) at the top, full prompts below. |
| `../assets/img-templates/top5-presale.md` | Top 5 images. Its own rules, slot glossary (`[HERO]`, `[RIVAL 1..4]`, `[POSE]`, `[PROOF ITEM]`...), fill table, then templates 1–40, then batch notes. New Top 5 templates must use its slot names. |
| `references/style-guide.md` | Before writing: voice rules, placeholder grammar, % layout, camera language, common pitfalls. |
| `../assets/img-templates/sources/` | Source image of each new template, named by ID (`SP-41-<slug>.jpg`, `T5-41-<slug>.png`). |

## Method (run in order)

### Step 1 — Get the pixels

Attached image or local path: read it directly. URL: download with curl; if the host blocks plain fetches (Notion, some CDNs), screenshot it in a browser, or ask the user to attach it. Never write a template from an image you haven't seen.

### Step 2 — Pick the library, check for duplicates

Decide sale page or Top 5 (table above), then read that library's templates. If the image's mechanic is already a template (same persuasion device, same layout logic; a different product doesn't make it new), say which number and ask whether to save it as a variant anyway. A different layout of a known mechanic is a new template; note "variant of #NN" in its tag.

### Step 3 — Analyze the image

Look at the actual pixels and answer ALL of these.

**Ad mechanic (answer first, in one sentence)**
- What is the persuasion device, stripped of the product? e.g. "competitor lineup + same-kind proof in front of each + red circle on the winner", "creator points at a ranking whiteboard over a lineup".
- If each product shows its own evidence, what is the **proof**: the one thing a buyer would put side by side to compare (capsules in a cap → kibble in a scoop → sweat on a paper towel → a flashlight's light pool)? It becomes a `[PROOF like ...]` slot, and how the hero's proof looks better becomes a `[WIN like ...]` slot. If the hero wins by position or lighting alone, there is no PROOF/WIN; slot whatever carries the category instead (foreground prop, setting).

**Layout & composition**
- Aspect ratio: measure it, don't guess.
- How is the frame divided? (Top X% / Bottom Y%, Left / Right, full-bleed, diagonal, radial, grid)
- Where does the eye land first? Is there a clear hero element?

**Photography / rendering style** (if relevant)
- Studio / lifestyle / UGC-iPhone / flatlay / editorial / illustration / 3D
- Lighting, lens feel, depth of field, color grade

**Typography**
- Headline weight, family, case, italic? Subhead, body, pull-quote?
- Special treatment: highlighter fills, hand-drawn underlines, oversized caps

**Color system**
- Background type, 1–3 dominant colors, accent / CTA color, contrast direction

**UI / trust elements**
- Stars, verified badges, review or comment cards, press logos, customer counts, platform screenshots (Reddit / X / iOS Notes / Facebook), seals, pills, banner bars

**Copy elements**
- Read every word literally: headline, sub-copy, callouts, stats, CTA, fine print, logo placement. Each becomes a slot with that wording as its example.

**Subject / props / setting**

### Step 4 — Write the prompt

Read `references/style-guide.md` and calibrate against the closest templates in the chosen library. Top 5 templates follow `top5-presale.md`'s own conventions (its slot names, its rules section). Skeleton:

```
[Reference instruction if applicable]. Create: [shape of the image] [on a <BACKGROUND> / set in <SETTING>]. <Layout using top X% / bottom Y% / left / right / center>. <Photography: lens, lighting, depth of field>. <Typography for each text block>. <UI / trust elements>. <Mood>. <Aspect ratio>.
```

**Reference-instruction line**, by source type:
- Designed / studio: `Use the attached images as reference. Match the exact <subject / product> design, colors, and typography precisely.`
- UGC / native: `Use the attached images as reference for <subject / product> color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's <Story / Reddit screenshot / iPhone selfie / mirror photo>.` The "do NOT polish" line is load-bearing; without it the model defaults to glossy output.
- Tone only: `Use the attached images as reference for visual tone ONLY.`
- No reference needed: omit the line.

**Placeholder rules** (what makes it reusable):
- Every copy, color, prop and subject element is a `[SLOT like "example from the source"]`. The example anchors the model; a bare `[HEADLINE]` gives generic output. Pure structural slots (banner positions, divider lines) need no example.

**Category-agnostic wording**:
- Outside brackets use only generic nouns (`product`, `competitors`, `proof`, `logo`, `packaging`) and neutral verbs (`opened or used`, `facing the camera`, `logo visible`). Category nouns (bottle, bag, kibble, beam, brim) live only inside slot examples.
- Keep layout positions fixed across categories. If one category's proof wouldn't fit the spot, pick a proof that does (flashlight: the light pool on the counter in front of it, not beams on a far wall).
- Don't write `no readable text` / `no legible text` / `no logos`: the model can't scope the ban and erases the product's own label. Say `plain unmarked` for objects that shouldn't carry text; banning *added* layers (`no added graphics, captions or badges`) is safe.

**Camera lines** sound like a real photographer: `Shot on 50mm f/2.8`, `85mm f/2.0, shallow depth of field, warm bakery lighting`, `iPhone 15 quality, slightly grainy, kitchen lighting, no professional setup`.

**Closing line** is always the open aspect ratio slot, alone, with a period: `[ASPECT RATIO] aspect ratio.` No example ratio inside it: the ratio is chosen at gen time, never fixed by the template. Never write "square" / "vertical" for the frame itself; the slot decides. Record the measured source ratio outside the prompt as "Drawn at 4:5." (see Step 6). Describe layout as zones (text band, product row, photo area) in %, so "Aspect ratios" below can re-flow it.

**Length**: 80–280 words, matched to the image's density: every distinct element gets a slot, nothing padded.

### Step 5 — Sanity-check

- Every text element in the source has a `[PLACEHOLDER like "example"]` slot; no baked-in copy.
- Last sentence is `[ASPECT RATIO] aspect ratio.`; nothing else names the frame shape.
- Layout in % or clear positional terms.
- Lens or "iPhone quality" if photographic.
- Brand colors are `[COLOR like ...]` slots, not the source brand's color names.
- UGC / native: "do NOT polish" present.
- **Category swap test:** reread every word outside brackets: does it still make sense for a hat, a flashlight, dog food, a supplement? Anything that breaks → move it into a slot or make it generic.

If any check fails, rewrite before saving.

### Step 6 — Save to the library

Next number = highest number in that library + 1.

**Sale page** (`../assets/img-templates/sale-page.md`):
1. Append to the end of the file, same shape as the existing entries:
   ```
   ## 41. <Short Name>
   **Archetype tag**: <mechanic in one line>. Source: `sources/SP-41-<slug>.<ext>` (or the URL), added <YYYY-MM-DD>. Drawn at <measured ratio>.

   > <the template prompt, one paragraph>
   ```
2. Add its row to the index table: number, name, stage (Cold scroll-stop / Cold problem-aware / Warm proof / Warm comparison / Hot offer / Feature / education).

**Top 5** (`../assets/img-templates/top5-presale.md`): insert right after the last numbered template and before `## Ghi chú drift`, same shape as the existing entries:
````
### 41 — <Short name>

Source: `sources/T5-41-<slug>.<ext>` (or the URL), added <YYYY-MM-DD>. Drawn at <measured ratio>.

```
<the template prompt, one paragraph>
```
````
If it needs a slot not in the glossary, add a row to the glossary table.

Both: copy the source image to `../assets/img-templates/sources/<ID>-<slug>.<ext>` when you have the file. Skip if only a URL.

If the user only wants a one-off prompt and says not to save, skip this step.

## Output format

Return the prompt as a single fenced code block, then a short **fill table**: one row per slot that carries the mechanic (SURFACE/SETTING, PRODUCT CATEGORY, PROOF, WIN, ...), one column per category. Default columns: Hat / Flashlight / Dog food / Supplement, unless the user names their own range. For Top 5, use that file's fill-table columns instead. Close with one line saying where it was saved ("Saved as SP-41 (sale page) — Warm comparison." / "Saved as T5-41 (Top 5)."), and, if there is a PROOF slot, the question that finds it for a new product ("what would a buyer put side by side to compare?"). No other breakdown unless asked.

## Using saved templates

When the user asks for a template by number, name or stage ("cho mình template 13", "mấy template warm proof", "template top 5 số 2"), return it from the right library as is, slots intact. A bare number with no library named is ambiguous: ask "SP hay T5?" unless the context (sale page vs Top 5) already says. Only fill slots when the user gives the content to fill them with.

When filled prompts for a product are saved to a file, they go in `output/<product>/5-ads/meta/img-<sp|top5>/` (Meta, 1:1; a horizontal ratio for Google goes in `5-ads/google/img-<sp|top5>-<ratio>/`), the same folder as the generated images (`01.png`, `02.png`… numbered like the prompts), named `00-prompts-<sp|top5>-<YYYY-MM-DD>-<ratio>.md` (e.g. `00-prompts-top5-2026-10-02-9x16.md`; the `00-` keeps it sorted above the images): one paragraph per prompt, each starting with its number (`1. Use the attached…`, `2. …`) so it can be found by number, CRLF, separated by a blank line. Nothing else in the file. One file per ratio. No ratio named → 1:1, don't ask (ad images default to 1:1; other ratios only when the user names them). Next to it, `refs.json` = `{"1": [urls...], ...}`; for Top 5 the list follows that library's rule 8 (all 5 product images, ours first, plus the avatar first when a person is in the frame).

**Hand-off after gen** (Huy 2026-10-20): copy every generated image to `~/Downloads/<product>-ads-<sp|top5>/` (Google ratios: `~/Downloads/<product>-ads-<sp|top5>-<ratio>/`) named `<product-short>-<sp|top5>-NN.png`, `open` that folder, then run `funnel_view.py <product>`. Separate from `~/Downloads/<product>-images/`, which holds bundle images only.

## Aspect ratios

Ratio is never fixed by a template: `[ASPECT RATIO]` is filled at gen time, default 1:1. Every template works at any common ratio: 1:1, 4:5, 5:4, 9:16, 16:9, 1.91:1 (also 2:3, 3:2, 4:3). Its "Drawn at" note (Top 5: all 1:1) is only the ratio its % layout was written for. **At the drawn ratio, use the layout as written** (9:16 only adds the safe zones). At any other ratio, re-flow it: keep every element, every word of copy and the mechanic, and rewrite every % *and every position word* ("divided vertically", "center top", "top-right cell", "two columns", "portrait tiles", fixed eye heights) for the new frame. Name the ratio in the `Create:` sentence ("Create: a 9:16 native ranking ad, ...") and at the end. If the template has an **Other ratios** note, it overrides the rules below.

**Close to the drawn ratio (1:1 ↔ 4:5 ↔ 5:4)**: keep the layout, nudge the % so nothing crowds.

**Tall (9:16, 2:3)**:
- Safe zones: text, faces and the hero stay inside 14–80% height (Stories / Reels UI covers the rest). Backgrounds, rivals and props may run into the margins; corner items (logo, URL, handle, disclaimer, ticker) move to a corner at about 74–80%.
- Left/right splits → stack top over bottom (left goes on top), but only if each stacked half stays no wider than 2:1; otherwise keep them side by side. A divider becomes horizontal and anything "on the divider" (VS burst, pill over the seam) moves with it.
- Tables keep their columns at every ratio; only row height changes.
- A row of 4+ products with nothing paired to them → two rows, the front row the larger half (5 → 2 behind + 3 in front, 6 → 3 + 3, 7 → 3 + 4). The hero keeps the template's slot: center → front-center, first → front-left, unmarked → an ordinary front spot, never singled out.
- Products that each carry their own proof, tag, note, grade or triangle → **never stagger**: keep one row (overlap is fine) or use a 2-column grid of product-over-proof pairs. Sequences (wear stages, meters, rankings left to right) always stay one row.
- Grids: 2x2 stays 2x2; 5 cells → 2 + 2 + 1 with the last cell full width; 3x2 → 2x3; 4x2 → 2x4. Rewrite any per-cell order (grades, names) row by row. "On the seam between rows" = the 50% line. Each cell's subject and text sit inside 14–80%.
- A person in a narrow side column → centered, chest up, head at the top of the photo zone, below any text band (never overlapping it), everything inside 14–80%.

**Wide (16:9, 1.91:1, 3:2)**:
- Top-to-bottom bands → text panel left 35–40%, visual right 60–65%. Keep bands full width instead when the only text is a short pill, sticker or one-line band (max 20–25% height).
- Product rows: one row, each product about 12–16% of the width. If 5+ products won't fit the visual panel at that size, the row becomes a full-width bottom strip (max 30% height) under the text and visual.
- Grids: a 2x2 whose cells hold one object → 4 across; a 2x2 whose cells hold two things (product + result, product + note) stays 2x2. 3+2 → 5 across; 3x2 and 4x2 stay; drop "portrait" from tile descriptions.
- A person in a top or left zone → left or right third, chest up, unless the action needs the full body. Overlays (post cards, captions) sit beside the face, never on it.
- 1.91:1 is short. A full-width headline gets at most 2 lines; a headline over ~8 words goes in a full-width top band, 2 lines, max 25% height. Body copy (reviews, comments, manifestos, stat sentences, captions) keeps every word: widest column available, up to 6 lines, two columns past 10 lines.

**Every ratio**: size type as "as large as fits its zone's width", never as "% of frame height". A person's whole head stays in frame (eyes about a third down their zone) unless the template asks for a crop. Count products after re-flowing: "five" is still five.
