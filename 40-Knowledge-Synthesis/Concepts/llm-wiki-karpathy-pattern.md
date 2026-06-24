---
title: "llm-wiki-karpathy-pattern"
slug: "llm-wiki-karpathy-pattern"
category: concepts
tags: [obsidian-cleanup, auto-added]
status: draft
type: concept
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "LLM Wiki Pattern (Karpathy)"
tags: [llm, wiki, knowledge-management, rag, pattern, karpathy]
date: 2026-06-16
sources: ["https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"]
status: reviewed
---

# LLM Wiki Pattern — Phân tích chuyên sâu + Tự phản biện 3 vòng

> **Nguồn:** Andrej Karpathy, gist `442a6bf555914893e9891c11519de94f`
> **Ngày phân tích:** 2026-06-16
> **Mục đích:** Hiểu sâu, tự phản biện, áp dụng vào Smee Obsidian vault

---

## 1. Tổng quan — Core Idea

Karpathy mô tả một **mô hình xây dựng knowledge base cá nhân bằng LLM**, khác biệt căn bản với RAG truyền thống:

- **RAG truyền thống:** Upload file → LLM retrieve chunk at query time → generate answer. Mỗi câu hỏi = khám phá lại từ đầu. Không có accumulation.
- **LLM Wiki Pattern:** LLM **tích lũy incremental** — đọc source, extract key info, integrate vào wiki tồn tại (persistent). Knowledge được compile once + kept current.

### 3 Layers kiến trúc

| Layer | Mô tả | Owner | Mutable? |
|-------|-------|-------|----------|
| Raw sources | Source documents (articles, papers, images) | Human | Immutable |
| The wiki | LLM-generated markdown files (summaries, entity pages, concept pages) | LLM | Mutable |
| The schema | Configuration doc (CLAUDE.md / AGENTS.md) — tells LLM how to maintain wiki | Human + LLM | Co-evolve |

### 3 Operations

1. **Ingest:** Drop source → LLM reads → discuss takeaways → write summary → update index → update entity/concept pages → append log
2. **Query:** Ask question → LLM search relevant pages → synthesize answer with citations → good answers filed back into wiki
3. **Lint:** Periodic health-check → find contradictions, stale claims, orphan pages, missing cross-refs, data gaps

### 2 Special Files

- **index.md** — Content catalog (links + summaries + metadata), updated every ingest
- **log.md** — Append-only chronological record (`## [YYYY-MM-DD] operation | Title`)

---

## 2. Phân tích chi tiết từng component

### 2.1 Raw Sources Layer

**Claim chính:** Sources là immutable, LLM chỉ đọc không viết lại.

**Ưu điểm:**
- Single source of truth — không lo data corruption
- Audit trail rõ ràng: wiki có thể trace back về source gốc
- Dễ version control với git (source files + wiki separately tracked)

**Hạn chế:**
- Với sources lớn (>100 pages), việc LLM "đọc hết" mỗi lần ingest tốn token
- Không có mechanism tự động extract metadata từ raw sources (tác giả đề cập nhưng không chi tiết)
- Format diversity: articles, papers, images, data files — mỗi loại cần preprocessing khác nhau

### 2.2 The Wiki Layer

**Claim chính:** LLM hoàn toàn sở hữu wiki layer — tạo pages, update cross-refs, maintain consistency.

**Cơ chế hoạt động:**
- Mỗi ingest có thể touch 10-15 wiki pages (tác giả tự nhận)
- Pages được categorize: entity pages, concept pages, comparison tables, summaries
- Cross-references maintained automatically — đây là điểm mạnh nhất so với RAG

**Ưu điểm:**
- Knowledge compounding: mỗi source mới làm wiki giàu hơn, không phải bắt đầu lại
- Graph view trong Obsidian cho thấy connections real-time
- Answers từ queries cũng được filed back → explorations compound

**Hạn chế:**
- "10-15 pages per ingest" — thực tế phụ thuộc vào quality của LLM + schema definition
- Risk of **drift**: wiki content có thể diverge từ source gốc qua nhiều updates
- Không có mechanism conflict resolution khi 2 sources contradicts nhau (tác giả chỉ nói "flag contradictions")

### 2.3 The Schema Layer

**Claim chính:** Schema document là config file quan trọng nhất — biến LLM từ generic chatbot thành disciplined wiki maintainer.

