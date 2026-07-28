---
title: LLM Wiki — Sự thông sáng và ứng dụng
slug: llm-wiki-insights
category: knowledge
tags:
- llm
- wiki
- insights
- karpathy
- application
status: active
type: insight
created: 2026-06-16
last_updated: '2026-07-14'
source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
related:
- llm-wiki-karpathy-pattern
- llm-wiki-architecture
- llm-wiki-operations
- llm-wiki-critique
---

# LLM Wiki — Sự thông sáng và ứng dụng (Karpaathy)

## Key Insights

### 1. Vấn đề sổ sách
> "Điều tẻ nhạt trong việc duy trì một nền tảng kiến thức không phải là đọc hay suy nghĩ - đó là việc giữ sổ sách."

- Humans abandon wikis vì maintenance burden grows faster than value
- HM không cảm thấy chán, không quên qua f(x), có thể chạm 15 file trên mỗi thẻ
- **Insight:** LLM không phải thay thế human thinking — mà giải quyết operational overhead

### Khu 2.
- ** Công việc củaHuman:** Nguồn tin Curate, phân tích trực tiếp, đặt câu hỏi hay, nghĩ về ý nghĩa
- **LLMCông việc của họ:** Những thứ khác (chỉ là tổng hợp, tham khảo chéo, hồ sơ, sổ sách)
- **Insight:** Human-in-loop không phải "supervision" — mà là "direction"

### Vannevar Bush's Memex nhận ra (1945 _2026)
Bush Hình dung: lưu trữ kiến thức cá nhân với các đường dẫn liên kết giữa các tài liệu. riêng tư, tích cực quản lý, kết nối có giá trị như nội dung.
- **Những gì ông ta không thể giải quyết:** Ai bảo trì?
- **LLM Mẫu Wiki giải quyết điều này:** LLM Giữ gìn sức khỏe, chữa bệnh cho con người

### 4. RAG đấu với Wiki — Ca ngợi không thay thế
| | RAG | LLM Wiki |
|--|-----|---------|
| Best for | Các biểu đồ tần xuất cao, độ phức tạp vừa phải | Tổng hợp sâu, lập luận xuyên đại diện |
| Accumulation type | Vector (passive) | Semantic/ nartal (hoạt động) |
| Initial cost | Tào Tháo (mmeds + DB) | Low (markdown files) |
| Chi phí mua bán đơn giản | Low | Biến (phụ thuộc vào kích cỡ của quần đảo) |

### Comment
- Tại ~100 nguồn tài liệu, hàng trăm trang: index.md làm việc rất tốt
- Tránh cơ sở dữ liệu co sở dữ liệu véc tơ trên đầu
- Migration path to qmd khi scale lên

## Ứng dụng vào Cổng Smee

### Current Alignment
| Karpathy Concept | Smee Implementation | Status |
|-----------------|-------------------|--------|
| Raw sources | `30-Resources/` | ✅ Aligned |
| Wiki | `40-Knowledge-Synthesis/` | ✅ Aligned |
| Schema | AGENTS.md + `_templates/` | ✅ Aligned |
| index.md | `vault-master-index.md` | ✅ Exists |
| log.md | Daily notes (`02-Daily/`) | ⚠️ Partial |
| Ingest | Học tập mới _bắt bằng các đường hậu | ✅ Working |
| Query | Tập tin tổng hợp tập tin _pô | ⚠️ Manual |
| Lint | Bảng điều khiển cổng hàng ngày | ⚠️ Needs expansion |

### Thêm mục phân tích và hành động

**Gaps identified:**
1. Thiếu lớp Semantic — ghi chú được liên kết bởi văn bản, chứ không phải thuộc tính cấu trúc
2. Comment
3. Nhiễm sắc thể chỉ ăn 2 nốt/sesion (Karpaathy gợi ý 10-15)
4. Tìm kiếm phụ lục đầu không tối ưu hóa (không phân chia phân loại)

**Action items:**
- [ ] Phần phụ đề:
- [ ] Mở rộng thanh công cụ bảo trì hàng ngày cron times + thêm lipt pass
- [ ] Định nghĩa các quy tắc phiên bản cho các hội nghị schema
- [ ] Test batch ingest với max 5 sources per session
- [ ] Tạo mẫu trang/hình ảnh thẳng hàng với mẫu Karpaty

### Khuyên dùng công việc cho Smee

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
