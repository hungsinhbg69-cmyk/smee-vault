---
title: "Facebook Ads Index Master Table Of Contents"
slug: "facebook-ads-index-master-table-of-contents"
category: resource
tags: [vault-maintenance, facebook-ads]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---


# Facebook Ads - INDEX (Muc luc tra cuu nhanh)

## 01-fundamentals.md - Nen tang

### Chu de chinh
- Three-tier hierarchy: Campaign > Ad Set > Ad
- 7 campaign objectives phan theo funnel (Awareness -> Consideration -> Conversion)
- Khi nao dung objective gi?

### Quick reference
- Brand Awareness: nguoi hoi nho ads
- Reach: den nhieu nguoi nhat
- Traffic: click den web/app
- Engagement: post engagement, page likes
- Video Views: video watches
- Lead Generation: collect leads khong can rời FB
- Messages: Messenger/Instagram conversations
- Sales: purchases + catalog sales
- Leads: contact info forms
- App Installs: app downloads

### Khi nao dung?
| Goal | Objective |
|---|---|
| Ban hang online | Sales |
| Thu lead B2B | Lead Generation |
| Traffic web | Traffic |
| Build brand | Brand Awareness / Reach |
| Engagement page | Engagement |
| Messenger sales | Messages |

## 02-targeting.md - Audience Targeting

### 3 lo audiences chinh
1. Core Audiences: demographic, location, interest, behavior
2. Custom Audiences: pixel visitors, customer lists, engagement
3. Lookalike Audiences: similar to best customers (1-10%)

### Advantage+ Audiences (2026)
- AI tự find user tot nhat (broad targeting)
- Khong can narrow interest targeting
- Can tối thieu 50 conversions/week/ad set
- Tot hon interest targeting 3-5x neu co pixel data

### Targeting best practices
- Age: 13-65+
- Location: country/state/city/zip/radius
- Interests: categories -> specific interests -> combine for precision
- Behaviors: purchase behavior, device usage
- Exclude converters tu prospecting
- Start broad, layer sau

## 03-creative-formats.md - Ad Formats

### Format co ban
- Single Image/Static: test nhanh, chi phi thap
- Video In-Feed: engagement cao, hook 3s first
- Carousel Ads: 2-10 cards, product catalog
- Reels Ads: vertical 9:16, UGC style best
- Collection Ads: cover + product grid (ecommerce)
- Lead Ads: form on-platform, no landing page

### Image specs
- Recommended: 1080x1080 (square) hoac 1080x1350 (portrait)
- Feed: 1:1 hoac 4:5 aspect ratio
- JPG/PNG

### Video specs
- Recommended: 1080x1080 (square) hoac 1080x1920 (vertical)
- MP4/MOV format
- Max 4GB, 240 minutes
- Feed: 1:1 hoac 4:5
- Stories/Reels: 9:16

### Creative best practices 2026
- Test 3-5 different creatives per ad set
- Different formats (video, static, carousel)
- Hook trong 3 giay đầu
- Captions always (85% watch without sound)
- Mobile-optimized
- UGC style cho Reels
- CTA on every card

## 04-bidding-budget.md - Bidding & Budget

### Budget types
- Daily budget: trung binh spend/ngay
- Lifetime budget: tong spend qua campaign duration

### Bidding strategies
1. Lowest Cost: Facebook optimize low cost nhat (mac dinh)
2. Cost Cap: control average cost per result
3. Bid Cap: control maximum bid

### CBO - Campaign Budget Optimization
- Budget set at campaign level
- Meta phan phối tu dong den ad set tot nhat
- Min 2, max 6 ad sets
- Khong mix different audiences trong same CBO
- Allow learning phase complete

### Learning Phase
- Algorithm hoc which users to show ads to
- Can 50 optimization events/week/ad set
- Performance khong stable during learning
- Avoid major edits during learning
- Exit naturally hoac accelerate by increasing budget

### Budget recommendations
- Start -50/day minimum per ad set
- Test small budgets first
- Scale winners gradual (20% every 3-4 days)
- Aim 50+ conversions/week per ad set

## 05-tracking-pixel.md - Tracking & Pixel

### Meta Pixel functions
- Track actions on website
- Power optimization algorithm
- Enable retargeting
- Measure ROI

### Standard events to track
1. ViewContent
2. AddToCart
3. InitiateCheckout
4. Purchase
5. Lead
6. CompleteRegistration

### Conversions API (CAPI)
- Why need: iOS 14+ privacy changes limit pixel
- Server-side tracking more reliable
- Better data quality
- Improved attribution
- Use alongside pixel, deduplicate events

