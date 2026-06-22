---
title: "Spaced Repetition Config"
slug: "spaced-repetition-config"
category: learning
tags: [srs, review, learning]
status: active
type: config
created: 2026-06-20
last_updated: 2026-06-20
---

# 🔄 Spaced Repetition System (SRS) Configuration

> Cấu hình cho Obsidian Spaced Repetition plugin.
> Review atomic notes theo forgetting curve để kiến thức không bị quên.

## 📐 Interval Settings

| Phase | Days Between Reviews | Quality Target |
|-------|---------------------|----------------|
| New → 1st review | 1 day | ≥70% recall |
| 1st → 2nd review | 3 days | ≥60% recall |  
| 2nd → 3rd review | 7 days | ≥50% recall |
| Stable knowledge | 30+ days | Maintenance mode |

## 🎯 Review Strategy

### Daily (5-10 phút)
- Chỉ review notes có **status = active** trong `40-Knowledge-Synthesis/`
- Skip drafts và superseded
- Focus on FB Ads frameworks + Bac Giang psychology (high ROI knowledge)

### Weekly Connect Phase (Thứ 7 20:00)
- Review tất cả notes do hôm nay SRS flag là "failing" (<50% recall)
- Update note với insights mới
- Demote kiến thức cũ → archive hoặc superseded

## 📊 Quality Metrics

```dataview
TABLE 
  length(rows) AS "Total Notes",
  mean(status) AS "Avg Status"
FROM "40-Knowledge-Synthesis/Insights" OR "40-Knowledge-Synthesis/Frameworks"
WHERE type = "atomic-note"
GROUP BY status
```

## 🔔 Alert Rules (Agent Protocol)

- **>15 notes pending review** → alert Hùng ngay (overloaded)
- **<3 reviews completed last week** → suggest schedule adjustment
- **Notes failing 2+ consecutive reviews** → flag for rewrite or archive

---

*Created: 2026-06-20 by Smee — Layer 5 Deploy (SRS Config)*
*Configure in Obsidian Settings → Spaced Repetition → adjust intervals above.*
