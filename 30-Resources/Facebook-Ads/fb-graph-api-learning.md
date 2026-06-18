# Facebook Graph API Learning Notes

## Overview - Graph API

### Core Concepts
- **Graph API**: HTTP-based API để get data vào/ra khỏi Facebook platform
- **Social Graph**: Representation of information on Facebook
- **3 thành phần chính**:
  1. **Nodes**: Individual objects với unique ID (User, Page, Post, Photo, Comment...)
  2. **Edges**: Connections giữa các nodes (User → photos, Photo → comments)
  3. **Fields**: Node properties, dùng param `fields=` để query cụ thể

### HTTP & Host
- Tất cả dùng **HTTPS**, endpoint: `graph.facebook.com`
- Dùng `curl.exe` thay vì PowerShell curl (tránh URL encoding issues)

### Access Tokens
- Hầu hết endpoints đều cần access token
- 2 chức năng:
  1. Access user info without password
  2. Identify app, user, và permitted data type
- **Page Access Token** (Never-Expire): Coi như không bao giờ hết hạn

### Nodes
- Mỗi node có unique ID
- Example: `curl -i -X GET "https://graph.facebook.com/USER-ID?access_token=ACCESS-TOKEN"`
- **Node metadata deprecated** trong v25.0, sẽ remove hoàn toàn 19/05/2026

### /me Endpoint
- Special endpoint: translates đến object ID của person/Page whose token đang dùng
- Example: `curl -i -X GET "https://graph.facebook.com/me?access_token=ACCESS-TOKEN"`

### Edges
- Connection giữa 2 nodes
- Example: `curl -i -X GET "https://graph.facebook.com/USER-ID/photos?access_token=ACCESS-TOKEN"`

### Fields
- Node properties
- Dùng param `fields=id,name,email,picture&access_token=...`
- ID luôn được trả về mặc định

### Publishing, Updating, Deleting
- POST operations để update fields
- **Read-After-Write**: Create/Update endpoints có thể trả về fields ngay lập tức
- DELETE operation trên object ID để xóa nodes
- Example: `curl -i - X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&fields=created_time,from,id,message&access_token=ACCESS-TOKEN"`

### Versions
- Graph API có nhiều versions, **quarterly releases**
- Cần thêm `v25.0` vào URL path: `https://graph.facebook.com/v25.0/...`
- Không có version → default oldest version
- **Recommend**: Luôn include version number trong requests

## Rate Limits

### 2 loại Rate Limits
1. **Platform Rate Limits**: Application/User tokens
2. **Business Use Case (BUC) Rate Limits**: System user/Page access tokens

### Pages API Rate Limits
- **Page/System User token**: BUC Rate Limits
  - `Calls within 24 hours = 4800 * Number of Engaged Users`
- **App/User token**: Platform Rate Limits
  - `Calls within one hour = 200 * Number of Users`

### Error Codes Quan Trọng
- `4`: App reached rate limit
- `17`: User reached rate limit
- `32`: Page request limit reached (User/App token)
- `80001`: Page calls với Page/System User token (BUC)
- `80000/80004/80003`: Ads Insights/Management/Audience

### Headers để Check Rate Limit
- `X-App-Usage`: Platform Rate Limits
  - `call_count`: % calls made trong 1 hour rolling window
  - `total_cputime`: % CPU time used
  - `total_time`: % total time used
- `X-Business-Use-Case-Usage`: BUC Rate Limits
  - `call_count`: % calls made
  - `estimated_time_to_regain_access`: Time in minutes until unthrottled
  - `total_cputime`, `total_time`: % usage

### Best Practices
1. **Stop making calls** khi đạt limit (tiếp tục gọi = tăng thời gian reset)
2. **Spread out queries** đều để avoid traffic spikes
3. **Use filters** để limit response size
4. **Check headers** để xem current usage
5. **Multiple IDs in one request** (mỗi ID = 1 API call)
6. **Page Access Token** → BUC limits (tốt hơn Platform limits)

### API Call Counting
- Mỗi ID trong request = 1 API call
- `GET /photos?ids=4,5,6` = 3 calls (không phải 1!)
- Recommend: specify multiple IDs in one request để improve performance
