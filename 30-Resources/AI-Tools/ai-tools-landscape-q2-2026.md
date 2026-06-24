---
title: "AI Tools Landscape Q2 2026"
slug: "ai-tools-landscape-q2-2026"
category: resource
tags: [vault-maintenance]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

---

# AI Tools Landscape Q2 2026

> Tổng hợp + phân tích công cụ AI nổi bật Q2 2026, tập trung vào marketing stack của Hùng.

## Executive Summary

Q2/2026: AI tools đã chuyển từ "experimental" → "production-ready". Xu hướng chính:
1. **Multimodal là default** — text/image/video/audio trong cùng một model
2. **Agent loops** — tool không chỉ generate, mà tự execute workflow
3. **On-device/local AI** — privacy-first, chạy offline (Ollama ecosystem phát triển mạnh)
4. **Vertical AI** — tools chuyên ngành (legal, healthcare, real estate) thay vì generalist

## Model Layer — Core LLMs

### 1. OpenAI GPT-4o / GPT-5 (GPT-5 Preview)
- **Pricing:** $8/month (Plus), $200/month (Pro)
- **Strengths:** Multimodal native, Sora 2 integration (video gen), plugin ecosystem
- **Marketing use:** Content generation, document analysis, customer research
- **Weaknesses:** Rate limits trên free tier, bias toward US market data
- **For Hùng:** ChatGPT + GPT-5 là core tool cho content brainstorming + doc analysis

### 2. Anthropic Claude (Opus/Sonnet)
- **Pricing:** $17/month+, Opus cao hơn nhiều
- **Strengths:** Coding accuracy cao nhất, reasoning logic tốt, Claude Cowork (desktop automation)
- **Marketing use:** Code generation (OpenClaw skills), data analysis, structured output
- **Weaknesses:** Price premium so alternatives
- **For Hùng:** Claude Sonnet > GPT-4o cho coding tasks. Claude 4 Opus worth nếu budget cho phép

### 3. Google Gemini (Pro/Ultra + Deep Research)
- **Pricing:** $7.99/month+, Deep Research paid feature
- **Strengths:** Large context window, Deep Research auto-research, Nano Banana image gen, Audio Overview
- **Marketing use:** Research compilation, market analysis, content repurposing (audio summary)
- **Weaknesses:** Ecosystem lock-in với Google products
- **For Hùng:** Gemini Deep Research = competitor cho NotebookLM. Dùng để research niche markets

### 4. Open Source Local Models (Ollama ecosystem)
- **Models:** Qwen 3, Llama 4, Mixtral, Gemma variants
- **Pricing:** Free (local), inference cost ≈ $0
- **Strengths:** Privacy, no rate limits, customizable, fine-tunable
- **Marketing use:** Daily agent operations (OpenClaw running on Ollama)
- **For Hùng:** Current setup `mixi/fredrezones55-qwen36-aggressive-stable:latest` là solid choice. Consider swapping to Qwen 3 Turbo khi available

## AI Video Generation — Marketing Goldmine

### 5. Google Veo 3
- **Pricing:** Free tier, paid $19.99/month+
- **Strengths:** Cinematic quality, smooth camera movement, natural motion, synchronized sound
- **Marketing use:** Product ads, social media teasers, branded visuals, mood-driven scenes
- **For Hùng:** Veo 3 > Sora 2 cho realistic product videos. Integration với Synthesia

### 6. OpenAI Sora 2
- **Strengths:** Story-driven narrative, cinematic clips
- **Marketing use:** Brand storytelling, campaign videos
- **Weaknesses:** Less control over specific shots vs Veo

### 7. Higgsfield AI
- **Pricing:** $9/month (no free tier)
- **Strengths:** All-in-one image+video, multi-model testing, community trending content
- **Marketing use:** Creative concept iteration, A/B test ad creatives rapidly
- **For Hùng:** Best for rapid creative testing. Unlimited image gen + video pipeline

### 8. Synthesia
- **Pricing:** Free tier, $18/month+
- **Strengths:** AI avatars, Video Agents (interactive), Veo 3 + Sora 2 integration
- **Marketing use:** Training videos, product explainers, multilingual content, interactive demos
- **For Hùng:** Video Agents = game changer for real estate property tours

## Voice & Audio AI

### 9. ElevenLabs
- **Pricing:** $5-$99/month
- **Strengths:** Most realistic voices, voice cloning, Voice Agents (conversational bots), multilingual
- **Marketing use:** Podcast narration, YouTube voiceovers, customer support bots, ad voiceovers
- **For Hùng:** Voice Agents cho Facebook Messenger/Telegram auto-reply. Clone brand voice

### 10. Google Audio Overview (Gemini)
- **Pricing:** Free within Gemini
- **Strengths:** Podcast-style summaries from documents
- **Marketing use:** Content repurposing, quick learning on-the-go

## Research & Knowledge Management

### 11. NotebookLM (Google)
- **Pricing:** Free, $8.99/month+
- **Strengths:** Document Q&A, audio summaries, knowledge base creation
- **Marketing use:** Market research synthesis, competitor analysis, content planning
- **For Hùng:** Upload Bac Giang market reports → get instant insights. Audio summary cho commute

