---
title: "Entity Page Template (Karpathy)"
slug: "entity-page-template"
category: concepts
tags: [template, karpathy, wiki, entity]
date: 2026-06-16
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related: ["wiki-schema-versioning-rules", "llm-wiki-architecture"]
status: draft
type: template
---

# Entity Page Template

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
One-paragraph summary of what this entity is and why it matters.

## Key Attributes
- Attribute 1: value
- Attribute 2: value
- Attribute 3: value

## History / Evolution
Timeline or chronological development of this entity.

## Relationships
- Related to: [[related-note-1]]
- Contrasts with: [[related-note-2]]
- Predecessor: [[related-note-3]]

## Sources
- [Source Name](url) — date accessed

## Notes
Any additional observations, contradictions found, or evolving understanding.

---

*Created: YYYY-MM-DD | Last updated: YYYY-MM-DD*
