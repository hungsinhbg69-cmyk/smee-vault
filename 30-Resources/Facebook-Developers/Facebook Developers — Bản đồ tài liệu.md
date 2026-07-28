---
title: "Facebook Developers — Bản đồ tài liệu"
slug: "facebook-developers-ban-do-tai-lieu"
category: resource
tags:
  - facebook
  - api
  - meta
  - reference
status: active
type: moc
created: 2026-07-15
last_updated: 2026-07-15
source_url: "https://developers.facebook.com/docs/"
source_fetched_at: "2026-07-15T09:48:02.619Z"
source_sha256: "8e87e134a09307cd90376027b00772a0dcf0ebb7210971676ba8f654f0c77b4a"
root_verified_at: "2026-07-15T18:20:52+07:00"
root_verified_sha256: "27269865312afe6e944cb69f06deba6582800b368f65b5ba5307fa04fdf21c33"
full_site_ingested: false
---

# Facebook Developers — Bản đồ tài liệu

> [!success] Kết quả kiểm kê an toàn
> Trang gốc [Meta for Developers](https://developers.facebook.com/docs/) có **47 URL nội bộ duy nhất** trong **16 nhóm catalog**. Lần kiểm tra lại ngày 2026-07-15 vẫn thấy 47 URL. Đây là toàn bộ taxonomy quan sát được từ trang gốc, **không phải toàn bộ nội dung website**.

## Bản đồ học tập đề xuất

1. [[01-nen-tang-va-graph-api|Tài liệu dành cho nhà phát triển trên Meta]] — 1 liên kết
2. [[02-phat-trien-chinh-sach-va-quyen-rieng-tu|Hướng dẫn dành cho nhà phát triển]] — 5 liên kết
3. [[03-xac-thuc-va-dang-nhap|Xác thực]] — 3 liên kết
4. [[04-graph-api|API Đồ thị]] — 1 liên kết
5. [[05-rest-api|Rest API]] — 1 liên kết
6. [[06-tich-hop-ung-dung|Tiện ích tích hợp ứng dụng]] — 4 liên kết
7. [[07-tich-hop-mang-xa-hoi|Tiện ích tích hợp với mạng xã hội]] — 5 liên kết
8. [[08-nhan-tin-doanh-nghiep|Nhắn tin doanh nghiệp]] — 4 liên kết
9. [[09-marketing-va-thuong-mai|Marketing và thương mại]] — 11 liên kết
10. [[10-sdk|SDK]] — 5 liên kết
11. [[11-video|Video]] — 2 liên kết
12. [[12-game|Game]] — 1 liên kết
13. [[13-kha-nang-di-chuyen-du-lieu|Khả năng di chuyển dữ liệu]] — 1 liên kết
14. [[14-nen-tang-co-trach-nhiem|Sáng kiến về nền tảng có trách nhiệm]] — 1 liên kết
15. [[15-mcp|MCP]] — 1 liên kết
16. [[16-meta-admin-center|Công việc và học vấn]] — 1 liên kết

## Phân cấp khái niệm

1. **Nền tảng và quản trị:** phát triển ứng dụng, chính sách, quyền riêng tư, nền tảng có trách nhiệm.
2. **Danh tính và quyền truy cập:** Facebook Login, Limited Login, Login Connect with Messenger.
3. **Lớp dữ liệu và sự kiện:** Graph API, REST API, Webhooks, App Events, Meta Pixel.
4. **Kênh sản phẩm:** Pages, Instagram, Threads, Messenger, WhatsApp, video và game.
5. **Kinh doanh:** Marketing API, Catalog, Commerce, Conversions API và các gateway.
6. **Công cụ triển khai:** SDK, MCP và Meta Admin Center.

> [!warning] Các nhóm có giao nhau
> Một sản phẩm có thể thuộc nhiều lớp. Ví dụ Conversions API vừa là dữ liệu sự kiện vừa phục vụ marketing; Messenger Connect vừa là xác thực vừa là nhắn tin. Vì vậy cấu trúc này dùng wikilink chéo thay vì ép mỗi khái niệm vào một “hộp” duy nhất.

## Lộ trình triển khai thực tế

1. Đọc nền tảng, điều khoản, quyền riêng tư và quy trình App Review.
2. Chọn mô hình xác thực và quyền tối thiểu.
3. Học Graph API, token, versioning, paging, rate limit và error handling.
4. Chọn kênh sản phẩm cần dùng; chỉ đọc SDK/tài liệu tương ứng.
5. Thiết kế Webhooks/App Events/Pixel hoặc Conversions API nếu cần dữ liệu sự kiện.
6. Trước khi production, kiểm tra lại phiên bản API và tài liệu chính thức tại thời điểm triển khai.

## Ghi chú hiện có trong vault

- [[facebook-operations-seven-agent-playbook|Facebook Operations Playbook — Hệ 7 agent]] — khung vận hành từ tài khoản thật đến Page/API.
- [[Meta-Developer-Platform-Guide]] — hướng dẫn tổng hợp đã có.
- [[fb-graph-api-learning]] — ghi chú học Graph API.
- [[fb-graph-api-quick-ref]] — mẫu tham khảo nhanh.
- [[fb-graph-api-v25-reference]] — snapshot tham chiếu v25; cần kiểm tra phiên bản trước khi dùng.
- [[30-Resources/Facebook-Ads/INDEX|Facebook Ads — INDEX]] — MOC quảng cáo Facebook.

## Provenance, giới hạn và cập nhật

- Snapshot catalog: 2026-07-15T09:48:02.619Z; phương pháp `defuddle --md`; SHA-256 `8e87e134a09307cd90376027b00772a0dcf0ebb7210971676ba8f654f0c77b4a`.
- Kiểm tra lại root: 2026-07-15T18:20:52+07:00; SHA-256 `27269865312afe6e944cb69f06deba6582800b368f65b5ba5307fa04fdf21c33`; robots SHA-256 `6f25a24c5aeac50fa1ca285f3fa8e27595b99fc0ff7d87a80726d52c7d20797b`.
- Cờ an toàn: `full_site_ingested: false`.
- Không mở rộng crawl tự động khi chưa có bằng chứng cho phép bằng văn bản từ Meta.
- Khi cập nhật: trích lại riêng trang gốc, chuẩn hóa URL, so diff 47 URL/16 nhóm, rồi review thủ công trước khi sửa ghi chú.

## Trạng thái phân tích sâu 47 trang

> [!todo] Đang chờ nguồn hợp lệ — 0/47
> Hệ 7 agent đã kiểm tra robots.txt, nguồn tải chính thức và các repository GitHub chính thức của Meta. Chưa tìm thấy kho chính thức chứa trọn bộ 47 trang; không agent nào được phép né robots, chống bot, rate limit hoặc điều khoản nền tảng.

- Checklist bàn giao: [[Facebook Developers — Thu thập sâu thủ công]].
- Nguồn chấp nhận: file Markdown/HTML/PDF do người dùng tự export hoặc corpus được Meta cho phép bằng văn bản.
- Khi validator đạt 47/47, OpenClaw và Hermes có thể xử lý song song; Codex nghiệm thu provenance, phân cấp, wikilink và import.

## Nguồn

- [Meta for Developers](https://developers.facebook.com/docs/)
- [robots.txt của developers.facebook.com](https://developers.facebook.com/robots.txt)
