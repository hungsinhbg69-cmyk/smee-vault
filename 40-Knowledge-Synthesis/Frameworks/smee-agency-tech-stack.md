---
title: "smee-agency-tech-stack"
slug: "smee-agency-tech-stack"
category: frameworks
tags: [obsidian-cleanup, auto-added]
status: draft
type: framework
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: "Smee Agency — Tech Stack & Automation"
slug: "smee-agency-tech-stack"
category: technical
tags: [smee, tech-stack, automation, openclaw, ollama]
status: active
type: reference-note
created: 2026-06-15
last_updated: 2026-06-15
---

# 🤖 Smee Agency Tech Stack & Automation

> [!SUMMARY] Hệ thống AI automation của Smee Agency Bắc Giang: OpenClaw orchestrator + Ollama local LLM + Facebook Graph API + Obsidian vault. Khác biệt so với agency truyền thống: tự động hóa nội dung, dreaming cron jobs, community pipeline.

## 1. CORE INFRASTRUCTURE

| Component | Version/Config | Vai trò |
|-----------|---------------|---------|
| **OpenClaw** | 2026.6.5 | AI Agent orchestrator (main controller) |
| **Ollama** | 0.30.7 | Local LLM inference |
| **Model** | mixi/fredrezones55-qwen36-aggressive-stable:latest | Primary reasoning model |
| **Context** | num_ctx=262144, flash attention enabled | VRAM optimization |
| **Ollama Env** | NUM_PARALLEL=2, MAX_QUEUE=256, KV_CACHE=q8_0 | Performance tuning |

## 2. FACEBOOK ECOSYSTEM

### Page 1 — Smee Sale & Marketing
- **Page ID:** `1094674520391475`
- **App ID:** `1640859240534684`
### Page 2 — Bệnh Viện Mắt Hà Nội - Bắc Ninh
- **Page ID:** `997717610098937`
- **App ID:** `1963488660946232`
- **Token:** Hardcoded, verified OK (never-expire)
- **Permissions:** read_insights, pages_manage_posts, pages_manage_engagement...

### FB Safety Rules
| Block Rate | Level | Action |
|-----------|-------|--------|
| 1-2% | Normal | Tiếp tục bình thường |
| 3-5% | Danger | Giảm tần suất messages |
| 6-8%+ | Blocked | Chỉ 1 standard message/24h |

**Lách từ khóa OCR:** "Trị dứt điểm" → "Hỗ trợ cải thiện"
**Spin content:** 3-5 variants để tránh duplicate detection

## 3. COMMUNITY PIPELINE

```
Batch Collect Comments → Filter (lead intent) → Auto Reply → Profile Lookup → Daily Log
```

- **Max:** 3 turns/batch, 50K tokens/session
- **Verify state** after each action
- **Comment response format:** "Dạ, em chào anh/chị ạ. [Nội dung]. Anh/chị cứ nhắn em nếu cần hỗ trợ thêm ạ. Em cảm ơn anh/chị nhiều."

## 4. CRON JOBS

| Job | Schedule | Session | Status |
|-----|----------|---------|--------|
| Memory Dreaming | `0 3 * * *` | isolated, delivery=none | ✅ Active |
| Daily Vault Maintenance | `0 6 * * *` tz=Asia/Ho_Chi_Minh | isolated, delivery=none | ⚠️ ERRORS (4 consecutive timeouts at 120s) |

**Fix pending:** Tăng timeoutSeconds hoặc split thành smaller tasks.

## 5. OBSIDIAN VAULT (Second Brain)

- **Path:** `C:\Users\Hung\Desktop\Smee Obsidian\Smee`
- **Structure:** PARA + Zettelkasten hybrid
- **Plugins:** 40 community + 21 core = 61 total
- **Smart Connections:** Local embedding (nomic-embed-text-v2-moe via Ollama)
- **Template system:** 7 templates
- **Capture rules:** Max 2 notes/session, every new note MUST have ≥1 backlink same day

## 6. MEMORY SYSTEM

- **Backend:** builtin vector search
- **Sources:** `memory`, `sessions`
- **Provider:** node-llama-cpp (local) — ⚠️ currently unavailable (needs rebuild)
- **Dreaming:** enabled via memory-core plugin

---

## 🔗 Backlinks
- [[smee-agency-bac-giang-deep-dive]]
- [[Obsidian-Vault-Setup]]

---

*Smee 🦞 | 2026-06-15*
