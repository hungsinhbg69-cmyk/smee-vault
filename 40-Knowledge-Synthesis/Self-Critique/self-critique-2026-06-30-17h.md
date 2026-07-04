---
title: "Self-Critique — 2026-06-30 17h00"
slug: "self-critique-2026-06-30-17h"
category: knowledge-synthesis
type: insights
status: draft
created: 2026-06-30 17:00
tags: [self-critique, self-improvement, daily-review]
---

## ❌ Lỗi & Vấp phải

> Note: Self-critique ban đầu (từ session 9:54 AM) đã ghi 6 lỗi từ buổi sáng. Phần này bổ sung thêm lỗi từ 3 session chiều.

### Buổi Sáng (đã ghi trước đó — giữ nguyên tham chiếu)
| Session | Lỗi | Nguyên nhân gốc (5 Whys) | Bài học |
|---------|-----|-------------------------|--------|
| **09:54 Morning Setup** | `skill_view` fail vì skill không tồn tại | Blind assumption về skills available → Didn't call skills_list first | Call skills_list/verify before relying on specific skill names |
| **09:54 Morning Setup** | `read_file` paths hardcoded, 2 file không tồn tại | Không dùng search_files để discover trước | discover → then act pattern |
| **10:51 Cron Ritual** | `read_file` tool không tồn tại trong cron session | Cron chỉ có enabled_toolsets=["terminal"] | Luôn check available tools cho cron context |

### Buổi Chiều — MỚI (từ 2 sessions chiều)

| Session | Lỗi | Nguyên nhân gốc (5 Whys) | Bài học |
|---------|-----|-------------------------|--------|
| **11:11 AM — HN + Ollama** (93 msgs, session `20260630_111140`) | Browser navigate click link → page empty → assistant trả về **empty response** thay vì xử lý kết quả tool output | Why? Không kiểm tra browser response có nội dung hay không trước khi return → Why? Không có pattern inspect-page-then-act trong browser workflow → Root: Assumed browser_click success = immediate content available, didn't re-navigate or snapshot | **Browser click pattern**: Sau click, luôn verify bằng browser_snapshot hoặc browser_navigate lại URL — đừng return empty chỉ vì chưa read tool output |
| **11:11 AM — Ollama pull** (19GB model) | Terminal timeout sau 180s khi download manifest — quá hạn cho model lớn | Why? Timeout=180 không đủ cho 19GB → Root: Không scale timeout theo kích thước file | **Large file rule**: ollama pull >10GB → timeout ≥300s; dùng process(poll) để check progress |
| **11:11 AM — Model comparison** | Lỗi `missing tensor blk.64.attn_norm.weight` khi chạy Qwen3.6-27B dense trên GPU, nhưng không test Q4_K_M version trước → session kết thúc mà không có benchmark hoàn thành | Why? Assumed Q5_KM sẽ load được → Why? Không check model tags (available quantizations) trước → Root: Jump to test without verifying model availability/compatibility | **Test-before-run pattern**: ollama list/api/tags → verify available quantizations → test smallest first before benchmark |
| **11:11 AM — todo tool** | Passed `todos` as string `"[{...}]"` instead of JSON object → `{"error": "must be a list of objects, got unparseable string"}` | Why? Used escaped string notation instead of proper JSON array → Root: Không format tool args đúng syntax cho tools cần structured data | Luôn build toolargs là dict/JSON object, không string — test với `json_parse` nếu不确定 |
| **02:04 PM — Hermes Maintenance** (30 msgs, session `20260630_140413`) | Typo `hermis config migrate` thay vì `hermes config migrate` → failed, phải retry | Why? Không double-check command spelling khi dùng CLI tool → Root: Fast typing without verification on first run cho command mới | **CLI safety**: Trước khi chạy terminal command dài, read lại command string để verify spelling — đặc biệt với commands có 3+ words |
| **02:04 PM — Memory path** | `cat "$HOME/.hermes/...` fail vì $HOME resolve sai trên Windows → `/c/Users/Hung/.hermes/` không tồn tại | Why? Dùng `$HOME` mà không verify trên Windows host → Root: Assumed POSIX shell variable works like Linux | **Windows env vars**: `$HOME` thường về `/home/<user>` hoặc undefined — prefer absolute paths hoặc `%USERPROFILE%` |

