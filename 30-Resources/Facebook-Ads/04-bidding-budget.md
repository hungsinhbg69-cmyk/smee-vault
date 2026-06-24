---
title: "Bidding & Budget"
slug: "bidding-budget"
category: resource
tags: [facebook-ads, meta-ads]
status: reference
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

﻿# 04 - Bidding & Budget (Chinh sach chi phi + Bidding)

## Budget Types

### Daily Budget
- Average spend per day (Facebook may fluctuate +/-15%)
- Good for: consistent daily delivery, predictable spending
- Minimum: depends on currency, typically /day minimum
- Use when: you want steady daily results

### Lifetime Budget
- Total spend over entire campaign duration
- Facebook distributes across days based on opportunity
- Good for: time-limited campaigns, events, promotions
- Use when: campaign has fixed start/end date

**Recommendation:** For most campaigns, daily budget gives more predictable results. Lifetime budget works well for time-sensitive offers.

## Bidding Strategies

### 1. Lowest Cost (Mac dinh)
- Facebook auto-optimizes for lowest cost per result
- No bid cap - spends full budget for maximum results
- Best for: maximizing results within budget, new campaigns
- Risk: may overspend on expensive audiences initially
- **Use this by default** when starting

### 2. Cost Cap (Control average cost)
- Sets target average cost per result
- Facebook tries to get results AT or BELOW target cost
- May spend less than full budget if opportunities limited
- Best for: scaling campaigns with known CPA targets
- Risk: may exit learning phase if too few results at cap

**Setting cost cap:** Start with 1.5-2x your target CPA, then tighten as algorithm learns.

### 3. Bid Cap (Control maximum bid)
- Sets hard maximum bid for auction
- Facebook only enters auctions where you can win at or below bid
- Most control, least flexibility
- Best for: competitive auctions, specific placement bids
- Risk: may not spend full budget if bids too low

## Campaign Budget Optimization (CBO) Deep Dive

### How CBO works
1. Set ONE budget at campaign level
2. Create 2-6 ad sets within campaign
3. Meta distributes budget dynamically to best-performing ad sets
4. Algorithm shifts budget every ~hour based on real-time performance
5. Best ad sets get more budget automatically

### CBO requirements
- Minimum 2 ad sets, maximum 6 ad sets per campaign
- Similar audience types (don't mix broad LAL with narrow interests)
- Each ad set needs minimum ~/day to gather data
- Allow 48 hours for algorithm to stabilize distribution

### When to use CBO vs ABO
| Scenario | Budget Type | Why |
|---|---|---|
| Testing new audiences | ABO (ad set budget) | Equal spend per test |
| Scaling winners | CBO (campaign budget) | Algorithm finds cheapest results |
| Established campaign, 3+ ad sets | CBO | Proven distribution works |
| Single ad set | Either | No difference with 1 ad set |
| Limited budget (</day total) | ABO | Guarantee each test gets spend |
| Large budget (+/day) | CBO | Algorithm distributes efficiently |

### CBO best practices
1. Don't mix very different audiences in same CBO campaign
2. Use similar audience sizes for fair comparison
3. Set minimum ad set spend if needed (via cost cap per ad set)
4. Allow learning phase before making changes (48+ hours)
5. Budget should be at least 10x your target CPA minimum

## The Learning Phase (Phase Hoc)

### What triggers learning phase
- New campaign/ad set created
- Significant edit made (>25% budget change, creative swap, targeting change)
- Ad paused and reactivated
- Delivery issue resolved

### Learning phase requirements
- **50 optimization events per week per ad set** - this is the magic number
- Optimization event = the conversion event you're optimizing for (purchase, lead, etc.)
- If fewer than 50 events/week, stays in learning indefinitely

### During learning phase
- Performance UNSTABLE and unpredictable
- Cost may be higher than normal
- Don't make major edits during this period
- Allow minimum 48 hours before judging performance
- **Do NOT panic and stop early** - this is where most advertisers lose money

### Exiting learning phase
1. Naturally: accumulate 50+ events/week over time
2. Accelerate: increase budget (but max 20% every 3-4 days)
3. Reduce ad sets: consolidate budget into fewer ad sets for more data per ad set
4. Broaden targeting: more people = more conversion opportunities

### Learning phase indicators in Ads Manager
- "Learning Limited" = not enough events to exit learning
- "Active" + no learning badge = successfully exited learning phase
- Check weekly: how many optimization events per ad set?

## Budget Recommendations by Campaign Type

### E-commerce (Sales objective)
- Starting budget: -50/day per ad set minimum
- CBO recommended once proven winners identified
- Scale 20% every 3-4 days when profitable
- Monthly budget should allow for Q4 increase (2-3x)

### Lead Generation
- Budget: -30/day per ad set
- CPL varies by industry (-)
- Test lead quality vs quantity at different budgets
- Follow up leads within 1 hour

### Brand Awareness
- Budget: -25/day sufficient (optimizing for reach/impressions)
- Lower CPA than conversion campaigns
- Measure via ad recall lift studies

## Cost Benchmarks (US Market, 2026)
- **CPM:** - (varies by industry, season, audience)
- **CPC:** .50-.00
- **CPL:** - (heavy industry dependency)
- **Q4 premium:** October-December costs 2-3x higher
- **Retargeting vs Prospecting:** Retargeting always cheaper per result

## Budget Scaling Rules
1. **Max 20% increase every 3-4 days** - more = reset learning phase
2. **Duplicate strategy:** Copy winning ad set to new campaign with higher budget (preserves original learning)
3. **Horizontal scaling:** Expand to similar audiences/larger LALs
4. **Vertical scaling:** Increase budget on proven ad sets gradually
5. **Monitor CPA after scale:** If CPA increases >20%, slow down scaling

## Key Takeaways
- Lowest Cost bidding = default choice, use Cost Cap when you know target CPA
- CBO for scaling, ABO for testing new audiences
- 50 optimization events/week/ad set needed to exit learning phase
- Max 20% budget increase every 3-4 days to avoid learning reset
- Q4 costs are 2-3x higher - plan budget accordingly
- Learning Limited status = not enough data, consolidate or broaden targeting

---
*Created: 2026-06-15 | Sources: marketingadvice.ai, marketingagency.one*