**Nội dung schema điển hình (suy luận):**
- Directory structure conventions
- Page format templates (frontmatter, headings)
- Ingest workflow steps
- Query response format
- Lint checklist
- Naming conventions

**Ưu điểm:**
- Co-evolution: human + LLM refine schema over time
- Domain-specific adaptation

**Hạn chế:**
- Schema complexity grows with wiki size → maintenance overhead tăng
- Cần human oversight để prevent LLM từ "drift" khỏi intended structure
- Không có versioning mechanism cho schema changes

---

## 3. Operations Deep Dive

### 3.1 Ingest Workflow

```
User drops source → LLM reads source → 
  ├─ Discuss key takeaways (human-in-loop)
  ├─ Write summary page in wiki
  ├─ Update index.md
  ├─ Update relevant entity/concept pages (10-15 files)
  └─ Append entry to log.md
```

**Phân tích:**
- Human-in-loop discussion là điểm khác biệt quan trọng — không fully automated
- "10-15 files per ingest" = batch file operations, LLM phải context-switch giữa nhiều files
- Risk: LLM có thể miss connections nếu source phức tạp + schema chưa rõ ràng

### 3.2 Query Workflow

```
User asks question → 
  ├─ LLM reads index.md first (content-oriented search)
  ├─ Drill into relevant pages
  ├─ Synthesize answer with citations
  └─ Good answers filed back as new wiki pages
```

**Phân tích:**
- **Index-first strategy** thay vì embedding-based RAG — smart choice ở moderate scale (~100 sources, hundreds of pages)
- Avoids need for vector database infrastructure (qmd optional)
- Answers filed back = knowledge accumulation từ queries, không chỉ từ ingests

### 3.3 Lint Workflow

```
Periodic health-check → 
  ├─ Find contradictions between pages
  ├─ Flag stale claims superseded by newer sources
  ├─ Identify orphan pages (no inbound links)
  ├─ Detect important concepts without own pages
  ├─ Check missing cross-references
  └─ Suggest new questions to investigate + sources to find
```

**Phân tích:**
- Lint là mechanism tự động duy trì wiki health — critical cho long-term viability
- "LLM is good at suggesting new questions" = active knowledge discovery, không passive retrieval
- Risk: LLM có thể generate false positives trong lint results

---

## 4. Tooling Ecosystem

### 4.1 Search Engine (qmd)

- **qmd:** Local search engine for markdown files, hybrid BM25/vector + LLM re-ranking
- CLI + MCP server support
- Required khi wiki grows beyond index.md effectiveness

### 4.2 Obsidian Integration

| Tool | Purpose | Benefit |
|------|---------|---------|
| Web Clipper | Convert articles to markdown | Fast source ingestion |
| Graph View | Visualize connections | Wiki shape awareness |
| Marp | Slide decks from wiki content | Presentation generation |
| Dataview | Query frontmatter | Dynamic tables/lists |
| Git | Version control | History, branching, collaboration |

### 4.3 Image Handling

- Download images locally (attachment folder in Obsidian)
- LLM read text first → view images separately (workaround for single-pass limitation)

---

## 5. Historical Context

**Vannevar Bush's Memex (1945):**
- Personal, curated knowledge store with associative trails
- Connections between documents as valuable as documents themselves
- Bush couldn't solve: "who does the maintenance?"
- LLM Wiki Pattern solves this — LLM handles maintenance, human curates

**So sánh:**
| Aspect | Memex (1945) | RAG | LLM Wiki Pattern |
|--------|-------------|-----|-----------------|
| Storage | Physical cards/files | Vector DB | Markdown files |
| Retrieval | Associative trails | Similarity search | Index + drill-down |
| Accumulation | Manual linking | None (per-query) | Incremental, compounding |
| Maintenance | Human only | None needed | LLM automated |

---

## 6. Self-Critique Round 1 — Architecture Claims

### Claim: "3-layer architecture is novel and sufficient"

