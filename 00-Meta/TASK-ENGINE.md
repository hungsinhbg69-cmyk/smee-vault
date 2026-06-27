---
title: "Task Engine Configuration"
slug: "task-engine-configuration"
category: meta
tags: [workflow, tasks, automation]
status: active
type: reference
created: 2026-06-27
last_updated: 2026-06-27
---

# Task Engine Configuration

> Central config cho **obsidian-tasks-plugin** + metadata-menu + calendar integration  
> Custom commands qua **cmdr** plugin để shortcut workflow

## Global Tasks Plugin Block (copy vào every project note)

```tasks
not done
group by heading
sort by priority descending
reverse
hide backlinks
hide id
hide due date
hide cancelled date
hide created date
hide start date
hide modified date
hide task field explanations
```

## Task Priority Convention

| Symbol | Meaning | Auto-color (tasks-plugin) |
|--------|---------|--------------------------|
| P1 | Critical - due this week | red |
| P2 | Important - due this month | orange |
| P3 | Normal - next sprint | yellow |
| P4 | Low priority / nice-to-have | green |

## Quick Commands (cmdr plugin macros)

Configure mỗi command trong Settings -> cmdr:

### Command 1: "Create Task from Selected Text"
Shortcut: T+T
Steps:
1. Select text in any note
2. Press Cmdor Shift+T
3. Templater generates task-item with selected text as description
4. Automatically linked to current project date

### Command 2: "Mark Done + Add Reflection"  
Shortcut: Shift+Enter on task
When marking a task done, prompts for reflection notes before closing

### Command 3: "Weekly Task Brain Dump"
Opens new note in `40-Knowledge-Synthesis/Insights/` withe auto-generated tasks block for all pending items

## Metadata Menu Quick Edits

Plugin **metadata-menu** cung cap GUI de edit frontmatter - khng can go tay.

### Bat Edit Pattern
1. Mo note trong metadata-menu
2. Edit tags/status/category -> applies in real-time  
3. Multiple select trong file explorer -> bat-edit metadata
4. View changes live without reload

## Calendar Integration Tasks

**Plugin: calendar + periodic-notes** - tasks c linked voi ngay due:

- Daily notes (02-Daily/) auto-log capture timestamps
- Weekly review runs task scan via dataview queries
- Monthly review archives completed tasks from 60-Archive/

## Overdue Escalation Rule

```dataview
TABLE status as "Priority", due as "Due Date"
FROM ""
WHERE due < date(today) AND done = false
SORT due ASC
LIMIT 20
```

**Rule:** Any task overdue >7 days -> escalate to P1 or move to "Waiting For".
**Rule:** Any task waiting 30+ days -> archive or delete.
