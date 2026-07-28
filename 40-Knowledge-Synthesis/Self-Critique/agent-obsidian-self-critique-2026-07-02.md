---
title: "Agent Obsidian Tự nhận diện mình — 2026-07-02"
slug: "agent-obsidian-self-critique-2026-07-02"
category: knowledge
type: self-critique
status: active
created: 2026-07-02
last_updated: 2026-07-02
tags: [self-critique, obsidian, agent-improvement]
---

# Đặc vụ. Obsidian Tự nhận diện mình — 2026-07-02

## Phần 1: Tự Phê Bình Thẳng Thắn

### ❌ LỖI NẶNG — Sai vị trí vault khi search (tần suất: nhiều lần)

**Dấu hiệu:** Khi `terminal` tìm file trong vault, tao luôn dùng `C:\Users\Hung\Desktop\Smee Obsidian\Smee` nhưng rồi sau đó lại tạo/xóa file ở nơi khác hoặc fail vì đường dẫn sai. Kỹ thuật viên đã đổi name của vault thành "Tri kiến Nhân Loại" và đưa vào `Obsidian/Tri kiến Nhân Loại`, nhưng agent vẫn search ở Smee path cũ — dẫn đến **file created trong folder sai, không thấy khi search, phải làm lại.**

**Gây ra lỗi gì:**
- Tạo note ở wrong directory → không tìm được bằng wikilinks
- Patch file không tồn tại → session bị block phải redo
- Index/MOC trỏ đến file wrong location → links broken

### ❌ LỖI NẶNG — Read file qua pagination bị mất context lớn (tần suất: liên tục)

**Dấu hiệu:** Dùng `read_file` với default limit (~500 dòng) cho file >60KB (ví dụ: Hoang-Ninh-Ecolife-ContentPlan-Th7.md là 40KB+). Thấy được phần đầu, đoán cấu trúc, rồi dùng `patch` anchor sai → file hỏng.

**Nguyên nhân gốc rễ.** không phải pagination — mà là **đọc nhanh rồi patch luôn** mà không verify rằng content mình đang nhìn vẫn khớp với current state của file. File có thể đã bị agent khác edit giữa chừng.

**Sửa bằng:** Luôn dùng `execute_code` để kiểm tra line numbers chính xác trước khi patch, hoặc read full file (`read_file` với limit lớn) cho file >20KB trước khi edit.

### ❌ LỖI NẶNG — Bỏ update vault indexes sau khi tạo note (tần suất: gần như mọi session)

**Dấu hiệu:** Sau khi `write_file` vào obsidian, agent almost NEVER:
1. Update Vault-MOC.md — note mới không xuất hiện trong master list
2. Update Vault-Quick-Ref.md — navigation bị stale
3. Cross-link với notes related — note mới thành island
4. Git commit — changes bị orphan khỏi version control

**Nguyên nhân:** Tạo note → next task luôn làm việc khác, quên update index vì không có "final validation step" trong workflow.

**Fix phải enforce:** Mỗi workflow obsidian kết thúc phải có: (a) check wikilinks resolve, (b) confirm vault indexes updated, (c) git commit.

### 🟡 LỖI TRUNG BÌNH — Không áp dụng skill `vault-audit` đúng cách (tần suất: khi cần)

**Dấu hiệu:** Khi user yêu cầu "đọc vault" hoặc "kiểm tra obsidian", agent thường chỉ search files rồi copy-paste kết quả, chưa chạy full audit workflow (frontmatter check → orphan detection → link validation).

**Thực tế từ scan 2026-07-02:**
- ✓ 196/197 files có valid frontmatter — tốt
- ✗ 1 file `wiki-schema-versioning-rules.md` bị triple-dash trap — gây frontend parse lỗi vĩnh viễn nếu không sửa
- Cần kiểm tra orphaned links trong Vauc-MOC

### 🟡 LỖI TRUNG BÌNH — Flat-filename convention ở 10-Projects/ không được tôn trọng (tần suất: khi tạo project notes)

