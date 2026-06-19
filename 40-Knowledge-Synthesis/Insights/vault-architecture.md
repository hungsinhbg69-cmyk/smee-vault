---
title: "vault-architecture"
slug: "vault-architecture"
category: insights
tags: [obsidian-cleanup, auto-added]
status: draft
type: insight
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "Atomic Note — Vault Architecture: PARA + Zettelkasten Hybrid"
slug: "vault-architecture-para-zettelkasten-hybrid"
category: knowledge
tags: [obsidian, zettelkasten, para]
status: draft
type: atomic-note
created: 2026-06-12
last_updated: 2026-06-12
cited_count: 0
---

# 🔬 Vault Architecture: PARA + Zettelkasten Hybrid

## 📝 One Idea Summary
PARA organizes notes by actionability (Projects/Areas/Resources/Archive) while Zettelkasten organizes by knowledge density (atomic, linked notes) — combining both gives you a vault that works for execution AND thinking.

## 📖 Explanation
**PARA method** (Tiago Forte) provides the outer structure:
- **P**rojects — time-bound, have deadlines
- **A**reas — ongoing responsibilities, no deadline
- **R**esources — reference materials of interest
- **A**rchive — inactive items from above

**Zettelkasten method** (Niklas Luhmann) provides the inner knowledge layer:
- Atomic notes — one idea per note, 300-700 words
- Bidirectional links — every note connects to others
- Promote from daily → atomic when cited 2+ times

**The hybrid approach:**
1. Use PARA for folder structure (actionability)
2. Use Zettelkasten for knowledge synthesis within `40-Knowledge-Synthesis/`
3. Daily notes = scratchpad, promote validated ideas to atomic notes
4. Weekly connect phase = link orphans, update projects

**Why this works for OpenClaw agent:**
- Token-efficient retrieval: scan summary → follow links = 5% token cost
- %% comments layer = agent instructions invisible in reading mode
- Smart Connections + Ollama = semantic search without API costs

## 🔄 Connections
### Related Concepts
- [[Obsidian-Vault-Setup]] — Project MOC for this vault launch
- [[Vault-Governance]] — Detailed rules and naming conventions
- [[Agent-Operating-Protocol]] — Smee's operating guide

### Applied In
- Smee's second brain — primary knowledge repository
- Daily capture workflow — daily notes → atomic notes promotion

## 📚 Sources
- Tiago Forte — PARA method (Building a Second Brain)
- Niklas Luhmann — Zettelkasten method (sociological research)
- Obsidian community best practices

---
%% Agent instructions:
- One idea per note. If >2 H2 sections on different topics → split
- 300-700 words target. Short = reusable, linkable
- Promote from daily notes when cited 2+ times
- Every new atomic note MUST have at least 1 backlink same day
- Status: draft → active (when linked 3+) → superseded (when updated)
%%
