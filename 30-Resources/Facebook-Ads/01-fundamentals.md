---
title: "Facebook Ads Fundamentals — Campaign Structure"
slug: "facebook-ads-fundamentals"
category: resource
tags: [facebook-ads, fundamentals, campaign-structure]
status: active
type: reference
created: 2026-06-15
last_updated: 2026-06-15
---

# 01 - Facebook Ads Fundamentals (Nen tang)

## Meta Ads Hierarchy: 3-Tier Structure

`
Ad Account
+-- Campaign (Objective selection)
    +-- Ad Set 1 (Targeting + Budget + Placements)
    |   +-- Ad 1 (Creative A)
    |   +-- Ad 2 (Creative B)
    |   +-- Ad 3 (Creative C)
    +-- Ad Set 2 (Different audience/placement)
    |   +-- Ad 1, 2, 3...
    +-- Ad Set 3...
`

### 1. Campaign Level
- **Objective:** Chon mot muc tieu duy nhat cho campaign (khong mix objectives)
- **Campaign Budget:** Optional - CBO enabled
- **A/B Test Setup:** Experimental mode
- **Special ad categories:** Housing, Employment, Credit

**Golden rule 2026:** 1 campaign per objective. Never mix Sales + Leads + Traffic trong cung 1 campaign. Each objective optimizes differently.

### 2. Ad Set Level
- **Targeting:** Audience selection (demographics, interests, custom, lookalike)
- **Placements:** Automatic or manual placement selection
- **Budget & Schedule:** Daily/lifetime budget, start/end dates
- **Optimization & Delivery:** Conversion event, delivery type (standard/accelerated)
- **Pacing:** Frequency cap, bid strategies

**Golden rule 2026:** 1-3 broad ad sets per campaign. Data volume per ad set > narrow targeting precision. Algorithm needs 50+ conversions/week/ad set to exit learning phase.

### 3. Ad Level
- **Creative:** Images, videos, carousel cards, copy
- **Links & CTAs:** Destination URL, CTA button
- **Tracking:** Pixel events attached
- **Ad variations:** Dynamic creative optimization

## Campaign Objectives (7 categories theo funnel)

### Awareness
| Objective | When to use | Key metric |
|---|---|---|
| Brand Awareness | Nguoi hoi nho your brand, top-of-funnel reach | GRP, ad recall lift |
| Reach | Show ads to maximum number of people in budget | Cost per 1000 reached |

### Consideration
| Objective | When to use | Key metric |
|---|---|---|
| Traffic | Drive clicks to website/app/landing page | CPC, CTR, landing page views |
| Engagement | Post engagement, page likes, event responses | Engagement cost, reach |
| Video Views | Maximize video watches/completions | 3-second videos, ThruPlays |
| Lead Generation | Collect leads via in-platform forms | CPL, form opens |
| Messages | Start conversations Messenger/Instagram | Cost per conversation start |

### Conversion
| Objective | When to use | Key metric |
|---|---|---|
| Sales (Conversions) | Drive purchases + catalog sales | CPA, ROAS, purchase conversion value |
| Leads | Generate leads (contact info forms) | CPL, lead quality |

## Choosing the Right Objective

### Decision tree
`
What is your primary goal?
├── Get people to visit website/app -> Traffic
├── Collect emails/phone numbers -> Lead Generation
├── Sell products online -> Sales (Conversions)
├── Get page likes or post engagement -> Engagement
├── Start Messenger conversations -> Messages
├── Maximize video views -> Video Views
├── Build brand awareness -> Brand Awareness
└── Reach maximum people -> Reach
`

### Critical rules
1. **Algorithm optimizes for YOUR objective** - If objective is Sales, it finds purchasers. If Traffic, it finds clickers. Choose wisely.
2. **One objective per campaign** - Mixing objectives fragments data and confuses algorithm
3. **Optimization event must match business goal** - Don't optimize for link clicks if you want purchases
4. **Conversions > Link Clicks > Impressions** - Always optimize furthest down funnel possible

## Campaign Budget vs Ad Set Budget

### CBO (Campaign Budget Optimization)
- Budget set at campaign level
- Meta auto-distributes to best-performing ad sets
- Algorithmic optimization, not manual allocation
- Best for: multiple ad sets competing for same audience type
- **Min 2, max 6 ad sets** per CBO campaign
- Don't mix very different audiences in same CBO

### ABO (Ad Set Budget Optimization)
- Budget set per ad set
- Manual control over each ad set spend
- Best for: testing new audiences, equal budget distribution
- Useful when you need guaranteed minimum spend per test

### When to use which
- **CBO:** Scaling established campaigns, proven winners, 3+ ad sets
- **ABO:** Testing phase, equal distribution needed, limited ad sets (1-2)

## Key Takeaways
- 3-tier structure: Campaign (objective) > Ad Set (targeting/budget) > Ad (creative)
- 1 campaign per objective - never mix objectives
- Algorithm needs data volume: 50+ conversions/week/ad set to learn optimally
- Choose objective that matches actual business goal, not vanity metric
- CBO for scaling, ABO for testing

---
*Created: 2026-06-15 | Sources: marketingadvice.ai, marketingagency.one*