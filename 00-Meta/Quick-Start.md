---
title: "Hướng dẫn thiết lập nhanh — Obsidian Vault"
slug: "quick-start"
category: meta
tags: [meta, setup, obsidian]
status: active
type: reference
created: 2026-06-12
last_updated: 2026-06-15
---

# 🚀 Hướng dẫn thiết lập nhanh — Obsidian Vault

## Đánh giá trạng thái hiện tại

**Vault:** `C:\Users\Hung\Desktop\Smee Obsidian\Smee`
**Trạng thái:** Cài đặt mới — 0 ghi chú, 41 plugin đã cài đặt, Smart Connections + Copilot đã được cấu hình
**Plugins:** Tất cả cơ sở hạ tầng cốt lõi sẵn sàng (Templater, Dataview, Tasks, Kanban, Git, Zotero, Excalidraw, v.v.)

## ✅ Thiết lập hoàn tất

### 1. Cấu trúc thư mục đã tạo
```
00-Meta/          → Các hệ thống tệp tin, READMEs, quy định quản trị
01-Inbox/         → Thu thập nhanh (chưa phân loại)
02-Daily/         → Ghi chú hàng ngày (YYYY-MM-DD.md)
10-Projects/      → Các dự án đang hoạt động (có thời hạn)
20-Areas/         → Những trách nhiệm đang diễn ra
30-Resources/     → Tài liệu tham khảo
40-Knowledge-Synthesis/  → Ghi chú nguyên tử, những hiểu biết, khái niệm
│   ├── Insights/
│   ├── Concepts/
│   └── Frameworks/
50-Reviews/       → Đánh giá hàng tuần/hàng tháng
60-Archive/       → Các mục đã hoàn thành/không hoạt động
70-Outputs/       → Sản phẩm cuối cùng
_templates/       → 7 mẫu ghi chú
```

### 2. Mẫu ghi chú đã tạo (tổng cộng 7)
1. `daily-note.md` — Ghi chép hàng ngày kèm hướng dẫn cho tác nhân
2. `meeting-note.md` — Tóm tắt cuộc họp kèm các công việc cần làm
3. `project-kickoff.md` — Tạo MOC dự án
4. `literature-note.md` — Tổng hợp bài báo học thuật
5. `atomic-note.md` — Ghi chú kiến thức vĩnh cửu
6. `weekly-review.md` — Nghi thức đánh giá hàng thứ Bảy
7. `experiment-note.md` — Nhật ký kiểm tra giả thuyết

### 3. Tài liệu hệ thống đã tạo
1. `00-Meta/README.md` — Trung tâm Vault với tổng quan kiến trúc
2. `00-Meta/Protocol.md` — Quy định quản trị + Quy tắc tác nhân (đã hợp nhất)
3. `00-Meta/Tag-Taxonomy.md` — Tham chiếu thẻ

## 🎯 Các bước tiếp theo cho Hùng

### Ngay lập tức (Hôm nay)
1. **Mở Obsidian** → xác minh tất cả thư mục hiển thị chính xác
2. **Kiểm tra Templater** → Tạo một ghi chú hàng ngày mới → mẫu sẽ tự động điền
3. **Tạo dự án đầu tiên** → Sử dụng mẫu `project-kickoff.md` cho một dự án đang hoạt động
4. **Viết ghi chú nguyên tử đầu tiên** — Thu thập một hiểu biết từ công việc gần đây

### Trong tuần này
1. **Cấu hình Dataview** → Thêm các truy vấn bảng điều khiển vào README hoặc tạo `Dashboard.md`
2. **Thiết lập Git** → Khởi tạo kho lưu trữ, thực hiện lần cam kết đầu tiên (plugin obsidian-git đã sẵn sàng)
3. **Đánh giá hàng tuần đầu tiên** — Thứ Bảy 20h — làm trống hộp thư đến, liên kết ghi chú
4. **Kết nối Zotero** → Nhập bất kỳ bài báo nào có sẵn qua obsidian-zotero-desktop-connector

### Trong tháng này
1. **Phát triển Areas** → Tạo ghi chú cho các lĩnh vực Marketing, Thiết kế, Lập trình, AI-Agent
2. **Tạo MOCs dự án** — Tài liệu hóa các dự án đang hoạt động kèm hành động tiếp theo
3. **Thiết lập nhịp điệu hàng ngày** — Smee thu thập trong các phiên làm việc, Hùng đánh giá hàng tuần
4. **Hoàn thiện thẻ** — Điều chỉnh phân loại dựa trên mẫu sử dụng thực tế

