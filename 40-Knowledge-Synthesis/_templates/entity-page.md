---
title: "Các mẫu trang thực (Karpathy)"
slug: "entity-page-template"
category: knowledge
tags: [template, karpathy, wiki, entity]
date: 2026-06-16
source: "GitHub Gist - Karpathy LLM Wiki Pattern"
related: ["wiki-schema-versioning-rules", "llm-wiki-architecture"]
status: draft
created: 2026-06-16
type: template
last_updated: 2026-07-13
---


# Mẫu độ đậm đặc

> Template cho entity pages trong LLM Wiki Pattern (Karpathy). Dùng để tạo pages cho các thực thể: người, tổ chức, sản phẩm, địa điểm, khái niệm cụ thể.

## Frontmatter

```yaml
---
title: "Entity Name"
slug: "entity-name"
category: concepts
tags: [tag1, tag2]
date: YYYY-MM-DD
source: "..."
related: []
status: draft
type: entity
entity_type: person|organization|product|place|concept
---
```

## Template Body

# Entity Name

## Overview
Tóm tắt một tập trước thực thể này là gì và tại sao nó quan trọng.

## Key Attributes
- Attribute 1: value
- Attribute 2: value
- Attribute 3: value

## History / Evolution
Dòng thời gian hoặc sự phát triển thời gian của thực thể này.

## Relationships
- Related to: [[related-note-1]]
- Contrasts with: [[related-note-2]]
- Predecessor: [[related-note-3]]

## Sources
- [Source Name](https://example.com) — Thay thế bằng nguồn URL và ngày truy cập

## Notes
Bất cứ quan sát nào khác, mâu thuẫn hay phát triển sự hiểu biết.

---

*Created: YYYY-MM-DD-DD cập nhật cuối cùng: YYYY-MM-DDD*
