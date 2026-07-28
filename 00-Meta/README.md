---
title: "Kho lưu trữ — Trung tâm não bộ thứ hai"
slug: "vault-hub"
category: meta
tags: [meta, vault-governance, protocol]
status: active
type: hub
created: 2026-06-12
last_updated: 2026-07-13
---

# 🧠 Kho lưu trữ — Trung tâm não bộ thứ hai

## 🏗 Kiến trúc: Lai giữa PARA và Zettelkasten

```
vault/
├── AGENTS.md                   # Quy tắc chung cho OpenClaw + Hermes
├── 00-Meta/                    # Quản trị, MOCs, bảng điều khiển, phân loại học
│   └── README.md               # ← Bạn đang ở đây
├── 01-Inbox/                   # Thu thập nhanh, chưa sắp xếp
├── 02-Daily/                   # Ghi chú hàng ngày (YYYY-MM-DD.md)
├── 10-Projects/                # Các dự án đang hoạt động (có giới hạn thời gian)
├── 20-Areas/                   # Trách nhiệm liên tục
├── 30-Resources/               # Tài liệu tham khảo
├── 40-Knowledge-Synthesis/     # Ghi chú nguyên tử, kiến thức vĩnh cửu
│   ├── Insights/               # Những nhận thức mới được khám phá
│   ├── Concepts/               # Các khái niệm đã tổng hợp
│   └── Frameworks/             # Mô hình tư duy, khung lý thuyết
├── 50-Reviews/                 # Đánh giá hàng tuần/tháng
├── 60-Archive/                 # Các mục đã hoàn thành/không hoạt động
├── 70-Outputs/                 # Sản phẩm cuối cùng (bản nháp, công bố)
├── _templates/                 # Mẫu ghi chú có thể tái sử dụng
└── _scripts/                   # Script tự động hóa kho lưu trữ
```

## 📐 Quy ước đặt tên

| Loại | Định dạng | Ví dụ |
|------|-----------|-------|
| Chỉ mục dự án | `TênDựAn.md` | `Facebook-Marketing-Automation.md` |
| File có ngày tháng | `YYYY-MM-DD-MôTả.md` | `2026-06-12-cet-lap-vault.md` |
| Ghi chú nguyên tử | `slug-dau-ghep-thuong-hoa.md` | `zettelkasten-modern-principles.md` |
| Ghi chú cuộc họp | `YYYY-MM-DD-TenCuocHop.md` | `2026-06-15-ket-noi-voi-khach-hang.md` |

**Quy tắc:**
- Slug dạng kebab-case (dấu gạch ngang, không có dấu gạch dưới)
- Chỉ viết thường
- Không thêm hậu tố "notes" — file CHÍNH là ghi chú
- YYYY-MM-DD cho tất cả ngày tháng → sắp xếp theo thời gian ở mọi nơi

## 🏷 Phân loại học thẻ (Tag Taxonomy)

```
#project/Alpha        #area/Marketing      #Status/draft
#Status/active        #Method/interview     #Concept/attention
#Tool/Obsidian        #Type/meeting         #Type/atomic-note
```

**Giới hạn:**
- Tối đa 5 thẻ mỗi ghi chú
- Viết thường, có dấu gạch ngang
- Xác định phân loại học tại đây trước khi đạt 400 ghi chú
- Mục tiêu: <50 thẻ duy nhất tổng cộng

## 📊 Chỉ số sức khỏe (Kiểm toán hàng quý)

| Chỉ số | Mục tiêu | Hiện tại |
|--------|----------|----------|
| Tổng số ghi chú | Đang tăng trưởng | 0 |
| Trung bình liên kết/ghi chú | 8+ | 0 |
| Tỷ lệ ghi chú mồ côi | <10% | N/A |
| Nợ inbox | <5 mục | 0 |
| Sử dụng mẫu | >80% | 0% |

## 🔄 Quy trình: Thu thập → Kết nối → Quyết định → Thực thi

```
Inbox (01-Inbox/) 
  → Ghi chú hàng ngày (02-Daily/) — thu thập nhanh
  → Đánh giá hàng tuần — kết nối & sắp xếp lại
  → Dự án (10-Projects/) hoặc Ghi chú nguyên tử (40-Knowledge-Synthesis/)
  → Lưu trữ (60-Archive/) khi hoàn thành
```

## 🤖 Lớp giao tiếp tác nhân

- `%% bình luận hai dấu phần trăm %%` — Hướng dẫn vô hình ở chế độ đọc (tác nhân đọc markdown thô)
- `<!-- Bình luận HTML -->` — Chỉ thị cấu trúc cho định tuyến/ưu tiên

## 📌 Quy tắc cốt lõi

1. **Kho lưu trữ = Bộ nhớ, không phải Lưu trữ** — Mỗi ghi chú đều có ngữ cảnh và kết nối
2. **Hàng ngày = Thước đo, Nguyên tử = Bền vững** — Đừng bao giờ trộn lẫn chúng
3. **Nâng hạng khi được trích dẫn 2+ lần** — Ý tưởng hàng ngày → ghi chú nguyên tử
4. **Liên kết hai chiều bắt buộc** — Mỗi ghi chú mới phải có liên kết trong cùng ngày
5. **Frontmatter trên mọi ghi chú** — Cho phép truy vấn Dataview
6. **Đánh giá hàng tuần không thể thương lượng** — 30 phút, có giá trị hơn bất kỳ plugin nào
7. **Tối đa 2 lần thu thập mỗi phiên** — Chất lượng hơn số lượng

## 📚 Mẫu (trong `_templates/`)

| Mẫu | Trường hợp sử dụng |
|----------|-------------------|
| Ghi chú hàng ngày | Ghi nhật ký hàng ngày, thu thập nhanh |
| Ghi chú gặp gỡ | Tóm tắt cuộc họp, các mục cần thực hiện |
| Đã bị loại.md | Tạo MOC cho dự án mới |
| Ghi chú- chú | Tổng hợp bài báo học thuật |
| Ghi chú nguyên tử | Ghi chú kiến thức vĩnh cửu |
| Xem hàng tuần.md | Nghi thức đánh giá hàng thứ Bảy |
| Ghi chú thử ra | Nhật ký kiểm tra giả thuyết |

## 🔗 Liên kết chính

- [[Protocol]] — Quản trị + Quy tắc tác nhân (đã hợp nhất, nguồn sự thật duy nhất)
- [[Vault-MOC]] — Bản đồ nội dung trung tâm
- [[Vault-Quick-Ref]] — Điều hướng tiết kiệm token
- [[Tag-Taxonomy]] — Tham khảo đầy đủ thẻ

---
*Tạo: 2026-06-12 | Đánh giá lại lần cuối: 2026-07-13 (đồng bộ phân cấp)*
*Kiến trúc: Lai giữa PARA và Zettelkasten*
*Tác nhân: Smee (OpenClaw) + Hùng (Con người)*
