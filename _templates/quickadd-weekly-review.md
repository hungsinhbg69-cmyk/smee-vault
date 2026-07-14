---
title: "Weekly Review — {{DATE:GGGG-[W]WW}}"
slug: "weekly-review-{{DATE:GGGG-[W]WW}}"
category: meta
tags: [review, weekly, workflow]
status: active
type: weekly-review
created: "{{DATE:YYYY-MM-DD}}"
last_updated: "{{DATE:YYYY-MM-DD}}"
---

# Weekly Review — {{DATE:GGGG-[W]WW}}

## Daily notes — 7 ngày gần nhất

```dataview
LIST FROM "02-Daily"
WHERE file.day >= date(today) - dur(7 days)
SORT file.day DESC
```

## Inbox cần xử lý

- [ ] Chuyển ý quan trọng thành atomic note
- [ ] Gắn liên kết và nguồn
- [ ] Đóng hoặc lên lịch lại task tồn

## Dự án đang chạy

```dataview
TABLE status, next_action
FROM "10-Projects"
WHERE status != "done"
SORT file.mtime DESC
```

## Kết luận tuần

- Điều đã làm tốt:
- Điều cần sửa:
- Ưu tiên tuần tới:
