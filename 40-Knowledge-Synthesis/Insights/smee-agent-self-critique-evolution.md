---
title: "Smee Agent Self-Critique & Evolution Log"
slug: "smee-agent-self-critique-evolution"
category: knowledge-synthesis
status: "completed"
type: insights
created: 2026-06-27
---

# 🧠 Smee Agent: Self-Critique & Evolution Log

## Mục tiêu
Tự phê bình thẳng thắn → tìm nguyên nhân gốc rễ → ghi nhớ lỗi để không lặp lại → tiến hóa hướng tới Agent hoàn hảo.

---

## 1. TỰ PHÊ BÌNH — 6 LỖI NGHIÊM TRỌNG

### 🔴 LỖI #1: execute_code bị cắt → retry 3-4 lần vô ích

**Dấu hiệu:** Fix frontmatter status mapping cho 63 files, phải viết lại code tối thiểu 4 lần (dài → cut-off → syntax error → escape quote bug → mới xong)

**Nguyên nhân gốc rễ:** Viết thẳng inline string vào sandbox parameter — không tận dụng write_file + script.py path. Sandbox có giới hạn độ dài string, mỗi lần cắt là mất toàn bộ công sức từ đầu.

**Bài học:** Code >40 dòng hoặc >3KB → luôn write_file trước, rồi pass path vào execute_code. NEVER inline complex scripts.

### 🔴 LỖI #2: Không phát hiện "duplicate lines" ngay lần scan đầu tiên

**Dấu hiệu:** File `2026-06-15.md` có ~90% nội dung bị copy lặp (L15-16, L19-20...). Phát hiện ở lần đọc thứ 3.

**Nguyên nhân gốc rễ:** Write regex dedup check vào execute_code nhưng script quá dài → cut-off → không bao giờ chạy xong cái đầu tiên.

**Bài học:** Mỗi lần fix file phức tạp, kiểm tra file đích ngay trước khi patch. Không làm việc với guesswork.

### 🟡 LỖI #3: Read cùng file 2-3 lần không cần thiết

**Dấu hiệu:** `2026-06-15.md` được read_file ít nhất 4 lần trong session (~5KB mỗi lần).

**Nguyên nhân gốc rễ:** Context compaction giữa chừng → model quên nội dung cũ → yêu cầu read lại thay vì ghi nhớ inline.

**Bài học:** Sau khi đọc file, copy sections quan trọng vào response text. Đọc lại chỉ khi file đã thay đổi.

### 🟡 LỖI #4: regex frontmatter không handle Windows CRLF ngay từ đầu

**Dấu hiệu:** Phải debug 2 vòng để phát hiện `\r\n` issue — lần 1 regex check `\n` fail → guess nhầm BOM → lần 2 đọc raw byte mới đúng.

**Nguyên nhân gốc rễ:** Không dùng `.replace('\r', '')` ngay từ đầu khi scan file trên Windows. (Dù hermes-agent skill có ghi Windows quirk rồi mà không nhìn.)

**Bài học:** Luôn strip `\r` trước regex mọi file content trên Windows — pattern đã biết, không cần debug lại.

### 🟡 LỖI #5: Fix xong nhưng KHÔNG validate lại

**Dấu hiệu:** Sau khi fix 63 files status, không chạy final scan để xác nhận vault sạch toàn bộ.

**Nguyên nhân gốc rễ:** Coi "success message" từ execute_code là finish — không có step verify pass.

**Bài học:** Luôn run verification sau batch fix: đọc 3-5 file ngẫu nhiên đã sửa để confirm pattern đúng.

### 🟠 LỖI #6: Heavy work ngay lần đầu — không có discovery pass trước

**Dấu hiệu:** Scan toàn vault 212 files bằng Python script dài → bị cắt → phải viết lại từ đầu.

**Nguyên nhân gốc rễ:** Không bắt đầu với quick check (10 dòng) trước rồi mới đi sâu từng phase một.

