---
title: "Facebook Graph API Reference — Tổng Hợp (2026-06-09)"
slug: "facebook-ads-comprehensive-guide-to-facebook-graph-api-v25"
category: resource
tags: [vault-maintenance]
status: reference
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
3. **Batch requests** — Multiple API requests trong 1 call
4. **Debug requests** — Debug API requests
5. **Handle errors** — Xử lý common errors
6. **Field expansion** — Limit objects returned + nested requests
7. **Secure requests** — Secure API requests
8. **Resumable Uploads API** — Upload files

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
| **Message** | Message trong Facebook messaging | ⭐⭐ |
| **Thread** | Thread (Messenger) | ⭐⭐ |
| **Conversation** | Conversation object | ⭐⭐ |
| **Page/insights** | Single Insights metric tied to Page/App/Post | ⭐⭐⭐ |
| **Page Call To Action** | Page's call-to-action | ⭐⭐ |
| **Page Upcoming Change** | Notification of page upcoming changes | ⭐ |
| **URL** | Shares, app links, Open Graph objects for a URL | ⭐⭐ |
| **Profile** | Profile object | ⭐ |
| **Album** | Photo album | ⭐ |
| **Event** | Event object | ⭐ |
| **Place** | Place object | ⭐ |
| **Place Tag** | Person tagged at place/photo/post | ⭐ |
| **Place Topic** | Category of a place Page | ⭐ |
| **Link** | Link shared on a wall | ⭐ |
| **Mailing Address** | Mailing address object | ⭐ |
| **Request** | Request object | ⭐ |
| **Test User** | Test user object | ⭐ |

### Ads & Marketing Objects

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Adgroup** | Ad object (visual display + ad set association) | ⭐⭐⭐ |
| **Canvas** | Canvas document (fullscreen ad) | ⭐⭐ |
| **Canvas Button** | Button inside canvas | ⭐ |
| **Canvas Carousel** | Carousel inside canvas | ⭐ |
| **Canvas Footer** | Footer of canvas | ⭐ |
| **Canvas Header** | Header inside canvas | ⭐ |
| **Canvas Photo** | Photo inside canvas | ⭐ |
| **Canvas Product List** | Product list inside canvas | ⭐ |
| **Canvas Product Set** | Product set inside canvas | ⭐ |
| **Canvas Text** | Text element of canvas | ⭐ |
| **Canvas Video** | Video inside canvas | ⭐ |
| **Collaborative Ads Directory** | Directory of collaborative ads businesses | ⭐ |
| **Extended Credit Allocation Config** | Credit line sharing between business portfolios | ⭐ |
| **Offline Conversion Data Set Upload** | Subset of Offline Event Data Set | ⭐ |
| **Ads Archive** | Archived ads (root edge) | ⭐⭐ |

### Instagram Objects

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Instagram Business Asset** | Instagram Business Asset | ⭐⭐ |
| **Instagram Oembed** | InstagramOembed | ⭐ |
| **IGUser** | Instagram User (Shadow IGUser) | ⭐ |

### Messenger & WhatsApp

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Messenger Business Template** | Schema for business message templates | ⭐⭐ |
| **Message Template Library** | List of message templates in app user's library (root edge) | ⭐⭐ |
| **WhatsApp Business Account** | WhatsApp Business Account info | ⭐⭐ |
| **WhatsApp Business HSM** | Message template info (WhatsApp HSM) | ⭐⭐ |
| **WhatsApp Message Template** | WhatsApp message template | ⭐⭐ |

### Comments & Reactions (Common Edges)

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Object Comments** | /comments edge — common to multiple nodes | ⭐⭐⭐ |
| **Object Likes** | /likes edge — common to multiple nodes | ⭐⭐⭐ |
| **Object Private Replies** | Private replies for an object | ⭐⭐ |
| **Object Reactions** | Reactions on an object | ⭐⭐ |
| **Object Sharedposts** | /object/sharedposts edge | ⭐ |

### Media & Content

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Video Copyright** | Video copyright | ⭐ |
| **Video List** | Playlist for videos | ⭐ |
| **Video Poll** | Embedded video poll | ⭐ |
| **Video Poll Option** | Single poll option | ⭐ |
| **Image Copyright** | Copyright on image asset | ⭐ |
| **Media Fingerprint** | Media fingerprint | ⭐ |
| **Live Video Input Stream** | Ingest stream for live video | ⭐ |

