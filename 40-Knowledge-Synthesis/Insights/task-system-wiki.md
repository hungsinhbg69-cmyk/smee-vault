---
title: "Task System Wiki"
slug: "task-system-wiki"
category: knowledge
tags: [tasks, wiki, quick-reference, kanban-integration]
status: active
type: insights
created: 2026-06-20
last_updated: 2026-06-20
---

# _ Hệ thống Wiki — Tham khảo nhanh

> Tất cả những gì anh cần biết về sáng tạo, quản lý, và truy vấn các nhiệm vụ trong hầm.

## _ĐÃ tạo tác vụ (3 cách)

### Phương pháp 1: Trực tiếp trên bất cứ thông tin nào
Gõ trực tiếp vào nơi cần thiết:
```markdown
- [ ] #priority/P2 Write ad copy for campaign {{due:: 2026-07-01}} {{project:: FB Campaign Q3}}
```

**Quick tip:** Dùng `{{due:: }}` và nhấn thẻ — Templater có thể tự động hoàn thành ngày hôm nay.

### Phương pháp 2: Bắt nhanh (trong hộp)
Dùng `01-Inbox/quick-capture-template.md` để thu nhanh từ bất kỳ bối cảnh nào:
- Mở nhanh mẫu thu được _Patch suy nghĩ thô thêm `{due}` `{priority}` thẻ sau trong thời gian ba giai đoạn.

### Phương pháp 3: Tác vụ chèn lệnh
Nếu sử dụng `/tasks insert` lệnh (từ tác vụ plugin_:
1. Bấm `Ctrl+P` _ gõ kiểu "Tasks" _Gỡ chọn nhiệm vụ chèn
2. Điền vào ngày tháng, ưu tiên trên liên kết
3. Lưu trực tiếp vào ghi chú hoạt động hàng ngày hoặc thư mục đã xác định

## Tham chiếu cú pháp toàn diện

### Due Date
```markdown
- [ ] Task description {{due:: 2026-07-15}}
```
- Format: `YYYY-MM-DD`
- Ngày tháng tương đối hoạt động trong thư mục: `today` `tomorrow` `next week monday`
- Ngày tháng quá khứ gây ra quá hạn phát hiện

### Thẻ ưu tiên (cần thiết)
Luôn luôn dùng định dạng chính xác — không có đường tắt:
- `#priority/P1` — 🔴 Critical
- `#priority/P2` — 🟠 High  
- `#priority/P3` — 🟡 Medium
- `#priority/P4` — 🔵 Low

### Project Tags
```markdown
- [ ] #priority/P2 Task {{due:: 2026-07-15}} {{project:: Campaign Name}}
```
- Dùng chữ hoa/ thường cho tên của dự án: `{{project:: fb-campaign-q3}}`
- Bật bộ lọc dựa vào thư mục trong bộ nhớ tạm

### Thẻ trạng thái ( Optale)
- `#status/doing` - tích cực làm việc trên nó
- `#status/waiting` - bị chặn bởi ai đó hay gì đó
- `#status/review` — cần xem lại trước khi hoàn tất

## _Tìm kiếm vỏ sò gian lận

| View | Query Block | Use Case |
|------|-------------|----------|
| Overdue | `not done / due before today` | Kiểm tra ưu tiên hàng ngày |
| This Week | `not done / due after today -7 days / due before next week monday` | Weekly planning |
| Dự án | `folder contains "10-Projects/Name"` | Name |
| Completed Today | `done after {{date:: YYYY-MM-DD}}` | Daily recap |

## _Kurban - Hợp nhất (Layer 2)

Ban điều hành liên kết với công việc thông qua những quy tắc này:

1. ** Dân số tự động:** Bài có `{{project:: Name}}` xuất hiện trong cột dự án
2. **Status bản đồ cột đến thẻ:** 
   - "Làm" → `#status/doing` hay không có thẻ trạng thái
   - "Waiting" → `#status/waiting`
   - Kiểm tra "Done" `- [x]` Hộp kiểm tra
3. **Drag-toup:** Di chuyển một lá bài để làm việc tự kiểm tra hộp tác vụ
4. **Syccc directions:** Kanban  Agents plugin (Tiếng đánh lạc hướng)

### Tạo một công việc từ Kanban
1. Nhấn vào mục « + » trên cột đích
2. Enter: `- [ ] #priority/P3 New idea {{due:: }}`
3. Lưu _Sổ địa chỉ

## 🔄 Quy trình: Từ thu thập đến hoàn tất

```
Capture (any note / quick-capture) 
  → Triage (daily inbox review, add due/priority/project) 
  → Schedule (assign date or defer to backlog) 
  → Execute (kanban board or daily note checklist) 
  → Complete (check box → auto-tracked in done queries)
```

### Daily Rhythm
- **Chào:** Kiểm tra quá hạn + ô xem tuần này _chọn tối đa 3 mục tiêu
- **Ngày qua ngày:** Thêm công việc vào hàng khi chúng xuất hiện
- ** Buổi tối:** Xem lại mục "Done Today" → thu sự hiểu biết từ công việc hoàn tất

---
## Related
- [[vault-command-center]] — Bảng thông tin dùng hệ thống tác vụ này
- [[kanban-board]] - Lớp tích hợp Kanban
- [[protocol]] - Bắt giữ các quy tắc và các giai đoạn kết nối hàng tuần

*Created: 2026-06-20-R2GGLLLOGG cho tất cả những người dùng két sắt.
