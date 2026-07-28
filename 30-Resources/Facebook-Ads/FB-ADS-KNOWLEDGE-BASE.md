---
title: "📘 Cơ Sở Kiến Thức Facebook Ads — Tổng Hợp 2026"
slug: "fb-ads-knowledge-base"
category: resource
tags: [vault-maintenance]
status: "draft"
type: reference
created: 2026-06-24
last_updated: 2026-06-24
---


# 📘 Cơ Sở Kiến Thức Facebook Ads — Tổng Hợp 2026

> **Mục đích:** Nguồn sự thật duy nhất (single source of truth) cho toàn bộ kiến thức về Facebook/Meta Ads. Được tổng hợp, phân loại và tối ưu hóa để agent đọc/nhánh nhanh.
> 
> **Cập nhật cuối:** 2026-06-20 | **Tổng hợp từ:** ~45+ file trong vault
> 
> **Cấu trúc:** 8 module theo quy trình thực chiến → từ thiết lập đến quy đổi (attribution)

---

## 📋 Mục Lục Nhanh

| Module | Nội dung | File gốc |
|--------|----------|----------|
| M1 | Fundamentals & Hierarchy | 01-fundamentals.md, INDEX |
| M2 | Khán giả đang nhắm đến cuộc chiến | Rạp 02-targe.md, lợi thế hơn-narrow-targeing.md |
| M3 | Định dạng sáng tạo và Kiểm tra | 3ccative-formats.md, sáng tạo kiểm tra-BAR-lever.md |
| M4 | Bidding, Budget & CBO | 04-bidding-budget.md, 10-advanced-bidding.md |
| M5 | Tracking: Pixel + CAPI + Attribution | 05-tracking-pixel.md, 11-attribution-tracking.md |
| M6 | Lợi thế+AI | Góc nhìn 0-07-clock |
| M7 | & Lực hấp dẫn | 9 và chuyển sang dùng thẻ tín dụng, quảng cáo sâu-jun-jun-26.md |
| M8 | Thuật toán, Benchmarks + Case Studies | 8- ti- mét- đối xứng. md, cs-key-ins-ights-26.d, vận động phân tích tập tin |

---

## MODULE 1: FUNDAMENTALS & CAMPAIGN HIERARCHY

### Cấu trúc Chiến dịch (3-Tier)
```
Tài khoản Quảng cáo
└── Chiến dịch (Mục tiêu duy nhất)
    └── Nhóm quảng cáo (Targeting + Ngân sách + Vị trí hiển thị)
        └── Quảng cáo (Sáng tạo A/B/C, Nội dung, Nút kêu gọi hành động)
```

**Quy tắc vàng 2026:** 1 chiến dịch cho mỗi mục tiêu. Không bao giờ trộn Bán hàng + Dữ liệu khách hàng tiềm năng + Lưu lượng truy cập trong cùng một chiến dịch. Mỗi mục tiêu được tối ưu hóa khác nhau.

### 7 Mục Tiêu Chiến Dịch — Khi Nào Dùng Gì?

| Mục tiêu | Mục đích | KPI chính | Phù hợp cho |
|-----------|----------|-----------|-------------|
| **Bán hàng** (Conversions) | Thúc đẩy mua hàng + bán qua catalog | CPA, ROAS | Thương mại điện tử, DTC |
| **Thu thập dữ liệu khách hàng tiềm năng** | Thu thập lead trên nền tảng | CPL, chất lượng form | B2B, bất động sản, giáo dục |
| **Tin nhắn** | Hội thoại Messenger/IG | Chi phí/bắt đầu hội thoại | Doanh nghiệp địa phương, tư vấn |
| **Lưu lượng truy cập** | Click vào website/app | CPC, CTR, lượt xem LP | blog, trang hạ cánh, liên lạc |
| **Nhận thức / Tiếp cận** | Ghi nhớ thương hiệu + tiếp cận tối đa | GRP, tăng nhận diện quảng cáo | Ra mắt thương hiệu mới |
| **Tương tác** | Tương tác bài viết, like trang | Chi phí tương tác | Xây dựng cộng đồng |
| **Video Views** | Video watches/completions | 3-sec views, ThruPlays | Content creators, training |

### CBO vs ABO — Khi Nào Dùng Gì?

