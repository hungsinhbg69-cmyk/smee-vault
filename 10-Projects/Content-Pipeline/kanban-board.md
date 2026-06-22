---
title: "Kanban Content Pipeline"
tags: [kanban, content-pipeline]
status: active
type: project-dashboard
created: 2026-06-20
last_updated: {{date}}
---

# Kanban Board — FB Ads Content Workflow

Drag cards between columns to track progress. Auto-categorized by tag.

## Ideas / Brainstorming

```kanban
column_id: ideas
filter_tags: ["tag::idea", "status::draft"]
group_by: status
sort_order: created desc
max_cards: 20
card_fields: [title, tags, status]
empty_message: No pending ideas. Use QuickAdd > New Idea to capture.
```

## Drafting (Dang viet)

```kanban
column_id: drafting
filter_tags: ["status::in-progress"]
group_by: priority
sort_order: created desc
max_cards: 10
card_fields: [title, tags, status, due]
empty_message: No active drafts.
```

## Review (Cho duyet)

```kanban
column_id: review
filter_tags: ["status::review"]
group_by: priority
sort_order: created desc
max_cards: 10
card_fields: [title, tags, status, reviewer]
empty_message: No items for review.
```

## Published (Da dang)

```kanban
column_id: published
filter_tags: ["status::published"]
group_by: platform
sort_order: mtime desc
max_cards: 30
card_fields: [title, tags, status, publish_date, performance]
empty_message: No published content yet.
```

---

## Pipeline Stats (auto-updated)

| Stage | Count | Avg Time | Notes |
|-------|-------|----------|-------|
| Ideas | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "draft").length` | - | draft count |
| Drafting | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "in-progress").length` | - | in progress |
| Review | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "review").length` | - | awaiting review |
| Published | `=dv.pages('"10-Projects/Content-Pipeline"').filter(p => p.status == "published").length` | - | total published |

---

*Created: 2026-06-20 by Smee — Layer 2 Deploy (Kanban Board)*
