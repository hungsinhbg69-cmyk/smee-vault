---
title: "Metrics & Benchmarks"
slug: "metrics-benchmarks"
category: resource
tags: [facebook-ads, meta-ads]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

﻿# 08 - Metrics & Benchmarks (KPIs + Cost benchmarks 2026)

## Key Metrics Definitions

### Cost Metrics
| Metric | Full name | Formula | What it tells you |
|---|---|---|---|
| CPM | Cost per Mille | (Spend / Impressions) x 1,000 | How expensive the audience/placement is |
| CPC | Cost Per Click | Spend / Link Clicks | Cost to drive traffic |
| CPL | Cost Per Lead | Spend / Leads | Cost per lead generation |
| CPA | Cost Per Acquisition | Spend / Purchases | Cost per customer/sale |
| CPP | Cost Per Result | Spend / Total Results | Cost per any optimization event |

### Performance Metrics
| Metric | Formula | What it tells you |
|---|---|---|
| CTR (Link) | Link Clicks / Impressions | How compelling your ad is |
| CTR (All) | All Clicks / Impressions | Total engagement rate |
| Conversion Rate | Conversions / Link Clicks | Landing page effectiveness |
| ROAS | Revenue / Ad Spend | Revenue efficiency |
| Frequency | Impressions / Unique Reach | Ad fatigue indicator |

### Quality Metrics
| Metric | Benchmark | Action if below |
|---|---|---|
| CTR (Link) | > 1% | Improve creative/copy |
| Landing Page CVR | > 2% (e-com) | Optimize landing page |
| Frequency | < 3.0 | Rotate new creatives |
| Video 3-sec Views Rate | > 25% | Improve first 3 seconds |
| Purchase CVR from Pixel | > 1-3% (varies) | Check pixel + checkout flow |

## Cost Benchmarks by Market (2026)

### United States (reference market)
| Metric | Range | Notes |
|---|---|---|
| CPM | - | Varies heavily by industry |
| CPC | .50-.00 | Broad targeting = lower end |
| CPL | - | B2B at higher end, consumer lower |
| CPA (e-com) | - | Depends on AOV |
| ROAS average | 2-4x | Profitable if margin supports it |

### Vietnam market (estimated)
| Metric | Range | Notes |
|---|---|---|
| CPM | - | Much lower than US |
| CPC | .05-.30 | Competitive market pricing |
| CPL | .50- | Very competitive lead costs |
| Frequency threshold for fatigue | > 2.5-3.0 | Similar to global |

### Seasonal variations (US)
| Period | CPM multiplier | Notes |
|---|---|---|
| Q1 (Jan-Mar) | 1.0x (baseline) | Cheapest quarter |
| Q2 (Apr-Jun) | 1.2-1.5x | Gradual increase |
| Q3 (Jul-Sep) | 1.3-1.5x | Back-to-school prep |
| Q4 (Oct-Dec) | 2.0-3.0x | Holiday season, highest costs |

### Industry variations (US CPM ranges)
| Industry | CPM range | Why |
|---|---|---|
| E-commerce | - | Competitive, broad audience |
| SaaS/Tech | - | High-value audiences |
| Real Estate | - | Expensive leads justify cost |
| Finance/Insurance | -+ | High LTV customers |
| Travel/Hospitality | - | Seasonal, broad appeal |
| Education | - | Moderate competition |

## ROAS Benchmarks by Funnel Stage

### Top of Funnel (Awareness/Prospecting)
- **Acceptable ROAS:** 2-3x
- **Goal:** Find profitable audiences and creatives
- **Timeframe:** 14-30 days to evaluate
- **Note:** TOFU campaigns often show delayed ROI through retargeting

### Middle of Funnel (Consideration)
- **Target ROAS:** 3-4x
- **Goal:** Nurture warm audiences toward conversion
- **Key metric:** Add to cart / Initiate checkout rate
- **Timeframe:** 7-14 days to evaluate

### Bottom of Funnel (Retargeting/Conversion)
- **Target ROAS:** 5-10x+
- **Goal:** Convert warm audiences at lowest CPA
- **Key metric:** Cart abandonment recovery rate
- **Timeframe:** Immediate to 7 days

### Overall blended ROAS target
- **Break-even ROAS:** 1 / Profit Margin % (e.g., 50% margin = 2.0x break-even)
- **Profitable ROAS:** Break-even x 1.3 (30% buffer for overhead)
- **Scaling ROAS:** 4-5x+ (sufficient profit to reinvest in ads)

## Conversion Rate Benchmarks

### By industry (e-commerce landing pages)
| Industry | CVR benchmark | Notes |
|---|---|---|
| Fashion/Apparel | 1.5-3% | Highly competitive, visual-driven |
| Electronics | 2-4% | Higher consideration, longer decision |
| Beauty/Skincare | 2-5% | Strong impulse purchase potential |
| Home/Garden | 1.5-3% | Higher AOV, longer consideration |
| Health/Supplements | 2-4% | Trust-dependent, review-heavy |
| Digital products | 3-8% | Lower friction, instant delivery |

