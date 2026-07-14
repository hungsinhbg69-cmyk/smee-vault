---
title: "Chiến lược đặt giá nâng cao"
slug: "advanced-bidding"
category: resource
tags: [facebook-ads, meta-ads]
status: "draft"
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

# 10 - Chiến lược đặt giá nâng cao (Chi tiết chiến lược bid)

## 5 Chiến lược đặt giá (2026)

| Strategy | Control Model | Khi nào dùng |
|----------|---------------|--------------|
| **Lowest Cost** | Không ràng buộc; Meta chi tiêu ngân sách để đạt kết quả tối đa | Mặc định cho 80% chiến dịch <€50k/tháng |
| **Cost Cap** | Mục tiêu CPA trung bình; có thể đặt giá cao hơn trong từng phiên đấu thầu | Khi có ≥50 chuyển đổi/tuần/ad-set + ≥€5k chi tiêu hàng tuần/ad-set |
| **Bid Cap** | Giới hạn cứng cho mỗi phiên đấu thầu | Thu hẹp: dữ liệu cấp phiên đấu thầu đã biết, danh mục sản phẩm lớn với biên lợi nhuận/SKU chính xác |
| **Value Optimization** | Tối ưu hóa theo giá trị mua hàng (không phải khối lượng) | DTC với phạm vi AOV rộng |
| **ROAS Goal** | Ngưỡng ROAS tối thiểu | Thương mại điện tử có theo dõi doanh thu; đặt ở 80% mức ROAS trung bình 28 ngày qua |

## Cost Cap — 3 Điều kiện sống còn

1. **≥50 conversions/week/ad-set** — Meta cần tín hiệu thống kê để ước tính CPA
2. **≥€5,000 weekly spend/ad-set** — Ngân sách hàng ngày đủ tham gia đấu thầu để trung bình hóa các chuyển đổi chi phí cao + thấp
3. **Cap ≥ trailing 7-day average CPA** — Cap đặt ở mức mục tiêu là đặt dưới mức trung bình thực tế → giao dịch sụp đổ

> ⚠️ Cost Cap quá thấp: ad-set với €12 Cost Cap trong thị trường CPAs €16 sẽ cạn kiệt cửa sổ khám phá ngân sách hàng ngày, thất bại trong việc tìm kiếm kho lưu trữ tuân thủ, gần như không có lượt hiển thị.
>
> Bid Cap làm hỏng nhiều chiến dịch hơn là sửa chữa: chỉ 20-25% các bài kiểm tra giảm CPA, còn lại tăng hoặc sụp đổ giao dịch.

## Value Optimization (VO)

### Khi nào dùng
- DTC với phạm vi AOV rộng (từ $20 đến $500+)
- Cần tối ưu giá trị MUA HÀNG, không phải khối lượng
- Danh mục sản phẩm có chênh lệch biên lợi nhuận đáng kể giữa các mặt hàng

### Cách hoạt động
- Mô hình dự đoán giá trị mua hàng, không chỉ xác suất
- Ưu tiên người dùng có khả năng chi tiêu cao hơn
- Tự động phân bổ ngân sách cho các chuyển đổi có giá trị cao

### Setup VO
1. Set objective = Sales (Conversions)
2. Trong ad set: optimization_guide = VALUE
3. Đảm bảo sự kiện Purchase có tham số `value` với doanh thu chính xác
4. Cần ≥50 purchases/week để mô hình có tín hiệu đủ

## ROAS Goal

### Khi nào dùng
- Thương mại điện tử với theo dõi doanh thu (CAPI + Pixel)
- Đã có dữ liệu lịch sử ROAS ổn định
- Muốn kiểm soát lợi nhuận tối thiểu

### Setting ROAS Goal
1. Set objective = Sales (Conversions)
2. Trong ad set: optimization_guide = ROAS GOAL
3. Set roas_goal_value = 80% mức ROAS trung bình 28 ngày qua
4. Không đặt quá thấp → Meta sẽ không giao dịch đủ khối lượng

> ⚠️ ROAS Goal yêu cầu theo dõi doanh thu sạch. Sự kiện trùng lặp hoặc giá trị thiếu sót → phép toán ROAS sai lệch → giao dịch không tối ưu.

## CBO — 3 Sai lầm phổ biến

### 1. Giới hạn chi tiêu tối thiểu không bảo vệ các ad-set nhỏ
Thuật toán dừng lại 3/4 ad-set ở mức sàn, dồn 75% cho "người thắng" — thường là đối tượng rộng có tín hiệu lịch sử cao nhất, chưa chắc là phân khúc ICP.

