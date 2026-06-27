---
title: "<%% tp.file.title %%>"
slug: "<%% tp.string.title_to_slug(tp.file.title) %%>"
category: project
tags: [meeting, minutes]
status: draft
type: meeting
created: <%% tp.date.now("YYYY-MM-DD") %%>
last_updated: <%% tp.date.now("YYYY-MM-DD") %%>
---

# Meeting - <%% tp.date.now("dddd, MMMM Do YYYY") %%>

## Details
- Attendees: 
- Duration: 
- Project: [[ ]]

<!-- Plugin obsidian-outliner: nhap Ctrl+O de activate outliner mode -->
<!-- Plugin mermaid-tools: dung de ve flow diagram cuoc hep -->

## Agenda
1. 

## Minutes
<%%* tp.insert(outliner_list) *%%>

## Decisions Made
- [ ] 

## Action Items -- auto-linked to tasks-plugin

```tasks
not done
tag includes meeting-%%tp.date.now("YYYY-MM-DD")%%
sort by due
```

### Follow-up Deadlines
| Person | Task | Due | Status |
|--------|------|-----|--------|
|  |  |  | |

## Notes & Resources
> Use pdf-plus for annotated documents from meeting  
> Use excalidraw for visual whiteboard sketches: right canvas -> Excalidraw

---