| Tình huống | Loại Ngân sách | Lý do |
|----------|-------------|-------|
| Kiểm tra các đối tượng mới | **ABO** (ngân sách nhóm quảng cáo) | Chi tiêu đều cho mỗi lần kiểm tra |
| Mở rộng quy mô các chiến thắng | **CBO** (ngân sách chiến dịch) | Thuật toán tìm kết quả rẻ nhất |
| 3+ nhóm quảng cáo đã được thiết lập | **CBO** | Phân phối đã được chứng minh hiệu quả |
| Ngân sách hạn chế (<$50/ngày tổng cộng) | **ABO** | Đảm bảo mỗi lần kiểm tra đều nhận chi tiêu |
| Chỉ có một nhóm quảng cáo | Cả hai | Không khác biệt với 1 nhóm quảng cáo |

---

## MODULE 2: CHIẾN LƯỢC TARGETING ĐỐI TƯỢNG

### 3 Loại Đối tượng

| Loại | Mô tả | Khi dùng |
|------|--------|----------|
| **Cốt lõi** (Manual) | Nhân khẩu học, vị trí, sở thích, hành vi | Tài khoản mới, khởi động lạnh |
| **Tùy chỉnh** (Retargeting) | Người truy cập Pixel, danh sách khách hàng, người tương tác | MOFU/BOFU — luôn vượt trội hơn so với đối tượng lạnh |
| **Giống nhau** (LAL) | Giống những khách hàng tốt nhất | Tìm kiếm TOFU có dữ liệu hỗ trợ |

### Advantage+ Audiences vs Targeting Truyền thống

| Chiều kích | Sở thích Truyền thống | Đối tượng Advantage+ (Tiêu chuẩn 2026) |
|-----------|---------------------|-------------------------------------|
| Đầu vào | Sở thích/hành vi hẹp | Rộng (chỉ tuổi/giới tính/vị trí) |
| AI tìm người dùng? | Không — lựa chọn thủ công | Có — dựa trên dữ liệu quy đổi + tín hiệu sáng tạo |
| Phụ thuộc dữ liệu | Chất lượng cơ sở dữ liệu sở thích | Chất lượng quy đổi Pixel/CAPI |
| Hiệu suất với pixel | Cơ sở | **Tốt hơn 3-5 lần** so với target theo sở thích |

### Quy tắc: Advantage+ > Targeting hẹp khi có ≥50 conversions/tuần/nhóm quảng cáo. Chỉ dùng target theo sở thích cho tài khoản mới/khởi động lạnh.

### Phân cấp Phễu × Bản đồ Đối tượng

| Giai đoạn Phễu | Chiến lược Đối tượng |
|--------------|----------------------|
| **TOFU** (Tìm kiếm) | Advantage+ rộng, LAL 1% từ người mua, Sở thích (chỉ tài khoản mới) |
| **MOFU** (Xem xét) | Người truy cập website 30-90d, Người xem video 50%+, Người tương tác IG 90d |
| **BOFU** (Quy đổi/Tái mục tiêu) | Người truy cập 7-14d, Người bỏ giỏ hàng, Khách mua trước đó (bán chéo), Người tương tác 30d |

### Thang đo Chất lượng LAL
- **1%** → Giống nhất, chất lượng cao nhất, phạm vi tiếp cận nhỏ nhất — BẮT ĐẦU TỪ ĐÂY
- **5%** → Cân bằng giữa chất lượng + phạm vi
- **10%** → Phạm vi lớn nhất, chất lượng thấp nhất
- Nguồn đối tượng tối thiểu: 1.000 người (nguồn tốt nhất = người mua > lead > người tương tác)

### Mẹo Targeting Đặc thù Việt Nam
- Danh sách số điện thoại có tỷ lệ khớp cao hơn email ở VN
- Tương tác Instagram cao — dùng người tương tác IG cho tái mục tiêu
- Messenger là kênh quy đổi chính — mục tiêu Tin nhắn hoạt động tốt
- Target theo bán kính hiệu quả cho doanh nghiệp địa phương

---

## MODULE 3: ĐỊNH DẠNG SÁNG TẠO & HỆ THỐNG KIỂM TRA

### Định dạng Quảng cáo Có sẵn (2026)

