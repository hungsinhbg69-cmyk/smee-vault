---
title: "OpenClaw + Hermes Agent Integration Framework"
slug: "agent-integration-framework"
category: framework
tags: [vault-maintenance]
status: "active"
type: reference
created: 2025-12-01
last_updated: 2026-07-13
---


# 🔄 OpenClaw + Hermes Agent Integration Framework

> Một lớp luật chung kết nối OpenClaw và Hermes với Smee Obsidian vault mà không nhân đôi quy tắc.

## 🏗️ Architecture

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ OpenClaw/Hermes│────▶│  Vault AGENTS.md│────▶│  Output/Actions   │
│  (Chat)      │◀────│  Layer          │◀────│                 │
└──────────────┘     │                 │     └──────────────────┘
                     │ 1. Scan Quick-Ref │
                     │ 2. Capture/Create │
                     │ 3. Connect/Link   │
                     │ 4. Log/Commit     │
                     └─────────────────┘
```

## 📦 Integration Layers (4 Total)

### Layer 1: Shared Operating Contract
**What it does:** Mọi agent đọc root `AGENTS.md`, sau đó áp dụng `Protocol.md` cho naming, frontmatter, folders và tags.
**How verified:** Quality gate check in Protocol Section 6 + Section 12.
**Agent behavior:** Read rules at session start → apply to every file create/edit.

### Layer 2: Daily Vault Logging
**What it does:** Chỉ capture, decision, output và structural change có ý nghĩa mới được ghi vào `02-Daily/YYYY-MM-DD.md`.
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
| Daily log signal quality | Không có log đọc/search vụn | Manual spot-check |
| Dirty-worktree safety | Không ghi đè thay đổi có sẵn | Git status + diff |

## 🧩 Agent Responsibility Map

| Agent | Vai trò chính | Không dùng làm nguồn luật |
|---|---|---|
| OpenClaw | Gateway, channels, heartbeat, cron, memory, orchestration dài hạn | Workspace backup hoặc memory cũ |
| Hermes | Phiên tương tác, research, skills, tool execution | `SOUL.md` cho đường dẫn/schema dự án |
| Cả hai | Search → patch → link → validate theo root `AGENTS.md` | Bản sao cây thư mục trong file riêng |

---
*Created: 2026-06-23 · Synchronized for OpenClaw + Hermes: 2026-07-13*
