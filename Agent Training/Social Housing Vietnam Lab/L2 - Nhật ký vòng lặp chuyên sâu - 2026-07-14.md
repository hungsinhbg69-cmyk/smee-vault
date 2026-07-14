---
title: L2 - Nhật ký vòng lặp chuyên sâu - 2026-07-14
date: 2026-07-14
updated: 2026-07-14T08:58:02+07:00
status: completed-not-passed
level: 2
pass_score: 97
legal_as_of: 2026-07-14
scope: national-with-local-variation
openclaw_independent_score: 62
hermes_independent_score: 55
tags:
  - agent-training
  - nha-o-xa-hoi
  - openclaw
  - hermes
  - strict-audit
---

# L2 — Nhật ký vòng lặp chuyên sâu ngày 2026-07-14

Liên quan: [[Nhà ở xã hội Việt Nam - Cầm tay chỉ việc]], [[L2 - Điều kiện hiện hành và 3 hồ sơ giả lập - 2026-07-14]], [[L2 - Retest độc lập D - 2026-07-14]], [[L2 - Final independent G - 2026-07-14]].

> [!danger] Kết luận vòng
> Chưa agent nào đạt ngưỡng độc lập 97/100. OpenClaw đạt 62/100 ở bài cuối; Hermes đạt 55/100 ở bài audit tinh cuối. Các artifact có hướng dẫn có thể đạt 98–100, nhưng không được dùng thay cho điểm năng lực độc lập.

## 1. Nguồn hiện hành được khóa