| Định dạng | Tốt nhất cho | Thông số kỹ thuật |
|--------|----------|------------------|
| Ảnh đơn/Tĩnh | Kiểm tra nhanh, chi phí thấp | 1080x1080 hoặc 1080x1350 (chân dung), JPG/PNG |
| Comment | Tương tác cao | Hook trong 3s đầu, MP4/MOV, luôn bật phụ đề |
| Quảng cáo Carousel | Trưng bày sản phẩm (2-10 thẻ) | Mỗi thẻ có CTA riêng |
| Reels Ads (9:16) | Tìm kiếm theo phong cách UGC | Toàn màn hình dọc, cảm giác chân thực |
| Quảng cáo Collection | Lưới sản phẩm thương mại điện tử | Bìa + lưới sản phẩm phủ lên |
| Lead Ads | Thu thập form trên nền tảng | Không cần landing page — ma sát thấp hơn |

### Khung Kiểm tra Sáng tạo (4 Bước)

**Bước 1: Kiểm toán Đối thủ cạnh tranh**
- Xác định các quảng cáo chạy từ 30+ ngày trong ngành → cấu trúc hook, cách khung offer
- Công cụ: Thư viện Quảng cáo Facebook, Meta Ad Inspector

**Bước 2: Ma trận Biến thể**
- 3 góc độ hook × 2 xử lý hình ảnh × 2 CTA = **12 biến thể cho mỗi brief sáng tạo**
- Không kiểm tra nhiều biến cùng lúc — kiểm tra biệt lập từng biến

**Bước 3: Cửa sổ Kiểm tra Tối thiểu**
- 1.000-2.000 lượt hiển thị + 7 ngày trước khi mở rộng/thu hồi
- Cần ≥50 conversions để có ý nghĩa thống kê

**Bước 4: Chu kỳ Làm mới**
- Mỗi **10-14 ngày** — đừng đợi hiệu suất sụp đổ
- Tuổi thọ sáng tạo trên Meta: **3-6 tuần**
> Tần suất >3.0 = tín hiệu mệt mỏi → làm mới ngay lập tức

### Thang đo Hook-Rate (lượt xem 3 giây / lượt hiển thị)
| Điểm số | Mức độ |
|-------|--------|
| 25%+ | Khá tốt |
| 30%+ | Tốt |
| 40%+ | Xuất sắc |

### Ma trận Quyết định UGC vs Sáng tạo Sản xuất

| Tình huống | Định dạng Tốt hơn | Tại sao |
|-----------|---------------|---------|
| Tìm kiếm đối tượng lạnh | **UGC** | Hòa vào feed; cảm giác như được đồng nghiệp giới thiệu |
| Sản phẩm dưới $100 | **UGC** | Ngưỡng xem xét thấp hơn |
| Sản phẩm $200+ | **Sản xuất/Hybrid** | AOV cao cần tín hiệu tin cậy |
| Tái mục tiêu đối tượng ấm | Cả hai | Đối tượng ấm phản ứng với các tín hiệu khác nhau |
| Nhận thức thương hiệu | **Sản xuất** | Chất lượng chuyên nghiệp thể hiện uy tín |

### Quy tắc Phân bổ Ngân sách (70-20-10)
- **70%** → Các chiến dịch thắng cuộc (mở rộng những gì đang hoạt động)
- **20%** → Kiểm tra các đối tượng/góc độ mới
- **10%** → Kiểm tra định dạng sáng tạo

---

## MODULE 4: ĐẤU GIÁ, NGÂN SÁCH & MỞ RỘNG QUY MÔ

### Loại Ngân sách

| Loại | Mô tả | Khi dùng |
|------|--------|----------|
| **Hàng ngày** | Chi tiêu trung bình/ngày (dao động ±15%) | Chi tiêu dự đoán được, phân phối ổn định |
| **Toàn bộ vòng đời** | Tổng chi tiêu qua thời gian chiến dịch | Chiến dịch có thời hạn, sự kiện, khuyến mãi |

### 5 Chiến lược Đấu giá — Khi Nào Dùng?

