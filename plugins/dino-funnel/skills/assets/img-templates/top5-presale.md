<!-- Library: TOP 5 PRE-SALE PAGE ads (ads driving to a Top 5 / buyer's-guide page). Copied verbatim from the top5-ad-templates skill. IDs: T5-01..T5-40 (33–40 added 2026-10-09, original designs), new templates from images continue at T5-41, inserted right after template 40 and before "## Ghi chú drift". Ratio is open: every prompt ends with `[ASPECT RATIO] aspect ratio.` and the ratio is picked at gen time (Top 5 ads default 1:1). All 40 % layouts were drawn at 1:1; any other ratio re-flows per "Aspect ratios" in SKILL.md. -->

# 40 Top-5 ad prompt templates, category-agnostic

Bản slot hoá của `top5-32-prompts-flashlight.md`. Bộ gốc bake cứng chữ "flashlight",
"batteries", "beam", "power outage" vào câu cấu trúc nên chết ngay khi đổi ngành.
Bản này giữ nguyên cơ chế thuyết phục và % layout, đẩy toàn bộ chữ thuộc ngành vào slot.
Số template giữ nguyên bộ gốc để truy vết.

**Khác gì `alex-cooper-ad-formats`:** bộ kia là ads dắt về **sale page** một sản phẩm.
Bộ này là ads dắt về **trang Top 5 / buyer's guide**, nên mọi layout đều có sẵn dãy 5 sản phẩm
và cơ chế "so sánh rồi mới chọn". Đừng trộn hai bộ trong cùng một chiến dịch.

## Luật dùng

1. **Điền hết slot trước khi paste.** Không để lại dấu ngoặc vuông, không để chữ "like".
   Model render nguyên chuỗi `[HEADLINE like ...]` thành typography trong ảnh.
2. **`[HERO]` là một câu khoá, viết một lần rồi lặp verbatim** ở mọi prompt có nó.
   Câu đó phải có: màu, chất liệu, hình dáng, phần cứng, chữ in trên sản phẩm.
   Lệch câu này là nguyên nhân số 1 làm ảnh không dùng được.
3. **Cấm prop trung gian.** Không dish, bowl, tray, saucer, lid trừ khi slot gọi tên.
   Đây là lỗi đã gặp: `small round white dish` bị render thành nắp hũ, vô nghĩa với mọi ngành.
4. **Đối thủ luôn là hàng tự chế, thân trơn**: không tên brand, không logo, kể cả tên bịa. Không name tag ghi tên sản phẩm. Wordmark của site review (TopReviewQueen) thì được.
5. **Tối đa 5 sản phẩm mỗi ảnh, không bao giờ hơn.** Đây là ads Top 5: ảnh có 6, 7, 10 sản phẩm là sai thông điệp. Template nào vẽ đống/hàng sản phẩm cũng chốt "exactly five".
6. Mọi prompt full-bleed, không viền. Tỉ lệ khung là ô `[ASPECT RATIO]`, chuyển bố cục theo mục "Aspect ratios" trong SKILL.md.
7. Không bịa tên người review. Không dựng giao diện Amazon / Trustpilot / báo thật.
8. **Image Input: tấm nào cũng gắn đủ 5 ảnh sản phẩm** (Huy 2026-10-09), kể cả tấm chỉ vẽ 1–4 sp hay tấm giấu hero. Thứ tự: sp mình trước, rồi 4 đối thủ. Khung có người → gắn thêm ảnh avatar (người trên trang đích, vd tác giả bài viết) **đặt trước** 5 ảnh sp, và thay người mẫu trong template bằng người đó (tả mặt, tóc, kính, áo một câu khoá, lặp verbatim).
   Câu mở đầu prompt nói rõ ảnh nào là gì:
   - Không người: `The first attached image is our [CATEGORY SINGULAR] and the other four are the rival [CATEGORY]; use them as reference for product color and details ONLY.` (template studio: thay "for product color and details ONLY" bằng "Match the exact product design and colors of each product precisely.")
   - Có người: `The first [N] attached images are [NAME], the same person; the next is our [CATEGORY SINGULAR] and the other four are the rival [CATEGORY]; use them as reference for [her/his] face and for product color and details ONLY.`

## Slot glossary

| Slot | Là gì |
|---|---|
| `[CATEGORY]` | tên ngành số nhiều, ví dụ mini flashlights, ball caps, bird feeders. Nằm trong headline/caption Title Case thì viết hoa từng chữ (Window Hummingbird Feeders) |
| `[CATEGORY SINGULAR]` | tên ngành số ít, cùng luật viết hoa trong headline Title Case |
| `[HERO]` | một câu khoá tả đúng sản phẩm thật, lặp verbatim mọi nơi |
| `[RIVAL 1..4]` | tả vật lý ngắn, mỗi cái một màu/kiểu khác nhau |
| `[POSE]` | cách đặt sản phẩm: đứng trên đế nếu đứng được, nằm ngửa nếu không |
| `[FAIL PART]` | đúng một bộ phận chết trước tiên trong ngành này |
| `[PROOF ITEM]` | món đi kèm mà mọi sản phẩm trong ngành đều có và bị đem ra so |
| `[PROOF RESULT]` | kết quả nhìn thấy được, chụp cạnh nhau được, tách hàng tốt khỏi hàng dở |
| `[SETTING]` | căn phòng đời thường nơi sản phẩm thực sự được dùng |
| `[HEADLINE]` | câu hỏi hoặc câu chốt đi từ vấn đề, không nói lumen/thông số |
| `[SUBHEAD]` | một câu |
| `[CLAIM]` | một câu nói đúng một thất bại mà chỉ một sản phẩm sống sót |
| `[SPEC CLAIM]` | con số ngành hay khoe và người mua hay tin nhầm |
| `[GOOD AXIS 1]`, `[GOOD AXIS 2]`, `[BAD AXIS]` | ba trục của biểu đồ cột |
| `[END CAP CLAIM]` | lợi thế duy nhất hero có mà cả bảng không có |
| `[FAILURE DEBRIS]` | đống mảnh vỡ ngành này để lại |
| `[PRICE SPENT]` | tổng tiền đã đốt để test |
| `[SPEC UNIT]` | đơn vị của `[SPEC CLAIM]` (lumens, oz, mAh) |
| `[TEST NAME]` | tên bài test dài hạn, ví dụ 90-DAY DAILY-USE TEST |
| `[LOW PRICE]`, `[HIGH PRICE]` | giá rẻ nhất / đắt nhất trong 5 món đã test |

## Bảng fill mẫu

| Slot | Mini flashlight | Ball cap | Bird feeder | Chef knife | Running shoe |
|---|---|---|---|---|---|
| POSE | đứng trên đuôi | nằm ngửa, chóp lên | đứng trên đế | nằm, lưỡi hướng ra | nằm, mặt ngoài lên |
| FAIL PART | nút cao su bên hông | đường may vành lưỡi trai | chốt khoá nắp | mối nối chuôi và lưỡi | keo dán đế |
| PROOF ITEM | dây sạc đi kèm | tem size khâu trong | móc treo đi kèm | bao dao đi kèm | lót trong rút ra |
| PROOF RESULT | vệt sáng trên tường | form mũ sau khi vò | hạt còn lại sau 1 tuần | lát giấy cắt được | mòn gót sau 200 dặm |
| SPEC CLAIM | số lumen | số lớp lưới thoáng | sức chứa gram hạt | độ cứng HRC | số gram nhẹ |
| SETTING | bàn nguội trong garage | bàn bếp gỗ | bàn sân sau | thớt trong bếp | bậc thềm trước nhà |

---

### 1 — Macro diorama cutaway

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a ranking ad, full-bleed, no border or frame around the image, on a bright soft light gray studio gradient. Top 62%: a surreal macro tabletop diorama. Center: a massive cutaway cross-section of [CUTAWAY SUBJECT — the one internal part that decides whether this category works or fails], opened so its layers, materials and moving parts all read at a glance, filling 90% of the width and towering over the scene. Swarming over and around it: about 20 miniature engineers in navy work shirts, safety glasses and yellow hard hats, some standing on top, some climbing aluminum stepladders and small rolling scaffolds, others inspecting its surfaces with [MEASURING TOOLS — the instruments this category is actually tested with], tablets, clipboards and tiny screwdrivers, with a large round work lamp glowing above the center. Photographed as a real miniature set, 100mm macro f/8, soft even studio light, gentle tilt-shift falloff at the edges, figures with natural faces, realistic fabric wrinkles and fine hand-painted detail, not CGI, not cartoon. At 63% to 69% height: a full-width rounded pill bar in pale cool gray with centered bold black sans-serif Title Case text reading "Top [CATEGORY] Tested & Ranked". Bottom 29%: pure white strip with five products in one evenly spaced row, each about 17% of the width, front-facing, bottoms aligned, [POSE], soft contact shadows, [HERO] in the center slot, flanked by four rivals: [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies. Nothing under or beside the lineup: no brand names, wordmarks, icons or captions, only white space below the products. Crisp packshot lighting on the lineup. Clean, credible, investigative, curiosity-driven. [ASPECT RATIO] aspect ratio.
```

### 2 — Report-card phone grid

```
Use the attached product images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like five real phone photos a person snapped at home and dropped into a simple collage. Create: a photo grid, full-bleed, no border or frame around the image, cells separated only by thin white gutters about 1% wide. Top row, 0% to 53% height: three equal cells. Bottom row, 53% to 100% height: two equal cells. Every cell shows the same spot: [SETTING], with the same two or three ordinary objects visible in the background of each cell, warm lamp light mixed with window daylight. In each cell, one product sits centered on the surface, filling about 60% of the cell height, [POSE], facing the camera: four rivals, [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], in four cells, plain unmarked bodies with no brand names or logos, and [HERO] in the top-right cell. A square neon orange sticky note is stuck to the upper-right edge of each product, slightly crooked and overlapping it, with one grade handwritten in thick black marker, big and uneven: top row left to right "B", "B+", "A+"; bottom row left to right "B-", "C+". The hero's grade is clearly the best on the page. Phone-camera quality, slightly grainy, natural shadows, tiny framing differences between cells, no professional setup. Do NOT polish, no retouching, no graphic overlays, no headline text. Honest, homemade, report-card feel. [ASPECT RATIO] aspect ratio.
```

Lỗi đã gặp (cat bed 2026-10-16): chỉ ghi "hero in the top-right cell" thì máy tự xếp ô, hero dính điểm C+. Khi fill phải gán từng ô theo thứ tự ("top row left to right R1, then R2, then HERO; bottom row R3, then R4") và gắn từng điểm vào tên món ("A+" on our ...).

### 3 — TopReviewKing editorial

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a editorial review ad, full-bleed, no border or frame around the image. Top 54%: pure white. At 4% to 11% height, centered: a small stacked "TopReviewKing" wordmark in dark navy bold sans-serif with "King" in bright red, a tiny gold crown icon below. At 13% to 21% height: a rounded rectangle banner in royal blue spanning 90% of the width, with centered heavy white sans-serif text reading "[YEAR]'s Top [CATEGORY]". At 23% to 32%: two centered lines of bold sans-serif text in royal blue: "[HEADLINE — a question naming the failure the buyer has already lived]" then "[SUBHEAD — see which ones pass and which ones quit]". At 34% to 53%: five products in one evenly spaced row, each about 17% of the width, front-facing, bottoms aligned, [POSE], soft packshot light: [HERO] in the center slot, flanked by four rivals: [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies. No brand names, wordmarks, icons or captions on or under the row. Bottom 46%: two photos side by side, 50% each, no gap. Left: a calm man in his early 50s with a short gray beard and a flannel shirt in [SETTING], [GOOD SCENE — him getting the result the category is bought for with the hero, hands relaxed, nothing going wrong]. Right: a man in his mid 60s with thinning gray hair in the same kind of place, [BAD SCENE — him hitting the exact failure named in the headline, same task, wrong product]. Both at 85mm f/2.0, natural skin texture with real pores and fine lines, candid, not airbrushed, not CGI. Centered over the seam at 88% to 96% height: a white rounded pill with bold sans-serif text in royal blue reading "#1 isn't sold on Amazon...". Trustworthy, curiosity-driven. [ASPECT RATIO] aspect ratio.
```

Other ratios: At wide: the wordmark and blue banner go inline in the headline band (max 25% height), no left text panel, so the two photos run full width at about 50% height, product row a bottom strip.

### 4 — Before and after macro split

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a ranking ad, full-bleed, no border or frame around the image. Top 61%: two extreme close-up photos side by side, 50% width each, meeting at a hard vertical seam with no gap. Left: [FAIL PART] of an old worn-out unit, in its failed state, described down to the texture: what has torn, split, corroded, stripped or come apart, with the grime and wear that comes with it. Right: the same subject from the same angle and framing in its healthy state, [FAIL PART] of a new unit, clean, intact and correctly seated, with the one detail that makes it last visible beside it. Both shot at 100mm macro f/5.6, soft diffused daylight, razor-sharp micro detail and real surface texture; if a person or animal is shown, natural skin or fur texture, not airbrushed, not CGI, not illustrated. The contrast between the two halves must read in one glance. Overlapping the bottom edge of the photos at 60% to 68% height: a full-width rounded pill bar in pale cool gray with centered bold black sans-serif Title Case text reading "Top [CATEGORY] Tested & Ranked". Bottom 30%: pure white strip with five products in one evenly spaced row, each about 17% of the width, front-facing, bottoms aligned, [POSE], soft contact shadows, [HERO] in the center slot, flanked by four rivals: [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies. No brand names, wordmarks, icons or captions on or under the products. Crisp packshot lighting on the lineup. Clinical, visceral, clear problem-then-solution feel. [ASPECT RATIO] aspect ratio.
```

### 5 — Listicle with tester proof photo

```
Use the attached product images as reference for product color and details ONLY. The photo section must look like a real tester's phone snapshot, not an ad shoot. Create: a listicle ad, full-bleed, no border or frame around the image, on a pure white background. At 3% to 12% height: a centered heavy all-caps sans-serif headline in bright red reading "TOP 5 [CATEGORY]". At 13% to 24%: two centered lines of bold black sans-serif sentence-case text reading "[SUBHEAD — we tested the most popular ones, here are the best we found, in the tester's own plain words]". From 26% to 71% height, edge to edge: a candid close-up photo in [SETTING] of the same five products as the row below, the same five designs and no others, put through the same test at the same time in one frame, arranged so [PROOF RESULT] can be compared side by side: [HERO] nearest the camera, clearly passing, while the four rivals clearly fall short, plain unmarked bodies. Phone-camera quality, shallow depth of field, slightly grainy, available light with a reflective sheen, natural clutter at the edges, no professional setup. Do NOT polish the photo, no retouching, no graphic overlays on it. From 74% to 96% height: five products in one evenly spaced row on white, each about 17% of the width, front-facing, bottoms aligned, [POSE], soft contact shadows: [HERO] and four rivals, [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies. No brand names, wordmarks, icons or captions on or under the row. Honest, hands-on, tested-by-a-real-person feel. [ASPECT RATIO] aspect ratio.
```

### 6 — Gradient hero, four corners

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a ranking ad, full-bleed, no border or frame around the image, on a bright smooth diagonal gradient background blending sky blue at the left, soft lavender at the top right and warm butter yellow at the bottom. Top 22%: two centered lines of heavy black sans-serif Title Case headline, tight leading, reading "[HEADLINE — a question, problem first, no specs]". Center: [HERO], [POSE], front-facing, about 32% of the width, spanning 34% to 82% height, clearly the biggest object in the frame. A thin black vertical hairline drops from just under the headline to the top of the hero, as if the hero hangs from the question. Four smaller competitors, each about 20% of the width, sit in the corners around it as crisp cut-out packshots with soft drop shadows, upper-left and upper-right at 26% to 52% height, lower-left and lower-right at 58% to 86% height: [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies. No brand names, wordmarks, icons or captions on or under the products. Bottom center at 88% to 95% height: a small rectangular badge with a thin rainbow gradient outline and no fill, holding "TopReviewKing" in bold black sans-serif followed by a tiny magnifying-glass icon. Even soft studio lighting on all products, generous breathing room between them, no other text. Playful, confident, obvious-winner feel. [ASPECT RATIO] aspect ratio.
```

Other ratios: At wide: the headline stays a top band, max 22% height; the hero hangs centered below it on the hairline, two rivals stacked on each side.

### 7 — Wear progression

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a ranking ad, full-bleed, no border or frame around the image. Top 65%: a hyperreal progression image on a pale blue-gray textured plaster wall with a soft vignette. Five versions of the same [FAIL PART], seen in tight close-up from the same angle, overlap left to right in a fanned row, each worse than the last, and each one changing exactly one visible thing from the one before it: [WEAR SEQUENCE — stage 1 new and correct, stage 2 first cosmetic wear, stage 3 first real damage, stage 4 the failure, stage 5 the part unusable]. The first is largest, 6% to 34% width, each next one slightly higher and smaller, so the row climbs toward the upper-right. Photoreal material texture, soft top light, gentle shadows, not cartoon, not flat vector. From the bottom of each version, a thin dashed vertical leader line drops to a caption in regular dark charcoal sans-serif sentence case, captions stepping upward from left to right between 38% and 60% height: "New", "[TIME 1]", "[TIME 2]", "[FAILURE WORD]", "[CONSEQUENCE]". At 66% to 72% height: a full-width rounded pill bar in pale cool gray with centered bold black sans-serif Title Case text reading "Top [CATEGORY] Tested & Ranked". Bottom 27%: pure white strip with five products in one evenly spaced row, each about 17% of the width, front-facing, bottoms aligned, [POSE], soft contact shadows, [HERO] first on the left, followed by [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies. No brand names, wordmarks, icons or captions on or under the products. Crisp packshot lighting. Educational, alarming, clear escalation. [ASPECT RATIO] aspect ratio.
```

### 8 — Three-band GOOD / BAD

```
Use the attached product images as reference for product color and details ONLY. Do NOT use polished ad layouts for the photos. They should look like a real tester's phone snapshots taken at home. Create: a three-band listicle ad, full-bleed, no border or frame around the image. Top 37%, edge to edge: a slightly overhead close-up of two units of this category lying side by side on glossy black subway tile with white grout, both opened or turned so the part that decides the category is visible on each, the left one showing [GOOD INTERNALS — the hero's own key part, opened or lifted out, showing what a well-built one looks like], the right one showing [BAD INTERNALS — the same part on a rival of a visibly different design, failed]. Written on each one, or on a strip of tape stuck to it, in thick black marker with big uneven handwritten capitals: "GOOD [CATEGORY SINGULAR]" on the left and "BAD [CATEGORY SINGULAR]" on the right. Middle band, 37% to 60% height, pure white: a centered heavy all-caps sans-serif headline in bright red reading "TOP 5 [CATEGORY]", and below it two centered lines of bold black sans-serif sentence-case text reading "[SUBHEAD]". Bottom 40%, edge to edge: a crowded, overlapping pile of exactly five units, [HERO], [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], crammed together on a surface in [SETTING], plain unmarked bodies with no brand names or logos. Phone-camera quality, slightly grainy, flat overhead indoor light, real reflections, no professional setup. Do NOT polish, no retouching, no graphic overlays on the photos. Honest, hands-on, we-did-the-homework feel. [ASPECT RATIO] aspect ratio.
```

### 9 — Marble shelf editorial

```
Use the attached images as reference for product color and details. Match the typography style precisely. Create: a editorial ranking ad, full-bleed, no border or frame around the image. Top 40%: flat clean white. 5% to 24%: three centered lines of heavy all-caps sans-serif in bright red, tight leading: "WE RANKED THE BEST [CATEGORY] OF [YEAR]". 26% to 40%: three centered lines of regular sans-serif body copy in near-black, sentence case: "We tested 5 popular [CATEGORY]. Here's the one that [THE ONE THING THAT MATTERS], especially if [BUYER SITUATION].", with "5 popular [CATEGORY]" and "especially if [BUYER SITUATION]" set in bold. Bottom 60%: full-width photo of a two-tier white marble display shelf, soft even daylight, shot straight on at 50mm f/4, deep focus. Upper tier, 40% to 68%: three matching small clear round glass bowls, evenly spaced, each holding one of the three competing versions of [PROOF ITEM] this category ships with, each with a small paper tag on the front in mint green, butter yellow and soft pink, small monospace caps in black naming them left to right. Lower tier, 70% to 100%: five units in a row, [POSE]: [HERO], [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies with no brand names or logos. Bright, clean, trustworthy test-report mood. [ASPECT RATIO] aspect ratio.
```

Other ratios: At 9:16: a three-tier shelf (bowls / 3 units / 2 units).

### 10 — Native "cheap ones are a scam"

```
Use the attached images as reference for product color and details ONLY. Do NOT polish; this should look like a real person's phone photo of their home test setup, mid-test, not a styled ad. Create: a native ad, full-bleed, no border or frame around the image. Top 34%: flat plain white with centered text. Line one, heavy condensed all-caps sans-serif in bright red: "CHEAP [CATEGORY]". Line two, same font in black: "ARE A SCAM". Below, three short lines of regular lowercase sans-serif in black: "(well, most of them at least)", "we tested the popular ones,", "here are our top 5". Bottom 66%: candid photo on a worn wooden kitchen table in a bright lived-in home kitchen with windows, a plant and a fruit bowl behind, natural window daylight, smartphone wide lens, slight grain, deep focus. Right 30%: a man in his late 50s with short gray hair and gray stubble, faded plaid flannel shirt, head resting on one hand, tired but warm closed-mouth smile at the camera, natural skin texture with fine lines, candid, not airbrushed, not CGI. Center: five competing units in mixed sizes, plain unmarked bodies with no brand names or logos. In front of each, laid directly on the table: its own [PROOF ITEM], with one of the five having none at all. Behind them: opened cardboard shipping boxes. Left edge: a ceramic coffee mug on a woven placemat. Lower-left corner: a spiral notebook of handwritten test notes with a black pen. Honest, slightly messy, real-tester mood. [ASPECT RATIO] aspect ratio.
```

### 11 — Stacked bar chart

```
Use the attached images as reference for product details. Match the chart style and typography precisely. Create: a infographic comparison ad on a flat very light warm gray, full-bleed, no border or frame around the image. 5% to 17%: centered heavy sans-serif headline in black, Title Case, tight tracking: "Top [CATEGORY] Tested". 22% to 96%: a horizontal stacked bar chart with five evenly spaced rows. Left 16%: one small clean cutout packshot per row, five different units [POSE], fronts facing the camera, rivals with plain unmarked bodies with no brand names or logos, [HERO] in the top row. Just right of the packshots: a thin vertical black axis line running the full chart height. Each row is a flat, square-cornered bar made of segments, with bold condensed all-caps text in white centered in each. Segment one in forest green: "[GOOD AXIS 1]". Segment two in navy blue: "[GOOD AXIS 2]". Rows two, three and four add a third segment in bright red: "[BAD AXIS]" plus a small circled X, short in row two, long in rows three and four. Rows one and five end with a narrow mid gray end cap and condensed caps text just outside the bar in black: "[END CAP CLAIM]". Top row: the longest green and navy segments, each text followed by a checkmark, no red segment. Row five: both good segments short, no bad segment. Flat vector graphic, no shadows, crisp edges, data-report clarity. [ASPECT RATIO] aspect ratio.
```

### 12 — Granite counter, red band

```
Use the attached images as reference for product color and details ONLY. Do NOT polish the photo; it should look like a real person's quick phone snapshot at home, not a studio shot. Create: a native ranking ad, full-bleed, no border or frame around the image. Full frame: candid phone photo on a speckled granite kitchen counter, overhead room light mixed with window daylight, smartphone photo quality, slight grain, shot from standing height at a slight downward angle. Top 8%: the photo continues, heavily blurred, showing a soft yellow kitchen towel against a white wall. 8% to 38%: a full-width solid deep brick red band. Inside it, three centered lines of heavy all-caps sans-serif in white: "WE RANKED THE", "BEST [CATEGORY SINGULAR]", "IN [YEAR]", with the year in neon green. Bottom 62%: five units in a tight row, [POSE]: [RIVAL 1], [RIVAL 2], [HERO], [RIVAL 3] and [RIVAL 4], plain unmarked bodies with no brand names or logos, a bit of everyday clutter peeking out behind them. Foreground, on the surface in front of the products: [FAILURE DEBRIS — the broken parts this category leaves behind, three or four of them], casually placed, not arranged. Honest, unstyled, real-home mood. [ASPECT RATIO] aspect ratio.
```

### 13 — Creator thumbnail

```
Use the attached images as reference for product color and details ONLY. Do NOT polish into a glossy ad; this should look like a real creator's video thumbnail shot at home. Create: a curiosity ad, full-bleed, no border or frame around the image. Top 15%: a solid white band with two centered lines of heavy all-caps sans-serif in black, tight leading: "[TEST LINE — I put all 5 through the one test that matters]" and "[RESULT LINE — only one survived it]". 15% to 89%: photo in [SETTING], soft window daylight, 35mm f/2.8, background gently out of focus. Center, framed chest up: a friendly man in his early 50s, short gray hair, trimmed salt-and-pepper beard, faded navy work t-shirt, forearms resting on the surface, big genuine smile into the camera, natural skin texture, visible pores, candid, not airbrushed, not CGI. Lower third of the photo, across the surface in front of the person: five units in a single row, [POSE], plain unmarked bodies with no brand names or logos: [RIVAL 1], [RIVAL 2], then [HERO] in the center, slightly larger and closest to the camera, then [RIVAL 3] and [RIVAL 4]. No test result is shown anywhere; the outcome stays hidden. Bottom 11%: a full-width solid bright red band with centered heavy all-caps sans-serif in white: "SEE WHICH ONE". High-contrast, clickbait-thumbnail energy. [ASPECT RATIO] aspect ratio.
```

### 14 — Overhead haul flatlay

```
Use the attached images as reference for product color and details ONLY. Do NOT polish; this should look like a real person's overhead phone photo for a short-video app slideshow, not a styled flatlay. Create: a native haul ad, full-bleed, no border or frame around the image. Full frame: straight-down top view of a light natural oak surface with visible grain, soft indirect daylight from one side, faint natural shadows, smartphone photo quality, slight grain. 6% to 20%, centered: a solid lemon yellow rounded-rectangle caption sticker in native app text style, holding two centered lines of bold sans-serif in black, Title Case: "Best [CATEGORY] for [USE CASE] [YEAR]". 22% to 92%: a loose, overlapping pile of exactly five different units, [HERO], [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], some still in retail packaging with cardboard hang tags, dropped casually, some slightly rotated, edges overlapping, plain unmarked bodies and packaging with no brand names or logos. No hero singled out; the haul is the point. A thin margin of bare surface shows around the pile on all sides. Honest, I-bought-them-all mood. [ASPECT RATIO] aspect ratio.
```

### 15 — Sky blue grid of eight

```
Use the attached images as reference for product details. Do NOT use polished ad layouts; this should look like one slide from a short-video app photo carousel. Create: a native list ad on a flat pale sky blue, full-bleed, no border or frame around the image. 5% to 20%: a solid white rounded-rectangle caption box holding two centered lines of bold sans-serif in black, Title Case: "Best [CATEGORY]" and "(and Some to Avoid)". Below: a grid of clean cutout packshots of exactly five units, [POSE], fronts facing the camera, evenly spaced, equal height: [RIVAL 1], [HERO] and [RIVAL 2] in row one, [RIVAL 3] and [RIVAL 4] in row two. Row one, three units, sits at 25% to 55%; row two, two units centered, at 62% to 92%. Plain unmarked bodies with no brand names, logos or name tags. No rankings, checkmarks or X marks shown; which are best and which to avoid stays hidden, so every viewer scans the grid for the one they already own. Flat, simple, swipe-to-find-out mood. [ASPECT RATIO] aspect ratio.
```

### 16 — 2x2 grid, product plus proof

```
Use the attached images as reference for product color and details ONLY. Do NOT polish; this should look like four real phone photos a person took at home and stitched into a grid in a short-video app. Create: a native comparison ad, full-bleed, no border or frame around the image. The frame is a 2 by 2 grid of four equal photos with thin seams and no gaps. Exactly four photos and exactly four products in the whole image, one product per photo; never split a quadrant into more photos. In each quadrant: one unit on the left (top-left [RIVAL 1], top-right [RIVAL 2], bottom-left [HERO], bottom-right [RIVAL 3]), filling most of the height, [POSE], front facing the camera, plain unmarked body with no brand name or logo, with [PROOF RESULT] shown on or right around that same unit, never as a second unit. One product per quadrant, never a second unit or a duplicate, shot in the same place, at the same angle and distance in all four, so they read as one fair test. Each result looks clearly different from the others, and the difference is the only thing that changes between quadrants. Background: [SETTING], overhead room light, smartphone photo quality, slight grain, shot at eye level with the products. In each quadrant, a lime-green sticky note stuck next to the result with one big handwritten number in black marker: "1", "2", "3", "4". Center, overlapping all four quadrants at 38% to 62% height: a white rounded-rectangle caption box, 90% wide, with three centered lines of bold sans-serif in black, Title Case: "Which of These is the Best [CATEGORY SINGULAR] (And Which is a Waste of Money)?" in plain upright letters, no italics. No winner marked. Raw, curious, side-by-side test mood. [ASPECT RATIO] aspect ratio.
```

### 17 — Cream, same-frame before and after

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts, this should look like a simple native post built from real phone photos. Create: a ad on a flat warm pale cream background, full-bleed, no border or frame around the image. Top 6% to 20%: a centered two-line headline in bold black geometric sans-serif, Title Case, tight leading, reading "See the #1 [CATEGORY SINGULAR] That [THE ONE THING IT DOES]". Middle, 23% to 72%: two photos side by side with a thin cream gap between them, each about 46% wide. Left photo: [BAD SCENE — the exact moment the failure happens, shot in one ordinary place, on a rival of a visibly different design, never the hero]. Right photo: the same place, same angle, same framing, same crop, [GOOD SCENE — the same moment going right because of the hero], so the change reads instantly with nothing else different between the two. Both shot on an iPhone, ordinary available lighting, natural skin texture with real pores if a person is shown, candid, not airbrushed, not CGI. Bottom, 76% to 94%: a single evenly spaced row of five product cutouts on the plain background, similar height, [POSE], fronts facing the camera: [RIVAL 1], [RIVAL 2], [RIVAL 3], then [HERO] in the fourth spot, then [RIVAL 4], plain unmarked bodies with no brand names or logos. No arrows, circles, prices or ranking marks on the row, the viewer has to wonder which one is #1. Clean, plain, native feed look. [ASPECT RATIO] aspect ratio.
```

### 18 — One in each hand

```
Use the attached images as reference for product color and details ONLY. Do NOT polish, this should look like a real creator's phone video frame posted as a native feed image, not an ad. Create: an image, full-bleed, no border or frame around the image. Top 22%: a flat soft warm off-white band with a centered two-line headline in bold black sans-serif, Title Case, reading "Which [CATEGORY SINGULAR] is Better?". Bottom 78%: one candid photo running edge to edge. A smiling man in his early 50s with short gray hair and a trimmed beard, wearing a faded red flannel shirt stands centered, facing the camera with a big genuine smile, holding one product in each hand at chest height, arms slightly forward so both face the lens and fill the lower middle of the frame. Left hand: [RIVAL 1], plain unmarked body. Right hand: [HERO]. Both held at the same height and roughly the same size in frame, neither favored, so the viewer wants to know which one wins. Background: [SETTING], slightly soft. iPhone rear camera quality, wide phone lens feel, warm natural window light, slight grain, natural skin texture with visible pores, candid, not airbrushed, not CGI, no studio setup. No other text, no logos, no arrows. Plain, honest, creator-review mood. [ASPECT RATIO] aspect ratio.
```

### 19 — Overhead pile, don't get scammed

```
Use the attached images as reference for product color and details ONLY. Do NOT polish, this should look like a real person's quick phone photo posted with a native text sticker, not an ad. Create: a overhead photo, full-bleed, no border or frame around the image, of a light honey oak wood table filling the whole frame. From 24% to 94% high: a loose, slightly messy pile of exactly five products, [HERO], [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], laid flat and overlapping at small angles, every product facing up, many still in loud colored retail packaging with no brand names or logos, several with a huge [SPEC CLAIM] and starburst stickers on the front. The hero product is not singled out, it sits in the pile like the rest. Shot straight down from about 60cm on an iPhone, bright soft daylight from a window, faint natural shadows under each product, real surface texture, slight phone grain, no styling. Top 7% to 20%: a centered text sticker in social-video caption style, two lines of bold black sans-serif, each line on its own white rounded-rectangle background hugging the text. Line 1: "🚫 Don't Get Scammed 🚫". Line 2: "By Cheap [CATEGORY]". Nothing else on the image: no logo, no arrows, no circles, no prices. Mood: a friend warning you before you waste money. [ASPECT RATIO] aspect ratio.
```

Other ratios: At wide: three or four rough columns instead of two.

### 20 — Sky blue zigzag roundup

```
Use the attached images as reference. Match the exact product design and colors of each product precisely. Create: a listicle-style roundup ad on a flat soft sky blue background, full-bleed, no border or frame around the image. Top 4% to 20%: a white rounded-rectangle banner about 90% of the width, holding a centered two-line headline in heavy all-caps geometric sans-serif in royal blue, tight leading: "TOP [CATEGORY] THAT ACTUALLY [THE ONE THING THAT MATTERS]". Below, from 23% to 96%: five clean studio cutouts of products floating on the background in a loose staggered zigzag, not a grid, at different heights with slight size differences, each shown at its most recognizable angle facing the camera, no surface, no drop shadow: [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4] plain unmarked bodies with no brand names or logos, plus [HERO]. Arrangement: two products high at upper-left and upper-right (about 23% to 62%), three lower at lower-left, center and lower-right (about 52% to 96%), the center one sitting lowest. The hero product takes one of the upper spots, same size as the others, no badge. Even soft studio lighting, crisp edges, true-to-life colors that contrast gently with the background. No stars, no prices, no extra logos. Clean, trustworthy, editorial "best of" list mood. [ASPECT RATIO] aspect ratio.
```

### 21 — Kitchen table POV

```
Use the attached images as reference for product color and details ONLY. Do NOT polish, this should look like a real creator's short-video frame, not an ad. Create: a candid photo, full-bleed, no border or frame around the image, of a worn oak kitchen table against a plain light gray wall. Left 35%, from 5% to 58% high: a man in his early 50s with a short gray beard, gray t-shirt seated at the table, one forearm resting on it, [HERO IN USE — him using the hero the way this category is actually used, held so the product reads clearly], eyes looking straight into the lens with a quiet, satisfied expression. Bottom 45%: the table surface. Across the center and right, from 35% to 100% wide: a crowded row of five competing units on the table, [POSE], the hero in front nearest the person, the others partly overlapping behind it and cut off at the right edge, with plain unmarked bodies with no brand names or logos. In front of the products, laid directly on the table with no dish or tray: each unit's own [PROOF ITEM], each one tagged with a strip of masking tape handwritten in black marker with a number "1", "2", "3", "4", "5". Upper right, 12% to 32%: a caption in social-video style, three centered lines of bold black sans-serif, each line on its own white rounded background: "POV: you tested all the popular [CATEGORY] and finally found one that [THE ONE THING THAT MATTERS]". iPhone rear camera, soft bright indoor daylight, slight grain, natural skin texture with visible pores, candid, not airbrushed, not CGI. Mood: the end of a long, honest test. [ASPECT RATIO] aspect ratio.
```

### 22 — 2x2 grid with scores

```
Use the attached images as reference for product color and details ONLY. Do NOT polish, this should look like four real phone photos stitched into a grid for a native post, not an ad. Create: a 2x2 photo grid, full-bleed, no border or frame around the image, each quadrant exactly half the width and half the height, separated only by thin white gutter lines about 1% wide. Each quadrant is its own phone photo taken at the same spot in [SETTING], same angle and distance, so the four read as one fair test. In each quadrant: one competing unit in the left 60%, [POSE], facing the camera, plain unmarked body with no brand name or logo. To the right of each product: [PROOF RESULT] for that unit, each one visibly different from the others. At the bottom edge of each quadrant: a lime green sticky note with a handwritten score such as "7/10", partly cut off by the frame. No quadrant is marked as the winner. Dead center, straddling the horizontal gutter: a white rounded-rectangle caption about 80% wide with two centered lines of bold black sans-serif: "Which [CATEGORY SINGULAR] Did We Rank #1 Best in [YEAR]?". iPhone rear camera, bright warm indoor light, soft shadows, slight grain, real textures, one ordinary prop at an edge. Mood: an honest side-by-side you want the answer to. [ASPECT RATIO] aspect ratio.
```

### 23 — Tabletop row plus sticky note

```
Use the attached images as reference for product color and details ONLY. Do NOT polish, this should look like a real person's straight-on phone photo of a home test, not an ad. Create: a photo, full-bleed, no border or frame around the image, on a plain matte warm white tabletop that fills the frame, with a soft natural falloff toward the corners. Top 8% to 40%: four products from the same category in one evenly spaced row on the same base line, all presented the same way, [POSE], fronts facing the camera, plain unmarked bodies with no brand names or logos, sizes matched so no one product dominates the row: three rivals in three different colours, plus [HERO]. The hero is one of the four, not singled out: no badge, no circle, no arrow, no halo. Directly in front of each product, 43% to 60%: its own [PROOF ITEM], one per product, laid directly on the tabletop in the same orientation and at the same size, nothing holding them, and no dishes, bowls, trays, saucers or lids of any kind anywhere in the frame. The four proofs look nearly identical on purpose, so nothing visual gives the winner away. Centered below, 64% to 92%: a square bright yellow sticky note stuck flat on the surface, slightly off-level, with three or four lines of casual handwriting in black marker reading "[CLAIM]". Shot straight on from slightly above at 50mm on an iPhone, bright soft daylight, gentle realistic shadows, true colors, slight phone grain. No other text, no arrows, no circles, no logo overlay. Mood: a quiet, credible personal experiment. [ASPECT RATIO] aspect ratio.
```

### 24 — Research table with log

```
Use the attached images as reference for product color and details ONLY. Do NOT polish, this should look like a real person's phone photo of their own research table, not an ad. Create: a photo, full-bleed, no border or frame around the image, shot from standing height at about 40 degrees down onto a light pine kitchen table in a lived-in family kitchen with wood cabinets, a coffee maker and a dining table with chairs behind. Back of the table, 40% to 68% high: a row of exactly five competing units side by side, [POSE], left to right: [RIVAL 1]; [RIVAL 2]; [HERO]; [RIVAL 3]; and [RIVAL 4]. Plain unmarked bodies with no brand names or logos. Also on the table, [TWO OLD-WAY PROPS — the low-tech things people used before this category existed] at the far left. Front of the table, 58% to 100%, loosely laid out like real homework: on the left two printed pages titled "[PRINTED DOCUMENT — the official-looking page a worried buyer would print]"; in the center a crumpled white paper towel holding [FAILURE DEBRIS]; on the right a spiral notebook with a handwritten three-column log headed "[CHECK 1]", "[CHECK 2]", "[CHECK 3]", exactly five rows numbered "1" to "5" in the same left-to-right order as the units, with no product names written anywhere, checkmarks and X marks under each, and only row 3, the middle unit, all checkmarks; nothing else written on the page below the log; a blue pen and a phone face down at the edge. Top 12% to 28%: two centered lines of bold white sans-serif, each line on its own black rounded-rectangle caption bar. Line 1: "[PROBLEM LINE — why yours fails, stated as a fact]". Line 2: "And the one that doesn't...". iPhone rear camera, bright warm window light, soft shadows, slight grain, real paper and handwriting, no styling. Mood: an insider tip backed by homework. [ASPECT RATIO] aspect ratio.
```

Other ratios: At 9:16: the units in one overlapping back row at 26–44%, the homework at 46–80% with the notebook center-front.

### 25 — Money spent, meter bar

```
Use the attached images as reference. Match the exact product design, colors, and typography precisely. Create: a clean designed comparison graphic on a soft light gray fading to white at the center, full-bleed, no border or frame around the image. Top 20%: two centered lines of heavy all-caps condensed sans-serif in near-black, filling about 85% of the width, reading "I SPENT [PRICE SPENT] ON [CATEGORY]". From 26% to 50%: one evenly spaced horizontal row of exactly five competitor products, [POSE], with plain unmarked bodies with no brand names or logos, facing the camera, heights and shapes varying naturally, soft contact shadows on an invisible floor, and a few loose [PROOF ITEM] resting between two of them. The rightmost product is the hero: heavily gaussian-blurred so no branding can be read, wrapped in a soft warm white halo, with a gold rosette ribbon badge reading "#1" on its upper-right corner. At 54%: a small solid upward triangle centered under each product, colored in sequence from red through orange and yellow to bright green under the hero. A thin gray dashed vertical line drops from each triangle to a wide rounded horizontal meter bar spanning 70% to 77% of the height, filled with a smooth left-to-right gradient from red to bright green, thin white rim, faint outer glow. From 83% to 93%: one centered line of heavy all-caps condensed sans-serif in deep forest green reading "ONLY ONE WAS WORTH IT". Bright flat studio lighting, crisp e-commerce cutout look, generous white space, no other text. [ASPECT RATIO] aspect ratio.
```

Other ratios: Full-width bands at every ratio, all seven products in one row so each lines up with its triangle and the meter.

### 26 — Testing table with notepad

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's phone photo of their own testing table. Do NOT polish: no studio lighting, slight phone grain, natural clutter. Create: a photo, full-bleed, no border or frame around the image, shot standing at the end of a worn light oak kitchen table angled 45 degrees down, a bright window along the top edge in soft overcast daylight. From 12% to 24%: two centered caption lines in white bold rounded sans-serif, each on its own black rounded-rectangle text box, line one "I tested 5 popular [CATEGORY]" with "5 popular [CATEGORY]" in pale butter yellow, line two "so you don't have to.". From 30% to 50%: three competitor units spread loosely across the back, plain unmarked bodies with no brand names or logos. Lower half: two more units at front left, five units in total, each with its own [PROOF ITEM] laid on a crumpled white paper towel in front of it. Center: a printed page headed "[PRINTED DOCUMENT]" with the name blacked out, and on top a spiral notepad with a hand-drawn three-column table in blue ballpoint: headers "[TIME 1]", "[TIME 2]", "[TIME 3]", entries "5 [CATEGORY]", "3 left", "1 left", the count clearly dropping out left to right. Around it: a blue click pen on the pad, tortoiseshell reading glasses, a white mug of black coffee cropped at the right edge. Smartphone main camera quality, deep focus, true-to-life colors. [ASPECT RATIO] aspect ratio.
```

### 27 — Six-selfie collage

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's five phone selfies stitched into one collage in a free app. Do NOT polish: no retouching, no studio lights, no matched color grading between tiles. Create: a collage, full-bleed, no border or frame around the image, five tiles separated only by hairline white gutters, the outer tiles running to the edges: three equal portrait tiles in the top row, two equal wider tiles in the bottom row. Every tile shows the same man in his mid 40s with a trimmed dark beard going gray, faded navy ball cap, gray t-shirt, arm's-length front-camera selfie, big genuine grin, natural skin texture with visible pores and slight shine, candid, not airbrushed, not CGI. In each tile he has a different competitor unit, plain unmarked with no brand name or logo, [WORN OR HELD — worn on the body for anything wearable, held up close to the lens beside his face for anything else], the product filling about 45% of the tile and slightly distorted by the wide lens. Each tile is a different corner of the same home: cabinets, an appliance, a window, a painted wall sign. Mixed indoor daylight and warm ceiling light, slight phone grain, some tiles slightly tilted or cropped at the forehead. Centered, straddling the seam between the two rows: a rounded-rectangle banner tag in burnt orange with bold white all-caps sans-serif reading "SEE WHO WINS", about 45% of the frame width. No other text overlay. Smartphone front camera quality. [ASPECT RATIO] aspect ratio.
```

### 28 — Counter pile with scrim

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like the cover slide of a real person's photo carousel on a short-video app. Do NOT polish: phone photo, slightly messy pile, no studio lighting. Create: a photo, full-bleed, no border or frame around the image, of a bright white-cabinet kitchen with a stainless steel fridge in soft daylight, shot at counter height with a smartphone main camera. Top 60%: a crowded, casually stacked pile of exactly five competitor units of all sizes, all different designs, plain unmarked bodies with no brand names or logos, facing the camera, overlapping in two loose rows across the counter, tallest items at the back, and an opened cardboard shipping box cut off by the right edge. Bottom 45%: a smooth vertical gradient from transparent to near-black at 85% opacity so the pile fades into it while the upper photo stays bright. Over the scrim, centered: "[PROBLEM LINE — stop buying the ones that fail this way]" in bold white sentence-case sans-serif, three lines, tight leading, about 88% of the width, from 60% to 80% of the height. Below at 84%: "Here's the BEST (+ WORST) of them" in regular white sans-serif, about half the headline size, the two ranking words in all caps. At 91%: a small white outline button, fully rounded, holding a thin right-pointing arrow as the swipe cue. Straight-on angle, deep focus on the pile, true-to-life colors. [ASPECT RATIO] aspect ratio.
```

### 29 — Overhead flat-lay, orange line

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's cover photo for a short video, shot straight down with a phone. Do NOT polish: natural daylight, real soft shadows, tiny imperfections in the surface and spacing. Create: an image, full-bleed, no border or frame around the image, split into a photo zone and a text zone. Top 64%: a flat-lay shot from directly overhead on a smooth off-white countertop in bright window daylight. From 10% to 38%: a single row of four competitor units lying flat and evenly spaced, plain unmarked bodies with no brand names or logos, facing up, each a different color and style. From 42% to 58%: directly in front of each product, its own [PROOF ITEM], four visibly different versions of the same kind of thing laid in one row so they can be compared side by side, nothing holding them. A thin safety orange horizontal line runs edge to edge at 64%. Bottom 36%: plain white with a centered headline in heavy bold black sans-serif Title Case, tight leading, two or three lines filling about 80% of the width, reading "Popular [CATEGORY] Ranked Best to Worst". No rank numbers, no logos, no other text anywhere. Smartphone main camera quality, straight overhead, deep focus, crisp true-to-life colors. [ASPECT RATIO] aspect ratio.
```

### 30 — Overhead foam board, question marks

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's overhead phone photo for a ranking video. Do NOT polish: slightly uneven spacing, natural indoor daylight, soft real shadows. Create: a photo shot from directly overhead, full-bleed, no border or frame around the image, on a matte white foam board that fills the entire frame edge to edge, only a sliver of floor visible at the two top corners. From 8% to 36%: a row of four competitor units lying flat, plain unmarked bodies with no brand names or logos, facing up, edges slightly overlapping. From 40% to 64%: directly below each product, what came in its box, four visibly different versions of [PROOF ITEM], evenly spaced in one row. From 72% to 86%: one square sticky note centered under each column in lemon yellow, coral pink, aqua, tangerine, stuck slightly crooked, each hand-written in thick black marker with "#?". The rank marks are the only text in the image. Bottom 10%: empty surface. Smartphone main camera quality, straight overhead, deep focus, true-to-life colors, clean and bright. [ASPECT RATIO] aspect ratio.
```

### 31 — Dry-erase board, pointing

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's cover frame for a short video filmed at home on a phone. Do NOT polish: no studio lights, no retouching, casual framing. Create: a photo, full-bleed, no border or frame around the image, in [SETTING], bright with daylight coming in. Left 35%, from 4% down to 72%: a man in his early 50s with a short gray beard, navy t-shirt under a tan canvas work apron with leather straps, his whole head and face fully in frame with a little headroom above his hair, eyes at about 18% of the height, looking into the lens, warm genuine smile, natural skin texture, candid, not airbrushed, not CGI, his right arm extended with the index finger pointing at the board. Center-right, from 38% to 92% of the width and 12% to 52% of the height: a white dry-erase board with a thin aluminum frame on a black tripod easel. On it, hand-written in marker: line one "[CATEGORY]:" in dark maroon, line two "Ranked Best to Worst!" in black, and below a simple black doodle of [CATEGORY SINGULAR]. Bottom 30%: exactly five competitor units of mixed sizes with plain unmarked bodies with no brand names or logos, on a table, crowded shoulder to shoulder and cropped by the bottom edge. Floating above each product: a hand-drawn bright yellow question mark with a thin black outline, slightly tilted, sticker style. Smartphone rear camera, 26mm equivalent, bright natural daylight, slight softness. [ASPECT RATIO] aspect ratio.
```

Other ratios: At 9:16: board full width at 16–42%, the man at 38–72% pointing up at it with his eyes around 45%, the products at 70–88% running into the bottom margin.

### 32 — Dry-erase board, hero in use

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's cover frame for a short video filmed at home. Do NOT polish: phone camera, mixed indoor light, lived-in background. Create: a photo, full-bleed, no border or frame around the image, in a kitchen with warm honey oak cabinets and a stainless microwave, shot at chest height, straight on. Left 45%, from the top edge to 70%: a friendly man in his late 40s with a short salt-and-pepper beard, faded navy ball cap, gray t-shirt under an open tan canvas work jacket, relaxed proud smile looking into the lens, natural skin texture, visible pores, candid, not airbrushed, not CGI. [HERO IN USE — he is using the hero at chest height toward the camera, doing the one thing this category is bought for, so the proof is visible in frame]. Right side, from 50% to 95% of the width and 28% to 58% of the height: a white dry-erase board with a thin silver frame propped on the counter, hand-written in black marker in three lines, casual uneven handwriting, reading "[CATEGORY] / Ranked / Best to Worst". Bottom 32%: a light counter across the full width, with five competitor units at the back with plain unmarked bodies with no brand names or logos, and directly in front of each one its own [PROOF ITEM], so the difference is obvious at a glance. Smartphone rear camera quality, 26mm equivalent, deep focus, true-to-life warm colors, slight phone sharpening. [ASPECT RATIO] aspect ratio.
```

### 33 — Tier list, S tier hidden

Source: original, no source image, built from the T5-01..32 mechanics (ranking + hidden winner), added 2026-10-09. Drawn at 1:1.

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a tier-list ranking graphic, full-bleed, no border or frame around the image, on a flat dark charcoal background. Top 4% to 16%: a centered heavy all-caps sans-serif headline in white, tight leading, reading "[CATEGORY] TIER LIST". From 18% to 96% height: five full-width horizontal tier rows stacked with thin charcoal gaps about 1% tall, each row about 14% tall. Left 18% of each row: a square label cell holding one big heavy black letter, top to bottom "S" on coral red, "A" on tangerine orange, "B" on butter yellow, "C" on lime green, "F" on sky blue. Right 82% of each row: a flat medium gray track. Products are clean cutout packshots, each about 13% of the frame width and as tall as the row allows, [POSE], fronts facing the camera, left-aligned in their track with small even gaps, soft contact shadows. Row S: one solid near-black silhouette the size of a product with a big white "?" centered on it, nothing else. Row A: [RIVAL 1]. Row B: [RIVAL 2] and [RIVAL 3]. Row C: empty track. Row F: [RIVAL 4]. Rivals have plain unmarked bodies, no brand names, logos or captions anywhere on or beside them. Flat graphic, crisp edges, no other text. Scroll-stopping, who-made-S-tier curiosity. [ASPECT RATIO] aspect ratio.
```

Other ratios: At wide: tier rows keep full width, each row about 15% tall, headline as a top band; products about 9% of the width.

### 34 — Return box, one keeper

Source: original, no source image, added 2026-10-09. Drawn at 1:1.

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's phone photo of their returns pile, not an ad. Do NOT polish: slight phone grain, everyday clutter, no studio light. Create: a photo, full-bleed, no border or frame around the image, on a light kitchen counter in [SETTING], soft window daylight, shot from standing height at a slight downward angle. Left 58%, from 30% to 96% height: an open brown cardboard shipping box with its flaps up, a white printed shipping label on its side with a big black "RETURN" and a barcode, a roll of packing tape beside it. Tossed into the box at careless angles, half out of their packaging and each still visible above the rim: exactly four competitor units, [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies with no brand names or logos. Right 42%, from 40% to 88% height: [HERO] alone on the counter, [POSE], front facing the camera, upright and clearly kept, and on the counter in front of it a square lime-green sticky note handwritten in thick black marker: "KEEPER". Top 5% to 22%: two centered lines of bold white sans-serif, each line on its own black rounded-rectangle caption bar. Line 1: "I returned 4 of the 5 [CATEGORY] I bought". Line 2: "Here's the one I kept 👇". Smartphone main camera, 26mm equivalent, deep focus, true-to-life colors. Honest, I-already-made-the-mistakes mood. [ASPECT RATIO] aspect ratio.
```

### 35 — Podium, gold step under a cloth

Source: original, no source image, added 2026-10-09. Drawn at 1:1. Hero giấu dưới khăn: vẫn gắn đủ 5 ảnh (luật 8) nhưng khoá hero dưới khăn (xem "Tấm vẽ hàng hỏng"), máy hay đặt nó lên bục 2.

```
Create: a ranking ad, full-bleed, no border or frame around the image, in a clean studio on a seamless warm off-white backdrop, soft even studio light, shot straight on at 50mm f/5.6. Top 4% to 18%: two centered lines of heavy black sans-serif, Title Case, tight leading: "We Ranked 5 [CATEGORY]." and "Only One Got Gold.", with "Gold" in metallic gold. From 30% to 86% height, centered and 80% wide: a three-step matte white winners' podium, the center step tallest, with big numerals on the front faces: gold "1" in the center, silver gray "2" on the left, bronze "3" on the right. On step 2: [RIVAL 1], [POSE]. On step 3: [RIVAL 2], [POSE]. On step 1: one object fully hidden under a draped deep red velvet cloth, about the size of the other products, only a soft rounded shape showing, a small gold tag hanging off the cloth with a black "?". On the floor in front of the podium, lower-left and lower-right at 76% to 94% height: [RIVAL 3] and [RIVAL 4], [POSE], slightly turned away, unranked. All rivals have plain unmarked bodies, no brand names, logos or captions. Soft contact shadows, no other text. Awards-night suspense, who-got-gold curiosity. [ASPECT RATIO] aspect ratio.
```

### 36 — Box claim vs measured

Source: original, no source image, added 2026-10-09. Drawn at 1:1.

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: an infographic comparison ad on a flat white background, full-bleed, no border or frame around the image. Top 4% to 16%: a centered heavy all-caps condensed sans-serif headline in near-black, two lines, tight leading: "WHAT THE BOX SAYS" and "VS. WHAT WE MEASURED". From 19% to 48% height: five products in one evenly spaced row, each about 17% of the width, [POSE], front facing, bottoms aligned, soft contact shadows: [RIVAL 1], [RIVAL 2], [HERO] in the center, [RIVAL 3], [RIVAL 4], rivals with plain unmarked bodies, no brand names or logos. From 52% to 90%: a clean thin-line table with five columns lined up under the five products and two rows. Above the first row, small gray all-caps label at the left edge: "CLAIMED ([SPEC UNIT like lumens])". First row, one bold black number per column: "[RIVAL CLAIM 1 like 2000]", "[RIVAL CLAIM 2 like 1500]", "[HERO CLAIM like 500]", "[RIVAL CLAIM 3 like 1800]", "[RIVAL CLAIM 4 like 3000]". Above the second row, small gray all-caps label: "TESTED". Second row: the four rival cells in bright red with a small red down arrow, "[RIVAL RESULT 1 like 410]", "[RIVAL RESULT 2 like 380]", "[RIVAL RESULT 3 like 520]", "[RIVAL RESULT 4 like 290]"; the hero cell in forest green with a checkmark, "[HERO RESULT like 540]". Bottom 93% to 97%: one small centered line in mid gray: "[TEST NOTE like Same test, same day, same room]". Flat vector clarity, no shadows on the table, no other text. Data-report, myth-busting feel. [ASPECT RATIO] aspect ratio.
```

### 37 — Phone notes ranking, #1 blacked out

Source: original, no source image, added 2026-10-09. Drawn at 1:1.

```
Use the attached images as reference for product color and details ONLY. Do NOT use polished ad layouts. This should look like a real person's phone screenshot of a plain notes app, not an ad. Create: a native screenshot, full-bleed, no border or frame around the image, of a notes-app page with a white background and a faint warm paper tint. Top 0% to 4%: a thin phone status bar with the time "9:41", signal and battery icons. 5% to 8%: a small yellow "‹ Notes" back link at the left. 10% to 16%: the note title in heavy black system sans-serif: "[CATEGORY] I tested (honest ranking)". From 18% to 48%: a photo inserted in the note, rounded corners, 92% wide: a candid phone photo in [SETTING] of exactly five units side by side, [POSE], plain unmarked bodies with no brand names or logos, none singled out, slight grain, ordinary indoor light. From 52% to 94%: a numbered list in regular black system sans-serif, one line each, left-aligned: "1. ███████ ✅ [WIN REASON like the only one still working after a month]", with the product words covered by a solid black redaction bar; "2. the [RIVAL 1 SHORT like gray one] – [FLAW 1 like good, but the clip snapped]"; "3. the [RIVAL 2 SHORT like red one] – [FLAW 2 like died in two weeks]"; "4. the [RIVAL 3 SHORT like tall one] – [FLAW 3 like cheap feel] ❌"; "5. the [RIVAL 4 SHORT like black one] – [FLAW 4 like returned it] ❌". No keyboard, no other UI. Crisp screenshot, real system font, flat. Mood: a friend's private notes you weren't meant to see. [ASPECT RATIO] aspect ratio.
```

### 38 — Survivor stamps

Source: original, no source image, added 2026-10-09. Drawn at 1:1.

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a ranking ad, full-bleed, no border or frame around the image, on a flat light concrete gray background with fine real texture. Top 4% to 20%: two centered lines of heavy all-caps condensed sans-serif in near-black, tight leading: "5 [CATEGORY] WENT IN." and "1 CAME OUT.", with "1" in bright green. At 23% to 29%: a centered black rounded pill with white all-caps text: "[TEST NAME like 90-DAY DAILY-USE TEST]". From 34% to 76% height: five products in one evenly spaced row, each about 17% of the width, [POSE], front facing, bottoms aligned, soft contact shadows: [RIVAL 1], [RIVAL 2], [HERO] in the center, [RIVAL 3], [RIVAL 4], rivals with plain unmarked bodies, no brand names or logos. Stamped diagonally across each of the four rivals: a big red rubber-stamp "FAILED" in distressed all-caps with real ink texture, each rotated a little differently, partly transparent so the product still reads through it. The hero has no stamp. Under each product at 80% to 87%: a short caption in dark gray handwritten-style marker: "[DAY 1 like Day 9]", "[DAY 2 like Day 23]", then under the hero in forest green "Still going", then "[DAY 3 like Day 41]", "[DAY 4 like Day 60]". Crisp packshot lighting, no other text. Brutal, last-one-standing feel. [ASPECT RATIO] aspect ratio.
```

### 39 — Listing photo vs what showed up

Source: original, no source image, added 2026-10-09. Drawn at 1:1. Ô phải vẽ hàng đối thủ xuống cấp: gắn đủ 5 ảnh (luật 8), khoá món xuống cấp là `[RIVAL 1]`, sp mình chỉ xuất hiện nguyên vẹn.

```
Create: a native comparison ad, full-bleed, no border or frame around the image. Top 0% to 14%: a flat white band with a centered two-line headline in heavy black sans-serif, Title Case, tight leading: "Cheap [CATEGORY] Online vs. What Actually Shows Up". From 14% to 62%: two panels side by side, 50% each, meeting at a thin white seam. Top-left corner of each panel: a small black tag with white all-caps text, "THE LISTING" on the left, "WHAT ARRIVED" on the right. Left panel only is polished: [RIVAL 1] as a glossy, over-lit catalog render floating on pure white, flawless, too-perfect CGI look, with a loud starburst sticker beside it reading "[SPEC CLAIM like 3000 LUMENS!]". Right panel: do NOT polish, a real phone photo of the same rival design on [SETTING], flat overhead room light, slight grain, [ARRIVED STATE like thinner cheaper material, a crooked seam, one part already loose], a torn plastic mailer bag beside it. Both show plain unmarked bodies with no brand names or logos. At 64% to 70% height: a full-width rounded pill bar in pale cool gray with centered bold black sans-serif Title Case text: "Top [CATEGORY] Tested & Ranked". Bottom 28%: pure white strip with five products in one evenly spaced row, each about 17% of the width, front-facing, bottoms aligned, [POSE], soft contact shadows, [HERO] in the center slot, flanked by [RIVAL 1], [RIVAL 2], [RIVAL 3] and [RIVAL 4], plain unmarked bodies, no captions under the row. Relatable, been-burned-before feel. [ASPECT RATIO] aspect ratio.
```

### 40 — Price tags, hero's tag flipped

Source: original, no source image, added 2026-10-09. Drawn at 1:1.

```
Use the attached product images as reference. Match the exact product design and colors of each product precisely. Create: a ranking ad, full-bleed, no border or frame around the image, on a flat warm cream background. Top 4% to 22%: two centered lines of heavy sans-serif, Title Case, tight leading: "We Tested 5 [CATEGORY] From [LOW PRICE like $12] to [HIGH PRICE like $89]" in black, then "The Winner Wasn't the Priciest" in bright red. From 30% to 66% height: five products in one evenly spaced row, each about 17% of the width, [POSE], front facing, bottoms aligned, soft contact shadows, sorted left to right: [RIVAL 1], [RIVAL 2], [HERO], [RIVAL 3], [RIVAL 4], rivals with plain unmarked bodies, no brand names or logos. Tied to each product with a thin white string: a manila paper price tag with a reinforced hole, lying on the surface in front of it at 68% to 86%, each at a slightly different angle, handwritten in black marker: "[LOW PRICE like $12]", "[PRICE 2 like $24]", then the hero's tag flipped to its blank back with only a big handwritten "?", then "[PRICE 4 like $65]", "[HIGH PRICE like $89]". Bottom 90% to 96%: one small centered line in mid gray: "Ranked by testing, not by price tag". 50mm f/5.6, soft even studio light, crisp true colors, no other text. Smart-shopper surprise. [ASPECT RATIO] aspect ratio.
```

---

## Ghi chú drift

Template cũ bake cứng chữ ngành ở 9 chỗ, đã slot hoá hết: 9 (bowls đựng pin), 10, 12, 21, 23, 26, 29, 30, 32 đều dùng "the batteries or cable it runs on", nay là `[PROOF ITEM]`.
Prompt 23 còn bỏ hẳn `small round white dish`, prompt 21 bỏ `small white dishes`, vì model render thành nắp hũ trắng và prop đó không mang nghĩa gì. Proof nằm thẳng trên mặt bàn.
`standing on their tails` ở 2, 5, 11, 13, 15, 22, 23 nay là `[POSE]`, để mũ và giày không phải đứng.

---

## Bổ sung — bài học từ các lô đã chạy

### Khi gắn ảnh THẬT của đối thủ làm reference

Gắn ảnh thật giải quyết rủi ro lớn nhất: máy vẽ năm cây na ná nhau và ảnh đọc thành
*"một sản phẩm chụp năm lần"* thay vì *"năm sản phẩm được so sánh"*.

Nhưng ảnh thật mang theo **tên hãng in trên sản phẩm**. Nhúng câu này vào mọi prompt có đối thủ:

> *each photographed turned so that any printed lettering or brand name on its body is rotated fully away from the camera and is not visible*

Giữ được hình dáng thật, bỏ được cái tên. **Gen xong phóng to soi từng sản phẩm — lọt một chữ là bỏ tấm đó.**
Meta hay từ chối quảng cáo hiển thị nhãn hiệu hãng khác, kể cả khi so sánh đúng sự thật.

### Nếu KHÔNG gắn ảnh thật

Phải tả **hình dáng khác hẳn nhau** cho từng `[RIVAL]`, không chỉ khác màu.
Ví dụ ngành đèn bút: *đèn móc khoá bạc lùn · đèn bút đen dài nút to · đèn đen ngắn kẹp hai chiều ·
đèn bạc vặn đầu có khoen*. Để máy tự do là nó vẽ năm cái giống nhau.

### Luật chữ và số

- **Không bao giờ in con số thông số của sản phẩm mình** nếu con số đó đang bị chính khách phản bác.
  Ví dụ đã gặp: listing ghi 500 lumens, khách viết *"Not a 500 lumen light"*.
  Con số đó chỉ được xuất hiện **kèm dấu hỏi** (như một lời tố) hoặc trong câu tự nhận lỗi.
  Được in số hãng khác tự công bố (47, 54, 180) vì kiểm chứng được.
- **Tối đa một cụm chữ** mỗi tấm, trừ template có cấu trúc bảng/checklist rõ ràng.
- **Soi từng ký tự.** Sai một chữ là bỏ, không sửa Photoshop.

### Quy trình chạy một lô

1. **Gen một tấm nhiều chữ trước tiên** (template 1, 3 hoặc 11) làm QA.
   Chữ ra sai là dừng, đổi model. Đừng đốt cả lô khi chưa biết model viết chữ được không.
2. Ba tấm trụ tiếp theo: một tấm **bảng số**, một tấm **so sánh hình**, một tấm **xếp hạng 1–5**.
   Ngân sách chỉ đủ ba creative thì chạy đúng ba tấm đó.
3. Hook lạnh, rồi phần còn lại.

### Tấm vẽ hàng hỏng: gắn đủ 5 ảnh nhưng khoá chặt ai hỏng

Trước đây các tấm 4, 7, 8, 12, 17, 24, 35, 39 chạy text-to-image (xoá hết reference). Từ 2026-10-09 theo luật 8 vẫn gắn đủ 5 ảnh. Rủi ro cũ vẫn còn: máy có thể vẽ **chính hàng mình** bị gãy, ăn mòn, bục chỉ (đã suýt dính hai lần). Nên ở các tấm này:
- Món hỏng phải gọi đích danh bằng câu khoá của `[RIVAL]`, và viết thêm câu: our product (the first attached image) appears only intact and in its good state, never damaged.
- Tấm 35 (hero giấu dưới khăn): thêm `our product (the first attached image) is the one hidden under the cloth and must not appear anywhere else`.
- Gen xong soi kỹ: sp mình mà hỏng là bỏ tấm, sửa câu khoá, gen lại.

Tấm proof (5, 16, 21, 22, 29, 32...): gắn đủ 5 ảnh thì máy hay chép lại packshot sạch và mất proof. Viết khác biệt proof là "the whole point of the photo and must be obvious", tả rõ trạng thái tốt của sp mình và trạng thái xấu của từng đối thủ.

Prompt các tấm trên vẫn phải **gọi tên từng sản phẩm** bằng `[HERO]` và `[RIVAL 1..4]`, và `[POSE]` phải nói rõ đây là món gì (ví dụ "a loose, empty fabric cover, no seat inside"). Đã gặp ở tấm 24, ngành tấm phủ ghế: template cũ chỉ ghi "five competing units, in five different colours" cộng pose "fitted on an invisible car seat", máy vẽ ra 5 cái ghế ô tô 5 màu. Cuốn sổ cũng phải khoá: đánh số dòng, không ghi tên sp, chỉ dòng của hero toàn dấu tích. Nếu để tự do, máy tự viết "gray quilted = best so far" khen đối thủ.

### Tấm mạnh nhất thường là tấm tự nhận mình không nhất

Ví dụ đã dùng: năm cây đèn cùng chiếu lên một bức tường, và cây của mình **không phải**
vũng sáng to nhất. Trong ngành mà mọi listing đều hét một con số bịa, tấm ảnh dám xếp
hàng mình đứng thứ hai là thứ đáng tin nhất mua được. Nếu gen ra mà mình to nhất thì gen lại.

### Xuất file cho tool gen

File prompt (`.md`) phải là **CRLF**, các prompt cách nhau bằng `\r\n\r\n`, **chỉ có prompt**,
mỗi prompt mở đầu bằng số thứ tự `1. `, `2. `… (the user muốn vậy để tìm prompt theo số), không tên template, không dòng trống thừa.
Notepad trên Windows gộp LF-only thành một dòng, và mọi dòng chữ giữa các prompt đều bị
tool đếm thành một prompt riêng.

### Checklist trước khi đăng

- [ ] Đếm sản phẩm: tấm nói "năm" phải đúng năm, tấm nói "ba" phải đúng ba, không tấm nào quá 5 sản phẩm
- [ ] Năm sản phẩm khác hình dáng nhau rõ rệt
- [ ] Soi từng ký tự mọi dòng chữ
- [ ] Không tên brand, không logo nào (thật hay bịa) trên thân sản phẩm
- [ ] Không tên sản phẩm mình, không wordmark nhà mình (ads dắt về trang Top 5 đóng vai
      site đánh giá độc lập — dán logo mình vào là khách hiểu ngay đây là quảng cáo trá hình)
- [ ] Đếm ngón tay
- [ ] Tấm có người: sản phẩm đúng tỉ lệ thật so với người. Hàng to (bed, ghế, túi lớn) hay bị vẽ thành đồ chơi; ghi kích thước thật trong prompt ("about 50 cm across, roughly as wide as her shoulders, never miniature or toy-sized") (cat bed 2026-10-16, tấm 13)
