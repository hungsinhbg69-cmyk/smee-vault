# 11 - Attribution & Measurement (Attribution + Measurement Stack)

## Attribution Windows (Post-iOS 14)

| Window | Khi nào dùng | Ghi chú |
|--------|--------------|---------|
| **7-day click + 1-day view** (default) | Đa số accounts — cân bằng giữa credit accuracy và volume | Mac dinh, dùng cho 90% trường hợp |
| **1-day click** | Impulse purchases, low-consideration products | Conservative attribution |
| **7-day click only** | Accounts cần conservative attribution | Loại trừ view-through credit |

### January 12, 2026 — Attribution Update
Meta permanently removed 7-day view and 28-day view windows từ Ads Insights API. Overnight, advertiser dashboards mất credit cho view-through conversions.

> ⚠️ **Quan trọng:** Chỉ còn click attribution + short view window. View-through conversions giảm đáng kể → ROAS numbers thấp hơn trước đây mặc dù actual performance có thể không đổi.

## Measurement Stack (2026)

```
Layer 1: Pixel + CAPI → primary conversion tracking
Layer 2: GA4 cross-check → sanity check (GA4 luôn thấp hơn Meta vì attribution model mismatch)
Layer 3: MMM / Incrementality test → budget decisions transcend any single platform's math
Layer 4: SKAdNetwork → mobile app campaigns (distinct track, không extension của web stack)
```

### Layer 1: Pixel + CAPI
- Primary conversion tracking source
- Deduplication key: event_id + Pixel ID + event_name
- Window: events within 48 hours → Meta counts ONE conversion
- **Failure mode phổ biến:** Pixel gửi `event_id: "order_123_1678901234"`, server gửi `"order_123_1678901234.567"` (precision khác) → Meta đếm 2 conversions → ROAS inflate

### Layer 2: GA4 Cross-Check
- GA4 luôn thấp hơn Meta vì attribution model mismatch
- Dùng để sanity check, không phải source of truth
- UTM structure chuẩn: source/medium/campaign/content/term
- Check monthly trend direction, không phải absolute numbers

### Layer 3: Incrementality Testing
- Hold out 10-15% audience từ ads trong 2 weeks
- So sánh conversion rates giữa treated vs control group
- Separates true incremental sales from credited ones
- Đặc biệt quan trọng với ASC broad targeting (dễ attribution overlap)

### Layer 4: SKAdNetwork
- Mobile app campaigns tracking
- Distinct track, không extension của web stack
- iOS 16+ support SKAdNetwork 4.0

## AEM — Aggregated Event Measurement (8 Priority Events)

Rank by conversion value, NOT frequency:

| Rank | Event | Why This Rank |
|------|-------|---------------|
| 1 | Purchase | Highest conversion value |
| 2 | InitiateCheckout | High intent signal |
| 3 | AddToCart | Frequent but lower value |
| 4 | ViewContent | Broadest reach, lowest value |
| 5 | Lead | Medium-high value for lead gen |
| 6 | CompleteRegistration | Account activation |
| 7 | Search | Intent signal, variable value |
| 8 | PageView | Lowest conversion value |

> ⚠️ Rank AddToCart cao hơn Purchase vì thấy nhiều hơn → Meta attribute về AddToCart, ROAS math collapse nếu Purchase event missing hoặc delayed.

## Event Deduplication Details

### Deduplication Key Format
```
Deduplication key: event_id + Pixel ID + event_name
Window: events within 48 hours
Result: Meta counts ONE conversion
```

### Common Failure Modes
1. **Precision mismatch:** `"order_123"` vs `"order_123.0"` → counted as 2 conversions
2. **Timing gap >48h:** Pixel fires event at T=0, CAPI fires at T=50h → no deduplication
3. **Different event_id format:** One uses UUID, other uses order number → no match

### Best Practices
- Generate event_id ONCE (preferably server-side)
- Use consistent format across Pixel and CAPI
- Include timestamp in event_id for debugging: `"order_123_20260615T130000Z"`
- Monitor deduplication rate trong Events Manager

## Event Match Quality (EMQ)

| Score | Level | Description |
|-------|-------|-------------|
| 0-2 | Poor | Missing email + phone — CAPI nearly useless |
| 3-5 | Fair | Has email OR phone — some matching possible |
| 6-8 | Good | Email + phone at minimum — measurable performance gains |
| 9-10 | Excellent | Full parameters (email, phone, name, IP, user agent) — optimal matching |

### EMQ Parameters Weight
1. **Email** (highest weight) — hashed SHA-256
2. **Phone number** (second-highest) — formatted E.164
3. **First name + Last name**
4. **Client IP address**
5. **User agent string**

> ⚠️ EMQ ≥6 = break-even point từ CAPI. Dưới 6: Meta không thể match đa số events → CAPI gần như vô dụng.

## Incrementality Testing Framework

### Setup
1. **Control group:** 10-15% of target audience, NOT exposed to ads
2. **Test group:** Remaining audience, served ads normally
3. **Duration:** Minimum 2 weeks (capture weekly cycles)
4. **Metric:** Conversion rate difference between groups

### Analysis
```
Incremental ROAS = (Test CVR - Control CVR) × AOV / CPA
True Incremental Conversions = Test conversions - Control conversions
```

### When to Use
- ASC broad targeting accounts (attribution overlap risk)
- Large budgets where small % changes matter ($10K+/month)
- Before major budget increases
- Quarterly validation of channel effectiveness

## Key Takeaways
- Attribution windows simplified: 7-day click + 1-day view is default
- Measurement stack needs all 4 layers for complete picture
- Deduplication key format must be consistent between Pixel and CAPI
- EMQ ≥6 required for measurable CAPI gains
- Incrementality testing separates true incremental sales from credited ones

---
*Created: 2026-06-15 | Sources: facebook-ads-deep-dive, ads-deep-dive-june-2026*
