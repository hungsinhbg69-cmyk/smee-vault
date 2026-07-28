---
title: "Quy chế quản trị kho lưu trữ"
slug: "vault-governance"
category: meta
tags: [meta, governance]
status: superseded
type: reference
created: 2026-06-12
last_updated: 2026-07-14
---

# 📜 Quy tắc quản trị kho lưu trữ

> [!warning] Đã bị thay thế
> Nguồn quy chế chính thức là [[Protocol]]. Bản sao lịch sử này được giữ lại chỉ để phục vụ mục đích kiểm toán.

## Quy ước đặt tên

### Tên tệp
- **Dự án:** `TenDuaAnh.md` — KHÔNG thêm hậu tố như "notes" hay "doc"
- **Tệp có ngày tháng:** `YYYY-MM-DD-MoTa.md` — Ngày theo chuẩn ISO để sắp xếp theo thứ tự thời gian
- **Ghi chú nguyên tử (atomic notes):** `kebab-case-slug.md` — chữ thường, chỉ dùng dấu gạch ngang
- **Họp hành:** `YYYY-MM-DD-TenCuoi.md`

### Slug
- kebab-case: `facebook-ad-optimization` thay vì `Facebook Ad Optimization`
- Không có dấu gạch dưới, không có ký tự đặc biệt
- Nhất quán trên các hệ thống tệp Linux/macOS

## Quy tắc Frontmatter

**Mọi ghi chú PHẢI có:**
```yaml
---
title: "Tiêu đề chính xác"
slug: "tiêu-de-chinh-xac-slug"
category: project | area | resource | knowledge | daily | review
tags: [tag1, tag2]  # tối đa 5
status: draft | active | reference | output | archived
type: atomic-note | insight | meeting | project | literature-note
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

## Quy tắc thư mục

| Quy tắc | Chi tiết |
|---------|----------|
| Số tiền tố (Prefix numbers) | 00-99 để sắp xếp, khoảng cách 10 để mở rộng |
| Không có thư mục theo chủ đề | Dùng thẻ (tags) cho chủ đề, dùng thư mục cho loại ghi chú |
| Thư mục đính kèm duy nhất | `00-Meta/Attachments/` — tất cả tệp đều ở đây |
| Mẫu trong `_templates/` | Tiền tố dấu gạch dưới để sắp xếp lên đầu |

## Kỷ luật quy trình làm việc

### Thu thập (Inbox)
- Thu thập thô với ít ma sát nhất có thể
- Ghi chú hàng ngày = hộp thư đến nhanh cho những ý nghĩ thoáng qua
- Cắt từ web, highlight → đưa vào Inbox trước
- **KHÔNG sắp xếp trong lúc thu thập**

### Kết nối (Kiểm tra hàng tuần)
- Xóa sạch inbox → di chuyển/phân loại tất cả mục
- Liên kết ghi chú với các MOC hiện có hoặc lưu trữ nếu ngữ cảnh đã hết giá trị
- Nâng cấp những ý tưởng hàng ngày có giá trị cao → ghi chú nguyên tử
- Tạo liên kết ngược (backlink) cho mọi ghi chú mới ngay lập tức

### Quyết định (Kiểm tra dự án)
- Mọi ghi chú về dự án đều phải trả lời: "Tiếp theo sẽ xảy ra gì?"
- Quy trình nghiên cứu: thu thập → trích xuất → gắn thẻ → nâng cấp các điểm đã được xác thực
- Dòng chảy từ họp đến đầu ra: thu thập → quyết định → nhận thức → bản thảo

### Giao hàng (Outputs)
- Phương pháp lấy bằng chứng trước: tập hợp các tham chiếu liên kết → trích xuất luận điểm → soạn thảo → xác minh
- Lưu phiên bản sẵn sàng giao hàng trong `70-Outputs/`
- Giữ nguyên các liên kết nguồn đính kèm

## Lịch trình bảo trì

| Tần suất | Nhiệm vụ | Người phụ trách |
|----------|----------|-----------------|
| Hàng ngày | Ghi lại các thu thập vào ghi chú hàng ngày | Smee + Hùng |
| Hàng tuần (Chủ nhật 20h) | Xóa sạch inbox, liên kết các mục mồ côi, cập nhật dự án | Smee |
| Hàng tháng | Dọn dẹp thẻ, kiểm tra đường dẫn hỏng | Smee |
| Hàng quý | Lưu trữ các mục cũ, rà soát cấu trúc, danh sách plugin | Smee + Hùng |

## Tiêu chuẩn chất lượng

### Bắt buộc phải có
- ✅ Frontmatter trên mọi ghi chú
- ✅ Ít nhất 1 liên kết ngược cho mỗi ghi chú mới
- ✅ kebab-case slug
- ✅ Trường status chính xác
- ✅ Ngày cập nhật cuối cùng hiện tại

### Nên có (Nice to Have)
- ⭐ Dòng tóm tắt trong frontmatter
- ⭐ Ghi chú liên quan được liên kết
- ⭐ Truy vấn Dataview cho bảng điều khiển
- ⭐ Lớp %% comments để hướng dẫn tác nhân (agent instructions)

## Chính sách lưu trữ

Di chuyển vào `60-Archive/` khi:
- Dự án hoàn thành (tiến độ = 100%)
- Ghi chú không hoạt động > 1 năm
- Bị thay thế bởi phiên bản mới hơn
- Không còn ý nghĩa thực thi

Việc lưu trữ giúp giữ cho gốc kho lưu trữ sạch sẽ. Các ghi chú đã lưu trữ vẫn có thể tìm kiếm nhưng không làm rối các quan điểm đang hoạt động.

---
*Phiên bản quy chế: 1.0*
*Lần xem xét cuối cùng: 2026-06-12*
