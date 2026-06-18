# Facebook Bot Safety Rules

## Nguyên tắc cơ bản
- Facebook rất nhạy cảm với bot activity
- Làm CHẬM, ĐỪNG quá nhanh
- Học kỹ trước khi làm

## Các quy tắc quan trọng

### 1. Rate Limiting
- Đừng gọi API liên tục quá nhanh
- Giữa các request nên có khoảng 1-2 giây
- Giới hạn số lần gọi trong 1 giờ

### 2. User-Agent
- Luôn dùng `curl.exe` với User-Agent cụ thể
- Đừng dùng PowerShell curl mặc định (bị URL encoding)

### 3. Token Testing
- Dùng `curl.exe` để test token
- Test `/me` endpoint trước khi dùng token dài
- Page Access Token (Never-Expire) coi như không hết hạn

### 4. Posting
- Giới hạn ~100 posts/ngày cho page
- Đừng repost cùng content quá 3 lần/ngày
- Tránh posting liên tục không nghỉ

### 5. Commenting
- Giới hạn ~100 comments/ngày
- Đừng comment cùng template quá nhiều lần
- Nghỉ giữa các comments

### 6. Error Codes Thường Gặp
- 190: Token hết hạn (nhưng Page Token thì hiếm khi)
- 4: Invalid request
- 1: General error
- 32: Page access issue

### 7. Best Practices
- Test token trước khi dùng
- Dùng `curl.exe` thay vì PowerShell curl
- Ghi log các request để theo dõi
- Nghỉ giữa các batch operations
