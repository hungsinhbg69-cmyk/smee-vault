---
title: "OpenClaw Deep Dive — Chuyên Sâu Toàn Diện"
slug: "openclaw-deep-dive-2026-06-15"
category: archive
tags: [vault-maintenance]
status: archived
type: reference
created: 2026-06-24
last_updated: 2026-06-24
---


# OpenClaw Deep Dive — Chuyên Sâu Toàn Diện

**Ngày:** 2026-06-15  
**Tài liệu nghiên cứu:** Docs chính thức, GitHub source, Reddit, DEV.to, Hacker News, community blogs  
**Tổng số từ:** ~3200+ từ

---

## Mục Lục

1. [Overview](#1-overview)
2. [Architecture](#2-architecture)
3. [Core Features](#3-core-features)
   - 3.1 Memory System
   - 3.2 Cron & Scheduling
   - 3.3 Skills & Plugin System
   - 3. 4 Tác vụ phụ và tác vụ nền
   - 3.5 Browser Automation
   - 3.6 Canvas (A2UI)
   - 3. 7 nút (iOS/Andero/macOS)
   - 3.8 MCP Integration
4. [Config Deep Dive](#4-config-deep-dive)
5. [Best Practices](#5-best-practices)
6. [Gotchas & Limitations](#6-gotchas--limitations)
7. [Comparison with Alternatives](#7-comparison-with-alternatives)

---

## 1. Overview

OpenClaw là một **self-hosted AI agent gateway** mã nguồn mở (MIT license), được tạo bởi Peter Steinberger và cộng đồng. Nó cho phép chạy một AI assistant cá nhân trên thiết bị của bạn, kết nối với hàng chục messaging channels (WhatsApp, Telegram, Discord, Slack, Signal, iMessage, Microsoft Teams, Zalo, v.v.) thông qua một Gateway duy nhất.

### Đặc điểm nổi bật
- **Self-hosted**: Chạy trên hardware của bạn, dữ liệu ở lại local
- **Multi-channel**: Một Gateway phục vụ nhiều channels đồng thời
- **Agent-native**: Built cho coding agents với tool use, sessions, memory, multi-agent routing
- ** Nguồn mở**: bằng lái MIT, định hướng cộng đồng (379K+ GitHub Sao)
- **Runtime**: Node 24 (recommended) hoặc Node 22.19+

### Kiến trúc tổng quan
```
[Chat apps + plugins] → [Gateway (WebSocket)] → [OpenClaw agent]
                                         ↓
                              [CLI / Web Control UI / macOS app / Mobile nodes]
```

Gateway là **single source of truth** cho sessions, routing, và channel connections. Tất cả clients (CLI, web UI, macOS app, mobile nodes) kết nối qua WebSocket trên cổng 18789 (mặc định).

### Cài đặt nhanh
```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
openclaw dashboard  # Mở browser Control UI
```

---

## 2. Architecture

### Gateway (Daemon)
- Là một process duy nhất chạy trên mỗi host
- Duy trì kết nối đến nhà cung cấp (Những gì App by Baileys, Telegram qua grammY, v.v.)
- Exposes typed WebSocket API với requests, responses, và server-push events
- Kiểm tra các khung đang tiến tới chống lại JSON Schema
- Emits events: `agent`, `chat`, `presence`, `health`, `heartbeat`, `cron`

### WebSocket Protocol
- Transport: WebSocket, text frames với JSON payloads
- First frame **phải** là `connect` — non-JSON hoặc non-connect frame → hard close
- Sau handshake:
  - Requests: `{type:"req", id, method, params}` → `{type:"res", id, ok, payload|error}`
  - Events: `{type:"event", event, payload, seq?, stateVersion?}`
- Shared-secret auth dùng `connect.params.auth.token` hoặc `connect.params.auth.password`
- Idempotency keys cho side-effecting methods (`send`, `agent`) để retry an toàn

### Trust Model
- **Personal assistant model**: Một trusted operator boundary per gateway
- KHÔNG phải hostile multi-tenant security boundary
- Nếu cần adversarial-user isolation → split trust boundaries (separate gateway + credentials)
- `sessionKey` là routing key, không phải auth token
- Gateway và node trong cùng một operator trust domain

### Nhận diện tín nhiệm Node
| Boundary | Ý nghĩa | Common misread |
|----------|---------|----------------|
| `gateway.auth` | Xác nhận người gọi tới cổng ADIs | "Cần per-message signatures" |
| `sessionKey` | Đang khởi động phím cho ngữ cảnh/session | "Session key là auth boundary" |
| Node pairing | Name | "Ném thiết bị = quyền truy cập không đáng tin cậy" |

---

## 3. Core Features

### 3.1 Memory System

OpenClaw không có "hidden state" — memory là **plain Markdown files** trong workspace:

#### Các loại memory files
- **`MEMORY.md`**: bộ nhớ lâu dài, sở thích và sự kiện bền vững. Đã được nạp vào mỗi phiên chạy DM.
- **`memory/YYYY-MM-DD.md`**: ghi chú hàng ngày, ngữ cảnh làm việc. Đã chỉ mục cho `memory_search`.
- **`DREAMS.md`** (tùy chọn): Nhật ký & quét giấc mơ tóm tắt.

#### Memory backends
| Backend | Mô tả | Extra deps |
|---------|-------|------------|
| **Builtin (default)** | Dựa vào gói_h gian , từ khóa + véc- tơ + lai tìm kiếm | Không cần |
| **QMD** | Xe phụ thứ nhất cục bộ, quay trở lại, mở rộng truy vấn | Cần cài plugin |
| **Honcho** | Bộ nhớ xuyên đại diện AI, mô hình người dùng | Plugin install |
| **LanceDB** | OpenAI- tương ứng với nhau, gọi tự động | Bundled |

#### Memory search
- Khi embedding provider được cấu hình → **hybrid search**: vector similarity + keyword matching
- Mặc định dùng OpenAI embeddings
- Có thể set `agents.defaults.memorySearch.provider` để dùng Gemini, Voyage, Mistral, local/Ollama, Bedrock

#### Tự động dội bộ nhớ
- Trước khi compaction xảy ra, OpenClaw chạy một silent turn nhắc agent lưu context quan trọng vào memory files
- Có thể config model riêng cho memory flush: `agents.defaults.compaction.memoryFlush.model`

#### Dreaming (optional)
- Nền được củng cố qua bộ nhớ cho bộ nhớ
- Score candidates, promote qualified items vào MEMORY.md
- Passed score, recall frequency, và query diversity gates
- Phase summaries viết vào DREAMS.md để human review

**Quan trọng:** Memory là **state + rehydration**, không phải "học" theo nghĩa machine learning. Agent chỉ "nhớ" những gì được save xuống disk.

### 3.2 Cron & Scheduling

Cron là Gateway's built-in scheduler, chạy **bên trong Gateway process**:

#### Schedule types
| Kind | CLI flag | Description |
|------|----------|-------------|
| `at` | `--at` | One-shot timestamp (ISO 8601 hoặc relative như `20m`) |
| `every` | `--every` | Fixed interval |
| `cron` | `--cron` | 5-field hoặc 6-field cron expression với optional `--tz` |

#### Execution styles
| Style | `--session` value | Runs in | Best for |
|-------|-------------------|---------|----------|
| Main session | `main` | ♪ Đường đi bộ dâng hiến cron | Nhắc nhở, các sự kiện hệ thống |
| Isolated | `isolated` | Dedicated `cron:<jobId>` | Báo cáo, việc làm nền |
| Current session | `current` | Hạn chế vào thời gian tạo | Công việc tái phát của văn cảnh |
| Custom session | `session:custom-id` | & Tiếp tục tên phiên chạy | Dòng chảy làm việc xây dựng lịch sử |

#### Đặc điểm quan trọng
- Job definitions, runtime state, và run history **persist trong SQLite** → restart không mất schedules
- On startup, overdue isolated agent-turn jobs được rescheduled ra khỏi channel-connect window
- All cron executions tạo [background task](#34-sub-agents--background-tasks) records
- Chạy « cun » (bộ nhớ tạm) tốt nhất chạy gần nhất để che đậy việc theo dõi bộ duyệt Mạng và xử lý khi chạy xong
- Công việc chụp một tấm (theo một tấm)`--at`) Tự động phát hành sau khi thành công theo mặc định

#### Ứng xử biểu thức thập phân
- Croner parser: khi cả day-of-month và day-of-week đều non-wildcard → **OR logic** (tiêu chuẩn Vixie cron)
- `0 9 15 * 1` = "9 AM ngày 15 HOẶC 9 AM thứ Hai" (~5-6 lần/thay vì 0-1 lần)
- Để require cả hai: dùng Croner's `+` modifier: `0 9 15 * +1`

### 3.3 Skills & Plugin System

#### Skills Loading Order (precedence cao nhất trước)
| Priority | Source | Path |
|----------|--------|------|
| 1 — highest | Workspace skills | `<workspace>/skills` |
| 2 | Kỹ năng tác nhân dự án | `<workspace>/.agents/skills` |
| 3 | Kỹ năng đặc vụ cá nhân | `~/.agents/skills` |
| 4 | Quản lý/cơ quan | `~/.openclaw/skills` |
| 5 | Bundled skills | được chuyển đi với cài đặt |
| 6 — lowest | Extra dirs | `skills.load.extraDirs` + plugin skills |

#### Những kỹ năng chia sẻ từng tác vụ
| Scope | Path | Visible to |
|-------|------|------------|
| Per-agent | `<workspace>/skills` | Chỉ agent đó |
| Project-agent | `<workspace>/.agents/skills` | Đặc vụ vùng làm việc |
| Personal-agent | `~/.agents/skills` | Tất cả agents trên machine |
| Shared managed | `~/.openclaw/skills` | Tất cả agents trên machine |

#### Agent Allowlists
```json5
{
  agents: {
    defaults: { skills: ["github", "weather"] }, // shared baseline
    list: [
      { id: "writer" }, // inherits github, weather
      { id: "docs", skills: ["docs-search"] }, // replaces defaults entirely
      { id: "locked-down", skills: [] }, // no skills
    ],
  },
}
```

#### Plugins
- Bổ sung mở rộng OpenClaw Các kênh v Whosi, các nhà cung cấp mô hình, các công cụ, kỹ năng, bài nói, giọng nói, giọng nói, sự hiểu biết phương tiện, việc lấy web, tìm kiếm web
- Install từ ClawHub, npm, git, hoặc local path
- Config under `plugins.entries.<id>.config`
- Plugin hooks: typed hooks via `api.on(...)` (preferred) và internal hook system via `api.registerHook(...)`

#### ClawHub Registry
- Public skills registry tại clawhub.ai
- Install: `openclaw skills install <slug>`
- Kiểm tra phong bì tin tưởng: `openclaw skills verify <slug>`
- Publish: `clawhub sync --all`

### 3. 4 Tác vụ phụ và tác vụ nền

#### & Nền:
Tasks là **activity ledger** cho background work — không phải scheduler:
- ACP, subagents, cron jobs, CLI operations → tạo tasks
- Heartbeat turns và normal interactive chat → KHÔNG tạo tasks
- Máy chính: `queued` → `running` → Máy cuối (`succeeded` `failed` `timed_out` `cancelled` `lost`)
- Terminal records kept 7 days rồi auto-prune

#### Task States
| Status | Ý nghĩa |
|--------|---------|
| `queued` | Tạo, đợi tác vụ khởi động |
| `running` | Đặc vụ quay tích cực thực hiện |
| `succeeded` | Completed successfully |
| `failed` | Hoàn tất với lỗi |
| `timed_out` | Đã quá giờ đã cấu hình |
| `cancelled` | Bị ngừng lại bởi tổng đài |
| `lost` | Đã mất thời gian để hỗ trợ quyền hạn sau 5 phút ân sủng |

#### Notify Policies
| Policy | What delivered |
|--------|----------------|
| `done_only` (default) | Chỉ nhà máy khách |
| `state_changes` | Name |
| `silent` | Không có gì |

#### Phân tích ngữ cảnh con
- Mỗi sub-agent có session riêng, workspace riêng
- Memory isolation: mặc định `memory_search` và `memory_get` bị blocked trong `SUBAGENT_TOOL_DENY_ALWAYS`
- Cần explicit allowlist để sub-agent truy cập memory tools
- Isolated cron runs: fresh session per run (không inherit ambient conversation context)

#### Giới hạn con đã biết (June 2026)
- **Issue #85030**: MCP tools không được inject vào subagent sessions — `bundle-mcp` + per-tool allowlist bị ignore
- **Issue #55385**: `memory_search` và `memory_get` hardcoded trong `SUBAGENT_TOOL_DENY_ALWAYS`

### 3.5 Browser Automation

OpenClaw cung cấp **dedicated Chrome/Brave/Edge/Chromium profile** cho agent:

#### Profiles
| Profile | Mô tả |
|---------|-------|
| `openclaw` | Managed, isolated browser (mặc định) |
| `user` | Xây dựng trong hrome MCP Name |

#### Features
- Điều khiển thẻ tối ưu (danh sách/ mở/tạp/ gần)
- Hành động đặc vụ: click/ type/dag/sator
- Hình chụp, hình chụp màn hình, PDFs
- Bundled `browser-automation` Kĩ năng cho trình duyệt đa bước điều khiển
- Hỗ trợ đa phương thức tuỳ chọn
- SSRF-guarded navigation và open-tab
- Screenshot vision cho text-only models (dùng image-understanding runtime để describe screenshots)

#### Điểm cấu hình trình duyệt
- `tabCleanup`: idle cleanup sau 120 phút, max 8 tabs per session
- `localLaunchTimeoutMs`: thời hạn cho phép khởi chạy Chromium (mặc định 15s)
- `actionTimeoutMs`: chương trình duyệt hoạt động chậm (60) mặc định
- Repeated launch failures → circuit-breaker để tránh spawn Chromium liên tục

### 3.6 Canvas (A2UI)

Canvas là agent-driven visual workspace:
- Agent có thể present HTML/CSS/JS lên connected nodes
- A2UI (Agent-to-User Interface): push text, JSONL payloads lên canvas
- Mobile nodes dùng bundled WebView renderer
- Commands: `canvas.present`, `canvas.navigate`, `canvas.eval`, `canvas.snapshot`, `canvas.a2ui.push`

### 3. 7 nút (iOS/Andero/macOS)

Nodes là companion devices kết nối với Gateway WebSocket:

#### Pairing Flow
1. Node connect với `role: "node"` và declared commands
2. Gateway tạo device pairing request
3. Approve via `openclaw devices approve <requestId>`
4. Name

#### Node Capabilities
- Điều khiển Canvas (hiện tại, định hướng, va li, hình chụp)
- Máy ảnh (snap, clip, danh sách)
- Ghi lại màn hình
- Địa điểm nhận/ thả
- Notifications management
- Giọng nói thức giấc + chế độ nói (psh- to- talk)
- Chạy hệ thống ( gõ lệnh khi máy nút)

#### Máy nút (hành quyết từ chối)
```bash
# Trên node machine:
openclaw node run --host <gateway-host> --port 18789 --display-name "Build Node"

# Trên gateway host:
openclaw devices list
openclaw devices approve <requestId>
```

#### Command Policy
- Nodes phải declare command trong `connect.commands`
- Gateway's platform policy phải allow declared command
- Dangerous commands (camera.snap, screen.record) cần explicit opt-in qua `gateway.nodes.allowCommands`
- `denyCommands` wins over defaults và allowlist entries

### 3.8 MCP Integration

MCP (Model Context Protocol) là cách OpenClaw connect với external tool servers:
- Discover tools at runtime từ bất kỳ MCP server nào
- Plugin-owned node commands có Gateway node-invoke policy riêng
- Known issue: Bundled MCP/LSP tools có thể bypass configured tool policy (GHSA-qrp5-gfw2-gxv4, patched 2026.4.20+)

---

## 4. Cấu hình lặn sâu

### File Structure
```
~/.openclaw/
├── openclaw.json              # Main config
├── workspace/                 # Default workspace
│   ├── MEMORY.md              # Long-term memory
│   ├── AGENTS.md              # Agent instructions
│   ├── SOUL.md                # Persona/personality
│   └── skills/                # Workspace skills
└── agents/<agentId>/          # Per-agent state
    ├── agent/                 # Auth profiles, model registry
    └── sessions/              # Session store
```

### Phần cấu hình khoá

#### Gateway Auth
```json5
{
  gateway: {
    auth: {
      mode: "shared-secret",  // or "trusted-proxy" for Tailscale
      token: "your-token",
      allowTailscale: true,   // Tailscale Serve support
    },
    nodes: {
      pairing: { autoApproveCidrs: ["192.168.1.0/24"] },
      allowCommands: ["camera.snap", "screen.record"],
      denyCommands: ["camera.clip"],
    },
  },
}
```

#### Session Management
```json5
{
  session: {
    dmScope: "per-channel-peer",  // isolate by channel + sender
    reset: { idleMinutes: 480 },  // 8-hour idle reset
    maintenance: {
      mode: "enforce",
      pruneAfter: "30d",
      maxEntries: 500,
    },
  },
}
```

#### Dùng đa chương trình
```json5
{
  agents: {
    list: [
      { id: "main", workspace: "~/.openclaw/workspace-main" },
      { id: "coding", workspace: "~/.openclaw/workspace-coding" },
    ],
  },
  bindings: [
    { agentId: "main", match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } } },
    { agentId: "coding", match: { channel: "discord", guildId: "guild-xxx" } },
  ],
}
```

#### Model Configuration
```json5
{
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-sonnet-4-6" },
      models: {
        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },
        "openai/*": {},       // wildcard for all OpenAI models
        "ollama/*": {},       // wildcard for all Ollama models
      },
    },
  },
}
```

#### Sandboxing
```json5
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main",     // only non-main sessions in sandbox
        scope: "agent",       // one container per agent
        backend: "docker",    // Docker-backed
      },
    },
  },
}
```

---

## 5. Best Practices

### Security Hardening
1. **Chạy `openclaw security audit --deep`** sau mỗi config change
2. **Dùng `agents.defaults.sandbox.mode: "non-main"`** để sandbox group/channel sessions
3. **Set `gateway.nodes.allowCommands`** cho dangerous commands thay vì accept all
4. **Sử dụng Tailscale hoặc SSH tunnel** cho remote access thay vì public exposure
5. **Dùng `session.dmScope: "per-channel-peer"`** khi nhiều người dùng shared agent

### Performance Optimization
1. **Enable session maintenance** để auto-prune old sessions (30 days, max 500 entries)
2. **Config compaction model riêng** cho summarization thay vì dùng primary model
3. **Dùng isolated cron** cho background tasks để không block main session
4. **Set `tabCleanup`** cho browser để prevent orphaned tabs

### Memory Management
1. **Distill từ daily notes vào MEMORY.md** định kỳ để giữ file nhỏ gọn
2. **Dùng action-sensitive memories** khi note liên quan đến timing/authority/expiry
3. **Enable dreaming** nếu muốn automatic memory consolidation
4. **Monitor `MEMORY.md` size** — nếu vượt bootstrap budget, OpenClaw truncates injected copy

### Thiết lập đa đại biểu
1. **Không reuse `agentDir`** giữa các agents (gây auth/session collisions)
2. **Copy chỉ portable static profiles** (`api_key`, `token`) khi share credentials
3. **Dùng bindings deterministic routing** với most-specific-wins strategy
4. **QMD Tìm kiếm bộ nhớ qua** qua `agents.list[].memorySearch.qmd.extraCollections`

---

## 6. Gotchas & Limitations

### Critical Gotchas

1. **Ngày tháng của thời gian trôi qua + ngày-tháng-truyện-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-thô-tì-thô-thô-thô-tì-t-t" `0 9 15 * 1` Lửa cháy vào ngày 15 và mỗi thứ Hai, không chỉ ngày 15 nếu là thứ Hai. `0 9 15 * +1`

2. **Sandboxing OFF by default**: Nếu không config sandbox, `host=auto` resolves to `gateway`. Explicit `host=sandbox` fails closed nếu sandbox chưa enabled.

3. **MCP tools not in subagents**: MCP tools được inject vào main session nhưng KHÔNG tự động inject vào subagent sessions (Issue #85030)

4. **Memory tools blocked in subagents**: `memory_search` và `memory_get` hardcoded trong `SUBAGENT_TOOL_DENY_ALWAYS` — cần explicit allowlist

5. **DMs share one session by default**: Nếu nhiều người dùng shared agent, tất cả share cùng conversation context (Alice's messages visible to Bob)

6. **Session reset freshness based on `sessionStartedAt`**, không phải `updatedAt`. Heartbeat/cron turns write metadata nhưng không extend daily/idle reset freshness.

7. **Docker-out-of-Docker**: Khi Gateway chạy trong Docker, `workspace` config MUST dùng host absolute path, không phải container internal path.

8. **MCP/LSP bypass vulnerability** (GHSA-qrp5-gfw2-gxv4): Patched trong 2026.4.20+ — đảm bảo update lên phiên bản mới nhất.

### Chọn mô hình
- Mô hình Nội thất đã được chuẩn hoá thành chữ thường; nhà cung cấp ID chính xác xác trường hợp nhạy cảm
- `/model` user selection persists per-session, không ảnh hưởng config primary
- Changing `agents.defaults.model.primary` không rewrite existing session selections
- Khi `agents.defaults.models` là allowlist, model rejected trước khi reply được generate → tin nhắn có vẻ "không response"

### Browser Gotchas
- `tools.profile: "coding"` bao gồm `web_search` và `web_fetch` nhưng KHÔNG bao gồm `browser` tool — cần explicit `alsoAllow: ["browser"]`
- Repeated managed Chrome launch failures → circuit-breaker, không spawn Chromium mỗi lần
- Ảnh chụp ngược lại: công cụ.media. ảnh ảnh Mô tả mặc định Model cho nhà cung cấp thô

---

## 7, so sánh với những lựa chọn khác

| Feature | OpenClaw | n8n/Make | LangChain | AutoGen | CrewAI |
|---------|----------|----------|-----------|---------|--------|
| Self-hosted | ✅ Full control | Partial | ✅ | ✅ | ✅ |
| Multi-channel | 20+ channels native | Via connectors | Via adapters | Limited | Limited |
| Memory system | Xây dựng markdown + QMD/LanceDB | Manual | Custom | Custom | Custom |
| Cron scheduling | Được xây dựng, chia sẻ SBS | Workflow-based | Custom | Custom | Custom |
| Sandbox | Docker/SSH/OpenShell | N/A | Container | Multi-agent isolation | Agent isolation |
| Browser automation | Xây dựng hồ sơ | Via tools | Via plugins | Via agents | Via agents |
| Mobile nodes | iOS/Andero/macOS bản xứ | No | No | No | No |
| Open source | _TIẾNG MIT, 309K+ sao | ✅ Apache 2.0 | ✅ MIT | ✅ MIT | ✅ MIT |
| Config-driven | Tập tin cấu hình JSON5 | Visual UI | Code-based | YAML/code | YAML/code |
| Định tuyến đa tác vụ | Hệ thống ràng buộc bản địa | Via workflows | Custom | Built-in | Built-in |

### Khi nào dùng OpenClaw
- Bạn muốn một **personal AI assistant** chạy 24/7 trên thiết bị của mình
- Cần kết nối với nhiều messaging channels từ cùng một agent
- Muốn persistent memory mà không cần database riêng
- Cần browser automation, cron jobs, và sandboxing trong một package
- Prefer config-driven approach thay vì code-heavy

### Khi nào cân nhắc alternatives
- **Enterprise multi-tenant**: OpenClaw là personal-assistant model, không phải multi-tenant platform
- **Complex ETL pipelines**: n8n/Make tốt hơn cho workflow automation với UI
- **Research/experimentation**: LangChain tốt hơn cho rapid prototyping của LLM chains

---

## Tổng kết

OpenClaw là một AI agent platform mature với kiến trúc solid, được build cho self-hosted personal assistant use case. Điểm mạnh lớn nhất là:

1. ** Cửa ra không xác định** cho 20 kênh+
2. **Bilt-in-trong hệ thống bộ nhớ** kông c quing c quiten coun cơ sở dữ liệu bên ngoài
3. **Sandboxing linh hoạt** (Docker/SSH/ openShell)
4. **Sub-agent isolation** với background task tracking
5. **Active community** với 379K+ GitHub stars và ecosystem skills/plugins phong phú

Những hạn chế chính cần lưu ý:
- Sub-agent MCP injection chưa hoàn thiện
- Memory tools blocked trong subagents (cần explicit config)
- Sandbox không phải perfect security boundary
- Cần update thường xuyên để patch vulnerabilities mới

---

*Documpt tạo ra: 2026-06-15 Nguồn: tiến sĩ.openclawChào. github.com/comopenclaw/openclaw, Reddit threads, DV.to, How openClaw, TheAgentStack Substack, ClawHub, GitHub số #85030 - #55385, GHSA cố vấn*
