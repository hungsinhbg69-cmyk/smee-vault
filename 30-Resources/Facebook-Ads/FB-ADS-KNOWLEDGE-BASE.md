# 📘 Facebook Ads Knowledge Base — Tổng Hợp 2026

> **Mục đích:** Single source of truth cho toàn bộ kiến thức Facebook/Meta Ads. Được tổng hợp, phân loại và tối ưu cho agent đọc/nhánh nhanh.
> 
> **Cập nhật cuối:** 2026-06-20 | **Tổng hợp từ:** ~45+ file trong vault
> 
> **Cấu trúc:** 8 module theo workflow thực chiến → từ setup đến attribution

---

## 📋 Mục Lục Nhanh

| Module | Nội dung | File gốc |
|--------|----------|----------|
| M1 | Fundamentals & Hierarchy | 01-fundamentals.md, INDEX |
| M2 | Audience Targeting Strategy | 02-targeting.md, advantage-over-narrow-targeting.md |
| M3 | Creative Formats & Testing | 03-creative-formats.md, creative-testing-key-lever.md |
| M4 | Bidding, Budget & CBO | 04-bidding-budget.md, 10-advanced-bidding.md |
| M5 | Tracking: Pixel + CAPI + Attribution | 05-tracking-pixel.md, 11-attribution-tracking.md |
| M6 | Advantage+ AI Campaigns | 07-advantage-plus.md |
| M7 | Andromeda Algorithm & Auction | 09-andromeda-auction.md, ads-deep-dive-june-2026.md |
| M8 | Metrics, Benchmarks + Case Studies | 08-metrics-benchmarks.md, cs-key-insights-2026.md, campaigns analysis files |

---

## MODULE 1: FUNDAMENTALS & CAMPAIGN HIERARCHY

### Campaign Structure (3-Tier)
```
Ad Account
└── Campaign (Objective duy nhất)
    └── Ad Set (Targeting + Budget + Placements)
        └── Ad (Creative A/B/C, Copy, CTA)
```

**Golden Rule 2026:** 1 campaign per objective. Never mix Sales + Leads + Traffic trong cùng 1 campaign. Mỗi objective optimize khác nhau.

### 7 Campaign Objectives — Khi Nào Dùng Gì?

| Objective | Mục tiêu | KPI chính | Phù hợp cho |
|-----------|----------|-----------|-------------|
| **Sales** (Conversions) | Drive purchases + catalog sales | CPA, ROAS | E-commerce, DTC |
| **Lead Generation** | Collect leads in-platform | CPL, form quality | B2B, real estate, education |
| **Messages** | Messenger/IG conversations | Cost/conversation start | Local business, consulting |
| **Traffic** | Clicks to website/app | CPC, CTR, LP views | Blog, landing page, affiliate |
| **Awareness / Reach** | Brand recall + max reach | GRP, ad recall lift | New brand launch |
| **Engagement** | Post engagement, page likes | Engagement cost | Community building |
| **Video Views** | Video watches/completions | 3-sec views, ThruPlays | Content creators, training |

### CBO vs ABO — Khi Nào Dùng Gì?

| Scenario | Budget Type | Lý do |
|----------|-------------|-------|
| Testing new audiences | **ABO** (ad set budget) | Equal spend per test |
| Scaling winners | **CBO** (campaign budget) | Algorithm finds cheapest results |
| 3+ ad sets established | **CBO** | Proven distribution works |
| Limited budget (<$50/day total) | **ABO** | Guarantee each test gets spend |
| Single ad set | Either | No difference with 1 ad set |

---

## MODULE 2: AUDIENCE TARGETING STRATEGY

### 3 Loại Audiences

| Type | Mô tả | Khi dùng |
|------|--------|----------|
| **Core** (Manual) | Demographic, location, interest, behavior | New accounts, cold starts |
| **Custom** (Retargeting) | Pixel visitors, customer lists, engagers | MOFU/BOFU — always outperform cold |
| **Lookalike** (LAL) | Similar to best customers | TOFU prospecting with data |

### Advantage+ Audiences vs Traditional Targeting

| Dimension | Traditional Interest | Advantage+ Audience (2026 standard) |
|-----------|---------------------|-------------------------------------|
| Input | Narrow interests/behaviors | Broad (age/gender/location only) |
| AI finds users? | No — manual selection | Yes — based on conversion data + creative signals |
| Data dependency | Interest database quality | Pixel/CAPI conversion quality |
| Performance with pixel | Baseline | **3-5x better** than interest targeting |

### Rule: Advantage+ > Narrow Targeting khi có ≥50 conversions/week/ad set. Dùng interest targeting chỉ cho new accounts/cold starts.

