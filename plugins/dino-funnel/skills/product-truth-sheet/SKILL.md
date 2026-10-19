---
name: product-truth-sheet
description: Product truth sheet: one 4-panel reference image (white background, 16:9) that locks a product's exact look, made from its real listing photos, then used as the reference when generating scene images or videos of that product, ours or a competitor's. Use when the user asks for a "truth sheet", "sheet sản phẩm", "character sheet cho sản phẩm", or when generated images/videos keep getting a product's details wrong (port count, shape, parts).
---

# Product truth sheet

Adapted from Ori Silver's *Character Sheet Playbook* (one sheet locks a character from several views so the model stops guessing). For products the sheet fixes the **overall look** (silhouette, colors, main parts); small details (port shape, a flat vs deep base, flutes) can still drift in scenes, so every use ends with a check against the real photos.

Model: Kie **GPT Image 2.5 Flare** (`gpt-image-2-5-flare-image-to-image`), 1K, ~6 credits, 16:9. Script: `scripts/sheet.py`.

## Steps

1. **Real photos in.** 3-4 public URLs of the real product from different angles: hi-res listing images (`"hiRes"` from the Amazon page, see `pre-sale-page` *Amazon research*), our Shopify gallery, an exploded/parts photo if one exists. Our product: the sale page's `shopify-urls.json`. Done when every part you will describe in step 2 is visible in at least one input.
2. **Pick the 4 panels** by product shape:
   - **Round / symmetric** (feeders, bottles, lights): a view where every countable part shows at once (top-down for ports), straight-on front, close-up of the selling detail (moat, lock, clip), the in-use or taken-apart state (base off, lid open). Rotating a round product 45° shows nothing new.
   - **Has a front and sides** (holster, bag, garment, seat cover): close-up of the selling detail, straight-on front, then the guide's two 45° panels with its mirror wording ("faces the LEFT edge ... faces the RIGHT edge ... exact mirror images, never the same direction").
3. **Write the prompt** in `<out_dir>/prompt.txt` from the template below. The identity paragraph names every part with **counts and shapes stated as numbers and negatives** ("exactly five yellow flower ports, not six"; "raised bell-shaped flowers standing on a flat top surface"). The model invents whatever the prompt leaves vague.
4. **Generate:** `python3 ${CLAUDE_PLUGIN_ROOT}/skills/product-truth-sheet/scripts/sheet.py <out_dir>/sheet.png <out_dir>/prompt.txt <url1> <url2> ...` (python3 with `requests`; key `KIE_API_KEY` from `.env` at the working folder root). Writes `sheet.png` + `sheet.url.txt`.
5. **Check panel by panel against the real photos:** exactly 4 panels, no borders or text, every count right, every part real (nothing added), proportions right. Any miss → tighten that part's wording in the identity paragraph and regenerate. Done when the user has seen the sheet next to one real photo and said ok.

Output: `output/<sp>/truth-sheet/<product-key>/` (`prompt.txt`, `sheet.png`, `sheet.url.txt`). A competitor gets its own folder, one product per sheet.

## Prompt template

```
Using the product in the reference images as the exact identity source, create a product reference sheet on a pure white background (#FFFFFF), studio lighting, no shadows on the background. One horizontal row of exactly four panels, side by side, all the same height.

From left to right:
1. Far left: [PANEL 1 like the red feeding base seen from directly above, filling the panel, so all its ports show at once: exactly FIVE yellow flower ports in a circle. Count them: five, not six].
2. [PANEL 2 like the full assembled product, upright, facing the camera straight on, top to bottom fully visible, eye level].
3. [PANEL 3].
4. [PANEL 4].

Preserve the product with 100% fidelity in all four panels, identical product across every panel: [IDENTITY: every part with material, color, shape, size and count]. Same proportions, same colors, same counts in every panel. Do not redesign, do not add or remove parts, do not add logos or text. If a side is not visible in the references, reconstruct it fully consistent with the visible design.

Photorealistic product photography, white cyclorama, soft even lighting, 85mm look, no text labels, no watermarks, no grid lines, no borders between panels.
```

Worked example (Matthew 6:26 hummingbird feeder, passed the check): `output/hummingbird-feeder/truth-sheet/prompt-v2.txt` → `sheet-v2.png`.

## Using the sheet

- **Scene image:** inputs = the sheet's URL (`sheet.url.txt`) as reference 1, **plus one real photo** as reference 2, plus a *locked details* sentence repeating the counts and shapes from the identity paragraph. Sheet alone failed (2026-10-13, feeder in a garden): Flare redrew the flower ports as flat stickers on the side wall and the flat base as a deep bowl. Name the sheet in the prompt: "Reference 1 is a product truth sheet of one [product] from several views; reproduce that exact [product]."
- **Several products in one image** (comparison hero): one sheet per product, each as its own reference, described in the prompt by position.
- **Video (Kling 3.0 on Kie, works 2026-10-13):** model `kling-3.0/video`, input `multi_shots: true`, `multi_prompt: [{prompt, duration}]` (≤5 shots, ≤500 chars each, `@name` costs 37), `duration` = sum as string, `mode: std`, `sound: false`, `image_urls: [first frame]` (aspect follows it), `kling_elements: [{name, description, element_input_urls: [sheet, 1 real photo]}]` (2-4 images), and `@name` in each shot prompt. 2 shots × 3s std no sound = 84 credits; product held across shots. Example: `output/hummingbird-feeder/video/hummzinger-drowned/gen.py`.
- **Local files as refs** (a user photo, a sheet whose Kie URL expired): upload to Kie `POST https://kieai.redpandaai.co/api/file-stream-upload` (Bearer `KIE_API_KEY`, form `file` + `uploadPath`, URL in `data.downloadUrl` (or `data.fileUrl`), deleted after 24h). Shopify Files only for images that appear on a Shopify page.
- After every use, run step 5's check on the product in the result.

## Model notes (2026-10-13 tests, one feeder, small sample)

| | Flare (default) | Nano Banana 2 (`nano-banana-2`, ~8 credits) |
|---|---|---|
| Making the sheet | follows the 4-panel layout | broke it (6 bordered panels) and invented a part |
| Small details in a scene | ports flattened, base turned into a bowl (sheet alone) | ports and base closer once, wrong again in a backlit shot |

Flare stays the default (hub rule). NB2 only when the user asks: its inputs go in `image_input` (`sheet.py --model nano-banana-2`), and a ratio it lacks is `--ratio auto`, never the nearest one.
