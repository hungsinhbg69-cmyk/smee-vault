---
title: "Vault — Second Brain Hub"
slug: "vault-hub"
category: meta
tags: [meta, vault-governance, protocol]
status: active
type: hub
created: 2026-06-12
last_updated: 2026-06-12
---

# 🧠 Vault — Second Brain Hub

## 🏗 Architecture: PARA + Zettelkasten Hybrid

```
vault/
├── 00-Meta/                    # System files, READMEs, templates
│   ├── README.md               # ← You are here
│   └── _templates/             # All note templates
├── 01-Inbox/                   # Quick capture, unsorted
├── 02-Daily/                   # Daily notes (YYYY-MM-DD.md)
├── 10-Projects/                # Active projects (time-bound)
├── 20-Areas/                   # Ongoing responsibilities
├── 30-Resources/               # Reference materials
├── 40-Knowledge-Synthesis/     # Atomic notes, permanent knowledge
│   ├── Insights/               # New insights discovered
│   ├── Concepts/               # Synthesized concepts
│   └── Frameworks/             # Mental models, frameworks
├── 50-Reviews/                 # Weekly/monthly reviews
├── 60-Archive/                 # Completed/inactive items
└── 70-Outputs/                 # Finalized artifacts (drafts, publications)
```

## 📐 Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| Project index | `ProjectName.md` | `Facebook-Marketing-Automation.md` |
| Dated files | `YYYY-MM-DD-Descriptor.md` | `2026-06-12-vault-setup.md` |
| Atomic notes | `kebab-case-slug.md` | `zettelkasten-modern-principles.md` |
| Meeting notes | `YYYY-MM-DD-MeetingTitle.md` | `2026-06-15-client-sync.md` |

**Rules:**
- kebab-case slugs (hyphens, no underscores)
- Lowercase only
- No "notes" suffix — file IS a note
- YYYY-MM-DD for all dates → sorts chronologically everywhere

## 🏷 Tag Taxonomy

```
#project/Alpha        #area/Marketing      #Status/draft
#Status/active        #Method/interview     #Concept/attention
#Tool/Obsidian        #Type/meeting         #Type/atomic-note
```

**Limits:**
- Max 5 tags per note
- Lowercase, hyphenated
- Define taxonomy here before reaching 400 notes
- Target: <50 unique tags total

## 📊 Health Metrics (Quarterly Audit)

| Metric | Target | Current |
|--------|--------|---------|
| Total notes | Growing | 0 |
| Avg links/note | 8+ | 0 |
| Orphan ratio | <10% | N/A |
| Inbox backlog | <5 items | 0 |
| Template usage | >80% | 0% |

## 🔄 Workflow: Capture → Connect → Decide → Ship

```
Inbox (01-Inbox/) 
  → Daily Notes (02-Daily/) — quick capture
  → Weekly Review — connect & organize
  → Projects (10-Projects/) or Atomic Notes (40-Knowledge-Synthesis/)
  → Archive (60-Archive/) when done
```

## 🤖 Agent Communication Layer

- `%% double percent comments %%` — Instructions invisible in reading mode (agent reads raw markdown)
- `<!-- HTML comments -->` — Structural directives for routing/priority

## 📌 Core Rules

1. **Vault = Memory, not Storage** — Every note has context and connections
2. **Daily = Scratch, Atomic = Durable** — Never mix them
3. **Promote when cited 2+ times** — Daily ideas → atomic notes
4. **Bidirectional links mandatory** — Every new note linked same day
5. **Frontmatter on every note** — Enables Dataview queries
6. **Weekly review non-negotiable** — 30 min, more valuable than any plugin
7. **Max 2 captures per session** — Quality over quantity

## 📚 Templates (in `_templates/`)

| Template | Use Case |
|----------|----------|
| daily-note.md | Daily logging, quick capture |
| meeting-note.md | Meeting summaries, action items |
| project-kickoff.md | New project MOC creation |
| literature-note.md | Academic paper synthesis |
| atomic-note.md | Permanent knowledge notes |
| weekly-review.md | Saturday review ritual |
| experiment-note.md | Hypothesis testing logs |

## 🔗 Key Links

- [[Protocol]] — Governance + Agent Rules (merged, single source of truth)
- [[Tag-Taxonomy]] — Full tag reference

---
*Created: 2026-06-12 | Last reviewed: 2026-06-15 (vault cleanup)*
*Architecture: PARA + Zettelkasten Hybrid*
*Agent: Smee (OpenClaw) + Hùng (Human)*
