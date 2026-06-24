---
title: "SRS Flashcards — FB Ads Knowledge"
slug: "facebook-srs-flashcards"
category: resource
tags: [vault-maintenance]
status: reference
type: reference
created: 2025-12-01
last_updated: 2026-06-24
---

---

# 🃏 SRS Flashcards — FB Ads Knowledge

> Auto-imported from vault knowledge. Review via Obsidian Spaced Repetition plugin.

## High Priority (Must Know)

### Facebook Algorithm Core Signals

Facebook algorithm 2026 prioritizes engagement quality over raw volume?::Time spent viewing, saves, shares are top signals. Comments > reactions. Likes are least weighted. Key principle: "quality > quantity" — algorithm favors content that keeps users in app longer.

What is the primary ranking signal for Facebook feed in 2026?::1) Time spent viewing (longest weight), 2) Saves/bookmarks, 3) Shares with comments, 4) Comments on post, 5) Reactions. Raw engagement count matters less than engagement type and duration.

How does the Andromeda auction system work in 2026?::Three tiers: Tier 1 (80%+ win rate) = high relevance score + competitive bid. Tier 2 (60-80%) = balanced relevance/bid, needs monitoring. Tier 3 (<60%) = optimization needed — check CTR, frequency, creative freshness. Ad rank = Bid × Estimated Action Rate × Value.

What's the difference between broad and narrow targeting in 2026?::Broad: no interests/behaviors, let algorithm find audience via creative + pixel data. Best for scaling (2026 shift). Narrow: interest stacks, lookalikes, detailed targeting. Good for cold starts but limits learning phase. Broad wins when you have good creatives and pixel history.

### Bidding & Budget Strategy

What is the CBO scaling rule for Facebook ads?::Increase budget by max 20% per day per ad set. Scale winners vertically first (same audience, new creative), then horizontally (new audiences). Never increase budget on losing ad sets — pause or refresh creative instead.

What's the minimum daily budget for meaningful testing in Vietnam?::$10-20/day per ad set minimum for statistical significance. Conversion campaigns targeting high-value products: start $30+/day. Need at least 50 conversions/week/ad set to exit learning phase reliably.

When should you switch from CPC to CPM bidding?::Switch to CPM when CTR < 1% — gives algorithm freedom to find converters. Stick with CPC when CTR > 2%. For brand awareness: always use CPM or reach. For conversions: CPM generally outperforms CPC in 2026 due to Advantage+ algorithms.

What is frequency capping best practice?::Frequency < 3.0 for prospecting (fresh creatives needed). Frequency 1.5-2.5 for retargeting/remarketing. If frequency >4.0 within 7 days = creative fatigue, rotate new assets immediately. Retargeting audiences naturally have higher acceptable frequency.

### Metrics & Benchmarks

What's the ideal CPM range for Vietnam market in 2026?::FB Ads Vietnam: $0.50-$1.50 broad reach, $1.50-$3.00 targeted niche. If CPM >$4: audience too narrow or creative fatigue detected. Compare against industry benchmarks — e-commerce typically lower, education/healthcare higher.

What's the optimal ad frequency for conversion campaigns?::Frequency < 3.0 prospecting (rotate creatives). Frequency 1.5-2.5 retargeting. If frequency >4.0 within 7 days = creative fatigue, rotate new assets. Retargeting: accept higher frequency but cap at 6-8 over 30 days.

What CTR should I expect for Facebook ads in Vietnam?::Good CTR benchmark: 1.5-2.5% (link clicks). Below 1% = creative or targeting issue. Above 3% = strong performer, consider scaling. Video view CTR different metric — focus on link CTR for conversion campaigns.

What's a good ROAS target for Facebook ads in Vietnam?::Break-even ROAS = 1 / profit margin %. E-commerce: aim 200-400%+ (2-4x). Services: can tolerate lower initially (150-200%). Health/education often achieve higher due to LTV. Track blended ROAS across all campaigns, not per-campaign.

## Medium Priority (Important)

### Campaign Structure & Setup

How to structure a Facebook Ads campaign hierarchy?::Campaign (objective) > Ad Set (audience + budget + placement) > Ad (creative). One objective per campaign. Test one variable at a time between ad sets. Use CBO for scaled campaigns, ABO for testing.

What is Advantage+ Shopping Campaigns (ASC) best used for?::E-commerce product catalogs with clean pixel data. Best when you have 50+ conversions/week. Use ASC for scaling winners from manual campaigns, not cold starts. Combine with manual campaigns: test manually → scale via ASC.

