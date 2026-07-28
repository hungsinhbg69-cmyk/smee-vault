---
title: "OpenClaw + Hermes Đặc vụ Hợp nhất Khung Làm việc"
slug: "agent-integration-framework"
category: knowledge
tags: [vault-maintenance]
status: "active"
type: reference
created: 2025-12-01
last_updated: 2026-07-13
---


# _Nghề nghiệp: OpenClaw + Hermes Comment

> Một lớp luật chung kết nối OpenClaw và Hermes với Smee Obsidian vault mà không nhân đôi quy tắc.

## 🏗️ Architecture

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ OpenClaw/Hermes│────▶│  Vault AGENTS.md│────▶│  Output/Actions   │
│  (Chat)      │◀────│  Layer          │◀────│                 │
└──────────────┘     │                 │     └──────────────────┘
                     │ 1. Scan Quick-Ref │
                     │ 2. Capture/Create │
                     │ 3. Connect/Link   │
                     │ 4. Log/Commit     │
                     └─────────────────┘
```

## Lớp hợp nhất (4 tổng)

### Lớp 1: Hợp đồng hoạt động chia sẻ
**What it does:** Mọi agent đọc root `AGENTS.md`, sau đó áp dụng `Protocol.md` cho naming, frontmatter, folders và tags.
** Xác nhận thế nào:** Kiểm tra cổng chất lượng trong mục 6 + Khu vực 12.
** Hành vi thông minh:** Đọc các quy tắc tại phiên chạy bắt đầu áp dụng cho mọi tập tin tạo/dot.

### Lớp 2: Cổng mỗi ngày ghi chép
**What it does:** Chỉ capture, decision, output và structural change có ý nghĩa mới được ghi vào `02-Daily/YYYY-MM-DD.md`.
**Format:** `[HH:MM] <type>: "<summary>" → [[slug]]`
** likes:** thu thập, kết nối, kết quả, quyết định, dọn dẹp.
** Hành vi thông minh:** Tự động-vỗ sau mỗi hành động có ý nghĩa — không chỉ kết thúc phiên chạy.

### Lớp 3: Bảo trì đồ thị tri thức
**Những gì nó làm:** Đặc vụ tạo ra liên kết hình cáp hai chiều giữa nội dung mới và ghi chú tồn tại trong quá trình sáng tạo.
** Xác nhận thế nào:** kiểm toán xác chết (bộ phận bảo trì 8) — mỗi nốt có đường dẫn 1 ra ngoài.
Hành vi sinh học:** Mọi nốt mới kết nối với ít nhất 1 chùm hầm đã có ngay lập tức.

### Lớp 4: Đang tải văn cảnh thông minh
** Những gì nó làm:** Đặc vụ tự động nạp các ghi chú miền liên quan dựa trên chủ đề trò chuyện - được nạp từ cổng-MMC. Khi thảo luận Facebook Ads _Nợ _IDEX.md + sub-notes thích hợp. Khi nào trên Bac Giang _Gang nạp hồ sơ văn hóa + ghi chú thị trường.
** Xác nhận thế nào:** Bản ghi phiên chạy được nạp vào văn cảnh miền nào.
** Hành vi sinh học:** Đọc MOC iC fold  ser load 2-3 neo từ cụm đó trước khi làm việc sâu.

## 🔄 Feedback Loops

### Vòng lặp tích cực (sự đòi hỏi)
Đặc vụ bắt được thông tin sâu sắc _SP sẽ tạo ra lưu ý nguyên tử bằng các liên kết i- tơ- tơ-ni-gia tiếp theo nạp các ngữ cảnh thích hợp cho các tác nhân xây dựng trên các kho kiến thức hiện có tăng cường sự tái tạo của i-terilcril càng chính xác hơn.

### Pha kết nối hàng tuần
Thứ Bảy vào lúc 20h: rỗng thư mục hộp → cổ vũ những ý tưởng hàng ngày có hiệu lực đến những ghi chú nguyên tử → liên kết trẻ mồ côi → Kiểm tra dự án tiếp theo → Lưu các mục đã chết → - Thay đổi git.

## 📐 Quality Metrics

| Metric | Target | How Measured |
|--------|--------|--------------|
| Liên kết ra ngoài mỗi nốt | ≥1 | Kiểm tra cuối cùng thông qua tìm kiếm tập tin |
| Backlink coverage | >50% các ghi chú liên kết đến nhau | Quét đồ thị cổng |
| Chất lượng tín hiệu nhật ký hàng ngày | Không có log đọc/search vụn | Kiểm tra vị trí thủ công |
| Bảo vệ cây ô uế | Không ghi đè thay đổi có sẵn | Trạng thái Git + di chuyển |

## Bản đồ trách nhiệm

| Agent | Vai trò chính | Không dùng làm nguồn luật |
|---|---|---|
| OpenClaw | Gateway, channels, heartbeat, cron, memory, orchestration dài hạn | Workspace backup hoặc memory cũ |
| Hermes | Phiên tương tác, research, skills, tool execution | `SOUL.md` cho đường dẫn/schema dự án |
| Cả hai | Tìm kiếm → Lưới → liên kết → Xác nhận gốc `AGENTS.md` | Bản sao cây thư mục trong file riêng |

---
*Created: 2026-06-23 · Synchronized for OpenClaw + Hermes: 2026-07-13*
