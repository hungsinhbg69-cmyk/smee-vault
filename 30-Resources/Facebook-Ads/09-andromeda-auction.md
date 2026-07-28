---
title: "Thị trường đấu giá Andromeda"
slug: "andromeda-auction"
category: resource
tags: [facebook-ads, meta-ads]
status: "draft"
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

# 09 - Andromeda & Động lực đấu giá (Hệ thống đấu giá mới)

## Thuật toán Meta Andromeda (2024-2026)

Andromeda thay thế engine xếp hạng cũ của Meta — hệ thống học sâu hai giai đoạn chạy trên toàn bộ bề mặt: Facebook Feed, Instagram Feed, Reels, Stories, Marketplace.

### Kiến trúc 2 Giai đoạn

| Stage | Mô tả | Thời gian |
|-------|--------|-----------|
| **Retrieval** | Tra cứu láng giềng gần nhất xấp xỉ — nhúng quảng cáo/người dùng thành vector, lọc từ hàng tỷ ứng viên xuống vài nghìn ứng viên liên quan | ~50ms |
| **Ranking** | Mô hình xếp hạng sâu đánh giá 100+ đặc trưng: lịch sử tương tác, tín hiệu mua hàng, yếu tố sáng tạo (kiểu hình ảnh, cảm xúc văn bản, CTA), hiệu suất lịch sử, thời điểm trong ngày, thiết bị, sự cạnh tranh đấu giá | ~150ms |

### Công thức Giá trị Tổng thể

```
Total Value = Bid × Predicted Action Rate + Estimated User Value
```

- **Predicted Action Rate**: Xác suất người dùng thực hiện hành động bạn đặt giá thầu (click, mua hàng, lead)
- **Estimated User Value**: Chất lượng trải nghiệm dài hạn — phạt các quảng cáo mà người dùng ẩn, báo cáo hoặc bỏ qua trong vòng 1 giây
- **Hệ quả**: Sáng tạo chất lượng thấp không chỉ tự đánh bại mình mà còn giảm tính cạnh tranh trong đấu giá

### Hàm ý của Andromeda

1. **Sáng tạo = Mục tiêu tiếp cận mới.** Andromeda phân tích hình ảnh, văn bản, định dạng, tông giọng và tín hiệu ngữ cảnh để tự động suy ra đối tượng mục tiêu. Sáng tạo yếu = không được hiển thị vì thuật toán không xác định được đối tượng.
2. **Các tập quảng cáo với định nghĩa chặt chẽ hoạt động ổn định nay thường không thoát khỏi giai đoạn học** — vì lớp retrieval đã biết phải hiển thị quảng cáo cho ai mà không cần được chỉ dẫn.
3. **Andromeda đòi hỏi dữ liệu nhiều hơn tiền nhiệm:** cần ≥50 sự kiện tối ưu hóa/tập quảng giá/tuần để thoát khỏi giai đoạn học một cách ổn định. CPA trong giai đoạn học cao hơn 20-35% so với mức trung bình sau khi đã học xong.

## Động lực đấu giá: Meta vs Google

| Dimension | Google Ads | Meta Ads |
|-----------|------------|----------|
| Kích hoạt đấu giá | Truy vấn tìm kiếm của người dùng | Người dùng mở ứng dụng / cuộn feed |
| Tín hiệu ý định | Rõ ràng (từ khóa) | Ẩn (Hồ sơ người dùng + hành vi) |
| Điểm số chất lượng | Quality Score 1-10 | Chẩn đoán liên quan (Trên/Bình thường/Dưới mức trung bình) |
| Công thức thắng cuộc | Điểm số chất lượng Bid_× | Bid × Tỷ lệ hành động × Chất lượng quảng cáo |
| Loại đấu giá | Chung | Vickrey thứ hai-primce |

## Ba Chẩn đoán Liên quan (Mức Quảng cáo)

