---
title: "<%% tp.file.title %%>"
slug: "<%% tp.string.title_to_slug(tp.file.title) %%>"
category: area
tags: [fleeting, capture-%%tp.date.now("YYYY")%%]
status: draft
type: fleeting-note
created: <%% tp.date.now("YYYY-MM-DD HH:mm") %%>
---

## Đang hạ cánh Ghi chú — chụp %tp.date. now("H:mm")%% H:

<!-- Viết tự động để ghi chú mỗi ngày qua QuickAdd -->
`[[<%* try { print(daily) } catch(e) { print(tp.date.now("YYYY-MM-DD")) } %>>] ` Đang hạ cánh -> xem xét trong tuần kết nối tiếp theo

- 

> Ghi chú: Xem lại trạng thái của FLEEEING -> phát hành lưu ý nguyên tử trong vòng 7 ngày hoặc lưu trữ nếu cũ.  
> **Plugin: quickadd** vĩ mô cấu hình `capture-quick-thought` Ghi chú tự động lưu ý mỗi ngày.
