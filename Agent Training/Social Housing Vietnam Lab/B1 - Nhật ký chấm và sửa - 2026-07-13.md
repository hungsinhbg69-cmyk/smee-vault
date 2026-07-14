---
title: B1 - Nhật ký chấm và sửa - 2026-07-13
date: 2026-07-13
updated: 2026-07-13T19:22:30+07:00
tags:
  - agent-training
  - social-housing
  - grading
  - openclaw
  - hermes
status: in-progress
scenario: 1
step: 1
---

# B1 — Nhật ký chấm và sửa

Nguồn bài: [[Nguồn chính thức và bài tập B1 - 2026-07-13]]. Lab chính: [[Nhà ở xã hội Việt Nam - Cầm tay chỉ việc]].

## Mục tiêu kiểm tra

- Dựng đủ chuỗi 12 nguồn L1–Q4.
- Nhận ra Nghị định 100/2024 không được đọc tách khỏi 261/2025, 54/2026 và 136/2026.
- Giữ phạm vi toàn quốc ở 34 tỉnh/thành hiện hành.
- Phân biệt snapshot Internet do Thầy xác minh với việc agent tự truy cập web.
- Không kết luận cá nhân chắc chắn đủ điều kiện.

## OpenClaw

### Lần 1 — 82/100

- Run: `b34f64f2-a0e2-40d8-8148-3703ad9e8f85`.
- Thời gian: khoảng 118 giây; hoàn thành, không tool-loop.
- Đạt: đủ 12 ID; đúng chuỗi D1–D4; provenance đúng; không nói đã mở web; có Q4 và con số 34; không kết luận đủ điều kiện.
- Lỗi: `phát triển/quản chế NSXH`; `cụm thể`; `D chế`; bốn mục sàng lọc chỉ lặp việc kiểm tra văn bản, thiếu sự kiện/tài liệu của người hỏi, nguồn dự án/địa phương và xác nhận thẩm quyền.

### Bản sửa có chỉ dẫn — 96/100

- Run: `b5db1945-300d-416a-81e0-639fb21a6473`.
- Thời gian: khoảng 86 giây.
- Đã sửa đúng toàn bộ lỗi logic và nộp changelog 7 dòng.
- Tạo hai lỗi trình bày mới: `Hiệu lập` và `2    026–2030`.

### Micro-patch — bản cuối 100/100

- Run: `44aec508-9d3c-4907-9a30-bf12ac3f040d`.
- Thời gian: khoảng 57 giây.
- Sửa đúng, chỉ sửa hai vị trí được giao: `Hiệu lực 01-08-2024` và `2026–2030`.
- **Điểm 100 là chất lượng artifact sau coaching**, không phải điểm năng lực làm độc lập ở lượt đầu.

## Hermes

### Audit lần 1 — 38/100, không đạt

- Thời gian: khoảng 84 giây.
- Đủ hình thức 12 ID và provenance, nhưng kết luận `PASS B1` sai.
- Tự gõ sai `43/2024/QH15` thành `QH1SS`.
- Bịa nhận xét D2 “sửa chính nó”, trong khi snapshot nói Nghị định 261/2025 sửa Nghị định 100/2024 và Nghị định 192/2025.
- Đánh `NEEDS-CHECK` cho Q4 dù con số 34 có trực tiếp trong snapshot.
- Bỏ sót `quản chế`, `cụm thể`, `D chế`.
- Cho qua bốn mục sàng lọc dù thiếu dữ kiện người hỏi, nguồn địa phương và xác nhận thẩm quyền.

### Remediation lần 1 — 0/100 độ hoàn chỉnh

- Chỉ trả chuỗi `<|tool>`; không có deliverable.
- Log không cho thấy lỗi inference rõ ràng tại thời điểm kiểm tra; coi đây là lỗi độ tin cậy đầu ra.

### Remediation safe mode — 90/100 có hướng dẫn

- Nhận đủ bảy lỗi Thầy chỉ ra.
- Chuyển kết luận thành `NEEDS-REVISION`, sửa trạng thái Q4 và bỏ nhận xét sai về D2.
- Đây là bản sửa theo đáp án lỗi đã được cung cấp; chưa chứng minh audit độc lập.

### Independent retest — 92/100 tự làm; bản cuối 100/100 có hướng dẫn

- Bài biến thể: [[B1 - Hermes independent retest variant]].
- Hermes bắt đủ 6/6 lỗi cố ý: L2 sai hiệu lực; D1 dùng độc lập; D4 sai năm; Q3 sai phạm vi; Q4 dùng 63 thay vì 34; provenance giả.
- Không đánh nhầm sáu dòng fact đúng.
- Tuy nhiên tạo ba lỗi trong báo cáo: dẫn hiệu lực L2 thành “theo nguồn D1”; viết hỏng `D4` thành `D truyền thừa`; đổi Q2 từ Nghị quyết thành Nghị định.
- Micro-patch đã sửa đúng ba vị trí và không thay nội dung khác.
- Kết luận của Thầy: khả năng phát hiện lỗi đạt; độ chính xác biên tập còn cần guardrail. Artifact cuối đạt 100/100 sau coaching.

## Gold correction cho bốn bước sàng lọc

1. Thu thập sự kiện và tài liệu của người hỏi cần đối chiếu.
2. Xác minh chuỗi quy định hiện hành và điều khoản đã được sửa đổi.
3. Kiểm tra thông báo chính thức của dự án/cơ quan địa phương tại đúng tỉnh/thành và thời điểm.
4. Ghi rõ phần còn thiếu cần cơ quan có thẩm quyền xác nhận; không hứa người hỏi đủ điều kiện.

## Quyết định của Thầy

> [!success] Mở Bước 2 có điều kiện
> Cả hai đạt Bước 1 sau coaching. Được phép đọc bản ký chính thức và xử lý ca giả lập; mọi kết luận cá nhân vẫn phải dừng ở `cần xác nhận`, và Tình huống 2–3 tiếp tục khóa.

## Bài kiểm tra kế tiếp

- Bước 2 dùng bản ký chính thức để lập `điều kiện quốc gia / biến thể địa phương / tài liệu cần xác nhận`.
- Tạo ba hồ sơ công dân giả lập ở ba tỉnh/thành khác nhau; agent chỉ được phân luồng bằng chứng, không xác nhận chắc chắn đủ điều kiện.
- Bắt buộc kiểm tra thông báo dự án/địa phương theo đúng ngày trước khi viết nội dung truyền thông.
