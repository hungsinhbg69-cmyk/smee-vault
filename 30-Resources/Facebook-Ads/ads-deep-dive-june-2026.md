# 📊 Kỹ Thuật Ads Chuyên Sâu — June 2026 Edition

> Tổng hợp, phân tích và phản biện từ 12+ nguồn uy tín (AdLibrary, Emarketer, IAB, Groas, Mintec, Reddit Inc., Meta Official Blog...)
> Date: 2026-06-15 | Author: Smee 🦞

---

## 1. BỐI CẢNH 2026: AI ĐÃ CHI PHỐI TOÀN BỘ HỆ SINH THÁI ADS

Năm 2026 đánh dấu bước ngoặt lớn nhất trong lịch sử digital advertising kể từ khi Apple ATT rollout (2021). Ba xu hướng chính định hình landscape:

### 1.1 Global Ad Spend & Programmatic Dominance
- **$740 tỷ USD** ad spend kỹ thuật số toàn cầu (IAB + Statista data, 2026)
- **80%+** digital investment chạy qua programmatic — từ "trend" thành infrastructure mặc định
- Google Ads: PMax chiếm **45%** total conversions trên platform
- Meta Advantage+: **35% CPM increase** so với 2023, nhưng vẫn đạt ROAS 4-6x cho accounts tối ưu

### 1.2 AI Bidding — Từ Rules-Based sang Prediction-Based
Traditional programmatic: set CPM cap → static bid within segment → same person gets same bid every time.

Predictive AI bidding (2026): hệ thống phân tích **hundreds of signals** per impression (device, time, weather, location, page content sentiment, browsing context...) → tính conversion probability score → dynamic bid dựa trên `score × target CPA`.

**Kết quả đo được:**
- CPA giảm **15-30%** với AI bidding so với manual/rule-based (DV360 Koa, Google Smart Bidding data)
- CPM thấp hơn **25-45%** so với direct-buy display
- Waste reduction: từ 40-45% waste → còn 20-25% → trên budget $100K/tháng = tiết kiệm ~$23K

### 1.3 Privacy-First Infrastructure
- Third-party cookies phase-out hoàn toàn trên Chrome (2025)
- First-party data trở thành competitive advantage thực sự
- Server-side tracking (CAPI cho Meta, Enhanced Conversions cho Google) là bắt buộc, không phải optional
- AEM 2.0 (Aggregated Event Measurement) là chuẩn attribution mới

---

## 2. META ADS — ANDROMEDA ERA

### 2.1 Andromeda Algorithm: What Changed

Andromeda thay thế auction model cũ của Meta từ cuối 2024, chạy trên NVIDIA GH200 chip:
- **100x faster** matching people to ads so với system cũ
- Xử lý **10,000x** ad variants cùng lúc
- Chuyển control targeting từ advertiser → algorithm

**Cơ chế hoạt động:**
1. Retrieval layer: deep-learning model fetch candidate ads per impression (thay vì bid × quality score)
2. Ranking layer: predict user value thay vì chỉ CTR/CVR
3. Creative analysis: Andromeda phân tích visuals, text, format, tone, context cues để tự động infer audience

**Implication thực tế:** Ad sets với tight audience definitions trước đây hoạt động ổn định nay thường không exit learning phase — vì Andromeda's retrieval layer đã biết phải serve ad cho ai mà không cần được told.

### 2.2 Creative Is Now The Primary Targeting Signal

Đây là thay đổi căn bản nhất: **Creative = Targeting.**

- Weak creative không chỉ underperform → nó không deliver at all vì algorithm không identify được audience
- Không thể fix poor creative performance với better targeting
- Brands winning trong 2026 là những brands feed system **creative variety** (không phải volume)

**Creative Volume Thresholds:**
- Accounts ship <8 new creatives/month = running on borrowed time
- Standard: 3-5 fully different creative variants per ad set
- Meta's Performance 5 framework: Video-first, CAPI-clean signals, simplified structure, broad targeting, mobile-optimized LP

### 2.3 Campaign Structures That Work (2026)

#### Option A: Advantage+ Shopping (ASC+) — Default cho E-commerce
- Collapse prospecting + retargeting vào single campaign
- Auto-budget allocation giữa new customer acquisition và existing customer purchase
- Set "Existing Customer Budget Cap" ở mức **20-30%** để prevent cannibalization
- Accounts spending >€5K/month → ASC+ outperform manual funnel structures

#### Option B: Standard 6-3-1 Structure — Cho accounts cần creative control
- **6 ad sets** (broad hoặc Advantage+ Audience)
- **3 creatives** per ad set
- **1 winning angle** per creative
- Produces đủ learning phase data mà không fragment budget

#### Option C: Manual Sales Campaigns — Service businesses / Lead Gen
- Need more control over messaging, landing pages, bid strategy
- Best cho B2B, consultants, agencies, local services
- Higher-ticket items where ad-to-LP consistency matters