### Apps & Developer Tools

| Node | Mô tả | Quan trọng |
|------|--------|-----------|
| **Application** | Facebook app | ⭐⭐ |
| **App Link Host** | App link host object | ⭐ |
| **Debug Token** | Debug token endpoint | ⭐⭐ |
| **Branded Content Search** | Branded content search (root edge) | ⭐⭐ |

### Other

| Node | Mô tả |
|------|--------|
| Binary Transparency Artifacts | BinaryTransparencyArtifacts |
| Binary Transparency Proofs | BinaryTransparencyProofs |
| CPASAdvertiser Partnership Recommendation | Retailer-brand pair + advertiser recommendation |
| Event | Get fields and edges on an Event |
| Games IAPProduct | In-app-purchaseable product |
| Group Doc | Group doc |
| Group Message | GroupMessage |
| Milestone | Milestone object |
| Payment | Payment object |
| Threat Exchange Impact Report | Partner on-platform impact report |

---

## 🔗 GRAPH API ROOT EDGES

Root edges có thể query trực tiếp, truy cập collections of nodes không thuộc parent node.

| Root Edge | Mô tả |
|-----------|--------|
| **Ads Archive** | Returns archived ads based on search |
| **Binary Transparency Artifacts** | BinaryTransparencyArtifacts |
| **Binary Transparency Proofs** | BinaryTransparencyProofs |
| **Branded Content Search** | Branded content (FB + IG, từ Aug 17 2023) |
| **Debug Token** | Metadata about access token |
| **Message Template Library** | Message templates in app user's library |

---

## 📋 SIDEBAR NAVIGATION (Tất cả endpoints có thể truy cập)

Danh sách đầy đủ từ sidebar (có thể click vào từng endpoint để xem chi tiết fields/edges/operations):

1. `/video` — Video
2. Adgroup — Ad object
3. Ads Archive — Archived ads (root edge)
4. Album — Photo album
5. App Link Host — App link host
6. Application — Facebook app
7. Binary Transparency Artifacts
8. Binary Transparency Proofs
9. Branded Content Search (root edge)
10. Canvas — Canvas document
11. Canvas Button
12. Canvas Carousel
13. Canvas Footer
14. Canvas Header
15. Canvas Photo
16. Canvas Product List
17. Canvas Product Set
18. Canvas Text
19. Canvas Video
20. Collaborative Ads Directory
21. Comment — Facebook comment ⭐
22. Conversation
23. Debug Token ⭐
24. Event
25. Games IAPProduct
26. Group Doc
27. Group Message
28. Image Copyright
29. Instagram Business Asset ⭐
30. Instagram Oembed
31. Link
32. Live Video Input Stream
33. Mailing Address
34. Media Fingerprint
35. Message ⭐
36. Message Template Library (root edge) ⭐
37. Messenger Business Template ⭐
38. Milestone
39. Object Comments (common edge) ⭐
40. Object Likes (common edge) ⭐
41. Object Private Replies
42. Object Reactions
43. Object Sharedposts
44. Oembed Page
45. Oembed Post
46. Oembed Video
47. Offline Conversion Data Set Upload
48. **Page** ⭐⭐⭐
49. Page Call To Action ⭐⭐
50. Page Post ⭐⭐⭐
51. Page Upcoming Change
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
64. Threat Exchange Impact Report
65. URL ⭐⭐
66. **User** ⭐⭐
67. Video Copyright
68. Video List
69. Video Poll
70. Video Poll Option
71. **WhatsApp Business Account** ⭐⭐
72. **WhatsApp Message Template** ⭐⭐
73. **WhatsApp Business HSM** ⭐⭐

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
| `/{page-id}/permissions` | Check page permissions |
| `/{app-id}/products` | App products |
| `/{user-id}/accounts` | List user's pages |
| `/search` | Search endpoint |

---

*Generated: 2026-06-09 12:17 GMT+7*
*Version: v25.0 (latest)*
*Source: https://developers.facebook.com/docs/graph-api/reference*