### 12. Gemini Deep Research
- **Pricing:** Paid feature within Gemini
- **Strengths:** Automated multi-step research, interactive reports, reasoning traces
- **Marketing use:** Competitive analysis, trend spotting, niche market research
- **For Hùng:** Replace manual research workflow. Feed URL → get structured report

## No-Code App Building

### 13. Lovable
- **Pricing:** Free tier, $25/month+
- **Strengths:** Prompt-to-app, no coding needed, interactive widgets
- **Marketing use:** Landing pages, MVPs, internal tools, lead capture forms
- **For Hùng:** Quick campaign landing pages without developer

## Presentation & Document Generation

### 14. Gamma
- **Pricing:** Free tier, $9-$90/month
- **Strengths:** Notes-to-decks, clean design, AI visuals, PPTX export
- **Marketing use:** Client proposals, pitch decks, training materials
- **For Hùng:** Turn research notes → professional client presentations in minutes

## Meeting & Workflow Automation

### 15. Fathom
- **Pricing:** Free (forever), $15/month+
- **Strengths:** Zoom/Teams integration, auto-transcription, action item extraction, CRM sync
- **Marketing use:** Client meeting notes, team sync, action tracking
- **For Hùng:** Record client calls → auto summary + follow-up tasks

## Agent-Specific Tools (OpenClaw Context)

### 16. OpenClaw Gateway
- **Current:** v2026.6.5
- **Role:** AI agent orchestration, cron jobs, memory system, multi-channel routing
- **For Hùng:** Core infrastructure — everything runs through here

### 17. Obsidian + Smart Connections MCP
- **Role:** Second brain, semantic search, vault automation
- **Current:** 139 notes, 8386 blocks, 384-dim vectors (bge-micro-v2)
- **For Hùng:** Knowledge base for all research, agent retrieval

### 18. Multi-Search Engine Skill
- **Role:** 6 search engines (4 global + 2 CN), no API keys needed
- **For Hùng:** Market research across regions, competitor monitoring

## Pricing Comparison — Monthly Cost Stack

| Category | Tool | Free | Paid | Marketing ROI |
|----------|------|------|------|---------------|
| Core LLM | ChatGPT Plus | Limited | $8/mo | High |
| Core LLM | Claude Pro | Limited | $17/mo | Medium (coding) |
| Research | NotebookLM | ✅ | $8.99/mo | Medium |
| Video | Veo 3 | ✅ | $19.99/mo | High (ads) |
| Video | Higgsfield | ❌ | $9/mo | High (creative testing) |
| Voice | ElevenLabs | ✅ | $5-$99/mo | Medium-High |
| No-Code | Lovable | ✅ | $25/mo | Low-Medium |
| Presentations | Gamma | ✅ | $9+/mo | Medium |
| Meetings | Fathom | ✅ | Free tier | Medium |

**Minimal viable stack for Hùng:** ChatGPT Plus ($8) + Veo 3 free + Higgsfield ($9) + ElevenLabs starter ($5) = **$22/month** for core marketing AI tools.

## Vietnamese Market Specific Tools

### Local AI Tools (Vietnam-focused)
- **VUI.AI** — Vietnamese conversational AI, customer support bots
- **VNLP** — Vietnamese NLP toolkit for text analysis
- **SpeechPro VN** — Vietnamese speech-to-text
- **AI Content VN** — Vietnamese content generation (SEO, social media)

### Facebook/Local Platform Tools
- **Meta Business Suite** — Free, native FB/IG management
- **Canva AI** — Design + AI image gen (free tier available)
- **CapCut** — Video editing + AI features (free)
- **Zalo AI Chatbot** — Vietnamese messaging platform bot

## Integration Map — Hùng's Stack 2026 Q2

```
[Content Planning] → NotebookLM (research) → ChatGPT/Claude (drafting) → Gamma (presentation)
       ↓
[Creative Production] → Higgsfield (image gen) → Veo 3 (video) → ElevenLabs (voiceover)
       ↓
[Distribution] → OpenClaw (scheduling + automation) → Facebook Pages (Graph API)
       ↓
[Engagement] → ElevenLabs Voice Agent (auto-reply) → Fathom (meeting notes)
       ↓
[Analysis] → Gemini Deep Research (market trends) → Obsidian (knowledge base)
```

## Key Trends Q3 2026 Preview

1. **AI-native browsers** — Browsing with AI agent built-in (not just extensions)
2. **Real-time video avatars** — Live stream with AI host (Synthesia Video Agents expanding)
3. **Multimodal search** — Search by image/audio/video, not just text
4. **Personal AI clones** — Your AI that knows your style, preferences, decision patterns
5. **Edge AI chips** — On-device LLMs on phones/laptops (no cloud needed)
6. **AI regulation compliance** — EU AI Act enforcement starting mid-2026

## Sources & Verification

- Primary: Synthesia "12 Best AI Tools for 2026" (June 2026) — verified live URL
- Secondary: FutureTools.io directory (Matt Wolfe)
- Model data: Official pricing pages, OpenAI/Anthropic/Google docs
- Local ecosystem: Ollama model registry, Obsidian plugin marketplace
- **Last verified:** 2026-06-17

---

*Created: 2026-06-17 | Updated: 2026-06-17 | Next review: 2026-09-17 (Q3 update)*
