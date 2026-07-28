---
title: "Weekly Review — <%% tp.date.now('w') %%>"
slug: "weekly-review-<%% tp.date.now('YYYY-MM-DD') %%>"
category: meta
tags: [review, weekly, workflow]
status: active
type: weekly-review
created: <%% tp.date.now("YYYY-MM-DD") %%>
last_updated: <%% tp.date.now("YYYY-MM-DD") %%>
---

# 📋 Weekly Review — <%% tp.date.now("dddd, MMMM Do YYYY") %%>

## ▪ Hành động nhanh chóngQuickAdd Macros)
| Action | Macro | Description |
|--------|-------|-------------|
| 📥 Capture Note | `capture-new-note` | Tự động frontmatter liên kết thông minh |
| 💭 Fleeting Thought | `capture-quick-thought` | Ghi chú nhanh mỗi ngày |
| 📊 Weekly Init | `review-weekly-init` | Mở mẫu duyệt này |

---

## ▪ Ghi chú mỗi ngày

**Plugin: dataview + lịch** — Quét thời gian thực qua ghi chú hàng ngày

```dataview
LIST FROM "02-Daily"
WHERE file.name >= date("<%% tp.date.now("YYYY-MM-DD") %%>") - dur(6 days)
  AND file.name <= "<%% tp.date.now("YYYY-MM-DD") %%>"
SORT file.name DESC
```

**Action:** Quét mỗi ghi chú mỗi ngày để bắt những thứ cần được thăng tiến thành những ghi chú nguyên tử.

---

## ▸ Inbox Zero

**Plugins: quickadd + templater** — dùng macro `capture-quick-thought` để process

### Bỏ xử lý mục từ 01- Inbox/
```dataview
LIST FROM "01-Inbox"
SORT file.mtime DESC
```

- [ ] Chuyển sang cập nhật PRA frontmatter  
- [ ] Xoá mục cũ/ đang tìm kiếm  
- **Goal: hộp rỗng trước khi chuyển đi**

---

## _Tiếng nói công việc — obsidian- Những nhiệm vụ...plugin + cmdr

**Plugin: obsidian- Những nhiệm vụ...plugin** — Tất cả các tác vụ hoạt động được liệt kê tự động

### Làm quá tác vụ (TIẾNG THỞ LẠI)
```tasks
not done
is overdue
exclude id:: 
group by file.path
```

### Công việc ưu tiên trong tuần này
```tasks
not done
due during this week
sort by priority
```

**Action:** Chọn 5 việc cho tuần này.  
**Quick Command (cmdr plugin):** `T+T` để chuyển đổi văn bản đã chọn sang điều khiển

---

## _ Quảng cáo địa vị dự án —kanban + dataview

**Plugins:kanban + dataview + Điều khiển- giữa các dự án**

````dataview
TABLE status as "Status", type as "Focus"
FROM "10-Projects"
WHERE status = "active" OR status = "researching"
SORT file.mtime DESC
````

Đối với mỗi dự án hoạt động, trả lời:
1. Hành động NEXT trong dự án này là gì?
2. **Plugin:kanban** — kéo vào cột bảngkanban (sẵn sàng làm bài ôn lại)

---

## _Gắt thẻ Hygiene — Thợ điều khiển thẻ

**Plugin:: card-wrangler** — trộn, thay đổi tên, dọn dẹp thẻ trong Batch mode

### Thẻ gần đây ( 14 ngày qua)
```dataview
TABLE file.name as "Note"
WHERE any(file.tags, t => date("<%% tp.date.now("YYYY-MM-DD") %%>") - dur(14 days) < file.mtime)
FLATTEN file.tags as tag
SORT file.mtime DESC
LIMIT 50
```

- [ ] Các thẻ sai chính tả hợp nhất (#Status/draft #status/draft)  
- [ ] Kết hợp các khái niệm thừa dạng qua phần đuôi thẻ  
- [ ] Kho lưu các thẻ không dùng từ quý cuối

---

## _Các ghi chú mồ côi bị lỗi

**Plugin: kết nối thông minh + omnisearch** — tìm ghi chú mà không có hậu thuẫn

```dataview
TABLE length(file.outlinks) as "Outbound Links"
WHERE file.folder = "40-Knowledge-Synthesis" OR file.folder = "30-Resources"
WHERE length(file.outlinks) < 2
SORT length(file.outlinks) ASC
LIMIT 20
```

**Action:** Tạo các đường dẫn hậu phương từ Smart Connections Mọi dấu hiệu mới phải có liên kết _1 ra (Pitocol  6).

---

## _ Chất lượng cổng vào — git + siêu dữ liệu

**Plugins: obsidian-git + giao diện siêu dữ liệu + từ xa - stave**

- [ ] _Việc rửa sạch trạng thái Git?
- [ ] Bộ mã kiểm tra với **metadata-expactor**
- [ ] Liên kết bị đứt qua **omnisearch**: dán `[[` để tìm những trọng tài đã chết
- [ ] Xu hướng tăng trưởng tập tin: xem lại **VULT-ALYTS.md** để tìm biểu đồ

---

## ▸ Reflections

### Tuần này, những gì đã làm rất tốt:


### Cái gì không thành công:


### Ý nghĩa của tuần:


### Tuần tới hãy ưu tiên (x 3):



---

*Chúng tôi có thể ôn lại mẫu · Tích hợ 14+ bổ sung: tuần hoàn- chú thích, lịch, công việc-plugin dataviewNgười đánh bắt bắt, người Anh, templater quickaddMối liên hệ thông minh, omnisearch obsidian-git, siêu dữ liệu-menu, từ xa-save, cmtr*