### Funnel Stage × Audience Mapping

| Funnel Stage | Audience Strategy |
|--------------|-------------------|
| **TOFU** (Prospecting) | Advantage+ broad, LAL 1% từ purchasers, Interest (new account only) |
| **MOFU** (Consideration) | Website visitors 30-90d, Video viewers 50%+, IG engagers 90d |
| **BOFU** (Conversion/Retargeting) | Visitors 7-14d, Cart abandoners, Previous purchasers (cross-sell), Engagers 30d |

### LAL Quality Scale
- **1%** → Most similar, highest quality, smallest reach — START HERE
- **5%** → Balance of quality + reach
- **10%** → Largest reach, lowest quality
- Source audience minimum: 1,000 people (best source = purchasers > leads > engagers)

### Vietnam-Specific Targeting Tips
- Phone number lists có match rate cao hơn email ở VN
- Instagram engagement cao — dùng IG engagers cho retargeting
- Messenger là key conversion channel — Messages objective hoạt động tốt
- Radius targeting hiệu quả cho local businesses

---

## MODULE 3: CREATIVE FORMATS & TESTING SYSTEM

### Ad Formats Available (2026)

| Format | Best for | Spec |
|--------|----------|------|
| Single Image/Static | Quick test, low cost | 1080x1080 hoặc 1080x1350 (portrait), JPG/PNG |
| Video In-Feed | High engagement | Hook trong 3s đầu, MP4/MOV, captions always on |
| Carousel Ads | Product showcase (2-10 cards) | Each card có CTA riêng |
| Reels Ads (9:16) | UGC style prospecting | Vertical full-screen, authentic feel |
| Collection Ads | E-commerce product grid | Cover + product grid overlay |
| Lead Ads | In-platform form capture | No landing page needed — lower friction |

### Creative Testing Framework (4 Bước)

**Bước 1: Competitor Audit**
- Identify 30+ day running ads trong category → hook structures, offer framings
- Tools: Facebook Ad Library, Meta Ad Inspector

**Bước 2: Variant Matrix**
- 3 hook angles × 2 visual treatments × 2 CTAs = **12 variants per creative brief**
- Không test nhiều biến cùng lúc — isolate variable testing

**Bước 3: Test Window Minimum**
- 1,000-2,000 impressions + 7 days trước khi scale/kill
- Cần ≥50 conversions cho statistical significance

**Bước 4: Refresh Cadence**
- Every **10-14 days** — don't wait for performance collapse
- Creative lifespan on Meta: **3-6 weeks**
- Frequency >3.0 = fatigue trigger → refresh ngay

### Hook-Rate Benchmarks (3-second views / impressions)
| Score | Level |
|-------|-------|
| 25%+ | Solid |
| 30%+ | Good |
| 40%+ | Elite |

### UGC vs Produced Creative Decision Matrix

| Situation | Better Format | Why |
|-----------|---------------|-----|
| Cold audience prospecting | **UGC** | Blends into feed; feels peer-recommended |
| Products under $100 | **UGC** | Lower consideration threshold |
| Products $200+ | **Produced/Hybrid** | Higher AOV needs trust signals |
| Retargeting warm audiences | Both | Warm audiences respond to different signals |
| Brand awareness | **Produced** | Professional quality signals credibility |

### Budget Allocation Rule (70-20-10)
- **70%** → Winning campaigns (scale what works)
- **20%** → Testing new audiences/angles
- **10%** → Creative format testing

---

## MODULE 4: BIDDING, BUDGET & SCALING

### Budget Types

| Type | Mô tả | Khi dùng |
|------|--------|----------|
| **Daily** | Average spend/ngày (±15% fluctuation) | Predictable spending, consistent delivery |
| **Lifetime** | Total spend qua campaign duration | Time-limited campaigns, events, promotions |

### 5 Bidding Strategies — Khi Nào Dùng?

| Strategy | Control Model | Requirement | Khi dùng |
|----------|---------------|-------------|----------|
| **Lowest Cost** (Default) | No constraint; max results within budget | None | 80% campaigns — START HERE |
| **Cost Cap** | Target avg CPA | ≥50 conv/week + ≥€5k spend/week | Khi đã biết target CPA, scaling phase |
| **Bid Cap** | Hard per-auction ceiling | Auction-level data known | Competitive auctions, precise margin/SKU |
| **Value Optimization** | Optimize for purchase VALUE not volume | Wide AOV range ($20-$500+) | DTC với differential margins giữa products |
| **ROAS Goal** | Min ROAS threshold | Clean revenue tracking (CAPI+Pixel) | E-commerce đã có historical ROAS stable |

