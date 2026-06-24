---
title: "Andromeda Auction"
slug: "andromeda-auction"
category: resource
tags: [facebook-ads, meta-ads]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

# 09 - Andromeda & Auction Dynamics (Hệ thống đấu giá mới)

## Meta Andromeda Algorithm (2024-2026)

Andromeda thay thế engine xếp hạn cũ của Meta — hệ thống deep-learning hai giai đoạn chạy trên toàn bộ surface: Facebook Feed, Instagram Feed, Reels, Stories, Marketplace.

### Kiến trúc 2 Stage

| Stage | Mô tả | Thời gian |
|-------|--------|-----------|
| **Retrieval** | Approximate nearest-neighbor lookup — embedding ads/users thành vectors, lọc từ hàng tỷ candidate xuống vài nghìn relevant candidates | ~50ms |
| **Ranking** | Deep ranking model đánh giá 100+ features: engagement history, purchase signals, creative elements (visual type, text sentiment, CTA), historical performance, time-of-day, device, auction competition | ~150ms |

### Total Value Formula

```
Total Value = Bid × Predicted Action Rate + Estimated User Value
```

- **Predicted Action Rate**: Xác suất user thực hiện action bạn bid (click, purchase, lead)
- **Estimated User Value**: Long-term experience quality — penalize ads users hide, report, or skip within 1 second
- **Hệ quả**: Creative chất lượng thấp không chỉ tự đánh bại mình mà còn giảm competitiveness trong auction

### Andromeda Implications

1. **Creative = Targeting mới.** Andromeda phân tích visuals, text, format, tone, context cues để tự động infer audience. Weak creative = không deliver at all vì algorithm không identify được audience.
2. **Ad sets tight definitions hoạt động ổn định nay thường không exit learning phase** — vì retrieval layer đã biết phải serve ad cho ai mà không cần được told.
3. **Andromeda data-hungry hơn predecessor:** cần ≥50 optimization events/ad-set/week để exit learning phase ổn định. CPA trong learning phase cao hơn 20-35% so với post-learning averages.

## Auction Dynamics: Meta vs Google

| Dimension | Google Ads | Meta Ads |
|-----------|------------|----------|
| Auction trigger | User search query | User opens app / scrolls feed |
| Intent signal | Explicit (keyword) | Implicit (user profile + behavior) |
| Quality score | Quality Score 1-10 | Relevance diagnostics (Above/Average/Below) |
| Winning formula | Bid × Quality Score | Bid × Action Rate × Ad Quality |
| Auction type | Generalized second-price | Vickrey second-price |

## Ba Relevance Diagnostics (Ad-Level)

Diagnostic ở ad-level, không phải campaign-level. Dùng để pinpoint problem source:

1. **Quality Ranking**: Perceived quality vs competing ads — Below average = creative issue
2. **Engagement Rate Ranking**: Expected engagement rate — Below average = hook/messaging weak
3. **Conversion Rate Ranking**: Expected conversion rate vs audience+objective — Below average = landing page/offer issue

## Campaign Structures That Work (2026)

### Option A: Advantage+ Shopping (ASC+) — Default cho E-commerce
- Collapse prospecting + retargeting vào single campaign
- Auto-budget allocation giữa new customer acquisition và existing customer purchase
- Set "Existing Customer Budget Cap" ở mức **20-30%** để prevent cannibalization
- Accounts spending >€5K/month → ASC+ outperform manual funnel structures

### Option B: Standard 6-3-1 Structure — Cho accounts cần creative control
- **6 ad sets** (broad hoặc Advantage+ Audience)
- **3 creatives** per ad set
- **1 winning angle** per creative
- Produces đủ learning phase data mà không fragment budget

### Option C: Manual Sales Campaigns — Service businesses / Lead Gen
- Need more control over messaging, landing pages, bid strategy
- Best cho B2B, consultants, agencies, local services
- Higher-ticket items where ad-to-LP consistency matters

## What Still Works vs What's Dead (2026)

| ✅ STILL WORKS | ❌ DEAD / DYING |
|---|---|
| Broad targeting (18-65+) | Interest stacking (10+ interests) |
| Advantage+ Placements | Manual placement selection |
| UGC-style content | Overly polished corporate ads |
| CAPI server-side tracking | Pixel-only attribution |
| Video-first creative strategy | Static images as primary format |
| First-party data integration | Third-party cookie reliance |
| 20% budget increase every 3 days | Overnight budget doubling |

## Key Takeaways
- Andromeda = deep learning 2-stage (Retrieval ~50ms + Ranking ~150ms)
- Total Value = Bid × Action Rate + Estimated User Value
- Creative quality thấp → giảm competitiveness trong auction, không chỉ underperform
- Relevance diagnostics ở ad-level: dùng để pinpoint creative vs post-click issue

---
*Created: 2026-06-15 | Sources: facebook-ads-deep-dive, ads-deep-dive-june-2026*
