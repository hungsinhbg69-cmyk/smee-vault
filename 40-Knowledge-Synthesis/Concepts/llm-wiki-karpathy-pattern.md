---
title: LLM Mẫu Wiki (Karpathy)
slug: llm-wiki-karpathy-pattern
category: knowledge
tags:
- llm
- wiki
- knowledge-management
- rag
- pattern
status: active
type: concept
created: 2026-06-16
last_updated: '2026-07-14'
sources:
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
related_tags:
- karpathy
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
| Raw sources | Tài liệu nguồn (hình ảnh, giấy, ảnh) | Human | Immutable |
| The wiki | LLM- Phát triển markdown tập tin (baseries, trang thực thể, trang khái niệm) | LLM | Mutable |
| The schema | Tiến sĩ cấu hình (CLUUDE / AgentS.md) — nói LLM Cách duy trì ngọc trai | Human + LLM | Co-evolve |

### 3 Operations

1. **Ingest:** Nguồn thả LLM đọc __Nghề nghiệp
2. ** Hỏi:** Hỏi ____________________________________________________________________i LLM Tìm kiếm trang liên quan _ đáp án tổng hợp với trích dẫn _Rraws câu trả lời tốt được điền vào i- vi-a
3. **Lint:** Kiểm tra sức khỏe định kì i kiểm tra định kỳ tìm thấy mâu thuẫn, tuyên bố cũ, trang mồ côi, các dấu hiệu bị thiếu, lỗ hổng dữ liệu

### 2 Special Files

- **index.md** — Sổ tay nội dung ( liên kết + tóm tắt + siêu dữ liệu), cập nhật mỗi thức ăn
- **log.md** — Phụ đề thời gian sử dụng (không có thời gian)`## [YYYY-MM-DD] operation | Title`)

---

## 2. Phân tích chi tiết từng component

### Lớp nguyên thô 2. 1

**Claim chính:** Sources là immutable, LLM chỉ đọc không viết lại.

**Ưu điểm:**
- Một nguồn lẽ thật duy nhất — nạn tham nhũng dữ liệu
- Audit trail rõ ràng: wiki có thể trace back về source gốc
- Phiên bản Dễ điều khiển v Whoi git ( nam tính tập tin + i)

**Hạn chế:**
- Với sources lớn (>100 pages), việc LLM "đọc hết" mỗi lần ingest tốn token
- Không có mechanism tự động extract metadata từ raw sources (tác giả đề cập nhưng không chi tiết)
- Format diversity: articles, papers, images, data files — mỗi loại cần preprocessing khác nhau

### 2. 2. 2.

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

### 2. 3 Lớp kế hoạch

**Claim chính:** Schema document là config file quan trọng nhất — biến LLM từ generic chatbot thành disciplined wiki maintainer.

**Nội dung schema điển hình (suy luận):**
- Comment
- Mẫu định dạng trang (frontmatter, tiêu đề)
- Bước làm việc nhanh nhất
- Định dạng trả lời truy vấn
- Lint checklist
- Naming conventions

**Ưu điểm:**
- Sự đồng tiến hóa: con người + LLM Comment
- Tùy chỉnh đặc trưng miền

**Hạn chế:**
- Schema complexity grows with wiki size → maintenance overhead tăng
- Cần human oversight để prevent LLM từ "drift" khỏi intended structure
- Không có versioning mechanism cho schema changes

---

## 3 Chiến dịch lặn sâu

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
- Tránh cần thiết cơ sở dữ liệu co sở dữ liệu véc- tơ (qmd tùy chọn)
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
- "LLM là tốt trong đề nghị câu hỏi mới " = khám phá kiến thức tích cực, kông thụ động tái tạo
- Risk: LLM có thể generate false positives trong lint results

---

## 4. Tooling Ecosystem

### 4. 1 Cơ chế tìm kiếm (qmd)

