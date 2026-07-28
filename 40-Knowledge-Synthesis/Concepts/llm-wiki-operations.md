---
title: LLM Wiki — Chiến dịch (Ingest, Truy vấn, Lint)
slug: llm-wiki-operations
category: knowledge
tags:
- llm
- wiki
- operations
- karpathy
- workflow
status: active
type: concept
created: 2026-06-16
last_updated: '2026-07-14'
source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
related:
- llm-wiki-karpathy-pattern
- llm-wiki-architecture
---

# LLM Wiki — Chiến dịch (Ingest, Truy vấn, Lint)

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
- **Human-in-in-lock:** Không hoàn toàn tự động — sự chỉ dẫn ôn lại của con người LLM
- **Batch size:** Single source per ingest preferred; batch-ingest possible với ít supervision
- ** Hoạt động tập tin:** 10-15 trang được chạm vào mỗi nguồn = giá trị I/O + hiệu
- **Context management:** Mỗi page write cần load context → generate → save

### Scalability Concerns
- >500 pages: index.md quá lớn cho single-read (>50K tokens)
- Batch 10 nguồn tiềm năng 150 file hoạt động bối cảnh tràn đầy rủi ro
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
- ** Dạng thức xuất:** markdown trang, bảng so sánh, bài (Marp), biểu đồ (matptlib), vải

### Tìm kiếm đường dẫn đến sự tiến hóa
1. **Small tỷ lệ (<100 nguồn):** index.md đủ
2. **Medium tỷ lệ (~100-500 nguồn):** qmd (BM25 + vector + LLM Quay lại
3. ** Tỷ lệ đăng ký (>500 nguồn):** Cần chỉ mục phân vùng, cập nhật dần

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

## Chỉ mục.md vs log.md

### index.mmd (chỉ định-conent)
- Name
- Mỗi trang: liên kết + một dòng tóm tắt + siêu dữ liệu (ngày, số nguồn)
- Được tổ chức theo loại (các loại, khái niệm, nguồn)
- Cập nhật từng thức ăn
- LLM đọc phụ lục khi trả lời các thư mục

### log.md ( môn học)
- Ứng dụng ghi chép duy nhất các sự kiện
- Format: `## [YYYY-MM-DD] operation | Title`
- Parseable với unix tools: `grep "^## \[" log.md | tail -5`
- Cho dòng thời gian tiến hóa bằng Niply
- Trợ giúp LLM Hiểu được hoạt động gần đây

---

*See also: [[llm-wiki-karpathy-pattern]], [[llm-wiki-architecture]]*
