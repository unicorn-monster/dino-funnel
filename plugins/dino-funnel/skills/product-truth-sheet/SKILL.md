---
name: product-truth-sheet
description: Product truth kit for one product (ours or a rival): a truth.md with the counted Details line + real-photo refs, and a labelled 3:4 continuity sheet (profile + spec table, turnaround FRONT / 3/4 / SIDE / BACK, six close-ups, DO NOT CHANGE block), plus a second "worn / in use" sheet for anything worn or mounted. Every image or video of the product is generated from it. Use before any step generates an image of a product that has no `output/<sp>/0-brief/truth-sheet/<key>/truth.md` yet, when Huy asks for a "truth sheet", "sheet sản phẩm", "character sheet cho sản phẩm", "bộ chuẩn sản phẩm", or when generated images/videos get a product's details wrong (port count, shape, parts, how it is worn).
---

# Product truth sheet (bộ chuẩn sản phẩm)

One kit per product, built once, read by every skill that generates an image or video of it, so the product looks the same and correct everywhere. Method from Ori Silver's *Character Sheet Playbook* and AI_GOAT's character continuity sheet (x.com/0xAIGOAT/status/2111581771913429110): a labelled page with a profile, a turnaround incl. the BACK, detail close-ups, in-use poses and a DO NOT CHANGE block. Method updated 2026-10-23.

Talk to Huy in Vietnamese. Model: Kie **GPT Image 2.5 Flare**, 1K, ~6 credits. Script: `scripts/sheet.py` (local files are uploaded to Kie first).

## The kit

`output/<sp>/0-brief/truth-sheet/<product-key>/` (`<product-key>` = short kebab name, e.g. `sunslice`; a rival gets its own folder):

| File | Content |
|---|---|
| `truth.md` | Details line, Worn line (worn products), real-photo refs, durable sheet URL, after-gen count check (template below) |
| `sheet.png` | Sheet 1, the product alone, portrait 3:4: A profile + spec table, B turnaround FRONT / 3/4 / SIDE / BACK, D six labelled close-ups, F colour + DO NOT CHANGE. Checked against real photos. Other skills point at this name |
| `sheet-worn.png` | Sheet 2, only for products worn by or strapped to a person / animal (holster, harness, collar, carrier, seat cover): C worn turnaround, E four in-use poses, F DO NOT CHANGE about how it sits. Everything else (feeder, bed, light...) gets ONE sheet with two IN USE panels in it (Huy 2026-10-23) |
| `sheet-prompts.md` | Exact prompt, model, ratio, refs, one section per sheet |
| `sheet.url.txt` | Kie result URL (expires in ~24 h) |

Kie URLs die after a day: upload each approved sheet to the Dino CDN (`python3 ${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts/cdn.py <sheet.png> --prefix truth-<sp>`) and write that URL in `truth.md`; prompts and `refs.json` use the CDN URL.

Older kits (`hummingbird-feeder`, `oriole-feeder`) have one 16:9 four-panel `sheet.png` + `prompt.txt`: keep using it until it is redone in this format.

## Which refs a generation uses

| What is being generated | Refs, in this order |
|---|---|
| Still image (ad, sale page section, PDP slide, pre-sale) | 1-3 real photos listed in `truth.md` |
| Video (Seedance, Kling, any image-to-video), or the product has fewer than 3 usable real photos | the sheet(s) first (`sheet-worn.png` when it is worn in the scene), then one real packshot. Whole sheet as ref: the back view matters for video |
| Still image where the product is worn | real photos incl. the front-view worn photo, plus `sheet-worn.png` |
| Top 5 ad images (`fb-top5`, Google Discover images) | author photo (when a person is in frame), our `sheet.png`, then the rival sheets |

Every prompt that shows the product pastes the Details line from `truth.md` (and the Worn line when it is worn). After every gen, count each item of the Details line in the result before Huy sees it.

Real photos stay first for stills: real-photo refs and sheet refs both drew the right counts in hard scenes, and a wrong sheet spreads its error to every image. A sheet alone as the only ref for a still drifted (2026-10-13, feeder in a garden: flower ports drawn as flat stickers, flat base drawn as a bowl).