## 🔧 Danh sách kiểm tra cấu hình plugin

### Đã được cấu hình ✅
- [x] Smart Connections _NHỮNG NGƯỜI ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ ĐỂ Ollama Đang tách (bge-micro-v2)
- [x] Copilot → Các lệnh tùy chỉnh đã tải về
- [x] Calendar plugin → Plugin cốt lõi đã bật
- [x] Daily Notes → Plugin cốt lõi đã bật
- [x] Backlinks + Graph View → Các plugin cốt lõi đã bật

### Cần cấu hình ⚠️
- [ ] **Templater** → Đặt thư mục mẫu vào `_templates/`
- [ ] **Dataview** → Bật máy ảo JavaScript (Cài đặt → Dataview)
- [ ] **obsidian-tasks-plugin** → Cài đặt mặc định cho truy vấn
- [ ] **obsidian-git** → Đường dẫn kho lưu trữ, khoảng thời gian đồng bộ tự động
- [ ] **remotely-save** → Điểm đến sao lưu
- [ ] **Zotero Integration** → Kết nối ứng dụng máy tính Zotero
- [ ] **QuickAdd** — Thiết lập quy trình thu thập
- [ ] **Homepage** — Nội dung trang chủ tùy chỉnh

### Các nâng cấp tùy chọn 🔮
- [ ] Digital Garden → Triển khai trang tĩnh
- [ ] Advanced Canvas — Bản đồ kiến thức trực quan
- [ ] Spaced Repetition — Lịch xem lại thẻ ghi nhớ
- [ ] Mermaid Tools — Tích hợp biểu đồ

## 📊 Chỉ số thành công (Mục tiêu 30 ngày)

| Metric | Current | 30-Day Target |
|--------|---------|---------------|
| Tổng số ghi chú | 0 | 20+ |
| Dự án đang hoạt động | 0 | 2-3 với MOCs |
| Ghi chú nguyên tử | 0 | 10+ |
| Liên kết trên mỗi ghi chú | 0 | Trung bình 5+ |
| Nợ hộp thư đến (Inbox backlog) | 0 | <5 mục |
| Tỷ lệ sử dụng mẫu | 0% | >80% các ghi chú mới |

## 🤝 Quy trình làm việc Người-Tác nhân

### Hùng thực hiện:
- Thu thập ý tưởng thô, ghi chú cuộc họp, điểm nổi bật từ bài viết
- Đánh giá hàng tuần (30 phút vào thứ Bảy)
- Lập kế hoạch dự án và theo dõi cột mốc
- Quyết định phân loại thẻ

### Smee (Tác nhân) thực hiện:
- Tự động thu thập trong các cuộc trò chuyện (tối đa 2/session)
- Tạo ghi chú nguyên tử từ những hiểu biết được trích dẫn
- Duy trì liên kết hai chiều
- Chạy giai đoạn kết nối hàng tuần
- Cập nhật tiến độ dự án
- Tạo truy vấn Dataview cho bảng điều khiển

### Chung:
- Ghi chép vào ghi chú hàng ngày
- Bảo trì MOCs dự án
- Thực thi đánh giá hàng tuần
- Dọn dẹp thẻ hàng tháng
- Kiểm tra cấu trúc định kỳ hàng quý

## 💡 Mẹo chuyên gia

1. **Bắt đầu lộn xộn, tinh chỉnh sau** — Đừng quá kỹ thuật hóa trong tuần đầu tiên
2. **Một hiểu biết trên mỗi ghi chú nguyên tử** — Ngắn = có thể liên kết = hữu ích
3. **Liên kết ngay lập tức** — Một ghi chú không có liên kết là một ngõ cụt
4. **Sử dụng %% bình luận** — Hướng dẫn tác nhân vô hình trong chế độ đọc
5. **Tin tưởng vào đánh giá hàng tuần** — 30 phút/tuần > bất kỳ tính năng plugin nào

---
*Ngày thiết lập: 2026-06-12*
*Bản Vault: 1.0*
*Kiến trúc: PARA + Zettelkasten Hybrid*
