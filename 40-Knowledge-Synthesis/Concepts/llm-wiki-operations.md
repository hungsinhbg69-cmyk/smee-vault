---
title: "llm-wiki-operations"
slug: "llm-wiki-operations"
category: concepts
tags: [obsidian-cleanup, auto-added]
status: draft
type: concept
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "LLM Wiki — Operations (Ingest, Query, Lint)"
tags: [llm, wiki, operations, karpathy, workflow]
date: 2026-06-16
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related: ["llm-wiki-karpathy-pattern", "llm-wiki-architecture"]
status: reviewed
---

# LLM Wiki — Operations (Ingest, Query, Lint)

## Ingest Workflow

```
User drops source → 
  ├─ LLM reads source (full or sampled)
  ├─ Discuss key takeaways with human (human-in-loop)
  ├─ Write summary page in wiki
  ├─ Update index.md
  ├─ Update relevant entity/concept pages (10-15 files)
  └─ Append entry to log.md
```

### Key Details
- **Human-in-loop discussion:** Không fully automated — human review và guide LLM
- **Batch size:** Single source per ingest preferred; batch-ingest possible với ít supervision
- **File operations:** 10-15 pages touched per source = substantial I/O + token cost
- **Context management:** Mỗi page write cần load context → generate → save

### Scalability Concerns
- >500 pages: index.md quá lớn cho single-read (>50K tokens)
- Batch 10 sources → potentially 150 file ops → context overflow risk
- No parallelism strategy defined — pages có thể update song song nếu không dependencies

## Query Workflow

```
User asks question → 
  ├─ LLM reads index.md first (content-oriented search)
  ├─ Drill into relevant pages based on index metadata
  ├─ Synthesize answer with citations
  └─ Good answers filed back as new wiki pages
```

### Key Details
- **Index-first strategy:** Smart choice ở moderate scale — avoids embedding infrastructure
- **Answer filing:** Answers từ queries cũng compound vào knowledge base (không chỉ ingests)
- **Output formats:** markdown page, comparison table, slide deck (Marp), chart (matplotlib), canvas

### Search Evolution Path
1. **Small scale (<100 sources):** index.md sufficient
2. **Medium scale (~100-500 sources):** qmd (BM25 + vector + LLM re-ranking)
3. **Large scale (>500 sources):** Need partitioned index, incremental updates

## Lint Workflow

```
Periodic health-check → 
  ├─ Find contradictions between pages
  ├─ Flag stale claims superseded by newer sources
  ├─ Identify orphan pages (no inbound links)
  ├─ Detect important concepts without own pages
  ├─ Check missing cross-references
  └─ Suggest new questions to investigate + sources to find
```

### Key Details
- **Self-healing mechanism:** Lint là secret weapon cho long-term wiki health
- **Active discovery:** "LLM good at suggesting new questions" — không passive retrieval
- **Token cost:** Với 500 pages × 2K tokens = 1M+ tokens per lint pass (local Ollama: 5-15 phút)

## Index.md vs log.md

### index.md (Content-oriented)
- Catalog of everything in wiki
- Each page: link + one-line summary + metadata (date, source count)
- Organized by category (entities, concepts, sources)
- Updated on every ingest
- LLM reads index first khi answering queries

### log.md (Chronological)
- Append-only record of events
- Format: `## [YYYY-MM-DD] operation | Title`
- Parseable với unix tools: `grep "^## \[" log.md | tail -5`
- Gives timeline of wiki evolution
- Helps LLM understand recent activity

---

*See also: [[llm-wiki-karpathy-pattern]], [[llm-wiki-architecture]]*