### Cost Cap — 3 Điều Kiện Sống Còn
1. ≥50 conversions/week/ad-set → Meta cần statistical signal để estimate CPA
2. ≥€5,000 weekly spend/ad-set → đủ auction participation
3. Cap ≥ trailing 7-day average CPA → cap đặt below realistic = delivery collapse

### Learning Phase (Phase Học) — Critical Rules

| Trigger | Action Required |
|---------|-----------------|
| New campaign created | Allow 48h before judging performance |
| Budget change >25% | Resets learning phase |
| Creative swap | May trigger re-learning |
| Ad paused + reactivated | Re-enter learning |
| **Magic number: ≥50 optimization events/week/ad set** | Exit learning naturally |

### Learning Phase Statuses
- **"Learning Limited"** = chưa đủ events → consolidate ad sets hoặc broaden targeting
- **"Active" (no badge)** = successfully exited → optimize freely
- **CPA trong learning phase cao hơn 20-35%** so với post-learning averages

### Scaling Rules — Vertical vs Horizontal

| Method | How | Pros | Cons | Rule |
|--------|-----|------|------|------|
| **Vertical** (increase budget) | Tăng trên ad set cũ | Đơn giản, giữ learning data | Risk reset learning nếu tăng quá nhanh | ≤20% mỗi lần, ≥48h giữa các lần |
| **Horizontal** (duplicate + expand) | Copy campaign → test new audiences | Preserve original learning | More management overhead | Recommended — preserves learning data |

### Budget Pacing Phases

| Phase | Days | Velocity | Purpose |
|-------|------|----------|---------|
| **Exploration** | 1-7 | Cap at 60-70% optimal budget | Buy algorithm time to map conversion landscape |
| **Momentum** | 8-21 | Increase ≤15% every 48h | Exploit accumulated intelligence |
| **Saturation** | 22+ | Slow down or refresh creative | Frequency >2.5-3.0 = audience saturation |

### CBO — 3 Sai Lầm Phổ Biến
1. **Minimum spend limits không bảo vệ small ad-sets** → Algorithm park 3/4 ở floor, funnel 75% cho "winner"
2. **Campaign budget ≠ daily spend cap** → Monday có thể spend 2x average, Thursday chỉ 0.4x (lifetime budget)
3. **Audience overlap giết efficiency** → Algorithm không arbitrage được khi share audience

---

## MODULE 5: TRACKING — PIXEL + CAPI + ATTRIBUTION

### Measurement Stack (4 Layers)

```
Layer 1: Pixel + CAPI → primary conversion tracking ← SOURCE OF TRUTH
Layer 2: GA4 cross-check → sanity check (GA4 luôn thấp hơn Meta)
Layer 3: MMM / Incrementality test → budget decisions transcend platform math
Layer 4: SKAdNetwork → mobile app campaigns (separate track)
```

### Pixel + CAPI — Deduplication Rules

| Parameter | Requirement |
|-----------|-------------|
| **Dedup key** | event_id + Pixel ID + event_name |
| **Window** | Events within 48h → Meta counts ONE conversion |
| **Best practice** | Generate event_id ONCE server-side, consistent format across both |

### Event Match Quality (EMQ) — CAPI Effectiveness

| EMQ Score | Level | Result |
|-----------|-------|--------|
| 0-2 | Poor | CAPI nearly useless |
| 3-5 | Fair | Some matching possible |
| **6-8** | **Good** | **Break-even point — measurable gains** ← TARGET |
| 9-10 | Excellent | Optimal matching |

> ⚠️ EMQ ≥6 = break-even từ CAPI. Dưới 6: CAPI gần như vô dụng. Priority params: Email (SHA-256) > Phone (E.164) > Name > IP > User Agent.

### AEM — Aggregated Event Measurement (8 Priority Events)

| Rank | Event | Why This Rank |
|------|-------|---------------|
| 1 | **Purchase** | Highest conversion value |
| 2 | **InitiateCheckout** | High intent signal |
| 3 | **AddToCart** | Frequent but lower value |
| 4 | **ViewContent** | Broadest reach, lowest value |
| 5 | **Lead** | Medium-high for lead gen |
| 6 | **CompleteRegistration** | Account activation |
| 7 | **Search** | Intent signal, variable value |
| 8 | **PageView** | Lowest conversion value |

> ⚠️ Rank AddToCart cao hơn Purchase vì thấy nhiều hơn → Meta attribute về AddToCart, ROAS math collapse nếu Purchase missing/delayed.

### Attribution Windows (Post-January 2026 Update)