### Pixel setup checklist
- Generate pixel code in Events Manager
- Add to website (manually or plugin)
- Verify installation
- Test events
- Configure all standard events
- Aim 100+ Purchase events/month for Advantage+ to work best

## 06-optimization.md - Optimization & Scaling

### Testing strategy
- Test one variable at a time
- Run tests minimum 7 days
- Minimum 50 conversions for statistical significance
- Document learnings
- Implement winners, kill losers

### What to test
- Audiences (interest, lookalike, custom)
- Creative (images, videos, formats)
- Copy (headlines, primary text, CTAs)
- Placements
- Ad formats
- Landing pages

### When to scale
- Campaign profitable
- Consistent performance 7+ days
- Learning phase complete
- Budget allows

### How to scale
- Increase budget 20% every 3-4 days (not more)
- Duplicate winning ad sets
- Expand to similar audiences
- Test new creative variations
- Add more placements

### Automation ideas
- Performance alert system (check every 6 hours)
- Budget pacer (daily check)
- Creative rotation schedule

## 07-advantage-plus.md - Advantage+ AI Campaigns

### Advantage+ Shopping Campaigns (ASC)
- AI-driven ecommerce campaigns
- Similar to Google Performance Max
- Combines prospecting + retargeting in one campaign
- Uses product catalog automatically
- Optimizes placements auto (Feed, Stories, Reels, Audience Network)
- Best for: ecommerce with product catalog, 50+ conversions/month

### Advantage+ Audiences
- AI finds best users automatically
- Broad targeting (age/gender only)
- Needs conversion data from Pixel/CAPI
- 3-5x more effective than interest targeting without pixel data
- Need minimum 50 conversions/week/ad set

### Advantage+ Creative
- AI tests creative combinations
- Auto-generates variations
- Learns which hooks/formats work best

### When to use Advantage+
- Have enough conversion data (50+/week)
- Ecommerce with product catalog -> ASC
- Scaling existing campaigns
- Want less manual management

## 08-metrics-benchmarks.md - KPIs & Benchmarks

### Cost benchmarks (US market, 2026)
- CPM: - (varies industry/season)
- CPC: .50-.00
- CPL: - (depends industry)
- Q4 (Oct-Dec): 2-3x more expensive

### Key metrics to track
- CPM (Cost per 1,000 impressions)
- CPC (Cost per Click)
- CTR (Click Through Rate) - benchmark: >1% good
- CPA/CPP (Cost per Acquisition/Result)
- ROAS (Return on Ad Spend) - primary metric for ecommerce
- Conversion Rate
- Frequency (too high = ad fatigue)

### ROAS targets by funnel stage
- Top of funnel (awareness): ROAS 2-3x acceptable
- Middle funnel (consideration): ROAS 3-4x target
- Bottom funnel (conversion): ROAS 4-5x+ target
- Retargeting: ROAS 5-10x typical

### Optimization checklist
- [ ] Pixel installed + all events tracking
- [ ] 50+ conversions/week per ad set
- [ ] 3-5 creatives rotating per ad set
- [ ] CBO enabled for multi-ad set campaigns
- [ ] Weekly creative rotation
- [ ] Budget scale max 20% every 3-4 days
- [ ] Monitor frequency (ad fatigue >3.0)
- [ ] A/B test new hooks monthly

## 09-andromeda-auction.md - Andromeda Algorithm & Auction

### Chu de chinh
- Andromeda = deep learning 2-stage (Retrieval ~50ms + Ranking ~150ms)
- Total Value = Bid x Action Rate + Estimated User Value
- Creative = Targeting moi: Andromeda phan tich visuals, text, format, tone de tu dong infer audience
- Relevance diagnostics 3 chi so (Quality, Engagement, Conversion Rate) o ad-level
- Campaign structures 2026: ASC+, 6-3-1 structure, Manual Sales

### Khi nao dung?
| Scenario | Structure |
|---|---|
| E-commerce >€5K/month | ASC+ (Advantage+ Shopping) |
| Creative control needed | 6-3-1 structure (6 ad sets, 3 creatives) |
| B2B/Service/Lead Gen | Manual Sales Campaigns |

### Still Works vs Dead (2026)
| ✅ STILL WORKS | ❌ DEAD/DYING |
|---|---|
| Broad targeting (18-65+) | Interest stacking (10+ interests) |
| Advantage+ Placements | Manual placement selection |
| UGC-style content | Overly polished corporate ads |
| CAPI server-side tracking | Pixel-only attribution |

