---
title: "Task System Wiki"
slug: "task-system-wiki"
category: insight
tags: [tasks, wiki, quick-reference, kanban-integration]
status: active
type: insights
created: 2026-06-20
last_updated: 2026-06-20
---

# 📚 Task System Wiki — Quick Reference

> Everything you need to know about creating, managing, and querying tasks in the vault.

## ✍️ Adding a Task (3 Ways)

### Method 1: Inline on Any Note
Type directly where needed:
```markdown
- [ ] #priority/P2 Write ad copy for campaign {{due:: 2026-07-01}} {{project:: FB Campaign Q3}}
```

**Quick tip:** Use `{{due:: }}` and hit Tab — Templater can auto-fill today's date.

### Method 2: Quick Capture (Inbox)
Use `01-Inbox/quick-capture-template.md` for rapid capture from any context:
- Open quick capture template → paste raw thought → add `{due}`, `{priority}` tags later during triage.

### Method 3: Tasks Insert Command
If using the `/tasks insert` command (from tasks plugin):
1. Press `Ctrl+P` → type "Tasks" → select task insertion mode
2. Fill in due date, priority inline
3. Saves directly to your active daily note or specified folder

## 🏷️ Full Syntax Reference

### Due Date
```markdown
- [ ] Task description {{due:: 2026-07-15}}
```
- Format: `YYYY-MM-DD`
- Relative dates work in queries: `today`, `tomorrow`, `next week monday`
- Past due dates trigger overdue detection

### Priority Tags (Required)
Always use the exact format — no shortcuts:
- `#priority/P1` — 🔴 Critical
- `#priority/P2` — 🟠 High  
- `#priority/P3` — 🟡 Medium
- `#priority/P4` — 🔵 Low

### Project Tags
```markdown
- [ ] #priority/P2 Task {{due:: 2026-07-15}} {{project:: Campaign Name}}
```
- Use kebab-case for project names: `{{project:: fb-campaign-q3}}`
- Enables folder-based filtering in queries

### Status Tags (Optional)
- `#status/doing` — actively working on it
- `#status/waiting` — blocked by someone/something
- `#status/review` — needs review before completion

## 📊 Query Cheat Sheet

| View | Query Block | Use Case |
|------|-------------|----------|
| Overdue | `not done / due before today` | Daily priority check |
| This Week | `not done / due after today -7 days / due before next week monday` | Weekly planning |
| By Project | `folder contains "10-Projects/Name"` | Project status view |
| Completed Today | `done after {{date:: YYYY-MM-DD}}` | Daily recap |

## 🔗 Kanban Integration (Layer 2)

The kanban board connects to tasks through these rules:

1. **Auto-population:** Cards with `{{project:: Name}}` appear in the matching project column
2. **Status columns map to tags:** 
   - "Doing" → `#status/doing` or no status tag
   - "Waiting" → `#status/waiting`
   - "Done" → checked `- [x]` checkbox
3. **Drag-to-update:** Moving a card to Done column auto-checks the task box
4. **Sync direction:** Kanban ↔ Tasks plugin (bidirectional)

### Creating a Task from Kanban
1. Click "+" on target column
2. Enter: `- [ ] #priority/P3 New idea {{due:: }}`
3. Save → appears in tasks queries immediately

## 🔄 Workflow: Capture to Completion

```
Capture (any note / quick-capture) 
  → Triage (daily inbox review, add due/priority/project) 
  → Schedule (assign date or defer to backlog) 
  → Execute (kanban board or daily note checklist) 
  → Complete (check box → auto-tracked in done queries)
```

### Daily Rhythm
- **Morning:** Check overdue + this-week views → pick max 3 focus items
- **During day:** Add tasks inline as they come up
- **Evening:** Review "Done Today" section → capture insights from completed work

---
## Related
- [[vault-command-center]] — Dashboard queries use this task system
- [[kanban-board]] — Kanban integration layer
- [[protocol]] — Capture rules & weekly connect phase

*Created: 2026-06-20 | Quick reference for all vault users.*
