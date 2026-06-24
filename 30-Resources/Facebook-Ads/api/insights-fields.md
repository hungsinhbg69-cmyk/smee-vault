---
title: "Fb Api Insights Fields Reference"
slug: "fb-api-insights-fields-reference"
category: reference
tags: [vault-maintenance, facebook-ads]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---


# API Insights Fields (Reporting + Metrics)

## Meta Graph API - Insights Endpoint

### Base endpoint
`
GET /act_{AD_ACCOUNT_ID}/insights
GET /{CAMPAIGN_ID}/insights
GET /{ADSET_ID}/insights
GET /{AD_ID}/insights
`

### Required parameters
- level: campaign | adset | ad | criteria (required)
- ields: comma-separated metric fields (required)

### Optional parameters
- date_preset: today | yesterday | last_7d | last_30d | this_month | last_month | lifetime | custom
- since / until: custom date range (ISO 8601)
- iltering: JSON array of filter conditions
- reakdowns: array of breakdown dimensions
- sort: field to sort by
- limit: results per page

## Key Insight Fields

### Cost fields
| Field | Description | Example value |
|---|---|---|
| spend | Ad spend in minor currency units (cents) | 5000 = .00 |
| cpm | Cost per 1,000 impressions | 8.50 |
| ecpm | Effective CPM (includes all placements) | 9.20 |
| cost_per_total_action | Average cost per all actions | 3.50 |

### Click fields
| Field | Description | Example value |
|---|---|---|
| clicks | Total clicks (all types) | 1500 |
| link_clicks | Clicks on links only | 800 |
| unique_clicks | Unique clickers | 650 |
| ctr | Click-through rate (clicks/impressions) | 0.025 |
| click_through_rate | Link CTR specifically | 0.015 |
| cost_per_link_click | CPC for link clicks | 0.63 |
| cost_per_unique_click | Cost per unique clicker | 0.77 |

### Conversion fields
| Field | Description | Example value |
|---|---|---|
| actions | Array of conversion events by type | See breakdown below |
| cost_per_action_type | CPA for each event type | See breakdown below |
| purchases | Number of purchase conversions | 25 |
| purchase_roas | Return on ad spend (purchase) | 3.85 |
| results | Total optimization results | 150 |
| cost_per_result | Average cost per optimization result | 2.00 |

### actions field breakdown format
`json
"actions": [
  {"action_type": "purchase", "value": "25"},
  {"action_type": "add_to_cart", "value": "80"},
  {"action_type": "link_click", "value": "800"},
  {"action_type": "post_engagement", "value": "45"}
]
`

### cost_per_action_type breakdown format
`json
"cost_per_action_type": [
  {"action_type": "purchase", "cost_per_action": "2.00"},
  {"action_type": "add_to_cart", "cost_per_action": "0.63"},
  {"action_type": "link_click", "cost_per_action": "0.01"}
]
`

### Reach & Frequency fields
| Field | Description | Example value |
|---|---|---|
| impressions | Total ad impressions | 50000 |
| reach | Unique people reached | 35000 |
| frequency | Average impressions per person | 1.43 |
| unique_impressions | Unique impressions (deduplicated) | 42000 |
| unique_reach | Unique reach (deduplicated) | 35000 |

### Video fields
| Field | Description | Example value |
|---|---|---|
| video_avg_time_watched_seconds | Average watch time | 8.5 |
| videos_3sec_watches | 3-second video views | 12000 |
| videos_10sec_watches | 10-second video views | 4500 |
| videos_full_views | Complete video watches | 1200 |
| video_avg_time_watched | Average watch time (formatted) | "8.5s" |

### Engagement fields
| Field | Description | Example value |
|---|---|---|
| post_engagement_results | Post engagement count | 450 |
| page_likes | Page likes gained | 12 |
| campaign_group_objective_reach | Reach optimized for objective | 30000 |

## Breakdown Dimensions

### Available breakdowns
| Dimension | Description |
|---|---|
| platform | Facebook vs Instagram vs Audience Network |
| device | Desktop vs Mobile vs Tablet |
| age | Age brackets |
| gender | Male vs Female vs All |
| country | By country code |
| region | By region/state |
| city | By city |
| placement | Feed vs Stories vs Reels vs etc |
| impression_device | Device type at impression time |
| publisher_platform | Where ad was shown |
| creative_asset_category | Image vs Video vs Carousel |

### Example with breakdowns
`
GET /act_{ID}/insights?level=ad&fields=spend,impressions,actions,purchase_roas&breakdowns=[placement,platform,age,gender]&date_preset=last_7d
`

## Date Preset Options
| Preset | Description |
|---|---|
| today | Current day (UTC) |
| yesterday | Previous day (UTC) |
| last_7d | Last 7 days including today |
| last_14d | Last 14 days including today |
| last_30d | Last 30 days including today |
| this_month | Current month so far |
| last_month | Previous full month |
| last_3m | Last 3 months |
| this_quarter | Current quarter |
| last_quarter | Previous full quarter |
| lifetime | All time |
| custom | Use since/until parameters |

## Filter Operators
| Operator | Description | Example |
|---|---|---|
| = | Equals | {"field":"objective","op":"eq","value":"CONVERSIONS"} |
| != | Not equals | {"field":"status","op":"neq","value":"DELETED"} |
| > | Greater than | {"field":"spend","op":"gt","value":"10000"} |
| < | Less than | {"field":"frequency","op":"lt","value":"3.0"} |
| >= | Greater or equal | {"field":"purchases","op":"gte","value":"50"} |
| <= | Less or equal | {"field":"cpm","op":"lte","value":"10.0"} |
| IN | In list | {"field":"objective","op":"in","value":["CONVERSIONS","SALES"]} |

## Common API Queries

### Get all ad sets performance (last 7 days)
`
GET /act_{ID}/insights?level=adset&fields=adset_name,spend,impressions,clicks,link_clicks,ctr,cpc,cpm,actions,purchase_roas&date_preset=last_7d
`

### Get top 5 performing ads by ROAS
`
GET /act_{ID}/insights?level=ad&fields=ad_name,spend,purchases,purchase_roas,actions&breakdowns=[creative_asset_category]&date_preset=last_30d&sort=-purchase_roas&limit=5
`

### Find ad sets in learning phase
`
GET /act_{ID}/insights?level=adset&fields=adset_name,spend,results,impressions,reach,frequency&date_preset=last_7d&filtering=[{"field":"optimization_guide","op":"eq","value":"CONVERSIONS"}]
`

### Breakdown by placement (find best performing)
`
GET /act_{ID}/insights?level=adset&fields=adset_name,spend,actions,cpm,cpc,ctr&breakdowns=[placement]&date_preset=last_14d
`

## API Rate Limits
- Standard: ~200 requests per app per user per hour
- Burst: Up to 50 requests/second (short bursts)
- Check X-Marketing-App-Event-Header for remaining quota
- Implement exponential backoff on 429 responses

---
*Created: 2026-06-15 | Reference: Graph API v25.0 docs*