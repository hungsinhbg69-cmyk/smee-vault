---
title: "JeffSu-Prompt-Engineering"
slug: "jeffsu-prompt-engineering"
category: frameworks
tags: [obsidian-cleanup, auto-added]
status: draft
type: framework
created: 2026-06-19
last_updated: 2026-06-19
---

---
title: JeffSu - Prompt Engineering Guide
tags: [jeffsu, prompt-engineering, ai, chatgpt, claude, gemini]
source: NotebookLM "JeffSu Master Learning"
created: 2026-06-18
type: framework
---

# Prompt Engineering Guide (from JeffSu)

## Core Principles

### First Try Fallacy
Don't expect perfect results from one prompt. Effective prompting involves iterative refinement.

### The Magic Instruction
**"First ask me five questions that will improve the response you'll be giving me."**
- Forces AI to gather context before generating final output
- Dramatically improves response quality

## Prompt Templates & Patterns

### Notion Prompt Database Template
- Use Callout Boxes for placeholders (Command + E)
- Visually distinguish variables like [insert data set]
- Organize by use case: drafting, research, code, analysis

### AI Agent System Prompt Structure
```
[Role definition]
[Tool usage rules]
[Output format requirements]
[Error handling instructions]
```

### ChatGPT Best Practices
- Ask clarifying questions before generating
- Use step-by-step reasoning for complex tasks
- Specify output format explicitly

## Tool-Specific Prompting

### Claude
- Best for: Writing functional, high-quality code on first try
- Strength: Code generation accuracy
- Weakness: Less optimized for real-time search

### ChatGPT
- Best for: Following complex checklists, reasoning tasks
- Strength: Complex multi-step workflows
- Tip: Use "ask me 5 questions" pattern

### Perplexity AI
- Best for: Search scalpel — real-time fact-fetching with citations
- Use as replacement for Google Search
- Verify facts quickly with source attribution

### NotebookLM
- Best for: Q&A from uploaded sources only (zero hallucination)
- Use @YouTube command for podcast analysis
- Ask for top 3 takeaways + actionable steps from long videos

### Google Gemini
- **Canvas feature:** Write/run code (Python/HTML/JS) directly in chat
- **@YouTube command:** Analyze 2-hour podcasts, get key takeaways
- **Reverse-engineer prompts:** Paste image → ask for original prompt
- Multimodal: Process text, audio, video, images simultaneously

## Prompt Overload Paradox
- Problem: Consuming many AI prompts without optimizing core few in daily work
- Solution: Build personal prompt library, test and refine, use consistently

## Google's NEW Prompting Guide Highlights
- Structured approach to prompt design
- Context-setting before task description
- Output specification with format requirements

## Backlinks
- [[JeffSu-AI-Agents-Explained]]
- [[JeffSu-Channel-Summary]]