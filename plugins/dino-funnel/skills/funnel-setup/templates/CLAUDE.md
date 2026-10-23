# Dino Funnel (work folder)

Funnel work for Business DINO (Dinosaurized Store LLC) with the `dino-funnel` plugin. Start or resume a product with `/dino-funnel:funnel <amazon link> [offer link]`; first time on this computer: `/dino-funnel:funnel-setup`.

- Reply in Vietnamese, short. Page and ad copy in plain American English.
- Run everything from this folder. Output per product in `output/<sp>/` (see the `funnel` skill). Read `output/<sp>/0-brief/0-product-brief.md` before writing copy for that product.
- Images: Kie GPT Image 2.5 Flare only, 1K, key `KIE_API_KEY` in `.env` here. Never put the key anywhere else.
- Don't comment on claims, compliance, review counts or ratings: a lawyer reviews everything before it's published; numbers given are real.
- Pre-sale pages for topreviewking.com / topreviewqueen.com: zip the page folder (without `research/`) and send it to Huy, he deploys. Funnelish pages: paste into a Custom HTML block yourself.
- Something new learned (a fix, a rule, a gotcha): tell Huy so he adds it to the plugin, don't edit the plugin files.
- "Cập nhật plugin": run `claude plugin marketplace update dino-funnel && claude plugin update dino-funnel@dino-funnel`, then tell the user to quit and reopen Claude Code.
