---
title: "Content Pipeline — FB Ads"
slug: "content-pipeline-fb-ads"
category: kanban
tags: [kanban, content, facebook-ads]
status: active
type: kanban-board
created: 2026-06-20
last_updated: 2026-06-20
---

# 📋 Content Pipeline — FB Ads Kanban Board

> Drag cards across columns to move content through pipeline.
> Each card links to source material and atomic notes.

## 🔍 Ideas (Brainstorm)

```dataview
LIST FROM "30-Resources/Facebook-Ads" OR "40-Knowledge-Synthesis/Insights" 
WHERE contains(tags, "idea") AND status = "draft"
SORT file.name ASC
```

## ✏️ Drafting (Đang viết)

```dataview
LIST FROM "" WHERE type = "content-draft" AND status = "in-progress"
```

## ✅ Review (Chờ duyệt)

```dataview
LIST FROM "" WHERE status = "review"
```

## 🚀 Published (Đã đăng)

```dataview
LIST FROM "" WHERE status = "published"
SORT file.mtime DESC
LIMIT 10
```

---

*Created: 2026-06-20 by Smee — Layer 3 Deploy (Kanban Board)*
*Use QuickAdd to create new content cards → auto-categorized into pipeline stage.*