| Chiến lược | Mô hình Kiểm soát | Yêu cầu | Khi dùng |
|----------|---------------|---------|----------|
| **Chi phí thấp nhất** (Mặc định) | Không ràng buộc; tối đa hóa kết quả trong ngân sách | Không có gì | 80% chiến dịch — BẮT ĐẦU TỪ ĐÂY |
| **Giới hạn chi phí** | Mục tiêu CPA trung bình | ≥50 quy đổi/tuần + ≥€5k chi tiêu/tuần | Khi đã biết target CPA, giai đoạn mở rộng |
| **Giới hạn đấu giá** | Trần cứng mỗi phiên đấu giá | Dữ liệu cấp phiên đấu giá đã biết | Phiên đấu giá cạnh tranh, biên lợi nhuận/SKU chính xác |
| **Tối ưu hóa Giá trị** | Tối ưu cho GIÁ TRỊ mua hàng không phải số lượng | Phạm vi AOV rộng ($20-$500+) | DTC với biên lợi nhuận khác nhau giữa các sản phẩm |
| **Mục tiêu ROAS** | Ngưỡng ROAS tối thiểu | Theo dõi doanh thu sạch (CAPI+Pixel) | Thương mại điện tử đã có ROAS lịch sử ổn định |

### Giới hạn Chi phí — 3 Điều Kiện Sống Còn
1. ≥50 conversions/tuần/nhóm quảng cáo → Meta cần tín hiệu thống kê để ước tính CPA
2. ≥€5.000 chi tiêu hàng tuần/nhóm quảng cáo → đủ tham gia phiên đấu giá
3. Cap ≥ trung bình 7 ngày qua của CPA → đặt cap dưới mức thực tế = sụp đổ phân phối

### Giai đoạn Học (Learning Phase) — Quy tắc Quan trọng

| Kích hoạt | Hành động Yêu cầu |
|---------|-------------------|
| Chiến dịch mới được tạo | Cho phép 48h trước khi đánh giá hiệu suất |
| Thay đổi ngân sách >25% | Đặt lại giai đoạn học |
| Đổi sáng tạo | Có thể kích hoạt học lại |
| Quảng cáo tạm dừng + tái kích hoạt | Vào lại giai đoạn học |
| **Con số thần kỳ: ≥50 sự kiện tối ưu hóa/tuần/nhóm quảng cáo** | Thoát khỏi giai đoạn học một cách tự nhiên |

### Trạng thái Giai đoạn Học
- **"Hạn chế về dữ liệu"** = chưa đủ sự kiện → gom nhóm các nhóm quảng cáo hoặc mở rộng target
- **"Hoạt động" (không có huy hiệu)** = đã thoát thành công → tối ưu hóa thoải mái
> CPA trong giai đoạn học cao hơn **20-35%** so với mức trung bình sau khi thoát khỏi giai đoạn học

### Quy tắc Mở rộng — Theo chiều dọc vs theo chiều ngang

| Phương pháp | Cách thức | Ưu điểm | Nhược điểm | Quy tắc |
|--------|-----|------|-------|----------|
| **Theo chiều dọc** (tăng ngân sách) | Tăng trên nhóm quảng cáo cũ | Đơn giản, giữ dữ liệu học | Rủi ro đặt lại giai đoạn học nếu tăng quá nhanh | ≤20% mỗi lần, ≥48h giữa các lần |
| **Theo chiều ngang** (sao chép + mở rộng) | Sao chép chiến dịch → kiểm tra đối tượng mới | Bảo toàn dữ liệu học | Nhiều công việc quản lý hơn | Khuyến nghị — bảo toàn dữ liệu học |

### Các Giai đoạn Phân phối Ngân sách

| Giai đoạn | Ngày | Tốc độ | Mục đích |
|-------|------|----------|---------|
| **Khám phá** | 1-7 | Giới hạn ở 60-70% ngân sách tối ưu | Mua thời gian cho thuật toán lập bản đồ phong cảnh quy đổi |
| **Động lượng** | 8-21 | Tăng ≤15% mỗi 48h | Khai thác trí tuệ tích lũy |
| **Bão hòa** | 22+ | Chậm lại hoặc làm mới sáng tạo | Tần suất >2.5-3.0 = bão hòa đối tượng |

### CBO — 3 Sai lầm Phổ biến
1. **Giới hạn chi tiêu tối thiểu không bảo vệ các nhóm quảng cáo nhỏ** → Thuật toán để 3/4 ở sàn, dồn 75% cho "người thắng cuộc"
2. **Ngân sách chiến dịch ≠ giới hạn chi tiêu hàng ngày** → Thứ Hai có thể chi tiêu gấp đôi mức trung bình, thứ Tư chỉ 0.4x (ngân sách vòng đời)
3. **Chồng chéo đối tượng giết hiệu quả** → Thuật toán không thể arbitrage khi chia sẻ đối tượng

