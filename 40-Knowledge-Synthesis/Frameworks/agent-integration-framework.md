---
title: "Hermes Agent Integration Framework"
slug: "agent-integration-framework"
category: framework
tags: [vault-maintenance]
status: reference
type: reference
created: 2025-12-01
last_updated: 2026-06-24
---

---

# 🔄 Hermes Agent Integration Framework

> Auto-connects every Hermes agent conversation to Smee Obsidian vault — creating a closed-loop Second Brain.

## 🏗️ Architecture

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│  Conversation │────▶│  Vault Agent    │────▶│  Output/Actions   │
│  (Chat)      │◀────│  Layer          │◀────│                 │
└──────────────┘     │                 │     └──────────────────┘
                     │ 1. Scan Quick-Ref │
                     │ 2. Capture/Create │
                     │ 3. Connect/Link   │
                     │ 4. Log/Commit     │
                     └─────────────────┘
```

## 📦 Integration Layers (4 Total)

### Layer 1: Protocol-Driven Operations
**What it does:** Every agent action follows `Protocol.md` section rules — naming, frontmatter, folders, tags.
**How verified:** Quality gate check in Protocol Section 6 + Section 12.
**Agent behavior:** Read rules at session start → apply to every file create/edit.

### Layer 2: Daily Vault Logging
**What it does:** Every conversation action appends to `02-Daily/YYYY-MM-DD.md` with timestamp, type, and wikilinks.
**Format:** `[HH:MM] <type>: "<summary>" → [[slug]]`
**Types:** capture, connect, output, decision, cleanup.
**Agent behavior:** Auto-append after every meaningful action — not just at session end.

### Layer 3: Knowledge Graph Maintenance
**What it does:** Agent creates bidirectional wikilinks between new content and existing notes during creation. Weekly orphan scan promotes valid findings from daily logs to atomic notes.
**How verified:** Dead-end audit (Protocol Section 8 maintenance) — every note has ≥1 outbound link.
**Agent behavior:** Every new note connects to at least 1 existing vault cluster immediately.

### Layer 4: Smart Context Loading
**What it does:** Agent auto-loads relevant domain notes based on conversation topic — loaded from Vault-MOC. When discussing Facebook Ads → loads INDEX.md + relevant sub-notes. When on Bac Giang → loads cultural profile + market notes.
**How verified:** Session logs track which domain contexts were loaded and used.
**Agent behavior:** Read MOC → identify topic cluster → load 2-3 anchor notes from that cluster before deep work.

## 🔄 Feedback Loops

### Positive Loop (Reinforcement)
Agent captures insight → creates atomic note with wikilinks → next session loads relevant context → agent builds on existing knowledge → vault grows richer → retrieval gets more precise.

### Weekly Connect Phase
Every Saturday at 20h: empty inbox folder → promote validated daily ideas to atomic notes → link orphans → verify project next-actions → archive dead items → commit git changes.

## 📐 Quality Metrics

| Metric | Target | How Measured |
|--------|--------|--------------|
| Outbound wikilinks per note | ≥1 | Dead-end audit via search_files |
| Backlink coverage | >50% of notes linked TO from others | Vault graph scan |
| Daily capture log completeness | 100% of actions logged | Manual spot-check |
| Session end commit rate | Every active session | Git status check |

## 🧩 Agent Tools Mapping

| Hermes Tool | Vault Operation | Path Convention |
|-------------|-----------------|-----------------|
| `read_file` | Read notes for context | `C:/Users/Hung/Desktop/Smee Obsidian/Smee/<path>` |
| `write_file` | Create/update notes | Same base path, forward slashes |
| `patch` | Targeted edits | Anchored by stable text |
| `search_files` | Content/filename search | target="content" for search, "files" for listing |
| `execute_code` | Bulk operations, batch create | Python raw Windows paths |
| `terminal` | Git operations | `git add . && git commit -m "..."` from vault root |

---
*Created: 2026-06-23 by Hermes Agent Integration*
