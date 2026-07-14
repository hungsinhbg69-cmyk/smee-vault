---
title: "Vault Command Center"
slug: "vault-command-center"
category: dashboard
tags: [meta, dashboard, command-center]
status: active
type: hub
created: 2026-06-20
last_updated: 2026-07-14
---

# 🧠 Vault Command Center

> [[Protocol]] — Central hub. Mở đầu mỗi session tại đây.  
> **Plugins active:** Templater · QuickAdd · Dataview · Tasks · Git · Kanban · Smart Connections · Excalidraw

---

## ⚡ QUICK CAPTURE (Hotkeys)

| Action | Hotkey | QuickAdd Choice |
|---|---|---|
| 💭 Quick thought → Daily | `Mod+Shift+Space` | capture-quick-thought |
| 📥 Idea → Inbox | `Mod+Shift+I` | capture-inbox |
| 📝 Atomic note | `Mod+Shift+N` | capture-new-note |
| ✅ Task hôm nay | `Mod+Shift+T` | capture-task-today |
| 🚀 New project | `Mod+Shift+P` | init-new-project |
| 📚 Literature note | — | capture-literature-note |
| 📅 Weekly review | `Mod+Shift+W` | review-weekly-init |
| 🔍 Smart Connections | `Mod+Shift+S` | — |
| 🔎 Omnisearch | `Mod+Shift+O` | — |
| 🔄 Git pull | `Mod+Shift+G` | — |

---

## 🔴 ACTIVE PROJECTS

```dataview
TABLE status AS "Status", last_updated AS "Updated", tags AS "Tags"
FROM "10-Projects"
WHERE status = "active" OR status = "draft"
SORT last_updated DESC
```

## ✅ TASKS — QUÁ HẠN (Action Now!)

```tasks
not done
due before today
sort by due ascending
group by file.link
limit 20
```

## 📋 TASKS — TUẦN NÀY

```tasks
not done
due this week
sort by due ascending
group by priority
limit 30
```

## 📥 INBOX (Chưa xử lý — target < 5)

```dataview
TABLE file.ctime AS "Captured", file.size AS "Size"
FROM "01-Inbox"
SORT file.ctime DESC
```

## 🔥 RECENT KNOWLEDGE (7 ngày)

```dataview
TABLE created AS "Date", category AS "Cat", status AS "Status"
FROM "40-Knowledge-Synthesis" OR "30-Resources"
WHERE created >= date(today) - dur(7 days)
SORT created DESC
LIMIT 10
```

## 📊 VAULT HEALTH SNAPSHOT

### Notes by Status

```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE file.folder != ".obsidian" AND file.folder != "copilot" AND file.folder != "_templates"
GROUP BY status
SORT length(rows) DESC
```

### Orphan Notes (< 2 backlinks)

```dataview
TABLE length(file.inlinks) AS "Backlinks", length(file.outlinks) AS "Outlinks"
FROM "40-Knowledge-Synthesis" OR "30-Resources"
WHERE length(file.inlinks) < 2
SORT length(file.inlinks) ASC
LIMIT 15
```

### Notes Created This Month

```dataview
TABLE created AS "Created", type AS "Type"
FROM "40-Knowledge-Synthesis"
WHERE created >= date(this month)
SORT created DESC
```

## 📚 FACEBOOK ADS PIPELINE

```dataview
TABLE status AS "Status", tags AS "Tags", type AS "Type"
FROM "30-Resources/Facebook-Ads" OR "40-Knowledge-Synthesis/Frameworks"
WHERE contains(tags, "facebook-ads") OR type = "framework"
SORT last_updated DESC
LIMIT 10
```

## 🏘️ BẮC GIANG PROJECTS

```dataview
TABLE status AS "Status", type AS "Type", last_updated AS "Updated"
FROM "40-Knowledge-Synthesis/Real-Estate" OR "30-Resources/Bac-Giang"
SORT last_updated DESC
LIMIT 10
```

---

## 🤖 AGENT NOTES

- **Smee** (vault scope): Xem [[AGENTS.md]] — quy tắc vận hành
- **cli-rest-mcp**: Running on port 27124 — REST API + MCP active
- **Smart Connections**: TF-IDF index, excludes: copilot, templates, archive
- **Last plugin setup**: 2026-07-14 by Antigravity

---

*Dashboard v3 — 2026-07-14 · Rebuilt by Antigravity agent · Professional plugin setup*