---

## MODULE 5: THEO DÕI — PIXEL + CAPI + QUY ĐỔI

### Hệ thống Đo lường (4 Lớp)

```
Lớp 1: Pixel + CAPI → theo dõi quy đổi chính ← NGUỒN SỰ THẬT
Lớp 2: Kiểm tra chéo GA4 → kiểm tra sanity (GA4 luôn thấp hơn Meta)
Lớp 3: MMM / Thử nghiệm tăng thêm → quyết định ngân sách vượt trên toán học nền tảng
Lớp 4: SKAdNetwork → chiến dịch ứng dụng di động (theo dõi riêng)
```

### Pixel + CAPI — Quy tắc Loại trùng

| Tham số | Yêu cầu |
|-----------|---------|
| **Khóa loại trùng** | event_id + ID Pixel + tên sự kiện |
| **Cửa sổ thời gian** | Sự kiện trong 48h → Meta đếm MỘT quy đổi |
| **Thực hành tốt nhất** | Tạo event_id LẦN ĐẦU TIÊN server-side, định dạng nhất quán trên cả hai |

### Chất lượng Khớp Sự kiện (EMQ) — Hiệu quả CAPI

| Điểm số EMQ | Mức độ | Kết quả |
|-----------|-------|---------|
| 0-2 | Kém | CAPI gần như vô dụng |
| 3-5 | Khá | Có thể khớp một phần |
| **6-8** | **Tốt** | **Điểm hòa vốn — lợi nhuận đo lường được** ← MỤC TIÊU |
| 9-10 | Xuất sắc | Khớp tối ưu |

> ⚠️ EMQ ≥6 = điểm hòa vốn từ CAPI. Dưới 6: CAPI gần như vô dụng. Các tham số ưu tiên: Email (SHA-256) > Số điện thoại (E.164) > Tên > IP > User Agent.

### AEM — Đo lường Sự kiện Tổng hợp (8 Sự kiện Ưu tiên)

| Hạng mục | Sự kiện | Lý do xếp hạng này |
|------|-------|------------------|
| 1 | **Mua hàng** | Giá trị quy đổi cao nhất |
| 2 | **Bắt đầu thanh toán** | Tín hiệu ý định cao |
| 3 | **Thêm vào giỏ hàng** | Thường xuyên nhưng giá trị thấp hơn |
| 4 | **Xem nội dung** | Phạm vi rộng nhất, giá trị thấp nhất |
| 5 | **Lead** | Trung bình-cao cho thu thập lead |
| 6 | **Hoàn thành đăng ký** | Kích hoạt tài khoản |
| 7 | **Tìm kiếm** | Tín hiệu ý định, giá trị biến động |
| 8 | **Xem trang** | Giá trị quy đổi thấp nhất |

> ⚠️ Xếp hạng AddToCart cao hơn Purchase vì thấy nhiều hơn → Meta gán cho AddToCart, toán học ROAS sụp đổ nếu thiếu/delayed Purchase.

### Cửa sổ Quy đổi (Cập nhật sau tháng 1/2026)

| Cửa sổ | Khi nào dùng | Ghi chú |
|--------|--------------|---------|
| **7-day click + 1-day view** (mặc định) | 90% tài khoản — cân bằng độ chính xác và khối lượng | Mặc định, lựa chọn an toàn |
| **1-day click** | Mua hàng tức thời, sản phẩm ít xem xét | Bảo thủ |
| **7-day click chỉ** | Tài khoản cần quy đổi bảo thủ | Không có tín hiệu view-through |

> ⚠️ 12 tháng 1 năm 2026: Meta vĩnh viễn loại bỏ cửa sổ 7-day view và 28-day view từ Ads Insights API. View-through conversions giảm → số liệu ROAS thấp hơn mặc dù hiệu suất thực tế có thể không đổi.

### Khung Thử nghiệm Tăng thêm (Incrementality)
- Giữ lại **10-15% đối tượng** khỏi quảng cáo trong **2 tuần**
- So sánh tỷ lệ quy đổi giữa nhóm được xử lý và nhóm kiểm soát
- Đặc biệt quan trọng với target Advantage+ rộng (rủi ro chồng chéo quy đổi)
> Công cụ Conversion Lift miễn phí từ Meta — dùng khi ngân sách $10K+/tháng

