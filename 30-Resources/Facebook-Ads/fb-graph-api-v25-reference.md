---
title: "Facebook Graph API Reference — Tổng Hợp (2026-06-09)"
slug: "facebook-ads-comprehensive-guide-to-facebook-graph-api-v25"
category: resource
tags: [vault-maintenance]
status: "draft"
type: reference
created: 2025-12-01
last_updated: 2026-06-24
---

# Facebook Graph API Reference — Tổng Hợp (2026-06-09)

> Nguồn: https://developers.facebook.com/docs/graph-api/reference
> & https://developers.facebook.com/docs/graph-api
> Phiên bản hiện tại: **v25.0**

---

## 📌 Graph API — Tổng Quan

**Graph API** là cách chính để apps đọc/ghi vào Facebook social graph. Tất cả SDKs và products của Meta đều tương tác với Graph API. Các APIs khác là extensions của Graph API.

### 8 Tài Liệu Nền Tảng (từ Graph API docs)
1. **Overview** — Cấu trúc Facebook Social Graph
2. **Get Started** — Explorer tool + request đầu tiên
3. **Batch yêu cầu** — Nhiều API yêu cầu cuộc gọi thứ nhất
4. ** Yêu cầu debug** — gỡ lỗi API yêu cầu
5. **Handle errors** — Xử lý common errors
6. **Felid mở rộng** — Giới hạn đối tượng trả lại yêu cầu làm tổ
7. **Secure yêu cầu** — Bảo mật API yêu cầu
8. **su tải có thể tái sử dụng API** — Tải lên tập tin

---

## 🏗️ GRAPH API ROOT NODES

Root nodes có thể query trực tiếp. Non-root nodes query qua root nodes hoặc edges.

### Core Objects (dùng thường xuyên cho Page bot)

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Page** | Page object | ⭐⭐⭐ |
| **Page Post** | Facebook Feed story (post trên Page) | ⭐⭐⭐ |
| **Post** | Facebook Feed story | ⭐⭐⭐ |
| **Photo** | Photo trên Facebook | ⭐⭐ |
| **Comment** | Facebook comment | ⭐⭐⭐ |
| **User** | User object | ⭐⭐ |
| **Video** | Video object | ⭐⭐ |
| **Message** | Thông điệp trong Facebook Tin nhắn | ⭐⭐ |
| **Thread** | Thread (Messenger) | ⭐⭐ |
| **Conversation** | Conversation object | ⭐⭐ |
| **Page/insights** | Một bộ đo thấu hiểu liên quan đến Trang/ App/ blug | ⭐⭐⭐ |
| ** Trang gọi hành động** | Lệnh nhập của trang | ⭐⭐ |
| ** Trang lên tới thay đổi** | Thông báo trang sẽ thay đổi | ⭐ |
| **URL** | Chia sẻ, liên kết ứng dụng, đồ thị Mở cho a URL | ⭐⭐ |
| **Profile** | Profile object | ⭐ |
| **Album** | Photo album | ⭐ |
| **Event** | Event object | ⭐ |
| **Place** | Place object | ⭐ |
| **Place Tag** | Người được gắn dấu tại vị trí/ cột/ điểm | ⭐ |
| **Place Topic** | Loại trang | ⭐ |
| **Link** | Liên kết được chia sẻ trên tường | ⭐ |
| **Mailing Address** | Thư điện tử: | ⭐ |
| **Request** | Request object | ⭐ |
| **Test User** | Đối tượng người dùng thử | ⭐ |

### Các mục quảng cáo

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Adgroup** | Đối tượng có chức năng (xem ảnh và kết hợp thiết lập) | ⭐⭐⭐ |
| **Canvas** | Tập tin Canvas ( đầy màn hình quảng cáo) | ⭐⭐ |
| **Canvas Button** | Nút bên trong vải | ⭐ |
| **Canvas Carousel** | Tấm vải bên trong | ⭐ |
| **Canvas Footer** | Màu | ⭐ |
| **Canvas Header** | Tiêu đề bên trong vải | ⭐ |
| **Canvas Photo** | Ảnh chụp bên trong vải | ⭐ |
| **Bravas books** | Danh sách sản xuất bên trong vải | ⭐ |
| **Canvas st** | Sản phẩm được đặt bên trong vải | ⭐ |
| **Canvas Text** | Phần tử vải | ⭐ |
| **Canvas Video** | Ảnh động bên trong vải | ⭐ |
| ** Thư mục cố vấn hợp tác** | Thư mục các doanh nghiệp quảng cáo hợp tác | ⭐ |
| **Trích từ cấu hình cấu hình mã hóa tín dụng** | Đường dây tín dụng chia sẻ giữa các danh mục đầu tư kinh doanh | ⭐ |
| **Bragline Conversion Data thiết lập tải lên** | Bộ dữ liệu buổi tiệc phụ thuộc | ⭐ |
| **Ads Archive** | Quảng cáo đã lưu (dòng chủ) | ⭐⭐ |

