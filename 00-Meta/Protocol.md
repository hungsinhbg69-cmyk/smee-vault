---
title: "Giao thức Kho lưu trữ — Quản trị + Quy tắc Tác nhân"
slug: "vault-protocol"
category: meta
tags: [meta, governance, agent]
status: active
type: reference
created: 2026-06-12
last_updated: 2026-07-14
---

# 📜 Giao thức Kho lưu trữ — Quản trị + Quy tắc Tác nhân

> Hợp nhất của Quản trị Kho lưu trữ + Quy tắc Vận hành Tác nhân (2026-06-15). Loại bỏ sự trùng lặp từ cấu hình hai tệp ban đầu.

## 1. Quy ước Đặt tên

### Tên Tệp
- **Dự án:** `TenDuAn.md` — KHÔNG có hậu tố như "ghi chú" hoặc "doc"
- **Tệp có ngày tháng:** `YYYY-MM-DD-MoTa.md` — Ngày theo chuẩn ISO để sắp xếp theo thời gian
- **Ghi chú nguyên tử (Atomic notes):** `kebab-case-slug.md` — chữ thường, chỉ dùng dấu gạch ngang
- **Họp hành:** `YYYY-MM-DD-TenCuocHop.md`

### Slug
- kebab-case: `facebook-ad-optimization` thay vì `Facebook Ad Optimization`
- Không có dấu gạch dưới, không có ký tự đặc biệt
- Nhất quán trên hệ thống tệp Linux/macOS

## 2. Quy tắc Frontmatter

