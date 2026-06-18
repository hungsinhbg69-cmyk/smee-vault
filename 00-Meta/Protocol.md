---
title: "Vault Protocol — Governance + Agent Rules"
slug: "vault-protocol"
category: meta
tags: [meta, governance, agent]
status: active
type: reference
created: 2026-06-12
last_updated: 2026-06-17
---

# 📜 Vault Protocol — Governance + Agent Rules

> Merge of Vault Governance + Agent Operating Protocol (2026-06-15). Eliminates duplication from original two-file setup.

## 1. Naming Conventions

### File Names
- **Projects:** `ProjectName.md` — NO suffixes like "notes" or "doc"
- **Dated files:** `YYYY-MM-DD-Descriptor.md` — ISO date sorts chronologically
- **Atomic notes:** `kebab-case-slug.md` — lowercase, hyphens only
- **Meetings:** `YYYY-MM-DD-MeetingTitle.md`

### Slugs
- kebab-case: `facebook-ad-optimization` not `Facebook Ad Optimization`
- No underscores, no special characters
- Consistent across Linux/macOS filesystems

## 2. Frontmatter Rules

**Every note MUST have:**
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

## 3. Folder Rules

| Rule | Detail |
|------|--------|
| Prefix numbers | 00-99 for sorting, gaps of 10 for expansion |
| No topic-based folders | Use tags for topics, folders for note types |
| Single attachment folder | `00-Meta/Attachments/` — all files here |
| Templates in `_templates/` | Underscore prefix sorts to top |

## 4. Capture Workflow

### Capture (Inbox)
- Raw capture with minimal friction
- Daily note = quick-capture inbox for fleeting thoughts
- Web clips, highlights → Inbox first
- **NO organizing during capture**

### Connect (Weekly Review)
- Empty inbox → move/categorize all items
- Link notes to existing MOCs or archive if dead context
- Promote high-value daily ideas → atomic notes
- Backlink every new note immediately

### Decide (Project Reviews)
- Every project note answers: "What happens next?"
- Research workflow: capture → extract → tag → promote validated points
- Meeting-to-output pipeline: capture → decisions → insights → drafts

### Ship (Outputs)
- Evidence-first method: collect linked refs → extract claims → draft → verify
- Store ship-ready version in `70-Outputs/`
- Keep source links attached

## 5. Agent Capture Protocol

When Hùng shares insights, decisions, or lessons:

1. **Identify type** → match to folder structure
2. **Create note** → use appropriate template from `_templates/`
3. **Add frontmatter** → always present
4. **Link bidirectionally** → connect to at least 1 existing note
5. **Log capture** → append to daily note with timestamp

### During Conversations
- Max 2 new notes per session
- Every new note linked same day (no orphaned content)
- Log in daily note: `[HH:MM] capture: "<topic>" → created <path>`

### Session Lifecycle
- **Start:** Read `02-Daily/YYYY-MM-DD.md` → scan active projects → load domain context
- **End:** Log captures → create atomic notes → update projects → verify backlinks
- **Weekly (Sat 20h):** Empty inbox → link orphans → verify project next-actions → archive dead items

## 6. Quality Standards

### Must Have
- ✅ Frontmatter on every note
- ✅ At least 1 backlink per new note
- ✅ kebab-case slug
- ✅ Status field accurate
- ✅ Last updated date current

### Atomic Note Rules
- One idea per note — if >2 topics → split
- 300-700 words target — short = reusable, linkable
- Promote from daily notes when cited 2+ times
- Status flow: draft → active (when linked 3+) → superseded (when updated)

## 7. Maintenance Schedule

| Frequency | Task | Owner |
|-----------|------|-------|
| Daily | Log captures to daily note | Smee + Hùng |
| Weekly (Sat 20h) | Empty inbox, link orphans, update projects | Smee |
| Monthly | Tag cleanup, broken-link audit | Smee |
| Quarterly | Archive old items, structure review, plugin inventory | Smee + Hùng |

## 8. Archive Policy

Move to `60-Archive/` when:
- Project completed (progress = 100%)
- Note inactive >1 year
- Superseded by newer version
- No execution relevance

## 9. Agent Communication Layer

### `%% double percent comments %%`
Invisible in reading mode. AI reads raw markdown. Use for:
- Standing instructions
- Revision notes
- Context flags for agent routing

### `<!-- HTML comments -->`
Structural directives. Use for:
- "Scanned FIRST by daily planning"
- Priority markers
- Section routing hints

## 10. Token-Efficient Retrieval Pattern

### Step 1: Scan Quick-Ref Hub (~3K tokens)
```
Read: 00-Meta/Vault-Quick-Ref.md → master navigation by domain
  → Jump directly to specific file for the task
```

### Step 2: Follow Links for Depth
When a project or concept is referenced → read that specific note
→ Same info, 5% token cost vs full vault scan

## 11. Tag Taxonomy Summary

| Prefix | Purpose | Examples |
|--------|---------|----------|
| `#Project/` | Active projects | `#Project/Facebook-Marketing` |
| `#Area/` | Ongoing responsibilities | `#Area/Marketing` |
| `#Status/` | Note lifecycle | `#Status/draft`, `#Status/active` |
| `#Type/` | Content classification | `#Type/atomic-note`, `#Type/insight` |
| `#Concept/` | Topic tags (create as needed) | `#Concept/marketing-automation` |
| `#Tool/` | Tools and platforms | `#Tool/Obsidian` |
| `#Method/` | Techniques and approaches | `#Method/capture-first` |

**Rules:** Max 5 tags/note, max 50 unique tags total. Lowercase, hyphenated. Define before using.

---
*Protocol version: 2.1 (updated 2026-06-17 — added Vault-Quick-Ref hub navigation)*
*Replaces: Vault-Governance.md + Agent-Operating-Protocol.md*
