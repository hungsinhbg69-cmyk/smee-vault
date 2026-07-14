---
title: Phú Thọ 33 NOXH - Nhật ký kiểm toán multi-agent
date: 2026-07-14
tags:
  - agent-training
  - noxh/phu-tho
  - legal-audit
  - hermes
  - openclaw
status: completed
final_score: 92
verdict: PASS_WITH_LIMITATIONS
---

# Phú Thọ 33 NOXH — Nhật ký kiểm toán multi-agent

> [!success] Kết quả cuối
> Registry parse thành công: **33 dòng**, gồm **24 hồ sơ/phần NOXH định danh được** và **9 vị trí chưa định danh có kiểm soát**. OpenClaw vòng cuối chấm **92/100**, không còn sửa đổi bắt buộc.

## Hồ sơ bàn giao

- [[Bao-cao-kiem-chung-33-du-an-NOXH-Phu-Tho-2026-07-14|Báo cáo Markdown]]
- ![[Bao-cao-kiem-chung-33-du-an-NOXH-Phu-Tho-2026-07-14.pdf]]
- `project_registry.json` — registry máy đọc được.
- `evidence_pack.md` — gói chứng cứ đã trích từ nguồn cho phép.
- `openclaw-audit-round2.json` — biên bản kiểm toán cuối.
- `hermes-final-exact.json` — bài sửa schema cuối của Hermes.

## Diễn biến huấn luyện

| Vòng | Agent | Kết quả | Điểm/Trạng thái | Lỗi chính | Can thiệp của Thầy |
|---|---|---|---|---|---|
| 1 | Hermes | Trích xuất pháp lý | 65/100 | JSON hỏng; email Famia biến dạng; thiếu CĐT Tiên Cát; dùng vốn Thụy Vân cũ; sai key | Tách lỗi dữ liệu, schema và ownership; đưa ví dụ đúng theo từng trường |
| 1 | OpenClaw | Audit Hermes + report | 45/100 sau hiệu chỉnh rubric | Phát hiện đúng lỗi Hermes nhưng gán nhầm sang báo cáo Leader; verdict FAIL mâu thuẫn điểm 95 | Buộc phân loại `hermes_raw` và `leader_report` trước khi chấm |
| 2A | Hermes | Phản biện OpenClaw | Chưa đạt | Nhận đúng ownership nhưng JSON vẫn hỏng (`err` không quote), sai “Thụy Vân”, lặp sửa đổi đã hoàn thành | Micro-repair chỉ tập trung schema và danh sách lỗi cố định |
| 2B | Hermes | Strict transcription | PASS | JSON parse nghiêm ngặt, đúng key, đúng 4 lỗi, không còn sửa đổi giả | Cung cấp schema exact và kiểm tra tự động bằng `json.loads` |
| 2 | OpenClaw | Final cross-audit trên session sạch | 92/100 | Không còn lỗi bắt buộc; tự sửa ownership vòng 1 | Chuyển sang session mới sau lỗi compaction và yêu cầu 5 spot-check cụ thể |

## Bốn lỗi Hermes đã sửa

1. Email Famia: từ chuỗi bị biến dạng về `Nguyenthanhtrung.thudo@gmail.com`; giữ nhãn free-mail, không gọi là email tên miền doanh nghiệp.
2. OXH3: loại key sai `invest_name`; xác nhận Công ty TNHH Xây dựng Tự Lập, QĐ 2100/QĐ-UBND.
3. Tiên Cát: bổ sung đúng Công ty Cổ phần Môi trường và Dịch vụ Đô thị Việt Trì; vốn cập nhật 452 tỷ đồng.
4. Thụy Vân: dùng QĐ 1745/QĐ-UBND và 3.006,612 tỷ đồng, không dùng số công bố ban đầu 3.881,060 tỷ đồng.

## Các bẫy dữ liệu đã khóa

- 33 là tổng số dự án NOXH trong thống kê 344 dự án nhà ở; 22 là snapshot dự án đang được triển khai.
- 369.996,8 tỷ đồng là tổng vốn của 344 dự án, không phải riêng 33 NOXH.
- 17.244 - 2.107 = 15.137; số 2.353 căn trong một bài Báo Phú Thọ được giữ là nghi vấn lỗi số liệu.
- Không gộp các dự án cùng tên chung “Thanh Miếu”.
- Không gộp hai quy mô Phú Hà 588 căn và 558 căn khi chưa có văn bản nối định danh.
- Flora Cera: “có sản phẩm quý III/2026” không đồng nghĩa hoàn thành; mốc mới hơn là tòa đầu tiên quý II/2027, toàn dự án năm 2028.

## Giới hạn được chấp nhận

> [!warning]
> Chưa tìm thấy phụ lục công khai từ bốn nhóm nguồn cho phép ánh xạ đủ 33 tên dự án. Vì vậy 9 vị trí được giữ `chưa định danh`, không bịa chủ đầu tư, quyết định hoặc liên hệ để lấp đủ số lượng.

## Sự cố vận hành

- Lần chạy OpenClaw vòng 2 trên session cũ lỗi `CLI transcript compaction failed: Already compacted`; chạy lại bằng session sạch đã thành công.
- Gateway OpenClaw hoạt động và agent turn chạy được; log đồng thời ghi Telegram token trả 401 dù bảng trạng thái từng hiển thị OK. Đây là lỗi kênh ngoài phạm vi dữ liệu dự án và chưa được sửa trong nhiệm vụ này.

## Quy tắc tái sử dụng

1. Luôn tách `raw agent output` khỏi `leader registry` trước khi chấm lỗi.
2. Mọi đầu ra JSON phải qua parser thật, không chấm bằng mắt.
3. Giá trị mới hơn không tự động xóa lịch sử; lưu cả số ban đầu và số cập nhật trong audit log.
4. Thiếu dữ liệu là một trạng thái hợp lệ; không được tối ưu “đủ 33” bằng suy đoán.
