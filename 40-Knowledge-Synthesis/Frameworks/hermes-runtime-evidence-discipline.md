---
title: "Hermes Chạy và sửa chữa bằng chứng - đã được xác nhận 2026-07-13"
slug: "hermes-runtime-evidence-discipline"
category: knowledge
tags: ["project/ai-agent-engineering", "concept/ai-agent-design", "type/atomic-note", "status/reference"]
status: active
type: reference
created: 2026-07-13
last_updated: 2026-07-13
---

# Hermes Chạy và sửa đổi chứng cứ - đã biến 2026-07-13

## Trạng thái runtime đã kiểm chứng

- Hermes Agent `v0.18.2 (2026.7.7.2)`, cài bằng Git, có `+1 carried commit`.
- Python `3.11.15`; gateway đang chạy dưới manual process.
- Model hiện tại: `sonct988/gemma4-26b-a4b-it-q4km-256k:latest`; provider: `ollama-launch`.
- Built-in memory hoạt động; trạng thái cho thấy 149 sessions trong database và 1 session active tại thời điểm kiểm tra.
- Không sao chép API key, token hoặc credential từ cấu hình Hermes vào vault.

## Drift cần xử lý

`hermes doctor` báo một lỗi cấu hình chính: `model.default` dùng vendor/model slug trong khi provider là `ollama-launch`. Cần xác nhận format model mà provider local yêu cầu trước khi sửa.

Hai cron job đều để `active` nhưng lần chạy gần nhất bị skip để tránh phát sinh chi phí ngoài ý muốn sau khi global model đổi:

1. `Obsidian Daily Morning Ritual - Every Day 8:30`.
2. `Tổng kết & Tự phê bình buổi chiều` lúc 17:00.

Muốn chạy lại phải pin rõ provider/model mong muốn cho từng job; không nên bỏ cơ chế chống drift.

`doctor` còn ghi nhận `agent-browser` là broken symlink và Gemini connectivity trả HTTP 400. Các auth/provider không dùng không được xem là lỗi bắt buộc.

## Security backlog

`hermes security audit` quét 156 components và tìm 29 findings. Nhóm HIGH cần ưu tiên đánh giá tương thích trước khi nâng cấp:

| Package hiện tại | Finding HIGH | Bản vá tối thiểu được audit đề xuất |
|---|---|---|
| `cryptography 46.0.7` | OpenSSL trong wheel có lỗ hổng | `48.0.1` |
| `python-multipart 0.0.27` | Querystring parsing có thể gây CPU DoS | `0.0.30` |
| `starlette 1.0.1` | Form limits bị bỏ qua | `1.3.1` |
| `starlette 1.0.1` | SSRF/NTLM credential theft qua UNC path trên Windows | `1.1.0` |

> [!warning] Chưa remediation
> Phiên này chỉ audit và ghi nhận. Không nâng dependency hàng loạt khi chưa backup và test Hermes gateway, cron, browser và plugin compatibility.

## Tài liệu Hermes đang stale

Các file persona/config cũ không được dùng làm nguồn trạng thái live:

- `USER.md` còn ghi OpenClaw `2026.6.1`.
- `TOOLS.md` còn ghi OpenClaw `2026.6.5`, model/context và cron từ snapshot cũ.
- `memory/openclaw-dead-memory.md` ghi lần cập nhật cuối `2026-06-16` và chứa các quyết định đã trôi trạng thái.

Root `AGENTS.md` của vault là nguồn luật vận hành; `SOUL.md` chỉ giữ personality. Trạng thái hệ thống phải lấy từ command live và bằng chứng mới nhất.

## Evidence discipline

Bài huấn luyện ngày 2026-07-13 cho thấy Hermes vẫn bịa timestamp, hành động đã chạy và dữ kiện không có trong đề. Điểm các lần là `59 → 43 → 38`, nên chưa được mở tình huống 2.

Quy tắc bắt buộc cho mọi bàn giao:

- Tách `Đã quan sát` / `Suy luận` / `Chưa biết`.
- Không dùng timestamp hoặc tương quan làm bằng chứng nhân quả.
- Không viết hành động ở thì đã thực hiện nếu chưa có tool output.
- Mỗi claim quan trọng phải trỏ đến log, command output, file hoặc nguồn cụ thể.

## Backlog ưu tiên

- [ ] Chốt format model slug đúng cho `ollama-launch` và kiểm tra bằng một turn thật.
- [ ] Pin provider/model cho hai cron job sau khi xác nhận model mục tiêu.
- [ ] Lập kế hoạch nâng các dependency HIGH có backup và regression test.
- [ ] Sửa hoặc gỡ `agent-browser` symlink hỏng.
- [ ] Làm sạch tài liệu Hermes stale; không lưu credential trong Markdown.

## Kết nối

- [[OpenClaw và Hermes - 3 tình huống khó - 2026-07-13]]
- [[agent-integration-framework]]
- [[openclaw-windows-operations]]
- [[Vault-MOC]]

