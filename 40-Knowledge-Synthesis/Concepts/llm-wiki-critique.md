---
title: LLM Wiki — Tự gọi (3 vòng)
slug: llm-wiki-critique
category: knowledge
tags:
- llm
- wiki
- critique
- karpathy
- analysis
status: active
type: concept
created: 2026-06-16
last_updated: '2026-07-14'
source: GitHub Gist - Karpathy LLM Wiki Pattern
related:
- llm-wiki-karpathy-pattern
- llm-wiki-architecture
- llm-wiki-operations
---

# LLM Wiki — Tự nhận dạng 3 vòng tròn (Karpamey)

## Vòng 1: Kiến trúc khẳng định

### Nói: "Một kiến trúc 3-Sader là tiểu thuyết và đủ"

**Critique:**
- **Thiếu semantic layer:** Wiki pages linked by text references, không structured relationships (không RDF/property-based). Không có ontology ở cấp độ cao hơn markdown links.
- **Raw sources immutable — đúng về audit trail nhưng sai về practicality.** Cần preprocessing pipeline cho metadata extraction, thumbnail generation, format conversion. Tác giả không đề cập.
- **Schema co-evolution risk:** Human + LLM refine schema together nhưng không có mechanism versioning → breaking changes risk khi schema drift.

**Verdict:** 3-layer model hữu ích nhưng oversimplified. Cần thêm: (1) semantic layer cho structured relationships, (2) preprocessing pipeline, (3) schema versioning strategy.

### Nói: "LLM sở hữu toàn bộ cord"

**Critique:**
- **Ownership độc giả dùng chung:** LLM Tác vụ hoạt động ( Tạo trang, cập nhật các trang, cập nhật các tin tức, các quyết định chiến lược của con người (các nguồn đáng ngờ, hướng dẫn thảo luận, duyệt lại, quyết định chất lượng câu trả lời).
- **Consistency guarantee ambiguous:** Surface-level (links work) hay deep-level (claims align)? Không có mechanism cho consistency verification.

**Verdict:** LLM ownership hợp lý cho operational tasks, nhưng strategic decisions cần human oversight. Model hoạt động tốt khi human-in-loop duy trì.

## Vòng 2: Hoạt động & Hình vuông

### Tuyên bố: "Tìm kiếm đầu tiên ở mức vừa phải [~100 nguồn, hàng trăm trang]

**Critique:**
- **Index degradation >500 pages:** index.md có thể >50K tokens → reading full index per query = inefficient. Không đề cập optimization strategy (partial reads, category filters).
- **qmd transition point unclear:** Khi nào cần qmd? Không metric cho decision boundary.
- **Search precision:** BM25 + vector hybrid tốt hơn text search nhưng không giải quyết semantic ambiguity (từ nhiều nghĩa).

**Solution:** Category-indexed index (partition by topic), incremental index updates (không rebuild toàn bộ mỗi ingest).

### Tuyên bố: " Nguồn từ tầu Single chạm 1015 trang size"

**Critique:**
- **Overhead estimation:** 10-15 file writes = substantial I/O + token cost. Context window management quan trọng cho local LLM.
- ** Hiệu quả Batch không xác định:** Batch 10 nguồn tiềm năng 150 hồ sơ hoạt động trong bối cảnh tràn ngập rủi ro.
- **No parallelism strategy:** Independent page updates có thể parallelized.

**Verdict:** Operations scalable nhưng cần: (1) selective page updates, (2) batch size limits (~5 sources max), (3) parallel write strategy.

### Nói: "LLM tốt trong việc đưa ra những câu hỏi mới"

**Critique:**
- **Quality variance phụ thuộc scope:** Narrow domain → focused but limited suggestions. Broad domain → diverse but potentially irrelevant.
- **No feedback loop:** Human không rate suggestion quality → LLM không learn. Suggestions có thể repetitive sau nhiều lint passes.

## Vòng 3: Khả năng so sánh/ Mặc định thế giới

### Tuyên bố: "Gia đình hợp hơn RAG"

**Critique:**
- **Accumulation advantage là thật:** Wiki tích lũy knowledge → query cost giảm theo thời gian. Không phải re-retrieve mọi source mỗi lần.
- **Tuy nhiên:** RAG cũng có accumulation qua embedding updates. Difference là type: RAG = vector accumulation, Wiki = semantic/structural accumulation.
- **Cost comparison:**
  - RAG: mức thiết lập đầu tiên thấp trên mỗi cửa sổ (tốt cho mức độ phức tạp cao, vừa phải)
  - Wiki: giá thiết lập thấp biến đầu tiên cho mỗi tùy chọn (tốt cho sự tổng hợp sâu, lập luận thập phân)

**Verdict:** Wiki pattern tốt hơn cho use cases cần deep synthesis. RAG tốt hơn cho high-volume queries. **Complement, không replacement.**

### Tuyên bố: "Tiền tăng cường gần 0 với llMs"

**Critique:**
- **Token cost thực tế:** Lint pass = read all pages → detect issues → generate fixes. 500 pages × 2K tokens = 1M+ tokens/pass (local Ollama: 5-15 phút).
- **Human verification cost:** LLM suggest fixes, human review + approve (đặc biệt contradictory claims). "Near zero" chỉ đúng khi wiki stable — growing phase cao hơn nhiều.
- **Stale data risk:** Không có mechanism auto-detect outdated sources nếu không ingest regularly.

### Nói: "Công việc cho cá nhân, nghiên cứu, đọc, kinh doanh"

**Viability matrix:**

| Context | Complexity | Viability | Yếu tố quan trọng để thành công |
|---------|-----------|-----------|-------------------|
| Personal | Low | High | Con người hoàn toàn kiểm soát được. |
| Research | Medium-High | Medium-High | Comment |
| Đọc (fan izz) | Medium | High | Vùng cấu trúc, kiểu trang có thể đoán trước |
| Business/Team | High | Medium | Hệ thống sửa trị cộng LLM Name |

**Verdict:** Pattern universal về concept, nhưng implementation cần customization theo context. **Không phải "one size fits all".**

---

## Tóm tắt Critique

### Sự thông cảm đúng đắn
1. ✅ Index-first search là smart choice ở moderate scale
2. ▪ Kiến thức tổng hợp qua các mảnh gốm bền bỉ — lợi thế hơn RAG
3. ✅ Lint workflow là secret weapon cho long-term maintenance
4. ✅ Human-in-loop discussion during ingest quan trọng cho quality

### Thiếu sót gì hay quá phổ biến
1. Lớp Semantic (những mối quan hệ có cấu trúc bên ngoài liên kết văn bản)
2. Chiến lược phiên bản _bản kế hoạch
3. Đường dẫn khả năng cấu hình (>500 trang — chỉ số bị thoái hóa, phân chia)
4. Chiến thuật song song cho các hoạt động hàng loạt
5. _Nghề ngược lại để học chất lượng
6. _Công cụ trước các đường ống dẫn cho các nguồn thô đa dạng

### Recommended Enhancements
- Thêm mục lục đã phân loại (bị phân loại theo chủ đề)
- Implement incremental index updates (không rebuild toàn bộ)
- Define schema versioning với backward compatibility
- Giới hạn cỡ mẻ (~5 nguồn tối đa mỗi lần ăn)
- Tạo cơ chế phản hồi cho các đề nghị bổ sung
- Đang xử lý đường ống dẫn cho việc lấy siêu dữ liệu nguồn thô

---

*See also: [[llm-wiki-karpathy-pattern]], [[llm-wiki-architecture]], [[llm-wiki-operations]]*
