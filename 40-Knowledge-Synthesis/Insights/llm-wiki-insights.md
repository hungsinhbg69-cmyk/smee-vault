---
title: "llm-wiki-insights"
slug: "llm-wiki-insights"
category: insights
tags: [obsidian-cleanup, auto-added]
status: draft
type: insight
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "LLM Wiki — Insights & Application"
tags: [llm, wiki, insights, karpathy, application]
date: 2026-06-16
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related: ["llm-wiki-karpathy-pattern", "llm-wiki-architecture", "llm-wiki-operations", "llm-wiki-critique"]
status: reviewed
---

# LLM Wiki — Insights & Application (Karpathy)

## Key Insights

### 1. The Bookkeeping Problem
> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."

- Humans abandon wikis vì maintenance burden grows faster than value
- LLMs don't get bored, don't forget cross-refs, can touch 15 files per pass
- **Insight:** LLM không phải thay thế human thinking — mà giải quyết operational overhead

### 2. Division of Labor
- **Human's job:** Curate sources, direct analysis, ask good questions, think about meaning
- **LLM's job:** Everything else (summarizing, cross-referencing, filing, bookkeeping)
- **Insight:** Human-in-loop không phải "supervision" — mà là "direction"

### 3. Vannevar Bush's Memex Realized (1945 → 2026)
Bush envisioned: personal knowledge store with associative trails between documents. Private, actively curated, connections as valuable as content.
- **What he couldn't solve:** Who does the maintenance?
- **LLM Wiki Pattern solves this:** LLM handles maintenance, human curates

### 4. RAG vs Wiki — Complement not Replacement
| | RAG | LLM Wiki |
|--|-----|---------|
| Best for | High-volume queries, moderate complexity | Deep synthesis, cross-document reasoning |
| Accumulation type | Vector (passive) | Semantic/structural (active) |
| Initial cost | High (embeddings + DB) | Low (markdown files) |
| Per-query cost | Low | Variable (depends on wiki size) |

### 5. Index-First > Embedding-First at Moderate Scale
- At ~100 sources, hundreds of pages: index.md works surprisingly well
- Avoids vector database infrastructure overhead
- Migration path to qmd khi scale lên

## Application to Smee Vault

### Current Alignment
| Karpathy Concept | Smee Implementation | Status |
|-----------------|-------------------|--------|
| Raw sources | `30-Resources/` | ✅ Aligned |
| Wiki | `40-Knowledge-Synthesis/` | ✅ Aligned |
| Schema | AGENTS.md + `_templates/` | ✅ Aligned |
| index.md | `vault-master-index.md` | ✅ Exists |
| log.md | Daily notes (`02-Daily/`) | ⚠️ Partial |
| Ingest | New learning → capture with backlinks | ✅ Working |
| Query | Search vault → synthesize → file back | ⚠️ Manual |
| Lint | Daily Vault Maintenance cron | ⚠️ Needs expansion |

### Gap Analysis & Action Items

**Gaps identified:**
1. Semantic layer missing — notes linked by text, not structured properties
2. Schema versioning undefined
3. Batch ingest limited to 2 notes/session (Karpathy suggests 10-15)
4. Index-first search not optimized (no category partitioning)

**Action items:**
- [ ] Implement category-indexed vault master index (partition by PARA folder)
- [ ] Expand Daily Vault Maintenance cron timeout + add lint pass
- [ ] Define schema versioning rules cho wiki conventions
- [ ] Test batch ingest với max 5 sources per session
- [ ] Create entity/concept page templates aligned with Karpathy pattern

### Workflow Recommendation for Smee

```
1. Ingest new learning source
   → Read full source (web_fetch / file_read)
   → Extract key concepts + arguments
   → Write to appropriate vault folder (theo PARA)
   → Update vault-master-index.md
   → Add entry to daily log
   → Create ≥1 backlink same day

2. Query existing knowledge
   → Read index first (content-oriented search)
   → Drill into relevant notes
   → Synthesize answer
   → File good answers back as new wiki pages

3. Periodic lint (weekly)
   → Check for orphan pages
   → Flag stale claims
   → Suggest connections between existing notes
```

---

*See also: [[llm-wiki-karpathy-pattern]], [[llm-wiki-architecture]], [[llm-wiki-operations]], [[llm-wiki-critique]]*
