---
title: "Self-Critique — 2026-07-03 17h00"
slug: "self-critique-2026-07-03-17h"
category: knowledge-synthesis
type: insights
status: draft
created: 2026-07-03 17:00
tags: [self-critique, self-improvement, daily-review]
---

## ❌ Lỗi & Vấp phải

| Session | Lỗi | Nguyên nhân gốc (5 Whys) | Bài học |
|---------|-----|-------------------------|--------|
| **14h36** — OCR "Thôi Miên Bằng Ngôn Từ 003" (session 136 msgs) | `NameError: name 'terminal' is not defined` trong execute_code | Why? Script dùng `terminal()` mà không import từ `hermes_tools`. Why? Confuse execute_code sandbox vs direct tool call. Why? Khi cần gọi terminal từ within execute_code, phải `from hermes_tools import terminal`. **Root**: Luôn import hermes_tools khi dùng terminal() bên trong script. | execute_code → `from hermes_tools import terminal` mỗi lần cần terminal call |
| **14h36** — OCR session 1 | Background process exit code 2: `can't open file 'C:\\c\\Users\\Hung\\Desktop\\ocr_thoi_mien.py'` (duyệt path `/c/...` double-cprefixed) | Why? execute_code sandbox chạy lệnh với prefix `/c/` lên Windows path. Why? Script file nằm ở `C:/Users/Hung/Desktop/ocr_thoi_mien.py`, nhưng terminal chạy Python với arg `C:\c\Users\...`. Root: Khi write script tới disk rồi run qua terminal, cần dùng `/c/Users/...` POSIX path, không phải native Windows路径. | Sau write_file → chạy file qua terminal: dùng POSIX path `/c/Users/...` cho git-bash |
| **14h36 + 16h16** — OCR session (2 lần) | PyMuPDF `get_tess_data_dir()` → `AttributeError: no such attribute` (pymupdf v1.28.0) | Why? Attribute này có thể đã bị rename trong version cụ thể. Why? Không kiểm tra API contract trước khi gọi. Root: PyMuPDF 1.28.x có thay đổi API — `get_tess_data_dir()` → thử dùng `pymupdf.get_config()` hoặc check docstring. | Trước invoke PyMuPDF API mới → test inline trước với page count + get_text() |
| **16h16** — OCR session 2 | Path discovery chaos: tồn tại CẢ hai thư mục `41 SÁCH BÁN HÀNG-MARKETING` HOẶC `MARKTING` (không G) — agent đoán mãi mất 10+ tool calls | Why? Có 2 thư mục hơi khác tên → pathlib.glob trả về kết quả sai. Why? Hardcode tên thư mục trong Unicode path → render khác nhau giữa bash và Python sandbox. Root: Dùng `os.walk()` hoặc glob để discover dynamic thay vì hardcode. **Mới**: Có đến 2 dirs khác tên trên cùng máy — MARKETING (correct) vs MARKTING (typo cũ). | Folder Việt + số + dấu: luôn search/dynamic (iterdir/glob), never hardcode name in raw string literal |
| **14h36 + 16h16** — OCR session (2 lần) | `pymupdf4llm.to_markdown()` extract ra 7,727 chars cho 382 trang scanned (chỉ watermark "Sachvui.Com") | Why? pymupdf4llm default không dùng RapidOCR. Why? Không detect OCR fallback path trước khi chạy to_markdown(). Root: Cho tài liệu scans → phải test OCR capability TRƯỚC, dùng RapidOCR page-by-page cho scanned PDFs, không rely vào to_markdown(). | Scanned PDF → check if page.get_text() <50 chars/content → nếu yes → RapidOCR per-page pipeline, NOT pymupdf4llm.to_markdown() |
| **16h16** — OCR session 2 | execute_code sandbox path detection: find extracted file `111KB` ở `/Tri thức Nhân Loại/_extracted_full_text.txt` nhưng sandbox mở thấy `C:/Tri thức Nhân Loại/41 SÁCH BÁN HÀNG-MARKETING/_extracted_full_text.txt` (empty) | Why? 2 sessions OCR khác nhau ghi vào DIFFERENT paths. Why? Không cleanup file name giữa sessions → collision. Root: Mỗi session OCR nên có unique temp filename timestamp-based. | Temp files → prefix `session-<timestamp>_` hoặc unique ID để tránh collision |

