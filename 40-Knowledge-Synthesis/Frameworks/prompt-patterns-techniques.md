---
title: Khuyên giục kiến trúc — Mẫu mực và kỹ thuật
slug: prompt-patterns-techniques
category: knowledge
tags:
- prompt-engineering
- patterns
- few-shot
- chain-of-thought
status: draft
type: framework
created: 2026-06-18
last_updated: '2026-07-14'
aliases:
- Prompt Patterns
- Prompting Techniques
parent: prompt-architecture-overview.md
---

# Prompt Architecture — Patterns & Techniques (Cập Nhật 06/2026)

## 📋 Tổng Quan Các Pattern Hiệu Quả Nhất

### 1. mẫu xuất đã cấu trúc

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

#### Định dạng xuất bị hạn chế
Claude mạnh về XML-tagged output:
```
<analysis>
  <audience>Millennials aged 25-35</audience>
  <insights>...</insights>
</analysis>
```

### 2. Ít học mẫu

#### Mẫu: Những gương trong văn cảnh
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

### 3 Mẫu hình chuỗi tư duy

#### CoT chuẩn (cho mô hình lý luận)
```
Hãy suy nghĩ từng bước:
1. Xác định audience chính
2. Phân tích pain points
3. Đề xuất content angles
4. Viết recommendations
```

#### Co- conni chính (công việc tự xác định)
```
Hãy đưa ra 3 cách tiếp cận khác nhau cho task này, 
sau đó chọn cách tốt nhất và giải thích tại sao.
```

**Khi nào dùng:**
- _lý luận phức tạp, quyết định đa bước
- Phân loại đơn giản, rút gọn
- ⚠️ Reasoning models: CoT tự động trong nội bộ (không cần explicit)
- ⚠️ GPT models: Cần explicit CoT instructions

### 4 gợi ý đóng vai trò

```
Bạn là một chuyên gia marketing với 10 năm kinh nghiệm 
trong ngành FMCG tại Việt Nam. Bạn am hiểu tâm lý tiêu dùng 
Việt Nam và thành thạo Facebook Ads.
```

**Best practice:**
- Role phải SPECIFIC (không generic "bạn là AI assistant")
- Bao gồm chuyên môn miền và kinh nghiệm cấp
- Match role với task context

### 5 Người được huấn luyện

```
RULES:
- Không quá 300 từ
- Chỉ dùng tiếng Việt
- Không dùng từ "tuyệt vời", "hấp dẫn"
- Format: bullet points, không paragraphs
```

**Sự hạn chế:**
1. **Hard constraints** (không thỏa = fail): word count, language, format
2. **Soft constraints** (ưu tiên nhưng có exception): tone, style
3. **P tương thích** (có-có: ví dụ, cấu trúc chi tiết

### 6 Gương tốt về sự cải thiện

```
BƯỚC 1: Tạo draft content cho sản phẩm X
BƯỚC 2: Review draft — chỉ ra 3 điểm yếu
BƯỚC 3: Cải thiện dựa trên review
BƯỚC 4: Final polish với tone Y
```

**Hãy tạo ra nội dung, thế hệ mã hóa, phân tích phức tạp.

## _ Mẫu đặc trưng (06/2026)

### Mô hình lý luận (o-series)
- **Minimal prompts work best** — model tự fill gaps
- Explicit CoT không cần thiết (internal reasoning)
- Nhiệm vụ mơ hồ G spiritsi: "Hãy phân tích những tài liệu này và nói cho tôi biết cái gì còn thiếu"
- Kế hoạch đa bước: "Hãy giải quyết vấn đề này thành từng bước, rồi giải quyết từng bước"

### Mô hình GPT (giầy ngựa)
- **Neted chỉ thị rõ ràng** — ít khoan dung của mơ hồ
- Chương trình xuất được cấu trúc + định dạng rõ cần thiết
- Những chỉ dẫn từng bước một được ưu tiên hơn những lời nhắc mở
- Tốt cho thực hiện: "Hãy ghi 5 Facebook Các biến thế dựa trên phân tích này"

### Claude Models
- Thẻ XML hoạt động tốt nhất cho đầu vào/ đầu ra có cấu trúc
- Văn cảnh dài quản lý cấp trên — tốt cho các công việc nặng nề tài liệu
- Hệ thống nhắc nhở sự kiên trì trên các lượt (không giống như OpenAI hướng dẫn)

## _Trích dẫn cấu trúc mẫu

### Cấu trúc mẫu đã sẵn sàng
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
*R năng lượng ngày: 2026-06-18 Nguồn: OpenAI API Bác sĩ, Sổ nấu ăn Antropic, nhắc nhở Guide.ai, các điểm tập thể.
