---
title: "Cấu hình Lặp lại theo khoảng cách"
slug: "spaced-repetition-config"
category: meta
tags: [srs, review, learning]
status: active
type: config
created: 2026-06-20
last_updated: 2026-06-20
---

# 🔄 Cấu hình Hệ thống Lặp lại theo Khoảng cách (SRS)

> Cấu hình cho plugin Obsidian Spaced Repetition.
> Ôn tập các ghi chú nguyên tử theo đường cong quên lãng để kiến thức không bị mất đi.

## 📐 Cài đặt khoảng thời gian

| Giai đoạn | Số ngày giữa các lần ôn tập | Mục tiêu chất lượng |
|-----------|-----------------------------|---------------------|
| Mới → Lần 1 ôn tập | 1 ngày | ≥70% nhớ lại |
| Lần 1 → Lần 2 ôn tập | 3 ngày | ≥60% nhớ lại |  
| Lần 2 → Lần 3 ôn tập | 7 ngày | ≥50% nhớ lại |
| Kiến thức ổn định | 30+ ngày | Chế độ bảo trì |

## 🎯 Chiến lược Ôn tập

### Hàng ngày (5-10 phút)
- Chỉ ôn các ghi chú có **status = active** trong thư mục `40-Knowledge-Synthesis/`
- Bỏ qua bản nháp và phiên bản đã bị thay thế
- Tập trung vào khung quảng cáo Facebook + tâm lý học Bac Giang (kiến thức mang lại lợi nhuận cao)

### Giai đoạn Kết nối hàng tuần (Thứ 7 lúc 20:00)
- Ôn tập tất cả các ghi chú mà hôm nay SRS đánh dấu là "thất bại" (<50% nhớ lại)
- Cập nhật ghi chú với những nhận thức mới
- Hạ cấp kiến thức cũ → lưu trữ hoặc đánh dấu đã bị thay thế

## 📊 Chỉ số chất lượng

```dataview
TABLE 
  length(rows) AS "Tổng số ghi chú",
  mean(status) AS "Trạng thái trung bình"
FROM "40-Knowledge-Synthesis/Insights" OR "40-Knowledge-Synthesis/Frameworks"
WHERE type = "atomic-note"
GROUP BY status
```

## 🔔 Quy tắc cảnh báo (Giao thức Agent)

- **>15 ghi chú chờ ôn tập** → cảnh báo Hùng ngay (quá tải)
- **<3 lần ôn tập hoàn thành tuần trước** → gợi ý điều chỉnh lịch trình
- **Ghi chú thất bại 2+ lần liên tiếp** → đánh dấu để viết lại hoặc lưu trữ

---

*Tạo: 2026-06-20 bởi Smee — Triển khai Lớp 5 (Cấu hình SRS)*
*Cấu hình trong Cài đặt Obsidian → Lặp lại theo khoảng cách → điều chỉnh các khoảng thời gian ở trên.*
