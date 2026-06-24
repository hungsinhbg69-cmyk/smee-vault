---
title: "Smee Self-Critique — 2026-06-20"
slug: "smee-self-critique-2026-06-20"
category: knowledge
tags: [vault-maintenance]
status: reference
type: reference
created: 2026-06-24
last_updated: 2026-06-24
---


# Smee Self-Critique — 2026-06-20

## Summary
Hùng phạt: "biết tài liệu nhưng không dùng, lặp response 7 lần/phiên, xác định page sai."
Root cause: Không có discipline trong việc áp dụng kiến thức đã học.

## Errors Found
1. **Duplicate Response Loop** — Same message repeated 5-7 times/session (sessions 14:36, 15:27)
2. **Ignoring Reference Docs** — Has fb-graph-api-deep-dive.md but acts on confidence not evidence
3. **Context Confusion** — Wrong page ID/token after session reset
4. **Sequential API Calls** — Tested 15 permissions one-by-one instead of batch
5. **Conflicting Token Info** — MEMORY.md had contradictory entries for Page 2

## Root Causes & Fixes
| Symptom | Root Cause | Fix Applied |
|---|---|---|
| Lặp response | No last_action tracking | AGENTS.md STEP 1: State Declaration + turn scan |
| Bỏ qua ref docs | Skips Step 0 | AGENTS.md STEP 0: Reference Check mandatory |
| Context nhầm lẫn | No explicit state block | AGENTS.md STEP 1: STATE block at session start |
| API tuần tự | Not using batch | AGENTS.md STEP 2: Batch First rule |
| Claim sai | Verify after action not before | AGENTS.md STEP 3: Verify Then Claim |

## Token Priority Order (Updated)
1. `.env` file → primary source of truth, verify by calling API first use
2. Hardcoded in config → fallback for never-expire tokens only
3. `/me/accounts` refresh → last resort with user token

## Rules Applied To Files
- AGENTS.md: Added CORE OPERATING PROTOCOL (4 steps)
- MEMORY.md: Added Common Mistakes section + Token Priority Order
- Session notes cleaned up, duplicate entries removed

---
## Related
- [[protocol]] — CORE OPERATING PROTOCOL (updated after this critique)
- [[agent-operating-protocol]] — Smee's operating rules
- [[vault-command-center]] — Health dashboard tracks these KPIs

*Tags: #self-audit #facebook-api #operations #2026-06-20*