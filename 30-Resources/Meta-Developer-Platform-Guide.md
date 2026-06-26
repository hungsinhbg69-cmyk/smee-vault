---
title: "Meta Developer Platform - Full Guide"
slug: "meta-developer-platform-guide"
category: knowledge
type: guide
status: v1-complete
created: 2026-06-24
tags: [api, facebook, meta, dev-platform, integration]
last_updated: {{date}}
---

# Meta Developer Platform - Hướng Dẫn Tổng Hợp

> [!INFO] Tổng quan
> **Nguồn:** [[https://developers.facebook.com/docs/]] 
> **Mục đích:** Ghi nhớ các chính sách, quy tắc giới hạn API để agent hoạt động tốt trên nền tảng Facebook/Meta
> **Đừng làm trái luật:** Platform Terms, Privacy Policy, Messaging Standards

---

## Mục Lục

- [[#1. Điều Khoản Nền Tảng (Platform Terms)|Điều khoản]]
- [[#2. Graph API|Graph API]]
- [[#3. Đăng Nhập Bằng Facebook (Facebook Login)|Facebook Login]]
- [[#4. Instagram API|Instagram API]]
  - [[#Basic Display API|Basic Display]]
  - [[#Graph API for Instagram|Graph API (Instagram)]]
- [[#5. Messenger Platform|Messenger Platform]]
- [[#6. WhatsApp Business Platform|WhatsApp Business]]
- [[#7. Rate Limits & Usage Limits|Giới hạn tốc độ & Sử dụng]]
- [[#8. App Review Process|Quy trình xem xét ứng dụng]]
- [[#9. Các API Endpoints Quan Trọng|Endpoints quan trọng]]
- [[#10. Webhooks|Webhook]]

---

## 1. Điều Khoản Nền Tảng (Platform Terms)

> [!UPDATE] Cập nhật gần nhất: 03/02/2026  
> Full policy: https://developers.facebook.com/policy/

### 1.1 Giới Thiệu
- **Nền tảng Meta for Developers** là tập hợp các API, SDK, công cụ, plugin, mã, công nghệ, nội dung và dịch vụ cho phép nhà phát triển (bao gồm cả app developers và website operators) có thể:
  - Phát triển chức năng trên nền tảng Meta
  - Truy xuất dữ liệu từ Meta
  - Cung cấp dữ liệu trở lại bất kỳ Sản phẩm nào của Meta

### 1.2 Bảo Mật Dữ Liệu & Thu Hủy
- Các loại Data bị **giới hạn lưu trữ 12 tháng**(365 ngày) kể từ ngày App cuối cùng truy cập (ví dụ: khi app đã lấy data).
- Một số loại Data cho phép lưu dài hơn theo quy định riêng.

### 1.3 Chính Sách Quyền Riêng Tư (Privacy Policy)
App bắt buộc phải có Privacy Policy với URL công khai, accessible. Phải liệt kê rõ:
- Các trường/fields dữ liệu nào được yêu cầu thu thập từ người dùng
- Cách sử dụng mỗi field

### 1.4 Sử Dụng Dữ Liệu Cấm (Prohibited Use Cases)
- Không xử lý Platform Data để **phân biệt đối xử** trên đặc tính: chủng tộc, dân tộc, màu da, quốc gia, tôn giáo, giới tính...
- Lưu trữ tối đa __365 ngày__ kể từ lần truy cập cuối

### 1.5 Quyền Xem Xét & Tạm Chấm (Compliance Review)
- Meta có thể yêu cầu bạn gửi App cho review/approval
- Nếu không cung cấp thông tin trong **30 ngày**, Meta có quyền tạm dừng/hủy ngay lập tức
- Vi phạm bất kỳ điều khoản nào → bị đình chỉ/chấm dứt

### 1.6 Bồi Thường (Indemnification)
Phải bồi hoàn cho các công ty thuộc Meta từ mọi khiếu nại/ tranh chấp liên quan đến việc sử dụng Platform, xử lý data, nội dung của bạn.

### 1.7 Chuyển Dữ Liệu Quốc Tế (EEA Data Transfer)
- Áp dụng chế độ bảo vệ tương đương với EU GDPR
- Khi transfer data từ EEA sang nonadequate jurisdictions: có yêu cầu bổ sung

### 1.8 Quy Định Chung
- Không thể chuyển giao quyền theo điều khoản cho bên khác khi chưa được Meta chấp thuận **bằng văn bản**
- App ID & data app thuộc bạn nhưng Meta còn xóa sau chấm dứt trong vòng 90 ngày

---

## 2. Graph API

> [!INFO] Resource: [[https://developers.facebook.com/docs/graph-api/overview#standard-param]]
> Reference full: https://developers.facebook.com/docs/graph-api/reference/

### 2.1 Cấu Trúc URL Cơ Bản
```
https://graph.facebook.com/{VERSION}/{OBJECT_ID}?fields={FIELDS}&access_token={TOKEN}
```

### 2.2 Các Version Graph API
- Meta versioned API: mỗi phiên bản có lifecycle và deprecation date
- Luôn dùng version mới nhất còn active, check [Graph API Explorer](https://developers.facebook.com/docs/graph-api/using-graph-api/) để test

### 2.3 Parameter Quy Tắc Chung (Standard Parameters)
Các tham số tiêu chuẩn:
- `access_token` Token truy cập bắt buộc đối với hầu hết requests
- `fields` Comma-separated list of fields để lấy
- `limit` Số record giới hạn trả về (default thường là 25)
- `since/until` Date range filter

### 2.4 Các Method HTTP Được Hỗ Trợ
- **GET** - Lấy dữ liệu
- **POST** - Tạo mới / cập nhật  
- **PUT/PEACH** - Cập nhật toàn bộ
- **DELETE/Xóa** - Xóa record

### 2.5 Error Handling
- Response codes: 200 (OK), 400 (Bad Request), 403 (Forbidden), 429 (Rate Limited), 500 (Server Error)
- Format response error JSON: `{"error": {"message": "...", "type": "...", "code": ..., "fbtrace_id": "..."}}`

---

## 3. Đăng Nhập Bằng Facebook (Facebook Login)

> [!UPDATE] Cập nhật: 3 Tháng 3, 2026  
> Full docs: https://developers.facebook.com/docs/facebook-login/guides/advanced/

### 3.1 Facebook Login Flow (OAuth 2.0)
```
1. Người dùng click "Login with Facebook" 
2. Redirect đến Facebook OAuth URL
3. Người dùng xác nhận permissions
4. Facebook redirect back với authorization_code
5. Exchange code cho access_token
6. Access token lấy data theo permissions đã grant
```

### 3.2 Access Token Types
- **User Access Token** - Dành cho user action, có expiration ngắn (1h) hoặc dài (60 days) 
- **App Access Token** - ID + App Secret, dùng server-to-server call
- **Long-Lived User Access Token** - Renewed từ short-lived (tối đa 60 ngày)
- **Page Token** - Dành cho Page access/action

### 3.3 Permissions & Scopes Quan Trọng
- `public_profile` - Default: name, profile picture, gender, locale, id
- `email` - Email của user  
- `user_posts`, `user_photos` - Data từ user's own timeline
- `pages_read_engagement` - Page insights/posts

### 3.4 GDPR & EU Social Plugin Changes
- Khu vực châu Âu: có danh sách countries specific cho social plugin behavior
- Cần compliance EU regulations khi xử lý EU user data

---

## 4. Instagram API

> [!INFO] Resource: [[https://developers.facebook.com/docs/instagram-api/]]

### 4.1 Basic Display API (for Personal Accounts)

**URL:** https://developers.facebook.com/docs/instagram-basic-display-api/  
**Dành cho:** Instagram personal accounts, không phải Business accounts

#### Authentication Flow
```https://instagram.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=user_profile,user_media&response_type=code```

#### Permissions (Scopes)
- `user_profile` - Access basic profile info  
- `user_media` - Access user's own media only

#### Key Endpoints
- `/me` - Get logged-in user's profile
- `/me/media` - Get user's media list
- `/MEDIA_ID` - Get specific media details

### 4.2 Graph API for Instagram (Business/Creator Accounts)

**URL:** https://developers.facebook.com/docs/instagram-api/content  
**Dành cho:** Instagram Business accounts & Instagram Creator accounts via Page

#### Authentication
```https://www.instagram.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URi}&scope=user_profile,user_media&response_type=code```

### 4.3 Webhooks (Instagram Notifications)
- Subscription để nhận notifications khi có mới content, profile updates
- URL: https://developers.facebook.com/docs/graph-api/guides/webhooks/

---

## 5. Messenger Platform 

> [!INFO] Full guide: [[https://developers.facebook.com/docs/messenger-platform/overview/]]
> Sending messages reference: https://developers.facebook.com/docs/messenger-platform/send-messages/
> Get started: https://developers.facebook.com/docs/messenger-platform/getting-started/

### 5.1 Kiến Trúc Messenger Platform
- **Page Plugin** - Embed Facebook Page on external site
- **Messenger Plugin** - Allow visitors to message your page from external website
- **Bot API** - Full bot capabilities (messaging, webhooks, etc.)

### 5.2 Message Types & Capabilities
- **Text Messages** - Plain text, up to ~4000 characters per payload
- **Buttons** - quick replies, web URL button, postback button
- **Templates** - Generic template, receipt template, media templates
- **Media Attachments** - Images, video, audio, files (max file size: 25MB)
- **Stickers** / **Share Button** / **Open URLs**

### 5.3 Webhooks (Events)
```json
{
    "object": "",
    "entry": [{
        "id": "",
        "time": 1457764197627,
        "messaging": [{
            "sender":{"id":"<PSID>"},
            "recipient":{"id":"<PAGE_ID"},
            "timestamp": 1457764203965,
            "message": {
                "mid":"mid.1457764200896:41d5a3ff09f1c",
                "seq":73,
                "text":"Hello!"
            }
        }]
    }]
}
```

### 5.4 Messenger Policy Limits
- Rate limits theo rate types (thoai, day active users - DAUs)
- Messaging Standard: user-initiated vs server-initiated messages
- 24-hour rule: Có thể gửi message cho user trong vòng 24h kể từ lần cuối họ tương tác

---

## 6. WhatsApp Business Platform

> [!INFO] Cloud API Guide: [[https://developers.facebook.com/docs/whatsapp/cloud-api/]]
> Template Messages: https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates  
> **Note:** On-Premises API was deprecated - end of life 23/10/2025

### 6.1 Cloud API (New) vs Messaging API (Legacy On-Prem)
- **Cloud API** - Hosted by Meta, no self-host server needed
- **On-Premises API** - Deprecated, final version expired 2025-10-23

### 6.2 Pricing Model
- Per conversation pricing: charged per 24-hour session window
- Category types: Marketing, Utility, Authentication, Registration, Service

### 6.3 Message Templates
#### Template Structure
```json
{
    "messaging_product": "whatsapp",
    "to": "+12025551234",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {"code": "en"},
        "components": [{
            "type": "body",
            "parameters": [{
                "type": "text",
                "text": "Hung"
            }]
        }, {
            "type": "button",
            "sub_type": "quick_reply",
            "index": 0,
            "parameters": [{
                "type": "text",
                "text": "Yes"
            }]
        }]
    }
}
```

### 6.4 Template Categories
1. **Marketing** - Promo offers, flash sales, new product launches
2. **Utility** - Account alerts, shipping notifications, appointment confirmations
3. **Authentication** - One-time PIN (OTP), login codes
4. **Registration** - Verification/confirmation codes
5. **Service** - Post-purchase info, account-related

---

## 7. Rate Limits & Usage Limits

### 7.1 Graph API Rate Limits
- Default limit: ~200 requests per app per user per hour (varies by endpoint/purpose)
- Pagination required for large datasets (max `limit=25` default, up to `50`)
- Secure Requests require `access_token` with proper scopes

### 7.2 Messenger Platform Rate Types
1. **User-initiated**: User → App messages
   - Unlimited in 24h window after user first interaction
2. **Server-initiated**: App → User (within 24h)
3. **Threaded** vs **Non-threaded** conversation rate limits differ

### 7.3 WhatsApp Cloud API Rate Limits
- Default: ~80 messages per second per phone number
- Burst limit: short bursts allowed above daily average
- Per-day limits depend on template approval status

### 7.4 Instagram API Limits
- Basic Display: ~200 requests/user/hour
- Graph API (Business): ~600 requests/business_day/user

---

## 8. App Review Process  
> https://developers.facebook.com/docs/apps/review/

### 8.1 Flow
```
1. Add permissions/scopes trong App Settings → Permissions
2. Test app với "App Review" → Submit for approval
3. Meta review team sẽ kiểm tra:
   - Permission usage demo
   - Privacy Policy URL validation
   - Data retention compliance (max 12 months)
4. Nếu approved → live cho tất cả users
```

### 8.2 Permissions Cần Review
- Các permissions mặc định (public_profile, email): auto-approved khi app được tạo
- Permission nâng cao (user_posts, user_photos, pages_manage_posts...): cần review + demo
- Custom permission scope: cũng cần submission/approval

### 8.3 Common Rejection Reasons
- Privacy Policy không liệt kê các field thu thập
- Demo chưa show sử dụng permissions đúng cách
- App hiển thị nội dung không liên quan đến feature

---

## 9. Các API Endpoints Quan Trọng

### Facebook/Graph
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/me` | GET | Get logged-in user profile |
| `/me/friends` | GET | User's friends list (max ~250 if app has permission) |
| `/me/feed` | GET | User posts/timeline |
| `/PAGE_ID` | GET | Page info |
| `/{POST_ID}` | GET/PUT/DELETE | Manage post object |

### Instagram Graph API
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/me` | GET | Logged-in user profile (Basic Display) |
| `/me/media?fields=id,caption,media_type` | GET | User media list |
| `/{MEDIA_ID}` | GET | Specific media object |
| `/?access_token={TOKEN}&id={IG_USER_ID}` | GET | IG user's insights |

### WhatsApp Cloud API
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/PHONE_NUMBER_ID/messages` | POST | Send message to user |
| `/MESSAGE_TEMPLATE_NAME` | GET | Get template details |

---

## 10. Webhooks & Event Subscriptions  

### Facebook Page/Post Events
- `feed` - New posts on a page
- `messaging` - User interaction with Messenger bot
- `account_linking` - Account linking events

### Webhook Setup Steps
1. App Dashboard → Add Product → Messenger/Messaging API
2. Setup webhook URL trong App Settings
3. Verify token với challenge response từ Facebook
4. Subscribe to relevant objects/fields
5. Validate HMAC signature (X-Hub-Signature-256 header)

---

## 11. Best Practices Cho Agent/Bot

### Token Management
- Cache short-lived tokens, renew before expiration  
- Store long-lived tokens securely (max 60 days validity)
- Implement token refresh logic cho app access tokens

### Error Handling
```python
if response.get("error", {}).get("code") == 80:
    # Rate limited - implement exponential backoff
    wait_time = min(2 ** attempt * random.random(), 600)
elif response.get("error", {}).get("code") == 32:
    # Permission denied - request permission or use fallback flow
```

### Pagination Strategy
- Dùng `paging.next` URL từ Graph API responses
- Không làm quá 50 requests/page để tránh rate limiting

### Data Storage Limits (Graph API)
- Max: 12 months data retention after last access (365 days default)
- Một số exceptions cho specific fields/categories (check [[https://developers.facebook.com/docs/graph-api/overview]] for specifics)

---

## 12. Links Quan Trọng  

### Core Docs  
| Resource | URL |
|----------|-----|
| Platform Overview | https://developers.facebook.com/docs/ |
| Graph API | https://developers.facebook.com/docs/graph-api/ |
| Graph API Reference | https://developers.facebook.com/docs/graph-api/reference/ |
| App Dashboard | https://developers.facebook.com/apps/ |
| Permissions Reference | https://developers.facebook.com/docs/permissions/reference/ |

### APIs  
| Platform | Docs URL |
|----------|-----------|
| Facebook Login | https://developers.facebook.com/docs/facebook-login/guides/advanced/ |
| Instagram API | https://developers.facebook.com/docs/instagram-api/ |
| Messenger Platform | https://developers.facebook.com/docs/messenger-platform/overview/ |
| WhatsApp Cloud API | https://developers.facebook.com/docs/whatsapp/cloud-api/ |

### Policies  
| Policy | URL |
|--------|-----|
| Platform Terms | https://developers.facebook.com/policy/ |
| Privacy Policy | https://www.facebook.com/privacy/policy/ |
| Content Policy | https://www.facebook.com/policies/content/ |
| Community Standards | https://www.facebook.com/communitystandards/ |

---

*Last updated: 24/06/2026 — Agent knowledge base for Facebook/Meta platform compliance*


> [!UPDATE] Extra info extracted 24/06/2026 — từ Messenger Platform overview (updated 23 Tháng 3, 2026)

### Messenger Platform Core Concepts
- **Messenger from Meta**: Trang Facebook hoặc tài khoản Công việc trên Instagram có thể trả lời tin nhắn qua Facebook, Instagram hay plugin Meta trên app di động/trang web.
- **Mọi người phải bắt đầu cuộc trò chuyện trước** — bạn có thể dùng Nền tảng Messenger miễn phí.
- Khi người gửi tin nhắn đến → webhook trigger → App gọi Graph API → xác định phản hồi phù hợp → gửi trong 24h.

### Scoped IDs (ID theo phạm vi cụ thể)
Mỗi người nhắn tin cho Trang/Tài khoản Instagram được gán một **Scoped ID** riêng biệt:
- **Scoped ID (Page)**: tạo khi người nhắn tin qua Trang Facebook của bạn
- **Scoped ID (Instagram)**: tạo khi người nhắn tin qua IG Business/Creator Account
- Scoped IDs giúp mapping hoạt động giao tiếp giữa nhiều apps — nhưng **không thể cross-platform**: FB User không nhắn cho IG Account và ngược lại.

### Messenger Platform Key Concepts
| Khái niệm | Mô tả |
|-----------|--------|
| Access Token | Chuỗi mờ (masking string) cung cấp quyền truy cập tạm thời & an toàn vào Graph API endpoints để gửi/nhận tin |
| Page Access Token | Type của Access Token dùng thay mặt Trang Facebook thực hiện API calls. Cần thiết để gửi và nhận tin qua Messenger Platform. Được tạo sau khi Page Admin grant permissions cho app. |
| App Level Access | **Standard (default)**: chỉ users có Role trên app hoặc Page của bạn mới tiếp cận dữ liệu. **Advanced**: mở rộng quyền access cho mọi user trong app, yêu cầu App Review. |
| Facebook Login for Business | Bắt buộc để yêu cầu người dùng grant permission gửi/nhận tin nhắn thay họ. |
| Webhooks | Realtime notifications về tin nhắn đến Trang/Instagram Account — giúp không cần polling Graph API. |
| Rate Limiting | Giới hạn số API calls và message throughput. Inbox tính năng có thể tạm disable khi messages volumes quá cao. |
| Policy | Các chính sách nền tảng, feedback requirements và community standards phải tuân để duy trì API access. |
| CDN URL | Privacy-first content delivery network for fetching rich media files from shared Instagram content. Media expires after deletion or time limit. |

### Pre-Requisites Before Starting Messenger Platform
1. **Tài khoản developer** đăng ký trên Meta
2. **Application trên Meta** với use case Messenger
3. **Facebook Page** liên kết với app của bạn
4. **Instagram Business/Creator Account** (cho Instagram DM)
5. **Business Verification** (tùy chọn nếu chỉ gửi/nhận cho Page của riêng mình)
6. **App Review** (bắt buộc nếu cần Advanced Access)

### Required Permissions for Messaging
| Permission | Ghi chú |
|------------|---------|
| `pages_show_list` | Hiển thị list của Pages mà app có quyền access |
| `pages_manage_metadata` | Quản lý metadata của Page |
| `pages_messaging` (mới) | Cho phép gửi/nhận tin nhắn trên behalf — thay thế pages_read_engagement cho messaging workflows |
| `pages_read_engagement` | Đọc engagement data từ Page |

### Messenger Platform Pricing Model (2024+)
- **Free tier**: 1,000 conversations/month đầu tiên miễn phí
- Sau đó: theo conversation model với categories (Marketing/Utility/Authentication)

---

> [!UPDATE] Extra info extracted 24/06/2026 — từ Graph API Overview (Instagram)

### Instagram Graph API (dành cho Business/Creator Accounts qua Page)
**URL:** https://developers.facebook.com/docs/instagram-api/overview  
**Giới thiệu cập nhật:** Phiên bản API mới nhất đang active.

#### Khi nào dùng Basic Display vs Graph API
| Criteria | Basic Display API | Graph API for Instagram |
|----------|-------------------|-------------------------|
| Account type | Personal accounts only | Business & Creator accounts (via Page) |
| Data scope | User's own media only | Full Page + IG insights, comments, replies |
| Requires App Review | No (only user consent) | Yes (if using advanced permissions) |

#### Instagram Graph API Key Endpoints
- `GET /me` — Logged-in user profile connected to a FB Page
- `GET /me/media?fields=id,caption,media_type,timestamp,permalink` — Get media list
- `GET /{MEDIA_ID}` — Specific media object details
- `GET /?id={IG_USER_ID}&fields=username,media_count,follows_count,followers_count` — Insights endpoint

---
