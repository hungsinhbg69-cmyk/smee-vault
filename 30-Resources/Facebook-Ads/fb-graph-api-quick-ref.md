---
title: "Facebook Graph API — Tham Khảo Nhanh"
slug: "facebook-ads-quick-reference-api-crud-patterns"
category: resource
tags: [vault-maintenance]
status: "draft"
type: reference
created: 2025-12-01
last_updated: 2026-06-24
---

# Facebook Graph API — Tham Khảo Nhanh

_Ghi chú từ tài liệu chính thức của Facebook, 2026-06-09_

---

## 1. Tổng Quan

Graph API là cách chính để đưa dữ liệu vào/ra khỏi nền tảng Facebook. Là HTTP-based API, các ứng dụng (apps) sử dụng nó để:
- Truy vấn dữ liệu
- Đăng story mới
- Quản lý quảng cáo
- Tải lên ảnh
- Và vô số tác vụ khác

Graph API được đặt tên theo khái niệm "social graph" — biểu diễn thông tin trên Facebook, bao gồm 3 thành phần:
- **Nodes** — các đối tượng cụ thể (User, Page, Post, Photo, Comment)
- **Edges** — kết nối giữa các nodes
- **Fields** — thuộc tính/dữ liệu của một node

---

## 2. HTTP

- Tất cả request sử dụng **HTTP/1.1** và **HTTPS**.
- Host URL: `graph.facebook.com`
- Hoạt động với mọi ngôn ngữ có thư viện HTTP (cURL, urllib).
- Có thể sử dụng trực tiếp trong trình duyệt.

Ví dụ:
```
https://graph.facebook.com/facebook/picture?redirect=false
```

---

## 3. Access Tokens

Access token cho phép ứng dụng truy cập Graph API. Hầu hết các endpoints đều yêu cầu token này. Nó thực hiện hai chức năng chính:
1. Cho phép ứng dụng truy cập thông tin người dùng mà không cần mật khẩu.
2. Xác định ứng dụng, người dùng đang sử dụng và loại dữ liệu được phép truy cập.

---

## 4. Nodes

Node là đối tượng riêng biệt với ID duy nhất (unique ID). Ví dụ: User, Page, Post, Photo, Comment.

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

⚠️ **Metadata đã ngừng hoạt động trong Graph API phiên bản v25.0** — không còn trả về siêu dữ liệu nữa. Hãy sử dụng **Graph API Explorer** hoặc tài liệu tham khảo API thay thế. Tính năng này ngừng hoạt động từ ngày **19/05/2026**.

Để xem danh sách các fields của một đối tượng:
```bash
curl -i -X GET "https://graph.facebook.com/USER-ID?metadata=1&access_token=ACCESS-TOKEN"
```

---

## 5. /me Endpoint

Đây là điểm cuối (endpoint) đặc biệt — tự động chuyển đổi thành ID của người dùng hoặc Trang đang sử dụng access token hiện tại.

**Lấy tên và ID của chính mình:**
```bash
curl -i -X GET "https://graph.facebook.com/me?access_token=ACCESS-TOKEN"
```

---

## 6. Edges (Cạnh)

Edge là kết nối giữa hai nodes. Ví dụ: Node User → cạnh photos → các Node Photo.

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

Fields là thuộc tính của node. Mặc định, API trả về tập hợp các fields theo mặc định. Để chỉ định cụ thể các fields muốn nhận:

**Sử dụng tham số `fields` và liệt kê từng field:**
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
Tham khảo hướng dẫn "Chia sẻ lên Facebook" để đăng bài lên Feed, hoặc tài liệu Page API.

**Đăng tin nhắn lên Feed của Trang:**
```bash
curl -i -X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&fields=created_time,from,id,message&access_token=ACCESS-TOKEN"
```

### Cập Nhật (POST)
Cập nhật các fields bằng phương thức POST:
```bash
curl -i -X POST "https://graph.facebook.com/USER-ID?email=YOURNEW@EMAILADDRESS.COM&access_token=ACCESS-TOKEN"
```

### Đọc sau khi ghi
API trả về ID của đối tượng vừa được tạo/cập nhật. Thêm `fields` để lấy thêm thông tin:
```bash
curl -i -X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&fields=created_time,from,id,message&access_token=ACCESS-TOKEN"
```

### Xóa (DELETE)
Xóa các nodes (Post, Photo) bằng phương thức DELETE trên ID:
```bash
curl -i -X DELETE "https://graph.facebook.com/PHOTO-ID?access_token=ACCESSSS-TOKEN"
```

---

## 10. Lỗi

Request không thành công sẽ trả về phản hồi lỗi tiêu chuẩn. Xem phần "Xử lý lỗi" để biết thêm chi tiết.

---

## 11. Webhooks

Đăng ký webhook để nhận thông báo về các thay đổi của nodes hoặc tương tác với nodes.

---

## 12. Phiên Bản

API có nhiều phiên bản, được phát hành hàng quý. Chỉ định phiên bản trong URL:

```bash
curl -i -X GET "https://graph.facebook.com/v4.0/USER-ID/photos?access_token=ACCESS-TOKEN"
```

- **Không thêm version** → Facebook tự động chọn phiên bản cũ nhất hiện có.
- **Nên luôn chỉ định version** trong request.
- Xem phần "Hướng dẫn cách lập phiên bản" và "Nhật ký thay đổi Graph API" để biết tất cả các phiên bản.

---

## 13. Các Bước Tiếp Theo

- Bắt đầu với **Graph API Explorer (Trình khám phá đồ thị)** — thử nghiệm API trực tiếp.
- Chạy request mẫu để lấy dữ liệu.

---

## 14. API, SDK và Nền Tảng Của Facebook

Kết nối giao diện và phát triển trên nhiều nền tảng bằng cách sử dụng các API, SDK và nền tảng khác nhau của Facebook.

---

## Tóm Tắt Các Mẫu Cú Pháp Curl

| Thao tác | Method | Ví dụ |
|---------|--------|-------|
| Đọc node | `GET` | `curl -i -X GET "https://graph.facebook.com/ID?fields=id,name&access_token=TOKEN"` |
| Đọc edge | `GET` | `curl -i -X GET "https://graph.facebook.com/ID/photos?access_token=TOKEN"` |
| Đọc /me | `GET` | `curl -i -X GET "https://graph.facebook.com/me?access_token=TOKEN"` |
| Đăng bài | `POST` | `curl -i -X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&access_token=TOKEN"` |
| Cập nhật | `POST` | `curl -i -X POST "https://graph.facebook.com/ID?field=value&access_token=TOKEN"` |
| Xóa | `DELETE` | `curl -i -X DELETE "https://graph.facebook.com/ID?access_token=TOKEN"` |

---

_Lưu thành file để tra cứu nhanh. Sử dụng `curl.exe` (không dùng alias curl của PowerShell)._
