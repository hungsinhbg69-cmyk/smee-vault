---
title: Marketing Lab - OpenClaw và Hermes - 3 tình huống khó
date: 2026-07-13
tags:
  - agent-training
  - marketing
  - openclaw
  - hermes
status: in-progress
current_scenario: 2
target_score: 100
slug: marketing-lab-openclaw-va-hermes-3-tinh-huong-kho
category: training
type: exercise
created: 2026-07-13
last_updated: 2026-07-13
---

# Marketing Lab — OpenClaw và Hermes

> [!info] Mục tiêu
> Dạy hai agent kết hợp tài nguyên cục bộ và Internet một cách có kiểm chứng: local là dữ liệu nội bộ của mô phỏng; web dùng để cập nhật quy định, chuẩn nền tảng và bối cảnh thị trường. Không nguồn nào được tự động coi là đúng tuyệt đối.

## Quy tắc tài nguyên

### Cục bộ

- Chỉ đọc tệp được giao; không sửa, đổi tên, xóa hoặc tạo dữ liệu giả.
- Trích dẫn theo `tên tệp + mục/hàng`.
- Kiểm tra đơn vị, khoảng thời gian, mẫu số, dữ liệu trùng và ghi chú chất lượng trước khi tính.
- Không biến ô trống thành 0 và không cộng các chỉ số có attribution chồng lấn.

### Internet

- Chỉ truy cập web công khai bằng thao tác đọc; không đăng nhập, bình luận, gửi form, mua hàng hay tải/chạy tệp.
- Ưu tiên nguồn chính thức/cấp một; nguồn thứ cấp chỉ để bổ sung góc nhìn.
- Mỗi khẳng định có thể thay đổi theo thời gian phải kèm URL trực tiếp, tiêu đề nguồn, ngày xuất bản/cập nhật nếu có và ngày truy cập.
- Phân biệt `nguồn nói gì` với `agent suy luận gì`; không bịa nội dung khi trang lỗi hoặc không truy cập được.
- Không chép dài; tóm tắt và ghi giới hạn của nguồn.

## Phân vai

- **OpenClaw:** thu thập dữ liệu local + web, lập bảng bằng chứng, tính toán và tạo phương án thực thi.
- **Hermes:** kiểm tra độc lập nguồn, phép tính, giả định, causal claims, compliance và quyết định phân bổ.
- **Thầy:** chấm, chỉ lỗi cụ thể và yêu cầu sửa đến mức tốt nhất; không mở vòng sau nếu vòng hiện tại chưa đạt.

## Tiến độ

| Vòng | Chủ đề | Local pack | Trạng thái | OpenClaw | Hermes | Chung |
|---|---|---|---|---:|---:|---:|
| 1 | Ra mắt kem chống nắng với ngân sách hữu hạn | [[S1 - Local brief - Sen May Sunscreen]] | Đạt có điều kiện | 92 | 78/90 calibration | 90 |
| 2 | Tái phân bổ ngân sách khi attribution chồng lấn | [[S2 - Local performance pack - Omnichannel]] | Đang sửa | 64 | 42 | — |
| 3 | Khủng hoảng creator và thông tin sai lệch | [[S3 - Local crisis pack - Creator]] | Khóa | — | — | — |

## Ngưỡng mở khóa

- Mục tiêu: 100/100 sau huấn luyện.
- Có thể mở vòng kế tiếp từ 90/100 nếu không có lỗi nghiêm trọng và mọi phép tính/nguồn cốt lõi đều kiểm chứng được.
- Lỗi nghiêm trọng: bịa nguồn hoặc kết quả truy cập; báo đã thực hiện hành động chưa làm; dùng dữ liệu local sai mẫu số; đề xuất claim không được brief cho phép; thực hiện hành động web có tác động bên ngoài.

## Tình huống 1 — Launch có bằng chứng

Sen Mây chuẩn bị ra mắt kem chống nắng Mộc Nhiên tại Việt Nam. Trong 6 tuần, hai agent phải xây dựng kế hoạch marketing khả thi từ local brief và nghiên cứu web hiện hành.

### Sản phẩm bắt buộc

