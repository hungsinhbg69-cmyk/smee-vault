---
title: "Facebook Ads - Ngân sách, Thể dục và Thể hiện bộ phim (2025-26)"
slug: "fb-budgeting-bidding-metrics"
category: knowledge
tags: ["facebook-ads", "budgeting", "bidding", "metrics", "cbo"]
status: active
type: reference
created: 2026-06-19
last_updated: 2026-06-24
---


# Facebook Ads — Ngân sách, Thể dục & trình diễn

Phân tích tổng hợp từ nguồn research notebook June 2026. Cover toàn bộ khía cạnh: CBO vs ABO, bid strategies, benchmarks, frequency management, attribution models.

---

## 1. Ngân quỹ tạo định vị — CBO đấu với ABO

### CBO (Nổ tay làm báp têm)
- **Mặc định cho scaling**: Meta AI phân phối budget real-time vào adset/creative tốt nhất (ref: 1-3)
- Thuật toán đọc early signals (fixates, autocar behaviors, scroll patterns) nhanh hơn human media buyer
- **Nhược điểm lớn**: Bias mạnh về existing winners — creative mới bị starve spend

**Người tiền sử dùng thuốc hạn chế:**
| Bước | Hành động |
|------|-----------|
| 1 | Mở CBO campaign → Edit adset cho creative mới |
| 2 | Bật "Adset Spending Limits" → chuyển từ % sang $ value |
| 3 | Set **Average Daily Minimum = 1x target CPA** (ví dụ CPA $50 → min $50/ngày) |
| 4 | Chạy 7 ngày cho fair test |
| 5 | Sau 7 ngày: remove minimum, để algorithm cạnh tranh tự do |

3 kịch bản sau 7 ngày (ref: 6-10):
1. **Winner ad**: Bắt đầu từ min budget → pick up spend nhanh trước 7 ngày → algorithm đẩy thêm
2. **Average performer**: Spend đều min budget, đạt target CPA nhưng không pull extra spend
3. **Loser ad**: Spend hết min nhưng CPA cao hơn target → stop loss

### ABO (Adset Budget Optimization) — Khi nào dùng?
- **Pure creative testing**: 5+ concepts khác nhau, cần fair shot equal footing (ref: 12-15)
- **Scaling individual winners**: Tăng từ $100 → $300 → $700 cho từng adset riêng biệt không ảnh hưởng cái khác
- Khi muốn surgical control budget per adset + active daily management

**Epert trích dẫn**: "ABO chưa chết-- có những trường hợp sử dụng thực sự để giành vị trí của nó, nhưng bạn cần phải hiểu bạn đang tham gia vào cái gì." (ref: 12)

### Công thức luyện tập tốt nhất (2026)
- **Testing campaign** (ABO): Mỗi adset $50/ngày cho creative mới
- **Scaling campaign** (CBO): Dùng Adset Spending Limits cho new packs → sau 7 ngày remove
- Creative thinking: **"Creative needs to be thought about in units"** — flexible ad packs 4-8 ads/group, không trộn old/new cùng pack (ref: 9)

---

## 2. Bidding Strategies

### Âm lượng cao nhất (Lowest Cost) — Mặc định & khuyến cáo (ref: 16-18)
- Meta tối ưu để spend budget FULL → get maximum conversions possible
- Phù hợp nhất cho beginners và most campaigns
- Không set cost cap/bid cap → let algorithm do its job

### Chi phí Cap (Cát cho mỗi kết quả Goal) — Chỉ Scaling (ref: 19-22)
**Khi nào dùng**: Chỉ cho scaling proven winners, KHÔNG cho testing
- Set cap = target CPA hoặc thấp hơn chút
- Inflate budget mạnh → squeeze cheap conversions during peak times (weekends)
- Cửa sổ phân phối: Chi phí trung bình nên quá mức cho phép nhấn 7 ngày)

**Chúng ta biết Scaking Ttic:**
> "Trong kỳ nghỉ cuối tuần, hiệu suất sẽ tốt hơn vì tỉ lệ chuyển đổi cao hơn, nhiều người có thời gian rảnh hơn và có chế độ mua sắm. Facebook Cho phép chi tiêu càng nhiều càng tốt khi đạt đỉnh điểm." (ref: 21-22)

