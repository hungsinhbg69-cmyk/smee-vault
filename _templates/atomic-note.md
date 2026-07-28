---
title: "Atomic Note — {{title}}"
slug: "{{title-slug}}"
category: knowledge
tags: []
status: draft # draft | active | superseded
type: atomic-note
created: {{date}}
last_updated: {{date}}
cited_count: 0
related_concepts: 
applied_in: 
difficulty: easy # easy | medium | hard
---

# 🔬 {{title}}

## Tóm tắt một ý tưởng
<%* tR += Đợi tp. system.prompt(" Một câu tóm tắt: "); *

## 📖 Explanation
[<small>300 700 từ, rõ ràng, chính xác, không có gì.</small>]

## 🔄 Connections
### Related Concepts
<%* Const liên quan = đợi tp. hệ thống.prompt(hoặc để trống):\ t% * khái niệm « / »; nếu (có liên quan? .trim()}{ cont mở =["[;; cont gần = "]]; t= "- + mở + mở liên quan.t) + "n" *

### Applied In
<%* tR + = "- [[Project-Name]] *>

## 📚 Sources
<%* Const sourceTtle = đợi tp. system.prompt(" sice title: "); const sourceUrl = chờ tp. system.prompt("Source () URL (hoặc để trống): "; nếu (sourceTitle?.trim()) tR += sourceUrl? .trim()? "- [" + sourceTitle.trim() + "](" + sourceUrl.trim() + ")\n" : "-" +  sourceTitle.trim() + "\n; *>

---
%% Agent instructions:
- Một ý tưởng trên mỗi nốt. Nếu >2 phần H2 trên các chủ đề khác nhau _ chia ra
- 300 700 từ có thể liên kết được.
- Tăng từ ghi chú hàng ngày khi trích dẫn 2+ lần
- Mỗi nốt nguyên tử mới phải có ít nhất 1 đường dẫn trong cùng một ngày
- Trạng thái: thao tác nháp (khi liên kết 3+) pided (khi cập nhật)
%%