**Fix:** Thiết lập ngân sách hàng ngày tối thiểu bằng nhau cho mỗi ad-set khi kiểm tra.

### 2. Ngân sách chiến dịch ≠ giới hạn chi tiêu hàng ngày
Với ngân sách trọn đời (lifetime budget), Meta nén/mở rộng việc giao dịch hàng ngày theo cơ hội đấu thầu. Thứ Hai có thể chi tiêu gấp đôi mức trung bình hàng ngày, thứ Tư chỉ 0.4x.

**Fix:** Giám sát tốc độ pacing mỗi giờ trong 3 ngày đầu. Điều chỉnh nếu cần.

### 3. Chồng chéo đối tượng giết hiệu quả
Các ad-set cùng Advantage Campaign Budget mà chia sẻ chồng chéo đối tượng → thuật toán không thể arbitrage, cứ phục vụ những người giống nhau từ 2 nguồn.

**Fix:** Kiểm tra chồng chéo đối tượng trước khi bật CBO. Loại trừ các phân khúc trùng lặp.

## Quy tắc mở rộng quy mô (Scaling Rules)

### Mở rộng theo chiều dọc (tăng ngân sách)
- Tăng ngân sách ≤20% mỗi lần, ≥48h giữa các lần tăng
- Giám sát CPA chặt chẽ sau mỗi lần tăng
- Nếu CPA tăng >20% → tạm dừng và giữ nguyên trong 3-4 ngày trước khi thử lại

### Mở rộng theo chiều ngang (ad-set mới)
- Sao chép chiến dịch thắng với ngân sách cao hơn
- Kiểm tra các phân khúc đối tượng mới (LL 3-5%)
- Mở rộng địa lý (thành phố/tỉnh mới)
- Thêm loại vị trí hiển thị nếu hiện tại bị giới hạn

> 💡 Mở rộng theo chiều ngang > mở rộng theo chiều dọc: bảo toàn dữ liệu giai đoạn học tập ban đầu trong khi mở rộng phạm vi tiếp cận.

## Các giai đoạn Pacing ngân sách (Budget Pacing Phases)

### Mô hình ba giai đoạn

| Phase | Days | Velocity | Mục đích |
|-------|------|----------|----------|
| **Exploration** | 1-7 | Giới hạn ở 60-70% ngân sách hàng ngày tối ưu | Mua thời gian cho thuật toán để lập bản đồ phong cảnh chuyển đổi |
| **Momentum** | 8-21 | Tăng dần ≤15% mỗi 48h | Khai thác trí tuệ tích lũy + học tập tăng dần |
| **Saturation** | 22+ | Chậm lại hoặc làm mới sáng tạo | Tần suất vượt quá 2.5-3.0 → bão hòa đối tượng |

### Các chỉ số Pacing chính (Key Pacing Metrics)

1. **Budget Deployment Velocity (BDV)**: Chi tiêu hàng ngày thực tế ÷ Chi tiêu hàng ngày mục tiêu, tính theo giờ. BDV 1.2 vào giữa trưa = pacing nhanh hơn 20%
2. **Learning Stability Index**: Hệ số biến thiên trong CPA qua các cửa sổ trượt 7 ngày — tăng lên = thuật toán đang gặp khó khăn ở tốc độ cao hơn
3. **Temporal Conversion Density**: Những giờ nào tạo ra tỷ lệ chuyển đổi cao nhất → cơ hội phân bổ theo thời gian (dayparting)
4. **Creative Fatigue Acceleration Rate**: Tốc độ tăng tần suất mỗi ngày trong khi duy trì/tăng ngân sách — >0.3/ngày = vùng nguy hiểm

> 💡 Pacing chậm hơn, kiểm soát tốt thường mang lại ROAS dài hạn tốt hơn vì ưu tiên trí tuệ thuật toán thay vì giao dịch brute-force. Meta diễn giải tốc độ pacing như một biến thế cho sự khẩn cấp của chiến dịch — pacing nhanh hơn = chuyển đổi ngay lập tức hơn hiệu quả học tập.

## Những điểm chính cần nhớ (Key Takeaways)
- Lowest Cost = mặc định cho 80% chiến dịch
- Cost Cap cần 3 điều kiện: ≥50 conv/tuần, ≥€5k chi tiêu/tuần, cap ≥ CPA trung bình
- Value Optimization cho phạm vi AOV rộng
- ROAS Goal đặt ở 80% mức ROAS trung bình 28 ngày qua
- Mở rộng theo chiều ngang > mở rộng theo chiều dọc để bảo toàn dữ liệu học tập

---
*Created: 2026-06-15 | Sources: facebook-ads-deep-dive, ads-deep-dive-june-2026*