---

## MODULE 6: CHIẾN DỊCH AI ADVANTAGE+

### Chiến dịch Mua hàng Advantage+ (ASC+)

| Chiều kích | Thương mại điện tử Truyền thống | ASC+ |
|-----------|----------------------|------|
| Số chiến dịch cần thiết | 3-5 (tìm kiếm, tái mục tiêu, catalog) | **1** (kết hợp tất cả) |
| Nhóm quảng cáo | Nhiều đối tượng phân đoạn | Tín hiệu xác định bởi AI |
| Vị trí hiển thị | Lựa chọn thủ công | Tự động tối ưu hóa |
| Thời gian quản lý | 5-10 giờ/tuần | **1-2 giờ/tuần** |
| Hiệu suất | Tốt với tối ưu hóa | Thường TỐT HƠN với dữ liệu |

### Yêu cầu & Thiết lập ASC+
- ✅ Danh mục sản phẩm Facebook đã kết nối + được Meta phê duyệt
- ✅ Tối thiểu **50+ conversions/tháng** (sự kiện mua hàng)
- ✅ Theo dõi Pixel/CAPI các sự kiện mua hàng với giá trị
- ⚙️ Đặt "Giới hạn ngân sách cho Khách hàng hiện có" ở mức **20-30%** để ngăn ăn mòn

### Kế hoạch Triển khai 4 Giai đoạn ASC+

| Giai đoạn | Thời gian | Hành động | Mục tiêu |
|-------|----------|---------|--------|
| Nền tảng | Tuần 1-2 | Cài đặt Pixel + CAPI, kết nối catalog, bật Mua hàng Advantage+ | Hoàn thành thiết lập |
| Tích lũy dữ liệu | Tuần 3-6 | Để ASC thu thập dữ liệu, thêm 3-5 sáng tạo, giám sát CPA/ROAS/tần suất hàng tuần | 50+ mua hàng/tháng qua ASC |
| Tối ưu hóa | Tuần 7-12 | Phân tích các sáng tạo thắng cuộc, thêm biến thể, kiểm tra mức ngân sách (mở rộng 20%/3-4 ngày) | Chu kỳ làm mới sáng tạo đã thiết lập |
| Mở rộng quy mô | Tháng 3+ | Sao chép ASC với ngân sách cao hơn nếu có lợi nhuận, mở rộng LAL bổ sung, kiểm tra A/B sáng tạo hàng tháng | ~2 giờ/tuần quản lý |

### Khi nào KHÔNG dùng Advantage+
- Cửa hàng mới <10 conversions/tháng → không đủ dữ liệu cho AI
- Doanh nghiệp dịch vụ không có catalog sản phẩm
- Cần kiểm soát đối tượng chi tiết (target sở thích cụ thể)
- Ngân sách rất hạn chế (<$20/ngày tổng cộng)
- Giai đoạn kiểm tra cần kiểm soát biến biệt lập

---

## MODULE 7: THUẬT TOÁN ANDROMEDA & ĐỘNG LỰC PHIÊN ĐẤU GIÁ

### Kiến trúc Andromeda — Học sâu 2 giai đoạn

| Giai đoạn | Chức năng | Độ trễ | Mô tả |
|-------|----------|---------|--------|
| **Thu thập** | Tìm kiếm vector ANN | ~50ms | Nhúng quảng cáo/người dùng → lọc từ hàng tỷ xuống hàng nghìn ứng viên phù hợp |
| **Sắp hạng** | Mô hình học sâu đa tính năng | ~150ms | 100+ tính năng: lịch sử tương tác, tín hiệu mua hàng, yếu tố sáng tạo, hiệu suất lịch sử, thời gian trong ngày, thiết bị, cạnh tranh phiên đấu giá |

### Công thức Giá trị Tổng cộng (Người thắng cuộc Phiên đấu giá)
```
Giá trị Tổng = Đấu giá × Tỷ lệ Hành động Dự đoán + Giá trị Người dùng Ước tính
```

