---
title: "Cấu hình Task Engine"
slug: "task-engine-configuration"
category: meta
tags: [workflow, tasks, automation]
status: active
type: reference
created: 2026-06-27
last_updated: 2026-06-27
---

# Cấu hình Task Engine

> Cấu hình trung tâm cho **obsidian-tasks-plugin** + metadata-menu + tích hợp lịch  
> Lệnh tùy chỉnh qua plugin **cmdr** để tạo lối tắt workflow

## Khối Plugin Tasks Toàn cục (sao chép vào mọi ghi chú dự án)

```tasks
not done
group by heading
sort by priority descending
reverse
hide backlinks
hide id
hide due date
hide cancelled date
hide created date
hide start date
hide modified date
hide task field explanations
```

## Quy ước Ưu tiên Công việc

| Ký hiệu | Ý nghĩa | Tự động đổi màu (tasks-plugin) |
|--------|---------|--------------------------|
| P1 | Quan trọng - đến hạn tuần này | đỏ |
| P2 | Cần thiết - đến hạn tháng này | cam |
| P3 | Bình thường - sprint tiếp theo | vàng |
| P4 | Ưu tiên thấp / có thể làm sau | xanh lá |

## Lệnh Nhanh (macro của plugin cmdr)

Cấu hình mỗi lệnh trong Settings -> cmdr:

### Lệnh 1: "Tạo công việc từ văn bản đã chọn"
Lối tắt: T+T
Các bước:
1. Chọn văn bản trong bất kỳ ghi chú nào
2. Nhấn Cmd hoặc Shift+T
3. Templater tạo mục công việc với văn bản đã chọn làm mô tả
4. Tự động liên kết đến ngày dự án hiện tại

### Lệnh 2: "Đánh dấu Hoàn thành + Thêm Suy ngẫm"  
Lối tắt: Shift+Enter trên công việc
Khi đánh dấu một công việc hoàn thành, hệ thống sẽ yêu cầu ghi chú suy ngẫm trước khi đóng lại

### Lệnh 3: "Dọn dẹp Công việc Hàng tuần"
Mở ghi chú mới trong `40-Knowledge-Synthesis/Insights/` với khối công việc tự động tạo cho tất cả các mục đang chờ xử lý

## Chỉnh sửa Nhanh qua Menu Metadata

Plugin **metadata-menu** cung cấp giao diện đồ họa để chỉnh sửa frontmatter - không cần làm thủ công.

### Bắt đầu Chỉnh sửa Mẫu
1. Mở ghi chú trong metadata-menu
2. Chỉnh sửa tags/trạng thái/hệ thống phân loại -> áp dụng ngay lập tức  
3. Chọn nhiều file trong trình duyệt explorer -> chỉnh sửa đồng bộ metadata
4. Xem thay đổi trực tiếp mà không cần tải lại

## Tích hợp Lịch và Công việc

**Plugin: calendar + periodic-notes** - công việc được liên kết với ngày đến hạn:

- Ghi chú hàng ngày (02-Daily/) tự động ghi lại thời gian bắt đầu
- Đánh giá hàng tuần chạy quét công việc qua truy vấn dataview
- Đánh giá hàng tháng lưu trữ các công việc đã hoàn thành từ 60-Archive/

## Quy tắc Xử lý Công việc Quá hạn

```dataview
TABLE status as "Ưu tiên", due as "Ngày đến hạn"
FROM ""
WHERE due < date(today) AND done = false
SORT due ASC
LIMIT 20
```

**Quy tắc:** Bất kỳ công việc nào quá hạn >7 ngày -> nâng cấp lên P1 hoặc di chuyển sang mục "Đang chờ xử lý".  
**Quy tắc:** Bất kỳ công việc nào chờ đợi từ 30+ ngày -> lưu trữ hoặc xóa.
