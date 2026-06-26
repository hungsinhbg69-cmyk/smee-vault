---
title: ""Spaced Repetition System (SRS)""
slug: spaced-repetition-system-srs
category: resource
tags: [learning, spaced-repetition, config]
created: 2026-06-27
last_updated: 2026-06-27
---

# Spaced Repetition — Marketing Knowledge Engine

Transform vault notes into flashcards using Obsidian Spaced Repetition plugin.

## Deck Organization (by folder)

| Folder | Deck Name | Focus Area | Review Schedule |
|--------|-----------|------------|-----------------|
| 30-Resources/Facebook-Ads/* | FB Ads Mastery | Algorithm, targeting, bidding | Daily review |
| 40-Knowledge-Synthesis/Frameworks/* | Frameworks & Systems | JeffSu, marketing frameworks | Weekly deep review |
| 40-Knowledge-Synthesis/Insights/* | Market Intelligence | Bac Giang, trends | Bi-weekly review |

## Card Creation Rules

### Flashcard Format (single-line)
```
Question?::Answer with key details
```

### Cloze Deletion Format  
```
The Facebook algorithm in 2026 prioritizes ==engagement quality== over raw volume. Key signal: [[time-spent-viewing]].
```

### Multi-line Format
```
What are the 5 KPIs from Co Hoc Tinh Hoa?
1. Customer Retention Rate
2. Content Value Score (Shares + Saves > Likes)
3. Algorithm Adaptation Speed
4. Crisis Response Time  
5. Long-term LTV:CAC Ratio::Remember: "Truoc khi danh nguoi phai biet gi minh" - measure before launch!
```

## Review Schedule

| Card Age | Interval | Difficulty Multiplier |
|----------|----------|----------------------|
| New (0-3 days) | Every day | 1.5x harder |
| Growing (4-14 days) | Every 2 days | 1.2x |
| Stable (15+ days) | Weekly to Monthly | Standard |

## Priority Tags for SRS

- `#srs/high` — Must know: FB algorithm core signals, bidding strategies, metrics benchmarks
- `#srs/medium` — Important but can reference: specific case study details  
- `#srs/low` — Nice to know: minor optimization tips, tool preferences
- `#flashcard` — Auto-flagged by SRS plugin for card creation

## Plugin Settings (current)

```json
{
  "flashcardTags": ["#flashcards"],
  "convertHighlightsToClozes": true,
  "enableReviewReminders": false,
  "reviewReminderIntervalMinutes": 5,
  "singleLineCardSeparator": "::",
  "multilineCardSeparator": "?",
  "clozePatterns": ["==[123;;]answer[;;hint]=="]
}
```

## SRS Flashcard Examples from FB Ads Knowledge

### High Priority Cards (Must Know)

Facebook algorithm 2026 prioritizes engagement quality over raw volume?::Time spent viewing, saves, shares. Likes are least weighted signal. Key: "quality > quantity" rule.

What is the CBO scaling rule for Facebook ads?::Increase budget by max 20% per day per ad set. Scale winners vertically first, then horizontally with new audiences. Never increase budget on losing ad sets.

What's the ideal CPM range for Vietnam market in 2026?::FB Ads Vietnam: $0.50-$1.50 for broad reach, $1.50-$3.00 for targeted. If CPM >$4, audience too narrow or creative fatigue detected.

What are the Andromeda auction tiers?::Tier 1 (win rate 80%+): high relevance score + low bid. Tier 2 (win rate 60-80%): balanced relevance/bid. Tier 3: need optimization — check CTR, frequency, creative freshness.

What's the optimal ad frequency for conversion campaigns?::Frequency < 3.0 for prospecting (fresh creatives). Frequency 1.5-2.5 for retargeting. If frequency >4.0 within 7 days = creative fatigue, rotate new assets.

### Medium Priority Cards

How to structure a Facebook Ads campaign hierarchy?::Campaign (objective) > Ad Set (audience + budget) > Ad (creative). One objective per campaign. Test one variable at a time between ad sets.

What's the minimum daily budget for meaningful testing?::$10-20/day per ad set minimum for statistical significance in Vietnam market. For conversion campaigns targeting high-value products, start $30+/day.

What is Advantage+ Shopping Campaigns (ASC) best used for?::E-commerce product catalogs with clean pixel data. Best when you have 50+ conversions/week. Use ASC for scaling winners from manual campaigns, not cold starts.

### Low Priority Cards

Quick tip: When should you switch from CPC to CPM bidding?::When your CTR < 1% — switching to CPM gives algorithm more freedom. When CTR > 2%, stick with CPC or optimize creative first.

What's the recommended pixel implementation for 2026 Facebook ads?::Conversions API (CAPI) + browser pixel combined. Server-side tracking essential after iOS 17+ ATT changes. Verify events in Events Manager daily.

---
*Configured: 2026-06-20 by Smee — Layer 4 (SRS)*
