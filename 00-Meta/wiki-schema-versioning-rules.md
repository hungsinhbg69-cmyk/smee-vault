---
title: "Wiki Schema Versioning Rules"
slug: "wiki-schema-versioning-rules"
category: meta
tags: [schema, versioning, wiki, karpathy, governance]
date: 2026-06-16
type: schema
version: "1.0.0"
status: active
---

# Wiki Schema Versioning Rules (Karpathy Pattern)

> Định nghĩa cho cách LLM và Hùng cùng phát triển wiki conventions qua thời gian — không breaking changes vô tình.

## 1. Schema Conventions

### 1.1 Frontmatter Standard (BẮT BUỘC)
Mọi note trong `40-Knowledge-Synthesis/` phải có frontmatter:
```yaml
---
title: "Note Title"
slug: "note-slug"
category: concepts|frameworks|insights
tags: [tag1, tag2]  # max 5 tags
date: YYYY-MM-DD   # creation date
source: "..."      # original source URL or "internal"
related: []        # backlinks to other vault notes
status: draft|reviewed|verified|archived
type: concept|framework|insight|comparison|template
---
```

### 1.2 Naming Conventions
- **File names:** kebab-case (e.g., `llm-wiki-karpathy-pattern.md`)
- **Folders:** lowercase, hyphen-separated (e.g., `Bac-Giang/`)
- **Slugs:** match filename, no special chars
- **Tags:** lowercase, max 5 per note

### 1.3 Directory Structure
```
40-Knowledge-Synthesis/
├── Concepts/          # Core ideas, models, patterns
│   ├── Bac-Giang/    # Domain-specific concepts
│   └── LLM/          # AI/ML concepts
├── Frameworks/        # Reusable frameworks, strategies
│   ├── Bac-Giang/
│   └── Marketing/
├── Insights/          # Discoveries, analyses, conclusions
│   ├── Bac-Giang/
│   └── Meta/
├── Templates/         # Note templates (Karpathy-aligned)
└── Comparison/        # Side-by-side comparisons
```

## 2. Versioning Strategy

### Semantic Versioning cho Schema
- **Major (X.0.0):** Breaking changes — structure, frontmatter fields, naming rules
- **Minor (0.X.0):** New conventions added — backward compatible
- **Patch (0.0.X):** Clarifications, typos — no functional change

### Migration Rules
| Version | Change | Migration Action |
|---------|--------|-----------------|
| Major bump | Added required frontmatter field | LLM auto-add default values |
| Major bump | Renamed folder | LLM update all backlinks |
| Minor bump | New optional field | No migration needed |
| Patch | Typo fix in convention docs | No migration needed |

### Version Tracking
- Schema file này có `version: "1.0.0"` — bump khi có breaking change
- Change log trong section 5 dưới đây
- Khi update schema → LLM scan toàn bộ vault để apply migration

## 3. LLM Operational Rules

### 3.1 Ingest Rules
- **MUST** add frontmatter before writing any new note
- **MUST** create ≥1 backlink trong cùng session
- **MUST** update vault-master-index.md khi tạo note mới
- **MUST** use correct category (Concepts/Frameworks/Insights)
- **MAX** 2 notes per session (token budget)

### 3.2 Query Rules
- Read vault-master-index.md first for navigation
- Drill into specific notes only after index scan
- Cite sources in answers with `[[note-slug]]` links
- File good answers back as new wiki pages (with frontmatter)

### 3.3 Lint Rules (Weekly/Bi-weekly)
- Check for orphans: notes with no backlinks AND not in index
- Flag stale claims: notes >30 days old referencing time-sensitive data
- Suggest connections: identify cross-linking opportunities
- Report: orphan count, stale count, connection suggestions

## 4. Backlink Requirements

### Every New Note MUST Have ≥1 Backlink Same Day
- Link to related existing note(s) in `related:` field
- Add backlink from existing note to new note (edit source note)
- Cross-reference in vault-master-index.md

### Orphan Detection Criteria
A note is ORPHANED if:
- No inbound links (`[[note-name]]`) from any other note, AND
- Not listed in vault-master-index.md, AND
- Created >7 days ago

## 5. Change Log

### v1.0.0 (2026-06-16) — Initial Schema
- Based on Karpathy LLM Wiki Pattern + Smee PARA structure
- Frontmatter standard defined
- Naming conventions established
- Versioning strategy (semantic) set up
- Migration rules defined

### Planned v1.1.0
- Add entity/concept page templates (Karpathy-aligned)
- Implement category-indexed vault master index
- Add lint pass to Daily Vault Maintenance cron

## 6. References

- Karpathy, Andrej. "LLM Wiki Pattern." GitHub Gist.
- [[vault-architecture]] — Overall vault design
- [[Vault — Second Brain Hub]] — Complete PARA structure