**Phản biện:**
- **Thiếu layer semantic:** Không có mechanism cho ontology/knowledge graph ở cấp độ cao hơn markdown links. Wiki pages linked by text references, không bằng structured relationships (không phải RDF/property-based).
- **Raw sources immutable — đúng hay sai?** Đúng về mặt audit trail, nhưng sai về practicality khi cần extract metadata, thumbnails, hoặc convert formats. Tác giả không đề cập preprocessing pipeline.
- **Schema co-evolution:** Tác giả nói "human + LLM co-evolve schema" nhưng không định nghĩa boundary — ai quyết định khi schema conflict? Không có mechanism versioning cho schema changes → risk của breaking changes.

**Verdict:** 3-layer model là abstraction hữu ích nhưng oversimplified. Real-world implementation cần thêm: (1) semantic layer cho structured relationships, (2) preprocessing pipeline cho raw sources, (3) schema versioning strategy.

### Claim: "LLM owns wiki entirely"

**Phản biện:**
- **Scope of ownership:** LLM tạo pages và update cross-refs, nhưng human vẫn phải: curate sources, guide discussion, review summaries, decide which queries are "good enough to file back". Ownership là shared, không exclusive.
- **Consistency guarantee:** "Keeps everything consistent" — nhưng consistency ở mức nào? Surface-level (links work) hay deep-level (claims align)? Không có mechanism cho consistency verification.

**Verdict:** LLM ownership là claim hợp lý cho operational tasks, nhưng strategic decisions vẫn cần human oversight. Model này hoạt động tốt khi human-in-loop được duy trì.

---

## 7. Self-Critique Round 2 — Operations & Scalability

### Claim: "Index-first search works at moderate scale (~100 sources, hundreds of pages)"

**Phản biện:**
- **Index degradation:** Khi wiki grows >500 pages, index.md becomes unwieldy (có thể >50K tokens). Reading full index mỗi query = inefficient. Tác giả không đề cập indexing strategy optimization (partial reads, category filters).
- **qmd dependency:** Tác giả nói "at small scale index is enough" — transition point unclear. Khi nào cần qmd? Không có metric cho decision boundary.
- **Search precision:** BM25 + vector hybrid trong qmd tốt hơn text search đơn thuần, nhưng không giải quyết vấn đề semantic ambiguity (từ nhiều nghĩa).

**Phản biện sâu hơn:** 
- Index-first approach là trade-off: simple và fast ở small scale, nhưng cần migration path khi scale. Solution: category-indexed index (partition by topic), incremental index updates (không rebuild toàn bộ mỗi ingest).

### Claim: "Single source touches 10-15 wiki pages"

**Phản biện:**
- **Overhead estimation:** 10-15 file writes per ingest = substantial I/O + token cost. Với LLM local (Ollama), context window management quan trọng — mỗi page write cần load context, generate content, save. 
- **Batch efficiency:** Tác giả đề cập batch-ingest nhưng không định nghĩa limits. Batch 10 sources → potentially 150 file operations = risk of context overflow + inconsistent updates.
- **No parallelism strategy:** Không đề cập parallel processing (multiple pages simultaneously). Thực tế, entity page updates có thể parallelized nếu không dependencies.

**Verdict:** Operations scale được nhưng cần optimization: (1) selective page updates (không phải mọi page cần update mỗi ingest), (2) batch size limits (~5 sources max), (3) parallel write strategy cho independent pages.

### Claim: "LLM is good at suggesting new questions to investigate"

**Phản biện:**
- **Quality variance:** Suggestion quality phụ thuộc vào scope của wiki hiện tại. Wiki narrow domain → suggestions focused nhưng limited. Wiki broad → suggestions diverse nhưng có thể irrelevant.
- **No feedback loop:** Không có mechanism để human rate suggestion quality → LLM không learn từ feedback. Suggestions có thể repetitive sau nhiều lint passes.

---

## 8. Self-Critique Round 3 — Comparison & Real-World Viability

### Claim: "Wiki is persistent, compounding artifact — better than RAG"

**Phản biện:**
- **Accumulation advantage là thật:** Wiki tích lũy knowledge → query cost giảm theo thời gian (không phải re-retrieve mọi source mỗi lần). Đây là lợi thế thực sự so với RAG.
- **Tuy nhiên:** RAG cũng có accumulation qua embedding updates. Difference không phải "có/không accumulation" mà là "type of accumulation": RAG = vector accumulation, Wiki = semantic/structural accumulation.
- **Cost comparison:** 
  - RAG: High initial setup (embeddings + vector DB) → low per-query cost
  - Wiki: Low initial setup (markdown files) → variable per-query cost (depends on wiki size + search strategy)

