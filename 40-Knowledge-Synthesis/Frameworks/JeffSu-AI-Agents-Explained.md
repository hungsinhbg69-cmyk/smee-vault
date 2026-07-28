---
title: JeffSu - Các đặc vụ viên được giải thích rõ ràng
slug: jeffsu-ai-agents-explained
category: knowledge
tags:
- jeffsu
- ai-agents
- llm
- workflow
- prompt-engineering
status: draft
type: framework
created: 2026-06-18
last_updated: '2026-07-14'
source: NotebookLM "JeffSu Master Learning"
---

# Các đặc vụ AI — Giải thích rõ ràng (từ JeffSu)

## Dòng chảy làm việc tương ứng với tác vụ: Sự khác biệt nghiêm trọng
- **AI WorkSn:** Đường dẫn xác định trước, con người quyết định từng bước, LLM Thực hiện tác vụ
- **AI Đặc vụ:** LLM Trở thành người đưa ra quyết định — lý do ra ngoài bước tự động và hành động để đạt được mục tiêu

## Ba thành phần của một đặc vụ AI
1. **Brain:** Mô hình trò chuyện và bộ nhớ (ghi nhớ ngữ cảnh)
2. **Công cụ:** ADIs for Google Shets, Slack, etc.
3. **Brain Stem:** Hệ thống nhắc kiểm soát công cụ sử dụng

## REACT Framework
- **Reason:** Nghĩ qua cách tiếp cận
- **Act:** Thực hiện công việc bằng công cụ
- Cho phép lặp lại tự động hướng tới mục tiêu

## Mỗi ngày, các mô hình lý luận
- **Flash model:** Nhanh, đơn giản (ChatGPT, Claude)
- **Pro/Reasoning:** Kế hoạch phức tạp, tự sửa chữa (Gemini Pro, OpenAI o-series)

## Key Principles
- Đừng mong đợi kết quả hoàn hảo từ một dấu chấm phẩy.
- **Prompt overload Paradox:** Việc thuyết phục nhiều lời nhắc nhở mà không tối ưu hóa hoặc luôn sử dụng lõi trong công việc hàng ngày.
- **" chừng năm câu hỏi"" :** Chỉ dẫn tốt nhất cho việc thu thập ngữ cảnh trước khi đáp ứng cuối cùng.

## Công cụ đặc biệt AISSSPS (bị hỏng)
| Tool | Best For |
|------|----------|
| Claude | Đang ghi mã chức năng vào lần thử đầu tiên |
| ChatGPT | Sau những bảng kiểm tra phức tạp, lý luận |
| Perplexity AI | Dao mổ tìm kiếm — thời gian thực với những lời trích dẫn |
| NotebookLM | Q & A chỉ từ các nguồn đã tải lên (không ảo giác) |
| Gemini | Chức năng của kênh Canvas — viết/run code in chat, xử lý đa sắc thái |

## RAG (thế hệ tái cấu trúc)
- AI tìm kiếm dữ liệu bên ngoài (cacendar, tin tức) trước khi trả lời
- Ngăn chặn ảo giác bằng cách đặt nền phản ứng trong dữ liệu thật

## Backlinks
- [[JeffSu-Channel-Summary]]
- [[JeffSu-Prompt-Engineering]]