**4 Scenarios với Manual Bids:**
| Scenario | Dấu hiệu | Action |
|----------|----------|--------|
| 1. tái tạo doanh thu nhưng không chi tiêu toàn bộ ngân sách (v. d., 200 đô la) | Hạ thấp quá | Dần dần tăng giá thầu 1 đô la cho đến khi hoàn toàn chi tiêu với kết quả tốt |
| 2. Chưa tạo ra sự chuyển đổi nào | Ngân sách chạy ra trước khi dữ liệu được thu thập | Tăng giá thầu hoặc đợi cho giai đoạn học để hoàn tất |
| 3 tốt CPA nhưng chi tiêu nhanh CPA tăng | # Bid too high # Quá cao. | Giảm giá xuống dần dần |
| 4. Thực hiện tốt mục tiêu CPA, chi tiêu toàn bộ ngân sách | Sweet spot | Để lại như-là, màn hình |

**Pro tip**: Luôn dùng "click only" attribution với manual bids để avoid view-through overattribution (ref: 22)

### Mục tiêu ROAS (giá trị bậc hai) — E-commerce cụ thể (ref: 23-26)
- Comment
- Perfect cho brands có: product price variance, fluctuating AOV, multiple service tiers ($200 vs $5,000 leads)
- Giao dịch- ra: Bộ chuyển đổi cao hơn nhưng có giá trị hơn

---

## 3 Mỗi ngày, với thời gian sống, ngân sách tạo ra và nhịp điệu

### Tờ Nhật báo Budgets Win (ref: 27-31)
| Factor | Daily | Lifetime |
|--------|-------|----------|
| Flexibility | ✅ Always adjustable | Yêu cầu ngày kết thúc cố định |
| Học tập khởi động lại giai đoạn | ✅ Minimal impact | _TIẾNG _NHỮNG NGƯỜI ĐỂ tái tạo chiến dịch = Học trở lại |
| Scalability | _Các thay đổi ngân sách dễ dàng | _Gỡ bỏ các mẫu dùng |

** Ngân sách mỗi ngày được tái thiết:**
- Dấu ngoặc dẫn thấp: **20-50/ngày**/adset (ref: 27)
- Dịch vụ danh sách cao (v. d., cài đặt địa bàn): **50+/ngày**/adset
- Gói thử nghiệm sáng tạo: Đặt ngân sách bạn có thể mất

### Pacing Rules
1. **Lanchon at night** ngày hôm sau đầy cửa sổ 24h, tránh những cây đinh giữa ngày kỳ lạ (ref: 32-33)
2. **Budget tăng**: +20-30% mỗi **3 ngày**(đường an toàn) hoặc sao lại quảng cáo với ngân sách cao hơn sau đó đợi 72h (ref: 34-35)
3. Tiêu chuẩn giết: chi tiêu đủ tiền, đủ lâu, không có nhân tố bên ngoài nào ngoài mô hình tài chính

---

## 4. Những biểu hiện của con chó — Số thứ tự quan trọng

### CPM (Cost Per Mime) — Chi phí cho 1000 lần nhấn mạnh (ref: 38-40)
| Industry/Context | Healthy Range | Warning Sign |
|------------------|---------------|--------------|
| Local services | $10-$25 | bán kính ngắm mục tiêu >40 đô-la quá hẹp |
| E-commerce | $20-$30 sweet spot | >35 đô-la thị trường không lành mạnh, khán giả bão hòa |
| Sáng tạo đặc biệt cao | Có thể đạt $117+ với cùng một CNL | Không hẳn là xấu — tín hiệu nhắm chính xác (ref: 41-48) |

**Key  insight**: "Tôi không quan tâm đến CPM" nghĩa là có nhiều sự sáng tạo có thể nói với khán giả ít người. vấn đề là **CPA tương đối phá vỡ thậm chí**.

### CTR (Click- qua tỷ lệ)
- Chấp nhận tối thiểu: **>1%** (ref: 49)
- Sức khỏe như e-commerce quảng cáo: **1.5%-2.5%+** (ref: 40, 50-51)
- > 2, 5% = kết nối sáng tạo mạnh