- **Tỷ lệ Hành động Dự đoán**: Xác suất người dùng thực hiện hành động đặt thầu của bạn (click, mua hàng, lead)
- **Giá trị Người dùng Ước tính**: Chất lượng trải nghiệm dài hạn — phạt quảng cáo mà người dùng ẩn/báo cáo/bỏ qua trong vòng 1 giây
> Hệ quả: Sáng tạo chất lượng thấp không chỉ hoạt động kém → giảm khả năng cạnh tranh trong phiên đấu giá hoàn toàn

### Sáng tạo = Targeting Mới — Thay đổi Mô hình
- Andromeda phân tích hình ảnh, văn bản, định dạng, giọng điệu, tín hiệu ngữ cảnh để tự suy ra đối tượng
> Sáng tạo yếu = không được hiển thị (thuật toán không xác định được đối tượng)
- Các thương hiệu thắng cuộc 2026 = các thương hiệu cung cấp cho hệ thống **đa dạng sáng tạo** (không phải khối lượng)
- Tài khoản gửi <8 sáng tạo mới/tháng = đang chạy trên thời gian vay mượn

### Cấu trúc Chiến dịch Hoạt động (Cây quyết định 2026)

| Tình huống | Cấu trúc Khuyến nghị | Tại sao |
|----------|----------------------|---------|
| Thương mại điện tử >€5K/tháng chi tiêu | **ASC+** | AI xử lý tìm kiếm + tái mục tiêu, hiệu quả quản lý |
| Cần kiểm soát sáng tạo | **Cấu trúc 6-3-1** (6 nhóm quảng cáo × 3 sáng tạo) | Dữ liệu học mà không phân mảnh ngân sách |
| B2B / Dịch vụ / Thu thập Lead | **Chiến dịch Bán hàng Thủ công** | Kiểm soát nhiều hơn về thông điệp, LP, chiến lược đấu giá |

### Vẫn Hoạt động vs Chết (Kiểm tra Thực tế 2026)

| ✅ VẪN HOẠT ĐỘNG | ❌ CHẾT/ĐANG CẢM GIÁC |
|---|------------------|
| Target rộng (18-65+) | Chồng chéo sở thích (10+ sở thích) |
| Vị trí hiển thị Advantage+ | Lựa chọn vị trí hiển thị thủ công |
| Nội dung phong cách UGC | Quảng cáo doanh nghiệp quá bóng bẩy |
| Theo dõi server-side CAPI | Quy đổi chỉ dựa trên Pixel |
| Chiến lược sáng tạo ưu tiên video | Ảnh tĩnh là định dạng chính |
| Tích hợp dữ liệu bên thứ nhất | Phụ thuộc cookie bên thứ ba |
| Tăng ngân sách 20% mỗi 3-4 ngày | Gấp đôi ngân sách qua đêm |

---

## MODULE 8: THỐNG KÊ, ĐÁNH GIÁ VÀ NHỮNG BÀI HỌC CHÌA KHÓA

### Các Thống kê Quan trọng Cần Theo dõi (Thứ tự Ưu tiên)

1. **ROAS** — Thống kê chính cho thương mại điện tử (Return on Ad Spend)
2. **CPA/CPP** — Chi phí trên mỗi Thu mua/Kết quả
3. **CPC** — Chi phí trên mỗi Click
4. **CTR** — Tỷ lệ Click Through (>1% = mức đánh giá tốt)
5. **Tần suất** — Quá cao = mệt mỏi quảng cáo (>3.0 kích hoạt làm mới)
6. **Tỷ lệ Quy đổi** — Hiệu quả landing page

### Mục tiêu ROAS theo Giai đoạn Phễu

| Giai đoạn | Mục tiêu ROAS | Ghi chú |
|-------|-------------|---------|
| Đầu phễu (nhận thức) | 2-3x chấp nhận được | Đối tượng rộng hơn, ý định thấp hơn |
| Giữa phễu (xem xét) | 3-4x mục tiêu | Đối tượng ấm |
| Cuối phễu (quy đổi) | 4-5x+ mục tiêu | Tái mục tiêu nóng |
| Đặc biệt là Tái mục tiêu | 5-10x điển hình | Người dùng có ý định cao |

### Thang đo Chi phí — Thị trường Việt Nam so với Toàn cầu

