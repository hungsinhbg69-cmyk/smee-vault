---
title: "prompt-patterns-techniques"
slug: "prompt-patterns-techniques"
category: frameworks
tags: [obsidian-cleanup, auto-added]
status: draft
type: framework
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "Prompt Architecture — Patterns & Techniques"
tags: [prompt-engineering, patterns, few-shot, chain-of-thought]
aliases: [Prompt Patterns, Prompting Techniques]
created: 2026-06-18
parent: prompt-architecture-overview.md
---

# Prompt Architecture — Patterns & Techniques (Cập Nhật 06/2026)

## 📋 Tổng Quan Các Pattern Hiệu Quả Nhất

### 1. Structured Output Patterns

#### JSON Schema Enforcement
OpenAI native support cho structured output — model luôn trả về đúng schema:
```json
{
  "model": "gpt-5.5",
  "input": [{"role": "user", "content": "Phân tích audience..."}],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "marketing_analysis",
      "schema": {
        "type": "object",
        "properties": {
          "audience": {"type": "string"},
          "insights": {"type": "array", "items": {"type": "string"}},
          "recommendations": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["audience", "insights", "recommendations"]
      }
    }
  }
}
```

**Lợi ích:** Parseable output, no regex needed, consistent structure.

#### Delimited Output Format
Claude mạnh về XML-tagged output:
```
<analysis>
  <audience>Millennials aged 25-35</audience>
  <insights>...</insights>
</analysis>
```

### 2. Few-Shot Learning Patterns

#### Pattern: Contextual Examples
```
INPUT: "skincare for sensitive skin"
OUTPUT: {"audience": "Sensitive skin millennials", "tone": "Gentle, reassuring"}

INPUT: "protein powder for athletes"  
OUTPUT: {"audience": "Fitness enthusiasts 18-35", "tone": "Energetic, science-backed"}

INPUT: "{current_product}"
OUTPUT:
```

**Quy tắc few-shot:**
- 2-4 examples đủ (overfitting >5 examples)
- Examples phải cover edge cases của task
- Đặt examples **sau system rules**, trước dynamic content (cache-friendly)

### 3. Chain-of-Thought Patterns

#### Standard CoT (cho reasoning models)
```
Hãy suy nghĩ từng bước:
1. Xác định audience chính
2. Phân tích pain points
3. Đề xuất content angles
4. Viết recommendations
```

#### Self-Consistency CoT (accuracy-critical tasks)
```
Hãy đưa ra 3 cách tiếp cận khác nhau cho task này, 
sau đó chọn cách tốt nhất và giải thích tại sao.
```

**Khi nào dùng:**
- ✅ Complex reasoning, multi-step decisions
- ❌ Simple classification, straightforward extraction
- ⚠️ Reasoning models: CoT tự động trong nội bộ (không cần explicit)
- ⚠️ GPT models: Cần explicit CoT instructions

### 4. Role-Based Prompting

```
Bạn là một chuyên gia marketing với 10 năm kinh nghiệm 
trong ngành FMCG tại Việt Nam. Bạn am hiểu tâm lý tiêu dùng 
Việt Nam và thành thạo Facebook Ads.
```

**Best practice:**
- Role phải SPECIFIC (không generic "bạn là AI assistant")
- Include domain expertise + experience level
- Match role với task context

### 5. Constraint-Based Prompting

```
RULES:
- Không quá 300 từ
- Chỉ dùng tiếng Việt
- Không dùng từ "tuyệt vời", "hấp dẫn"
- Format: bullet points, không paragraphs
```

**Hierarchy of constraints:**
1. **Hard constraints** (không thỏa = fail): word count, language, format
2. **Soft constraints** (ưu tiên nhưng có exception): tone, style
3. **Preferences** (nice-to-have): example inclusion, structure detail

### 6. Iterative Refinement Pattern

```
BƯỚC 1: Tạo draft content cho sản phẩm X
BƯỚC 2: Review draft — chỉ ra 3 điểm yếu
BƯỚC 3: Cải thiện dựa trên review
BƯỚC 4: Final polish với tone Y
```

**适用场景:** Content creation, code generation, complex analysis.

## 🎛️ Model-Specific Patterns (06/2026)

### Reasoning Models (o-series)
- **Minimal prompts work best** — model tự fill gaps
- Explicit CoT không cần thiết (internal reasoning)
- Gỏi ambiguous tasks: "Analyze these documents and tell me what's missing"
- Multi-step planning: "Break this problem into steps, then solve each step"

### GPT Models (workhorse)
- **Need explicit instructions** — less tolerant of ambiguity
- Structured output + clear format specs essential
- Step-by-step instructions preferred over open-ended prompts
- Good for execution: "Write 5 Facebook ad variants based on this analysis"

### Claude Models
- XML tags work best for structured input/output
- Long context handling superior — good for document-heavy tasks
- System prompt persistence across turns (unlike OpenAI instructions)

## 📐 Prompt Template Architecture

### Production-Ready Template Structure
```python
class PromptTemplate:
    # LAYER 1: System Rules (static, cached)
    SYSTEM = """
    ROLE: {role}
    DOMAIN: {domain}
    OUTPUT_FORMAT: {format_spec}
    CONSTRAINTS: {constraints}
    """
    
    # LAYER 2: Examples (static, cached)  
    EXAMPLES = """
    {few_shot_examples}
    """
    
    # LAYER 3: Dynamic Input (variable)
    USER_INPUT = """
    Product: {product_name}
    Target: {target_audience}
    Budget: {budget}
    Channel: {channel}
    """
    
    def build(self, **kwargs):
        return self.SYSTEM.format(**kwargs), self.USER_INPUT.format(**kwargs)
```

## 🔬 Self-Critique: 3 Lần Phản Biện

### Phán biện 1: Few-shot examples có worth token cost không?
→ Với context window 262K của Qwen36, cost thấp. Nhưng nếu >4 examples → diminishing returns. Rule: bắt đầu với 2 examples, thêm chỉ khi benchmark cho thấy improvement >5%.

### Phán biện 2: Chain-of-Thought có quan trọng với local models?
→ Mixi/Qwen36 có reasoning capability nhưng không mạnh như o-series. CoT vẫn hữu ích nhưng không mandatory. Test thực tế: prompt + explicit steps thường tốt hơn implicit CoT trên local models.

### Phán biện 3: Structured output JSON — có bắt buộc dùng response_format?
→ Với OpenAI API: `response_format` type="json_schema" cho reliability cao nhất. Nhưng Claude native JSON support cũng tốt. Local models (Qwen36): cần explicit instruction "Phải trả về JSON hợp lệ" — không có native schema enforcement.

---
*Research date: 2026-06-18 | Sources: OpenAI API docs, Anthropic Cookbook, PromptingGuide.ai, community benchmarks*