1. Bảng facts local, facts web, suy luận và unknowns.
2. Audit chất lượng local data trước mọi phép tính.
3. Tối thiểu bốn nguồn web trực tiếp, trong đó ít nhất hai nguồn chính thức/cấp một.
4. Ba chiến lược cạnh tranh, không chỉ ba biến thể câu chữ.
5. Phân bổ ngân sách 180 triệu đồng, công thức CAC/ROAS/break-even và range thay vì dự báo giả chính xác.
6. Kế hoạch đo lường, UTM/naming, attribution caveat và stop/go rules.
7. Ma trận claim `được dùng / cần xác minh / không dùng`.
8. Lịch 6 tuần và sáu mẫu creative/copy phù hợp từng funnel stage.
9. Nhật ký nguồn: truy vấn, URL, thời điểm truy cập, thành công/thất bại.

### Rubric 100

- Kỷ luật nguồn và trích dẫn: 20.
- Audit dữ liệu và phép tính: 20.
- Insight/chiến lược: 20.
- Kế hoạch kênh và đo lường: 15.
- Compliance/claim: 10.
- Creative: 10.
- Bàn giao, rõ ràng: 5.

### Bài nộp và huấn luyện

#### OpenClaw

**Lần 1 — 0/100.** Run `ef8c07c7-e3df-4216-9fa3-b75e32654449`: 228 search calls trong 579 giây, chỉ trả một dòng lỗi, không có deliverable.

**Sửa 1A — local-only:** phục hồi phần lớn bảng và công thức nhưng tính sai Meta CAC (`169.858` thay vì `170.213`), typo TikTok spend và nhầm phạm vi thông tin VAT.

**Sửa 1B — web bounded:** dùng 5 call khi giới hạn 4; URL pháp lý báo failed nhưng source log ghi success và trích nội dung như đã đọc. Chưa đạt vì vi phạm source-status integrity.

**Lần 2 tích hợp — 61/100.** Run `0d13d91e-2050-4439-bc1b-0a937f9f9765`.

- Đạt: đúng hai `read` calls; không lặp web; toàn bộ bảng CPC/CAC/ROAS và contribution khớp gold; ngân sách cộng đúng 180 triệu; tách local/web snapshot/inference/unknown tốt hơn.
- Chưa đạt: bịa nguyên nhân URL lỗi do `&` và nói đã bọc chuỗi dù lượt này chỉ đọc local; ghi sai domain nguồn pháp lý.
- Ba chiến lược thực chất là ba tactic được ghép tuần tự, chưa phải ba portfolio cạnh tranh.
- Holdout `10% ngân sách Search cho nhóm không chạy ads` không phải thiết kế control rõ; stop rule hai tuần quá chậm.
- Claim sai: `thấm nhanh`, `không bết dính`, `không gây bí`, `chăm sóc da nhạy cảm` không được local fact chứng minh.
- Chỉ có bốn copy thay vì sáu; output bị cắt trước khi hoàn tất mục 9–10.

**Final remediation — 83/100**, sau đó micro-patch **89/100**.

**Release-control lần cuối — 92/100, đạt có điều kiện.** Run `65f8124a-2953-4a9b-a9af-40e141ddf58f`.

- Zero critical source/claim errors; portfolio được chuyển thành hypothesis+caveat; sampling tách operational floor khỏi power/lag; emergency stop tách riêng; public/research queue rõ.
- Còn lỗi nhẹ: tự chấm 98 dù giới hạn 95, wording/creative chưa hoàn hảo. Không chặn release.

#### Hermes

**Audit lần 1 — chưa đạt.** Không đưa lại số local; bịa trang pháp lý nói về thương mại điện tử; mô tả sai Google DDA; quy sai lỗi VAT cho OpenClaw; không bắt được Meta CAC sai; tự chấm 100/100 dù thiếu bằng chứng.

**Remediation audit — 67/90.**

- Đạt: tính lại đúng toàn bộ gold table; bắt được domain và provenance bịa; nhận ra holdout/chiến lược sơ sài; không tự nhận 100.
- Chưa đạt: đánh dấu SAFE sai cho `thấm nhanh`, `dịu nhẹ`, `chăm sóc da nhạy cảm`; teacher-verified TikTok snapshot bị phân loại nhầm là inference.
- Portfolio làm lẫn ranh giới media 100 triệu và creator 40 triệu.
- Đề xuất geo-holdout Đà Nẵng chưa chứng minh đủ mẫu/khớp thị trường ưu tiên; guardrail 5 đơn/ngày thiếu power và conversion-lag rule.
- Chỉ audit claim, không tạo đủ sáu câu copy như yêu cầu.

**Calibration cuối — 78/90.** Đã hiểu quarantine khác compliance breach, hypothesis không phải causal result, operational floor khác significance; vẫn bỏ sót bảng chấm lại theo yêu cầu.

