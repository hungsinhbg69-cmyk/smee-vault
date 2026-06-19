---
title: "JeffSu-AI-Agents-Explained"
slug: "jeffsu-ai-agents-explained"
category: frameworks
tags: [obsidian-cleanup, auto-added]
status: draft
type: framework
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: JeffSu - AI Agents Clearly Explained
tags: [jeffsu, ai-agents, llm, workflow, prompt-engineering]
source: NotebookLM "JeffSu Master Learning"
created: 2026-06-18
type: framework
---

# AI Agents — Clear Explanation (from JeffSu)

## Workflow vs Agent: The Critical Difference
- **AI Workflow:** Predefined path, human decides each step, LLM executes tasks
- **AI Agent:** LLM becomes the decision-maker — reasons out steps autonomously and takes action to reach a goal

## Three Components of an AI Agent
1. **Brain:** Chat Model + Memory (context retention)
2. **Tools:** APIs for Google Sheets, Slack, etc.
3. **Brain Stem:** System Prompt controlling tool usage

## REACT Framework
- **Reason:** Think through the approach
- **Act:** Perform tasks using tools
- Enables autonomous iteration toward goals

## Everyday vs Reasoning Models
- **Flash models:** Quick, simple tasks (ChatGPT, Claude basic)
- **Pro/Reasoning models:** Complex planning, self-correction (Gemini Pro, OpenAI o-series)

## Key Principles
- **First Try Fallacy:** Don't expect perfect results from one prompt. Ask AI to ask *you* five clarifying questions first.
- **Prompt Overload Paradox:** Consuming many prompts without optimizing or consistently using core few in daily work.
- **"Ask me 5 questions" trick:** Best instruction for gathering context before final response.

## AI Tools Specialization (JeffSu's breakdown)
| Tool | Best For |
|------|----------|
| Claude | Writing functional code on first try |
| ChatGPT | Following complex checklists, reasoning |
| Perplexity AI | Search scalpel — real-time fact-fetching with citations |
| NotebookLM | Q&A from uploaded sources only (no hallucination) |
| Gemini | Canvas feature — write/run code in chat, multimodal processing |

## RAG (Retrieval-Augmented Generation)
- AI looks up external data (calendar, news) before answering
- Prevents hallucinations by grounding responses in real data

## Backlinks
- [[JeffSu-Channel-Summary]]
- [[JeffSu-Prompt-Engineering]]