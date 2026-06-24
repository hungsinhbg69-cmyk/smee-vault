---
title: "llm-wiki-architecture"
slug: "llm-wiki-architecture"
category: concepts
tags: [obsidian-cleanup, auto-added]
status: draft
type: concept
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "LLM Wiki — 3-Layer Architecture"
tags: [llm, wiki, architecture, karpathy, rag]
date: 2026-06-16
source: "GitHub Gist - Karpathy LLM Wiki Pattern"
related: ["llm-wiki-karpathy-pattern", "llm-wiki-operations", "llm-wiki-critique"]
status: reviewed
---

# LLM Wiki — 3-Layer Architecture (Karpathy)

## Overview

Andrej Karpathy đề xuất mô hình **3-layer knowledge base** thay vì RAG truyền thống.

## Layer 1: Raw Sources

- **Định nghĩa:** Collection của source documents (articles, papers, images, data files)
- **Tính chất:** Immutable — LLM đọc không ghi đè
- **Owner:** Human curates và drop sources vào collection
- **Purpose:** Single source of truth, audit trail cho mọi wiki content

## Layer 2: The Wiki

- **Định nghĩa:** Directory của LLM-generated markdown files
- **Content types:** Summaries, entity pages, concept pages, comparisons, overviews, synthesis
- **Tính chất:** Mutable — LLM tạo pages, update cross-refs, maintain consistency
- **Owner:** LLM hoàn toàn sở hữu operational layer này

**Key difference với RAG:** Wiki là persistent, compounding artifact. Mỗi source mới làm wiki giàu hơn, không phải re-retrieve từ đầu mỗi query.

## Layer 3: The Schema

- **Định nghĩa:** Document (CLAUDE.md / AGENTS.md) — config file cho LLM
- **Content:** Directory structure conventions, page formats, workflows, naming rules
- **Owner:** Human + LLM co-evolve over time
- **Purpose:** Biến LLM từ generic chatbot thành disciplined wiki maintainer

## So sánh với RAG truyền thống

| Aspect | RAG | LLM Wiki Pattern |
|--------|-----|-----------------|
| Retrieval | Vector similarity per query | Index-first drill-down |
| Accumulation | Embedding updates (passive) | Semantic integration (active) |
| Maintenance | None needed | LLM automated |
| Synthesis | Rediscover per query | Already compiled + kept current |
| Cross-refs | None automatic | Maintained by LLM |

## Critical Analysis

### Strengths
- Simple implementation (markdown files + git)
- No vector DB dependency at moderate scale
- Knowledge compounds over time
- Human readable và editable (không black-box)

### Weaknesses
- Index degradation khi wiki >500 pages (>50K tokens)
- No structured ontology — links là text-based, không property-defined
- Schema drift risk — co-evolution có thể dẫn đến inconsistency
- Batch ingest overhead — 10-15 files per source = context switching cost

## Application to Smee Vault

| Karpathy Layer | Smee Path |
|---------------|-----------|
| Raw sources | `30-Resources/` |
| Wiki | `40-Knowledge-Synthesis/` |
| Schema | AGENTS.md + `_templates/` |

---

*See also: [[llm-wiki-karpathy-pattern]], [[llm-wiki-operations]], [[llm-wiki-critique]]*
