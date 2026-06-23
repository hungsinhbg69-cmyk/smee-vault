---
title: "Agent Session Log"
slug: "agent-session-log"
category: meta
tags: [meta, agent, session-log]
status: active
type: framework
created: 2026-06-23
last_updated: 2026-06-23
---

# 🤖 Agent Session Log Template

> Hermes Agent session tracking — logs every action, capture, and decision for vault integration.

## Session Header

```yaml
session_id: YYYY-MM-DD-HHMM
agent: hermes-agent
vault_root: Smee Obsidian/Smee
protocol_version: 2.1
```

## Pre-Session Checklist

- [ ] Read `Protocol.md` → confirm current rules
- [ ] Read `Vault-Quick-Ref.md` → identify domain context needed
- [ ] Read active daily note → check prior captures
- [ ] Scan active projects in `10-Projects/`

## Session Actions Log

### Captures (new knowledge)
- `[HH:MM] capture: "<topic>" → [[slug-name]] (folder/#tags)`

### Connections (wikilinks created)
- `[HH:MM] connect: [[note-a]] ↕ [[note-b]]` → shared concept/cluster

### Outputs (deliverables)
- `[HH:MM] output: "<artifact type>" → [[target-path]]`

### Decisions
- `[HH:MM] decision: "<rationale>" → moved [[note]] from X to Y`

## Post-Session Routine

1. Append all actions to current daily note (02-Daily/YYYY-MM-DD.md)
2. Create atomic notes for validated insights (promoted from session captures)
3. Backlink new notes to relevant MOCs/insights
4. Commit via Git if vault has integration
