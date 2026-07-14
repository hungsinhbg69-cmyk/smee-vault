---
title: "Chốt giá & Ngân sách"
slug: "bidding-budget"
category: resource
tags: [facebook-ads, meta-ads]
status: "draft"
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

# 04 - Chốt giá & Ngân sách (Chính sách chi phí + Bidding)

## Các loại ngân sách

### Ngân sách hàng ngày
- Chi tiêu trung bình mỗi ngày (Facebook có thể dao động +/-15%)
- Phù hợp cho: phân phối đều đặn hàng ngày, chi tiêu dự đoán được
- Mức tối thiểu: phụ thuộc vào tiền tệ, thường là /ngày
- Sử dụng khi: bạn muốn kết quả ổn định hàng ngày

### Ngân sách trọn đời
- Tổng chi tiêu trong suốt thời gian chiến dịch
- Facebook phân bổ ngân sách theo ngày dựa trên cơ hội
- Phù hợp cho: các chiến dịch có thời hạn, sự kiện, khuyến mãi
- Sử dụng khi: chiến dịch có ngày bắt đầu/kết thúc cố định

**Khuyến nghị:** Đối với hầu hết các chiến dịch, ngân sách hàng ngày mang lại kết quả dự đoán được hơn. Ngân sách trọn đời hoạt động tốt cho các ưu đãi nhạy cảm về thời gian.

## Các chiến lược chốt giá (Bidding Strategies)

### 1. Chi phí thấp nhất (Mặc định)
- Facebook tự động tối ưu hóa để đạt chi phí thấp nhất trên mỗi kết quả
- Không có trần đặt giá - chi tiêu hết ngân sách để đạt số lượng kết quả lớn nhất
- Tốt nhất cho: tối đa hóa kết quả trong khuôn khổ ngân sách, chiến dịch mới
- Rủi ro: có thể chi quá mức cho các đối tượng đắt đỏ ban đầu
- **Sử dụng tùy chọn này làm mặc định** khi bắt đầu

### 2. Giới hạn chi phí (Cost Cap - Kiểm soát chi phí trung bình)
- Thiết lập mục tiêu chi phí trung bình trên mỗi kết quả
- Facebook cố gắng đạt được kết quả ĐÚNG hoặc DƯỚI mức giá mục tiêu
- Có thể chi ít hơn ngân sách đầy đủ nếu cơ hội bị giới hạn
- Tốt nhất cho: mở rộng quy mô chiến dịch với các mục tiêu CPA đã biết
- Rủi ro: có thể rời khỏi giai đoạn học tập nếu số lượng kết quả dưới ngưỡng trần quá thấp

**Cách thiết lập giá trần:** Bắt đầu bằng 1,5 đến 2 lần CPA mục tiêu của bạn, sau đó siết chặt khi thuật toán học được.

### 3. Giới hạn đặt giá (Bid Cap - Kiểm soát mức đặt giá tối đa)
- Thiết lập mức đặt giá cứng tối đa cho cuộc đấu thầu
- Facebook chỉ tham gia các cuộc đấu thầu mà bạn có thể thắng ở mức hoặc dưới mức đặt giá
- Mức kiểm soát cao nhất, ít linh hoạt nhất
- Tốt nhất cho: các cuộc đấu thầu cạnh tranh, đặt giá cụ thể theo vị trí hiển thị
- Rủi ro: có thể không chi hết ngân sách nếu mức đặt giá quá thấp

## Phân tích sâu về Tối ưu hóa Ngân sách Chiến dịch (CBO)

### Cách CBO hoạt động
1. Thiết lập MỘT ngân sách ở cấp chiến dịch
2. Tạo 2-6 bộ quảng cáo bên trong chiến dịch
3. Meta phân bổ ngân sách một cách động cho các bộ quảng cáo hiệu quả nhất
4. Thuật toán chuyển đổi ngân sách mỗi khoảng ~một giờ dựa trên hiệu suất thời gian thực
5. Các bộ quảng cáo tốt nhất sẽ nhận được nhiều ngân sách hơn tự động

### Yêu cầu của CBO
- Tối thiểu 2 bộ quảng cáo, tối đa 6 bộ quảng cáo mỗi chiến dịch
- Loại đối tượng tương tự (không trộn lẫn đối tượng rộng LAL với sở thích hẹp)
- Mỗi bộ quảng cáo cần mức ~/ngày tối thiểu để thu thập dữ liệu
- Cho phép 48 giờ để thuật toán ổn định việc phân bổ

### Khi nào sử dụng CBO so với ABO
| Kịch bản | Loại ngân sách | Lý do |
|---|---|---|
| Thử nghiệm các đối tượng mới | ABO (ngân sách bộ quảng cáo) | Chi tiêu bằng nhau cho mỗi lần thử |
| Mở rộng quy mô những người chiến thắng | CBO (ngân sách chiến dịch) | Thuật toán tìm ra kết quả rẻ nhất |
| Chiến dịch đã thiết lập, 3+ bộ quảng cáo | CBO | Phân phối đã được chứng minh hoạt động tốt |
| Một bộ quảng cáo duy nhất | Cả hai | Không có sự khác biệt với một bộ quảng cáo |
| Ngân sách hạn chế (</ngày tổng cộng) | ABO | Đảm bảo mỗi lần thử đều nhận được chi tiêu |
| Ngân sách lớn (+/ngày) | CBO | Thuật toán phân bổ hiệu quả |

### Các thực hành tốt nhất cho CBO
1. Không trộn lẫn các đối tượng quá khác nhau trong cùng một chiến dịch CBO
2. Sử dụng quy mô đối tượng tương tự để so sánh công bằng
3. Thiết lập mức chi tiêu tối thiểu của bộ quảng cáo nếu cần (thông qua giá trần trên mỗi bộ quảng cáo)
4. Cho phép giai đoạn học tập trước khi thực hiện thay đổi (48+ giờ)
5. Ngân sách nên ít nhất gấp 10 lần CPA mục tiêu tối thiểu của bạn