## Steps

1. **Material.** Read `output/<sp>/0-brief/0-product-brief.md` (what ships, colors) and `1-pre-sale-page/research/review-image-picks.md`. No picks yet: contact-sheet all photos in `1-pre-sale-page/research/amazon-review-images/` with PIL (5x4, numbered), look at every sheet, and pick 3-5 that show the layout seen from above (counts, spacing), the mechanism close-up (recessed vs raised parts) and how owners use or mount it. Log each pick in `review-image-picks.md` (what it proves + public URL). No reviews: use the listing hi-res images (`research/listing/`, see `pre-sale-page` *Amazon research*), supplier photos or the sale page's CDN images. Nothing usable, or unsure which color/variant we sell: stop and ask Huy for a packshot. Keep only our color/variant and only the parts that ship. **In-use refs must be real customer photos of it being used** (the bird at the feeder, the dog in the bed): listing photos alone made the model invent how it is used (oriole sheet v2: birds standing on a rod that barely exists).
2. **Details line.** Open the 2-3 clearest real photos large (PIL crop + zoom) and write 3-6 details the model gets wrong, each with a number or a shape you saw on the photo: counts (ports, wedges, petals, buttons, slots), spacing, recessed vs raised, color of each part, hook/handle/clip shape, what each hardware part is fixed to. Write only counts you counted on a zoomed real photo, never from the listing text or memory (a flower the listing called 5-petal had 6).
   - **Worn line (anything worn by or strapped to a person or animal, or mounted: holster, harness, collar, carrier, seat cover).** The Details line lists the parts; it does not say where they sit, and the model fills the gap with the category's usual design (a harness got a strap down the middle of the chest that the real one does not have). Look at real photos of it ON the body / in place from the FRONT and the side, then write a `**Worn**` line: which straps go where, where the buckle sits, and a NOT sentence naming the category's usual design that ours lacks. Add one real FRONT-view worn photo to the refs (blur any phone number first).
   - **How it is used** (every product with a user): from 3+ real customer photos, write where the user touches it (an oriole grips the OUTER RING or the cup's wire ring, body outside the ring, never stands on the orange), its size against the product, and the positions and gaps between parts that the use depends on (the cup fills the gap to the ring, no free rod beside it). Paste it in every prompt with the user in frame.
   - **How it goes on** (worn / mounted products): numbered steps from a real video of it being put on, never imagined. Source: the videos on the Amazon listing (brand + customer "Related videos", see `pre-sale-page` *Review videos* for the m3u8 + ffmpeg method), watched with the `watch` skill; save 3-4 frames as refs. Brand promo videos often skip it; customer videos usually show it.
3. **Sheet layout.** Two sheets at 1K so each panel stays big enough to check (one sheet of everything at 1K makes the panels too small). Portrait 3:4, white page, bold black headings, labelled panels, light-grey studio backgrounds:
   - **One sheet only** (anything not worn on a body, Huy 2026-10-23): TURNAROUND = FRONT, SIDE, BACK; DETAILS = four labelled close-ups; IN USE = two outdoor / real-setting panels from the How it is used line; DO NOT CHANGE block. Skip the spec table and swatches (they live in `truth.md`). Example: `output/2026-10-23-oriole-feeder/0-brief/truth-sheet/sunslice/`.
   - **Sheet 1, product** (worn products): A "PRODUCT PROFILE" = one large three-quarter view + a spec table (one row per Details item: what, how many, color); B "TURNAROUND" = FRONT, 3/4, SIDE, BACK (worn products: shaped as if worn by an invisible body); D "DETAILS" = six labelled close-ups of the parts the model gets wrong; F "COLOUR AND MATERIAL" swatches + a red "DO NOT CHANGE" checklist (each Details item as a short line, plus the NOT sentence).
   - **Sheet 2, worn / in use** (worn or mounted products): C "WORN TURNAROUND" = the same person / animal full body FRONT, 3/4, SIDE, BACK; E "IN USE" = four poses from the real use cases; F "DO NOT CHANGE" = how it sits (each line of the Worn line). Use the person or animal the ads already use, so the sheet doubles as their reference.
4. **Prompt.** Fill the template below and save it in `sheet-prompts.md`.
5. **Gen** (both sheets in parallel): `python3 ${CLAUDE_PLUGIN_ROOT}/skills/product-truth-sheet/scripts/sheet.py output/<sp>/0-brief/truth-sheet/<key>/sheet.png <prompt file> <ref1> [<ref2>] --ratio 3:4`. Refs = ref 1 a clean real photo where every countable part shows (often the empty listing packshot) + ref 2 a real customer photo of it in use (worn products: the front-view worn photo; sheet 2 puts it first). Say in the prompt what each ref is for ("copy the frame from the first; use the second only for how the bird perches"). Two review photos alone lost the structure (oriole v3 drew 6-7 small wedges instead of 4); listing photos alone lost the use (v2). **Never more than 2 refs** (extra customer photos changed a gold hook to silver; 5 refs made the model error). **Never an AI-made image as ref** (it carries its own mistakes). Flare drops a detail → tell Huy and ask before switching model; never switch quietly.
6. **Check every panel** against the real photos: count each Details item (PIL zoom), colors, shapes, incl. the BACK view and every worn panel. Keep one fully correct sheet. Both wrong: reword that detail in the prompt and gen 2 more. Show Huy the sheet next to one real photo plus what you counted; Huy approves it.
7. **Save the kit**: `sheet.png` (+ `sheet-worn.png`), `sheet-prompts.md`, `truth.md` with the CDN URL; add `Truth sheet: 0-brief/truth-sheet/<key>/ (Huy duyệt YYYY-MM-DD)` to `0-brief/0-product-brief.md`.

## Rival sheets (Top 5 ads, comparison images)

One sheet per product, the 4 rivals included. Same steps, sheet 1 only, with these changes:

- Folder `output/<sp>/0-brief/truth-sheet/<rival-key>/` with its own `truth.md` (Details line + Amazon link) and `sheet.png`.
- Source: the rival's photo on the pre-sale card (`output/<sp>/1-pre-sale-page/assets/`) plus its Amazon listing gallery for any angle the card does not show (base, hanger, ports). Keep our listing's color only, max 2 refs. No review-photo hunt.
- Details line: 2-4 items that make it look different from ours and from the other rivals (shape, material, color of each part, port count).
- Rivals are drawn unbranded: keep "no logos, no text"; if the source shows a brand name add "plain unmarked body, no brand name or lettering anywhere".
- Gen 1 sheet each (all 4 in parallel), check it against the source photo, show Huy the 4 sheets together.

## Sheet prompt template

```
The first image is [REF 1], the second is [REF 2]: use them as the exact identity source [and make it COLOR]. Create a photorealistic PRODUCT CONTINUITY SHEET for this one [PRODUCT]. White portrait page, bold black headings, clean grid, readable labels, light-grey studio backgrounds, soft natural lighting. Top: title "[PRODUCT NAME]" and under it a small widely spaced subtitle "PRODUCT CONTINUITY SHEET". Sections, each with a bold heading: 1) "PRODUCT PROFILE": one large three-quarter view on the left; on the right a small two-column table with rows "[PART] | [what, how many, color]" for each Details item. 2) "TURNAROUND": four equal panels labelled "FRONT", "3/4", "SIDE", "BACK". 3) "DETAILS": six equal labelled close-ups: "[PART 1]" ... "[PART 6]". 4) bottom left "COLOUR AND MATERIAL": labelled swatches; bottom right a red-bordered block with a lock icon titled "DO NOT CHANGE" and a checklist: "[one short line per Details item]", "[the NOT sentence]". Preserve the product with 100% fidelity in every panel: [DETAILS LINE]. [COUNT RULE / NOT sentence]. No invented parts, no logos, no phone numbers, no watermarks. Portrait 3:4.
```

Sheet 2 (worn) swaps the sections for "WORN TURNAROUND" (the same [PERSON / ANIMAL] full body FRONT, 3/4, SIDE, BACK), "IN USE" (four labelled real-use poses) and a DO NOT CHANGE block made of the Worn line, and pastes the Worn line + Details line.

Write counts as numbers and negatives ("exactly THREE wedge outlines on the left half, not four, the right half has NO wedges"): the model invents whatever the prompt leaves vague.

## truth.md template

```markdown
# <Product>: truth kit (Huy duyệt YYYY-MM-DD)

**Details** (paste into every prompt that shows the product):
<one line>

**Worn** (worn / mounted products only):
<one line, ending with the NOT sentence>

**Real-photo refs** (still images), in this order:
1. <what it proves> | `<local path>` | <public URL>

**Sheets**: `sheet.png` <CDN URL> (+ `sheet-worn.png` <CDN URL>). First ref for video, or when real photos are not enough.

**After gen**: count <items> in every image before sending to Huy.
```

Rival `truth.md`: title, `https://www.amazon.com/dp/<ASIN>`, Details line, sheet URL.

## Using the sheet in videos (Kling 3.0 on Kie, works 2026-10-13)

Model `kling-3.0/video`, input `multi_shots: true`, `multi_prompt: [{prompt, duration}]` (≤5 shots, ≤500 chars each, `@name` costs 37), `duration` = sum as string, `mode: std`, `sound: false`, `image_urls: [first frame]` (aspect follows it), `kling_elements: [{name, description, element_input_urls: [sheet, 1 real photo]}]` (2-4 images), and `@name` in each shot prompt. 2 shots × 3s std no sound = 84 credits; product held across shots. Example: `output/2026-10-05-hummingbird-feeder/video/hummzinger-drowned/gen.py`. Seedance: see `storyboard-video`.

Local files as refs: `sheet.py` uploads them to Kie (`POST https://kieai.redpandaai.co/api/file-stream-upload`, deleted after 24 h). For refs reused over days (`refs.json`), use the CDN URL.

## Model notes (2026-10-13 tests, one feeder, small sample)

| | Flare (default) | Nano Banana 2 (`nano-banana-2`, ~8 credits) |
|---|---|---|
| Making the sheet | follows the layout | broke it (extra bordered panels) and invented a part |
| Small details in a scene | ports flattened, base turned into a bowl (sheet alone) | closer once, wrong again in a backlit shot |

Flare stays the default (hub rule). NB2 only when Huy asks: `sheet.py --model nano-banana-2`, inputs go in `image_input`, a ratio it lacks is `--ratio auto`, never the nearest one.

## Common mistakes

| Mistake | Fix |
|---|---|
| Details written from listing text or memory | Count on a zoomed real photo |
| Sheet used without checking every panel | One of two sheets drew 4 ports instead of 5; check every panel, incl. the BACK view and every worn panel |
| Only views of the product alone for a worn product | The model never sees how it sits; add sheet 2 + the Worn line + a front-view worn real photo |
| Many refs for the sheet | 2 at most: 1 structure ref + 1 real in-use photo |
| Two sheets for a product nobody wears | One sheet with two IN USE panels |
| In-use panels drawn from listing photos only | Ref a real customer photo of it in use + write the How it is used line |
| Only counts checked, not positions | Also check gaps and positions the use depends on (cup next to the ring) |
| Sheet as the only ref for a still image while good real photos exist | Real photos first (table above) |
| AI-generated product images used as refs | Only real photos and the checked sheet. A person's face may come from the avatar library; say "use for face, hair and clothes ONLY" |
| A packshot showing 2 units + accessories as first ref for a single-product scene | Put a single-unit real photo first, or say "use only one" |
| Showing parts that do not ship (spare tails, extra cups) | Only the shipped parts in the Details line, the sheet and the packshot (see `pre-sale-page` step 0) |
| Kie sheet URL in `refs.json` | It expires in ~24 h; use the CDN copy |
| Model busy or erroring, so switch model quietly | Tell Huy and ask |