- [Luật Nhà ở 27/2023/QH15](https://vanban.chinhphu.vn/?classid=1&docid=209627&pageid=27160&typegroupid=3), Điều 76 và Điều 78.
- [24/VBHN-BXD ngày 18-05-2026](https://moc.gov.vn/vn/pages/ChiTietVanBan.aspx?TypeVB=2&vID=4943), Điều 29 và Điều 30; văn bản hợp nhất các sửa đổi hiện hành liên quan.
- [Hỏi đáp Bộ Xây dựng năm 2026](https://moc.gov.vn/vn/pages/ChiTietHoiDap.aspx?chID=10337): không có điều kiện cư trú cho mua/thuê mua; thông tin dự án phải kiểm tra tại nguồn địa phương/dự án.
- Local snapshot:
  - ![[Sources/Luat-Nha-o-27-2023-QH15-phan-1.pdf]]
  - ![[Sources/Luat-Nha-o-27-2023-QH15-phan-2.pdf]]
  - ![[Sources/24-VBHN-BXD-2026.pdf]]
  - ![[Sources/24-VBHN-BXD-2026-Phu-luc.pdf]]

## 2. Chuẩn chấm mới

- Qua vòng độc lập: 97–100.
- 93–96: sửa bắt buộc, chưa qua.
- Artifact có chỉ dẫn không được quy đổi thành điểm độc lập trên 96.
- Cap 69 nếu kết luận đủ/không đủ cuối cùng khi chứng cứ chưa đủ; áp điều kiện mua/thuê mua cho ca chỉ thuê; bịa hệ số/dự án/web; thêm điều kiện cư trú; hoặc đánh đồng đất với nhà.
- Tự ý ghi/sửa file khi đề cấm hoặc không xuất bài: 0.

## 3. OpenClaw

### Hạ tầng và model

- Gateway đầu vòng bị đóng bất thường; khởi động lại bằng `openclaw gateway start` và chứng minh đường agent trực tiếp bằng run `fe127b8c-6311-4fd0-96d9-9c46e5900c23` với marker `OPENCLAW_LEVEL2_READY`.
- Model mặc định vẫn là `local-qwen3.5-9b-q5km`, context 131072.
- Gemma `sonct988/gemma4-26b-a4b-it-q4km-256k:latest` ban đầu đăng ký context 32768, gây overflow vì prompt 13623 token lớn hơn ngân sách 12768 sau reserve.
- Đã dry-run, validate và nâng **riêng Gemma** lên `contextWindow=65536`, `num_ctx=65536`; không đổi model mặc định. Sau restart, run cuối có context thực 65536, prompt budget 45536, overflow 0.
- Trạng thái cuối: gateway reachable, Scheduled Task running, audit 0 critical; Telegram OK.

### Điểm và bằng chứng chạy thật

| Lượt | Model | Run/session | Điểm Thầy | Kết quả |
|---|---|---|---:|---|
| L2 đầu tiên | Qwen 9B | `cf8daaae-f7a7-4549-bdee-125c8e0231ad` | 0 | Tự gọi patch vào vault, patch thất bại, không xuất deliverable |
| Recovery A | Qwen 9B | `a897c7dd-7ae4-448e-8c49-f8fff3f1af63` | 68 | Lặp lỗi dẫn chiếu điểm a/b Điều 30 |
| Recovery A2 | Qwen 9B | `aebe8a03-17e7-4e1d-81e4-5eb0093f69e6` | 100 guided | Sửa đúng điểm a: hai nhánh độc thân; điểm b: đã kết hôn |
| Recovery B/B2 | Qwen 9B | `c1aa5f41-b0f6-49fe-88e3-3713cca3ad11`, `aee6c2e8-c8a6-4c80-890b-3cdd1599a903` | 94 → 100 guided | Sửa nhãn, cư trú, đất–nhà |
| Recovery C/C2 | Qwen 9B | `eb4826a5-846d-4701-af33-1cd9e83e4142`, `278c4ec6-e8f0-4edc-9bf5-fe6a1ba17575` | cap 69 → 98 guided | Sửa overclaim DN-B, queue và provenance |
| Retest D độc lập | Qwen 9B | `d3a571e5-4135-431f-ad29-87700564ba92` | 56 | Chỉ dùng `read` 2 lần, nhưng overclaim CT-E, sai đất–nhà, queue lạc/trùng |
| Guided correction D | Qwen 9B | `f95e821f-5ca7-4ed4-a822-eb1f806cc43d` | 91 guided | Sửa logic chính nhưng không tuân thủ đầu ra 8 dòng, còn câu “80 triệu không đáng kể” |
| Final G độc lập | Gemma 26B | `d0ed48f4-7738-4e42-a814-5c3e8d3af95e` | 62 | Chỉ dùng `read` 1 lần; vẫn ghi TH-K nhà ở/thu nhập là `CHƯA XÁC MINH` thay vì `KHÔNG ÁP DỤNG`, sai nhóm và queue |

### Lỗi chưa qua

1. Chưa khóa được nhánh **chỉ thuê**: phải ghi nhà ở/thu nhập `KHÔNG ÁP DỤNG`, không phải `CHƯA XÁC MINH`.
2. Hay mở rộng nhóm đối tượng từ lời khai cụ thể thành “nhóm 5/6/8”.
3. Biết số học nhưng thường không ghi quan hệ với ngưỡng cơ sở theo kiểu `nếu dữ kiện được xác nhận`.
4. Queue vẫn đưa hệ số địa phương vào hồ sơ chỉ thuê và bỏ sót dự án tương ứng.

## 4. Hermes

### Điểm và session

| Lượt | Model | Session | Điểm Thầy | Kết quả |
|---|---|---|---:|---|
| Audit D đầu | Qwen 9B | `20260714_083613_21892c` | 28 | Cho OpenClaw 97 sai; bịa “đã sửa”; sai số học và thang điểm |
| Audit D correction | Qwen 9B | `20260714_083936_6c96b8` | 41 | Bắt cap nhưng tiếp tục bịa quote, địa danh và mẫu số |
| Guided JSON repair | Qwen 9B | `20260714_084201_26ffe6` | 99 guided | JSON gần sạch sau khi khóa schema |
| Audit E độc lập | Qwen 9B | `20260714_084251_825050` | 12 | Đảo dấu `≤50` và `<15`, bỏ sót web/project/hệ số bịa |
| Audit E độc lập | Gemma 26B | `20260714_084406_b514e8` | 82 | Bắt phần lớn lỗi cốt lõi nhưng bỏ KH-I 36 > 35, sai rubric và thêm lời khen không có trong candidate |
| Guided correction E | Gemma 26B | `20260714_084622_12904f` | 99 guided | Sửa đúng bất đẳng thức, evidence và 6 mục rubric |
| Final audit F độc lập | Gemma 26B | `20260714_084742_954832` | 55 | Bỏ cap cho kết luận chắc chắn, bịa quote từ rubric, hiểu sai missing queue |

### Lỗi chưa qua

1. Audit-hallucination: trích câu không tồn tại hoặc khen một chi tiết candidate chưa hề nói.
2. Không giữ bất biến `cap = maximum`, đôi khi dùng cap như phép trừ tùy ý hoặc quên áp dụng.
3. Dễ đảo bất đẳng thức và đánh giá nhánh diện tích thấp nếu không có checklist số học riêng.
4. Hay đổi rubric 25+20+20+15+10+10 sang hạng mục tự tạo.
5. Không phân biệt “queue hiện có” với “mục còn thiếu trong queue”.

## 5. Sửa gói huấn luyện

- G6 đã được ghi chính xác: điểm a gồm cả hai nhánh độc thân; điểm b là đã kết hôn; điểm c là thời gian 12 tháng.
- Chuẩn hóa toàn bộ sang bốn nhãn: `ĐÃ XÁC MINH`, `CHƯA XÁC MINH`, `KHÔNG ÁP DỤNG`, `CHƯA ĐỦ HỒ SƠ`.
- Verification queue chỉ chứa việc chưa xác minh, xếp theo tác động; nguồn trung ương đã xác minh ghi riêng.

## 6. Quy tắc vận hành tạm thời

> [!warning] Không dùng độc lập cho quyết định pháp lý
> Cho đến khi vượt 97 ở bài biến thể mới, OpenClaw và Hermes chỉ được dùng để lập bảng sơ bộ. Mọi kết luận nhà ở xã hội phải qua checklist cố định và kiểm tra của Thầy.

- OpenClaw Qwen 9B: tác vụ ngắn, thu thập/định dạng có schema; không giao kết luận đa hồ sơ.
- OpenClaw Gemma 26B context 65536: dùng cho phân tích dài, nhưng vẫn bắt buộc kiểm tra nhánh thuê và queue.
- Hermes Qwen 9B: chỉ audit định dạng/marker đơn giản.
- Hermes Gemma 26B: audit pháp lý tốt hơn rõ rệt, nhưng chưa được tự chấm hoặc tự kết luận cuối.