When should I use video ads vs image ads in Vietnam?::Video ads outperform on brand awareness and top-of-funnel (TOFU). Image ads better for direct response and retargeting. Vietnam market: short-form vertical video (<15s) performs best. Static images with strong hook work well for bottom-funnel conversion.

What's the ideal campaign testing structure?::Test 3-5 creatives per ad set, not more. Keep audience constant while testing creative (isolate variable). Budget $10/ad set/day minimum. Run tests 4-7 days before deciding winners/losers. Kill underperformers at day 3 if <0.5% CTR or CPA >2x target.

### Pixel & Tracking

What's the recommended pixel implementation for 2026?::Conversions API (CAPI) + browser pixel combined. Server-side tracking essential after iOS 17+ ATT changes. Verify events in Events Manager daily. Match rules: email, phone, fbc_id for server-client matching.

How many conversion events should a business track?::Track 3-5 key actions max: Purchase (primary), Add to Cart, Initiate Checkout, Lead Form Submit, Page View (secondary). Too many events dilutes optimization data. Facebook needs ~50 conversions/week/event for reliable learning.

What are custom conversions vs standard events?::Standard events: pre-built FB tracking (Purchase, Lead, etc.). Custom conversions: rule-based triggers from URL/path/query parameters. Use standard events when possible — better integration with Advantage+ algorithms. Custom conversions for specific landing pages or checkout steps.

### Creative Strategy

How often should I refresh ad creatives in Vietnam?::Prospecting: rotate every 7-14 days (frequency-driven). Retargeting: can run longer (14-30 days). Create new creative variations weekly during active campaigns. A/B test formats: UGC-style > polished studio for cold traffic in Vietnam market.

What's the best ad copy structure for Facebook in Vietnam?::Hook (first 3 lines visible) → Problem/Pain point → Solution/Value prop → Social proof → CTA. Keep first line under 120 chars (before "See more" fold). Use Vietnamese natural language, not formal marketing speak. Emojis sparingly: 1-2 per post max.

What ad formats perform best for e-commerce in Vietnam?::Carousel (product showcase) > Single Image (direct offer) > Collection (shoppable catalog) > Video (awareness). For retargeting: single image with strong discount hook works best. Carousel needs high-quality product photos minimum 5-10 items.

## Low Priority (Nice to Know)

### Optimization Tips

Quick tip: When should you switch from CPC to CPM bidding?::When your CTR < 1% — switching to CPM gives algorithm more freedom to find converters. When CTR > 2%, stick with CPC or optimize creative first. CPM generally performs better in 2026 Advantage+ era for conversion campaigns.

What is a lookalike audience (LAL) and when to use it?::Lookalike audiences: Facebook finds users similar to your seed list (pixel data, customer list). Use 1-3% similarity for highest quality. Refresh LAL sources quarterly with new pixel events or uploaded customer lists. Combine with broad targeting for best results.

How does ad scheduling affect performance in Vietnam?::Vietnam peak engagement hours: 7-9 AM, 12-1 PM (lunch), 7-10 PM. Ad scheduling matters less in 2026 due to Advantage+ automated delivery. Only use schedule for time-sensitive offers or service businesses with limited support hours.

What's the impact of iOS updates on Facebook ads?::iOS 17+ ATT: ~30% traffic still opted out. CAPI becomes essential, not optional. Server-side tracking recovers 20-40% lost conversions vs browser-only. First-party data collection (email/phone capture) increasingly important for matching.

### Tool & Platform Notes

What's the difference between Facebook Ads Manager and Business Suite?::Ads Manager: full ad creation, targeting, bidding, reporting — use for running campaigns. Business Suite: lighter interface, scheduling organic posts + boosting — use for simple promotions and content planning. Full campaigns always in Ads Manager.

When should I use Facebook Lead Forms vs landing pages?::Lead forms (instant forms): higher volume, lower quality leads. Best for awareness/lead gen campaigns with tight budgets. Landing pages: lower volume, higher qualified leads. Essential for high-ticket products/services (>2M VND). Test both and compare cost per QUALIFIED lead, not just cost per lead.

---
*SRS cards generated: 2026-06-20 by Smee — Layer 4 (Spaced Repetition)*
*Total cards: ~30 across high/medium/low priority tiers*
*Tag these notes with #flashcard for SRS plugin auto-import*