### By traffic source
| Source | CVR benchmark | Why |
|---|---|---|
| Facebook Ads (warm) | 3-5% | Retargeting, high intent |
| Facebook Ads (cold) | 1-2% | Prospecting, lower intent |
| Organic social | 2-4% | Existing audience trust |
| Search ads | 4-8% | High purchase intent |

## Frequency Analysis

### Frequency tiers and actions
| Frequency | Status | Action |
|---|---|---|
| 1.0-1.5 | Optimal | Keep running, monitor CPA |
| 1.5-2.5 | Acceptable | Watch for performance decline |
| 2.5-3.0 | Warning | Prepare new creative variations |
| 3.0-4.0 | Fatigue building | Rotate new creatives immediately |
| 4.0+ | Severe fatigue | Replace all creatives, consider audience refresh |

### Frequency by campaign type
- **Retargeting:** Accept higher frequency (2-4) due to smaller audience
- **Prospecting:** Keep lower (1.5-2.5) for broader reach
- **Brand awareness:** Can tolerate higher frequency (3-5) for message reinforcement

## Facebook Ads API - Core Objects Reference

### Campaign objects
| Object | Purpose | Key fields |
|---|---|---|
| Campaign | Top-level container | id, name, objective, status, campaign_group_id (CBO), daily_budget/lifetime_budget |
| AdSet | Targeting + placement + budget | id, name, targeting, placements, optimization_guide, daily_budget/lifetime_budget, start_time/end_time |
| Ad | Creative content | id, name, creative, status, delivery_status |

### Campaign Objectives (objective field values)
- BRAND_AWARENESS
- AWARENESS
- TRAFFIC
- ENGAGEMENT
- LEADS
- APP_INSTALLS
- VIDEO_VIEWS
- MESSAGE
- CONVERSIONS
- CATALOG_SALES
- STORE_TRAFFIC
- SALES (newer value for conversions)

### AdSet targeting structure (JSON)
`json
{
  "targeting": {
    "geo_locations": {
      "countries": ["VN"],
      "regions": [],
      "cities": []
    },
    "age_min": 25,
    "age_max": 55,
    "genders": [1],
    "interests": [{"id": "interest_id", "name": "Interest Name"}],
    "behaviors": ["behavior_id"],
    "custom_audiences": ["custom_audience_id"]
  }
}
`

### Standard events (for pixel/CAPI)
- PAGE_VIEW
- VIEW_CONTENT
- SEARCH
- START_TRIAL
- ADD_TO_CART
- ADD_PAYMENT_INFO
- INITIATE_CHECKOUT
- PURCHASE
- LEAD
- COMPLETE_REGISTRATION
- CONTACT
- CUSTOMIZE_PRODUCT
- DONATE
- FIND_LOCATION
- Schedule
- SUBSCRIBE
- START_CHECKOUT

### Insights API fields (key metrics)
| Field | Returns | Level |
|---|---|---|
| impressions | Total ad impressions | campaign/adset/ad/criteria |
| spend | Ad spend in currency | campaign/adset/ad/criteria |
| clicks | All clicks | campaign/adset/ad/criteria |
| link_clicks | Link clicks only | campaign/adset/ad/criteria |
| ctr | Click-through rate | campaign/adset/ad/criteria |
| cpc | Cost per click | campaign/adset/ad/criteria |
| cpm | Cost per 1,000 impressions | campaign/adset/ad/criteria |
| actions | Conversion events by type | campaign/adset/ad/criteria |
| cost_per_action_type | CPA by event type | campaign/adset/ad/criteria |
| purchase_roas | Return on ad spend (purchase) | campaign/adset/ad/criteria |
| results | Total optimization results | campaign/adset/ad/criteria |

### Insights API example query
`
GET /act_{AD_ACCOUNT_ID}/insights?level=adset&fields=adset_name,spend,impressions,clicks,link_clicks,ctr,cpc,cpm,actions,purchase_roas&date_preset=last_7d
`

### Campaign Budget Optimization fields
- campaign_bid_amount: CBO budget (at campaign level)
- bid_type: LOWEST_COST_WITHOUT_CAP (default)
- conversion_rate_trend: algorithm confidence indicator

## Quick Reference: Metrics Dashboard

### Daily monitoring (5 min check)
- Spend vs daily target
- CPA vs target CPA
- Top 3 performing ads
- Any "Learning Limited" ad sets

### Weekly review (30 min)
- ROAS trend (7-day rolling average)
- Creative fatigue indicators (frequency, CTR decline)
- Learning phase status for all ad sets
- Budget pacing against monthly plan

### Monthly strategy (2 hours)
- Full funnel performance analysis
- New creative concept planning
- Audience expansion opportunities
- Competitor creative research
- Pixel data quality audit

## Key Takeaways
- ROAS is king - track it, optimize for it, scale with it
- CTR > 1% is good, CPA/ROAS are real success metrics
- Frequency > 3.0 = ad fatigue, rotate creatives
- Q4 costs 2-3x higher - plan budget accordingly
- Vietnam CPM much lower than US (-5 vs -20)
- Break-even ROAS = 1 / Profit Margin

---
*Created: 2026-06-15 | Sources: marketingadvice.ai, marketingagency.one*