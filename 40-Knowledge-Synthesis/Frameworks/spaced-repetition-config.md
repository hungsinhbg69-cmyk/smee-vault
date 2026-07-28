---
title: " Hệ thống lặp lại không gian (SRS)"
slug: spaced-repetition-system-srs
category: knowledge
tags: [learning, spaced-repetition, config]
status: active
type: system-config
created: 2026-06-27
last_updated: 2026-06-27
---

# Sự lặp lại không gian — Máy tri thức Thị trường

Chuyển đổi các ghi chú trong thẻ nhớ dùng Obsidian Sự lặp lại không gian plugin.

## Tổ chức cỗ máy (theo thư mục)

| Folder | Deck Name | Focus Area | Review Schedule |
|--------|-----------|------------|-----------------|
| 30-Resources/Facebook-Ads/* | FB Ads Mastery | Algorithm, targeting, bidding | Daily review |
| 40 đồng vàng-Sythesis/Frameworks/* | Frameworks & Systems | JeffSu, khuôn khổ marketing | Xem xét kỹ hàng tuần |
| 40-Knowledge-Synthesis/Insights/* | Market Intelligence | Bac Giang, trends | Bi-weekly review |

## Quy tắc sáng tạo

### Định dạng thẻ flash (dòng động)
```
Question?::Answer with key details
```

### Định dạng xoá tập tin  
```
The Facebook algorithm in 2026 prioritizes ==engagement quality== over raw volume. Key signal: [[time-spent-viewing]].
```

### Định dạng đa dòng
```
What are the 5 KPIs from Co Hoc Tinh Hoa?
1. Customer Retention Rate
2. Content Value Score (Shares + Saves > Likes)
3. Algorithm Adaptation Speed
4. Crisis Response Time  
5. Long-term LTV:CAC Ratio::Remember: "Truoc khi danh nguoi phai biet gi minh" - measure before launch!
```

## Review Schedule

| Card Age | Interval | Difficulty Multiplier |
|----------|----------|----------------------|
| New (0-3 days) | Every day | 1.5x harder |
| Growing (4-14 days) | Every 2 days | 1.2x |
| Stable (15+ days) | Hàng tuần đến hàng tháng | Standard |

## Thẻ ưu tiên cho SRS

- `#srs/high` - Phải biết: tín hiệu chính của thuật toán FB, chiến lược trả tiền, tiêu chuẩn đo lường
- `#srs/medium` — Quan trọng nhưng có thể tham khảo: cụ thể về chi tiết nghiên cứu trường hợp  
- `#srs/low` - Rất vui được biết: những mẹo tối ưu nhỏ, tùy thích công cụ
- `#flashcard` - Tự động bị SRS đánh cắp plugin tạo bài

## Plugin Thiết lập (hiện thời)

```json
{
  "flashcardTags": ["#flashcards"],
  "convertHighlightsToClozes": true,
  "enableReviewReminders": false,
  "reviewReminderIntervalMinutes": 5,
  "singleLineCardSeparator": "::",
  "multilineCardSeparator": "?",
  "clozePatterns": ["==[123;;]answer[;;hint]=="]
}
```

## Những ví dụ về các tia chớp của SRS là từ sự hiểu biết FB

### Thẻ ưu tiên cao (Must know)

Facebook Thuật toán 2026 ưu tiên chất lượng đính hôn hơn khối lượng thô:: dành thời gian xem, tiết kiệm, chia sẻ. giống như là ít trọng lượng nhất.

Quy tắc tăng trưởng của chiếc CBO là gì? Facebook adschi phí cho mỗi ngày tối đa 20%, tỷ lệ người thắng theo chiều ngang, sau đó theo chiều ngang với khán giả mới.

Phạm vi CPM lý tưởng cho thị trường Việt Nam vào năm 2026 là gì?::FB Ad Vietnam: $0.50-1.50 cho các đạt rộng, $1.50-3.00 cho mục tiêu. Nếu CPM >4, khán giả quá hạn hoặc quá mệt mỏi sáng tạo phát hiện.

Các cặp đấu giá của người đấu giá là gì?::Tier 1 (số lợi nhuận 80%+): điểm số điểm tương quan cao + giá thấp. 2 (số mũ 60-80%): cân bằng/b. Tier 3: tối ưu hóa — kiểm tra CTR, tần số, độ sáng tạo.

Tần số tối ưu cho các chiến dịch chuyển đổi là gì?::: tần số tối ưu < 3.0 để tìm kiếm (những sáng tạo mới). Tần số 1.5-2.5 để tái tạo. Nếu tần số >4. 0 trong 7 ngày = sự mệt mỏi sáng tạo, xoay tài sản mới.

### Thẻ ưu tiên vừa

Làm thế nào để cấu trúc một Facebook Ads Phân cấp chiến dịch:::Champaign (bị thu hút) > Ad Set (Khán giả + ngân sách) > Ad (creative). Một mục tiêu trong mỗi chiến dịch. Thử một biến trong một thời gian giữa các bộ quảng cáo.

Ngân sách tối thiểu cho việc thử nghiệm có ý nghĩa là gì:: 10-20/ngày trên quảng cáo tối thiểu cho tầm quan trọng thống kê trên thị trường Việt Nam. cho các chiến dịch chuyển đổi nhắm đến các sản phẩm giá trị cao, bắt đầu 30+/ngày.

Chiến dịch mua sắm kiểu Ad advantage+ được dùng tốt nhất cho mục đích nào?:: mục nhập sản phẩm E-commerce với dữ liệu điểm ảnh sạch. Tốt nhất khi bạn có 50+ chuyển đổi/ tuần. Hãy dùng MIME để tăng cường người thắng cuộc tranh cử bằng tay, chứ không phải bắt đầu lạnh.

### Thẻ ưu tiên thấp

Mẹo nhanh: Khi nào bạn nên chuyển từ CPC sang CPM?: Khi nào thì CTR < 1% — chuyển sang CPM sẽ mang lại tự do hơn. Khi CTR > 2%, hãy gắn với CPC hoặc tối ưu hóa sự sáng tạo trước tiên.

Điểm ảnh được đề nghị cho năm 2026 là gì? Facebook ads♪:: API Tổng cộng điểm ảnh trình duyệt. Theo dõi bên máy chủ cần thiết sau khi iOS 17+ ATT thay đổi. Kiểm tra các sự kiện trong bộ quản lý sự kiện mỗi ngày.

---
*Conated: 2026-06-20 by Smee — Lớp 4 (SRS)*