## 🔄 Các Pattern lặp lại

### Pattern 1: Retry cùng parameter thay vì đổi strategy (x3 sessions)
- `skill_view(file_path=...)` fail 3 lần → mới switch tool
- Browser click empty page → re-navigate homepage thay vì check cụ thể
- Todo với string args → nhận error rồi mới parse đúng
- **Root cause**: Không đọc error message từ tool response, chỉ repeat same call
- **Fix pattern**: Sau 1 failure → inspect output → change approach (add param / switch tool / fix format)

### Pattern 2: Giả định tool/skills tồn tại (x2 sessions)
- Morning setup: `skill_view("morning-ritual")` fail vì skill không tồn tại
- Cron session: `read_file` fail vì chỉ có terminal toolset
- **Root cause**: Default to known tool names without checking availability first
- **Fix pattern**: discover → then act; `skills_list`/`cronjob list` trước khi rely

### Pattern 3: Không verify CLI command spelling (1 session mới)
- Typo `hermis` vs `hermes` — wasted a terminal round-trip
- **Root cause**: Fast typing + no pre-flight check on long commands
- **Fix pattern**: Re-read command string before executing 3+ word commands

### Pattern 4: Không kiểm tra available resources trước khi dùng (1 session mới)
- Ollama pull 19GB với timeout=180s → quá ngắn
- Model comparison không check tags/quantizations trước → test bị hỏng tensor
- **Root cause**: Chọn giá trị default mà không scale theo context
- **Fix pattern**: Scale resource params (timeout, memory) theo input size

## ✅ Cái gì HIỆU QUẢ

| Task | Approach | Tại sao hiệu quả? |
|------|----------|------------------|
| Create cron job Morning Ritual repeat=365 | Dùng cronjob action=create với repeat count | Tự động chạy hàng năm, không cần người vận hành |
| Test script before deploy cron | Chạy execute_code test → phát hiện duplicate logic | Validate runtime behavior before automating |
| Session maintenance: `hermes doctor` + `config migrate` + create skill | Sequential health check workflow | Phát hiện 10+ warnings, fix config v30→v32 trong 1 session |
| Ollama pull thành công (dấu hiệu terminal output progress) | Terminal background tracking cho large download | Model đã available sau pull, có thể dùng `api/tags` verify |

## 🚀 Best Practices phát hiện hôm nay

1. **Browser post-click verification**: Sau `browser_click`, luôn gọi `browser_snapshot` để confirm page state thay vì assume success
2. **Ollama pre-test protocol**: Trước benchmark → `ollama list` + `curl :11434/api/tags` → select smallest quantization cho test first
3. **Tool parameter format discipline**: Tools nhận structured data → pass dict/object, không escaped string
4. **CLI command double-check**: Commands 3+ words/flags → re-read string before terminal execute

## 🧠 Lessons cần ghi persistent memory

| Lesson | Đã lưu? |
|--------|---------|
| write_file cho scripts >40 lines | ✅ |
| Windows → strip \r | ✅ |
| validate với 3 sample reads sau batch fix | ✅ |
| discover-then-exploit workflow | ✅ |
| Cron sessions: no read_file, use terminal | ✅ |
| skill_view luôn cần name param + check skills_list trước | ✅ (cũng có trong session này) |
| **Browser post-click → verify với snapshot** | ❌ MỚI — cần lưu |
| **Ollama pull >10GB → timeout ≥300s + process(poll)** | ❌ MỚI — cần lưu |
| **Check ollama api/tags trước khi benchmark model** | ❌ MỚI — cần lưu |
| **CLI command spelling: re-read trước execute 3+ word commands** | ❌ MỚI — cần lưu |

---
*Self-Critique Update by Hermes Agent — 17h00 Daily Review, 2026-06-30*
*Total sessions today: 4 (morning setup + morning cron + HN/ollama comparison + maintenance)*
*Errors found today: 5 new + 6 from morning = 11 total errors across sessions*
*Top lessons: (1) Post-tool-call verification → (2) Scale resources to input size → (3) Check availability before use → (4) Double-check CLI spelling*