- **qmd:** Công cụ tìm kiếm cục bộ cho markdown tập tin, BM25/vtor + LLM Quay lại
- CLI + MCP Hỗ trợ máy phục vụ
- Cần thiết khi size phát triển vượt quá hiệu quả chỉ mục.md

### 4.2 Obsidian Integration

| Tool | Purpose | Benefit |
|------|---------|---------|
| Web Clipper | Chuyển đổi các bài sang markdown | Name |
| Graph View | Visualize connections | Nhận thức hình Wiki |
| Marp | Name | Presentation generation |
| Dataview | Query frontmatter | Comment |
| Git | Version control | Lịch sử, chi nhánh, hợp tác |

### 4.3 Image Handling

- Tải về các ảnh cục bộ (thư mục gắn kết trong Obsidian)
- LLM Đọc văn bản đầu tiên _xem riêng ảnh (làm việc cho chỉ giới hạn qua cầu)

---

## 5. Historical Context

**Vannevar Bush's Memex (1945):**
- Những kiến thức cá nhân, được quản lý với những dấu vết liên kết
- Kết nối giữa tài liệu có giá trị như tài liệu
- Bush không thể giải câu: "Ai làm bảo trì?"
- LLM Mẫu Wiki giải quyết được vấn đề này — LLM Giữ gìn sức khỏe, chữa bệnh cho con người

**So sánh:**
| Aspect | Memex (1945) | RAG | LLM Wiki Pattern |
|--------|-------------|-----|-----------------|
| Storage | Thẻ thể chất/ tập tin | Vector DB | Markdown files |
| Retrieval | Associative trails | Similarity search | Chỉ mục + khoan xuống |
| Accumulation | Manual linking | Không có (hay yêu cầu) | Incremental, compounding |
| Maintenance | Human only | None needed | LLM automated |

---

## 6. Tự nhận là mình là người duy nhất sống sót.

### Nói: "Một kiến trúc 3-Sader là tiểu thuyết và đủ"

**Phản biện:**
- **Thiếu layer semantic:** Không có mechanism cho ontology/knowledge graph ở cấp độ cao hơn markdown links. Wiki pages linked by text references, không bằng structured relationships (không phải RDF/property-based).
- **Raw sources immutable — đúng hay sai?** Đúng về mặt audit trail, nhưng sai về practicality khi cần extract metadata, thumbnails, hoặc convert formats. Tác giả không đề cập preprocessing pipeline.
- **Schema co-evolution:** Tác giả nói "human + LLM co-evolve schema" nhưng không định nghĩa boundary — ai quyết định khi schema conflict? Không có mechanism versioning cho schema changes → risk của breaking changes.

**Verdict:** 3-layer model là abstraction hữu ích nhưng oversimplified. Real-world implementation cần thêm: (1) semantic layer cho structured relationships, (2) preprocessing pipeline cho raw sources, (3) schema versioning strategy.

### Nói: "LLM sở hữu toàn bộ cord"

**Phản biện:**
- **Scope of ownership:** LLM tạo pages và update cross-refs, nhưng human vẫn phải: curate sources, guide discussion, review summaries, decide which queries are "good enough to file back". Ownership là shared, không exclusive.
- **Consistency guarantee:** "Keeps everything consistent" — nhưng consistency ở mức nào? Surface-level (links work) hay deep-level (claims align)? Không có mechanism cho consistency verification.

**Verdict:** LLM ownership là claim hợp lý cho operational tasks, nhưng strategic decisions vẫn cần human oversight. Model này hoạt động tốt khi human-in-loop được duy trì.

---

## 7, Tự kiểm tra liên kết 2 — Chiến dịch & Xác thực

### Tuyên bố: "Tìm kiếm đầu tiên ở mức vừa phải [~100 nguồn, hàng trăm trang]

