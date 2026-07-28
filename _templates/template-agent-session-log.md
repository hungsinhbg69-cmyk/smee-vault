---
title: "Bản ghi phiên chạy rực rỡ"
slug: "agent-session-log"
category: meta
tags: [meta, agent, session-log]
status: active
type: framework
created: 2026-06-23
last_updated: 2026-06-23
---

# Comment

> Hermes Theo dõi phiên chạy đặc vụ — ghi chép mọi hành động, thu và quyết định tích hợp két sắt.

## Session Header

```yaml
session_id: YYYY-MM-DD-HHMM
agent: hermes-agent
vault_root: Smee Obsidian/Smee
protocol_version: 2.1
```

## Danh sách kiểm tra trước

- [ ] Đọc `Protocol.md` _Gỡ bỏ
- [ ] Đọc `Vault-Quick-Ref.md` _cần xác định ngữ cảnh miền
- [ ] Đọc lưu ý hoạt động hàng ngày _ kiểm tra trước khi bắt
- [ ] Quét các dự án hoạt động vào `10-Projects/`

## Bản ghi hành động phiên chạy

### Chụp (hiểu biết mới)
- `[HH:MM] capture: "<topic>" → [[slug-name]] (folder/#tags)`

### Kết nối (đã tạo)
- `[HH:MM] connect: [[note-a]] ↕ [[note-b]]` _Trích từ ý niệm/cluster

### Outputs (deliverables)
- `[HH:MM] output: "<artifact type>" → [[target-path]]`

### Decisions
- `[HH:MM] decision: "<rationale>" → moved [[note]] from X to Y`

## Name

1. Phụ thêm mọi hành động vào chú thích hàng ngày hiện tại (02-Daily/YYYY-MM-D.md)
2. Tạo ghi chú nguyên tử để xác nhận sự hiểu biết (được hỗ trợ từ việc thu phiên chạy)
3. Liên kết các ghi chú mới với chức năng MOCs/insights
4. Nhấn để thêm chú thích...