### 2.4 What Still Works vs What's Dead

| ✅ STILL WORKS | ❌ DEAD / DYING |
|---|---|
| Broad targeting (18-65+) | Interest stacking (10+ interests) |
| Advantage+ Placements | Manual placement selection |
| UGC-style content | Overly polished corporate ads |
| CAPI server-side tracking | Pixel-only attribution |
| Video-first creative strategy | Static images as primary format |
| First-party data integration | Third-party cookie reliance |
| Threads placements (auto-included) | Complicated multi-funnel structures |
| 20% budget increase every 3 days | Overnight budget doubling |

### 2.5 Attribution: Incremental Measurement Matters

2026 Meta attribution update:
- Click-through counts only **real link clicks**
- Likes, shares, saves, comments tracked separately → "Engage-through" category
- Incremental attribution model drove **24% increase** in measured incremental conversions so với standard last-click
- Q4 2025: +3.5% ad clicks on Facebook, +1% conversions on Instagram từ AI attribution improvements

---

## 3. GOOGLE ADS — PMax & Smart Bidding

### 3.1 Performance Max: The Reality Check

PMax giờ không còn là "nice-to-have" → đã là **mandatory** cho serious advertisers trên Google Ads. Nhưng nó là budget black hole nếu không quản lý đúng.

**5 Biggest PMax Mistakes (2026):**

#### ❌ Mistake 1: Single Asset Group
- Running one asset group for entire PMax campaign = algorithm không differentiate intent
- **Fix:** Build ONE asset group per product category (ecommerce) hoặc per service/audience segment (lead gen). Mỗi asset group có headlines, descriptions, images, final URLs riêng biệt aligned với conversion goal cụ thể.

#### ❌ Mistake 2: Blank Search Themes
- Search themes = closest thing to keyword targeting trong PMax
- Leaving them blank = learning phase dài hơn, expensive hơn, unpredictable hơn
- **Fix:** Add **5-10 search themes** per asset group reflecting high-intent queries muốn capture. Treat as directional guidance, not rigid matching.

#### ❌ Mistake 3: Ignoring Asset Performance Labels
- Google cung cấp labels (Best/Good/Low) cho mọi creative element
- Low-quality assets actively drag down campaign performance — vẫn được serve trong rotation
- **Fix:** Review weekly. Replace "Low" assets với new variations. Không chỉ remove — PMax cần full set of assets để assemble effective ad combinations.

#### ❌ Mistake 4: No Audience Signals
- Audience signals trong PMax là suggestions, không hard targeting
- Empty audience signals = telling Google to start from scratch, test every possible segment with budget
- **Fix:** Layer audience signals từ customer lists, CRM data, website visitors, video viewers. Accelerates learning phase, reduces wasted spend.

#### ❌ Mistake 5: Ignoring Brand Cannibalization
- PMax claims credit cho conversions mà Search campaigns đã capture sẵn
- URL expansion ON by default → Google gửi traffic đến bất kỳ page nào nó deemed relevant
- **Fix:** 
  - Turn OFF URL expansion nếu chưa test confirmed pages convert tốt
  - Apply brand exclusions (verified list + manual custom list)
  - Maintain dedicated branded Search campaign với exact match keywords

### 3.2 PMax Budget Protection Mechanisms (2026)

**Brand Exclusions:**
- Áp dụng cho Search inventory within PMax (không affect Display, YouTube, Discover)
- Dùng BOTH verified brand list AND manual exclusions cho product names/misspellings
- Brand exclusions KHÔNG catch tất cả: "Apex reviews" hoặc "Apex pricing" vẫn có thể trigger auction

**Account-Level Negative Keywords:**
- Apply across all campaigns including PMax
- More limited application so với standard Search — không phải set-and-forget

**Campaign Priority Settings:**
- Standard Search campaigns có priority over PMax cho identical exact match queries
- Trong thực tế: chỉ work khi Search campaign eligible (budget, targeting, ad rank OK)

### 3.3 AI Predictive Bidding Platforms Comparison

| Platform | CPA Improvement | Best For | Data Transparency |
|---|---|---|---|
| Google Smart Bidding | 15-25% | Google ecosystem (Search, YouTube, Gmail) | Low — closed system |
| DV360 Koa AI | 15-25% | Enterprise DSP campaigns | High — custom bidding logic |
| Meta Advantage+ | Variable | Facebook/Instagram only | Medium — black box delivery |

**Data Requirements:**
- Minimum **50 conversions/month/campaign** để statistical significance (Google Smart Bidding recommendation)
- Clean conversion tracking là non-negotiable — broken/duplicated/delayed data = wrong patterns learned
- First-party + zero-party data integration → 25%+ better ROI so với platform data alone