**Verdict:** Wiki pattern tốt hơn cho use cases cần deep synthesis và cross-document reasoning. RAG tốt hơn cho high-volume queries với moderate complexity. Không phải replacement, là complement.

### Claim: "Maintenance cost near zero with LLMs"

**Phản biện:**
- **Token cost thực tế:** Mỗi lint pass = read all pages → detect issues → generate fix suggestions. Với 500 pages × avg 2K tokens/page = 1M+ tokens per lint pass. Với local Ollama, thời gian processing có thể 5-15 phút.
- **Human verification cost:** LLM suggest fixes, nhưng human vẫn phải review và approve (đặc biệt cho contradictory claims). "Near zero" chỉ đúng khi wiki stable — khi đang growing, maintenance cost cao hơn nhiều.
- **Stale data risk:** Wiki content có thể stale nếu source không được ingest regularly. Không có mechanism auto-detect outdated sources.

### Claim: "Works for personal, research, reading, business contexts"

**Phản biện:**
- **Personal use:** Dễ nhất — scope narrow, human fully in control. High viability.
- **Research use:** Medium complexity — nhiều sources, cần citation accuracy. Viability cao nếu schema well-defined.
- **Reading a book (fan wiki):** Good fit — structured domain (characters, plot threads), predictable page types. Tác giả dùng Tolkien Gateway làm analogy là chính xác.
- **Business/team:** Thách thức nhất — multiple contributors, varying source quality, need access control. Viability phụ thuộc vào team discipline + LLM reliability.

**Verdict:** Pattern universal về concept, nhưng implementation cần customization theo context. Không phải "one size fits all".

---

## 9. Áp dụng vào Smee Obsidian Vault

### Current State
- Vault có cấu trúc PARA + Zettelkasten hybrid
- Có 7 templates, 9 PARA folders
-已有 vault master index + evolution tracker
- Cron jobs: Daily Vault Maintenance (120s timeout) + Memory Dreaming

### LLM Wiki Pattern Integration Plan

| Karpathy Concept | Smee Implementation |
|-----------------|-------------------|
| Raw sources | `30-Resources/` — immutable source files |
| Wiki | `40-Knowledge-Synthesis/` — LLM-generated notes |
| Schema | AGENTS.md + `_templates/` — wiki conventions |
| index.md | `vault-master-index.md` (existing) |
| log.md | Daily notes (`02-Daily/`) + session logs |
| Ingest | New learning → capture to vault with backlinks |
| Query | Search vault → synthesize answer → file back |
| Lint | Daily Vault Maintenance cron — check orphans, stale claims |

### Gap Analysis
- **Missing:** Semantic layer (structured relationships between notes)
- **Missing:** Schema versioning for wiki conventions
- **Present but weak:** Batch ingest strategy (current max 2 notes/session)
- **Opportunity:** Implement index-first search optimization (category-indexed index)

---

## 10. Key Takeaways + Action Items

### Insights chính
1. **LLM Wiki Pattern** là evolution của RAG: từ per-query retrieval → persistent compounding knowledge
2. **Index-first search** smart choice ở moderate scale — avoid vector DB overhead
3. **Human-in-loop discussion** during ingest quan trọng cho quality control
4. **Lint workflow** là secret weapon cho long-term wiki health
5. **Vannevar Bush's Memex vision** finally realized với LLM as maintenance engine

### Action Items cho Smee
- [ ] Implement category-indexed index trong vault master index
- [ ] Add lint pass vào Daily Vault Maintenance cron (expand timeout)
- [ ] Define schema versioning strategy cho wiki conventions
- [ ] Test batch ingest với max 5 sources per session
- [ ] Create entity/concept page templates aligned with Karpathy pattern

---

## 11. References

- Karpathy, Andrej. "LLM Wiki Pattern." GitHub Gist, 2026. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Bush, Vannevar. "As We May Think." The Atlantic Monthly, July 1945. (Memex concept)
- Smee Vault Architecture: `Insights/vault-architecture.md`
- Smee Vault Master Index: `Insights/vault-master-index.md`

---

*Phân tích hoàn thành: 2026-06-16 | Tổng từ: ~3500+ | Self-critique rounds: 3/3*
