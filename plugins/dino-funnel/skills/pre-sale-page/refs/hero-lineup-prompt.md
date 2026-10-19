# Hero prompt: 5 san pham canh nhau trong boi canh that

Dung cho o `.compare-photo` (`lineup.webp`, 1440x810) cua moi trang top-5.
Ref: 2 anh the user gui 2026-09-26 (magnesium bottles + sea moss tren mat bep granite).

**Co che (giu nguyen khi doi nganh hang):** mot tam chup that tren mat bep nha
minh, ca 5 san pham dung canh nhau so le chieu sau, hang dung GIUA va gan may
nhat, va truoc mat moi cay la BANG CHUNG cung loai de nguoi doc so sanh mot
phat. KHONG ghep 5 anh listing lai.
**KHONG ANH VANG (anh Huy 2026-09-30):** cam tungsten/warm/golden. Luon ghi daylight 5500K + cau phu dinh "no yellow, orange or amber color cast". Ban holster dau tien ra ngon mau cam vang, bi loai.
**BOI CANH PHAI HOP NGANH HANG, KHONG mac dinh bep:** hoi "nguoi mua se bay may mon nay ra o dau?". Bep chi cho do an / supplement / do bep. Holster, flashlight, tool -> workbench garage. Quan ao, vest -> giuong phu chan xam tron. Pet -> san phong khach / hien nha. Holster dat trong bep bi anh Huy loai 2026-09-30.
**KHONG khoanh do / mui ten / chu.** Anh ref khong co bat ky do hoa nao (anh Huy nhac 2026-09-29).
Hang o giua chi nhich len truoc mot chut, khong phong to qua muc.

## Template prompt

```
Use the attached images as reference for the [PRODUCT CATEGORY like pocket pen light] shapes, colors and label details ONLY. Do NOT build a collage, a grid, a split screen or a polished studio ad. This must read as one continuous photograph a real person took of everything they bought, on their own counter, with their phone.

Create: five competing products of the same kind standing together in a single shot on [SURFACE like a worn light-oak wooden workbench], with [SETTING like a clean home garage, a white pegboard wall with a few hand tools] softly out of focus behind them. Stagger them in depth so it does not read as a straight line: two set slightly back and partly overlapping, two slightly forward. [HERO like a matte black machined-aluminium pen light, shown as all three lights of its three-pack] sits dead center, closest to camera and largest in frame, square to the lens with its branding fully legible. To its left [COMPETITOR A like a black Coast G19 penlight with a red band] and [COMPETITOR B like a long grey Streamlight Stylus Pro]; to its right [COMPETITOR C like a short black Lumintop Tool AAA with a keyring clip] and [COMPETITOR D like a slim black Maglite Solitaire], each turned so its own branding reads.

Lying loose on the counter in front of each product, place [PROOF like the actual units that come in that box, unpacked: three identical lights in front of the hero and one single light in front of every competitor], keeping the same kind for all five so they compare at a glance. The hero's is [WIN like three where every other product has one].

Lighting: soft daylight, neutral white balance around 5500K, true-to-life colors, whites read as clean white and blacks as neutral black. No yellow, orange or amber color cast, no warm tungsten light, no golden-hour glow, no cinematic grading. 35mm at f/4 from a slightly raised angle, moderate depth of field so all five stay readable, mild phone-camera grain, slightly imperfect framing, no retouching, no added text, no graphics, no arrows, no circles, no logos other than the products' own.

16:9 aspect ratio.
```

Can 4:3 (giong y 2 anh ref) thi doi dong cuoi thanh `4:3 aspect ratio.` roi crop
ve 1440x810 sau.

## Bang dien slot

| Slot | Pen light | Hat | Flashlight | Dog food | Supplement |
|---|---|---|---|---|---|
| SURFACE | garage workbench | bed, plain grey comforter | garage workbench | kitchen counter | granite kitchen counter |
| (holster) | light-oak workbench, garage, white pegboard; tape measure + coiled belt + reading glasses; all holsters empty, no guns/ammo/mags | | | | |
| SETTING | garage, white pegboard behind | bedroom, window daylight | garage, pegboard behind | kitchen, blurred fridge | home kitchen |
| PROOF | the units that come in the box, unpacked in front | a white paper towel pressed into its sweatband after a hot day | the pool of light it throws across the counter, switched on lying on its side | a small pile of its kibble in a plastic scoop | two of its capsules in its flipped-over cap |
| WIN | three where every other product has one | almost dry while the others show brown sweat stains | biggest, brightest white pool, others small and dim yellow | meatier, darker, more uniform | fuller and brighter white |

Cau hoi tim PROOF cho san pham moi: **nguoi mua se dat cai gi canh nhau de so sanh?**
