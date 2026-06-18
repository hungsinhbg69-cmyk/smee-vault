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
   - 3.4 Sub-agents & Background Tasks
   - 3.5 Browser Automation
   - 3.6 Canvas (A2UI)
   - 3.7 Nodes (iOS/Android/macOS)
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
- **Open source**: MIT license, community-driven (379K+ GitHub stars)
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
- Maintains provider connections (WhatsApp via Baileys, Telegram via grammY, v.v.)
- Exposes typed WebSocket API với requests, responses, và server-push events
- Validates inbound frames against JSON Schema
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

### Node Trust Concept
| Boundary | Ý nghĩa | Common misread |
|----------|---------|----------------|
| `gateway.auth` | Authenticates callers to gateway APIs | "Cần per-message signatures" |
| `sessionKey` | Routing key cho context/session | "Session key là auth boundary" |
| Node pairing | Operator-level remote execution | "Remote device = untrusted user access" |

---

## 3. Core Features

### 3.1 Memory System

OpenClaw không có "hidden state" — memory là **plain Markdown files** trong workspace:

#### Các loại memory files
- **`MEMORY.md`**: Long-term memory, durable facts & preferences. Loaded at start of every DM session.
- **`memory/YYYY-MM-DD.md`**: Daily notes, working context. Indexed for `memory_search`.
- **`DREAMS.md`** (optional): Dream diary & dreaming sweep summaries.

#### Memory backends
| Backend | Mô tả | Extra deps |
|---------|-------|------------|
| **Builtin (default)** | SQLite-based, keyword + vector + hybrid search | Không cần |
| **QMD** | Local-first sidecar, reranking, query expansion | Cần cài plugin |
| **Honcho** | AI-native cross-session memory, user modeling | Plugin install |
| **LanceDB** | OpenAI-compatible embeddings, auto-recall | Bundled |

#### Memory search
- Khi embedding provider được cấu hình → **hybrid search**: vector similarity + keyword matching
- Mặc định dùng OpenAI embeddings
- Có thể set `agents.defaults.memorySearch.provider` để dùng Gemini, Voyage, Mistral, local/Ollama, Bedrock

#### Automatic memory flush
- Trước khi compaction xảy ra, OpenClaw chạy một silent turn nhắc agent lưu context quan trọng vào memory files
- Có thể config model riêng cho memory flush: `agents.defaults.compaction.memoryFlush.model`

#### Dreaming (optional)
- Background consolidation pass cho memory
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
| Main session | `main` | Dedicated cron wake lane | Reminders, system events |
| Isolated | `isolated` | Dedicated `cron:<jobId>` | Reports, background chores |
| Current session | `current` | Bound at creation time | Context-aware recurring work |
| Custom session | `session:custom-id` | Persistent named session | Workflows builds on history |

