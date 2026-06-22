---
title: "Task System Configuration"
slug: "task-system-config"
category: framework
tags: [tasks, dataview, tasks-plugin, priority]
status: active
type: framework
created: 2026-06-20
last_updated: 2026-06-20
---

# 📋 Task System Configuration

> Framework for automated task management using Obsidian Tasks plugin + Dataview.

## 🎯 Priority System

| Level | Tag | Color | Description | When to Use |
|-------|-----|-------|-------------|-------------|
| P1 | `#priority/P1` | 🔴 Red | Critical — must do today or overdue | Blocker, deadline today |
| P2 | `#priority/P2` | 🟠 Orange | High — this week | Important but flexible timing |
| P3 | `#priority/P3` | 🟡 Yellow | Medium — this month | Nice to have, schedule when free |
| P4 | `#priority/P4` | 🔵 Blue | Low — backlog | Tidy up, no rush |

### Priority Rules
- **Max 1–2 tasks per day** are P1. If more → break down or defer some.
- Every task MUST have a priority tag (`#priority/P1` etc). No untagged tasks.
- Weekly review: demote stale P2→P3, promote overdue P3→P2.

## 📊 Tasks Query Dashboard Queries

### Overdue Tasks (Critical View)
```tasks
not done
due before today
sort by due desc
group by priority
```

> ⚠️ This query shows everything past deadline. Action required.

### This Week's Tasks
```tasks
not done
due after today -7 days
due before next week monday
sort by due asc
group by priority
```

> 📅 Your near-future workload. Plan around these dates.

### Project-Linked Tasks (Filter by Folder)
```tasks
not done
folder contains "10-Projects/Your-Project"
sort by priority desc
```

> 🔗 Replace `Your-Project` with actual project folder name. Each active project gets its own filter.

### All Active Tasks (Full View)
```tasks
not done
sort by due asc
group by priority
```

## 🏷️ Task Syntax Reference

Standard Obsidian task syntax extended with tasks plugin properties:

```markdown
- [ ] #priority/P2 🔴 Complete API integration {{due:: 2026-06-25}} {{project:: Facebook Ads Pipeline}}
```

| Property | Format | Example |
|----------|--------|---------|
| Due date | `{{due:: YYYY-MM-DD}}` | `{{due:: 2026-07-01}}` |
| Priority | Tag in task text | `#priority/P2` |
| Project | `{{project:: Name}}` | `{{project:: FB Campaign Q3}}` |
| Status | Inline tag (optional) | `#status/doing`, `#status/waiting` |

## 🔧 Integration Points

### With Daily Notes
- Each daily note has a tasks query block showing relevant items.
- New tasks created from daily notes auto-capture in inbox.

### With Projects
- Every project folder (`10-Projects/*`) can have its own task view using `folder contains` filter.
- Project dashboard template includes task summary section.

### With Kanban (Layer 2)
- Tasks with `{{project:: Name}}` auto-populate into kanban board columns by status.
- Dragging a card updates the underlying `- [ ]` checkbox → marks done in tasks queries.

## 📐 Query Best Practices

1. **Always add due date** — enables overdue detection and sorting.
2. **Use priority tags consistently** — required for `group by priority`.
3. **Tag projects explicitly** — `{{project:: Name}}` enables folder-based filtering.
4. **Review weekly** — clear completed, reschedule overdue, archive stale tasks.

---

*Created: 2026-06-20 | Layer 1 Task System Deploy*
