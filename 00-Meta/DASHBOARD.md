---
title: "Trung tâm điều hành Vault"
slug: vault-dashboard
category: meta
tags: [meta, dashboard, command-center]
status: active
type: hub
created: 2026-06-20
last_updated: 2026-07-14
---

# 🧠 Trung tâm điều hành Vault

> [[Protocol]] — Hub trung tâm. Bắt đầu mỗi phiên làm việc tại đây.  
> **Các plugin đang hoạt động:** Templater · QuickAdd · Dataview · Tasks · Git · Kanban · Smart Connections · Excalidraw

---

## ⚡ THU NHẬN NGAY (Phím tắt)

| Hành động | Phím tắt | Lựa chọn QuickAdd |
|---|---|---|
| 💭 Suy nghĩ nhanh → Hàng ngày | `Mod+Shift+Space` | tư duy bắt giữ |
| 📥 Ý tưởng → Hộp thư đến | `Mod+Shift+I` | capture-inbox |
| 📝 Ghi chú nguyên tử | `Mod+Shift+N` | Ghi chú mới thu |
| ✅ Nhiệm vụ hôm nay | `Mod+Shift+T` | lưu- nhiệm vụ- ngày hôm nay |
| 🚀 Dự án mới | `Mod+Shift+P` | In- ra- mới |
| 📚 Ghi chú tài liệu | — | Ghi chú tự động thu |
| 📅 Tổng kết tuần | `Mod+Shift+W` | Xem xét- tuần |
| 🔍 Smart Connections | `Mod+Shift+S` | — |
| 🔎 Tìm kiếm toàn diện | `Mod+Shift+O` | — |
| 🔄 Kéo Git | `Mod+Shift+G` | — |

---

## 🔴 DỰ ÁN ĐANG TIẾN HÀNH

```dataview
TABLE status AS "Trạng thái", last_updated AS "Cập nhật", tags AS "Thẻ"
FROM "10-Projects"
WHERE status = "active" OR status = "draft"
SORT last_updated DESC
```

## ✅ NHIỆM VỤ — HẾT HẠN (Hành động ngay!)

```tasks
not done
due before today
sort by due ascending
group by file.link
limit 20
```

## 📋 NHIỆM VỤ — TUẦN NÀY

```tasks
not done
due this week
sort by due ascending
group by priority
limit 30
```

## 📥 HỘP THƯ ĐẾN (Chưa xử lý — mục tiêu < 5)

```dataview
TABLE file.ctime AS "Thu nhận", file.size AS "Kích thước"
FROM "01-Inbox"
SORT file.ctime DESC
```

## 🔥 KIẾN THỨC MỚI NHẤT (7 ngày qua)

```dataview
TABLE created AS "Ngày", category AS "Danh mục", status AS "Trạng thái"
FROM "40-Knowledge-Synthesis" OR "30-Resources"
WHERE created >= date(today) - dur(7 days)
SORT created DESC
LIMIT 10
```

## 📊 BỨC TRANH TỔNG QUAN SỨC KHỎE VAULT

### Ghi chú theo Trạng thái

```dataview
TABLE length(rows) AS "Số lượng"
FROM ""
WHERE file.folder != ".obsidian" AND file.folder != "copilot" AND file.folder != "_templates"
GROUP BY status
SORT length(rows) DESC
```

### Ghi chú bị bỏ rơi (< 2 liên kết ngược)

```dataview
TABLE length(file.inlinks) AS "Liên kết ngược", length(file.outlinks) AS "Liên kết xuôi"
FROM "40-Knowledge-Synthesis" OR "30-Resources"
WHERE length(file.inlinks) < 2
SORT length(file.inlinks) ASC
LIMIT 15
```

### Ghi chú được tạo trong tháng này

```dataview
TABLE created AS "Tạo", type AS "Loại"
FROM "40-Knowledge-Synthesis"
WHERE created >= date(this month)
SORT created DESC
```

## 📚 DÒNG CHUYỀN QUẢNG CÁO FACEBOOK

```dataview
TABLE status AS "Trạng thái", tags AS "Thẻ", type AS "Loại"
FROM "30-Resources/Facebook-Ads" OR "40-Knowledge-Synthesis/Frameworks"
WHERE contains(tags, "facebook-ads") OR type = "framework"
SORT last_updated DESC
LIMIT 10
```

## 🏘️ DỰ ÁN BẮC GIANG

```dataview
TABLE status AS "Trạng thái", type AS "Loại", last_updated AS "Cập nhật"
FROM "40-Knowledge-Synthesis/Real-Estate" OR "30-Resources/Bac-Giang"
SORT last_updated DESC
LIMIT 10
```

---

## 🤖 GHI CHÚ CHẤT LƯỢNG TỰ ĐỘNG (AGENT)

- **Smee** (phạm vi vault): Xem [[AGENTS.md]] — quy tắc vận hành
- **cli-rest-mcp**: Chạy trên cổng 27124 — REST API + MCP đang hoạt động
- **Smart Connections**: Chỉ mục TF-IDF, loại trừ: copilot, templates, archive
- **Cài đặt plugin cuối cùng**: 2026-07-14 bởi Antigravity

---

*Dashboard v3 — 2026-07-14 · Xây dựng lại bởi tác nhân Antigravity · Cài đặt plugin chuyên nghiệp*
