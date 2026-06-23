---
title: "Vault Command Center"
slug: "vault-command-center"
category: dashboard
tags: [meta, dashboard, command-center]
status: active
type: hub
created: 2026-06-20
last_updated: 2026-06-20
---

# 🧠 Vault Command Center

> [[Protocol]] — Central hub for all vault queries and project management.
> Updated daily by Smee agent during session start.

---

## 🔴 ACTIVE PROJECTS

```dataview
TABLE status AS "Status", last_updated AS "Updated"
FROM "10-Projects"
WHERE status = "active" OR status = null
SORT file.name ASC
```

## ✅ TASKS — OVERDUE (Ưu tiên cao nhất)
> Tasks past deadline. Action required now.

```tasks
not done
due before today
sort by due desc
group by priority
```

## 📋 TASKS — DUE THIS WEEK
> Near-future workload. Plan your time around these dates.

```tasks
not done
due after today -7 days
due before next week monday
sort by due asc
group by priority
```

## 🔥 THIS MONTH (Extended View)
> Upcoming work beyond this week. Prepare in advance.

```tasks
not done
due after this week monday
due before end of month
sort by due asc
group by project
```

## 📥 INBOX (Chưa xử lý)

```dataview
TABLE file.size AS "Size"
FROM "01-Inbox"
SORT file.name ASC
```

## 🔥 RECENT CAPTURES (30 ngày qua)

```dataview
TABLE created, status, type as "Type"
FROM "40-Knowledge-Synthesis" OR "02-Daily" 
WHERE created >= date(today) - 30 days AND file.name != this.file.name
SORT created DESC
LIMIT 15
```

## 📊 KNOWLEDGE HEALTH

### Notes by Category (Atomic = Durable Knowledge)

```dataview
TABLE length(rows) AS "Count"
FROM "40-Knowledge-Synthesis/Insights" OR "40-Knowledge-Synthesis/Frameworks" OR "40-Knowledge-Synthesis/Concepts"
WHERE type = "atomic-note" OR type = "framework" OR type = "concept"
GROUP BY type
```

### Orphan Notes (No Backlinks — cần connect)

```dataview
TABLE length(file.inlinks) AS "Backlinks"
FROM "" 
WHERE !file.name IN ["DASHBOARD", "README", "Protocol", "Tag-Taxonomy"] AND length(file.inlinks) = 0
SORT file.name ASC
LIMIT 20
```

## 📚 CONTENT CALENDAR (FB Ads Content Pipeline)

```dataview
TABLE status, tags AS "Tags"
FROM "30-Resources/Facebook-Ads" OR "40-Knowledge-Synthesis/Frameworks"
WHERE contains(tags, "content") OR type = "framework"
SORT file.name ASC
LIMIT 15
```

## 🗂️ VAULT STATISTICS

| Metric | Value |
|--------|-------|
| Total Markdown Files | See below |
| Active Projects | Query above |
| Unresolved Links | Check [[Vault-Quick-Ref]] |
| Smart Connections Index | 186+ notes embedded |

---

*Created: 2026-06-20 by Smee — Layer 2 Deploy (Dataview Dashboard)*  
*Updated: 2026-06-20 — Tasks plugin queries replace raw TABLE for task views.*
