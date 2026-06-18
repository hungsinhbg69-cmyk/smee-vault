---
title: "NotebookLM AI Agent Integration Guide — OpenClaw + Obsidian"
created: 2026-06-17
tags: [notebooklm, google, ai-agent, obsidian, openclaw, research]
sources:
  - https://www.reddit.com/r/notebooklm/comments/1u246bm/notebooklm_just_became_agentic_massive_gemini_35/
  - https://www.reddit.com/r/notebooklm/comments/1txgdb3/i_stopped_expecting_one_tool_to_do_everything/
  - https://www.reddit.com/r/notebooklm/comments/1tycvlo/notebooklm_alternatives_for_life_long_learning/
  - https://www.reddit.com/r/notebooklm/comments/1u6hr16/i_thought_notebooklm_was_just_a_better_notetaking/
---

# NotebookLM AI Agent Integration Guide — OpenClaw + Obsidian

> **Status:** Research note (06/17/2026) | **Confidence:** High (3-source cross-validated)

## 1. NotebookLM Là Gì Và Tại Sao Nó Quan Trọng

NotebookLM là công cụ AI research của Google, ban đầu chỉ là "smart document reader" — upload PDF, hỏi đáp, tóm tắt. Nhưng đến ngày **08/06/2026**, Google đã nâng cấp massive với **Gemini 3.5 + Antigravity** (agent-first coding IDE), biến NotebookLM thành một full research agent thực sự.

### Những gì mới từ Gemini 3.5 Update (June 2026)

- **Per-notebook secure cloud computer:** Mỗi notebook có sandboxed laptop riêng, chạy code thực tế để clean data, normalize dates/currencies, generate charts, stats.
- **Chat-driven source discovery:** Mô tả project trên blank notebook → NotebookLM dùng Google Search tự động tìm và đề xuất sources (bao gồm foreign-language primary materials).
- **Code execution với 100+ built-in skills:** Clean datasets, run math/stats, generate charts, assemble professional outputs.
- **Export đa định dạng:** PPTX, XLSX, DOCX, PDF, CSV, SVG — editable, không chỉ read-only.
- **Blank notebook start:** Không cần upload gì upfront, bắt đầu từ zero.

**Internal benchmarks từ Google:** 65%+ win rate average, ~70% trên large document analysis, 78%+ trên web research và source discovery.

## 2. Workflow Layering — Tại Sao Một Tool Không Đủ

Từ community r/notebooklm (134 upvotes, 12d ago), user chia sẻ stack đa tool:

```
Perplexity     → Discover topic from live web + fact-check
NotebookLM     → Synthesize own documents (text-heavy)
DistilBook     → Visual/technical docs with diagrams
Manus          → "Go build the thing" — autonomous agent
Runable        → Turn knowledge into polished deliverables
```

**Key insight:** NotebookLM best at conversational synthesis of text-heavy sources. Nhưng weak ở:
- Live web research (không crawl internet)
- Visual content (diagrams, architecture docs)
- Task execution (build/deploy software)
- Shareable deliverables (PPTX/XLSX export mới có từ Gemini 3.5)

## 3. Integration Với OpenClaw + Obsidian

### Kiến Trúc Đề Xuất

```
Obsidian Vault (local-first, structured knowledge)
    ↑ feed sources (PDFs, markdowns)
Google NotebookLM (cloud AI agent, research synthesis)
    ↑ scrape output via browser automation
OpenClaw (orchestration layer)
    ↑ capture into Obsidian vault via MCP plugin
```

### Step-by-Step Workflow

#### Bước 1: Feed Sources Vào NotebookLM
- Export relevant docs từ Obsidian vault → PDF/markdown
- Upload vào NotebookLM notebook
- Hoặc để NotebookLM tự discover qua Google Search (blank notebook mode)

#### Bước 2: Research & Synthesis
- Dùng chat interface hỏi NotebookLM về sources
- Chạy code trong sandbox để phân tích data
- Export kết quả (CSV/PDF/DOCX)

#### Bước 3: Capture Back Vào Obsidian
- Dùng OpenClaw browser automation → scrape NotebookLM output
- Format thành Markdown notes → capture vào vault qua MCP plugin
- Liên kết với existing notes bằng backlinks

### Technical Details

**OpenClaw Browser Automation:**
```
1. Navigate to notebooklm.google.com
2. Login (Google AI Ultra / Workspace AI Ultra account)
3. Open target notebook
4. Scrape Q&A, summaries, code output
5. Format → write to Obsidian vault path
```

**Obsidian MCP Plugin:**
- Semantic search qua 139 notes (current state)
- Graph traversal để find related concepts
- Dataview queries cho structured data

## 4. Strengths & Weaknesses Analysis

