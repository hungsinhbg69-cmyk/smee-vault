# 🎯 Facebook Ads — Quick Decision Matrix 2026

> **Mục đích:** Agent đọc trong <30 giây để đưa ra recommendation. Không giải thích dài, chỉ decision paths.

---

## DECISION: "Nên dùng campaign objective nào?"

| Business Goal | Objective | Bidding | Budget Min |
|---------------|-----------|---------|------------|
| Bán hàng online | **Sales** (Conversions) | Lowest Cost → ROAS Goal khi có data | $50+/ad set/day |
| Thu lead B2B/B2C | **Lead Generation** | Lowest Cost | $30+/ad set/day |
| Traffic website/app | **Traffic** | Lowest Cost | $20+/ad set/day |
| Build brand awareness | **Brand Awareness / Reach** | Lowest Cost | $25+/day |
| Engagement page/posts | **Engagement** | Lowest Cost | — |
| Messenger/IG sales | **Messages** | Lowest Cost | $30+/ad set/day |

---

## DECISION: "CBO hay ABO?"

```
Có ≥3 ad sets competing cho cùng audience type?
├── YES → CBO (Campaign Budget Optimization)
│   └── Max 6 ad sets, similar audiences only
└── NO
    ├── Testing new audiences? → ABO (equal spend per test)
    ├── Single ad set? → Either (no difference)
    └── Limited budget <$50/day total? → ABO (guaranteed min spend per test)
```

---

## DECISION: "Bidding strategy nào?"

```
Có ≥50 conv/week/ad-set + biết target CPA?
├── YES → Cost Cap (set cap = 1.5-2x target CPA ban đầu, tighten sau)
└── NO
    ├── E-commerce có historical ROAS stable? → ROAS Goal (=80% trailing 28-day ROAS)
    ├── Wide AOV range ($20-$500+)? → Value Optimization
    ├── Competitive auction + known margin/SKU? → Bid Cap
    └── Most cases (80%) → Lowest Cost (default — START HERE)
```

---

## DECISION: "ASC+ hay Manual?"

| Condition | ASC+ | Manual |
|-----------|------|--------|
| E-commerce + product catalog + ≥50 conv/month | ✅ **YES** | ❌ Overhead không cần thiết |
| Service business / Lead Gen | ❌ No catalog | ✅ Need messaging control |
| New store <10 conv/month | ❌ Not enough data for AI | ✅ Test variables in isolation |
| B2B high-ticket (> $5K) | ❌ Less granular control | ✅ Ad-to-LP consistency critical |

---

## DECISION: "Targeting strategy nào?"

```
Có ≥50 conv/week/ad-set + Pixel data?
├── YES → Advantage+ Audience (broad 18-65+)
│   └── Creative signals > Interest targeting trong 2026
└── NO (new account / cold start)
    ├── E-commerce? → Lookalike 1% từ purchasers (min 1,000 source people)
    ├── Local service? → Radius targeting + broad interest layer
    └── B2B/Professional? → Interest + behavior stack (job title, industry, life events)
```

---

## DECISION: "Creative format nào?"

| Situation | Format | Hook | CTA |
|-----------|--------|------|-----|
| Cold audience prospecting | UGC Video Reels (9:16) | Pattern interrupt (0-3s) | Soft: Learn More / Shop Now |
| Products <$100 | UGC style, authentic feel | Pain point + solution | Direct: Buy Now / Shop Now |
| Products $200+ | Produced/Hybrid video | Transformation story | Value-driven: Get Offer / Learn More |
| Retargeting warm audience | Carousel or Single Image | "Still thinking about it?" urgency | Direct: Order Now / Sign Up |
| Lead Gen B2B | Video + Native Form | Problem statement → solution | Lead form submit (no LP) |

---

## DECISION: "Budget pacing — tăng bao nhiêu?"

```
Campaign đã profitable 7+ days? Learning phase complete?
├── YES → Tăng ≤20% mỗi lần, ≥48h giữa các lần tăng
│   ├── Vertical scaling: increase trên ad set cũ
│   └── Horizontal (recommended): duplicate campaign → test new audiences
└── NO → Chờ learning phase exit hoặc consolidate vào fewer ad sets
```

**Budget Pacing Phases:**
- Days 1-7: Cap at 60-70% optimal budget (exploration)
- Days 8-21: Increase ≤15% every 48h (momentum)
- Day 22+: Slow down or refresh creative (saturation — frequency >2.5 = danger)

---

## DECISION: "Khi nào refresh creative?"

| Trigger | Action |
|---------|--------|
| Frequency >3.0 | **Immediate** — rotate new variants |
| CTR falling >15% from baseline | Within 48h — test new hooks |
| CPA increasing >20% from baseline | Hold 3-4 days → refresh creative |
| Creative run 3+ weeks without changes | Proactive refresh (creative lifespan = 3-6 weeks) |

---

## DECISION: "Tracking setup priority"

```
1. Install Meta Pixel + CAPI simultaneously ← NON-NEGOTIABLE
2. Configure all standard events (Purchase, Lead, ViewContent...)
3. Verify EMQ ≥6 via Events Manager ← Break-even point for CAPI
4. Set attribution window = 7-day click + 1-day view (default)
5. Cross-check with GA4 monthly (trend direction, not absolute numbers)
6. Run incrementality test quarterly if budget $10K+/month
```

---

## DECISION: "Vietnam-specific adjustments"

| Factor | Adjustment |
|--------|------------|
| CPM ₫20K-80K (thấp hơn US/EU 5-15x) | 50 conv/week achievable at lower spend → scale faster |
| iOS ATT opt-out ~40-50% (thấp hơn US 70%+) | Pixel degradation less severe, CAPI recommended but not urgent for SMBs |
| COD 60-70% payment behavior | Optimize "Purchase" event post-delivery confirmation, not just checkout |
| Zalo ecosystem major | Consider: Meta prospecting → Zalo closing funnel |
| Phone number lists high match rate | Upload phone numbers alongside emails for Custom Audiences |

---

*Quick reference only — see FB-ADS-KNOWLEDGE-BASE.md for full details*
