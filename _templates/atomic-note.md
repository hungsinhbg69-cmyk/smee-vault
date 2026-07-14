---
title: "Atomic Note — {{title}}"
slug: "{{title-slug}}"
category: knowledge
tags: []
status: draft # draft | active | superseded
type: atomic-note
created: {{date}}
last_updated: {{date}}
cited_count: 0
related_concepts: 
applied_in: 
difficulty: easy # easy | medium | hard
---

# 🔬 {{title}}

## 📝 One Idea Summary
<%* tR += await tp.system.prompt("One sentence summary: "); *>

## 📖 Explanation
[<small>300-700 words. Clear, precise, no fluff.</small>]

## 🔄 Connections
### Related Concepts
<%* const related = await tp.system.prompt("Related concept (or leave blank): "); if (related?.trim()) { const open = "[" + "["; const close = "]" + "]"; tR += "- " + open + related.trim() + close + "\n"; } *>

### Applied In
<%* tR += "- [[Project-Name]] — how this is used\n"; *>

## 📚 Sources
<%* const sourceTitle = await tp.system.prompt("Source title (or leave blank): "); const sourceUrl = await tp.system.prompt("Source URL (or leave blank): "); if (sourceTitle?.trim()) tR += sourceUrl?.trim() ? "- [" + sourceTitle.trim() + "](" + sourceUrl.trim() + ")\n" : "- " + sourceTitle.trim() + "\n"; *>

---
%% Agent instructions:
- One idea per note. If >2 H2 sections on different topics → split
- 300-700 words target. Short = reusable, linkable
- Promote from daily notes when cited 2+ times
- Every new atomic note MUST have at least 1 backlink same day
- Status: draft → active (when linked 3+) → superseded (when updated)
%%