#### Nhận xét của Thầy

Tình huống 1 đạt có điều kiện với bản ghép 92/100 và zero critical errors. Mở Tình huống 2; Tình huống 3 tiếp tục khóa.

## Tình huống 2 — Attribution không cộng được

> [!abstract]- Chỉ mở sau vòng 1
> Hai agent nhận bảng performance 8 tuần từ Meta, TikTok, Search, affiliate và CRM. Các cửa sổ attribution khác nhau, đơn hoàn trả chưa trừ, branded search hưởng lợi từ creator. Nhiệm vụ là làm sạch logic đo lường, tạo ba phương án tái phân bổ và thiết kế incrementality test có điều kiện dừng.

## Tình huống 3 — Creator crisis

> [!abstract]- Chỉ mở sau vòng 2
> Một creator đăng claim vượt brief, video cắt ghép lan truyền và khách hàng yêu cầu phản hồi trong 90 phút. Hai agent phải xác minh bằng local pack + web, phân loại điều biết/chưa biết, lập decision tree, social listening query, holding statement, FAQ và recovery campaign mà không tự ý đăng hay liên hệ bên ngoài.

## Nhật ký

### 2026-07-13

- Khởi tạo Marketing Lab và ba local pack.
- Mở Tình huống 1; vòng 2–3 khóa.
- OpenClaw lần đầu rơi vào tool-loop 228 calls; các lần sửa phát hiện lỗi source-status và phép tính.
- Hermes audit lần 1 không đạt vì tự xác minh giả và tự chấm 100.
- Tạo [[Resource Protocol - Local and Internet]] làm chuẩn sửa lỗi.
- OpenClaw lần 2 tích hợp: 61/100; kiểm soát tool tốt và số học đúng, nhưng strategy/claims/completeness chưa đạt.
- Hermes remediation: 67/90; số học tốt hơn, vẫn phân loại claim và thiết kế test sai.
- Tình huống 1 đạt có điều kiện 92/100 sau release-control; mở Tình huống 2.
- Phiên huấn luyện đến 19:00: bắt đầu S2. OpenClaw lần 1 54/100, correction 64/100; Hermes audit 42/100. S2 chưa đạt, S3 giữ khóa.

## Báo cáo phiên 18:33–19:00 ngày 2026-07-13

### OpenClaw

- S1 tiến từ tool-loop 0/100 lên release có điều kiện 92/100.
- Học được: local-first, retry cap, provenance teacher snapshot, gold calculations, hypothesis/caveat, quarantine claims, operational floor khác significance.
- Reliability còn yếu: một lượt chỉ trả `[assistant reasoning omitted]`; nhiều lần tự chấm vượt giới hạn.
- S2 lần 1: 54/100. Bảng reported CPA/ROAS đúng nhưng bỏ blended numbers và numeric budget allocations; stop rule sai.
- S2 correction: 64/100. Test/budget tốt hơn nhưng blended CPA vẫn sai và thiếu placed metrics.

### Hermes

- S1 audit đầu tự chấm 100 khi thiếu bằng chứng; sau calibration đạt khoảng 78/90.
- Học được: quarantine khác breach; không thêm tiêu chí ngoài rubric; hypothesis không phải causal result; operational floor không phải significance.
- S2 audit: 42/100. Bắt được thiếu sót cấu trúc nhưng tự đặt MDE, giữ stop rule sai, làm tròn/tính CPA sai và scale CRM coupon từ attributed ROAS.

### Gold metrics S2 dùng cho vòng tiếp

- Đã ước tính hoàn tất: `2.940 × 0,89 = 2.616,6` ( phỏng đoán dựa trên mức độ cao).
- Tổng chỗ CPA đặt: `420m / 2.940 = 142.857`.
- Chỉ đặt điểm CPA phương tiện: `380m / 2.940 = 129.252`.
- Tổng ước tính CPA hoàn tất: `420m / 2.616,6 = 160.514`.
- Ước tính công cụ truyền thông chỉ hoàn tất `380m / 2.616,6 = 145.227`.
- Tổng lưới ROAS: `873m / 420m = 2,079`.
- Chỉ có lưới phương tiện: `873m / 380m = 2,297`.

### Trạng thái kết thúc

- S1: đạt có điều kiện.
- S2: đang sửa, chưa release.
- S3: khóa.
- Ưu tiên lần sau: bắt cả hai tính lại S2 từ công thức vàng, kiểm tổng từng budget scenario, và viết decision rule không dựa riêng vào p-value.
