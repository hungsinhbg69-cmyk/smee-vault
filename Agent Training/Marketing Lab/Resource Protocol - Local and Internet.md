---
title: Resource Protocol - Local and Internet
date: 2026-07-13
tags:
  - agent-training
  - evidence-discipline
  - marketing
status: active-reference
---

# Resource Protocol — Local và Internet

## Quy trình bắt buộc

1. Đọc local pack và ghi nguyên văn các trường cần tính trước khi mở web.
2. Gắn mỗi dữ kiện với `file + heading + row`; không dựa vào trí nhớ khi có thể đọc lại.
3. Audit định nghĩa, đơn vị, timeframe, tax/VAT, status đơn và attribution overlap.
4. Viết công thức bằng ký hiệu trước, thế số sau, tính lại bằng phép kiểm tra độc lập.
5. Chốt ngân sách web: số query, số URL, retry/URL và thời gian tối đa.
6. Ưu tiên URL chính thức; search chỉ để tìm URL, không dùng snippet làm bằng chứng cuối.
7. `SUCCESS` chỉ khi tool trả nội dung đúng trang và có đoạn/heading hỗ trợ claim.
8. Cùng lỗi hai lần hoặc 401/403/429 lặp lại: dừng URL, ghi `FAILED/UNVERIFIED`, chuyển fallback.
9. Không dùng nội dung từ trí nhớ để lấp một URL thất bại; có thể tách rõ `BACKGROUND KNOWLEDGE — UNVERIFIED` nhưng không dùng ra quyết định.
10. Trước bàn giao, audit ngược: từng con số/claim → bằng chứng; từng tool call → ngân sách; từng hành động → quyền hạn.

## Stop rules

- Không quá 12 web calls cho toàn bài; không quá hai call/URL.
- Không tạo biến thể tên tool để thử liên tục.
- Không ghi `SUCCESS` nếu output tool báo `failed`, rỗng hoặc sai trang.
- Luôn giao phần local đã hoàn thành ngay cả khi web thất bại.

## Gold calculations cho S1

Nguồn: [[S1 - Local brief - Sen May Sunscreen#Historical pilot — 14 ngày]].

| Kênh | CPC | CAC/completed order | Gross dashboard ROAS |
|---|---:|---:|---:|
| Meta | 24.000.000 / 9.600 = **2.500** | 24.000.000 / 141 = **170.213** | 58.900.000 / 24.000.000 = **2,454** |
| TikTok | 18.000.000 / 11.250 = **1.600** | 18.000.000 / 96 = **187.500** | 39.500.000 / 18.000.000 = **2,194** |
| Search | 12.000.000 / 3.000 = **4.000** | 12.000.000 / 103 = **116.505** | 42.100.000 / 12.000.000 = **3,508** |
| Creator codes | N/A | 15.000.000 / 88 = **170.455** | 36.200.000 / 15.000.000 = **2,413** |

- Unit contribution tạm thời trước fulfillment/payment/return/tax: `329.000 - 112.000 = 217.000 VND`.
- Không cộng platform purchases hoặc completed orders theo kênh để suy ra unique total vì creator có thể overlap và attribution windows khác nhau.
- TikTok **spend** 18 triệu đã gồm VAT. Local pack không nói gross revenue của bất kỳ kênh nào đã gồm VAT hay chưa.
- `Completed orders` là trường OMS sau 14 ngày; local pack không định nghĩa đầy đủ xử lý hoàn muộn.
- Gross revenue chưa trừ hủy/hoàn và có thể lệch `completed × list price` do bundle/voucher.

## Verified web snapshot — accessed 2026-07-13

> [!warning]
> Snapshot dùng để huấn luyện, không thay thế kiểm tra hiệu lực pháp lý hoặc đọc lại tài liệu nền tảng khi triển khai thật.

1. [Thông tư 06/2011/TT-BYT — quản lý mỹ phẩm](https://vanban.chinhphu.vn/default.aspx?docid=99376&pageid=27160)
   - Điều 21: nội dung quảng cáo phải phù hợp tài liệu chứng minh an toàn/hiệu quả và hướng dẫn công bố tính năng ASEAN.
   - Điều 22: nội dung gồm tên, tính năng/công dụng, tổ chức chịu trách nhiệm và lưu ý nếu có.
   - Trang cũng nêu rủi ro quảng cáo khiến mỹ phẩm bị hiểu là thuốc hoặc dùng danh nghĩa/hình ảnh tổ chức, cán bộ y tế.
2. [TikTok Attribution Metrics](https://ads.tiktok.com/help/article/attribution?lang=en)
   - Trang glossary, last updated February 2026; nêu Pixel cho website và MMP cho app; có assisted metrics với phạm vi/cửa sổ riêng.
3. [TikTok Attribution Analytics](https://ads.tiktok.com/help/article/about-attribution-analytics)
   - Last updated May 2025; có performance comparison, time to conversion, touchpoints và assisted conversions.
4. [Google Ads — About attribution models](https://support.google.com/google-ads/answer/6259715?hl=en)
   - First click, linear, time decay và position-based không còn được hỗ trợ; data-driven là mặc định cho phần lớn conversion actions, last click vẫn được hỗ trợ.

## Bài học từ lần thi đầu

- OpenClaw: 228 search calls/579 giây và không deliver; sau đó source log ghi success cho URL tool báo failed.
- Hermes: không xuất số đã kiểm, dùng claim web sai và tự chấm 100 khi không có evidence ledger.
- Cả hai phải coi trạng thái tool output là bằng chứng, không phải chi tiết trang trí.

