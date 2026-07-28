---
title: "Trung tâm điều hành Vault"
slug: "vault-command-center"
category: meta
tags: [dashboard, dataview, analytics, automation]
status: active
type: moc
created: 2026-06-27
last_updated: 2026-06-27
---

# Trung tâm điều hành Vault

> Bảng điều khiển tích hợp - khai thác **dataview + tasks-plugin + charts + metadata-menu + calendar**  
> Cập nhật REAL-TIME với các truy vấn Dataview. Đồng bộ tự động qua obsidian-git.

## □ Khởi chạy nhanh (QuickAdd Macros)
| Hành động | Phím tắt Macro | Mô tả |
|--------|-----------|-------------|
| 🔥 Ghi chú nguyên tử mới | `capture-new-note` | Tự động tạo frontmatter và liên kết thông minh |
| 💭 Suy nghĩ thoáng qua | `capture-quick-thought` | Thu thập nhanh vào ghi chú hàng ngày qua templater |
| 📊 Đánh giá tuần | `review-weekly-init` | Mở mẫu đánh giá tuần với quét dataview |

> Nhập macro: Cài đặt -> QuickAdd -> Quản lý -> Nhập `_scripts/quickadd-macro-config.json`

---

## □ Nhịp điệu hàng ngày - Ghi chú mới nhất

**Plugin: dataview + calendar** — Quét thời gian thực qua các thư mục trong vault

```dataview
TABLE length(file.tags) as "Tags", type as "Type"
FROM ""
WHERE file.mtime > date("-30 days") AND file.type != undefined
SORT file.mtime DESC
LIMIT 15
```

---

## □ Nhiệm vụ đang hoạt động - Tất cả chưa hoàn thành

**Plugin: obsidian-tasks-plugin** — Xem tổng hợp nhiệm vụ, có thể sắp xếp theo mức độ ưu tiên

```tasks
not done
group by due
sort by priority descending
reverse
```

Nhiệm vụ ưu tiên cao trong tuần này
```tasks
not done
due during this week
priority matches /.*/
```

---

## □ Dự án đang hoạt động - Bảng điều khiển

**Plugins: dataview +kanban + siêu dữ liệu-menu**

````dataview
TABLE status as "Status", type as "Type", length(file.tags) as "Tags"
FROM "10-Projects"
WHERE status != "archived"
SORT file.ctime DESC
````

> Tiếp theo: Sử dụng plugin **kanban** (Ctrl+P -> Kanban: Tạo bảng mới) để theo dõi dự án trực quan. Liên kết thẻ với các dự án ở trên.

---

## □ Chất lượng metadata - 7 ngày gần nhất

**Plugin: metadata-menu + templater** — Chỉnh sửa frontmatter qua giao diện đồ họa, không cần gõ tay

### Các tệp đã sửa đổi gần đây
```dataview
TABLE file.mtime as "Modified Last"
FROM ""
WHERE file.mtime > date("-7 days")
SORT file.mtime DESC
LIMIT 20
```

---

## □ Xem nhanh phân tích Vault

**Plugin: biểu đồ + obsidian- Bản đồ tư duy + Công cụ Người cá + obsidian- Nhân vật chính**

1. **Mở bất kỳ ghi chú nào → Bản đồ tư duy**: Ctrl+P -> "MindMap" (plugin obsidian-mind-map)  
2. **Hiển thị biểu đồ trực tuyến**: dán khối ` ```mermaid ` (xem VAULT-ANALYTICS.md để biết mẫu)  
3. **Tùy chỉnh icon thư mục**: Cài đặt -> obsidian-icon-folder -> Thêm bộ icon

### Mẫu biểu đồ tăng trưởng
Xem `00-Meta/VAULT-ANALYTICS.md` cho định dạng chart.json đầy đủ và quy trình làm việc web clipper.

---

## □ Tóm tắt kích hoạt quy trình làm việc

| Bước | Plugin(s) | Hành động |
|------|-----------|-------------|
| Thu thập ghi chú | quickadd + templater + smart-connections | Ghi chú nguyên tử/thoáng qua tự động được tạo mới |
| Đánh giá tuần | Ghi chú tuần hoàn + lịch và thẻplugin | Kiểm toán tuần đầy đủ với quét nhiệm vụ |
| Theo dõi dự án | kanban + dataview + git + Người cá | Bảng Kanban + theo dõi sprint |
| Đồng bộ & sao lưu | obsidian-git + từ xa-save | Đồng bộ đám mây + lịch sử kiểm soát phiên bản |
| Trực quan hóa dữ liệu | sơ đồ + bộ trí- mảng và bộ tạo biểu tượng | Bảng điều khiển phân tích + icon thư mục |
| Tìm kiếm và kết nối | omnisearch + các kết nối thông minh và phụ lái | Tìm kiếm ngữ nghĩa + trò chuyện AI |

---

*Trung tâm điều hành tích hợp 7+ plugin cốt lõi.*
*Tham khảo [[PROJECT-COMMAND-CENTER]] · [[TASK-ENGINE]] · [[VAULT-ANALYTICS]] · _templates/weekly-review.md*
