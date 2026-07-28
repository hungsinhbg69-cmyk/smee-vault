---
title: "QuickAdd Macros Configuration"
slug: "quickadd-macros"
category: knowledge
tags: [automation, quickadd]
status: active
type: config-reference
created: 2026-06-20
last_updated: 2026-06-24
---

# QuickAdd Macro Library

Mọi vĩ mô có thể truy cập qua `Ctrl+Q` (mặc định) hoặc bảng chọn lệnh.

## Capture Macros

### New Idea
**Trigger:** `Ctrl+Q > New Idea`
**Action:** Tạo chú thích trong 01-Inbox/ với ý tưởng mẫu, tự động đánh dấu #idea + date
**Template:** See _templates/quick-idea.md

### Quick Note
**Trigger:** `Ctrl+Q > Quick Note`
**Action:** Tạo ghi chú nguyên tử trong 40-cyedge-Sythesis/Insights/ với nhãn thời gian
**Temramp:** Xem _temlates/tomic-note.md (đã có)

### Chụp ảnh & Web
**Trigger:** `Ctrl+Q > Web Clip`
**Action:** Mở trình duyệt, nhắc cho URLLưu vào bảng nháp sau đó dán vào lưu ý mới trong 30 mã nguồn/
**Variables:** url, tiêu đề, tác giả, ngày_ tháng

### Tác vụ từ phần chọn
**Trigger:** `Ctrl+Q > New Task (from selection)`
**Action:** Tạo tác vụ với đoạn đã chọn như mô tả, tự động- do- xác định ngày mai trừ khi được xác định
**Variables:** đã chọn_ text, _date

### Meeting Capture
**Trigger:** `Ctrl+Q > New Meeting`
**Action:** Tạo ghi chú cuộc họp trong 10 tờ báo/<project>/ hoặc 02-Daily/ nếu không có dự án được chọn
**Temramp:** Xem _temlates/mee-note.md (đã có)

## Output Macros

### Tạo các thẻ từ Ghi chú
**Trigger:** `Ctrl+Q > Flashcards from [[note]]`
**Action:** Trích dẫn các khái niệm khóa và tạo các thẻ lặp lại không gian với #flashcard
**Viariables:** Nguồn_note, card_ log (mặc định 10)

### Xuất ra PDF
**Trigger:** `Ctrl+Q > Export PDF`
**Action:** Dùng Pandoc để xuất ghi chú hiện thời dạng thông tin PDF
**Variables:** xuất_ filename

## Workflow Macros

### Tóm tắt mỗi ngày đứng lên
**Trigger:** `Ctrl+Q > Daily Standup`
**Action:** Truy vấn tác vụ, duyệt các ghi chú gần đây, tạo ra tóm tắt mỗi ngày với dataview Các thư mục
**Rapput:** Phụ đề đến 02-Daily / hôm nay

### Xem lại trang bìa hàng tuần
**Trigger:** `Ctrl+Q > Weekly Review`
**Action:** Quét tất cả thư mục cho mục chưa xử lý, danh sách ghi chú mồ côi, gợi ý kết nối
**Temramp:** Xem _temlates/smremly-review.md (đã có)

---
* Contture: 2026-06-20 by Smee — Lớp 3 (QuickAdd Tự động hóa*