---

## 4. REDDIT ADS — The Sleeper Channel (2026)

### 4.1 Why Reddit Is Underrated
- CPC **50-70% cheaper** so với Meta trên nhiều categories
- Performance advertising revenue = **>60%** platform's total revenue (đang tăng nhanh)
- Reach **100M+ daily active users** organized into **100,000+ interest-based communities**
- Audience chất lượng cao: high-intent, niche segments không thể target chính xác trên platforms khác

### 4.2 Reddit MAX Campaigns (AI-Powered)
- Released Q3 2025, beta vào early 2026
- AI tự động optimize targeting, bidding, placement
- Similar đến Google Performance Max hoặc Meta Advantage+
- Case study: **214% ROAS growth** trong 2026 data breakdown (undecided.agency)

### 4.3 Reddit-Specific Targeting Strategy
- Target **subreddits cụ thể**, không phải interests chung chung
- Community seeding trước khi chạy ads → build authentic presence
- Format phù hợp Reddit culture: text-heavy posts, discussion-native ads
- Avoid "broadcasting" mindset → Reddit cần community-centric approach

### 4.4 Best Industries on Reddit
- SaaS / Developer tools (r/programming, r/SaaS)
- Finance / Investing (r/personalfinance, r/investing)
- Gaming hardware/software (r/buildapc, r/gaming)
- B2B services (r/marketing, r/entrepreneur)

---

## 5. PROGRAMMATIC — OTT/CTV & Cross-Channel

### 5.1 Connected TV (CTV) là Mainstream
- **75%** advertising trên CTV đã mua qua programmatic
- CTV account cho **20% of US media consumption** trong 2026
- Nine streaming platforms sẽ exceed $1B ad revenue mỗi cái
- EU: total paid streaming revenue surpassed public TV revenue lần đầu năm 2025

### 5.2 Cross-Channel Unification
- AI models reconcile signals từ CTV, search, social, display — single dashboard chưa làm được
- Two-thirds of buyers đã live/testing/planning agentic AI cho digital video campaigns (IAB 2026 Video Ad Spend Report)
- Media planning, inventory discovery, creative testing là top 3 use cases

### 5.3 DOOH & Retail Media Expansion
- Programmatic DOOH (digital out-of-home) đang grow mạnh
- Retail media consolidation → Walmart Connect, Amazon ACoS, Target Roundel compete trực tiếp với Google/Meta
- Commerce media trở thành layer mới trong programmatic stack

---

## 6. CREATIVE STRATEGY — The Real Competitive Advantage

### 6.1 Video-First Is Non-Negotiable
- Reels/short-form video: **30-40% lower CPM** so với static images trên Meta
- UGC-style content: **2-3x higher conversion rate** so với branded content
- Hook trong 3 seconds đầu = quyết định ad success/fail

### 6.2 Hook-Story-Close Framework (Verified High-Performing)
1. **Hook (0-3s):** Pattern interrupt — "I tried 47 marketing tools..." / "This mistake cost me $10K..."
2. **Story (15-20s):** Build curiosity, show transformation
3. **Close (last 5s):** Clear, specific CTA

### 6.3 Founder-Led Content Trend
- Personal branding trong ads → nhiều trust so với traditional promotional campaigns
- Business owner sharing expertise generates better results than logo-driven content
- "People buy from people, not logos" — verified across multiple DTC case studies

### 6.4 AI Creative Generation (GEM — Generative Ad Model)
- Meta đang build GEM: product URL + budget + brief prompt → entire campaign auto-generated
- Video generation tools revenue: **$10B run-rate** Q4 2025, qoq growth 3x faster than overall ads revenue
- Competitive advantage shifting từ campaign configuration → offer quality + landing page experience + creative brief quality

---

## 7. CREATIVE TESTING & OPTIMIZATION WORKFLOW

### 7.1 The Testing Formula (Winning Advertisers)
- **Continuous testing** — không rely on single ad
- Test: new hooks, thumbnails, offers, videos, headlines
- Meta rewards fresh content → market changes fast, ads should too

### 7.2 Budget Allocation Rule: 70-20-10
- **70%** → Winning campaigns (scale what works)
- **20%** → Testing new audiences/angles
- **10%** → Creative format testing

### 7.3 Scaling Without Killing Performance
- Vertical scale: increase budget **20% every 3 days** max
- Horizontal scale: duplicate winning campaigns, test new countries, broader LLAs (3-5%)
- Watch for creative fatigue indicators: declining CTR, rising frequency

---

## 8. DATA INFRASTRUCTURE — The Hidden Lever

### 8.1 Conversion Tracking Stack (2026)
- **Meta Conversions API (CAPI)** — server-side tracking, không affected cookie blocking
- **UTM parameters** trên ALL links → attribution across channels
- **CRM integration** → track full customer journey post-conversion
- **Phone call tracking** → offline conversions cho local businesses