| Window | Khi nào dùng | Ghi chú |
|--------|--------------|---------|
| **7-day click + 1-day view** (default) | 90% accounts — cân bằng accuracy và volume | Default, safe choice |
| **1-day click** | Impulse purchases, low-consideration products | Conservative |
| **7-day click only** | Accounts cần conservative attribution | No view-through credit |

> ⚠️ January 12, 2026: Meta permanently removed 7-day view và 28-day view windows từ Ads Insights API. View-through conversions giảm → ROAS numbers thấp hơn mặc dù actual performance có thể không đổi.

### Incrementality Testing Framework
- Hold out **10-15% audience** khỏi ads trong **2 weeks**
- So sánh conversion rates giữa treated vs control group
- Đặc biệt quan trọng với ASC broad targeting (attribution overlap risk)
- Conversion Lift tool miễn phí từ Meta — dùng khi budget $10K+/month

---

## MODULE 6: ADVANTAGE+ AI CAMPAIGNS

### Advantage+ Shopping Campaigns (ASC+)

| Dimension | Traditional E-commerce | ASC+ |
|-----------|----------------------|------|
| Campaigns needed | 3-5 (prospecting, retargeting, catalog) | **1** (all combined) |
| Ad sets | Multiple segmented audiences | AI-determined signals |
| Placements | Manual selection | Auto-optimized |
| Management time | 5-10 hours/week | **1-2 hours/week** |
| Performance | Good with optimization | Often BETTER with data |

### ASC+ Requirements & Setup
- ✅ Facebook Product Catalog connected + approved by Meta
- ✅ Minimum **50+ conversions/month** (purchase events)
- ✅ Pixel/CAPI tracking purchases với values
- ⚙️ Set "Existing Customer Budget Cap" ở mức **20-30%** prevent cannibalization

### ASC+ 4-Phase Rollout Plan

| Phase | Timeline | Actions | Target |
|-------|----------|---------|--------|
| Foundation | Weeks 1-2 | Install Pixel + CAPI, connect catalog, enable Advantage+ Shopping | Setup complete |
| Data accumulation | Weeks 3-6 | Let ASC gather data, add 3-5 creatives, monitor weekly CPA/ROAS/frequency | 50+ purchases/month through ASC |
| Optimization | Weeks 7-12 | Analyze winning creatives, add variations, test budget levels (scale 20%/3-4 days) | Established creative refresh cycle |
| Scale | Month 3+ | Duplicate ASC at higher budget if profitable, expand LALs supplement, monthly creative A/B test | ~2 hours/week management |

### When NOT to Use Advantage+
- New store <10 conversions/month → not enough data for AI
- Service business without product catalog
- Need granular audience control (specific interest targeting)
- Very limited budget (<$20/day total)
- Testing phase needing isolated variable control

---

## MODULE 7: ANDROMEDA ALGORITHM & AUCTION DYNAMICS

### Andromeda Architecture — Deep Learning 2-Stage

| Stage | Function | Latency | Description |
|-------|----------|---------|-------------|
| **Retrieval** | ANN vector search | ~50ms | Embed ads/users → filter from billions to thousands of relevant candidates |
| **Ranking** | Multi-feature deep model | ~150ms | 100+ features: engagement history, purchase signals, creative elements, historical performance, time-of-day, device, auction competition |

### Total Value Formula (Auction Winner)
```
Total Value = Bid × Predicted Action Rate + Estimated User Value
```

- **Predicted Action Rate**: Probability user performs your bid action (click, purchase, lead)
- **Estimated User Value**: Long-term experience quality — penalize ads users hide/report/skip within 1 second
- **Implication:** Low-quality creative không chỉ underperform → giảm competitiveness trong auction hoàn toàn

### Creative = Targeting Mới — Paradigm Shift
- Andromeda analyzes visuals, text, format, tone, context cues để tự động infer audience
- Weak creative = không deliver at all (algorithm không identify được audience)
- Brands winning 2026 = brands feed system **creative variety** (không phải volume)
- Accounts ship <8 new creatives/month = running on borrowed time

### Campaign Structures That Work (2026 Decision Tree)

| Scenario | Recommended Structure | Why |
|----------|----------------------|-----|
| E-commerce >€5K/month spend | **ASC+** | AI handles prospecting + retargeting, management efficiency |
| Need creative control | **6-3-1 structure** (6 ad sets × 3 creatives) | Learning data without budget fragmentation |
| B2B / Service / Lead Gen | **Manual Sales Campaigns** | More control over messaging, LP, bid strategy |

### Still Works vs Dead (2026 Reality Check)

