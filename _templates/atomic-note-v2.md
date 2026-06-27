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
> Tai sao note nay ton tai? Gat voi project/area nao?

[[<%* const path = tp.file.folder(true); const folders = ["10-Projects", "20-Areas", "30-Resources", "40-Knowledge-Synthesis"]; folders.forEach(f => { if (path.includes(f)) print("[" + f + "]"); }) %>

## Key Points
- 

## Source / Evidence
- 

## Connections & Backlinks
> Plugin **smart-connections** se gui y cac note lien quan. Click `sc:` prefix de scan semantic links.

- 

## Tasks
```tasks
folder includes "02-Daily"
has tags
tag includes <% tp.file.selection() %>
```

<!-- Smart Connection Scan: sc: -->
