# Dino Funnel

Plugin Claude Code làm trọn funnel cho 1 sản phẩm: pre-sale top 5 → flip to win → sale page → checkout → bundle → upsell/downsell → ads FB.

## Cài lần đầu

1. Mở Claude app → **Code**, chọn 1 folder bất kỳ, gõ lần lượt:
   ```
   /plugin marketplace add unicorn-monster/dino-funnel
   /plugin install dino-funnel@dino-funnel
   ```
   Xong thì thoát rồi mở lại Claude Code.
2. Gõ `/dino-funnel:funnel-setup`. Claude tự cài các thứ cần và chỉ hỏi bạn 3 việc: key Kie, đăng nhập Shopify (tài khoản Huy cấp), bật 1 công tắc trong Chrome.
3. Từ đó về sau luôn mở Claude Code trong folder làm việc mà bước 2 tạo ra (mặc định `~/dino-work`).

## Làm việc

- Sản phẩm mới: `/dino-funnel:funnel <link Amazon> <link sale page>`
- Làm tiếp sản phẩm cũ: `/dino-funnel:funnel tiếp tục <tên sp>`
- Gọi riêng từng bước: `/dino-funnel:pre-sale-page`, `/dino-funnel:sale-page`, `/dino-funnel:checkout-funnelish`, `/dino-funnel:bundle`, `/dino-funnel:upsell-downsell`, `/dino-funnel:fb-top5`...
- Bảng tổng của 1 sp (slug từng bước, gói checkout, giá upsell/downsell) nằm ở `output/<sp>/0-funnel.md`, Claude tự cập nhật sau mỗi bước. Cần làm lại hay bổ sung: "làm 0-funnel.md cho sp <tên>" hoặc "funnel sp <tên> tới bước nào rồi, cập nhật 0-funnel.md".

Mỗi bước Claude dừng lại cho bạn duyệt. Trang top 5 lên topreviewking/topreviewqueen thì gửi folder trang cho Huy deploy.

## Cập nhật khi Huy báo có bản mới

Nói với Claude: **"cập nhật plugin dino-funnel"** (nó chạy `claude plugin marketplace update dino-funnel` rồi `claude plugin update dino-funnel@dino-funnel`), xong thoát rồi mở lại Claude Code.