| ✅ STILL WORKS | ❌ DEAD/DYING |
|---|---|
| Broad targeting (18-65+) | Interest stacking (10+ interests) |
| Advantage+ Placements | Manual placement selection |
| UGC-style content | Overly polished corporate ads |
| CAPI server-side tracking | Pixel-only attribution |
| Video-first creative strategy | Static images as primary format |
| First-party data integration | Third-party cookie reliance |
| 20% budget increase every 3-4 days | Overnight budget doubling |

---

## MODULE 8: METRICS, BENCHMARKS & KEY INSIGHTS

### Key Metrics to Track (Priority Order)

1. **ROAS** — Primary metric for e-commerce (Return on Ad Spend)
2. **CPA/CPP** — Cost per Acquisition/Result
3. **CPC** — Cost Per Click
4. **CTR** — Click Through Rate (>1% = good benchmark)
5. **Frequency** — Too high = ad fatigue (>3.0 trigger refresh)
6. **Conversion Rate** — Landing page effectiveness

### ROAS Targets by Funnel Stage

| Stage | Target ROAS | Notes |
|-------|-------------|-------|
| Top of funnel (awareness) | 2-3x acceptable | Broader audience, lower intent |
| Middle funnel (consideration) | 3-4x target | Warm audiences |
| Bottom funnel (conversion) | 4-5x+ target | Hot retargeting |
| Retargeting specifically | 5-10x typical | High-intent users |

### Cost Benchmarks — Vietnam Market vs Global

| Metric | US/EU Benchmark | Vietnam Reality | Note |
|--------|-----------------|-----------------|------|
| **CPM** | $10-$50 | ₫20,000-80,000 (~$0.80-3.20) | 50 conv/week achievable at lower spend in VN |
| **CPC** | $0.50-$4.00 | Lower range | Depends heavily on industry/creative quality |
| **iOS ATT opt-out rate** | 70%+ | ~40-50% (lower upgrade cycle) | Pixel degradation less severe; CAPI still recommended |

### ROAS Attribution Gap Reality
- Hexclad: Meta in-platform ROAS 3.1x → true blended 2.1x (gap = full revenue turn)
- Chomps: 65% iPhone buyers → platform-reported data structurally unreliable without cross-check
- **Rule:** Cross-check with Northband/GA4/incrementality testing — single-source optimization = flying blind post-iOS

### 10 Strategic Lessons Summary

| # | Lesson | Key Takeaway |
|---|--------|-------------|
| 1 | Attribution Gap Defining Challenge | Meta dashboard ROAS ≠ true blended ROAS. Cross-check mandatory. |
| 2 | Creative Quality > Volume | Hexclad: 60→8 variants = performance improvement. Concept discipline > production budget. |
| 3 | Advantage+ Double-Edged Sword | ASC improves but needs guardrails (value-based audiences, creative diversity, LTV-calibrated goals). |
| 4 | First-Party Data = New Gold Standard | Server-side CAPI + post-purchase surveys + CRM seeding = winning triad. |
| 5 | Retargeting Changing Fundamentally | Hexclad: 60% retargeting conversions organic in 72h. Reallocate to prospecting + nurturing. |
| 6 | Less Targeting, Better Performance | Titan Driveways: 1 campaign → CPL -50%. Soda Spoon: 1 ad → ROAS 3.61x. Consolidation wins. |
| 7 | Cross-Channel Signal Flow | Channels as signal generators for each other (Google search intent → Meta audiences). |
| 8 | Attribution Windows Distort Reality | Trust post-purchase survey data when platform disagrees with it. |
| 9 | Incrementality Testing Non-Negotiable | Without it = optimizing on last-click fiction. Use Meta's free Conversion Lift tool. |
| 10 | Creative Briefing = Scientific Process | Best creative comes from actual customer language — specific, weird phrases people use when explaining why they bought. |

### Optimization Checklist (Weekly Review)

- [ ] Pixel + CAPI tracking all events? EMQ ≥6?
- [ ] ≥50 conversions/week per ad set?
- [ ] 3-5 creatives rotating per ad set? Refresh cadence on schedule?
- [ ] CBO enabled for multi-ad-set campaigns?
- [ ] Budget scale ≤20% every 3-4 days?
- [ ] Frequency <3.0 (no creative fatigue)?
- [ ] A/B test new hooks monthly?
- [ ] Cross-check ROAS with GA4/incrementality?

---

*Created: 2026-06-15 | Consolidated & restructured: 2026-06-20 | Sources: marketingadvice.ai, marketingagency.one, redclawey.com + 9 case studies + Reddit r/FacebookAds + X + The Drum*
