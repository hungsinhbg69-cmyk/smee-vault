---
title: "Quyền sở hữu & Theo dõi"
slug: "attribution-tracking"
category: resource
tags: [facebook-ads, meta-ads]
status: "draft"
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

# 11 - Quyền sở hữu & Đo lường (Quyền sở hữu + Hệ thống đo lường)

## Cửa sổ quyên sở hữu (Sau iOS 14)

| Window | Khi nào dùng | Ghi chú |
|--------|--------------|---------|
| **7-day click + 1-day view** (default) | Đa số tài khoản — cân bằng giữa độ chính xác của tín hiệu và khối lượng dữ liệu | Mặc định, dùng cho 90% trường hợp |
| **1-day click** | Mua hàng theo cảm hứng, sản phẩm ít cần suy nghĩ | Quyên sở hữu thận trọng |
| **7-day click only** | Tài khoản cần quyên sở hữu thận trọng | Loại trừ tín hiệu xem qua (view-through) |

### 12 tháng 1 năm 2026 — Cập nhật về Quyền sở hữu
Meta đã vĩnh viễn loại bỏ cửa sổ xem 7 ngày và 28 ngày từ Ads Insights API. Ngay lập tức, bảng điều khiển của nhà quảng cáo mất tín hiệu cho các chuyển đổi xem qua (view-through conversions).

> ⚠️ **Quan trọng:** Chỉ còn quyên sở hữu theo click + cửa sổ xem ngắn hạn. Các chuyển đổi xem qua giảm đáng kể → con số ROAS thấp hơn trước đây mặc dù hiệu suất thực tế có thể không đổi.

## Hệ thống đo lường (2026)

```
Layer 1: Pixel + CAPI → theo dõi chuyển đổi chính
Layer 2: Kiểm tra chéo GA4 → kiểm tra tính hợp lý (GA4 luôn thấp hơn Meta do sự không khớp trong mô hình quyên sở hữu)
Layer 3: MMM / Thử nghiệm tăng thêm → các quyết định ngân sách vượt qua toán học của bất kỳ nền tảng đơn lẻ nào
Layer 4: SKAdNetwork → chiến dịch ứng dụng di động (theo dõi riêng biệt, không phải phần mở rộng của bộ công cụ web)
```

### Layer 1: Pixel + CAPI
- Nguồn theo dõi chuyển đổi chính
- Khóa loại bỏ trùng lặp: event_id + Pixel ID + event_name
- Cửa sổ: các sự kiện trong vòng 48 giờ → Meta chỉ tính MỘT chuyển đổi
- **Chế độ lỗi phổ biến:** Pixel gửi `event_id: "order_123_1678901234"`, server gửi `"order_123_1678901234.567"` (độ chính xác khác nhau) → Meta đếm 2 chuyển đổi → ROAS bị thổi phồng

### Layer 2: Kiểm tra chéo GA4
- GA4 luôn thấp hơn Meta do sự không khớp trong mô hình quyên sở hữu
- Dùng để kiểm tra tính hợp lý, không phải nguồn chân lý
- Cấu trúc UTM chuẩn: source/medium/campaign/content/term
- Theo dõi xu hướng hàng tháng, không phải số liệu tuyệt đối

### Layer 3: Thử nghiệm Tăng thêm (Incrementality Testing)
- Tạm dừng tiếp cận 10-15% khán mục tiêu từ quảng cáo trong 2 tuần
- So sánh tỷ lệ chuyển đổi giữa nhóm được xử lý và nhóm kiểm soát
- Phân tách doanh thu thực sự tăng thêm khỏi những gì đã được quyên cho
- Đặc biệt quan trọng với ASC (Automatic Targeting) nhắm mục tiêu rộng (nguy cơ chồng chéo quyên sở hữu cao)

### Layer 4: SKAdNetwork
- Theo dõi chiến dịch ứng dụng di động
- Theo dõi riêng biệt, không phải phần mở rộng của bộ công cụ web
- Hỗ trợ iOS 16+ cho SKAdNetwork 4.0

## AEM — Đo lường sự kiện tổng hợp (8 Sự kiện ưu tiên)

Sắp xếp theo giá trị chuyển đổi, KHÔNG phải tần suất:

