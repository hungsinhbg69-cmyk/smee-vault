---
title: "Facebook Graph API — Tham Khảo Nhanh"
slug: "facebook-ads-quick-reference-api-crud-patterns"
category: resource
tags: [vault-maintenance]
status: reference
type: reference
created: 2025-12-01
last_updated: 2026-06-24
---

# Facebook Graph API — Tham Khảo Nhanh

_Ghi chú từ tài liệu chính thức Facebook, 2026-06-09_

---

## 1. Tổng Quan

Graph API là cách chính để đưa dữ liệu vào/ra khỏi nền tảng Facebook. Là HTTP-based API, apps dùng để:
- Query dữ liệu
- Đăng story mới
- Quản lý ads
- Upload ảnh
- Vô số tác vụ khác

Graph API được đặt tên theo khái niệm "social graph" — biểu diễn thông tin trên Facebook, gồm 3 thành phần:
- **Nodes** — đối tượng cụ thể (User, Page, Post, Photo, Comment)
- **Edges** — kết nối giữa các nodes
- **Fields** — thuộc tính/dữ liệu của một node

---

## 2. HTTP

- Tất cả request dùng **HTTP/1.1** và **HTTPS**
- Host URL: `graph.facebook.com`
- Hoạt động với mọi ngôn ngữ có HTTP library (cURL, urllib)
- Có thể dùng trực tiếp trong trình duyệt

Ví dụ:
```
https://graph.facebook.com/facebook/picture?redirect=false
```

---

## 3. Access Tokens

Access token cho phép app truy cập Graph API. Hầu hết endpoints đều yêu cầu. 2 chức năng:
1. Cho phép app truy cập User info mà không cần password
2. Xác định app, User đang dùng, và loại dữ liệu được phép truy cập

---

## 4. Nodes

Node là đối tượng riêng biệt với unique ID. Ví dụ: User, Page, Post, Photo, Comment.

**Truy vấn node:**
```bash
curl -i -X GET "https://graph.facebook.com/USER-ID?access_token=ACCESS-TOKEN"
```

**Phản hồi mặc định (JSON):**
```json
{
  "name": "Your Name",
  "id": "YOUR-USER-ID"
}
```

### Siêu dữ liệu nút (metadata)

⚠️ **metadata đã ngừng hoạt động trong API Đồ thị v25.0** — không còn trả về siêu dữ liệu. Dùng **Trình khám phá API Đồ thị** hoặc tài liệu tham khảo API thay thế. Ngừng hoạt động từ **19/05/2026**.

Xem danh sách fields của một đối tượng:
```bash
curl -i -X GET "https://graph.facebook.com/USER-ID?metadata=1&access_token=ACCESS-TOKEN"
```

---

## 5. /me Endpoint

Điểm cuối đặc biệt — tự động chuyển thành ID của người/Trang có access token đang dùng.

**Lấy tên và ID của chính mình:**
```bash
curl -i -X GET "https://graph.facebook.com/me?access_token=ACCESS-TOKEN"
```

---

## 6. Edges (Cạnh)

Edge là kết nối giữa 2 nodes. Ví dụ: User node → photos edge → Photo nodes.

**Lấy danh sách ảnh của một người:**
```bash
curl -i -X GET "https://graph.facebook.com/USER-ID/photos?access_token=ACCESS-TOKEN"
```

**Phản hồi:**
```json
{
  "data": [
    {
      "created_time": "2017-06-06T18:04:10+0000",
      "id": "1353272134728652"
    },
    {
      "created_time": "2017-06-09T01:13+0000",
      "id": "1353269908062208"
    }
  ]
}
```

---

## 7. Fields (Trường)

Fields là thuộc tính của node. Mặc định trả về tập fields theo mặc định. Để chỉ định fields muốn nhận:

**Dùng tham số `fields` và liệt kê từng field:**
```bash
curl -i -X GET "https://graph.facebook.com/USER-ID?fields=id,name,email,picture&access_token=ACCESS-TOKEN"
```

