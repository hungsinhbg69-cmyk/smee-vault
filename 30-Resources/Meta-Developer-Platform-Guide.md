---
title: "Meta Nền tảng nhà phát triển - Hướng dẫn đầy đủ"
slug: "meta-developer-platform-guide"
category: resource
type: guide
status: completed
created: 2026-06-24
tags: [api, facebook, meta, dev-platform, integration]
last_updated: 2026-07-13
---

# Meta Developer Platform - Hướng Dẫn Tổng Hợp

> [!INFO] Tổng quan
> **Nguồn:** [Meta for Developers](https://developers.facebook.com/docs/)
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

> [!INFO] Resource: [Graph API overview](https://developers.facebook.com/docs/graph-api/overview#standard-param)
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
- `since/until` Lọc phạm vi ngày

### 2.4 Các Method HTTP Được Hỗ Trợ
- **GET** - Lấy dữ liệu
- **POST** - Tạo mới / cập nhật  
- **PUT/PEACH** - Cập nhật toàn bộ
- **DELETE/Xóa** - Xóa record

### 2.5 Error Handling
- Mã trả lời: 200 (OK), 400 (điều yêu cầu không chính thức), 403 (Forbbden), 429 (Rate Conver Conserted), 500 (lỗi máy phục vụ)
- Lỗi định dạng trả lời JSON: `{"error": {"message": "...", "type": "...", "code": ..., "fbtrace_id": "..."}}`

---

## 3. Đăng Nhập Bằng Facebook (Facebook Login)

> [!UPDATE] Cập nhật: 3 Tháng 3, 2026  
> Full docs: https://developers.facebook.com/docs/facebook-login/guides/advanced/

### 3.1 Facebook Dòng đăng nhập (OAth 2.0)
```
1. Người dùng click "Login with Facebook" 
2. Redirect đến Facebook OAuth URL
3. Người dùng xác nhận permissions
4. Facebook redirect back với authorization_code
5. Exchange code cho access_token
6. Access token lấy data theo permissions đã grant
```

### 3. 2 Truy cập các kiểu mực
- **User Access Token** - Dành cho user action, có expiration ngắn (1h) hoặc dài (60 days) 
- **App Access Token** - ID + App Secret, dùng server-to-server call
- **Long-Lived User Access Token** - Renewed từ short-lived (tối đa 60 ngày)
- **Page Token** - Dành cho Page access/action

### 3.3 Permissions & Scopes Quan Trọng
- `public_profile` - Mặc định: tên, hình ảnh hồ sơ, giới tính, địa phương, id
- `email` - Email của user  
- `user_posts`, `user_photos` - Data từ user's own timeline
- `pages_read_engagement` - Sự hiểu biết/ cột trang

### 3.4 GDPR & EU Sổ tay Plugin Thay đổi
- Khu vực châu Âu: có danh sách countries specific cho social plugin behavior
- Cần compliance EU regulations khi xử lý EU user data

---

## 4. Instagram API

> [!INFO] Resource: [Instagram API](https://developers.facebook.com/docs/instagram-api/)

### Màn hình 4. 1 API (cho các tài khoản cá nhân)

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

### 4.3 bộ giữ mạng ( Thú nhận dạng địa chỉ trên mạng)
- Subscription để nhận notifications khi có mới content, profile updates
- URL: https://developers.facebook.com/docs/graph-api/guides/webhooks/

---

## 5. Messenger Platform 

> [!INFO] Full guide: [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/overview/)
> Đang gửi thông điệp tham chiếu: https://developers.facebook.com/docs/messenger-platform/send-messages/
> Get started: https://developers.facebook.com/docs/messenger-platform/getting-started/

### 5.1 Kiến Trúc Messenger Platform
- ** Trang Plugin** - Embed Facebook Trang trên trang bên ngoài
- **Messenger Plugin** - Cho phép khách truy cập thông điệp từ trang bên ngoài
- **Bot API** - khả năng robot đầy đủ (mesing, webhoooks, etc.)

### 5.2 kiểu thông điệp và khả năng
- ** Văn bản tin nhắn** - Văn bản thường, lên đến ~4000 ký tự trên mỗi kiện hàng
- ** Buttons** - trả lời nhanh, web URL Nút sau
- **Temamps** - Giống nhau mẫu, mẫu biên nhận, mẫu phương tiện
- **Media phụ thuộc** - Ảnh, video, âm thanh, tập tin ( Cỡ tập tin trục: 25MB)
- **Stickers** / **Share Button** / ** Mở ra URL**

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

### Giới hạn chính sách của người đưa tin
- Tốc độ giới hạn các kiểu tỷ lệ (thoai, ngày hoạt động người dùng - DAUs)
- Tiêu chuẩn nhắn tin: tin nhắn đã nhập với máy phục vụ
- 24-hour rule: Có thể gửi message cho user trong vòng 24h kể từ lần cuối họ tương tác

---

## 6 Những gì phụ thuộc vào cơ sở kinh doanh

> [!INFO] Cloud API Guide: [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/)
> Template Messages: https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates  
> **Noe:** On-Premises API đã bị bác bỏ - cuối cuộc sống 23/10/2025

### 6. 1 mây API (New) Ghi chú API (Tiếng Nhật)
- **Cuoud API** - Máy móc bởi MetaKhông cần máy chủ tự động
- ** on-Premises API** - Bị phản đối, phiên bản cuối cùng hết hạn 2025-10-23

### 6.2 Pricing Model
- Mỗi lần thử trò chuyện: sạc một cửa sổ phiên chạy 24 tiếng
- Loại phân loại: Thị trường, tiện ích, xác thực, đăng ký, dịch vụ

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
1. ** Markett** - Promo đề nghị, bán flash, sản phẩm mới ra mắt
2. **Thuyết phục** - Báo động tài khoản, chuyển thông báo, xác nhận cuộc hẹn
3. **Authentication** - Một lần PIN (OTP), mã đăng nhập
4. **Registation** - Mã xác nhận/ xác thực
5. **Service** - sau khi-purchase thông tin, liên quan đến tài khoản

---

## 7 Tốc độ Giới hạn và hạn sử dụng

### Đồ thị 7.1 API Giới hạn tỷ lệ
- Giới hạn mặc định: ~200 yêu cầu mỗi ứng dụng mỗi giờ (có ý nghĩa cuối/ mục đích)
- Cần thiết độ phóng đại cho bộ dữ liệu lớn (xx) `limit=25` mặc định, lên tới `50`)
- Yêu cầu bảo mật `access_token` có phạm vi thích hợp

### Name
1. **User-inited**: người dùng truy cập truy cập
   - Vô hạn trong cửa sổ 24h sau khi người dùng tương tác đầu tiên
2. **Server-initiated**: App → User (within 24h)
3. **Threaded** vs **Non-threaded** tỷ lệ trò chuyện khác nhau

### 7.3 Những gì phụ thuộc vào mây API Giới hạn tỷ lệ
- Mặc định: ~80 tin nhắn mỗi giây trên mỗi số điện thoại
- Giới hạn mắc lỗi: Những vụ nổ ngắn được phép trên mức trung bình hàng ngày
- Giới hạn mỗi ngày phụ thuộc vào trạng thái chấp nhận mẫu

### 7.4 Instagram API Limits
- Màn hình cơ bản: ~200 yêu cầu/er/h
- Đồ thị API (T.Mễ: ~600 yêu cầu/ thương mại_ngày/người dùng

---

## Tiến trình ôn lại  
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

### 8; 3 Lý do từ chối thông thường
- Privacy Policy không liệt kê các field thu thập
- Demo chưa show sử dụng permissions đúng cách
- App hiển thị nội dung không liên quan đến feature

---

## 9. Các API Endpoints Quan Trọng

### Facebook/Graph
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/me` | GET | Lấy hồ sơ người dùng đăng nhập |
| `/me/friends` | GET | Danh sách bạn bè của người dùng (x ~250 nếu ứng dụng có sự cho phép) |
| `/me/feed` | GET | Người dùng đăng/ dòng giờ |
| `/PAGE_ID` | GET | Page info |
| `/{POST_ID}` | GÔ - TÊ - TÊ - TÊ - TÊ | Quản lý đối tượng bưu điện |

### Instagram Graph API
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/me` | GET | Hồ sơ người dùng đã đăng nhập (hiện bóng) |
| `/me/media?fields=id,caption,media_type` | GET | Danh sách phương tiện người dùng |
| `/{MEDIA_ID}` | GET | Đối tượng phương tiện đặc trưng |
| `/?access_token={TOKEN}&id={IG_USER_ID}` | GET | Sự hiểu biết của người dùng IG |

### WhatsApp Cloud API
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/PHONE_NUMBER_ID/messages` | POST | Gửi thông điệp cho người dùng |
| `/MESSAGE_TEMPLATE_NAME` | GET | Lấy chi tiết mẫu |

---

## 10. Hình móc trang Mạng và bản in tương ứng  

### Facebook Sự kiện trang/bb cờ
- `feed` - Bài mới trên trang
- `messaging` - Tương tác với robot trình nhắn tin
- `account_linking` - Tài khoản liên kết các sự kiện

### Bước thiết lập móc câuName
1. Phụ lục bảng tin nhắn/ Tin nhắn API
2. Cài đặt Hình mạng URL Thiết lập bộ đệm
3. Verify token với challenge response từ Facebook
4. Đăng ký các đối tượng/ sân có liên quan
5. Kiểm tra chữ ký HMAC (X-Hub-Signacture-256 fronter)

---

## 11. Bài tập tốt nhất Cho Đặc vụ/Bot

### Token Management
- Các vật kỷ niệm ngắn tuổi, hồi sinh trước khi hết hạn  
- Lưu những vật lưu trữ lâu bền (60 ngày hợp lệ)
- Sự bổ sung hiệu quả làm tươi tỉnh logic cho các biểu tượng truy cập ứng dụng

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

### Giới hạn lưu trữ dữ liệu (Graph API)
- Tối đa: 12 tháng lưu dữ liệu sau khi truy cập cuối (365 ngày mặc định)
- Một số exceptions cho specific fields/categories (check [Graph API overview](https://developers.facebook.com/docs/graph-api/overview) for specifics)

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

*Last update: 24/06/2026 — Cơ sở kiến thức đặc biệt cho Facebook/Meta Làm theo cách thức


> [!UPDATE] Extra info extracted 24/06/2026 — từ Messenger Platform overview (updated 23 Tháng 3, 2026)

### Name
- **Messenger from Meta**: Trang Facebook hoặc tài khoản Công việc trên Instagram có thể trả lời tin nhắn qua Facebook, Instagram hay plugin Meta trên app di động/trang web.
- **Mọi người phải bắt đầu cuộc trò chuyện trước** — bạn có thể dùng Nền tảng Messenger miễn phí.
- Khi người gửi tin nhắn đến → webhook trigger → App gọi Graph API → xác định phản hồi phù hợp → gửi trong 24h.

### Scoped IDs (ID theo phạm vi cụ thể)
Mỗi người nhắn tin cho Trang/Tài khoản Instagram được gán một **Scoped ID** riêng biệt:
- **Scoped ID (Page)**: tạo khi người nhắn tin qua Trang Facebook của bạn
- **Scoped ID (Instagram)**: tạo khi người nhắn tin qua IG Business/Creator Account
- Scoped IDs giúp mapping hoạt động giao tiếp giữa nhiều apps — nhưng **không thể cross-platform**: FB User không nhắn cho IG Account và ngược lại.

### Name
| Khái niệm | Mô tả |
|-----------|--------|
| Access Token | Chuỗi mờ (masking string) cung cấp quyền truy cập tạm thời & an toàn vào Graph API endpoints để gửi/nhận tin |
| Truy cập trang | Type của Access Token dùng thay mặt Trang Facebook thực hiện API calls. Cần thiết để gửi và nhận tin qua Messenger Platform. Được tạo sau khi Page Admin grant permissions cho app. |
| Truy cập cấp chấp nhận | **Standard (default)**: chỉ users có Role trên app hoặc Page của bạn mới tiếp cận dữ liệu. **Advanced**: mở rộng quyền access cho mọi user trong app, yêu cầu App Review. |
| Facebook Đăng nhập vào kinh doanh | Bắt buộc để yêu cầu người dùng grant permission gửi/nhận tin nhắn thay họ. |
| Webhooks | Realtime notifications về tin nhắn đến Trang/Instagram Account — giúp không cần polling Graph API. |
| Rate Limiting | Giới hạn số API calls và message throughput. Inbox tính năng có thể tạm disable khi messages volumes quá cao. |
| Policy | Các chính sách nền tảng, feedback requirements và community standards phải tuân để duy trì API access. |
| CDN URL | Mạng nội dung đầu tiên để lấy tập tin phương tiện giàu có từ nội dung trên mạng đã chia sẻ. Truyền thông hết hạn sau khi xóa, hoặc hạn chế thời gian. |

### Các nhà cầm quyền trước khi khởi động trình gửi thư
1. **Tài khoản developer** đăng ký trên Meta
2. **Application trên Meta** với use case Messenger
3. **Facebook Page** liên kết với app của bạn
4. **Instagram Business/Creator account** (cho hệ thống mạng vô tuyến)
5. **Business Verification** (tùy chọn nếu chỉ gửi/nhận cho Page của riêng mình)
6. **App Review** (bắt buộc nếu cần Advanced Access)

### Cần thiết quyền làm loạn
| Permission | Ghi chú |
|------------|---------|
| `pages_show_list` | Hiển thị list của Pages mà app có quyền access |
| `pages_manage_metadata` | Quản lý metadata của Page |
| `pages_messaging` (mới) | Cho phép gửi/nhận tin nhắn trên behalf — thay thế pages_read_engagement cho messaging workflows |
| `pages_read_engagement` | Đọc engagement data từ Page |

### Mô hình điểm ảnh cho trình tin nhắn (2024+)
- **Free tier**: 1,000 conversations/month đầu tiên miễn phí
- Sau đó: theo conversation model với categories (Marketing/Utility/Authentication)

---

> [!UPDATE] Extra info extracted 24/06/2026 — từ Graph API Overview (Instagram)

### Instagram Graph API (dành cho Business/Creator Accounts qua Page)
**URL:** https://developers.facebook.com/docs/instagram-api/overview  
**Giới thiệu cập nhật:** Phiên bản API mới nhất đang active.

#### Khi nào dùng Basic Display vs Graph API
| Criteria | Basic Display API | Đồ thị API cho trình nền |
|----------|-------------------|-------------------------|
| Account type | Chỉ tài khoản cá nhân | Tài khoản kinh doanh và Đấng Tạo Hóa (trangvia) |
| Data scope | Chỉ truyền thông của người dùng | Toàn bộ trang + IP nhìn thấu, bình luận, trả lời |
| Cần phải ôn lại | Không có (sự chấp thuận người dùng chỉ) | Có (nếu dùng quyền hạn cấp cao) |

#### Đồ thị trên mạng API Điểm kết thúc khóa
- `GET /me` - Hồ sơ người dùng đã đăng nhập vào kết nối đến trang FB
- `GET /me/media?fields=id,caption,media_type,timestamp,permalink` - Lấy danh sách phương tiện đi.
- `GET /{MEDIA_ID}` — cụ thể chi tiết phương tiện
- `GET /?id={IG_USER_ID}&fields=username,media_count,follows_count,followers_count` — Insights endpoint

---
