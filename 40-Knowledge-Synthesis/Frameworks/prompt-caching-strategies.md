---
title: "prompt-caching-strategies"
slug: "prompt-caching-strategies"
category: frameworks
tags: [obsidian-cleanup, auto-added]
status: draft
type: framework
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "Prompt Architecture — Tối Ưu Prompt Caching"
tags: [prompt-engineering, caching, performance, cost-optimization]
aliases: [Prompt Caching, Cache Optimization]
created: 2026-06-18
parent: prompt-architecture-overview.md
---

# Prompt Architecture — Tối Ưu Prompt Caching

## 🎯 Tại Sao Prompt Caching Quan Trọng?

Prompt caching không chỉ là "tốc độ" — nó là **kiến trúc chi phí**. Giảm 90% input token cost + 80% latency = khác biệt lớn khi scale.

## 📊 Cơ Chế Hoạt Động (OpenAI, 06/2026)

### Cache Routing
- Request được route đến server dựa trên **hash của prefix đầu prompt** (~256 tokens đầu)
- Exact prefix match → cache hit
- Không match → full processing + cache prefix cho lần sau

### Điều Kiện Kích Hoạt
- Tự động enabled cho prompts ≥ **1024 tokens**
- Requests < 1024 tokens: `cached_tokens` = 0
- Rate limit ~15 requests/minute per unique prefix (vượt quá → overflow)

### Cache Retention Policies

| Policy | Models Hỗ Trợ | Thời Gian | Cơ Chế |
|--------|--------------|-----------|--------|
| In-memory | gpt-4o+, trừ gpt-5.5+ | 5-10 phút (max 1h) | Volatile GPU memory |
| Extended (24h) | gpt-5.x, gpt-4.1 | Max 24h | Offloaded to GPU-local storage |

## 🏗️ Cấu Trúc Prompt Tối Ưu Cache

### Nguyên Tắc Vàng: STATIC → DYNAMIC

```
┌─────────────────────────────────┐ ← Cacheable (prefix)
│ System prompt rules             │
│ Output format spec              │
│ Few-shot examples               │
│ Tool definitions                │
│ Image references (identical)    │
├─────────────────────────────────┤
│ User-specific content           │ ← Variable (not cached)
│ Dynamic context                 │
│ Personalized data               │
└─────────────────────────────────┘
```

### Concrete Example

```python
# ✅ TỐI ƯU — Static prefix, dynamic suffix
prompt = """
Bạn là trợ lý marketing. Luôn trả về JSON.
Fields: audience (string), insights (array), recommendations (array).
Example: {"audience": "millennials", "insights": [...], ...}

[Tool definitions here - identical across requests]
[Few-shot examples here - identical across requests]
""" + f"""
Dữ liệu khách hàng: {customer_data}
Sản phẩm: {product_name}
Ngân sách: {budget}
"""

# ❌ KÉM — Dynamic content trộn vào prefix
prompt = f"""
Khách hàng {customer_data} cần marketing cho {product_name}.
Bạn là trợ lý marketing. Luôn trả về JSON.
Fields: audience, insights, recommendations.
Ngân sách: {budget}

[Tool definitions here]
[Few-shot examples here]
"""
```

## 🔧 Advanced Techniques

### 1. prompt_cache_key Parameter
```json
{
  "model": "gpt-5.5",
  "input": [...],
  "prompt_cache_key": "marketing_v2_062026"
}
```
- Custom key để control routing và improve cache hit rate
- Dùng khi nhiều requests share common prefix nhưng khác model/params
- **Quan trọng:** Giữ mỗi unique prefix-key combo < 15 req/min

### 2. Structured Output + Caching
Schema structured output là **prefix** của system message → được cache cùng lúc.
```json
{
  "model": "gpt-5.5",
  "input": [...],
  "response_format": {"type": "json_schema", "schema": {...}}
}
```

### 3. Image Tokenization Consistency
Images phải có `detail` parameter giống nhau giữa requests:
```json
{"type": "image_url", "image_url": {"url": "...", "detail": "high"}}
```
Thay đổi `detail` → khác tokenization → cache miss.

## 📈 Monitoring Cache Performance

Theo response usage:
```json
{
  "usage": {
    "prompt_tokens": 2006,
    "completion_tokens": 300,
    "prompt_tokens_details": {
      "cached_tokens": 1920  // ← Monitor这个数字
    }
  }
}
```

**Metrics cần track:**
- `cached_tokens / prompt_tokens` ratio → target > 80%
- Cache hit rate trong OpenAI Usage Dashboard
- Latency delta giữa cached vs non-cached requests

## ⚠️ Common Mistakes

1. **Đặt dynamic content ở đầu prompt** → cache miss every time
2. **Thay đổi tool definitions mỗi request** → mất cache prefix match
3. **Không dùng prompt_cache_key khi scale** → overflow rate cao
4. **Dùng different image detail levels** → tokenization mismatch
5. **Assume caching improves output quality** → chỉ improve speed/cost, không thay đổi output

## 🔬 Self-Critique: 3 Lần Phản Biện

### Phán biện 1: Prompt Caching có worth cái complexity không?
→ Với local models (Ollama) của Hùng: ít quan trọng hơn cloud API. Nhưng khi deploy lên cloud hoặc scale → critical. Quy tắc: cache optimization cho production, ignore cho prototyping.

### Phán biện 2: Extended caching 24h có privacy issue?
→ KV tensors được offloaded, original content giữ trong memory. Same organization only. Risk thấp, acceptable cho most use cases.

### Phán biện 3: prompt_cache_key — có cần thiết không?
→ Chỉ cần khi >15 req/min cho cùng prefix. Với Hùng's workflow (Facebook bot comments), thường <5 req/min → tự động routing đủ. Dùng khi scale lên batch processing.

---
*Research date: 2026-06-18 | Sources: OpenAI Prompt Caching docs, API reference*
