---
title: Prompt Architecture — Tổng Quan
slug: prompt-architecture-overview
category: knowledge
tags:
- prompt-engineering
- architecture
- framework
- ai-agents
status: draft
type: framework
created: 2026-06-18
last_updated: '2026-07-14'
aliases:
- Prompt Architecture Overview
---

# Prompt Architecture — Tổng Quan

## 📌 Định Nghĩa
**Prompt Architecture** là nghệ thuật và khoa học thiết kế cấu trúc prompt sao cho LLM (Large Language Model) luôn cho kết quả chính xác, nhất quán và chất lượng cao. Không phải "viết prompt", mà là **kiến tạo hệ thống instruction** — như lập trình hàm: developer message = function definition, user message = arguments.

## 🏗️ 3 Trụ Cột Chính

### 1. Hierarchical Instructions (Phân Cấp Lệnh)
Mô hình OpenAI Model Spec (`model-spec.openai.com/2025-02-12`) định nghĩa thứ tự ưu tiên:
```
developer (hệ thống) > user (người dùng) > assistant (mô hình)
```
- `developer` messages: quy tắc cố định, business logic — **độ ưu tiên cao nhất**
- `user` messages: input động, context thay đổi
- `assistant` messages: output của model

> 💡 Analogy: developer message = hàm `def`, user message = tham số `args`.

### 2. Prompt Caching Optimization (Tối Ưu Cache)
OpenAI Prompt Caching (06/2026): giảm latency 80%, giảm cost input tokens 90%.
- **Bắt buộc:** static content ở đầu prompt, dynamic content ở cuối
- Cache hit chỉ xảy ra với **exact prefix match** (first ~256 tokens)
- Tự động enabled cho prompts ≥1024 tokens
- `prompt_cache_key` parameter để control routing và improve hit rate

### 3. Mô hình đặc điểm nhắc ( Mô hình Lowai)
- **Rasoning mô hình (o-series):** "the plants" — gi spiriti unsici nhiệm vụ, kế hoạch đa bước, lý luận phức tạp
- **GPT models:** "the workhorses" — giỏi execution, fast & cost-efficient
- Thực hành tốt nhất: o-series cho kế hoạch + GPT cho thực hiện

## 📊 So sánh Provider (06/2026)

| Aspect | OpenAI | Anthropic (Claude) | Microsoft/Azure |
|--------|--------|-------------------|-----------------|
| Cơ chế nhắc hệ thống | `developer` role / `instructions` param | Name | `system` role |
| Caching | Gợi ý cắt tiền tố (tự động) | Comment | Nhắc điều chỉnh và kéo cắt |
| Structured output | JSON schema enforcement | Response format JSON | Function calling |
| Reasoning models | O-series (o3, o4-mini) | Claude Opus/Sonnet Haiku | GPT-5 series |
| Prompt objects | Đang chuẩn bị v1/prompts (Nov 2026) | Template system | Deployment-based |

## 🔑 Core Principles
1. **Sttic  lưỡng tính:** Đặt hướng dẫn đầu tiên, biến cuối
2. **Code-manages:** Lưu trong mã ứng dụng, không riêng biệt tập tin nhắc
3. **Pin hình chụp:** `gpt-5.5-2026-06-xx` cho sự nhất quán sản xuất
4. ** Tự định giá lặp lại:** Xây dựng các phòng thử nghiệm, theo dõi hành vi nhanh qua thời gian
5. **Chain của lệnh được tôn trọng:** Mô hình luôn luôn tôn trọng người phát triển > ưu tiên người dùng

## 📚 Tham Khảo Sâu
- [[prompt-hierarchical-instructions]] — Phân tích chi tiết hệ thống phân cấp
- [[prompt-caching-strategies]] — Tối ưu Prompt Caching
- [[prompt-patterns-techniques]] — Các pattern phổ biến nhất
- [[reasoning-vs-gpt-models]] — So sánh và phối hợp 2 loại model

---
*Reost date: 2026-06-18 Nguồn gốc: OpenAI Dr., Antropic tiến sĩ, Microsoft Azure AI, nhắc nhởGuide.ai, GitHub Cộng đồng*
