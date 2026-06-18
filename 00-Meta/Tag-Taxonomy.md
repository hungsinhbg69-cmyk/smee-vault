---
title: "Tag Taxonomy"
slug: "tag-taxonomy"
category: meta
tags: [meta, taxonomy]
status: active
type: reference
created: 2026-06-12
last_updated: 2026-06-12
---

# 🏷 Tag Taxonomy Reference

## Rule: Max 5 tags per note. Keep it small.

### #Project/* — Active projects
```
#Project/Facebook-Marketing
#Project/Client-Site
#Project/Obsidian-Vault
#Project/AI-Agent-Engineering
```

### #Area/* — Ongoing responsibilities
```
#Area/Marketing
#Area/Design
#Area/Coding
#Area/Content-Creation
```

### #Status/* — Note lifecycle
```
#Status/draft       — Created, not reviewed
#Status/active      — Reviewed, in use
#Status/reference   — Stable reference material
#Status/output      — Finalized artifact
#Status/archived    — Completed, no longer active
```

### #Type/* — Content classification
```
#Type/atomic-note   — Permanent knowledge note
#Type/insight       — New discovery/principle
#Type/meeting       — Meeting summary
#Type/literature    — Academic paper note
#Type/experiment    — Hypothesis test log
#Type/daily         — Daily note entry
```

### #Concept/* — Topic tags (create as needed)
```
#Concept/marketing-automation
#Concept/zettelkasten
#Concept/obsidian-workflow
#Concept/vietnamese-psychology
#Concept/sales-funnel
#Concept/content-strategy
#Concept/ai-agent-design
```

### #Tool/* — Tools and platforms
```
#Tool/Obsidian
#Tool/Facebook-Graph-API
#Tool/OpenClaw
#Tool/Ollama
#Tool/Telegram-Bot
#Tool/Notion
```

### #Method/* — Techniques and approaches
```
#Method/capture-first
#Method/bidirectional-linking
#Method/token-efficient-retrieval
#Method/weekly-review
```

## Tag Creation Rules

1. **Lowercase, hyphenated** — `#Concept/marketing-automation` not `#Concept/Marketing Automation`
2. **Consistent naming** — Once created, never rename (use tag-wrangler to merge)
3. **Define before using** — New tag → add to this document first
4. **Max 50 unique tags** — Beyond that = tag entropy → merge duplicates
5. **Nested structure** — Use `/` for hierarchy: `#Project/Alpha`, `#Status/draft`

## Deprecated Tags (merge into)

| Old | New |
|-----|-----|
| #meta | #Type/reference |
| #note | #Type/atomic-note |
| #todo | Check task status instead |
| #book | #Type/literature |

---
*Tag count: ~30 defined, target max 50*
*Last reviewed: 2026-06-12*
