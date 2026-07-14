---
title: "Phân loại thẻ (Tag Taxonomy)"
slug: "tag-taxonomy"
category: meta
tags: [meta, taxonomy]
status: active
type: reference
created: 2026-06-12
last_updated: 2026-07-14
---

# Tham khảo Phân loại Thẻ (Tag Taxonomy)

## Quy tắc

- Sử dụng tối đa năm thẻ cho mỗi ghi chú.
- Sử dụng tên viết thường, có dấu gạch ngang. Chỉ sử dụng `/` để tạo phân cấp ổn định.
- Bảo tồn các thẻ miền có ý nghĩa; chỉ hợp nhất những lỗi chính tả, khác biệt về chữ hoa/thường hoặc các đồng nghĩa đã được chứng minh.
- Thêm thẻ vào danh mục trước khi sử dụng lần đầu. Việc rà soát hàng quý sẽ loại bỏ các thẻ chết (dead aliases); nó không nhằm theo đuổi một số lượng tùy ý trên toàn kho lưu trữ.
- Chu kỳ sống thuộc về `status`; ngày tháng thuộc về thuộc tính. Các thẻ chỉ chứa số cần có tiền tố như `year/2026`.

## Phân cấp ổn định

```text
project/ai-agent-engineering
project/facebook-marketing
area/content-creation
area/marketing
status/active
status/draft
status/reference
type/atomic-note
tool/openclaw
concept/ai-agent-design
concept/content-strategy
```

## Đồng nghĩa an toàn (Safe aliases)

| Alias | Canonical |
|---|---|
| `bacgiang`, `BacGiang` | `bac-giang` |
| `bacninh`, `BacNinh` | `bac-ninh` |
| `fb-api` | `facebook-api` |
| `fb-graph` | `facebook-graph` |
| `Area`, `areas` | `area` |
| `Project`, `projects` | `project` |
| `obsidian-cleanup`, `auto-added` | loại bỏ; các thẻ này ghi lại quá trình di chuyển, không phải ý nghĩa của ghi chú |

## Danh mục hiện tại (Current registry)

```text
advanced
agent
agent-hub
agent-improvement
agent-training
agent-training/local-pack
ai-agents
analytics
ancient-texts
api
area/content-creation
area/marketing
audit-retest
automation
bac-giang
bac-ninh
bds
bidding
board
brian-tracy
budgeting
camilo-cruz
campaign-structure
capture
case-study
cbo
charts
clv-cac
command-center
commercial-condo
con-bo
concept
concept/ai-agent-design
concept/content-strategy
config
confucian-bias
content
content-card
content-pipeline
content-plan
content-strategy
creative
critical-review
daily
daily-review
dashboard
dataview
deploy-log
dev-platform
diagram
e-commerce
entity
evidence-discipline
excalidraw
expansion
facebook
facebook-ads
facebook-marketing
final-retest
flashcards
fundamentals
governance
grading
hermes
hoang-ninh-ecolife
home-services
human-nature
inbox
incident-response
index
insights
integration
intention
jeffsu
kanban
kanban-integration
karpathy
lead-gen
learning
legal-audit
legal-research
local-services
log
maintenance
market-data
marketing
marketing-architecture
meta
meta-ads
metrics
mind-map
moc
morning-ritual
navigation
nha-o-xa-hoi
no-xh
northern-vietnam
noxh
noxh/phu-tho
obsidian
official-sources
openclaw
para
people
personal-development
phu-tho
pipeline
pkm
placeholder
pricing
priority
productivity
project
project-management
project/ai-agent-engineering
project/facebook-marketing
protocol
psychology
q2-2026
quick-reference
quickadd
quiz
real-estate
reference
relationship-selling
research
research-paper
resource-index
review
sales
sales-funnel
scaling
schema
self-critique
self-improvement
setup
social-housing
spaced-repetition
srs
status/active
status/draft
status/reference
strategy
strict-audit
tasks
tasks-plugin
taxonomy
template
testing
tool/openclaw
type/atomic-note
vault-governance
vault-index
vault-maintenance
versioning
vietnam
vietnamese-book
web-clip
wiki
workflow
yen-the-golden-hill
zettelkasten
zotero
```

Danh mục đã được đối chiếu với frontmatter của ghi chú chính thống vào ngày 2026-07-14.
