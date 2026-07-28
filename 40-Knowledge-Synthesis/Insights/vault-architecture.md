---
title: 'Sốt ghi chép nguyên tử — Kiến trúc Cánh Cổng: PRA + Zettelkasten Hybrid'
slug: vault-architecture
category: knowledge
tags:
- obsidian
- zettelkasten
- para
status: draft
type: atomic-note
created: 2026-06-12
last_updated: '2026-07-14'
cited_count: 0
---

# Kiến trúc Cánh Cổng: PRA + Zettelkasten Hybrid

## Tóm tắt một ý tưởng
PRA tổ chức ghi chú theo khả năng hành động (Projcts/ Areas/Recers/Archive) trong khi Zettelkasten tổ chức theo mật độ kiến thức (phần lớn, liên kết) — kết hợp cả hai cho bạn một kho chứa để thực hiện và suy nghĩ.

## 📖 Explanation
**PA phương pháp** (Tiago Forte) cung cấp cấu trúc bên ngoài:
- **P**rojects — thời gian hạn, có hạn chót
- **A**res — đang tiếp tục trách nhiệm, không hạn chót
- **R**esources — vật liệu tham khảo của sự quan tâm
- **A**rchive — những vật không hoạt động từ trên

**Zettelkasten phương pháp** (Niklas Luhmann) cung cấp các lớp hiểu biết nội tâm:
- Ghi chú nguyên tử — một ý tưởng mỗi nốt, 300-700 từ
- Liên kết hai chiều — mỗi nốt nối với nhau
- Tăng cường nguyên tử hàng ngày khi được trích dẫn 2+ lần

**Sự tiếp cận lai:**
1. Dùng USA cho cấu trúc thư mục (không thể)
2. Sử dụng Zettelkasten để tổng hợp kiến thức bên trong `40-Knowledge-Synthesis/`
3. Ghi chú hàng ngày = bản in, cổ vũ các ý tưởng được xác nhận thành ghi chú nguyên tử
4. Kết nối giai đoạn = liên kết trẻ mồ côi, dự án cập nhật

** Tại sao điều này lại hiệu quả với OpenClaw Đặc vụ:**
- Mô phỏng hiệu quả Token: quét tổng kết pidm bed theo liên kết = 5% chi phí hiệu suất
- %% bình luận lớp = hướng dẫn tác nhân không thấy trong chế độ đọc
- Smart Connections + Ollama = Tìm kiếm ngữ nghĩa mà không cần API chi phí

## 🔄 Connections
### Related Concepts
- [[Obsidian-Vault-Setup]] - Dự án MOC cho việc phóng hầm
- [[Vault-Governance]] — Các quy tắc chi tiết và hội nghị đặt tên
- [[Protocol]] - Hướng dẫn hoạt động của Smee

### Applied In
- Bộ não thứ hai của Smee — kho chứa kiến thức chính
- Công việc hàng ngày tràn đầy — ghi chú hàng ngày → Ghi chú nguyên tử được thăng tiến

## 📚 Sources
- Tiago Forte — Phương pháp PRA (Xây dựng bộ não thứ hai)
- Niklas Luhmann — Phương pháp Zettelkasten (học về xã hội)
- Obsidian Tập luyện tốt nhất cộng đồng

---
%% Agent instructions:
- Một ý tưởng trên mỗi nốt. Nếu >2 phần H2 trên các chủ đề khác nhau _ chia ra
- 300 700 từ có thể liên kết được.
- Tăng từ ghi chú hàng ngày khi trích dẫn 2+ lần
- Mỗi nốt nguyên tử mới phải có ít nhất 1 đường dẫn trong cùng một ngày
- Trạng thái: thao tác nháp (khi liên kết 3+) pided (khi cập nhật)
%%
