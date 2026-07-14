---
title: "Dòng chảy nội dung Kanban"
slug: "content-pipeline-kanban"
category: project
type: template
created: 2026-06-20
last_updated: 2026-06-26
tags: [kanban, content-pipeline]
status: active
---

# Bảng Kanban — Quy trình làm việc nội dung quảng cáo Facebook

Kéo các thẻ giữa các cột để theo dõi tiến độ. Tự động phân loại theo thẻ.

## Ý tưởng / Sưu tầm ý tưởng

```kanban
column_id: ideas
filter_tags: ["tag::idea", "status::draft"]
group_by: status
sort_order: created desc
max_cards: 20
card_fields: [title, tags, status]
empty_message: Không có ý kiến chờ xử lý. Sử dụng QuickAdd > Ý tưởng mới để ghi lại.
```

## Viết nháp (Đang viết)

```kanban
column_id: drafting
filter_tags: ["status::in-progress"]
group_by: priority
sort_order: created desc
max_cards: 10
card_fields: [title, tags, status, due]
empty_message: Không có bản nháp đang hoạt động.
```

## Xem xét (Chờ duyệt)

```kanban
column_id: review
filter_tags: ["status::review"]
group_by: priority
sort_order: created desc
max_cards: 10
card_fields: [title, tags, status, reviewer]
empty_message: Không có mục nào cần xem xét.
```

## Đã công bố (Đã đăng)

```kanban
column_id: published
filter_tags: ["status::published"]
group_by: platform
sort_order: mtime desc
max_cards: 30
card_fields: [title, tags, status, publish_date, performance]
empty_message: Chưa có nội dung nào được công bố.
```

---

## Thống kê quy trình (tự động cập nhật)

| Giai đoạn | Số lượng | Thời gian trung bình | Ghi chú |
|-------|-------|----------|-------|
| Ý tưởng | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "draft").length` | - | số lượng bản nháp |
| Viết nháp | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "in-progress").length` | - | đang thực hiện |
| Xem xét | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "review").length` | - | chờ xem xét |
| Đã công bố | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "published").length` | - | tổng số đã công bố |

---

*Tạo: 2026-06-20 bởi Smee — Layer 2 Deploy (Bảng Kanban)*
