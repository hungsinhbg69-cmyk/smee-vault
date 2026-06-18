# 06 - Optimization & Scaling (Tieu chuan + Mo rong campaign)

## Testing Strategy Framework

### What to test (prioritized)
1. **Creative** (biggest lever for performance improvement in 2026)
   - Different visual styles (UGC vs studio)
   - Different hooks (question, stat, problem statement)
   - Different formats (video, static, carousel)
   - Different CTAs

2. **Audiences**
   - Advantage+ vs interest targeting
   - Lookalike 1% vs 5% vs broad
   - Custom audience segments by recency

3. **Copy**
   - Headlines (benefit-driven vs curiosity-driven)
   - Primary text length (short vs long form)
   - Tone (professional vs conversational)
   - Social proof placement

4. **Placements**
   - Automatic vs manual
   - Reels-only vs feed-only vs both
   - Audience Network inclusion/exclusion

5. **Landing pages**
   - Different offers
   - Different headlines
   - Different form lengths

### Testing best practices
- **Test ONE variable at a time** - isolates what caused the change
- **Run minimum 7 days** - avoid day-of-week bias, allow algorithm to stabilize
- **Minimum 50 conversions for statistical significance** per variant
- **Document ALL learnings** - create test log with results
- **Implement winners, kill losers** - don't let underperformers drain budget

### Test documentation template
`
Test: [what changed]
Date started: YYYY-MM-DD
Hypothesis: [why this should improve performance]
Variant A: [control - current version]
Variant B: [test - new version]
Duration: 7+ days OR 50+ conversions
Result: [winner/loser/tie/inconclusive]
Action taken: [implement, kill, or continue testing]
`

## Campaign Optimization Checklist (Weekly)

### Every Monday review
- [ ] Check which ad sets exited learning phase vs stuck in "Learning Limited"
- [ ] Review CPA/ROAS per ad set vs target
- [ ] Identify ads with CTR < 1% (underperforming creative)
- [ ] Check frequency per ad set (flag if >3.0 = ad fatigue)
- [ ] Verify budget pacing (on track for monthly goals?)
- [ ] Review top performing creatives - save winners

### Weekly actions
- Rotate new creatives into underperforming ad sets
- Kill ads with CPA > 2x target after 7 days
- Increase budget on winning ad sets (max 20% per cycle)
- Add new hooks to test (minimum 3 new concepts per month)
- Review audience performance - consolidate similar audiences

## Scaling Strategies

### When to scale (all must be true)
1. Campaign is profitable (ROAS > target OR CPA < target)
2. Consistent performance for minimum 7 days
3. Learning phase complete (50+ events/week, "Active" status)
4. Budget allows for expansion
5. Creative not showing fatigue (frequency < 3.0)

### Scaling method 1: Vertical scaling (increase budget)
- Increase budget max 20% every 3-4 days
- More than 20% may reset learning phase
- Monitor CPA closely after each increase
- If CPA increases >20%, pause and hold for 3-4 days before trying again

### Scaling method 2: Duplicate campaign (preserves learning)
- Copy winning ad set to NEW campaign
- Set higher budget on new campaign
- Original campaign continues learning undisturbed
- New campaign starts fresh learning phase with more budget
- Best for: doubling or tripling spend quickly

### Scaling method 3: Horizontal scaling (new audiences)
- Expand to similar lookalike audiences (1% -> 5%)
- Test new interest clusters
- Geographic expansion (new cities/provinces)
- New placements (if currently limited)

### Scaling method 4: Creative scaling (most sustainable)
- Produce variations of winning creative concepts
- Same hook, different visuals
- Same visual, different copy
- Same concept, different format (static -> video)
- Keeps performance fresh without changing audience

## Scaling Timeline Example

`
Week 1-2: Testing phase
  - 3 ad sets x 3 creatives = 9 ads
  - Budget: /day per ad set (/day total)
  - Identify top 2 performing ad sets + top creative per ad set

Week 3-4: Consolidation
  - Kill bottom 5 ads
  - Increase budget on winners by 20%
  - Add 3 new creative variations to test

Week 5-8: Scaling
  - CBO campaign with proven winners
  - Scale budget 20% every 3-4 days
  - Duplicate top campaign at higher budget level
  - Test horizontal audience expansion

Ongoing: Creative rotation
  - New creatives every 2-4 weeks per ad set
  - Monthly creative testing cycle (minimum 3 new concepts)
  - Save winning hooks for reuse in new formats
`

## Performance Alert Thresholds

### Critical alerts (immediate action needed)
- CPA > 2x target for 3+ consecutive days
- CTR dropped >50% week-over-week (creative fatigue)
- Frequency > 4.0 (severe ad fatigue)
- Learning Limited status > 7 days

### Warning alerts (monitor closely)
- CPA approaching 1.5x target
- Conversion rate dropping but volume stable
- Cost per click increasing without performance change
- Daily spend fluctuation >30%

### Healthy metrics (no action needed)
- CPA within target range
- CTR > 1%
- Frequency < 2.5
- Consistent daily conversion volume

## Automation Opportunities

### Performance alerts
- Check campaign metrics every 6 hours via API
- Slack/Telegram notification when CPA exceeds threshold
- Auto-pause ads with CPA > 3x target after 7 days

### Budget pacing
- Daily check: compare actual spend vs expected
- Alert if pacing deviates >10% from plan
- Projected monthly spend based on current trajectory

### Creative rotation schedule
- Weekly creative audit: identify ads at frequency >2.5
- Auto-refresh with pre-approved new creatives
- Monthly new concept testing cycle

## Key Takeaways
- Test ONE variable at a time, minimum 7 days or 50 conversions
- Scale budget max 20% every 3-4 days to avoid learning reset
- Duplicate campaigns for aggressive scaling (preserves original learning)
- Creative is the #1 lever for performance improvement in 2026
- New creatives every 2-4 weeks per ad set (combat ad fatigue)
- Frequency > 3.0 = time to refresh creative

---
*Created: 2026-06-15 | Sources: marketingadvice.ai, marketingagency.one*