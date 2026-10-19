# Style Guide — Image-to-Prompt Templates

Distilled from the template library (see `../../assets/img-templates/sale-page.md` and `../../assets/img-templates/top5-presale.md`). Use this as the voice and structure reference when writing a new prompt.

## The opening boilerplate

Every prompt opens with one of these flavors. Choose based on the source image:

**Designed / studio image:**
> Use the attached images as reference. Match the exact <subject / product> design, colors, and typography precisely.

**UGC / native-feeling image** (add a "do not polish" line after):
> Use the attached images as reference for <subject / product> color and details ONLY. Do NOT use polished layouts. This should look like a real person's <Story / Reddit screenshot / iPhone selfie / mirror photo>.

**Tone-only references** (editorial, mood pieces, where the source's brand or subject shouldn't be reproduced literally):
> Use the attached images as reference for visual tone ONLY.

**No reference at all** (pure-text-prompt creative): omit the opening line entirely.

## Layout language

Describe spatial breakdown in fractions or percentages, not vague position words. Patterns that recur:

- `Top 25%: [content]`
- `Top half / Bottom half`
- `Left 40% / Right 60%`
- `Upper-left / Lower-right`
- `Center, slightly below midline`
- `Full-bleed [photo]`
- `Bottom 20%: full-width [color] banner`

Avoid: "at the top", "off to one side", "somewhere in the middle". Be metric.

## Placeholder grammar

The 40 examples use a consistent pattern that gives the model both a slot AND a concrete anchor:

- `[COLOR]` — for any color the user will swap
- `[COLOR like deep indigo]` — when the source strongly suggests a color family
- `[COLOR with hex — a soft, muted tone works best]` — when the tone itself is the point
- `[SUBJECT]` / `[PRODUCT]` — generic
- `[PRODUCT like supplement bottle]` — when shape matters
- `[HEADLINE like "I finally found something that works!"]` — copy slot with example
- `[STAT 1 like 20g] / [LABEL like PROTEIN]` — paired stat slots
- `[PERSON DESCRIPTION like a woman in her early 30s, wearing a casual zip-up sweater]` — UGC subject

**The example inside the brackets is mandatory for any text slot, color slot, prop slot, or subject slot.** Without it the prompt produces generic output. With it the prompt one-shots.

For pure structural slots that have no copy (banner positions, divider lines, etc.) you don't need an example.

## Category-agnostic structure

One template must work across the whole product range (hat, flashlight, dog food, supplement, ...). Template the **mechanic**, not the object.

- Outside brackets: only generic nouns (`product`, `competitors`, `proof`, `logo`, `packaging`) and neutral verbs (`opened or used`, `facing the camera`).
- Inside brackets: the category-specific example that anchors the model.
- Comparison-style ads get two extra slots: `[PROOF like ...]` (what a buyer compares side by side) and `[WIN like ...]` (how the hero's proof looks better).

Bad (supplement-only): `each bottle's cap flipped upside down holding two capsules`
Good (any category): `in front of each product, [PROOF like two of its capsules in its flipped-over cap]`

Proof examples by category, all placed "in front of each product":

| Category | PROOF | WIN |
|---|---|---|
| Hat | a white paper towel pressed into its sweatband after a hot day | almost dry while the others show brown sweat stains |
| Flashlight | the pool of light it casts on the counter, switched on and lying on its side | biggest, brightest white pool, others small and dim yellow |
| Dog food | a small pile of its kibble in a plastic scoop | meatier, darker and more uniform |
| Supplement | two of its capsules in its flipped-over cap | fuller and brighter white |

## Photography spec language

Always include a lens or device spec when photography is involved. The 40 examples use phrases like:

- `Shot at 50mm f/2.8 from slightly above`
- `85mm f/2.8, soft side light`
- `35mm f/2.0`
- `Soft studio lighting`
- `Warm natural light`
- `Bright flat studio lighting`
- `iPhone 15 quality`
- `iPhone front camera, slightly grainy, bathroom/kitchen lighting, no professional setup`
- `Cinematic color grade with warm highlights and cool shadows`

Pick what matches the source ad. Don't invent specs that contradict what you see.

## Typography vocabulary

Match what's in the image:

- Weight: regular / medium / semi-bold / bold / heavy / black
- Family: serif / sans-serif / italic serif / condensed sans / rounded retro / Cooper Black style
- Case: all-caps / uppercase / sentence-case / Title Case / lowercase
- Treatment: tight leading / wide-tracked / oversized / pull-quote with quotation marks
- Color: bold white / [BRAND COLOR] / black

Example pattern: `bold all-caps condensed sans-serif headline filling the width of the frame in white text with key words in [HIGHLIGHT COLOR like neon yellow]`

## Trust / social-proof / UI elements

These show up often in commercial imagery. Use the standard nouns from the examples:

- `five filled gold stars` / `five filled [BRAND COLOR] stars`
- `blue checkmark` + `Verified Reviewer` / `Verified Buyer`
- `white rounded-rectangle review card with subtle shadow`
- `gray circular avatar icon`
- `helpfulness count like 150`
- `Was this review helpful? 👍`
- `As Featured In` + `five grayscale publication logos`
- `circular trust badge / seal reading "[GUARANTEE TEXT]"`
- `Facebook-style comment card` / `Reddit-style post` / `iOS Notes screenshot` / `Instagram Story highlighted text`

## Aspect ratio close

Always the last sentence, alone, with a period, as an open slot with no example ratio:

- `[ASPECT RATIO] aspect ratio.`

The ratio is picked at gen time (ads default 1:1), never fixed by the template. Measure the source, don't guess, and record it outside the prompt as "Drawn at 4:5." so fills at other ratios know what to re-flow. Templates are filled at any ratio (1:1, 4:5, 5:4, 9:16, 16:9, 1.91:1), so don't call the frame "square" or "vertical" anywhere else; the "Aspect ratios" section of SKILL.md re-flows the layout at fill time.

## Common pitfalls to avoid

1. **Baking in the source's actual copy** — every text element must be a placeholder slot. If you write `"THE GREATEST PANTS IN GOLF"` as literal copy, you've failed. Write `[HEADLINE like "THE GREATEST PANTS IN GOLF"]`.

2. **Missing the "do NOT polish" line on UGC** — without it the model defaults to glossy ad output. The line is load-bearing.

3. **Vague layout** — "the product is on one side" is not enough. Specify which side and roughly what fraction.

4. **No camera spec for photographic ads** — even one phrase ("soft studio lighting") tells the model what world to render in.

5. **Forgetting trust elements** — review cards, stars, verified badges, comment screenshots are often what make these ads convert. If they're in the source, they need to be in the prompt.

6. **Aspect ratio buried mid-prompt or hard-coded** — it goes at the end, alone, with a period, as the open `[ASPECT RATIO]` slot.

7. **Over-explaining** — the user wants ONE prompt they can paste. Don't add commentary inside the code block. Save the breakdown for outside the block if asked.

8. **Baking in the source's product category** — "bottles lined up, caps off, capsules in each cap" only works for supplements. Run the swap test: every word outside brackets must still make sense for a hat, a flashlight and dog food. See "Category-agnostic structure" above.

## Length calibration

| Ad complexity | Target word count |
|---|---|
| Single hero + headline (Bold Statement, Flavor Story) | 80–120 |
| Standard product ad with 4–5 elements | 120–180 |
| Information-dense (Stat Radial, Pull-Quote Review Card, Native Post-It) | 200–280 |

Don't pad. Don't under-spec. Match the density of what's actually in the image.