**Phản biện:**
- **Index degradation:** Khi wiki grows >500 pages, index.md becomes unwieldy (có thể >50K tokens). Reading full index mỗi query = inefficient. Tác giả không đề cập indexing strategy optimization (partial reads, category filters).
- **qmd dependency:** Tác giả nói "at small scale index is enough" — transition point unclear. Khi nào cần qmd? Không có metric cho decision boundary.
- **Search precision:** BM25 + vector hybrid trong qmd tốt hơn text search đơn thuần, nhưng không giải quyết vấn đề semantic ambiguity (từ nhiều nghĩa).

**Phản biện sâu hơn:** 
- Index-first approach là trade-off: simple và fast ở small scale, nhưng cần migration path khi scale. Solution: category-indexed index (partition by topic), incremental index updates (không rebuild toàn bộ mỗi ingest).

### Tuyên bố: " Nguồn từ tầu Single chạm 1015 trang size"

**Phản biện:**
- **Overhead estimation:** 10-15 file writes per ingest = substantial I/O + token cost. Với LLM local (Ollama), context window management quan trọng — mỗi page write cần load context, generate content, save. 
- **Batch efficiency:** Tác giả đề cập batch-ingest nhưng không định nghĩa limits. Batch 10 sources → potentially 150 file operations = risk of context overflow + inconsistent updates.
- **No parallelism strategy:** Không đề cập parallel processing (multiple pages simultaneously). Thực tế, entity page updates có thể parallelized nếu không dependencies.

**Verdict:** Operations scale được nhưng cần optimization: (1) selective page updates (không phải mọi page cần update mỗi ingest), (2) batch size limits (~5 sources max), (3) parallel write strategy cho independent pages.

### Nói: "LLM là tốt trong đề nghị những câu hỏi mới để điều tra"

**Phản biện:**
- **Quality variance:** Suggestion quality phụ thuộc vào scope của wiki hiện tại. Wiki narrow domain → suggestions focused nhưng limited. Wiki broad → suggestions diverse nhưng có thể irrelevant.
- **No feedback loop:** Không có mechanism để human rate suggestion quality → LLM không learn từ feedback. Suggestions có thể repetitive sau nhiều lint passes.

---

## 8. Tự gọi là Vòng 3 — So sánh & Tính bền vững của thế giới

### Nói: "Wiki là người kiên trì, hợp nhất — tốt hơn RAG"

**Phản biện:**
- **Accumulation advantage là thật:** Wiki tích lũy knowledge → query cost giảm theo thời gian (không phải re-retrieve mọi source mỗi lần). Đây là lợi thế thực sự so với RAG.
- **Tuy nhiên:** RAG cũng có accumulation qua embedding updates. Difference không phải "có/không accumulation" mà là "type of accumulation": RAG = vector accumulation, Wiki = semantic/structural accumulation.
- **Cost comparison:** 
  - RAG: thiết lập cấp cao (mbebeds + véc tơ DB) giá rẻ trên mỗi cửa sổ
  - Wiki: Thiết lập ban đầu thấp (markdown Tập tin) Chi phí biến trên mỗi cửa sổ (phụ thuộc vào kích cỡ HTML + chiến lược tìm kiếm)

**Verdict:** Wiki pattern tốt hơn cho use cases cần deep synthesis và cross-document reasoning. RAG tốt hơn cho high-volume queries với moderate complexity. Không phải replacement, là complement.

### Tuyên bố: "Tiền tăng cường gần 0 với llMs"

**Phản biện:**
- **Token cost thực tế:** Mỗi lint pass = read all pages → detect issues → generate fix suggestions. Với 500 pages × avg 2K tokens/page = 1M+ tokens per lint pass. Với local Ollama, thời gian processing có thể 5-15 phút.
- **Human verification cost:** LLM suggest fixes, nhưng human vẫn phải review và approve (đặc biệt cho contradictory claims). "Near zero" chỉ đúng khi wiki stable — khi đang growing, maintenance cost cao hơn nhiều.
- **Stale data risk:** Wiki content có thể stale nếu source không được ingest regularly. Không có mechanism auto-detect outdated sources.