Chẩn đoán ở mức quảng cáo, không phải mức chiến dịch. Dùng để xác định chính xác nguồn gốc vấn đề:

1. **Xếp hạng Chất lượng**: Chất lượng cảm nhận so với các quảng cáo cạnh tranh — Dưới mức trung bình = Vấn đề sáng tạo
2. **Xếp hạng Tỷ lệ tương tác**: Tỷ lệ tương tác dự kiến — Dưới mức trung bình = Hook/thông điệp yếu
3. **Xếp hạng Tỷ lệ chuyển đổi**: Tỷ lệ chuyển đổi dự kiến so với đối tượng+mục tiêu — Dưới mức trung bình = Vấn đề trang đích/đề nghị

## Cấu trúc Chiến dịch Hoạt động (2026)

### Lựa chọn A: Advantage+ Shopping (ASC+) — Mặc định cho E-commerce
- Gộp prospecting + retargeting vào một chiến dịch duy nhất
- Phân bổ ngân sách tự động giữa việc thu hút khách hàng mới và mua hàng của khách hàng hiện có
- Đặt "Ngân sách giới hạn cho Khách hàng Hiện có" ở mức **20-30%** để ngăn chặn sự cạnh tranh nội bộ (cannibalization)
- Tài khoản chi tiêu >€5K/tháng → ASC+ vượt trội so với cấu trúc phễu thủ công

### Lựa chọn B: Cấu trúc 6-3-1 Tiêu chuẩn — Cho tài khoản cần kiểm soát sáng tạo
- **6 tập quảng cáo** (rộng hoặc Advantage+ Audience)
- **3 sáng tạo** mỗi tập quảng cáo
- **1 góc độ thắng cuộc** mỗi sáng tạo
- Sản xuất đủ dữ liệu cho giai đoạn học mà không phân mảnh ngân sách

### Lựa chọn C: Chiến dịch Bán hàng Thủ công — Doanh nghiệp dịch vụ / Lead Gen
- Cần nhiều kiểm soát hơn về thông điệp, trang đích, chiến lược đặt giá thầu
- Tốt nhất cho B2B, chuyên gia tư vấn, các đại lý, dịch vụ địa phương
- Các mặt hàng có giá cao nơi tính nhất quán từ quảng cáo đến LP (trang đích) là quan trọng

## Những gì Vẫn Hoạt động vs Những gì Đã Chết (2026)

| ✅ VẪN HOẠT ĐỘNG | ❌ ĐÃ CHẾT / ĐANG CẢM GIÁC |
|---|---|
| Mục tiêu tiếp cận rộng (18-65+) | Tích hợp sở thích (10+ sở thích) |
| Vị trí Advantage+ | Lựa chọn vị trí thủ công |
| Nội dung phong cách UGC | Quảng cáo doanh nghiệp quá bóng bẩy |
| Theo dõi server-side CAPI | Thuộc tính chỉ dựa trên Pixel |
| Chiến lược sáng tạo ưu tiên Video | Hình ảnh tĩnh làm định dạng chính |
| Tích hợp dữ liệu bên thứ nhất | Phụ thuộc vào cookie bên thứ ba |
| Tăng 20% ngân sách mỗi 3 ngày | Tăng gấp đôi ngân sách qua đêm |

## Những điểm cốt lõi cần nắm
- Andromeda = học sâu 2 giai đoạn (Retrieval ~50ms + Ranking ~150ms)
- Tổng giá trị = Haid_ Hành động và ước tính giá trị người dùng
- Chất lượng sáng tạo thấp → giảm tính cạnh tranh trong đấu giá, không chỉ hoạt động kém hiệu quả
- Chẩn đoán liên quan ở mức quảng cáo: dùng để xác định chính xác vấn đề về sáng tạo hay vấn đề sau click

---
*Created: 2026-06-15 Nguồn: facebook-Những quảng cáo sâu sắc, sâu sắc-thôi-ki-ki-di-di-26*
