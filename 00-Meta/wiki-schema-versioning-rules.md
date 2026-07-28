---
title: "Các quy tắc về kế hoạch của Wiki"
slug: "wiki-schema-versioning-rules"
category: meta
tags: [schema, versioning, wiki, karpathy, governance]
date: 2026-06-16
type: schema
created: 2026-06-16
version: "1.0.0"
status: active
last_updated: 2026-07-13
---


# Chương trình dịch thuật Wiki

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
- ** Tên tập tin:** kebab- rib (e.g. `llm-wiki-karpathy-pattern.md`)
- **Folders:** Chữ thường, gạch ngang-sepheated (e.g. `Bac-Giang/`)
- **Slugs:** trùng tên tập tin, không có ký tự đặc biệt
- **Tags:** Chữ thường, tối đa 5 trên mỗi nốt

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

### Comment
- **Major (X.0.0):** Làm hỏng thay đổi — cấu trúc, frontmatter trường, quy tắc đặt tên
- **Minor (0.X.0):** Các hội nghị mới thêm vào — tương thích sau
- **Patch (0.0.X):** Sự phân tách, đánh máy — không thay đổi chức năng

### Migration Rules
| Version | Change | Migration Action |
|---------|--------|-----------------|
| Major bump | Đã thêm yêu cầu frontmatter trường | LLM Giá trị mặc định tự thêm |
| Major bump | Renamed folder | LLM Cập nhật mọi liên kết sau |
| Minor bump | trường tùy chọn mới | Không cần phải di cư |
| Patch | Sửa chữa Typo trong các bác sĩ đại hội | Không cần phải di cư |

### Version Tracking
- Schema file này có `version: "1.0.0"` — bump khi có breaking change
- Change log trong section 5 dưới đây
- Khi update schema → LLM scan toàn bộ vault để apply migration

## 3. LLM Operational Rules

### 3.1 Ingest Rules
- **MT** thêm frontmatter trước khi viết bất kỳ ghi chú mới
- **MUST** create ≥1 backlink trong cùng session
- **MUT** Cập nhật hầm-chủ-index. mh t-Kio lưu ý m Whoi
- **MUT** sử dụng đúng loại (những hình thức/sự chú ý)
- **MAX** 2 ghi chú mỗi phiên chạy (tiền tiêu)

### 3.2 Query Rules
- Đọc bảng điều khiển hầm trước tiên cho định vị
- Chỉ sau khi quét chỉ mục, hãy tập trung vào các ghi chú đặc trưng.
- Nguồn Cite trong câu trả lời `[[note-slug]]` liên kết
- Tập tin đáp án tốt như trang i- tơ mới (với frontmatter)

### 3 Lint quy tắc (Kèm quá/Bi tuần)
- Kiểm tra trẻ mồ côi: ghi chú không có đường nội dung và không trong chỉ mục
- Cờ cũ yêu cầu: ghi chú > 30 ngày cũ tham khảo lại dữ liệu nhạy thời gian
- Đề nghị kết nối: xác định cơ hội liên kết chéo
- Báo cáo: Số lượng trẻ mồ côi, số đếm chậm, gợi ý kết nối

## 4. Backlink Requirements

### Mỗi nốt nhạc phải có đường dẫn ngược 1 ngày
- Liên kết tới chú thích tồn tại trong `related:` trường
- Thêm liên kết ngược từ chú thích đã có tới chú thích mới (tin nhắn gốc)
- Tham chiếu chéo trong bộ trưởng-index.md

### Phát hiện trẻ mồ côi Criteria
Một tờ giấy có sẵn nếu:
- Không có liên kết đang tải (`[[note-name]]`) từ bất kỳ lưu ý khác, VÀ
- Không được liệt kê trong bộ trưởng-index.md, AND
- Tạo >7 ngày trước

## 5. Change Log

### v1.0. 0 (2026-06-16) — Ban đầu Schema
- Dựa trên sự thông cảm LLM Comment
- Frontmatter standard defined
- Các hội nghị về Nam diễn ra
- Thiết lập chiến lược phiên bản (semantic)
- Quy tắc di chuyển được định nghĩa

### Planned v1.1.0
- Thêm mẫu trang/ nhận diện
- Chỉ mục đào hầm hạng mục
- Thêm giấy qua đường cho Bảo trì Cổng Hàng Nhật

## 6. References

- Karpally, Andrej."LLM Mẫu của Wiki." GitHub Giist.
- [[vault-architecture]] - Thiết kế toàn bộ hầm
- [[README|Vault — Second Brain Hub]] - Toàn bộ cấu trúc của BA
