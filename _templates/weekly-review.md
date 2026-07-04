---
title: "Weekly Review — <%% tp.date.now('w') %%>"
slug: "weekly-review-<%% tp.date.now('YYYY-MM-DD') %%>"
category: meta
tags: [review, weekly, workflow]
status: active
type: weekly-review
created: <%% tp.date.now("YYYY-MM-DD") %%>
last_updated: <%% tp.date.now("YYYY-MM-DD") %%>
---

# 📋 Weekly Review — <%% tp.date.now("dddd, MMMM Do YYYY") %%>

## ▸ Quick Actions (QuickAdd Macros)
| Action | Macro | Description |
|--------|-------|-------------|
| 📥 Capture Note | `capture-new-note` | Auto frontmatter + smart-connections link |
| 💭 Fleeting Thought | `capture-quick-thought` | Quick-capture to daily note |
| 📊 Weekly Init | `review-weekly-init` | Open this review template |

---

## ▸ Daily Notes Review (Past 7 Days)

**Plugin: dataview + calendar** — Real-time scan qua daily notes

```dataview
LIST FROM "02-Daily"
WHERE file.name >= date("<%% tp.date.now("YYYY-MM-DD") %%>") - dur(6 days)
  AND file.name <= "<%% tp.date.now("YYYY-MM-DD") %%>"
SORT file.name DESC
```

**Action:** Scan each daily note for captures that need promotion to atomic notes.

---

## ▸ Inbox Zero

**Plugins: quickadd + templater** — dùng macro `capture-quick-thought` để process

### Unprocessed Items from 01-Inbox/
```dataview
LIST FROM "01-Inbox"
SORT file.mtime DESC
```

- [ ] Move to correct PARA folder → update frontmatter  
- [ ] Delete stale/fleeting items  
- **Goal: Empty inbox before moving on**

---

## ▸ Task Audit — obsidian-tasks-plugin + cmdr

**Plugin: obsidian-tasks-plugin** — All active tasks auto-listed

### Overdue Tasks (TIGHTEST)
```tasks
not done
is overdue
exclude id:: 
group by file.path
```

### This Week's Priority Tasks
```tasks
not done
due during this week
sort by priority
```

**Action:** Pick ≤ 5 tasks for this week. Mark rest as deferred or delete.  
**Quick Command (cmdr plugin):** `T+T` to convert selected text into task-item

---

## ▸ Projects Status — kanban + dataview

**Plugins: kanban + dataview + project-command-center**

````dataview
TABLE status as "Status", type as "Focus"
FROM "10-Projects"
WHERE status = "active" OR status = "researching"
SORT file.mtime DESC
````

For each active project, answer:
1. ✅ What's the NEXT action on this project?
2. **Plugin: kanban** — drag into kanban board columns (Ready → Doing → Review)

---

## ▸ Tag Hygiene — tag-wrangler

**Plugin: tag-wrangler** — Merge, rename, cleanup tags trong Batch Mode

### Recent Tag Usage (last 14 days)
```dataview
TABLE file.name as "Note"
WHERE any(file.tags, t => date("<%% tp.date.now("YYYY-MM-DD") %%>") - dur(14 days) < file.mtime)
FLATTEN file.tags as tag
SORT file.mtime DESC
LIMIT 50
```

- [ ] Merge misspelled tags (#Status/draft → #status/draft)  
- [ ] Combine redundant concepts via tag-wrangler  
- [ ] Archive unused tags from last quarter

---

## ▸ Orphaned Notes Scan

**Plugin: smart-connections + omnisearch** — find notes without backlinks

```dataview
TABLE length(file.outlinks) as "Outbound Links"
WHERE file.folder = "40-Knowledge-Synthesis" OR file.folder = "30-Resources"
WHERE length(file.outlinks) < 2
SORT length(file.outlinks) ASC
LIMIT 20
```

**Action:** Create backlinks from Smart Connections suggestions. Every new note MUST have ≥1 outbound link (Protocol Section 6).

---

## ▸ Vault Quality — git + metadata-menu

**Plugins: obsidian-git + metadata-menu + remotely-save**

- [ ] Git status clean? → commit if needed
- [ ] Encoding check with **metadata-extractor** export
- [ ] Broken links via **omnisearch**: paste `[[` to find dead refs
- [ ] File growth trend: review **VAULT-ANALYTICS.md** for charts

---

## ▸ Reflections

### What worked well this week:


### What didn't work:


### Insight of the week:


### Next week priorities (max 3):



---

*Weekly Review Template · Tích hợp 14+ plugins: periodic-notes, calendar, tasks-plugin, dataview, tag-wrangler, kanban, templater, quickadd, smart-connections, omnisearch, obsidian-git, metadata-menu, remotely-save, cmdr*
