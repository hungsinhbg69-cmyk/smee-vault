---
title: JeffSu - Hướng dẫn kỹ thuật nhanh nhấtStencils
slug: jeffsu-prompt-engineering
category: knowledge
tags:
- jeffsu
- prompt-engineering
- ai
- chatgpt
- claude
status: draft
type: framework
created: 2026-06-18
last_updated: '2026-07-14'
source: NotebookLM "JeffSu Master Learning"
related_tags:
- gemini
---

# Hướng dẫn kỹ thuật (từ JeffSu)

## Core Principles

### Thử phạm lỗi trước
Đừng mong đợi kết quả hoàn hảo từ một thời điểm, thúc đẩy hiệu quả liên quan đến sự tinh luyện lặp lại.

### Sự chỉ dẫn bằng phép lạ
**"Trước tiên hỏi tôi 5 câu hỏi sẽ cải thiện phản ứng của bạn sẽ cho tôi."**
- Buộc AI phải tập hợp ngữ cảnh trước khi tạo ra kết xuất cuối cùng
- Cách gây ấn tượng cải thiện chất lượng phản ứng

## Nhắc mẫu và mẫu

### Name
- Dùng hộp gọi cho bộ giữ chỗ (Chỉ thị + E)
- Phân biệt các biến số như [bộ dữ liệu ẩn]
- Tổ chức bằng cách sử dụng trường hợp: soạn thảo, nghiên cứu, mã hóa, phân tích

### Hệ thống đặc vụ AI gây ra sự suy thoái
```
[Role definition]
[Tool usage rules]
[Output format requirements]
[Error handling instructions]
```

### Chương trình tốt nhất cho trò chuyện
- Hỏi rõ câu hỏi trước khi tạo ra
- Dùng lý luận từng bước một cho các tác vụ phức tạp
- Ghi rõ định dạng xuất

## Comment

### Claude
- Tốt nhất cho: ghi chức năng, mã chất lượng cao trên thử đầu tiên
- Sức mạnh: độ chính xác của mã
- Yếu đuối: ít tối ưu hóa tìm kiếm thời gian thực

### ChatGPT
- Tốt nhất: Theo danh sách phức tạp, công việc lý luận
- Độ mạnh: dòng làm việc đa bước phức tạp
- Gợi ý: Dùng mẫu "Xin hỏi 5 câu"

### Perplexity AI
- Tốt nhất cho: Tìm kiếm dao mổ — thực tế thời gian thực với các trích dẫn
- Dùng làm kiểu thay thế cho Google
- Kiểm tra sự kiện nhanh chóng với nguồn gốc

### NotebookLM
- Tốt nhất: Q&A từ các nguồn đã tải lên (không ảo giác)
- Dùng lệnh & mật khẩu để phân tích
- Yêu cầu số 3 ra khỏi đầu và bước hành động từ video dài

### Google Gemini
- ** Đặc điểm Canvas:** Write/run code ()Python/ HTML/JS) trực tiếp trong trò chuyện
- **@YouTube ra lệnh:** Phân tích 2 giờ boardcast, nhận được key cade
- **Các nhắc nhở kỹ sư ngược lại:** Dán ảnh _phụ đề hỏi dấu nhắc gốc
- Đa sắc: Tiến trình văn bản, âm thanh, video, hình ảnh cùng một lúc

## Nhắc quá tải đối tượng
- Vấn đề: Số lượng AI thúc đẩy một số người làm việc hàng ngày mà không tối ưu hóa
- Giải pháp: Tạo thư viện nhanh riêng, kiểm tra và tinh luyện, luôn sử dụng

## Những điểm nổi bật trong sách hướng dẫn mới của Google
- Cách tiếp cận có cấu trúc để thúc đẩy thiết kế
- Name
- Đặc tả xuất với yêu cầu định dạng

## Backlinks
- [[JeffSu-AI-Agents-Explained]]
- [[JeffSu-Channel-Summary]]