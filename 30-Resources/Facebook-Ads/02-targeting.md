---
title: "Audience Targeting"
slug: "audience-targeting"
category: resource
tags: [facebook-ads, meta-ads]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

﻿# 02 - Audience Targeting (Phan hoi audience)

## Core Audiences: Manual Targeting

### Demographic Targeting
- **Age:** 13-65+ (recommended 18-65 for most businesses)
- **Gender:** All / Male / Female
- **Education:** Level of education, fields of study
- **Job title:** Seniority, industry, specific roles
- **Life events:** Newly engaged, new job, birthday, recently moved
- **Parents:** By child age range

### Location Targeting
- **Geography:** Country, state/province, city, zip/postal code
- **Radius targeting:** X km/miles around specific point (address, landmark)
- **Location options:**
  - "People living in this location" (resident)
  - "Recently in this location" (visited within past 28 days)
  - "People recently in this location" (includes travelers)
- **Exclude locations:** Remove underperforming areas

**Pro tip for Vietnam:** Radius targeting works well for local businesses. City-level targeting for urban campaigns. Province-level for broader reach.

### Interest Targeting
- **Categories:** Fitness, Technology, Travel, Food & Drink, Fashion
- **Specific interests:** Brand names, hobbies, pages liked
- **Behaviors:** Purchase behavior, device usage, travel behaviors
- **Facebook Pages liked:** Page category targeting

**Building effective interest audiences:**
1. Start broad with category-level interests
2. Combine intersecting interests (Narrow further)
3. Use behavior data for purchase intent signals
4. Exclude irrelevant audiences to reduce waste

### Example: Targeting Stack
`
Age: 25-55
Gender: All
Location: Vietnam (Hanoi, HCMC, Da Nang)
Interests (Must match ALL):
  - E-commerce
  AND Online shopping
Behavior (Any matches):
  - Engaged shoppers
  - Facebook payments users (3 months)
Exclude:
  - Competitor page A
`

## Custom Audiences (Retargeting)

### Website Visitors (Pixel-based)
- All visitors (last 30/60/90/180 days)
- Specific page visitors (product pages, pricing page, blog)
- Time-based segments (last 7, 30, 90 days)
- Visitors who completed specific actions

**Best practice:** Segment by recency. Last 7 days = hot retargeting. 30-90 days = warm retargeting with different creative.

### Customer Lists
- Email lists upload (hash match)
- Phone numbers upload
- Account IDs (app users)
- Match rates typically 40-80% depending on list quality

**Match rate tips:** Use clean, validated email lists. Include phone numbers for higher match rates in Vietnam (phone-number-heavy market).

### App Activity
- People who installed app
- People who took specific in-app actions
- In-app purchase data
- Users who uninstalled (re-engagement campaigns)

### Engagement Audiences
- Video viewers (25%, 50%, 75%, 95%, 100% thresholds)
- Instagram profile engagers (liked, commented, followed)
- Lead form openers (opened but didn't submit)
- Event responders (interested/attending)
- Messenger conversation starters

**Best practices for Custom Audiences:**
1. Exclude converters from prospecting audiences (don't retarget buyers)
2. Retarget cart abandoners with urgency messaging
3. Segment by engagement level (hot vs warm)
4. Create lookalike audiences from best customer segments
5. Refresh source audiences every 30-90 days

## Lookalike Audiences (LAL)

### How they work
Meta finds people SIMILAR to your source audience based on:
- Demographics patterns
- Interest overlaps
- Behavioral similarities
- Device patterns

### Similarity Scale
- **1%:** Most similar to source (highest quality, smallest reach)
- **5%:** Medium similarity (balance of quality and reach)
- **10%:** Least similar (largest reach, lower quality)

### Best Source Audiences for LAL (ranked)
1. **Purchasers** (highest value customers) - MIN 1,000 people
2. **High-value purchasers** (top 25% spenders)
3. **Website purchasers** (Pixel data)
4. **Lead converters** (qualified leads only)
5. **Engaged email subscribers** (opened + clicked emails)
6. **Video viewers 95%** (high engagement proxy)

### Lookalike Best Practices
- Start with 1% LAL for quality, expand to 5% for scale
- Minimum 1,000 people in source audience (500 for international)
- Test different source audiences against each other
- Refresh source audience every 30-90 days (stale data = poor performance)
- Stack multiple 1% LALs as separate ad sets for broader reach
- Use location: same country as source audience

## Advantage+ Audiences (2026 AI Targeting)

### What it is
AI-driven broad targeting. Meta automatically finds best users based on:
- Your conversion data (Pixel/CAPI)
- Creative signals (what the ad content communicates)
- User behavior patterns across Facebook + Instagram

### How it differs from traditional targeting
| Traditional | Advantage+ |
|---|---|
| Narrow interest targeting | Broad (age/gender only) |
| Many ad sets per campaign | Fewer, broader ad sets |
| Manual optimization | AI automatic optimization |
| Interest/behavior dependent | Creative-driven signals |

### Requirements for Advantage+
- Minimum 50 conversions/week per ad set
- Pixel or CAPI properly configured
- At least some historical conversion data (28+ days recommended)

### When to use Advantage+
- Scaling existing campaigns with proven creative
- E-commerce stores with sufficient conversion data
- Reducing management time while improving performance
- 3-5x more effective than interest targeting WITH pixel data

## Audience Strategy by Funnel Stage

### Top of Funnel (TOFU) - Awareness/Prospecting
- Advantage+ Audiences (broad, AI-driven)
- Lookalike 1% from purchasers (if have data)
- Interest-based (for new accounts without pixel data)
- Video view audiences for warm-up

### Middle of Funnel (MOFU) - Consideration
- Website visitors 30-90 days (Custom Audience)
- Video viewers 50%+ (Custom Audience)
- Instagram engagers 90 days
- Lead form openers

### Bottom of Funnel (BOFU) - Conversion/Retargeting
- Website visitors 7-14 days (hot retargeting)
- Add to cart / Initiate checkout (abandoners)
- Previous purchasers (cross-sell/upsell)
- Engagement audiences 30 days

## Vietnam-Specific Tips
- Phone number lists have higher match rates than emails in VN
- Instagram engagement is high - use IG engagers for retargeting
- Local interest categories may differ from US categories
- Consider "Recently in location" for physical store campaigns
- Messenger is key conversion channel - Messages objective works well

## Key Takeaways
- Custom Audiences (retargeting) always outperform cold audiences
- Lookalike quality depends on source audience quality, not size
- Advantage+ Audiences + Pixel data = 3-5x better than interest targeting
- Always exclude converters from prospecting
- Segment retargeting by recency and engagement level

---
*Created: 2026-06-15 | Sources: marketingadvice.ai, marketingagency.one*