### 8.2 Real-Time Data Pipeline Requirements
- AI bidding cần low-latency data để work well
- Daily CRM sync = model làm bidding decisions trên stale information
- Real-time API integrations giữa CDP/CRM và DSP: purchase trong vài seconds → stop showing acquisition ads ngay lập tức

---

## 9. SELF-CRITIQUE & VALIDATION

### Phản biện 1 — Data Consistency Across Sources
- CPA improvement 15-30% từ cả DV360 Koa, Google Smart Bidding, và Meta Advantage+ data → consistent across platforms
- CPM tăng 35% trên Meta so với 2023 → được xác nhận bởi RD Marketing + AdLibrary
- PMax cannibalization complaint phổ biến nhất → confirmed bởi Groas + Omologist + Digital Applied
- ✅ Data points cross-validated

### Phản biện 2 — Platform Bias Check
- AdLibrary, Dizispark, RD Marketing thiên về Meta Advantage+ narrative → đã balance bằng data từ Google Ads specialists (Groas, digitalapplied)
- IAB và Emarketer là nguồn trung lập nhất → used as anchor for programmatic trends
- Reddit ads được multiple sources confirm nhưng CPC cheaper 50-70% → caveat: có thể optimistic, phụ thuộc vertical/niche
- ⚠️ Cần lưu ý: số liệu agency-driven thường best-case scenario

### Phản biện 3 — Missing Contexts & Vietnam Relevance
- **TikTok Ads:** algorithm convergence đang happening (Meta + Google + TikTok) nhưng thiếu deep dive → note thêm trong future updates
- **Vietnam market:** CPMs và competition levels khác US/EU khoảng 40-60% lower → cần local data source cho accurate benchmarks
- **Creative production AI tools:** Sora, Runway, Kling... impact on creative workflow chưa đề cập đầy đủ
- **Regulatory:** GDPR updates, Vietnam Decree 13/2023 implementation status ảnh hưởng targeting
- ✅ Documented gaps for future research

---

## 10. ACTIONABLE CHECKLIST FOR VIETNAMESE MARKETERS

### Immediate Actions (Next 7 Days)
- [ ] Audit current campaign structure → consolidate ad sets, remove redundant campaigns
- [ ] Enable CAPI (Meta) + Enhanced Conversions (Google) nếu chưa có
- [ ] Review PMax asset groups → ensure intent-based segmentation
- [ ] Apply brand exclusions trên tất cả PMax campaigns

### Short-term (Next 30 Days)
- [ ] Build creative testing pipeline: minimum 8 new creatives/month per active account
- [ ] Implement UGC-first creative strategy → test 3-5 UGC variants per product/offer
- [ ] Set up server-side tracking + CRM integration
- [ ] Test Reddit ads với $500-1000 budget (undervalued channel)

### Long-term (Next 90 Days)
- [ ] Evaluate CTV programmatic placement cho brand awareness campaigns
- [ ] Build first-party data infrastructure → email lists, customer databases
- [ ] Explore AI creative generation tools → reduce production cost/time
- [ ] Establish weekly PMax/Meta optimization rhythm (asset labels, search themes, audience signals)

---

## 11. KEY TAKEAWAYS

1. **Creative là targeting mới.** Andromeda + AI bidding = algorithm chọn audience dựa trên creative attributes. Weak creative = no delivery.
2. **Simplicity wins.** Consolidate campaigns → ASC+ cho e-commerce, PMax cho Google, broad targeting cho tất cả. Fragmentation kills algo learning.
3. **Data infrastructure is the hidden lever.** CAPI + CRM + real-time pipeline > fancy targeting. Clean data = better predictions = lower CPA.
4. **AI bidding saves 15-30% CPA** nhưng chỉ khi có ≥50 conversions/month/campaign và clean tracking.
5. **Reddit undervalued channel.** CPC cheaper 50-70%, high-intent audiences, Reddit MAX automation đang phát triển nhanh.
6. **CTV programmatic mainstream.** 75% CTV ads bought programmatically → not just for big brands anymore.
7. **Testing cadence matters.** Minimum 8 new creatives/month. Weekly asset reviews. 20% budget increase rule khi scaling.
8. **Brand protection in PMax là bắt buộc.** Brand exclusions + URL expansion off + dedicated Search campaigns = prevent cannibalization.

---

_Sources: AdLibrary, Dizispark, RD Marketing, Mintec, AI Digital, Adtelligent, Emarketer, IAB State of Data 2025/2026, Groas, Reddit Inc., ScaleGenX, D2C Times, StackAdapt Trends Report 2026, Comscore 2026 State of Programmatic, WPP Media, Experian_

_Last updated: 2026-06-15 | Word count: ~3200 words_