**Mọi ghi chú PHẢI có:**
```yaml
---
title: "Tiêu đề chính xác"
slug: "exact-title-slug"
category: meta | inbox | daily | project | area | resource | knowledge | review | archive | output | training
tags: [tag1, tag2]  # tối đa 5
status: draft | active | in-progress | completed | reference | output | archived | superseded | blocked
type: atomic-note | insight | meeting | project | literature-note | reference | review | output | exercise | report | log | evidence
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

## 3. Quy tắc Thư mục

| Quy tắc | Chi tiết |
|---------|----------|
| Số tiền tố (Prefix numbers) | 00-99 để sắp xếp, khoảng cách 10 để mở rộng |
| Không có thư mục theo chủ đề | Sử dụng thẻ cho chủ đề, thư mục cho loại ghi chú |
| Định tuyến tệp đính kèm | Mặc định vào `00-Meta/Attachments/`. Các gói bằng chứng có thể giữ tệp trong thư mục `Sources/` cục bộ của dự án, và phương tiện đầu ra có thể ở bên cạnh kết quả đầu ra. Mọi tệp đính kèm đều phải được tham chiếu. |
| Mẫu trong `_templates/` | Tiền tố dấu gạch dưới để sắp xếp lên trên cùng |

## 4. Quy trình Thu thập

### Thu thập (Inbox)
- Thu thập thô với ít ma sát nhất
- Ghi chú hàng ngày = hộp thư đến nhanh cho những suy nghĩ thoáng qua
- Cắt dán web, highlight → Inbox trước
- **KHÔNG tổ chức trong quá trình thu thập**

### Kết nối (Kiểm tra hàng tuần)
- Rỗng inbox → di chuyển/phân loại tất cả mục
- Liên kết ghi chú với MOC hiện có hoặc lưu trữ nếu ngữ cảnh đã chết
- Nâng cấp ý tưởng hàng ngày giá trị cao → ghi chú nguyên tử
- Liên kết ngược mọi ghi chú mới ngay lập tức

### Quyết định (Kiểm tra dự án)
- Mọi ghi chú dự án đều trả lời: "Tiếp theo sẽ xảy ra gì?"
- Quy trình nghiên cứu: thu thập → trích xuất → gắn thẻ → nâng cấp các điểm đã xác minh
- Dòng chảy từ cuộc họp sang đầu ra: thu thập → quyết định → hiểu biết → bản nháp

### Giao hàng (Outputs)
- Phương pháp lấy bằng chứng trước: tập hợp tham chiếu liên kết → trích xuất tuyên bố → viết nháp → xác minh
- Lưu trữ phiên bản sẵn sàng giao hàng trong `70-Outputs/`
- Giữ nguyên các liên kết nguồn đính kèm

## 5. Quy tắc Thu thập Tác nhân (Agent)

Khi Hùng chia sẻ hiểu biết, quyết định hoặc bài học:

1. **Xác định loại** → khớp với cấu trúc thư mục
2. **Tạo ghi chú** → sử dụng mẫu phù hợp từ `_templates/`
3. **Thêm frontmatter** → luôn hiện diện
4. **Liên kết hai chiều** → kết nối với ít nhất 1 ghi chú hiện có
5. **Ghi lại thu thập** → thêm vào ghi chú hàng ngày kèm thời gian

### Trong các cuộc trò chuyện
- Tối đa 3 lần thu thập mới mỗi phiên trừ khi người dùng yêu cầu rõ ràng hơn
- Mọi ghi chú mới đều được liên kết trong cùng một ngày (không có nội dung bị bỏ rơi)
- Ghi lại trong ghi chú hàng ngày: `[HH:MM] capture: "<chủ đề>" → created <đường dẫn>`

### Vòng đời Phiên làm việc
- **Bắt đầu:** Đọc `02-Daily/YYYY-MM-DD.md` → quét các dự án đang hoạt động → tải ngữ cảnh miền
- **Kết thúc:** Ghi lại thu thập → tạo ghi chú nguyên tử → cập nhật dự án → xác minh liên kết ngược
- **Hàng tuần (Chủ Nhật 20h):** Rỗng inbox → liên kết nội dung bị bỏ rơi → xác minh hành động tiếp theo của dự án → lưu trữ các mục đã chết

## 6. Tiêu chuẩn Chất lượng

### Phải có
- ✅ Frontmatter trên mọi ghi chú
- ✅ Ít nhất 1 liên kết ngược cho mỗi ghi chú mới
- ✅ Slug dạng kebab-case
- ✅ Trường status chính xác
- ✅ Ngày cập nhật cuối cùng hiện tại

### Quy tắc Ghi chú Nguyên tử (Atomic Note)
- Một ý tưởng một ghi chú — nếu >2 chủ đề → tách ra
- Mục tiêu 300-700 từ — ngắn = có thể tái sử dụng, liên kết được
- Nâng cấp từ ghi chú hàng ngày khi được trích dẫn 2+ lần
- Dòng chảy status: draft (nháp) → active (hoạt động - khi liên kết ≥3+) → superseded (bị thay thế - khi đã cập nhật)

## 7. Lịch trình Bảo trì

| Tần suất | Nhiệm vụ | Người sở hữu |
|----------|----------|--------------|
| Hàng ngày | Ghi lại thu thập vào ghi chú hàng ngày | Smee + Hùng |
| Hàng tuần (Chủ Nhật 20h) | Rỗng inbox, liên kết nội dung bị bỏ rơi, cập nhật dự án | Smee |
| Hàng tháng | Dọn dẹp thẻ, kiểm tra liên kết hỏng | Smee |
| Hàng quý | Lưu trữ các mục cũ, xem xét cấu trúc, danh mục plugin | Smee + Hùng |

## 8. Chính sách Lưu trữ (Archive)

Di chuyển vào `60-Archive/` khi:
- Dự án hoàn thành (tiến độ = 100%)
- Ghi chú không hoạt động >1 năm
- Bị thay thế bởi phiên bản mới hơn
- Không còn ý nghĩa thực thi

## 9. Lớp Giao tiếp Tác nhân (Agent)

### `%% double percent comments %%`
Không hiển thị trong chế độ đọc. AI đọc markdown thô. Sử dụng cho:
- Hướng dẫn cố định
- Ghi chú sửa đổi
- Cờ ngữ cảnh để định tuyến tác nhân

### `<!-- HTML comments -->`
Chỉ thị cấu trúc. Sử dụng cho:
- "Được quét ĐẦU TIÊN bởi lập kế hoạch hàng ngày"
- Dấu hiệu ưu tiên
- Gợi ý định tuyến phần

## 10. Mô hình Lấy lại Hiệu quả Token (Token-Efficient Retrieval)

### Bước 1: Quét Hub Tham khảo Nhanh (~3K tokens)
```
Đọc: 00-Meta/Vault-Quick-Ref.md → điều hướng chính theo miền
  → Nhảy trực tiếp đến tệp cụ thể cho nhiệm vụ
```

### Bước 2: Theo dõi Liên kết để Tăng độ sâu
Khi một dự án hoặc khái niệm được tham chiếu → đọc ghi chú cụ thể đó
→ Thông tin giống nhau, chi phí token 5% so với quét kho lưu trữ đầy đủ

## 11. Tóm tắt Phân loại Thẻ (Tag Taxonomy)

| Tiền tố | Mục đích | Ví dụ |
|---------|----------|-------|
| `#project/` | Dự án đang hoạt động | `#project/Facebook-Marketing` |
| `#area/` | Trách nhiệm đang diễn ra | `#area/Marketing` |
| `#Status/` | Vòng đời ghi chú | `#Status/draft`, `#Status/active` |
| `#Type/` | Phân loại nội dung | `#Type/atomic-note`, `#Type/insight` |
| `#Concept/` | Thẻ chủ đề (tạo khi cần) | `#Concept/marketing-automation` |
| `#Tool/` | Công cụ và nền tảng | `#Tool/Obsidian` |
| `#Method/` | Kỹ thuật và phương pháp tiếp cận | `#Method/capture-first` |

**Quy tắc:** Tối đa 5 thẻ/ghi chú. Thẻ là chữ thường và có dấu gạch ngang; `/` được dành riêng cho phân cấp ổn định. Định nghĩa thẻ trong `Tag-Taxonomy.md` trước lần sử dụng đầu tiên, và hợp nhất các biệt danh trong kiểm tra hàng quý. Không có mục tiêu phá hủy toàn kho lưu trữ về số lượng thẻ.


