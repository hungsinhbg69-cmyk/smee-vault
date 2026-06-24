---
title: "prompt-architecture-overview"
slug: "prompt-architecture-overview"
category: frameworks
tags: [obsidian-cleanup, auto-added]
status: draft
type: framework
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "Prompt Architecture — Tổng Quan"
tags: [prompt-engineering, architecture, framework, ai-agents]
aliases: [Prompt Architecture Overview]
created: 2026-06-18
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

### 3. Model-Specific Prompting (Prompt Theo Loại Model)
- **Reasoning models (o-series):** "the planners" — giỏi ambiguous tasks, multi-step planning, complex reasoning
- **GPT models:** "the workhorses" — giỏi execution, fast & cost-efficient
- Best practice: o-series cho planning + GPT series cho execution

## 📊 So sánh Provider (06/2026)

| Aspect | OpenAI | Anthropic (Claude) | Microsoft/Azure |
|--------|--------|-------------------|-----------------|
| System prompt mechanism | `developer` role / `instructions` param | System message block | `system` role |
| Caching | Prompt prefix caching (auto) | Context window caching | Prompt tuning + caching |
| Structured output | JSON schema enforcement | Response format JSON | Function calling |
| Reasoning models | o-series (o3, o4-mini) | Claude Opus/Sonnet Haiku | GPT-5 series |
| Prompt objects | Deprecating v1/prompts (Nov 2026) | Template system | Deployment-based |

## 🔑 Core Principles
1. **Static → Dynamic:** Put instructions first, variables last
2. **Code-managed prompts:** Store in application code, not separate prompt files
3. **Pin model snapshots:** `gpt-5.5-2026-06-xx` cho production consistency
4. **Evaluate iteratively:** Build test suites, monitor prompt behavior over time
5. **Chain of command respected:** Model always honors developer > user priority

## 📚 Tham Khảo Sâu
- [[prompt-hierarchical-instructions]] — Phân tích chi tiết hệ thống phân cấp
- [[prompt-caching-strategies]] — Tối ưu Prompt Caching
- [[prompt-patterns-techniques]] — Các pattern phổ biến nhất
- [[reasoning-vs-gpt-models]] — So sánh và phối hợp 2 loại model

---
*Research date: 2026-06-18 | Sources: OpenAI docs, Anthropic docs, Microsoft Azure AI, PromptingGuide.ai, GitHub community*