| Rank | Event | Lý do xếp hạng này |
|------|-------|--------------------|
| 1 | Purchase | Giá trị chuyển đổi cao nhất |
| 2 | InitiateCheckout | Tín hiệu ý định mua hàng cao |
| 3 | AddToCart | Thường xuyên nhưng giá trị thấp hơn |
| 4 | ViewContent | Phạm vi tiếp cận rộng nhất, giá trị thấp nhất |
| 5 | Lead | Giá trị trung bình-cao cho tạo lead |
| 6 | CompleteRegistration | Kích hoạt tài khoản |
| 7 | Search | Tín hiệu ý định, giá trị biến động |
| 8 | PageView | Giá trị chuyển đổi thấp nhất |

> ⚠️ Xếp hạng AddToCart cao hơn Purchase vì thấy nhiều hơn → Meta quyên cho AddToCart, toán học ROAS sụp đổ nếu sự kiện Purchase bị thiếu hoặc chậm trễ.

## Chi tiết loại bỏ trùng lặp sự kiện (Event Deduplication)

### Định dạng khóa loại bỏ trùng lặp
```
Deduplication key: event_id + Pixel ID + event_name
Window: các sự kiện trong vòng 48 giờ
Kết quả: Meta chỉ tính MỘT chuyển đổi
```

### Các chế độ lỗi phổ biến
1. **Không khớp về độ chính xác:** `"order_123"` vs `"order_123.0"` → được tính là 2 chuyển đổi
2. **Khoảng cách thời gian >48h:** Pixel phát sự kiện tại T=0, CAPI phát tại T=50h → không loại bỏ trùng lặp
3. **Định dạng event_id khác nhau:** Một bên dùng UUID, bên kia dùng số đơn hàng → không khớp

### Thực hành tốt nhất
- Tạo event_id CHỈ MỘT LẦN (tốt nhất là phía server)
- Sử dụng định dạng nhất quán giữa Pixel và CAPI
- Bao gồm thời gian trong event_id để gỡ lỗi: `"order_123_20260615T130000Z"`
- Giám sát tỷ lệ loại bỏ trùng lặp trong Events Manager

## Chất lượng khớp sự kiện (EMQ)

| Score | Level | Mô tả |
|-------|-------|-------|
| 0-2 | Poor | Thiếu email + số điện thoại — CAPI gần như vô dụng |
| 3-5 | Fair | Có email HOẶC số điện thoại — có thể khớp một phần |
| 6-8 | Good | Tối thiểu có Email + Số điện thoại — cải thiện hiệu suất đo lường được |
| 9-10 | Excellent | Toàn bộ tham số (email, số điện thoại, tên, IP, user agent) — khớp tối ưu |

### Trọng số các tham số EMQ
1. **Email** (trọng số cao nhất) — mã hóa SHA-256
2. **Số điện thoại** (trọng số thứ hai) — định dạng E.164
3. **Tên đệm + Họ**
4. **Địa chỉ IP của khách hàng**
5. **Chuỗi User agent**

> ⚠️ EMQ ≥6 = điểm hòa vốn từ CAPI. Dưới 6: Meta không thể khớp đa số sự kiện → CAPI gần như vô dụng.

## Khung thử nghiệm Tăng thêm (Incrementality Testing)

### Thiết lập
1. **Nhóm kiểm soát:** 10-15% khán mục tiêu, KHÔNG được tiếp xúc với quảng cáo
2. **Nhóm thử nghiệm:** Khán còn lại, hiển thị quảng cáo bình thường
3. **Thời gian:** Tối thiểu 2 tuần (bắt trọn chu kỳ hàng tuần)
4. **Chỉ số:** Sự khác biệt về tỷ lệ chuyển đổi giữa các nhóm

### Phân tích
```
Incremental ROAS = (Test CVR - Control CVR) × AOV / CPA
True Incremental Conversions = Test conversions - Control conversions
```

### Khi nào sử dụng
- Tài khoản ASC nhắm mục tiêu rộng (nguy cơ chồng chéo quyên sở hữu)
- Ngân sách lớn nơi những thay đổi nhỏ % cũng quan trọng ($10K+/tháng)
- Trước khi tăng ngân sách lớn
- Xác minh hiệu quả kênh theo quý

## Những điểm chính cần nhớ
- Cửa sổ quyền sở hữu đã đơn giản hóa: 7-day click + 1-day view là mặc định
- Hệ thống đo lường cần cả 4 lớp để có bức tranh hoàn chỉnh
- Định dạng khóa loại bỏ trùng lặp phải nhất quán giữa Pixel và CAPI
- EMQ ≥6 là yêu cầu để có cải thiện CAPI đo lường được
- Thử nghiệm tăng thêm phân tách doanh thu thực sự tăng thêm khỏi những gì đã được quyên cho

---
*Created: 2026-06-15 | Sources: facebook-ads-deep-dive, ads-deep-dive-june-2026*