## 🔄 Các Pattern Lặp Lại

| Pattern | Xuất hiện | Root Cause |
|---------|-----------|------------|
| **OCR Path Detection** — mất 8-12 tool calls tìm đúng Unicode path | Hôm nay ×2 sessions (14h36, 16h16) | Hardcode tên folder thay vì dynamic discover; `os.listdir()` hoặc iterdir() là phải |
| **execute_code sandbox ≠ terminal** — file tồn tại ở sandbox nhưng không tìm thấy qua terminal và ngược lại | Hôm nay ×2 sessions | execute_code sandbox có filesystem context khác git-bash terminal. Phải dùng SAME method cho cả đọc và ghi. **Không mix**: nếu ghi bằng exec_code → đọc bằng exec_code, không dùng cat/head terminal |
| **RapidOCR kết cấu response** — format `(boxes_and_words,)` hoặc `(boxes, words)` tùy version | Hôm nay ×2 sessions | Không inspect result structure trước khi parse |
| **Background process exit 2 (path prefix)** — Python interpreter找不到file | 14h36 session | Terminal chạy command với `/c/` prefix lên Windows path → `/c/c/Users/...` double-cprefixed |

## ✅ Cái gì HIỆU QUẢ

| Task | Approach | Tại sao hiệu quả? |
|------|----------|------------------|
| PDF open + page count | `pymupdf.open(path)` rồi `doc.page_count` | Nhanh, 1 call confirm được file valid. Nên làm TRƯỚC mọi xử lý khác |
| Scanned detection | Check `page.get_text("text")` length <50 chars → suy ra scanned | Simple heuristic, avoid wasted OCR calls on text-PDFs |
| RapidOCR engine init test | Test 1 page before batch (page 3/index-2) | Avoid losing hours on full-batch khi cấu hình không đúng |
| pathlib discover pattern | `for d in TRI_THUC.iterdir(): if "SÁCH BÁN HÀNG" in str(d)` | Dynamic match với Unicode tên folder — robust hơn hardcode |
| Session reuse (14h36 → 16h16) | Session sau học từ session trước: path `MARKTING` thay vì `MARKETING`, RapidOCR format | Iteration pattern tốt — mỗi lần refine dựa trên findings trước |

## 🚀 Best Practices phát hiện hôm nay

1. **OCR Pipeline Decision Tree** (mới): Scanned PDF >50 pages → RapidOCR per-page via execute_code script (write_file → run) với `sys.stdout.reconfigure(line_buffering=True)` cho progress tracking. Text PDF → pymupdf4llm.to_markdown(). Không bao giờ guess — luôn check page 3 get_text() trước.

2. **Path Discovery Rule** (mới): Unicode Vietnamese directory names → ALWAYS use pathlib.Path.iterdir() + filter, NEVER hardcode display name in raw strings. Hardcoded `r"C:\...MARKETING\..."` fail nếu tên folder typo khác (`MARKTNG` vs `MARKTING`).

3. **Sandbox Consistency Rule** (mới): Ghi bằng execute_code → đọc bằng execute_code. Dùng terminal khi chạy CLI tools, dùng execute_code cho Python file ops. Không mix 2 contexts cùng thao tác trên 1 file.

4. **RapidOCR Result Inspection Rule**: Luôn `print(type(result), len(result))` trước khi unpack — RapidOCR API format thay đổi theo version.

## 📋 Hành động sửa ngay / TODO

- [ ] Test pymupdf.get_tess_data_dir() hoặc fallback path trong PyMuPDF 1.28.x
- [ ] Cleanup temp OCR scripts: `ocr_thoi_mien.py`, các file `oCr_v*.py` cũ trong thư mục books
- [ ] Tạo một single RapidOCR pipeline script cho scanned PDFs (300+ pages) với progress bar → test xong rồi pin làm skill
- [ ] Thêm path discovery logic vào pdf-knowledge-absorption skill references

---
*Auto-generated by Hermes Agent — 17h00 Daily Review on 2026-07-03*