#### Đặc điểm quan trọng
- Job definitions, runtime state, và run history **persist trong SQLite** → restart không mất schedules
- On startup, overdue isolated agent-turn jobs được rescheduled ra khỏi channel-connect window
- All cron executions tạo [background task](#34-sub-agents--background-tasks) records
- Isolated cron runs best-effort close tracked browser tabs/processes khi run complete
- One-shot jobs (`--at`) auto-delete after success by default

#### Cron expression behavior
- Croner parser: khi cả day-of-month và day-of-week đều non-wildcard → **OR logic** (tiêu chuẩn Vixie cron)
- `0 9 15 * 1` = "9 AM ngày 15 HOẶC 9 AM thứ Hai" (~5-6 lần/thay vì 0-1 lần)
- Để require cả hai: dùng Croner's `+` modifier: `0 9 15 * +1`

### 3.3 Skills & Plugin System

#### Skills Loading Order (precedence cao nhất trước)
| Priority | Source | Path |
|----------|--------|------|
| 1 — highest | Workspace skills | `<workspace>/skills` |
| 2 | Project agent skills | `<workspace>/.agents/skills` |
| 3 | Personal agent skills | `~/.agents/skills` |
| 4 | Managed / local skills | `~/.openclaw/skills` |
| 5 | Bundled skills | shipped with install |
| 6 — lowest | Extra dirs | `skills.load.extraDirs` + plugin skills |

#### Per-agent vs Shared Skills
| Scope | Path | Visible to |
|-------|------|------------|
| Per-agent | `<workspace>/skills` | Chỉ agent đó |
| Project-agent | `<workspace>/.agents/skills` | Workspace's agent |
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
- Plugins extend OpenClaw với channels, model providers, agent harnesses, tools, skills, speech, realtime transcription, voice, media understanding, web fetch, web search
- Install từ ClawHub, npm, git, hoặc local path
- Config under `plugins.entries.<id>.config`
- Plugin hooks: typed hooks via `api.on(...)` (preferred) và internal hook system via `api.registerHook(...)`

#### ClawHub Registry
- Public skills registry tại clawhub.ai
- Install: `openclaw skills install <slug>`
- Verify trust envelope: `openclaw skills verify <slug>`
- Publish: `clawhub sync --all`

### 3.4 Sub-agents & Background Tasks

#### Background Task System
Tasks là **activity ledger** cho background work — không phải scheduler:
- ACP, subagents, cron jobs, CLI operations → tạo tasks
- Heartbeat turns và normal interactive chat → KHÔNG tạo tasks
- State machine: `queued` → `running` → terminal (`succeeded`, `failed`, `timed_out`, `cancelled`, `lost`)
- Terminal records kept 7 days rồi auto-prune

#### Task States
| Status | Ý nghĩa |
|--------|---------|
| `queued` | Created, waiting for agent to start |
| `running` | Agent turn actively executing |
| `succeeded` | Completed successfully |
| `failed` | Completed with error |
| `timed_out` | Exceeded configured timeout |
| `cancelled` | Stopped by operator |
| `lost` | Runtime lost authoritative backing state after 5-min grace period |

#### Notify Policies
| Policy | What delivered |
|--------|----------------|
| `done_only` (default) | Only terminal state |
| `state_changes` | Every state transition and progress update |
| `silent` | Nothing at all |

#### Sub-agent Context Isolation
- Mỗi sub-agent có session riêng, workspace riêng
- Memory isolation: mặc định `memory_search` và `memory_get` bị blocked trong `SUBAGENT_TOOL_DENY_ALWAYS`
- Cần explicit allowlist để sub-agent truy cập memory tools
- Isolated cron runs: fresh session per run (không inherit ambient conversation context)

#### Known Sub-agent Limitations (June 2026)
- **Issue #85030**: MCP tools không được inject vào subagent sessions — `bundle-mcp` + per-tool allowlist bị ignore
- **Issue #55385**: `memory_search` và `memory_get` hardcoded trong `SUBAGENT_TOOL_DENY_ALWAYS`

### 3.5 Browser Automation

OpenClaw cung cấp **dedicated Chrome/Brave/Edge/Chromium profile** cho agent:

#### Profiles
| Profile | Mô tả |
|---------|-------|
| `openclaw` | Managed, isolated browser (mặc định) |
| `user` | Built-in Chrome MCP attach cho real signed-in Chrome session |

#### Features
- Deterministic tab control (list/open/focus/close)
- Agent actions: click/type/drag/select
- Snapshots, screenshots, PDFs
- Bundled `browser-automation` skill cho multi-step browser control
- Optional multi-profile support
- SSRF-guarded navigation và open-tab
- Screenshot vision cho text-only models (dùng image-understanding runtime để describe screenshots)

#### Browser Config Key Points
- `tabCleanup`: idle cleanup sau 120 phút, max 8 tabs per session
- `localLaunchTimeoutMs`: timeout cho Chromium startup (default 15s)
- `actionTimeoutMs`: default browser act timeout (60s)
- Repeated launch failures → circuit-breaker để tránh spawn Chromium liên tục

### 3.6 Canvas (A2UI)

Canvas là agent-driven visual workspace:
- Agent có thể present HTML/CSS/JS lên connected nodes
- A2UI (Agent-to-User Interface): push text, JSONL payloads lên canvas
- Mobile nodes dùng bundled WebView renderer
- Commands: `canvas.present`, `canvas.navigate`, `canvas.eval`, `canvas.snapshot`, `canvas.a2ui.push`

### 3.7 Nodes (iOS/Android/macOS)

Nodes là companion devices kết nối với Gateway WebSocket:

#### Pairing Flow
1. Node connect với `role: "node"` và declared commands
2. Gateway tạo device pairing request
3. Approve via `openclaw devices approve <requestId>`
4. Device token issued cho subsequent connects

#### Node Capabilities
- Canvas controls (present, navigate, eval, snapshot)
- Camera (snap, clip, list)
- Screen capture/record
- Location get/set
- Notifications management
- Voice wake + talk mode (push-to-talk)
- System run (exec commands on node machine)

#### Node Host (Remote Execution)
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

## 4. Config Deep Dive

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

### Key Config Sections

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

#### Multi-Agent Routing
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

### Multi-Agent Setup
1. **Không reuse `agentDir`** giữa các agents (gây auth/session collisions)
2. **Copy chỉ portable static profiles** (`api_key`, `token`) khi share credentials
3. **Dùng bindings deterministic routing** với most-specific-wins strategy
4. **QMD memory search cross-agent** qua `agents.list[].memorySearch.qmd.extraCollections`

---

## 6. Gotchas & Limitations

### Critical Gotchas

1. **Cron day-of-month + day-of-week OR logic**: `0 9 15 * 1` fires on EVERY 15th AND every Monday, not just the 15th if it's Monday. Fix: `0 9 15 * +1`

2. **Sandboxing OFF by default**: Nếu không config sandbox, `host=auto` resolves to `gateway`. Explicit `host=sandbox` fails closed nếu sandbox chưa enabled.

3. **MCP tools not in subagents**: MCP tools được inject vào main session nhưng KHÔNG tự động inject vào subagent sessions (Issue #85030)

4. **Memory tools blocked in subagents**: `memory_search` và `memory_get` hardcoded trong `SUBAGENT_TOOL_DENY_ALWAYS` — cần explicit allowlist

5. **DMs share one session by default**: Nếu nhiều người dùng shared agent, tất cả share cùng conversation context (Alice's messages visible to Bob)

6. **Session reset freshness based on `sessionStartedAt`**, không phải `updatedAt`. Heartbeat/cron turns write metadata nhưng không extend daily/idle reset freshness.

7. **Docker-out-of-Docker**: Khi Gateway chạy trong Docker, `workspace` config MUST dùng host absolute path, không phải container internal path.

8. **MCP/LSP bypass vulnerability** (GHSA-qrp5-gfw2-gxv4): Patched trong 2026.4.20+ — đảm bảo update lên phiên bản mới nhất.

### Model Selection Gotchas
- Model refs normalized to lowercase; provider IDs exact case-sensitive
- `/model` user selection persists per-session, không ảnh hưởng config primary
- Changing `agents.defaults.model.primary` không rewrite existing session selections
- Khi `agents.defaults.models` là allowlist, model rejected trước khi reply được generate → tin nhắn có vẻ "không response"

### Browser Gotchas
- `tools.profile: "coding"` bao gồm `web_search` và `web_fetch` nhưng KHÔNG bao gồm `browser` tool — cần explicit `alsoAllow: ["browser"]`
- Repeated managed Chrome launch failures → circuit-breaker, không spawn Chromium mỗi lần
- Screenshot vision fallback chain: tools.media.image → imageModel defaults → auth-backed provider

---

## 7. Comparison with Alternatives

| Feature | OpenClaw | n8n/Make | LangChain | AutoGen | CrewAI |
|---------|----------|----------|-----------|---------|--------|
| Self-hosted | ✅ Full control | Partial | ✅ | ✅ | ✅ |
| Multi-channel | 20+ channels native | Via connectors | Via adapters | Limited | Limited |
| Memory system | Built-in markdown + QMD/LanceDB | Manual | Custom | Custom | Custom |
| Cron scheduling | Built-in, SQLite-persisted | Workflow-based | Custom | Custom | Custom |
| Sandbox | Docker/SSH/OpenShell | N/A | Container | Multi-agent isolation | Agent isolation |
| Browser automation | Built-in, managed profile | Via tools | Via plugins | Via agents | Via agents |
| Mobile nodes | iOS/Android/macOS native | No | No | No | No |
| Open source | ✅ MIT, 379K+ stars | ✅ Apache 2.0 | ✅ MIT | ✅ MIT | ✅ MIT |
| Config-driven | JSON5 config file | Visual UI | Code-based | YAML/code | YAML/code |
| Multi-agent routing | Native bindings system | Via workflows | Custom | Built-in | Built-in |

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

1. **Unified gateway** cho 20+ channels
2. **Built-in memory system** không cần external database
3. **Sandboxing flexible** (Docker/SSH/OpenShell)
4. **Sub-agent isolation** với background task tracking
5. **Active community** với 379K+ GitHub stars và ecosystem skills/plugins phong phú

Những hạn chế chính cần lưu ý:
- Sub-agent MCP injection chưa hoàn thiện
- Memory tools blocked trong subagents (cần explicit config)
- Sandbox không phải perfect security boundary
- Cần update thường xuyên để patch vulnerabilities mới

---

*Document generated: 2026-06-15 | Sources: docs.openclaw.ai, github.com/openclaw/openclaw, Reddit threads, DEV.to, HowOpenClaw, TheAgentStack Substack, ClawHub registry, GitHub issues #85030 & #55385, GHSA advisory*
