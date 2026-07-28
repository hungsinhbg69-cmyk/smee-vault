---
title: "<%% tp.date.now('Atomic Note - ') %%><%* const title = await tp.user.quickadd_suggester(['Concept', 'Insight', 'Framework', 'Learning'], 'Type:', ['concept', 'insight', 'framework', 'learning']) %> "
slug: "<%% tp.string.title_to_slug(tp.file.title) %%>"
category: <%%# if (type === "framework") { print("knowledge"); } else if (type === "learning") { print("resource"); } else { print("area"); } %%>
tags: []
status: draft
type: atomic-note
created: <%% tp.date.now("YYYY-MM-DD") %%>
last_updated: <%% tp.date.now("YYYY-MM-DD") %%>
---

# <%% tp.file.title %%>

## Context
> Tai sao lưu ý nay ton tai dự án Gat voi/a nao?

[[<%* const path = tp.file.folder(true); const folders = ["10-Projects", "20-Areas", "30-Resources", "40-Knowledge-Synthesis"]; folders.forEach(f => { if (path.includes(f)) print("[" + f + "]"); }) %>

## Key Points
- 

## Source / Evidence
- 

## Connections & Backlinks
> Plugin ** Thông minh- kết nối** segui y lưu ý nằm. `sc:` Đầu tiên quét liên kết ngữ nghĩa.

- 

## Tasks
```tasks
folder includes "02-Daily"
has tags
tag includes <% tp.file.selection() %>
```

<!-- Thông minh kết nối: sc: -->
