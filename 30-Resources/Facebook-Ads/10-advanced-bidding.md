---
title: "Advanced Bidding"
slug: "advanced-bidding"
category: resource
tags: [facebook-ads, meta-ads]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

# 10 - Advanced Bidding Strategies (Chi tiết bid strategies)

## 5 Bid Strategies (2026)

| Strategy | Control Model | Khi nào dùng |
|----------|---------------|--------------|
| **Lowest Cost** | No constraint; Meta spends budget for max results | Default cho 80% campaigns <€50k/month |
| **Cost Cap** | Target average CPA; can bid above on individual auctions | Khi có ≥50 conversions/week/ad-set + ≥€5k weekly spend/ad-set |
| **Bid Cap** | Hard per-auction ceiling | Narrow: auction-level data known, massive catalogues with precise margin/SKU |
| **Value Optimization** | Optimize for purchase value (not volume) | DTC với wide AOV range |
| **ROAS Goal** | Minimum ROAS threshold | E-commerce với tracked revenue; set at 80% trailing 28-day ROAS |

## Cost Cap — 3 Điều Kiện Sống Còn

1. **≥50 conversions/week/ad-set** — Meta cần statistical signal để estimate CPA
2. **≥€5,000 weekly spend/ad-set** — daily budget đủ auction participation để average high-cost + low-cost conversions
3. **Cap ≥ trailing 7-day average CPA** — cap đặt ở target là đặt below realistic average → delivery collapse

> ⚠️ Cost Cap quá thấp: ad-set với €12 Cost Cap trong market CPAs €16 sẽ exhaust daily budget exploration window, fail tìm compliant inventory, near-zero impressions.
>
> Bid Cap break nhiều campaign hơn fix: chỉ 20-25% tests giảm CPA, còn lại tăng hoặc collapse delivery.

## Value Optimization (VO)

### Khi nào dùng
- DTC với wide AOV range (từ $20 đến $500+)
- Cần tối ưu purchase VALUE, không phải volume
- Product catalog có margin differential đáng kể giữa các items

### Cách hoạt động
- Model predict purchase value, không chỉ probability
- Ưu tiên users có khả năng chi tiêu cao hơn
- Tự động allocate budget cho high-value conversions

### Setup VO
1. Set objective = Sales (Conversions)
2. Trong ad set: optimization_guide = VALUE
3. Ensure Purchase event has `value` parameter với chính xác revenue
4. Cần ≥50 purchases/week để model có signal đủ

## ROAS Goal

### Khi nào dùng
- E-commerce với tracked revenue (CAPI + Pixel)
- Đã có historical ROAS data ổn định
- Muốn control minimum return

### Setting ROAS Goal
1. Set objective = Sales (Conversions)
2. Trong ad set: optimization_guide = ROAS GOAL
3. Set roas_goal_value = 80% trailing 28-day average ROAS
4. Không đặt quá thấp → Meta sẽ không deliver đủ volume

> ⚠️ ROAS Goal yêu cầu clean revenue tracking. Duplicated events hoặc missing values → ROAS math sai → delivery suboptimal.

## CBO — 3 Sai Lầm Phổ Biến

### 1. Minimum spend limits không bảo vệ small ad-sets
Algorithm park 3/4 ad-sets ở floor, funnel 75% cho "winner" — thường là broad audience có historical signal cao nhất, chưa chắc là ICP segment.

**Fix:** Set minimum daily budget per ad-set bằng nhau khi testing.

### 2. Campaign budget ≠ daily spend cap
Với lifetime budget, Meta compress/expand daily delivery theo auction opportunity. Monday có thể spend 2x daily average, Thursday chỉ 0.4x.

**Fix:** Monitor pacing hourly trong 3 ngày đầu. Adjust nếu cần.

### 3. Audience overlap giết efficiency
Ad-sets cùng Advantage Campaign Budget mà share audience overlap → algorithm không arbitrage được, cứ serve same people từ 2 pools.

**Fix:** Check audience overlap trước enable CBO. Exclude overlapping segments.

## Scaling Rules

### Vertical Scaling (increase budget)
- Tăng budget ≤20% mỗi lần, ≥48h giữa các lần tăng
- Monitor CPA closely sau mỗi increase
- Nếu CPA tăng >20% → pause và hold 3-4 ngày trước khi thử lại

### Horizontal Scaling (mới ad-sets)
- Duplicate winning campaign với higher budget
- Test new audience segments (LL 3-5%)
- Expand geography (new cities/provinces)
- Thêm placement types nếu currently limited

> 💡 Horizontal scaling > vertical scaling: preserves original learning phase data while expanding reach.

## Budget Pacing Phases

### Three Phase Model

| Phase | Days | Velocity | Purpose |
|-------|------|----------|---------|
| **Exploration** | 1-7 | Cap at 60-70% optimal daily budget | Buy algorithm time to map conversion landscape |
| **Momentum** | 8-21 | Progressive increase ≤15% every 48h | Exploit accumulated intelligence + incremental learning |
| **Saturation** | 22+ | Slow down or refresh creative | Frequency crosses 2.5-3.0 → audience saturation |

### Key Pacing Metrics

1. **Budget Deployment Velocity (BDV)**: Actual daily spend ÷ Target daily spend, hourly. BDV 1.2 by noon = pacing 20% fast
2. **Learning Stability Index**: Coefficient of variation in CPA over rolling 7-day windows — rising = algorithm struggling at higher velocity
3. **Temporal Conversion Density**: Which hours produce highest conversion rates → dayparting opportunity
4. **Creative Fatigue Acceleration Rate**: Frequency increase per day while maintaining/increasing budget — >0.3/day = danger zone

> 💡 Slower, controlled pacing often delivers better long-term ROAS vì prioritizes algorithmic intelligence over brute-force delivery. Meta interprets pacing rate as proxy for campaign urgency — faster pacing = immediate conversions over learning efficiency.

## Key Takeaways
- Lowest Cost = default cho 80% campaigns
- Cost Cap cần 3 điều kiện: ≥50 conv/week, ≥€5k spend/week, cap ≥ avg CPA
- Value Optimization cho wide AOV range
- ROAS Goal set at 80% trailing 28-day average
- Horizontal scaling > vertical scaling để preserve learning data

---
*Created: 2026-06-15 | Sources: facebook-ads-deep-dive, ads-deep-dive-june-2026*
