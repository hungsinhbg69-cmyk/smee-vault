---
title: Cơ quan kỹ thuật xếp chồng và tự động
slug: smee-agency-tech-stack
category: knowledge
tags:
- smee
- tech-stack
- automation
- openclaw
- ollama
status: active
type: reference-note
created: 2026-06-15
last_updated: '2026-07-14'
---

# Comment

> [!SUMMARY] Hệ thống AI automation của Smee Agency Bắc Giang: OpenClaw orchestrator + Ollama local LLM + Facebook Graph API + Obsidian vault. Khác biệt so với agency truyền thống: tự động hóa nội dung, dreaming cron jobs, community pipeline.

## 1. CORE INFRASTRUCTURE

| Component | Version/Config | Vai trò |
|-----------|---------------|---------|
| **OpenClaw** | 2026.6.5 | Trình soạn nhạc đặc vụ Alci (điều khiển phần cứng) |
| **Ollama** | 0.30.7 | Local LLM inference |
| **Model** | mixi/fredrezones55-qwen36-aggressive-stable:latest | Primary reasoning model |
| **Context** | Num_ctx=262144, đã bật khả năng chú ý nhanh | VRAM optimization |
| **Ollama Env** | NUM_PARALLEL=2, MAX_QUEUE=256, KV_CACHE=q8_0 | Performance tuning |

## 2. FACEBOOK ECOSYSTEM

### Page 1 — Smee Sale & Marketing
- **Page ID:** `1094674520391475`
- **App ID:** `1640859240534684`
### Page 2 — Bệnh Viện Mắt Hà Nội - Bắc Ninh
- **Page ID:** `997717610098937`
- **App ID:** `1963488660946232`
- **Tken:** Hard coded, xác nhận OK (không bao giờ-pearre)
- **Quyền:** read_insights, pages_manage_posts, pages_manage_engagement...

### Các quy tắc an toàn của FB
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

- **Max:** 3 lần rẽ/batch, 50K huy hiệu/sessition
- **Verify State** Sau mỗi hành động
- **Comment response format:** "Dạ, em chào anh/chị ạ. [Nội dung]. Anh/chị cứ nhắn em nếu cần hỗ trợ thêm ạ. Em cảm ơn anh/chị nhiều."

## 4. CRON JOBS

| Job | Schedule | Session | Status |
|-----|----------|---------|--------|
| Memory Dreaming | `0 3 * * *` | cô lập, giao=không | ✅ Active |
| Daily Vault Maintenance | `0 6 * * *` tz=Asia/Ho_Chi_Minh | isolated, delivery=none | ⚠️ ERRORS (4 consecutive timeouts at 120s) |

**Fix pending:** Tăng timeoutSeconds hoặc split thành smaller tasks.

## 5 phút. OBSIDIAN VAULT (N óc băng)

- **Path:** `C:\Users\Hung\Desktop\Smee Obsidian\Smee`
- **Structure:** PARA + Zettelkasten hybrid
- **Plugins:** 40 cộng đồng + 21 lõi = 61 tổng cộng
- **Smart Connections:** Sự nhúng vùng (không phải là tập tin- nền-v2-moe qua Ollama)
- **Các hệ thống bảng màu:** 7 mẫu
- ** Quy tắc khai thác:** Max 2 ghi chú/sessition, mỗi nốt nhạc mới phải có ≥1 vòng quay cùng ngày

## 6. MEMORY SYSTEM

- **Lbaend:** Tìm kiếm véc tơ đã xây dựng
- **Sources:** `memory`, `sessions`
- **Nhà cung cấp:** node-llama-cpp (cục bộ) — ⚠️ hiện không khả dụng (cần dựng lại)
- **Dreaming:** được bật qua bộ nhớ-cure plugin

---

## 🔗 Backlinks
- [[smee-agency-bac-giang-deep-dive]]
- [[Obsidian-Vault-Setup]]

---

*Smee 🦞 | 2026-06-15*