## Giai đoạn Học tập (Learning Phase)

### Những gì kích hoạt giai đoạn học tập
- Chiến dịch/bộ quảng cáo mới được tạo ra
- Chỉnh sửa quan trọng (>25% thay đổi ngân sách, thay đổi sáng tạo, thay đổi nhắm mục tiêu)
- Quảng cáo bị tạm dừng và tái kích hoạt
- Vấn đề phân phối được giải quyết

### Yêu cầu của giai đoạn học tập
- **50 sự kiện tối ưu hóa mỗi tuần cho mỗi bộ quảng cáo** - đây là con số ma thuật
- Sự kiện tối ưu hóa = sự kiện chuyển đổi bạn đang tối ưu hóa (mua hàng, lead, v.v.)
- Nếu có ít hơn 50 sự kiện/tuần, sẽ ở trong giai đoạn học tập vô hạn

### Trong giai đoạn học tập
- Hiệu suất KHÔNG ỔN ĐỊNH và không thể dự đoán
- Chi phí có thể cao hơn bình thường
- Không thực hiện chỉnh sửa lớn trong kỳ này
- Cho phép tối thiểu 48 giờ trước khi đánh giá hiệu suất
- **KHÔNG hoảng loạn và dừng sớm** - đây là nơi hầu hết các nhà quảng cáo mất tiền

### Thoát khỏi giai đoạn học tập
1. Tự nhiên: tích lũy 50+ sự kiện/tuần theo thời gian
2. Tăng tốc: tăng ngân sách (nhưng tối đa 20% mỗi 3-4 ngày)
3. Giảm số lượng bộ quảng cáo: hợp nhất ngân sách vào ít bộ quảng cáo hơn để có nhiều dữ liệu hơn cho mỗi bộ quảng cáo
4. Mở rộng nhắm mục tiêu: càng nhiều người thì càng nhiều cơ hội chuyển đổi

### Chỉ báo giai đoạn học tập trong Ads Manager
- "Learning Limited" = không đủ sự kiện để thoát khỏi giai đoạn học tập
- "Active" + không có huy hiệu học tập = đã thành công thoát khỏi giai đoạn học tập
- Kiểm tra hàng tuần: bao nhiêu sự kiện tối ưu hóa cho mỗi bộ quảng cáo?

## Khuyến nghị ngân sách theo loại chiến dịch

### Thương mại điện tử (Mục tiêu Bán hàng)
- Ngân sách khởi động: -50/ngày mỗi bộ quảng cáo tối thiểu
- CBO được khuyến nghị sau khi xác định những người chiến thắng đã được chứng minh
- Mở rộng 20% mỗi 3-4 ngày khi có lợi nhuận
- Ngân sách hàng tháng nên cho phép tăng vào quý IV (2-3 lần)

### Tạo Lead
- Ngân sách: -30/ngày mỗi bộ quảng cáo
- CPL thay đổi theo ngành (-)
- Thử nghiệm chất lượng lead so với số lượng ở các ngân sách khác nhau
- Theo dõi phản hồi lại lead trong vòng 1 giờ

### Nhận thức về Thương hiệu
- Ngân sách: -25/ngày là đủ (tối ưu hóa cho phạm vi hiển thị/lượt in ấn)
- CPA thấp hơn các chiến dịch chuyển đổi
- Đo lường thông qua nghiên cứu nâng cao khả năng ghi nhớ quảng cáo

## Các mốc chi phí (Thị trường Mỹ, 2026)
- **CPM:** - (thay đổi theo ngành, mùa, đối tượng)
- **CPC:** .50-.00
- **CPL:** - (phụ thuộc nặng vào ngành nghề)
- **Phí quý IV:** Chi phí từ tháng 10 đến tháng 12 cao hơn 2-3 lần
- **Retargeting so với Prospecting:** Retargeting luôn rẻ hơn trên mỗi kết quả

## Quy tắc mở rộng ngân sách
1. **Tăng tối đa 20% mỗi 3-4 ngày** - nhiều hơn = đặt lại giai đoạn học tập
2. **Chiến lược sao chép:** Sao chép bộ quảng cáo thắng cuộc sang chiến dịch mới với ngân sách cao hơn (bảo toàn việc học ban đầu)
3. **Mở rộng ngang:** Mở rộng sang các đối tượng tương tự/LAL lớn hơn
4. **Mở rộng dọc:** Tăng ngân sách trên các bộ quảng cáo đã được chứng minh một cách dần dần
5. **Giám sát CPA sau khi mở rộng:** Nếu CPA tăng >20%, làm chậm tốc độ mở rộng

## Những điểm chính cần nhớ
- Chốt giá Chi phí thấp nhất = lựa chọn mặc định, sử dụng Giới hạn chi phí (Cost Cap) khi bạn biết CPA mục tiêu
- CBO để mở rộng quy mô, ABO để thử nghiệm các đối tượng mới
- Cần 50 sự kiện tối ưu hóa/tuần/bộ quảng cáo để thoát khỏi giai đoạn học tập
- Tăng ngân sách tối đa 20% mỗi 3-4 ngày để tránh đặt lại việc học
- Chi phí quý IV cao hơn 2-3 lần - lên kế hoạch ngân sách tương ứng
- Trạng thái "Learning Limited" = không đủ dữ liệu, hãy hợp nhất hoặc mở rộng nhắm mục tiêu

---
*Tạo: 2026-06-15 | Nguồn gốc: marketingadvice.ai, marketingagency.one*