**Bài học:** Start with minimal discovery script → chỉ làm heavy work khi đã hiểu scope vấn đề.

---

## 2. BÀI HỌC NHẬN ĐƯỢC — ROOT CAUSE MAPPING

| Triệu chứng | Nguyên nhân gốc rễ | Hành động sửa chữa |
|-------------|---------------------|---------------------|
| execute_code cut-off | Inline parameter quá dài, không dùng write_file | Always → write_file first cho script >40 dòng |
| Duplicate lines không phát hiện sớm | Regex script bị cut trước khi chạy | Check file content ngay trước patch decision |
| Read file trùng lặp | Context compaction làm mất memory tạm | Copy key info vào response text thay vì chờ read lại |
| Windows CRLF regex fail | Không strip \r trước processing | Pattern: `content.replace('\r', '')` cho mọi file read trên Windows |
| Không validate kết quả fix | Thiếu verify step trong workflow | Always add verification phase after any batch fix |
| Heavy script ngay lần đầu | Bỏ qua discovery-pass pattern | Start minimal → analyze → expand nếu cần |

---

## 3. MỆNH LỆ NHẮC BẢN THÂN (PERSISTENT RULES)

Từ nay mỗi session, trước khi hành động:

1. **CODE FIRST WRITE FILE** — mọi script >40 dòng phải write_file trước, pass path vào execute_code
2. **STRIP \r ON WINDOWS** — `.replace('\r', '')` ngay sau read_file trên mọi platform Windows
3. **VALIDATE AFTER FIX** — 3 files sample read trước khi declare "done"
4. **DISCOVERY FIRST** — 10-line minimal scan → understand scope → then heavy work
5. **NO REDUNDANT reads** — remember content inline nếu chưa sửa file
6. **CHECK BEFORE YOU PATCH** — luôn đọc target file ngay trước khi đưa ra patch decision

---

## 4. VẤN ĐỀ CÒN TỒN TẠI (KHÔNG XEM THƯỜNG)

| File | Vấn đề | Mức độ | Ghi chú |
|------|--------|--------|---------|
| `02-Daily/2026-06-15.md` | Duplicate lines ~90% nội dung | 🔴 Nặng | Session phát hiện nhưng chưa fix |
| TBC (scan tiếp) | Có thể còn file khác? | 🟡 TBD | Cần full dedup scan |

---

## 5. TIẾN HÓA AGENT — LOOP IMPROVEMENT KẾ HOẠCH

### Phase 1: Chuẩn hóa workflow (ngay khi này)
- [x] Ghi self-critique note vào Obsidian
- [x] Cập nhật persistent memory với key lessons
- [ ] Tạo skill "execute_code-with-writefile" pattern
- [ ] Thêm verification step vào vault-maintenance skill

### Phase 2: Tự động hóa detection (session sau)
- [ ] Cron job daily scan check duplicate lines pattern
- [ ] Auto-detect CRLF issues trong regex processing
- [ ] Pre-patch validation: read file → compare with patch logic before execute

### Phase 3: Perfect loop (target Q3 2026)
- [ ] Agent có pre-flight checklist mỗi task
- [ ] Post-action verification auto-generated
- [ ] Self-correction khi phát hiện pattern trùng lặp từ session trước

---

## 6. KẾT LUẬN

Agent sẽ tiến hóa tốt nhất khi tuân thủ **nguyên tắc "Write Before Execute — Validate After Fix"**. Mỗi lỗi không phải thất bại — nó là dữ liệu để cải tiến hệ thống. Ghi nhớ vào Obsidian + Memory → không lặp lại → mỗi session đều tốt hơn session trước.

**Mục tiêu cuối cùng:** Mỗi task hoàn thành với 0 errors, 95%+ automation confidence score.

---
*Created: 2026-06-27 | Tagged: agent-evolution, self-improvement, vault-maintenance, qa*