**Phản hồi:**
```json
{
  "id": "USER-ID",
  "name": "EXAMPLE NAME",
  "email": "EXAMPLE@EMAIL.COM",
  "picture": {
    "data": {
      "height": 50,
      "is_silhouette": false,
      "url": "URL-FOR-USER-PROFILE-PICTURE",
      "width": 50
    }
  }
}
```

---

## 8. Tham Số Phức Tạp

- **List:** Định dạng JSON `["firstitem", "seconditem", "thirditem"]`
- **Object:** Định dạng JSON `{"firstkey": "firstvalue", "secondKey": 123}`

---

## 9. Đăng, Cập Nhật và Xóa

### Đăng (POST)
Tham khảo hướng dẫn "Chia sẻ lên Facebook" để đăng lên Feed, hoặc tài liệu Page API.

**Đăng tin nhắn lên Feed Page:**
```bash
curl -i -X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&fields=created_time,from,id,message&access_token=ACCESS-TOKEN"
```

### Cập Nhật (POST)
Cập nhật fields bằng POST:
```bash
curl -i -X POST "https://graph.facebook.com/USER-ID?email=YOURNEW@EMAILADDRESS.COM&access_token=ACCESS-TOKEN"
```

### Đọc sau khi ghi
API trả về ID của đối tượng vừa tạo/cập nhật. Thêm `fields` để lấy thêm thông tin:
```bash
curl -i -X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&fields=created_time,from,id,message&access_token=ACCESS-TOKEN"
```

### Xóa (DELETE)
Xóa nodes (Post, Photo) bằng DELETE trên ID:
```bash
curl -i -X DELETE "https://graph.facebook.com/PHOTO-ID?access_token=ACCESSSS-TOKEN"
```

---

## 10. Lỗi

Request không thành công → phản hồi lỗi tiêu chuẩn. Xem "Xử lý lỗi" để biết thêm.

---

## 11. Webhooks

Đăng ký webhook để nhận thông báo về thay đổi nodes hoặc tương tác với nodes.

---

## 12. Phiên Bản

API có nhiều phiên bản, phát hành hàng quý. Chỉ định phiên bản trong URL:

```bash
curl -i -X GET "https://graph.facebook.com/v4.0/USER-ID/photos?access_token=ACCESS-TOKEN"
```

- **Không thêm version** → Facebook tự chọn version cũ nhất hiện có
- **Nên luôn chỉ định version** trong request
- Xem "Hướng dẫn cách lập phiên bản" và "Nhật ký thay đổi API Đồ thị" để biết tất cả version

---

## 13. Các Bước Tiếp Theo

- Bắt đầu với **Trình khám phá đồ thị (Graph API Explorer)** — thử nghiệm API trực tiếp
- Chạy request mẫu để lấy dữ liệu

---

## 14. API, SDK và Nền Tảng Của Facebook

Kết nối giao diện và phát triển trên nhiều nền tảng bằng API, SDK, nền tảng khác nhau của Facebook.

---

## Tóm Tắt Curl Patterns

| Thao tác | Method | Ví dụ |
|---------|--------|-------|
| Đọc node | `GET` | `curl -i -X GET "https://graph.facebook.com/ID?fields=id,name&access_token=TOKEN"` |
| Đọc edge | `GET` | `curl -i -X GET "https://graph.facebook.com/ID/photos?access_token=TOKEN"` |
| Đọc /me | `GET` | `curl -i -X GET "https://graph.facebook.com/me?access_token=TOKEN"` |
| Đăng bài | `POST` | `curl -i -X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&access_token=TOKEN"` |
| Cập nhật | `POST` | `curl -i -X POST "https://graph.facebook.com/ID?field=value&access_token=TOKEN"` |
| Xóa | `DELETE` | `curl -i -X DELETE "https://graph.facebook.com/ID?access_token=TOKEN"` |

---

_Lưu thành file để tra cứu nhanh. Dùng `curl.exe` (không PowerShell curl alias)._
