---
title: "<%% tp.file.title %%>"
slug: "<%% tp.string.title_to_slug(tp.file.title) %%>"
category: area
tags: [fleeting, capture-%%tp.date.now("YYYY")%%]
status: draft
type: fleeting-note
created: <%% tp.date.now("YYYY-MM-DD HH:mm") %%>
---

## Fleeting Note — Captured %%tp.date.now("HH:mm")%%

<!-- Auto-log to daily note via QuickAdd -->
`[[<%* try { print(daily) } catch(e) { print(tp.date.now("YYYY-MM-DD")) } %>>] ` Fleeting capture -> review in next weekly connect phase

- 

> Note: Review status FLEETING -> Promote to atomic note within 7 days OR archive if stale.  
> **Plugin: quickadd** config macro `capture-quick-thought` de auto-append vao daily note.
