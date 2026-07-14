---
title: S2 - Local performance pack - Omnichannel
tags:
  - agent-training/local-pack
  - marketing
scenario: 2
fictional: true
status: active
---

# Local performance pack — Omnichannel

> [!info] Đã mở
> Tình huống 2 được mở sau khi S1 đạt release gate.

- Ngân sách 8 tuần: 420 triệu VND.
- Nguồn: Meta 7d-click/1d-view, TikTok 7d-click, Search data-driven, affiliate last-click, CRM coupon.
- 11% đơn OMS đã hủy/hoàn; dashboard kênh chưa trừ.
- 58% branded-search click xảy ra trong 48 giờ sau creator post.
- Một nhóm địa lý bị thiếu CRM match rate.
- Nhiệm vụ sau mở khóa: chuẩn hóa mẫu số, không cộng conversion chồng lấn, thiết kế geo/holdout test và ba phương án ngân sách.

## Dashboard exports — 8 tuần

| Kênh | Spend (VND) | Reported conversions | Reported revenue (VND) | Attribution | Ghi chú |
|---|---:|---:|---:|---|---|
| Meta | 126.000.000 | 1.120 | 406.000.000 | 7d click/1d view | Có modeled conversions |
| TikTok | 98.000.000 | 910 | 322.000.000 | 7d click | Có assisted creator traffic |
| Search | 84.000.000 | 860 | 301.000.000 | Data-driven | 58% branded clicks trong 48h sau creator post |
| Affiliate | 52.000.000 | 540 | 177.000.000 | Last-click code | Code có thể được share ngoài publisher |
| CRM coupon | 20.000.000 | 410 | 131.000.000 | Coupon redemption | Có thể overlap với mọi paid channel |
| Production/measurement | 40.000.000 | N/A | N/A | N/A | Không gán conversion trực tiếp |

## OMS reconciliation

- OMS có **2.940 unique placed orders** trong 8 tuần.
- **11%** unique placed orders bị hủy/hoàn; chưa có breakdown theo kênh.
- Net revenue sau voucher nhưng trước payment/fulfillment/tax: **873.000.000 VND**.
- Tổng reported conversions các nguồn không phải unique total và vượt OMS do overlap/window khác nhau.
- CRM match rate chung 76%; riêng một geo cell chỉ 43% nhưng chưa xác định nguyên nhân.

## Bài thi S2

1. Reconcile dashboard với OMS mà không ép phân bổ giả chính xác.
2. Tính reported CPA/ROAS từng nguồn và blended OMS placed/completed CPA theo hai mẫu số rõ ràng.
3. Lập overlap ledger và nêu điều gì không thể kết luận.
4. Tạo ba budget scenarios cho 420 triệu; production/measurement tối thiểu 40 triệu.
5. Thiết kế incrementality test có power inputs, contamination/brand-search caveat và stop rules.