## 12. Quy tắc Tích hợp OpenClaw + Hermes

### Nguyên lý Cốt lõi
Tệp `AGENTS.md` ở gốc vault là nguồn luật vận hành chung. OpenClaw phụ trách điều phối dài hạn, cổng, kênh, nhịp tim/cron và bộ nhớ không gian làm việc; Hermes phụ trách các tác vụ tương tác, nghiên cứu và sử dụng công cụ theo phiên. Cả hai đều dùng cùng schema, cây thư mục và cổng chất lượng.

### Quy ước Đường dẫn Tệp Công cụ
- **Gốc vault** cho gọi công cụ: `C:/Users/Hung/Desktop/Smee Obsidian/Smee` (dấu gạch chéo thuận)
- `read_file`, `write_file`, `patch` sử dụng đường dẫn gốc này
- Khi dùng `execute_code`, Python sử dụng đường dẫn Windows thô (`r"C:\..."`)
- **Tuyệt đối** không sử dụng biến shell như `$OBSIDIAN_VAULT_PATH` trong các cuộc gọi công cụ

### Vòng đời Phiên Tác nhân (Agent Session)
#### Bắt đầu phiên
1. Đọc `AGENTS.md` gốc và `00-Meta/Vault-Quick-Ref.md`
2. Kiểm tra `git status --short` và bảo tồn công việc hiện có
3. Chỉ đọc ghi chú hàng ngày của hôm nay khi sự liên tục phiên làm việc là cần thiết
4. Tải 2–3 ghi chú cụ thể cho nhiệm vụ từ `Vault-MOC`; không quét toàn bộ vault theo mặc định

#### Trong Phiên
1. **Định tuyến theo độ trưởng thành:** thu thập chưa chắc chắn/thô vào `01-Inbox/`; nội dung bền vững đi trực tiếp đến lớp đúng của nó
   - Nghiên cứu web/dữ liệu → `30-Resources/<domain>/` với thẻ phù hợp
   - Hiểu biết/tổng hợp → `40-Knowledge-Synthesis/Insights/` với wikilinks
   - Công việc dự án → `10-Projects/<ProjectName>/` 
2. **Luôn tạo wikilink đi ra** đến các ghi chú liên quan hiện có (giai đoạn kết nối)
3. **Luôn tạo liên kết ngược đi vào** từ nội dung mới khi phù hợp
4. **Ghi nhật ký hàng ngày:** thêm thu thập, quyết định, đầu ra và thay đổi cấu trúc có ý nghĩa; không ghi lại mọi lần đọc/tìm kiếm
5. **Tối đa 3 lần thu thập mỗi phiên** trừ khi người dùng yêu cầu rõ ràng hơn
6. **Không có ghi chú bị bỏ rơi:** mọi ghi chú mới PHẢI có ≥1 wikilink đến nội dung vault hiện có

#### Kết thúc Phiên
1. Thêm nhật ký hàng ngày ngắn gọn chỉ khi phiên tạo ra thay đổi vault có ý nghĩa
2. Xác minh các ghi chú được tạo/sửa đổi vượt qua kiểm tra chất lượng Protocol (Mục 6)
3. Tạo nhiệm vụ tiếp theo trong dự án/ghi chú hàng ngày phù hợp theo task-system-config.md
4. Chạy kiểm tra liên kết/mã hóa/khoảng cách; commit hoặc push chỉ khi Hùng yêu cầu

### Quy tắc Gắn thẻ cho Tác nhân
- Tác nhân tạo thẻ từ phân cấp `Tag-Taxonomy.md` — không bao giờ phát minh thẻ mới
- Mục nhập taxonomy mới → thêm vào phần liên quan trong Tag-Taxonomy.md TRƯỚC lần sử dụng đầu tiên
- Ngữ cảnh cụ thể phiên: TUYỆT ĐỐI không tạo thẻ `#session/*` hoặc `#hermes/*` (không thể thực thi)
- Sử dụng công cụ tác nhân: ghi lại trong `_templates/template-agent-session-log.md`, không dựa trên thẻ

### Cổng Chất lượng (Section 6 + Mục này)
Khi tác nhân tạo bất kỳ ghi chú nào, xác minh:
- [ ] Frontmatter đầy đủ và chính xác
- [ ] Slug sử dụng kebab-case khớp với Mục 1 của Protocol
- [ ] ≤5 thẻ từ taxonomy hiện có
- [ ] ≥1 wikilink đi ra được tạo
- [ ] Ghi chú hàng ngày đã cập nhật với nhật ký thu thập

---
*Phiên bản Protocol: 2.4 (cập nhật 2026-07-14 — danh mục căn chỉnh đường dẫn, trạng thái vòng đời, ngoại lệ tệp đính kèm và chính sách taxonomy không phá hủy)*
*Thay thế: Vault-Governance.md + Agent-Operating-Protocol.md*
---
