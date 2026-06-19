---
title: "prompt-hierarchical-instructions"
slug: "prompt-hierarchical-instructions"
category: frameworks
tags: [obsidian-cleanup, auto-added]
status: draft
type: framework
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "Prompt Architecture — Phân Cấp Instructions"
tags: [prompt-engineering, hierarchical, system-prompts, chain-of-command]
aliases: [Hierarchical Instructions, Chain of Command]
created: 2026-06-18
parent: prompt-architecture-overview.md
---

# Prompt Architecture — Phân Cấp Instructions (Chain of Command)

## 🎯 Khái Niệm Cốt Lõi

Mọi model hiện đại đều tuân thủ **Chain of Command** — thứ tự ưu tiên xử lý instructions từ các nguồn khác nhau. Đây là nền tảng của Prompt Architecture chuyên nghiệp.

## 📐 Model Spec Chain of Command (OpenAI)

Theo `model-spec.openai.com/2025-02-12`:

```
┌─────────────────────────────────────┐
│  developer messages (priority: HIGH) │ ← System rules, business logic
│  user messages (priority: MEDIUM)    │ ← Dynamic inputs, context
│  assistant messages (priority: LOW)  │ ← Model output, becomes context
└─────────────────────────────────────┘
```

### developer vs instructions param
- `instructions` param: high-level behavior override, **áp dụng cho current request**
- `developer` role message: persistent system rules, được model ưu tiên hơn user input
- `instructions` chỉ tồn tại trong current response generation — không persist qua conversation turns

## 🏛️ Claude System Message Architecture

Anthropic Claude dùng **System message block** với đặc thù riêng:

```python
system_prompt = """Bạn là trợ lý AI chuyên về marketing.
Nhiệm vụ: Phân tích audience và tạo content phù hợp.
Giới hạn: Không quá 500 từ, ngôn ngữ tiếng Việt."""

user_message = "Phân tích audience cho sản phẩm skincare..."
```

**Điểm khác biệt Claude so với OpenAI:**
- System message có thể dài hơn mà không bị override bởi user context
- Claude phân biệt rõ "system instruction" vs "user request" — ít bị prompt injection hơn
- Supports **XML tag delimiters** trong system prompt để cấu trúc instructions

## 🔄 So Sánh Thực Tế

| Scenario | developer role | instructions param | Claude System |
|----------|---------------|-------------------|---------------|
| Tone/style rule | ✅ Best practice | ✅ Works but per-request | ✅ Most persistent |
| Business logic | ✅ Core use case | ⚠️ Override risk | ✅ Reliable |
| Per-conversation rules | ❌ Not dynamic | ✅ Flexible | ⚠️ Needs re-send |
| Injection resistance | ✅ Strong | ⚠️ User can override | ✅ Strongest |

## 💡 Best Practices (06/2026)

### 1. Structure developer message như code
```python
# ĐÚNG — Modular system prompt
developer = """
ROLE: Marketing analyst AI
OUTPUT_FORMAT: JSON với fields: audience, insights, recommendations
CONSTRAINTS: Max 500 words, Vietnamese language only
TONE: Professional yet approachable

EXAMPLE_INPUT: "skincare for millennials"
EXAMPLE_OUTPUT: {audience: "...", insights: [...], recommendations: [...]}
"""
```

### 2. Sử dụng XML tags cho complex instructions (Claude)
```xml
<role>Marketing strategist</role>
<output_format>JSON</output_format>
<constraints>Max 500 words, Vietnamese only</constraints>
<examples>
  <example>
    <input>skincare product</input>
    <output>{"audience": "millennials", ...}</output>
  </example>
</examples>
```

### 3. Phân tách static vs dynamic content
```python
# STATIC (đầu prompt — được cache)
system_rules = """Bạn là trợ lý marketing chuyên nghiệp..."""

# DYNAMIC (cuối prompt — thay đổi per request)
user_input = f"""Dữ liệu khách hàng: {customer_data}
Yêu cầu: Phân tích audience cho {product_name}"""
```

## ⚠️ Pitfalls Cần Tránh

1. **Đặt user content trước system rules** → model có thể bị "override" bởi input dài
2. **Quá nhiều developer messages** → context window waste, không thêm giá trị
3. **Sử dụng `instructions` cho persistent rules** → chỉ effective per-request
4. **Không pin model snapshot** → behavior thay đổi giữa các version

## 🔬 Self-Critique: 3 Lần Phản Biện

### Phán biện 1: Chain of Command có thực sự quan trọng với local models?
→ Có. Mixi/Qwen36 (model hiện tại của Hùng) cũng tuân thủ developer > user priority. Tuy nhiên, local models ít rigid hơn cloud models — cần test thực tế trên model cụ thể.

### Phán biện 2: XML tags chỉ có ở Claude?
→ Không. OpenAI cũng hỗ trợ XML trong system messages. Nhưng Claude được optimize đặc biệt cho pattern này (context window caching theo XML boundaries).

### Phán biện 3: instructions param vs developer role — cái nào tốt hơn?
→ `instructions` param tiện cho rapid prototyping, nhưng `developer` role mạnh hơn cho production vì persistent qua multiple turns. Quy tắc: prototype → `instructions`, production → `developer` role.

---
*Research date: 2026-06-18 | Sources: OpenAI Model Spec, Anthropic docs, community benchmarks*
