# API Campaign Objects (Campaign/AdSet/Ad API)

## Meta Graph API v25.0 - Ads Objects

### Hierarchy in API
`
/{ad_account_id}
  +-- campaigns (POST to create)
      +-- /{campaign_id}
          +-- adsets (POST to create)
              +-- /{adset_id}
                  +-- ads (POST to create)
                      +-- /{ad_id}
`

### Campaign API Object

#### Key fields
| Field | Type | Required | Description |
|---|---|---|---|
| id | int64 | Auto | Campaign ID |
| name | string | Yes | Campaign name |
| objective | enum | Yes | Campaign objective (see list below) |
| status | enum | Yes | ACTIVE, PAUSED, DELETED, ARCHIVED |
| campaign_group_id | int64 | Conditional | CBO campaign if set |
| daily_budget | long | Conditional | Budget in minor units |
| lifetime_budget | long | Conditional | Total budget |
| special_ad_categories | list | No | Housing, Employment, Credit |

#### Objective enum values
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
- SALES

#### Creating a campaign via API
`
POST /act_{AD_ACCOUNT_ID}/campaigns
{
  "name": "My Campaign",
  "objective": "CONVERSIONS",
  "status": "ACTIVE",
  "campaign_group_id": {CBO_CAMPAIGN_ID}  // for CBO
}
`

### AdSet API Object

#### Key fields
| Field | Type | Required | Description |
|---|---|---|---|
| id | int64 | Auto | Ad Set ID |
| name | string | Yes | Ad set name |
| campaign_id | int64 | Yes | Parent campaign |
| status | enum | Yes | ACTIVE, PAUSED, DELETED, ARCHIVED |
| optimization_guide | enum | Yes | Conversion event to optimize for |
| bidding_info | list | No | Bid strategies |
| daily_budget / lifetime_budget | long | Conditional | Budget |
| start_time / stop_time | datetime | Conditional | Schedule |
| targeting | JSON | Conditional | Audience targeting |
| placements | list | No | Manual placements |

#### optimization_guide values
- LINK_CLICKS
- IMPRESSIONS
- PAGE_LIKES
- OPTIMIZED_AD_CLICKS
- CONVERSIONS
- VALUE
- LEADS
- ENGAGEMENT
- MESSAGES
- EVENT_RESPONSES
- POST_ENGAGEMENT
- OFFER_CLAIMS
- QUALITY_CALLING
- CALL_DISPUTES
- DYNAMIC_STORE_PRODUCT_ADS
- PRODUCT_CATALOG_SALES
- THRU_PLAYS
- INSTAGRAM_REELS

#### Targeting structure (JSON)
`json
{
  "geo_locations": {
    "countries": ["VN"],
    "regions": [],
    "cities": [],
    "zip_codes": [],
    "location_tracking": true
  },
  "age_min": 25,
  "age_max": 55,
  "genders": [1],
  "interests": [
    {"id": "{interest_id}", "name": "Interest Name"}
  ],
  "behaviors": ["{behavior_id}"],
  "custom_audiences": ["{custom_audience_id}"],
  "exclude_audiences": ["{exclude_audience_id}"]
}
`

#### Creating an ad set via API
`
POST /act_{AD_ACCOUNT_ID}/adsets
{
  "name": "Ad Set Name",
  "campaign_id": {CAMPAIGN_ID},
  "status": "ACTIVE",
  "optimization_guide": "CONVERSIONS",
  "daily_budget": 5000,  // in minor currency units (cents)
  "bid_amount": 200,     // optional: bid cap in cents
  "targeting": { targeting JSON },
  "pacing_type": ["STANDARD"],
  "start_time": "2026-06-15T00:00:00+0700"
}
`

### Ad API Object

#### Key fields
| Field | Type | Required | Description |
|---|---|---|---|
| id | int64 | Auto | Ad ID |
| name | string | Yes | Ad name |
| adset_id | int64 | Yes | Parent ad set |
| status | enum | Yes | ACTIVE, PAUSED, DELETED, ARCHIVED |
| creative | object | Yes | Ad creative object |
| delivery_status | enum | Auto | LIVE, UNSENT, EXPIRED, DEAD |

#### Creative structure (simplified)
`json
{
  "object_store_url": "{image_url}",
  "call_to_action": {"type": "SHOP_NOW"},
  "body": "Primary text here",
  "title": "Headline here",
  "url_params": "{landing_page_url}"
}
`

#### Creating an ad via API
`
POST /act_{AD_ACCOUNT_ID}/ads
{
  "name": "Ad Name",
  "adset_id": {ADSET_ID},
  "status": "ACTIVE",
  "creative": { creative JSON },
  "run_status": "ACTIVE"
}
`

## API Endpoints Summary

### CRUD operations
| Action | Method | Endpoint |
|---|---|---|
| Create campaign | POST | /act_{ID}/campaigns |
| Read campaign | GET | /{campaign_id} |
| Update campaign | POST | /{campaign_id} (with fields) |
| Delete campaign | DELETE | /{campaign_id} |
| Create ad set | POST | /act_{ID}/adsets |
| Read ad set | GET | /{adset_id} |
| Update ad set | POST | /{adset_id} (with fields) |
| Delete ad set | DELETE | /{adset_id} |
| Create ad | POST | /act_{ID}/ads |
| Read ad | GET | /{ad_id} |
| Update ad | POST | /{ad_id} (with fields) |
| Delete ad | DELETE | /{ad_id} |

## API Pagination
- Use fter and efore cursor for pagination
- Default limit varies by endpoint
- Always handle pagination in production code

---
*Created: 2026-06-15 | Reference: Graph API v25.0 docs*