### Instagram Objects

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Sự phân phối kinh doanh trên mạng** | Name | ⭐⭐ |
| **Instagram Oembed** | InstagramOembed | ⭐ |
| **IGUser** | Người dùng trên Facebook (Sendow IGUser) | ⭐ |

### Messenger & WhatsApp

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| ** Mẫu kinh doanh người đưa tin** | Comment | ⭐⭐ |
| ** Thư viện Mẫu Tin KDE** | Danh sách mẫu thông điệp trong thư viện của ứng dụng (root) | ⭐⭐ |
| **Những gì App Business account** | Thông tin tài khoản kinh doanh | ⭐⭐ |
| **Những gì App Business HSM** | Thông tin mẫu thông điệp ( Whats App HSM) | ⭐⭐ |
| **Những gì App message ♪ | Comment | ⭐⭐ |

### Chú thích và phản ứng (bên giao diện)

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Object Comments** | Đường viền / điểm chung — thường gặp ở nhiều nút | ⭐⭐⭐ |
| **Object Likes** | / Các cạnh — thông thường là nhiều nút | ⭐⭐⭐ |
| **Object binh nhì Replies** | Câu trả lời riêng cho một đối tượng | ⭐⭐ |
| **Object Reactions** | Phản ứng trên một đối tượng | ⭐⭐ |
| **Object Sharedposts** | ngưỡng | ⭐ |

### Media & Content

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Video Copyright** | Video copyright | ⭐ |
| **Video List** | danh sách nhạc cho video | ⭐ |
| **Video Poll** | Thăm dò phim nhúng | ⭐ |
| **Video Poll Option** | Single poll option | ⭐ |
| **Image Copyright** | Tác quyền trên tài sản ảnh | ⭐ |
| **Media Fingerprint** | Media fingerprint | ⭐ |
| **Live Video nhập dòng** | Dòng chảy mạnh nhất cho video trực tiếp | ⭐ |

### Công cụ & phát triển

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Application** | Facebook app | ⭐⭐ |
| **App Link Host** | App link host object | ⭐ |
| **Debug Token** | Điểm kết thúc hiển thị gỡ lỗi | ⭐⭐ |
| **Bed nội dung Tìm kiếm** | Tìm kiếm nội dung có hiệu lực (dòng chủ) | ⭐⭐ |

### Other

| Node | Mô tả |
|------|--------|
| Các hình thức trong suốt nhị phân | BinaryTransparencyArtifacts |
| Bằng chứng trong suốt nhị phân | BinaryTransparencyProofs |
| Đề nghị hợp tác giữa CPAS | & Sắp xếp lại |
| Event | Thu thập đồng ruộng và cạnh trên một lễ hội |
| Games IAPProduct | Sản phẩm có thể mua được trong top |
| Group Doc | Group doc |
| Group Message | GroupMessage |
| Milestone | Milestone object |
| Payment | Payment object |
| Báo cáo ảnh hưởng đến trao đổi đe dọa | Báo cáo tác động trên nền tảng |

---

## 🔗 GRAPH API ROOT EDGES

Root edges có thể query trực tiếp, truy cập collections of nodes không thuộc parent node.

| Root Edge | Mô tả |
|-----------|--------|
| **Ads Archive** | Name |
| **Binary icatecate** | BinaryTransparencyArtifacts |
| **Binary Testrive** | BinaryTransparencyProofs |
| **Bed nội dung Tìm kiếm** | Branded content (FB + IG, từ Aug 17 2023) |
| **Debug Token** | Siêu dữ liệu về hiệu bài truy cập |
| ** Thư viện Mẫu Tin KDE** | Name |

