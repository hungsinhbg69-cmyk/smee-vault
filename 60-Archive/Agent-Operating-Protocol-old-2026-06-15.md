---
title: "Agent Operating Protocol"
slug: "agent-operating-protocol"
category: meta
tags: [meta, agent, protocol]
status: active
type: reference
created: 2026-06-12
last_updated: 2026-06-12
---

# 🤖 Agent Operating Protocol — Smee × Obsidian Vault

## 🎯 Purpose

This vault is Smee's (OpenClaw agent) **external memory layer**. It bridges sessions, accumulates context, and serves as a queryable knowledge base.

## 📂 Folder Mapping to Agent Workflows

| Folder | Agent Use | Priority |
|--------|-----------|----------|
| `01-Inbox/` | Raw captures from conversations | Low (process weekly) |
| `02-Daily/` | Session logs, quick notes | High (check every session) |
| `10-Projects/` | Active project MOCs | Highest (context source) |
| `20-Areas/` | Domain expertise areas | Medium (reference) |
| `30-Resources/` | Tool docs, frameworks, references | Medium (lookup) |
| `40-Knowledge-Synthesis/` | Atomic notes, insights, concepts | Highest (retrieval target) |
| `50-Reviews/` | Weekly/monthly review summaries | Low (audit) |
| `60-Archive/` | Completed work | Lowest (historical) |
| `70-Outputs/` | Finalized drafts, publications | Medium (delivery) |

## 🔍 Token-Efficient Retrieval Pattern

### Step 1: Scan Summary Files (~1000 tokens)
```
Read: 10-Projects/ → list active projects
Read: 40-Knowledge-Synthesis/Insights/ → recent insights
Read: 20-Areas/ → domain context
```

### Step 2: Follow Links for Depth
When a project or concept is referenced → read that specific note
→ Same info, 5% token cost vs full vault scan

### Step 3: Dataview Queries (when available)
```dataview
TABLE status, last_updated
FROM "10-Projects"
WHERE status = "active"
```

## 📝 Capture Protocol

### During Conversations
When Hùng shares insights, decisions, or lessons:

1. **Identify type** → match to folder structure
2. **Create note** → use appropriate template from `_templates/`
3. **Add frontmatter** → always present
4. **Link bidirectionally** → connect to at least 1 existing note
5. **Log capture** → append to daily note with timestamp

### Example Capture Flow:
```
[Hùng mentions: "Facebook ad refresh every 7 days works best"]
→ Type: Insight/Principle
→ Path: 40-Knowledge-Synthesis/Insights/facebook-ad-rotation.md
→ Frontmatter: status=active, type=insight, tags=[facebook, ads, optimization]
→ Link: [[Facebook-Marketing-Automation]] project MOC
→ Daily log: [14:30] capture: "Facebook ad rotation 7-day cycle" → created ...
```

## 📤 Output Protocol

When creating content for Hùng (posts, drafts, reports):

1. **Draft in vault** → `70-Outputs/` folder
2. **Source links attached** → every claim backed by linked reference
3. **Review with Hùng** → %% comments layer for revision notes %%
4. **Finalize** → move to appropriate delivery location
5. **Backlink** → output note linked back to source vault notes

## 🔄 Session Lifecycle

### Session Start
1. Read `02-Daily/YYYY-MM-DD.md` (if exists)
2. Scan active project MOCs from `10-Projects/`
3. Check `%% comments %%` in daily note for standing instructions
4. Load relevant domain context from `20-Areas/` if needed

### Session End
1. Log session captures to daily note
2. Create any new atomic notes (max 2 per session)
3. Update project progress if work was done
4. Ensure all new notes have bidirectional links

### Weekly (Saturday 20h)
1. Empty `01-Inbox/` → distribute to proper folders
2. Find orphan notes → link or archive
3. Verify every active project has "next action"
4. Update vault health metrics in README.md
5. Log summary to `50-Reviews/weekly-review-YYYY-MM-DD.md`

## 🏷 Frontmatter Standards

Every note MUST have:
```yaml
---
title: "Exact Title"
slug: "exact-title-slug"
category: project | area | resource | knowledge | daily | review
tags: [tag1, tag2]  # max 5
status: draft | active | reference | output | archived
type: atomic-note | insight | meeting | project | literature-note
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

## 🔗 Link Types to Maintain

| Type | Direction | Example |
|------|-----------|---------|
| Vertical | Parent → Child | MOC → meeting notes → research files |
| Horizontal | Cross-domain | Marketing note → Design note |
| Referential | Project → Concept | Project → synthesized insight |

## ⚠️ Quality Guards

1. **Max 2 new notes per session** — prevents over-capture
2. **Every new note linked same day** — no orphaned content
3. **Frontmatter mandatory** — enables Dataview queries
4. **kebab-case slugs** — cross-platform compatible
5. **One idea per atomic note** — if >2 topics → split
6. **300-700 words per atomic note** — short = reusable

## 📊 Vault Health Dashboard

Run quarterly (integrate with Dataview):

| Check | Query | Action if Failed |
|-------|-------|------------------|
| Orphan notes | `LIST WHERE !outlinks AND file.name != "README"` | Link to hub or archive |
| Stale active notes | `WHERE status="active" AND last_updated < date(today)-30d` | Update or archive |
| Tag entropy | Count unique tags | Merge duplicates if >50 |
| Missing frontmatter | Search for notes without `---` YAML block | Add frontmatter |

## 🗣 Communication Layer Examples

### Standing Instructions (%% comments)
```markdown
%% Client prefers async updates over calls. Remember during meeting prep. %%
%% Always verify Facebook ad metrics before suggesting optimizations. %%
```

### Structural Directives (HTML comments)
```markdown
<!-- Scanned FIRST by daily planning: check this section every session -->
## Next Actions
- [ ] Review Q3 campaign data
```

---
*Protocol version: 1.0*
*Last updated: 2026-06-12*
*Author: Smee (OpenClaw Agent)*
