---
title: "OpenClaw Windows Operations - Verified 2026-07-13"
slug: "openclaw-windows-operations"
category: knowledge
tags: ["tool/openclaw", "project/ai-agent-engineering", "concept/ai-agent-design", "status/reference"]
status: active
type: reference
created: 2026-07-13
last_updated: 2026-07-13
---

# OpenClaw Windows Operations - Verified 2026-07-13

> [!success] Trạng thái đã kiểm chứng
> OpenClaw `2026.6.11` hoạt động trên gateway loopback; gateway và Telegram health check đạt. Live agent turn đã trả `OPENCLAW_OK` và `OPENCLAW_FINAL_OK`.

## Bộ kiểm tra chuẩn

```powershell
openclaw status --deep
openclaw security audit --deep
openclaw agent --thinking off --json
```

Không kết luận hệ thống đã sửa chỉ từ status nông. Bằng chứng mạnh nhất là deep status, deep security audit và một agent turn thật trên model đang hoạt động.

## Kiến trúc và an toàn hiện tại

- Gateway chỉ nghe loopback `127.0.0.1:18789`.
- Model mặc định lúc kiểm tra: `sonct988/gemma4-26b-a4b-it-q4km-256k:latest`.
- Security audit: `0 critical`, `1 warning`, `2 info`.
- Web/browser tools đang bị tắt cho small-model path, đúng với cấu hình hardening.
- Cảnh báo `gateway.trusted_proxies_missing` chỉ cần xử lý nếu đưa Control UI ra sau reverse proxy; giữ loopback-only thì không mở rộng cấu hình.

## Bài học timeout Ollama

Một sự cố trước đây do process-level `OLLAMA_CONTEXT_LENGTH=262144` làm runtime quá tải và agent timeout. Hạ xuống `32768`, kiểm tra `ollama ps`, rồi chạy live agent turn đã khôi phục luồng. Đây là bài học vận hành, không phải tuyên bố model chỉ hỗ trợ 32K.

## Cron và automation

| Job | Trạng thái 2026-07-13 | Ghi chú |
|---|---|---|
| Vault Daily Cleanup | OK | Chạy script trực tiếp |
| Daily Memory Cleanup | OK | Chạy script trực tiếp |
| Vault Monthly Audit | OK | Không có lỗi hiện tại |
| Vault Git Backup | Skipped | Cần kiểm tra điều kiện skip trước khi coi là lỗi |
| Obsidian Embedding Refresh | Skipped | Cần kiểm tra điều kiện skip trước khi coi là lỗi |
| Vault Weekly Connect | Error | Lỗi lịch sử còn tồn tại; cần điều tra riêng |

Automation xác định nên dùng direct command thay vì `agentTurn` để giảm timeout và token burn. Hai script cốt lõi hiện có:

- `C:\Users\Hung\.openclaw\workspace\vault-daily-check.ps1`
- `C:\Users\Hung\.openclaw\workspace\memory-cleanup.ps1`

Với vault Git, dùng `git -C <vault-path>` để cron không phụ thuộc current directory. Luôn backup config trước sửa và kiểm chứng lại bằng live turn.

## Backlog

- [ ] Điều tra `Vault Weekly Connect` bằng log của lần chạy lỗi gần nhất.
- [ ] Xác nhận hai job `Skipped` là điều kiện mong đợi hay cấu hình thiếu.
- [ ] Chỉ cấu hình trusted proxies khi thực sự có reverse proxy.

## Kết nối

- [[agent-integration-framework]]
- [[openclaw-deep-dive-2026-06-15]] - snapshot cũ, không dùng thay live status
- [[vault-health-bridge]]
- [[Vault-MOC]]