## 10-advanced-bidding.md - Advanced Bidding Strategies

### 5 Bid Strategies (2026)
1. **Lowest Cost:** Mac dinh, cho 80% campaigns <€50k/month
2. **Cost Cap:** Khi ≥50 conv/week + ≥€5k spend/week + cap ≥ avg CPA
3. **Bid Cap:** Narrow: auction-level data known, precise margin/SKU
4. **Value Optimization:** DTC wide AOV range (tu $20 den $500+)
5. **ROAS Goal:** E-commerce tracked revenue; set at 80% trailing 28-day ROAS

### CBO - 3 Sai Lam Pho Bien
1. Minimum spend limits khong bao ve small ad-sets → Algorithm funnel 75% cho "winner"
2. Campaign budget ≠ daily spend cap → Monday spend 2x daily average, Thursday 0.4x
3. Audience overlap git efficiency → algorithm khong arbitrage duoc

### Budget Pacing Phases
| Phase | Days | Velocity | Purpose |
|-------|------|----------|---------|
| Exploration | 1-7 | Cap at 60-70% optimal | Buy algorithm time to map conversion landscape |
| Momentum | 8-21 | Increase ≤15% every 48h | Exploit accumulated intelligence |
| Saturation | 22+ | Slow down or refresh creative | Frequency >2.5-3.0 = audience saturation |

### Scaling Rules
- Vertical: increase budget ≤20% mỗi lan, ≥48h giua cac lan tang
- Horizontal (recommended): duplicate winning campaign, test new audiences
- Budget Deployment Velocity (BDV): Actual ÷ Target daily spend hourly

## 11-attribution-tracking.md - Attribution & Measurement Stack

### Attribution Windows
| Window | Khi nao dung |
|--------|--------------|
| 7-day click + 1-day view (default) | Đa so accounts — cân bang credit accuracy và volume |
| 1-day click | Impulse purchases, low-consideration products |
| 7-day click only | Accounts cần conservative attribution |

### January 12, 2026 Update
Meta permanently removed 7-day view and 28-day view windows từ Ads Insights API.

### Measurement Stack (4 Layers)
1. **Layer 1:** Pixel + CAPI → primary conversion tracking
2. **Layer 2:** GA4 cross-check → sanity check (GA4 luôn thap hon Meta)
3. **Layer 3:** MMM / Incrementality test → budget decisions transcend platform math
4. **Layer 4:** SKAdNetwork → mobile app campaigns

### AEM Priority Events (8 events, rank by conversion value)
1. Purchase → 2. InitiateCheckout → 3. AddToCart → 4. ViewContent → 5. Lead → 6. CompleteRegistration → 7. Search → 8. PageView

> ⚠️ Rank AddToCart cao hon Purchase vì thay nhieu hon → Meta attribute ve AddToCart, ROAS math collapse.

### Event Deduplication
- Key: event_id + Pixel ID + event_name
- Window: events within 48 hours → Meta counts ONE conversion
- Failure mode: precision mismatch ("order_123" vs "order_123.567")

### EMQ (Event Match Quality)
| Score | Level |
|-------|-------|
| 0-2 | Poor — CAPI nearly useless |
| 3-5 | Fair — has email OR phone |
| 6-8 | Good — email + phone at minimum → measurable gains |
| 9-10 | Excellent — full parameters optimal |

> ⚠️ EMQ ≥6 = break-even point từ CAPI. Dưới 6: CAPI gần như vo dung.

### Incrementality Testing
- Hold out 10-15% audience từ ads trong 2 weeks
- So sánh conversion rates giữa treated vs control group
- Separates true incremental sales from credited ones
- Đặc biệt quan trọng với ASC broad targeting

---
*Created: 2026-06-15 | Sources aggregated from marketingadvice.ai, marketingagency.one, redclawey.com + facebook-ads-deep-dive + ads-deep-dive-june-2026*

## 📊 Case Studies 2026

### Level 1 — Local/Small ($500-$3K/tháng)
- `cs-local-service-titan-driveways.md` — Dịch vụ địa phương, CPL -50%
- `cs-small-ecommerce-soda-spoon.md` — E-commerce nhỏ, ROAS 3.61x (1 ad duy nhất)
- `cs-b2b-lead-gen-counselling.md` — Lead gen B2B, CPL $4.98 global