### Nói: "Công việc cho cá nhân, nghiên cứu, đọc, kinh doanh"

**Phản biện:**
- **Personal sử dụng:** Dễ nh sự trong phạm vi hẹp, con người hoàn toàn kiểm soát được.
- **Research use:** Medium complexity — nhiều sources, cần citation accuracy. Viability cao nếu schema well-defined.
- **Reading a book (fan wiki):** Good fit — structured domain (characters, plot threads), predictable page types. Tác giả dùng Tolkien Gateway làm analogy là chính xác.
- **Business/team:** Thách thức nhất — multiple contributors, varying source quality, need access control. Viability phụ thuộc vào team discipline + LLM reliability.

**Verdict:** Pattern universal về concept, nhưng implementation cần customization theo context. Không phải "one size fits all".

---

## 9. Áp dụng vào Smee Obsidian Vault

### Current State
- Vault có cấu trúc PARA + Zettelkasten hybrid
- Có 7 templates, 9 PARA folders
- Chỉ mục chính của hầm hầm và thiết bị theo dõi tiến hóa
- Công việc củaron: Bảo trì cổng hàng ngày (120) + mơ ước

### LLM Kế hoạch hợp nhất mẫu Wiki

| Karpathy Concept | Smee Implementation |
|-----------------|-------------------|
| Raw sources | `30-Resources/` - Tập tin nguồn không thể thay đổi |
| Wiki | `40-Knowledge-Synthesis/` — LLM-generated notes |
| Schema | Đặc vụ S.md + `_templates/` - Đại hội  kiên cố |
| index.md | `vault-master-index.md` (existing) |
| log.md | Ghi chú hàng ngày (`02-Daily/`+ bản ghi phiên chạy |
| Ingest | Học tập mới bắt được một quả bom có đường dây lưng |
| Query | Tìm hầm → Tổng hợp câu trả lời → tập tin |
| Lint | Bảo trì cổng hàng ngày — Kiểm tra trẻ mồ côi, tuyên bố cũ |

### Gap Analysis
- ** than:** Lớp Semantic (những mối quan hệ có cấu trúc giữa ghi chú)
- ** than phiền:** Schema phiên bản cho các hội nghị  size size
- **Tọa độ nhưng yếu:** Chiến lược ăn Batch (hiện tại 2 ghi chú/ssition)
- **Opportunity:** Vẫn còn phụ lục tìm kiếm đầu tiên (tiểu đồ phân loại)

---

## 10. Khóa

### Insights chính
1. **LLM Wiki Pattern** là evolution của RAG: từ per-query retrieval → persistent compounding knowledge
2. **Index-first search** smart choice ở moderate scale — avoid vector DB overhead
3. **Human-in-loop discussion** during ingest quan trọng cho quality control
4. **Lint workflow** là secret weapon cho long-term wiki health
5. **Vannevar Bush's Memex vision** finally realized với LLM as maintenance engine

### Mục hành động cho Smee
- [ ] Phần mềm phân loại chỉ mục chạy trên tầng hầm
- [ ] Add lint pass vào Daily Vault Maintenance cron (expand timeout)
- [ ] Định nghĩa chiến lược phiên bản cho các hội nghị schema
- [ ] Test batch ingest với max 5 sources per session
- [ ] Tạo mẫu trang/hình ảnh thẳng hàng với mẫu Karpaty

---

## 11. References

- Karpally, Andrej."LLM Mẫu của Wiki." GitHub Gia sư, 2026. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Bush, Vannevar. "Như chúng ta nghĩ." Tháng 7 Đại Tây Dương, tháng 7 năm 1945.
- Kiến trúc Cổng Smee: `Insights/vault-architecture.md`
- Chỉ mục Đóng cửa Smee: `Insights/vault-master-index.md`

---

*Phân tích hoàn thành: 2026-06-16 | Tổng từ: ~3500+ | Self-critique rounds: 3/3*