---

## 📋 SIDEBAR NAVIGATION (Tất cả endpoints có thể truy cập)

Danh sách đầy đủ từ sidebar (có thể click vào từng endpoint để xem chi tiết fields/edges/operations):

1. `/video` — Video
2. Nhóm người có ảnh hưởng lớn
3. Ads Archive — Quảng cáo được lưu trữ (dòng chủ)
4. Tập ảnh — Tập ảnh chụp
5. Máy liên kết bổ sung — Máy liên kết ứng dụng
6. Application — Facebook app
7. Các hình thức trong suốt nhị phân
8. Bằng chứng trong suốt nhị phân
9. Tìm kiếm nội dung bị đóng kết (dòng chủ)
10. Các băng — Tài liệu về Canvas
11. Canvas Button
12. Canvas Carousel
13. Canvas Footer
14. Canvas Header
15. Canvas Photo
16. Danh sách sản xuất Canvas
17. Các sản phẩm có thể được thiết lập
18. Canvas Text
19. Canvas Video
20. Thư mục cố vấn hợp tác
21. Comment — Facebook comment ⭐
22. Conversation
23. Debug Token ⭐
24. Event
25. Games IAPProduct
26. Group Doc
27. Group Message
28. Image Copyright
29. Name
30. Instagram Oembed
31. Link
32. Comment
33. Mailing Address
34. Media Fingerprint
35. Message ⭐
36. Thư viện mẫu thông điệp (dòng chủ) ⭐
37. Comment
38. Milestone
39. Chú thích đối tượng (dòng động) ⭐
40. Name
41. Comment
42. Object Reactions
43. Object Sharedposts
44. Oembed Page
45. Oembed Post
46. Oembed Video
47. Dữ liệu đảo chính ngoài tuyến đặt tải lên
48. **Page** ⭐⭐⭐
49. Gọi trang đến hành động
50. Page Post ⭐⭐⭐
51. Thay đổi trang
52. Page/insights ⭐⭐⭐
53. Payment
54. Photo ⭐⭐
55. Place
56. Place Tag
57. Place Topic
58. **Post** ⭐⭐⭐
59. Profile
60. Request
61. Shadow IGUser
62. Test User
63. Thread ⭐
64. Báo cáo ảnh hưởng đến trao đổi đe dọa
65. URL ⭐⭐
66. **User** ⭐⭐
67. Video Copyright
68. Video List
69. Video Poll
70. Tùy chọn làm việc trên ảnh động
71. **Những gì App Business account** ⭐⭐
72. **Những gì App message ♪ ⭐⭐
73. **Những gì App Business HSM** ⭐⭐

---

## 🎯 ENDPOINTS QUAN TRỌNG CHO PAGE BOT (Smee Sale & Marketing)

### Tier 1 — Dùng hàng ngày
| Endpoint | Công dụng |
|----------|-----------|
| `/{page-id}/feed` | POST posts lên Page |
| `/{page-id}/photos` | Upload ảnh lên Page |
| `/{page-id}/insights` | Lấy metrics Page |
| `/{page-id}/accounts` | Quản lý Page accounts |
| `/{page-id}/conversations` | Messenger conversations |
| `/{comment-id}` | Đọc chi tiết comment |

### Tier 2 — Thường dùng
| Endpoint | Công dụng |
|----------|-----------|
| `/{post-id}` | Đọc chi tiết post |
| `/{page-id}/posts` | List posts của Page |
| `/{page-id}/picture` | Lấy profile picture |
| `/{object-id}/comments` | List comments |
| `/{object-id}/likes` | List likes |
| `/{object-id}/reactions` | List reactions |

### Tier 3 — Occasionally
| Endpoint | Công dụng |
|----------|-----------|
| `/{page-id}/permissions` | Kiểm tra quyền hạn trang |
| `/{app-id}/products` | App products |
| `/{user-id}/accounts` | Liệt kê trang của người dùng |
| `/search` | Search endpoint |

---

*Generated: 2026-06-09 12:17 GMT+7*
*Version: v25.0 (latest)*
*Source: https://developers.facebook.com/docs/graph-api/reference*