| Thống kê | Đánh giá US/EU | Thực tế Việt Nam | Ghi chú |
|--------|-----------------|------------------|---------|
| **CPM** | $10-$50 | ₫20.000-80.000 (~$0.80-3.20) | 50 quy đổi/tuần khả thi với chi tiêu thấp hơn ở VN |
| **CPC** | $0.50-$4.00 | Phạm vi thấp hơn | Phụ thuộc nặng vào ngành/chất lượng sáng tạo |
| **Tỷ lệ từ chối iOS ATT** | 70%+ | ~40-50% (chu kỳ nâng cấp thấp hơn) | Suy giảm Pixel ít nghiêm trọng hơn; CAPI vẫn được khuyến nghị |

### Thực tế Khoảng cách Quy đổi ROAS
- Hexclad: ROAS trên nền tảng Meta 3.1x → ROAS tổng hợp thực 2.1x (khoảng cách = vòng quay doanh thu đầy đủ)
- Chomps: 65% người mua iPhone → dữ liệu được báo cáo trên nền tảng không đáng tin cậy về mặt cấu trúc nếu không có kiểm tra chéo
> **Quy tắc:** Kiểm tra chéo với Northband/GA4/thử nghiệm tăng thêm — tối ưu hóa nguồn đơn nhất = bay mù sau iOS

### Tóm tắt 10 Bài học Chiến lược

| # | Bài học | Điểm mấu chốt |
|---|--------|---------------|
| 1 | Khoảng cách Quy đổi là Thách thức Định nghĩa | ROAS trên bảng điều khiển Meta ≠ ROAS tổng hợp thực. Kiểm tra chéo bắt buộc. |
| 2 | Chất lượng Sáng tạo > Khối lượng | Hexclad: 60→8 biến thể = cải thiện hiệu suất. Kỷ luật khái niệm > ngân sách sản xuất. |
| 3 | Advantage+ là Con dao Hai lưỡi | ASC cải thiện nhưng cần rào chắn (đối tượng dựa trên giá trị, đa dạng sáng tạo, mục tiêu điều chỉnh theo LTV). |
| 4 | Dữ liệu Bên thứ nhất = Tiêu chuẩn Vàng Mới | CAPI server-side + khảo sát sau mua hàng + gieo CRM = bộ ba chiến thắng. |
| 5 | Tái mục tiêu đang thay đổi về cơ bản | Hexclad: 60% quy đổi tái mục tiêu tự nhiên trong 72h. Chuyển dịch sang tìm kiếm + nuôi dưỡng. |
| 6 | Ít Target hơn, Hiệu suất tốt hơn | Titan Driveways: 1 chiến dịch → CPL giảm 50%. Soda Spoon: 1 quảng cáo → ROAS 3.61x. Tổng hợp thắng cuộc. |
| 7 | Dòng chảy Tín hiệu Đa kênh | Các kênh là bộ tạo tín hiệu cho nhau (ý định tìm kiếm Google → đối tượng Meta). |
| 8 | Cửa sổ Quy đổi làm méo thực tế | Tin tưởng dữ liệu khảo sát sau mua hàng khi nền tảng không đồng ý. |
| 9 | Thử nghiệm Tăng thêm là Không thể Thương lượng | Không có nó = tối ưu hóa trên hư cấu click cuối cùng. Dùng công cụ Conversion Lift miễn phí của Meta. |
| 10 | Brief Sáng tạo = Quy trình Khoa học | Sáng tạo tốt nhất đến từ ngôn ngữ thực tế của khách hàng — cụm từ cụ thể, kỳ lạ mà mọi người dùng khi giải thích tại sao họ mua. |

### Danh sách Kiểm tra Tối ưu hóa (Kiểm tra Hàng tuần)

- [ ] Theo dõi Pixel + CAPI tất cả sự kiện? EMQ ≥6?
- [ ] ≥50 conversions/tuần cho mỗi nhóm quảng cáo?
- [ ] 3-5 sáng tạo xoay vòng cho mỗi nhóm quảng cáo? Chu kỳ làm mới đúng lịch?
- [ ] Bật CBO cho các chiến dịch đa-nhóm quảng cáo?
- [ ] Mở rộng ngân sách ≤20% mỗi 3-4 ngày?
- [ ] Tần suất <3.0 (không mệt mỏi sáng tạo)?
- [ ] Kiểm tra A/B hook mới hàng tháng?
- [ ] Kiểm tra chéo ROAS với GA4/tăng thêm?

---

*Created: 2026-06-15-com + 9 nghiên cứu cộng với Reddit r/FacebookAds + X + Drum*
