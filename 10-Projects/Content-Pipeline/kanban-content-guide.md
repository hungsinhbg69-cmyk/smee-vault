---
title: "Dòng chảy nội dung — Quảng cáo Facebook"
slug: "content-pipeline-fb-ads"
category: project
tags: [kanban, content, facebook-ads]
status: active
type: kanban-board
created: 2026-06-20
last_updated: 2026-06-20
---

# 📋 Dòng chảy nội dung — Bảng Kanban Quảng cáo Facebook

> Kéo các thẻ qua các cột để di chuyển nội dung trong quy trình.
> Mỗi thẻ liên kết đến tài liệu nguồn và ghi chú nguyên tử.

## 🔍 Ý tưởng (Góc độ)

```dataview
LIST FROM "30-Resources/Facebook-Ads" OR "40-Knowledge-Synthesis/Insights" 
WHERE contains(tags, "idea") AND status = "draft"
SORT file.name ASC
```

## ✏️ Viết nháp (Đang viết)

```dataview
LIST FROM "" WHERE type = "content-draft" AND status = "in-progress"
```

## ✅ Xem xét (Chờ duyệt)

```dataview
LIST FROM "" WHERE status = "review"
```

## 🚀 Đã công bố (Đã đăng)

```dataview
LIST FROM "" WHERE status = "published"
SORT file.mtime DESC
LIMIT 10
```

---

*Ngày tạo: 2026-06-20 bởi Smee — Layer 3 Deploy (Bảng Kanban)*
*Sử dụng QuickAdd để tạo thẻ nội dung mới → tự động phân loại vào giai đoạn quy trình.*
