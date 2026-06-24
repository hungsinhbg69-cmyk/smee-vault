---
title: "llm-wiki-critique"
slug: "llm-wiki-critique"
category: concepts
tags: [obsidian-cleanup, auto-added]
status: draft
type: concept
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "LLM Wiki — Self-Critique (3 Rounds)"
tags: [llm, wiki, critique, karpathy, analysis]
date: 2026-06-16
source: "GitHub Gist - Karpathy LLM Wiki Pattern"
related: ["llm-wiki-karpathy-pattern", "llm-wiki-architecture", "llm-wiki-operations"]
status: reviewed
---

# LLM Wiki — Self-Critique 3 Rounds (Karpathy)

## Round 1: Architecture Claims

### Claim: "3-layer architecture is novel and sufficient"

**Critique:**
- **Thiếu semantic layer:** Wiki pages linked by text references, không structured relationships (không RDF/property-based). Không có ontology ở cấp độ cao hơn markdown links.
- **Raw sources immutable — đúng về audit trail nhưng sai về practicality.** Cần preprocessing pipeline cho metadata extraction, thumbnail generation, format conversion. Tác giả không đề cập.
- **Schema co-evolution risk:** Human + LLM refine schema together nhưng không có mechanism versioning → breaking changes risk khi schema drift.

**Verdict:** 3-layer model hữu ích nhưng oversimplified. Cần thêm: (1) semantic layer cho structured relationships, (2) preprocessing pipeline, (3) schema versioning strategy.

### Claim: "LLM owns wiki entirely"

**Critique:**
- **Ownership là shared:** LLM operational tasks (create pages, update cross-refs), nhưng human strategic decisions (curate sources, guide discussion, review summaries, decide quality of answers).
- **Consistency guarantee ambiguous:** Surface-level (links work) hay deep-level (claims align)? Không có mechanism cho consistency verification.

**Verdict:** LLM ownership hợp lý cho operational tasks, nhưng strategic decisions cần human oversight. Model hoạt động tốt khi human-in-loop duy trì.

## Round 2: Operations & Scalability

### Claim: "Index-first search works at moderate scale (~100 sources, hundreds of pages)"

**Critique:**
- **Index degradation >500 pages:** index.md có thể >50K tokens → reading full index per query = inefficient. Không đề cập optimization strategy (partial reads, category filters).
- **qmd transition point unclear:** Khi nào cần qmd? Không metric cho decision boundary.
- **Search precision:** BM25 + vector hybrid tốt hơn text search nhưng không giải quyết semantic ambiguity (từ nhiều nghĩa).

**Solution:** Category-indexed index (partition by topic), incremental index updates (không rebuild toàn bộ mỗi ingest).

### Claim: "Single source touches 10-15 wiki pages"

**Critique:**
- **Overhead estimation:** 10-15 file writes = substantial I/O + token cost. Context window management quan trọng cho local LLM.
- **Batch efficiency undefined:** Batch 10 sources → potentially 150 file ops → context overflow risk.
- **No parallelism strategy:** Independent page updates có thể parallelized.

**Verdict:** Operations scalable nhưng cần: (1) selective page updates, (2) batch size limits (~5 sources max), (3) parallel write strategy.

### Claim: "LLM good at suggesting new questions"

**Critique:**
- **Quality variance phụ thuộc scope:** Narrow domain → focused but limited suggestions. Broad domain → diverse but potentially irrelevant.
- **No feedback loop:** Human không rate suggestion quality → LLM không learn. Suggestions có thể repetitive sau nhiều lint passes.

## Round 3: Comparison & Real-World Viability

### Claim: "Wiki compounding better than RAG"

**Critique:**
- **Accumulation advantage là thật:** Wiki tích lũy knowledge → query cost giảm theo thời gian. Không phải re-retrieve mọi source mỗi lần.
- **Tuy nhiên:** RAG cũng có accumulation qua embedding updates. Difference là type: RAG = vector accumulation, Wiki = semantic/structural accumulation.
- **Cost comparison:**
  - RAG: High initial setup → low per-query cost (good cho high-volume, moderate complexity)
  - Wiki: Low initial setup → variable per-query cost (good cho deep synthesis, cross-document reasoning)

**Verdict:** Wiki pattern tốt hơn cho use cases cần deep synthesis. RAG tốt hơn cho high-volume queries. **Complement, không replacement.**

### Claim: "Maintenance cost near zero with LLMs"

**Critique:**
- **Token cost thực tế:** Lint pass = read all pages → detect issues → generate fixes. 500 pages × 2K tokens = 1M+ tokens/pass (local Ollama: 5-15 phút).
- **Human verification cost:** LLM suggest fixes, human review + approve (đặc biệt contradictory claims). "Near zero" chỉ đúng khi wiki stable — growing phase cao hơn nhiều.
- **Stale data risk:** Không có mechanism auto-detect outdated sources nếu không ingest regularly.

### Claim: "Works for personal, research, reading, business contexts"

**Viability matrix:**

| Context | Complexity | Viability | Key Success Factor |
|---------|-----------|-----------|-------------------|
| Personal | Low | High | Human fully in control |
| Research | Medium-High | Medium-High | Schema well-defined + citation accuracy |
| Reading (fan wiki) | Medium | High | Structured domain, predictable page types |
| Business/Team | High | Medium | Team discipline + LLM reliability + access control |

**Verdict:** Pattern universal về concept, nhưng implementation cần customization theo context. **Không phải "one size fits all".**

---

## Summary of Critique

### What Karpathy Gets Right
1. ✅ Index-first search là smart choice ở moderate scale
2. ✅ Knowledge compounding qua persistent wiki — real advantage over RAG
3. ✅ Lint workflow là secret weapon cho long-term maintenance
4. ✅ Human-in-loop discussion during ingest quan trọng cho quality

### What's Missing or Oversimplified
1. ❌ Semantic layer (structured relationships beyond text links)
2. ❌ Schema versioning strategy
3. ❌ Scalability path (>500 pages — index degradation, partitioning)
4. ❌ Parallelism strategy for batch operations
5. ❌ Feedback loop for suggestion quality learning
6. ❌ Preprocessing pipeline for diverse raw sources

### Recommended Enhancements
- Add category-indexed index (partition by topic)
- Implement incremental index updates (không rebuild toàn bộ)
- Define schema versioning với backward compatibility
- Add batch size limits (~5 sources max per ingest)
- Create feedback mechanism cho lint suggestions quality
- Preprocessing pipeline cho raw source metadata extraction

---

*See also: [[llm-wiki-karpathy-pattern]], [[llm-wiki-architecture]], [[llm-wiki-operations]]*
