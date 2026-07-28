---
title: LLM Wiki — Kiến trúc 3-Layer
slug: llm-wiki-architecture
category: knowledge
tags:
- llm
- wiki
- architecture
- karpathy
- rag
status: active
type: concept
created: 2026-06-16
last_updated: '2026-07-14'
source: GitHub Gist - Karpathy LLM Wiki Pattern
related:
- llm-wiki-karpathy-pattern
- llm-wiki-operations
- llm-wiki-critique
---

# LLM Wiki — Kiến trúc 3-Layer (Karpacy)

## Overview

Andrej Karpathy đề xuất mô hình **3-layer knowledge base** thay vì RAG truyền thống.

## Lớp 1: Nguồn thô

- **Định nghĩa:** Collection của source documents (articles, papers, images, data files)
- **Tính chất:** Immutable — LLM đọc không ghi đè
- **Owner:** Human curates và drop sources vào collection
- **Purpost:** Nguồn tin lẽ thật độc nhất, kiểm toán cho m hết các nội dung của hệ thống định vị

## Lớp 2: Wiki

- **Định nghĩa:** Directory của LLM-generated markdown files
- ** Những kiểu độc đáo:** tổng hợp, trang thực thể, trang khái niệm, so sánh, tổng hợp, tổng hợp
- **Tính chất:** Mutable — LLM tạo pages, update cross-refs, maintain consistency
- **Owner:** LLM hoàn toàn sở hữu operational layer này

**Key difference với RAG:** Wiki là persistent, compounding artifact. Mỗi source mới làm wiki giàu hơn, không phải re-retrieve từ đầu mỗi query.

## Lớp 3: Sơ đồ

- **Định nghĩa:** Document (CLAUDE.md / AGENTS.md) — config file cho LLM
- **Content:** Cấu trúc thư mục, định dạng trang, dòng làm việc, đặt tên
- **Owner:** Con người + LLM Đồng-nởi qua thời gian
- **Purpose:** Biến LLM từ generic chatbot thành disciplined wiki maintainer

## So sánh với RAG truyền thống

| Aspect | RAG | LLM Wiki Pattern |
|--------|-----|-----------------|
| Retrieval | Tương tự véc- tơ trên mỗi truy vấn | khoan phụ lục- đầu tiên- xuống |
| Accumulation | Đang nhúng cập nhật (vô hạn) | Sự kết hợp giữa Semantic (hoạt động) |
| Maintenance | None needed | LLM automated |
| Synthesis | Thu hồi mỗi truy vấn | Đã soạn thảo + giữ hiện tại |
| Cross-refs | None automatic | Maintained by LLM |

## Critical Analysis

### Strengths
- Thực hiện đơn giản (markdown tập tin + git)
- Không có phụ thuộc véc- tơ DB ở mức vừa phải
- Kiến thức được hợp nhất theo thời gian
- Human readable và editable (không black-box)

### Weaknesses
- Chỉ mục Giảm thiểu khi _500 trang (>50K hiệu)
- No structured ontology — links là text-based, không property-defined
- Schema drift risk — co-evolution có thể dẫn đến inconsistency
- Nuốt ăn trên đầu — 10-15 tập tin mỗi nguồn = tổng hợp chuyển đổi chi phí

## Ứng dụng vào Cổng Smee

| Karpathy Layer | Smee Path |
|---------------|-----------|
| Raw sources | `30-Resources/` |
| Wiki | `40-Knowledge-Synthesis/` |
| Schema | AGENTS.md + `_templates/` |

---

*See also: [[llm-wiki-karpathy-pattern]], [[llm-wiki-operations]], [[llm-wiki-critique]]*