### Level 2 — Regional/Mid-Market ($3K-$25K/tháng)
- `cs-dtc-caraway-home.md` — DTC cookware, ROAS 2.9x→4.6x, CAC -34%
- `cs-dtc-cuts-clothing.md` — Fashion/Accessories, ROAS 2.9x→4.8x, CPA $48→$34
- `cs-high-ticket-home-improvement.md` — Home improvement, ROAS 1.18→6.47, $700K revenue

### Level 3 — Global/Large ($25K-$100K+/tháng)
- `cs-chomps-wellness.md` — DTC supplement, ROAS 3.2x→5.1x, CAC -31%
- `cs-hexclad-cookware.md` — Premium cookware, ROAS 2.4x→3.8x, CPA $88→$61
- `cs-momentous-nutrition.md` — Performance nutrition, ROAS 2.4x→4.1x, CAC $68→$41

### Tổng hợp
- `cs-key-insights-2026.md` — 10 bài học chiến lược tổng hợp
- `12-case-studies-2026.md` — INDEX tổng hợp case studies

## ⚡ Quick References

### FB-ADS-KNOWLEDGE-BASE.md
**Single source of truth — full knowledge base.** 8 modules theo workflow thực chiến. Đọc file này để có toàn bộ kiến thức tổng hợp.

### QUICK-DECISION-MATRIX.md
**Agent decision shortcuts trong <30 giây.** Decision trees cho objective, bidding, CBO/ABO, ASC+, targeting, creative format, budget pacing, tracking setup, Vietnam adjustments.

### creative-testing-framework.md
**Atomic note for creative testing workflow.** Competitor audit → variant matrix → test execution → scale & refresh. Hook-rate benchmarks + fatigue detection.

---

## 📚 Bonus: Creative Strategy Deep-Dive (from memory sources)

### Hook Rate Benchmark
- 25% = solid (3-second views / impressions)
- 30% = good
- 40%+ = elite

### UGC vs Produced Creative Decision Matrix
| Situation | Better Format | Why |
|-----------|---------------|-----|
| Cold audience prospecting | UGC | Blends into feed; feels peer-recommended |
| Products under $100 | UGC | Lower consideration threshold |
| Products $200+ | Produced/Hybrid | Higher AOV needs trust signals |
| Retargeting warm audiences | Both | Warm audiences respond to different signals |
| Brand awareness | Produced | Professional quality signals credibility |
| Seasonal launches (Q4) | Produced/Hybrid | Polished creative drives seasonal conversions |

### Creative Testing System
1. Competitor audit: Identify 30+ day running ads trong category → hook structures, offer framings
2. Variant matrix: 3 hook angles x 2 visual treatments x 2 CTAs = 12 variants per creative brief
3. Test window minimum: 1,000-2,000 impressions + 7 days trước khi scale/kill
4. Refresh cadence: Every 10-14 days — don't wait for performance collapse
5. Creative lifespan on Meta: 3-6 weeks

### Budget Allocation Rule (70-20-10)
- **70%** → Winning campaigns (scale what works)
- **20%** → Testing new audiences/angles
- **10%** → Creative format testing

### Creative Fatigue Management
- Frequency >3.0 = fatigue trigger
- Ads run 3-4 weeks without refresh: CPMs rise up to 29%, CTRs fall up to 35%
- Watch frequency + CTR trends → time refreshes proactively
- Fast pacing + rapid frequency increase = imminent creative fatigue

### Hook-Story-Close Framework (Verified High-Performing)
1. **Hook (0-3s):** Pattern interrupt — "I tried 47 marketing tools..." / "This mistake cost me $10K..."
2. **Story (15-20s):** Build curiosity, show transformation
3. **Close (last 5s):** Clear, specific CTA

### Vietnam-Specific Adjustments
| Factor | Global Benchmark | Vietnam Reality | Adjustment |
|--------|-----------------|-----------------|------------|
| CPM levels | $10-50 (US/EU) | ₫20,000-80,000 (~$0.80-3.20) | Budget thresholds scale down — 50 events/week achievable at lower spend |
| iOS ATT opt-out rate | 70%+ | ~40-50% (lower upgrade cycle) | Pixel degradation less severe; CAPI still recommended but not urgent for SMBs |
| Ad blocker penetration | 30%+ global | ~10-15% | Pixel-only gap narrower, but CAPI adds server-side events |
| Payment behavior | Credit card dominant | COD 60-70%, e-wallets rising | Optimize "Purchase" event post-delivery confirmation, not just checkout |
| Zalo ecosystem | N/A | Major social channel | Consider cross-channel: Meta prospecting → Zalo closing |