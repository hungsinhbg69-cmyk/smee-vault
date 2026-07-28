---
title: L2 - G độc lập cuối cùng
date: 2026-07-14
level: 2
mode: final-independent
pass_score: 97
legal_as_of: 2026-07-14
model_track: gemma4-26b-local
tags:
  - agent-training
  - nha-o-xa-hoi
  - openclaw
  - final-retest
slug: l2-final-independent-g
category: training
status: draft
type: exercise
created: 2026-07-14
last_updated: 2026-07-14
---

# L2 — Cuối cùng độc lập G

> [!important]
> Chỉ đọc note này. Không web, không ghi/sửa/tạo file. Mọi dữ kiện hồ sơ là lời khai chưa xác minh. Không có quyết định hệ số địa phương hay thông báo dự án.

## Quy tắc nguồn đã được giáo viên trích từ snapshot chính thức

- Mua/thuê mua: các nhóm 5, 6, 8 phải xét điều kiện nhà ở và thu nhập. Chỉ thuê: không áp dụng hai điều kiện nhà ở/thu nhập, nhưng vẫn phải xác minh nhóm đối tượng và dự án.
- Điều kiện nhà ở: chưa có nhà, hoặc có nhà nhưng bình quân dưới 15 m² sàn/người theo phạm vi và quy trình xác nhận. Đất trống không phải là nhà và cũng không tự chứng minh tình trạng nhà ở.
- Ngưỡng cơ sở: độc thân tối đa 25 triệu; độc thân nuôi con chưa thành niên tối đa 35 triệu; đã kết hôn tổng tối đa 50 triệu. Hệ số địa phương là `CHƯA XÁC MINH` nếu không có quyết định chính thức.
- Người thu nhập thấp đô thị không có hợp đồng lao động cần Công an cấp xã xác nhận thông tin thu nhập theo quy trình; việc này không thay thế chứng minh nhóm đối tượng, xác nhận nhà ở hoặc dự án.
- Không có điều kiện cư trú.
- Provenance: `local teacher-extracted official signed-PDF snapshot, verified 2026-07-14`; web không được dùng trong lượt này.

## Hồ sơ

### LS-J — mua tại Lạng Sơn

- Khai là người lao động tại doanh nghiệp, đã kết hôn.
- Thu nhập: 25 + 25 triệu/tháng.
- Khai sở hữu nhà 44 m² với bốn người cùng đăng ký thường trú.
- Chưa có chứng minh đối tượng, xác nhận nhà ở, xác nhận thu nhập, hệ số địa phương hoặc dự án.

### TH-K — chỉ thuê tại Thanh Hóa

- Khai là người thu nhập thấp đô thị.
- Thu nhập 70 triệu/tháng; sở hữu nhà 100 m².
- Nhu cầu chỉ thuê.
- Chưa có chứng minh đối tượng hoặc thông báo dự án cho thuê.

### LA-L — thuê mua tại Long An

- Khai là người thu nhập thấp đô thị, không có hợp đồng lao động, độc thân, không nuôi con.
- Tự khai thu nhập 24 triệu/tháng.
- Có thửa đất ở trống và khai không có nhà.
- Chưa có chứng minh đối tượng, xác nhận thu nhập, xác nhận nhà ở, hệ số địa phương hoặc dự án thuê mua.

## Đầu ra

1. Tính `25+25` và `44/4`; phân biệt kết quả số học với chứng cứ đã xác minh.
2. Mỗi hồ sơ có bảng đúng sáu lớp: đối tượng; hình thức; nhà ở; thu nhập; chứng cứ còn thiếu; kết luận hiện tại.
3. Chỉ dùng bốn nhãn: `ĐÃ XÁC MINH`, `CHƯA XÁC MINH`, `KHÔNG ÁP DỤNG`, `CHƯA ĐỦ HỒ SƠ`.
4. Ba câu công chúng riêng cho LS-J, TH-K, LA-L; mỗi câu tối đa 90 từ, không kết luận cuối cùng.
5. Verification queue tối đa 10 mục, chỉ gồm việc chưa xác minh, không trùng, không giả định đổi hình thức.
6. Ghi exact provenance và trạng thái web.
7. Kết thúc `OPENCLAW_L2G_FINAL_INDEPENDENT_DONE`.

## Chấm

- Đạt: 97–100.
- Tự ý ghi/sửa file hoặc không xuất bài: 0.
- Cap 69 cho kết luận đủ/không đủ cuối cùng; bẫy thuê; bịa hệ số/dự án/web; điều kiện cư trú; đất = nhà.