**Dấu hiệu:** Skill nói flat-filename trong 10-Projects/, nhưng agent nhiều lần vẫn tạo subdirectories cho các project note. Thực tế từ scan thấy:
- Hoang-Ninh-Ecolife.md ✅ đúng (flat, ở root 10-Projects/)
- Agent-Research-Expansion/project.md ✗ sai (sự kiện là flat file nên name phải là project.md trong folder 10-Projects/, nhưng agent tạo thêm folder wrapper)

## Phần 2: Rút Ra Bài Học — Nguyên Nhân Gốc Rễ

### ROOT CAUSE #1: "Context Window Economy" — bỏ qua step nhỏ vì tiết kiệm tokens
Agent thường tối ưu context window bằng cách: đọc nhanh, làm nhanh, next task. Nhưng dẫn đến thiếu verification -> lỗi phải làm lại tốn nhiều context hơn.

**Học:** Làm chậm ở bước verification để tránh redo costly later.

### ROOT CAUSE #2: Không có "Obsidian Workflow Guardrails"
So với coding (có linter, compiler), obsidian không có compile-time error cho wikilinks broken hay missing frontmatter. Agent tạo ra lỗi rồi chỉ phát hiện khi user báo hoặc search không thấy.

**Học:** Phải tự impose linting rules: sau mỗi file operation, verify metadata + links.

### ROOT CAUSE #3: Path resolution không được cached
Mỗi session phải rediscover vault path. Khi có nhiều "Obsidian" folder (Smee Obsidian/Smee AND Obsidian/Tri kiến Nhân Loại), hay nhầm lẫn source nào đang active.

**Học:** Cache resolved path ở đầu session, dùng một nguồn truth duy nhất.

## Phần 3: Lỗi Ghi Nhớ — Để Không Lặp Lại

### Quan trọng nhất: Vault Path
- **Primary vault:** `C:\Users\Hung\Desktop\Smee Obsidian\Smee` (structure có 10-Projects/, 20-Areas/, etc.)
- **Secondary/renamed:** `C:\Users\Hung\Obsidian\Tri kiến Nhân Loại` (Tiếng soi)
- Khi cần read/list — check cả hai nếu không sure

### Frontmatter Yêu cầu (Điều khoản bảo vệ phần mềm 2)
Tất cả notes phải có: title, slug, category, status, type, date/created
category chỉ được phép: resource | area | knowledge | project | daily | meta

### Mẫu thao tác tập tin
1. Đọc tìm kiếm_ tập tin ho _Grac đọc_ file
2. Write → write_file với frontmatter đầy đủ
3. Edit → patch với verified anchor từ read_file output
4. Verify → kiểm tra tồn tại file + links resolve + indexes reflect change

### Tra ba lần
File nào có `---\n---` ở đầu → frontmatter parser sẽ parse trống → hết fields. Sửa: thêm content giữa cặp --- đầu tiên.

## Phần 4: Tự Nhắc Mình Mỗi Khi Dùng Obsidian

> "Khi dùng obsidian, ALWAYS: (1) resolve path chính xác, (2) read full file trước patch file >5KB, (3) update index/MOC sau write, (4) verify wikilinks resolve, (5) git commit changes."

## Phần 5: Điểm Mạnh Của Vault Cần Phát Huy

- 📊 **Frontmatter quality cao** — 99.5% files có valid frontmatter → dùng search_files filtering by status/category rất hiệu quả
- 📚 **Structure rõ ràng** — Obsidian vault遵循 PARA method (00-Meta, 10-Projects, 20-Areas, 30-Resources, etc.)
- 🔗 **Wikilink ecosystem phong phú** — Concepts, Frameworks, Insights phân loại theo Bac-Giang/domain-specific
- 📝 **Daily notes active** — cron job daily-morning-ritual chạy every day 8:30 AM
- 🧠 **Self-Critique folder đang growth** — cần duy trì pattern này thường xuyên

## Phần 6: Action Items Ngay

1. Sửa `wiki-schema-versioning-rules.md` — loại bỏ vấn đề tiền mặt ba lần ( ít nỗ lực)
2. Liên kết giữa các thiết bị định dạng tập tin
3. Verify current vault path is primary (Smee Obsidian/Smee OR Tri kiến Nhân Loại?)
4. Add obsidian verification guardrails vào agent workflow checklist
