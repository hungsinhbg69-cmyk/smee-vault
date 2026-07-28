---
title: Cấu hình hệ thống "
slug: "task-system-config"
category: knowledge
tags: [tasks, dataview, tasks-plugin, priority]
status: active
type: framework
created: 2026-06-20
last_updated: 2026-06-20
---

# 📋 Cấu hình hệ thống tác vụ

> Khung làm việc cho quản lý tác vụ tự động dùng Obsidian Tác vụ plugin + Dataview.

## 🎯 Priority System

| Level | Tag | Color | Description | Khi dùng |
|-------|-----|-------|-------------|-------------|
| P1 | `#priority/P1` | 🔴 Red | Quan trọng — phải làm ngày nay hoặc quá hạn | Blocker, hạn chót hôm nay |
| P2 | `#priority/P2` | 🟠 Orange | Cao — tuần này | Thời gian quan trọng nhưng linh hoạt |
| P3 | `#priority/P3` | 🟡 Yellow | Vừa — tháng này | Rất vui được có lịch trình khi rảnh. |
| P4 | `#priority/P4` | 🔵 Blue | Low — backlog | Nhanh lên, không vội. |

### Priority Rules
- **Max 1–2 công việc mỗi ngày** là P1. Nếu nhiều hơn → Chia ra hoặc hoãn lại một số.
- Mỗi nhiệm vụ phải có một thẻ ưu tiên (`#priority/P1` Không có tác vụ chưa được đóng.
- Xem xét hàng tuần: P2P3 cũ kỹ, khuyến khích P3P2 quá hạn.

## Tác vụ _h_h_h_hịn tìm kiếm các Liên lạc bảng

### Thêm mục lục
```tasks
not done
due before today
sort by due desc
group by priority
```

> Yêu cầu này hiển thị mọi thứ qua thời hạn. Cần thiết hành động.

### Nhiệm vụ tuần này
```tasks
not done
due after today -7 days
due before next week monday
sort by due asc
group by priority
```

> Hãy sắp xếp những ngày tháng này.

### Tác vụ đã dự án (được quản lý bởi thư mục)
```tasks
not done
folder contains "10-Projects/Your-Project"
sort by priority desc
```

> Thay thế `Your-Project` Tên thư mục dự án thật. Mỗi dự án hoạt động có bộ lọc riêng.

### Mọi tác vụ hoạt động (toàn bộ xem)
```tasks
not done
sort by due asc
group by priority
```

## 🏷️ Tham khảo cú pháp tác vụ

Chuẩn Obsidian cú pháp tác vụ mở rộng với tác vụ plugin Thuộc tính:

```markdown
- [ ] #priority/P2 🔴 Complete API integration {{due:: 2026-06-25}} {{project:: Facebook Ads Pipeline}}
```

| Property | Format | Example |
|----------|--------|---------|
| Due date | `{{due:: YYYY-MM-DD}}` | `{{due:: 2026-07-01}}` |
| Priority | Thẻ trong văn bản tác vụ | `#priority/P2` |
| Project | `{{project:: Name}}` | `{{project:: FB Campaign Q3}}` |
| Status | Thẻ gạch chân (tùy chọn) | `#status/doing`, `#status/waiting` |

## 🔧 Integration Points

### Ghi chú hàng ngày
- Mỗi tờ giấy có một công việc bị chặn để trưng bày những thứ liên quan.
- Công việc mới được tạo ra từ ghi chú tự động lưu hàng ngày trong hộp thư.

### With Projects
- Mọi thư mục dự án (`10-Projects/*`) có thể có quan điểm riêng của mình sử dụng `folder contains` lọc.
- Bảng điều khiển của dự án bao gồm phần tóm tắt tác vụ.

### Với Kanban (Layer 2)
- Tác vụ bằng `{{project:: Name}}` Tự động phóng vào cột ban điều hành bằng cách đặt các cột.
- Kéo một lá bài cập nhật phần dưới `- [ ]` Hộp kiểm tra → Đánh dấu trong thư ký công việc.

## _Xem xét các thực hành tốt nhất

1. ** Luôn luôn thêm ngày tháng** — tạo ra khả năng phát hiện và phân loại quá hạn.
2. ** Dùng thẻ ưu tiên nhất định** — cần thiết cho `group by priority`.
3. **Tag dự án rõ ràng** — `{{project:: Name}}` hiệu lực lọc dựa trên thư mục.
4. **Review tuần** — rõ ràng hoàn thành, sắp xếp lại quá hạn, lưu trữ các công việc cũ.

---

*Created: 2026-06-20- Layer 1 Hệ thống tác vụ triển khai*
