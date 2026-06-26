---
title: "Vault Governance"
slug: "vault-governance"
category: meta
tags: [meta, governance]
status: active
type: reference
created: 2026-06-12
last_updated: 2026-06-12
---

# 📜 Vault Governance Rules

## Naming Conventions

### File Names
- **Projects:** `ProjectName.md` — NO suffixes like "notes" or "doc"
- **Dated files:** `YYYY-MM-DD-Descriptor.md` — ISO date sorts chronologically
- **Atomic notes:** `kebab-case-slug.md` — lowercase, hyphens only
- **Meetings:** `YYYY-MM-DD-MeetingTitle.md`

### Slugs
- kebab-case: `facebook-ad-optimization` not `Facebook Ad Optimization`
- No underscores, no special characters
- Consistent across Linux/macOS filesystems

## Frontmatter Rules

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

## Folder Rules

| Rule | Detail |
|------|--------|
| Prefix numbers | 00-99 for sorting, gaps of 10 for expansion |
| No topic-based folders | Use tags for topics, folders for note types |
| Single attachment folder | `00-Meta/Attachments/` — all files here |
| Templates in `_templates/` | Underscore prefix sorts to top |

## Workflow Discipline

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

## Maintenance Schedule

| Frequency | Task | Owner |
|-----------|------|-------|
| Daily | Log captures to daily note | Smee + Hùng |
| Weekly (Sat 20h) | Empty inbox, link orphans, update projects | Smee |
| Monthly | Tag cleanup, broken-link audit | Smee |
| Quarterly | Archive old items, structure review, plugin inventory | Smee + Hùng |

## Quality Standards

### Must Have
- ✅ Frontmatter on every note
- ✅ At least 1 backlink per new note
- ✅ kebab-case slug
- ✅ Status field accurate
- ✅ Last updated date current

### Nice to Have
- ⭐ Summary line in frontmatter
- ⭐ Related notes linked
- ⭐ Dataview queries for dashboards
- ⭐ %% comments layer for agent instructions

## Archive Policy

Move to `60-Archive/` when:
- Project completed (progress = 100%)
- Note inactive >1 year
- Superseded by newer version
- No execution relevance

Archive keeps the vault root clean. Archived notes are searchable but don't clutter active views.

---
*Governance version: 1.0*
*Last reviewed: 2026-06-12*