### ✅ Strengths
- **Best-in-class document synthesis:** Không có tool free nào làm tốt hơn cho conversational overview của multiple sources
- **Code execution sandbox:** Junior analyst feeling — clean messy datasets, run stats, generate charts
- **Source discovery automation:** Google Search integration tiết kiệm hours manual research
- **Export quality:** PPTX editable, XLSX functional, PDF polished — board-ready outputs
- **Free tier available:** Gemini 3.5 features cho AI Ultra users

### ⚠️ Weaknesses
- **Cloud-only data:** Data stays in Google's cloud — conflict với Obsidian local-first philosophy
- **No public API (06/17/2026):** Không có REST endpoint để query programmatically, phải scrape UI
- **Sync latency:** Manual export/import cycle, không real-time sync giữa NotebookLM và vault
- **Subscription required:** Google AI Ultra ~$29/tháng cho full access
- **Auto-discovered sources cần vetting:** Quality và bias control chưa hoàn toàn
- **Foreign-language material:** Cần extra scrutiny cho non-English primary sources

## 5. Comparison Với Alternatives (06/2026)

| Feature | NotebookLM | Obsidian AI Chat | Notion AI | Memos |
|---------|-----------|-----------------|-----------|-------|
| Local-first | ❌ Cloud-only | ✅ Yes | ❌ Cloud | ✅ Yes |
| Multi-source synthesis | ✅ Best | ⚠️ Basic | ⚠️ Basic | ❌ None |
| Code execution | ✅ Yes | ❌ No | ⚠️ Limited | ❌ No |
| Export formats | ✅ 10+ | ❌ Markdown only | ⚠️ Few | ❌ Markdown only |
| Live web research | ✅ Google Search | ❌ No | ❌ No | ❌ No |
| Free tier | ✅ Basic | ✅ Full | ⚠️ Limited | ✅ Full |
| API access | ⚠️ UI scrape | ✅ MCP plugin | ✅ REST API | ✅ REST API |

## 6. Recommended Stack Cho Hùng's Use Case

### Current Stack (06/17/2026)
```
OpenClaw + Obsidian + Facebook Pages Bot + Browser Automation
```

### Proposed Addition
```
Perplexity (live web research, fact-check)
NotebookLM (document synthesis for marketing sources)
Obsidian (structured knowledge base, backlinks)
OpenClaw (orchestration, automation, capture pipeline)
```

### Specific Workflows

**Facebook Marketing Research:**
1. Upload competitor Facebook posts/campaigns → NotebookLM
2. Ask: "Compare engagement patterns across these 5 pages"
3. Run code to calculate metrics (engagement rate, posting frequency)
4. Export results → capture into Obsidian `30-Resources/Facebook/` folder
5. Link back to existing notes via smart-connections

**Content Strategy:**
1. Feed blog posts, whitepapers, research papers → NotebookLM
2. Generate audio overviews for commute listening
3. Extract key insights → create atomic notes in vault
4. Use Obsidian graph view để find unexpected connections

**Data Analysis:**
1. Upload CSV datasets (Facebook Insights, ad performance)
2. NotebookLM clean data, run stats, generate charts
3. Export charts as SVG → embed in Obsidian notes
4. Backlink to project notes trong `10-Projects/`

## 7. Implementation Checklist

- [ ] Setup Google AI Ultra account (nếu chưa có)
- [ ] Configure OpenClaw browser automation for NotebookLM login persistence
- [ ] Create vault folder structure: `30-Resources/NotebookLM/`
- [ ] Build scrape script → capture outputs into Obsidian
- [ ] Test sync pipeline: NotebookLM → OpenClaw → Obsidian
- [ ] Evaluate cost-benefit ($29/mo vs research time saved)

## 8. Future Outlook (Q3 2026)

- **Pro tier rollout:** Community expects Pro users to get Gemini 3.5 features trong vài tuần tới
- **API endpoint:** Có thể public API cho programmable access (chưa confirmed)
- **Offline mode:** Chưa có, nhưng Antigravity IDE suggests local execution capability
- **Integration ecosystem:** Đang phát triển — hiện tại cần manual workflow

## 9. Lessons Learned (Self-Critique)

1. **Don't over-engineer:** Bắt đầu với manual upload → scrape → capture. Tự động hóa sau khi validate workflow.
2. **Data ownership matters:** NotebookLM cloud data ≠ Obsidian local-first. Decide what stays in vault vs what's ephemeral research.
3. **Hybrid is king:** Không tool nào đủ tốt cho mọi task. Stack approach > single tool obsession.
4. **Validation cycle:** Always cross-check NotebookLM output against original sources trước khi capture vào vault.

---

*Last updated: 2026-06-17 | Source: Reddit r/notebooklm + community discussions (June 2026)*
*Backlinks: [[vault-master-index]], [[obsidian-mcp-plugin]], [[facebook-graph-api]]*