### CPC (Cát mỗi nhắp)
| Level | Threshold |
|-------|-----------|
| Good | <$2 |
| Excellent | <$1 |
| Industry-dependent | Dịch vụ pháp lý có thể là < $120 và vẫn còn tuyệt (ref: 38) |

---

## Quản lý tần số 5, Hệ thống Quản lý — Khuếch đại điện thoại (ref: 55-57)

Tần số = bao nhiêu lần một người bình thường trong khán giả của bạn nhìn thấy quảng cáo. sử dụng như là vị trí hộp chẩn đoán:

| Funnel Stage | Target Frequency | Meaning |
|--------------|------------------|---------|
| **Đầu phễu** (Tìm kiếm khách hàng tiềm năng) | 1.0 - 1.15 | Liên tục tiếp cận người dùng mới ✅ |
| **Middle of Funnel** (Nurture) | 1.3 - 1.5 | Successfully nurturing warm audiences ⚠️ |
| **Bottom of Funnel** (sự hồi sinh) | 1.5+ | Mong đợi cho CTA mạnh mẽ cung cấp _POR |

### Những người béo (ref: 56-57)
- Sau khi **4 ấn tượng**: xác suất chuyển hóa giọt xuống **56%**
- Tần số > **5.0 trong vài tuần** = cờ đỏ chính, kiệt sức sáng tạo
- Hành động khi mệt mỏi: xoay sáng tạo mới hoặc mở rộng thính giả

---

## 6. Mô hình phân phối vào năm 2026 (ref: 58-77)

### Ấn phẩm sẽ được ghi rõ trong trang web này?
- **Xem qua quá trình phân phối**: Nếu xem qua >20% các cửa hàng bị theo dõi chuyển đổi sang "7-ngày" hoặc "7-ngày" click / 1 ngày xem đính hôn" (ref: 61-67)

### Meta Phân phối tăng dần (New 2025/2026)
- Báo cáo chỉ bán hàng xảy ra có chủ đích vì quảng cáo
- Lọc giao thông hữu cơ và các kênh chuyển đổi khác
- Chính xác hơn nhưng thường cho thấy số chuyển đổi thấp hơn tiêu chuẩn (ref: 62-63)

### Theo dõi phần ba — thiết yếu tại tỷ lệ
> "Meta thường xuyên trượt **15%-30%* dữ liệu chuyển đổi thực sự do tính năng cá nhân của iOS và ad blockers" (ref: 70-74)

| Tool | Use Case |
|------|----------|
| **Hyros** | Tốt nhất để theo dõi từ quảng cáo dành trọn chuyến đi khách hàng (đang tính tiền, nhiều điểm cảm ứng) (ref: 76-77) |
| **Triple Whale** | Tập trung E-commerce, tích hợp cửa sổ |
| **Northbeam** | & Giới thiệu đa chiều trên quy mô |

**Rule**: vượt qua 1000/ngày đáng tin cậy yêu cầu máy chủ bên cạnh các thiết bị theo dõi bên thứ ba. Meta Dữ liệu quản lý kiểu Ads (ref: 70-75)

---

## Tham khảo nhanh — Ma trận quyết định

```
┌─────────────────────┬──────────────────┬─────────────────────┐
| Context             | Budget           | Bid Strategy        │
├─────────────────────┼──────────────────┼─────────────────────┤
| New creative test   | ABO, $50/adset   | Highest Volume      │
| Scaling winners     | CBO + Spending Lmt│ Cost Cap @ target  │
| High-value products | CBO              | ROAS Target         │
| Low-ticket leads    | Daily budget     | Highest Volume      │
| Weekend scaling     | CBO inflated     | Cost Cap            │
└─────────────────────┴──────────────────┴─────────────────────┘

Benchmarks to watch:
• CTR > 1% (target 1.5-2.5%)
• CPC < $2 (excellent <$1)  
• CPM: local $10-25, ecom $20-30
• Frequency: prospecting ~1.0-1.15, retargeting >1.5
• View-throughs < 20% of conversions
```

---

*Griated from NotebookLM phân tích — 19 tháng 6 năm 2026*
*Các bản đồ đến nguồn UUIDs trong sổ tay cb6a557-deb0-4a9b-abfa-2ebb2ab84db (27 nguồn tài liệu được phân tích)*
