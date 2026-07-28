---
title: "Tham khảo đối tượng chiến dịch Facebook Ads API"
slug: "fb-api-campaign-objects-reference"
category: resource
tags: [vault-maintenance, facebook-ads]
status: "draft"
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---


# Đối tượng Chiến dịch API (Campaign/AdSet/Ad API)

## Meta Graph API v25.0 - Đối tượng Quảng cáo

### Hierarchy trong API
`
- Không, không, không.
  +-- campaigns (POST để tạo)
      +-- /{campaign_id}
          +-- adsets (POST để tạo)
              +-- /{adset_id}
                  +-- ads (POST để tạo)
                      +-- /{ad_id}
`

### Đối tượng Chiến dịch API

#### Các trường chính
| Trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|---|---|
| id | int64 | Tự động | ID chiến dịch |
| name | string | Có | Tên chiến dịch |
| objective | enum | Có | Mục tiêu chiến dịch (xem danh sách bên dưới) |
| status | enum | Có | ĐÃ TÂM, CÂU CHUYỆN, CÂU CHUYỆN, TIẾNG |
| _ nhóm_d | int64 | Điều kiện | Chiến dịch CBO nếu được thiết lập |
| daily_budget | long | Điều kiện | Ngân hàng theo đơn vị nhỏ nhất |
| lifetime_budget | long | Điều kiện | Tổng ngân sách |
| đặc_b____________________________________i_nh | list | Không | Nhà ở, Việc làm, Tín dụng |

#### Giá trị enum Mục tiêu
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

#### Tạo chiến dịch qua API
`
PST // chính xác{AD_ACCOT_D}/Craigns
{
  "name": "Chiến dịch của tôi",
  "objective": "CONVERSIONS",
  "status": "ACTIVE",
  "campaign_group_id": {CBO_CAMPAIGN_ID}  // for CBO
}
`

### Đối tượng AdSet API

#### Các trường chính
| Trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|---|---|
| id | int64 | Tự động | ID tập quảng cáo |
| name | string | Có | Tên tập quảng cáo |
| campaign_id | int64 | Có | Chiến dịch cha |
| status | enum | Có | ĐÃ TÂM, CÂU CHUYỆN, CÂU CHUYỆN, TIẾNG |
| optimization_guide | enum | Có | Sự kiện chuyển đổi để tối ưu hóa cho |
| bidding_info | list | Không | Các chiến lược đặt giá thầu |
| daily_budget / lifetime_budget | long | Conditional | Budget |
| khởi chạy_time/ stop_time | datetime | Điều kiện | Lịch trình |
| targeting | JSON | Điều kiện | Mục tiêu đối tượng |
| placements | list | Không | Vị trí hiển thị thủ công |

#### Giá trị optimization_guide
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

#### Cấu trúc Mục tiêu (JSON)
`json
{
  "geo_locations": {
    "countries": ["VN"],
    "regions": [],
    "cities": [],
    "zip_codes": [],
    "định vị_trat" đúng
  },
  "age_min": 25,
  "age_max": 55,
  "genders": [1],
  "interests": [
    {"id": "{interest_id}", "name": "Tên sở thích"}
  ],
  "behaviors": ["{behavior_id}"],
  "custom_audiences": ["{custom_audience_id}"],
  "exclude_audiences": ["{exclude_audience_id}"]
}
`

#### Tạo tập quảng cáo qua API
`
PST // chính xác{AD_ACCOT_D}/adset
{
  "name": "Tên Tập Quảng Cáo",
  "Camaign_id" :
  "status": "ACTIVE",
  " tuyệt chủng" "Chuyến đi"
  "daily_budget": 5000,  // theo đơn vị tiền tệ nhỏ nhất (xu)
  "bid_amount": 200,     // tùy chọn: trần đặt giá thầu tính bằng xu
  "targeting": { targeting JSON },
  "kiểu sau" :
  "bắt đầu giờ": "2026-06-15T00:00 + 0700"
}
`

### Đối tượng Quảng cáo API

#### Các trường chính
| Trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|---|---|
| id | int64 | Tự động | ID quảng cáo |
| name | string | Có | Tên quảng cáo |
| adset_id | int64 | Có | Tập quảng cáo cha |
| status | enum | Có | ĐÃ TÂM, CÂU CHUYỆN, CÂU CHUYỆN, TIẾNG |
| creative | object | Có | Đối tượng sáng tạo quảng cáo |
| delivery_status | enum | Tự động | Sống, KHÔNG, ĐÃ ĐƯỢC, ĐÃ ĐƯỢC, ĐÃ ĐƯỢC |

#### Cấu trúc Sáng tạo (đơn giản hóa)
`json
{
  "object_store_url": "{image_url}",
  "gọi_oa_action":{" Kiểu: "SHOP_NOW"
  "body": "Văn bản chính ở đây",
  "title": "Tiêu đề ở đây",
  "url_params": "{landing_page_url}"
}
`

#### Tạo quảng cáo qua API
`
PST // chính xác{AD_ACCOT_D}/ads
{
  "name": "Tên Quảng Cáo",
  "adset_id" :
  "status": "ACTIVE",
  "creative": { creative JSON },
  "run_status": "ACTIVE"
}
`

## Tóm tắt các điểm cuối API

### Thao tác CRUD
| Hành động | Phương thức | Điểm cuối |
|---|---|---|
| Tạo chiến dịch | POST | /act_{ID}/campaigns |
| Đọc chiến dịch | GET | /{campaign_id} |
| Cập nhật chiến dịch | POST | /{campaign_id} (với các trường) |
| Xóa chiến dịch | DELETE | /{campaign_id} |
| Tạo tập quảng cáo | POST | /act_{ID}/adsets |
| Đọc tập quảng cáo | GET | /{adset_id} |
| Cập nhật tập quảng cáo | POST | /{adset_id} (với các trường) |
| Xóa tập quảng cáo | DELETE | /{adset_id} |
| Tạo quảng cáo | POST | /act_{ID}/ads |
| Đọc quảng cáo | GET | /{ad_id} |
| Cập nhật quảng cáo | POST | /{ad_id} (với các trường) |
| Xóa quảng cáo | DELETE | /{ad_id} |

## Phân trang API
- Sử dụng fter và efore cursor để phân trang
- Giới hạn mặc định thay đổi tùy theo điểm cuối
- Luôn xử lý phân trang trong mã sản xuất

---
*Tạo: 2026-06-15 | Tham khảo: tài liệu Graph API v25.0*