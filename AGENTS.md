# Smee Vault — Quy tắc vận hành cho AI agent

Tệp này là nguồn hướng dẫn cấp vault cho mọi agent làm việc trong `Smee`, gồm OpenClaw và Hermes. Khi có xung đột, ưu tiên theo thứ tự: yêu cầu hiện tại của Hùng → tệp này → `00-Meta/Protocol.md` → ghi chú cũ.

## Khởi động tác vụ

1. Xác nhận vault gốc là `C:\Users\Hung\Desktop\Smee Obsidian\Smee`.
2. Đọc `00-Meta/Vault-Quick-Ref.md`; chỉ đọc thêm 2–3 ghi chú liên quan trực tiếp.
3. Với tác vụ dự án, kiểm tra `10-Projects/`. Với tác vụ vận hành lặp lại, kiểm tra `20-Areas/`.
4. Tìm trước khi tạo để tránh trùng ghi chú, slug hoặc wikilink.
5. Kiểm tra `git status --short`; không ghi đè thay đổi có sẵn của Hùng hay agent khác.

## Cây thư mục chuẩn

| Cấp | Thư mục | Nội dung |
|---|---|---|
| 00 | `00-Meta/` | Governance, MOC, dashboard, taxonomy, cấu hình |
| 01 | `01-Inbox/` | Capture thô, chưa phân loại |
| 02 | `02-Daily/` | Nhật ký ngày `YYYY-MM-DD.md` |
| 10 | `10-Projects/` | Kết quả có mục tiêu và thời hạn |
| 20 | `20-Areas/` | Trách nhiệm duy trì liên tục |
| 30 | `30-Resources/` | Nguồn tham khảo theo domain |
| 40 | `40-Knowledge-Synthesis/` | Concepts, Frameworks, Insights, tri thức đã tổng hợp |
| 50 | `50-Reviews/` | Xem xét hàng tuần/tháng |
| 60 | `60-Archive/` | Nội dung hoàn tất, cũ hoặc bị thay thế |
| 70 | `70-Outputs/` | Thành phẩm sẵn dùng/xuất bản |
| — | `_templates/`, `_scripts/` | Template và automation; không chứa ghi chú kiến thức |

Không tạo các cây cũ như `30-Inbox`, `50-Archive`, `60-Backups`, `70-Templates`, `80-Scripts`, `90-Inbox`, `A1-Pending Inbox`, `A2-Smee`.

## Quy tắc định tuyến

- Chưa rõ giá trị hoặc vị trí → `01-Inbox/`.
- Có deadline và kết quả cần hoàn thành → `10-Projects/`.
- Cần duy trì lâu dài, không có ngày kết thúc → `20-Areas/`.
- Tài liệu nguồn/chưa tổng hợp → `30-Resources/<domain>/`.
- Insight đã kiểm chứng → `40-Knowledge-Synthesis/Insights/`.
- Khái niệm độc lập → `40-Knowledge-Synthesis/Concepts/`.
- Quy trình/mô hình tái sử dụng → `40-Knowledge-Synthesis/Frameworks/`.
- Thành phẩm → `70-Outputs/`; nội dung ngừng hoạt động → `60-Archive/`.
- Không để ghi chú nghiệp vụ ở gốc vault.

## Chuẩn ghi chú

- Markdown UTF-8; không chuyển mã hoặc tạo ký tự mojibake.
- Ghi chú mới phải có properties: `title`, `slug`, `category`, `tags`, `status`, `type`, `created`, `last_updated`.
- `slug` dùng kebab-case; tối đa 5 tags đã có trong `00-Meta/Tag-Taxonomy.md`.
- Dùng `[[wikilink]]` cho nội bộ; URL Markdown cho nguồn ngoài.
- Mỗi ghi chú mới có ít nhất 1 liên kết ra và được gắn vào một MOC/index phù hợp.
- Chỉ cập nhật `02-Daily/YYYY-MM-DD.md` cho thay đổi có ý nghĩa; không log từng lần đọc/search.
- Không tự ý sửa hàng loạt frontmatter, đổi tên hoặc di chuyển từ 10 tệp trở lên nếu Hùng chưa yêu cầu rõ.

## Cách dùng công cụ

- Tìm file/nội dung: ưu tiên `rg --files` và `rg`.
- Sửa nhỏ: patch theo đoạn ổn định; không viết lại toàn bộ tệp nếu không cần.
- Di chuyển ghi chú trong Obsidian đang mở: ưu tiên thao tác hỗ trợ cập nhật link; nếu dùng filesystem, quét và xác minh wikilink trước/sau.
- Không chỉnh `.obsidian/workspace.json`, dữ liệu plugin, `.smart-env/` hoặc secrets trừ khi tác vụ yêu cầu trực tiếp.
- Không commit, push, gửi tin hay xuất bản nếu Hùng chưa yêu cầu.

## Quy trình kết thúc

1. Kiểm tra file mới/sửa đúng tầng thư mục và frontmatter.
2. Quét wikilink hỏng liên quan đến phần vừa đổi.
3. Kiểm tra UTF-8 và không có ký tự thay thế `U+FFFD` trong file đã sửa.
4. Chạy `git diff --check` và `git status --short`.
5. Báo ngắn gọn: đã đổi gì, file nào, kiểm tra nào đã chạy, phần nào chưa đụng tới.

## Phân vai agent

- **OpenClaw:** orchestration dài hạn, channel/gateway, heartbeat/cron, memory và automation. Dùng workspace skills khi có; tác vụ vault vẫn phải tuân thủ tệp này.
- **Hermes:** tác vụ tương tác, nghiên cứu, tool use, skill và xử lý theo phiên. `SOUL.md` chỉ định tính cách; quy tắc vault nằm ở đây.
- Cả hai không duy trì bản sao luật riêng. Khi cây vault đổi, sửa tệp này và các MOC trong `00-Meta/`.

## Tài liệu điều hướng

- [[Protocol]] — schema, lifecycle và quality gate chi tiết
- [[Vault-Quick-Ref]] — điểm vào tiết kiệm context
- [[Vault-MOC]] — bản đồ nội dung
- [[Tag-Taxonomy]] — tags hợp lệ
- [[agent-integration-framework]] — phối hợp OpenClaw/Hermes với vault
