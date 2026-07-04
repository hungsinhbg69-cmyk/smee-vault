---
title: "Vault Command Center"
slug: "vault-command-center"
category: meta
tags: [dashboard, dataview, analytics, automation]
status: active
type: moc
created: 2026-06-27
last_updated: 2026-06-27
---

# Vault Command Center

> Dashboard tích hợp - khai thac **dataview + tasks-plugin + charts + metadata-menu + calendar**  
> Cap nhat REAL-TIME voi Dataview queries. Tu dong sync qua obsidian-git.

## □ Quick Launch (QuickAdd Macros)
| Action | Macro Key | Description |
|--------|-----------|-------------|
| 🔥 New Atomic Note | `capture-new-note` | Auto frontmatter + smart-connections link |
| 💭 Fleeting Thought | `capture-quick-thought` | Quick-capture to daily note via templater |
| 📊 Weekly Review | `review-weekly-init` | Open weekly-review template with dataview scans |

> Import macros: Settings -> QuickAdd -> Manage -> Import `_scripts/quickadd-macro-config.json`

---

## □ Daily Pulse - Latest Notes

**Plugin: dataview + calendar** — Real-time scan across vault folders

```dataview
TABLE length(file.tags) as "Tags", type as "Type"
FROM ""
WHERE file.mtime > date("-30 days") AND file.type != undefined
SORT file.mtime DESC
LIMIT 15
```

---

## □ Active Tasks - All Unfinished

**Plugin: obsidian-tasks-plugin** — Consolidated task view, sortable by priority

```tasks
not done
group by due
sort by priority descending
reverse
```

This Week High Priority
```tasks
not done
due during this week
priority matches /.*/
```

---

## □ Active Projects - Dashboard

**Plugins: dataview + kanban + metadata-menu**

````dataview
TABLE status as "Status", type as "Type", length(file.tags) as "Tags"
FROM "10-Projects"
WHERE status != "archived"
SORT file.ctime DESC
````

> Next: Use **kanban** plugin (Ctrl+P -> Kanban: Create new board) for visual project tracking. Link cards to projects above.

---

## □ Metadata Quality - Recent 7 Days

**Plugin: metadata-menu + templater** — Edit frontmatter via GUI, khng can go tay

### Recently Modified Files
```dataview
TABLE file.mtime as "Modified Last"
FROM ""
WHERE file.mtime > date("-7 days")
SORT file.mtime DESC
LIMIT 20
```

---

## □ Vault Analytics Quick View

**Plugin: charts + obsidian-mind-map + mermaid-tools + obsidian-icon-folder**

1. **Open any note → Mind Map**: Ctrl+P → "MindMap" (plugin obsidian-mind-map)  
2. **Render diagrams inline**: paste ` ```mermaid ` blocks (see VAULT-ANALYTICS.md for templates)  
3. **Customize folder icons**: Settings → obsidian-icon-folder → Add sets

### Growth Chart Template
See `00-Meta/VAULT-ANALYTICS.md` for full chart.json formats and web clipper workflow.

---

## □ Smart Connections Shortcut

**Plugin: smart-connections + omnisearch + copilot**

- **Scans semantic links**: Smart Connections auto-suggests related notes when typing
- **Ctrl+E**: Trigger omnisearch for fuzzy search across entire vault  
- **Right-click → Copilot**: Chat with second brain — AI reads context from SC vectors

---

## □ Workflow Triggers Summary

| Step | Plugin(s) | Action |
|------|-----------|--------|
| Capture notes | quickadd + templater + smart-connections | New atomic/fleeting note auto-created |
| Review weekly | periodic-notes + calendar + tag-wrangler + tasks-plugin | Full weekly audit with task scan |
| Track projects | kanban + dataview + git + mermaid | Kanban board + sprint tracking |
| Sync & backup | obsidian-git + remotely-save | Cloud sync + version control history |
| Visualize data | charts + mind-map + icon-folder | Analytics dashboard + folder icons |
| Search & connect | omnisearch + smart-connections + copilot | Semantic search + AI chat |

---

*Command Center taichop 7+ plugin core.*
*Tham khao[[PROJECT-COMMAND-CENTER]] · [[TASK-ENGINE]] · [[VAULT-ANALYTICS]] · _templates/weekly-review.md*
