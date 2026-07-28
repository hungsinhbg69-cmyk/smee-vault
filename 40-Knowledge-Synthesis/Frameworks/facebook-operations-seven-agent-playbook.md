---
title: "Facebook Operations Playbook — Hệ 7 agent"
slug: "facebook-operations-seven-agent-playbook"
category: knowledge
tags:
  - facebook
  - api
  - meta
  - agent-hub
status: active
type: framework
created: 2026-07-15
last_updated: 2026-07-15
owners:
  - Codex
  - Antigravity
execution_mode: supervised
---

# Facebook Operations Playbook — Hệ 7 agent

> [!abstract] Mục tiêu
> Chuẩn bị chuỗi vận hành từ tài khoản Facebook thật → hồ sơ và bảo mật → Page doanh nghiệp → Meta Business Suite → Pages API/Webhooks. Playbook ưu tiên tính bền vững của tài khoản, quyền tối thiểu và khả năng phục hồi thay vì mô phỏng hành vi người dùng để né phát hiện.

## Ranh giới không thương lượng

- Chỉ một tài khoản cá nhân của chính người dùng, sử dụng danh tính xác thực.
- Không tạo hoặc duy trì nhiều tài khoản cá nhân, tài khoản nuôi, danh tính giả hay lịch sử tương tác giả.
- Không tự động hóa signup, CAPTCHA, OTP, checkpoint, xác minh danh tính hoặc khôi phục tài khoản.
- Không yêu cầu người dùng gửi mật khẩu, OTP, recovery code, cookie, session hoặc access token vào chat/Obsidian.
- Không spam, mua/bán tương tác, tự tương tác để tạo tín hiệu giả hoặc điều khiển trình duyệt nhằm giả làm người dùng để né hệ thống.
- Publish, gửi tin, xóa, ban, thay quyền truy cập, chạy quảng cáo và thêm phương thức thanh toán luôn cần cổng chấp thuận phù hợp.

Nguồn chính thức: Facebook yêu cầu tài khoản cá nhân dùng danh tính thật và không duy trì nhiều tài khoản; doanh nghiệp nên được đại diện bằng Page. Xem [chính sách nhiều tài khoản](https://www.facebook.com/help/975828035803295) và [tạo tài khoản](https://www.facebook.com/help/188157731232424/).

## Kiến trúc ba lớp

| Lớp | Công cụ | Phạm vi |
|---|---|---|
| Human-only | Trình duyệt do người dùng kiểm soát | Signup, mật khẩu, OTP, CAPTCHA, checkpoint, giấy tờ, 2FA, xác nhận điều khoản |
| Browser-assisted | Browser/Computer Use có người xác nhận | Điều hướng, điền dữ liệu không nhạy cảm, cấu hình Page, tạo draft, xem Insights |
| API-first | Trang APIĐồ thị API, Webhoooks | Đọc Page, xuất bản đã duyệt, bình luận/tin nhắn trong quyền cho phép, Insights, sự kiện thời gian thực |

## Pha 0 — Hồ sơ đầu vào

Người dùng chuẩn bị riêng, không gửi bí mật vào vault:

- Họ tên dùng trong đời sống hằng ngày.
- Email hoặc số điện thoại do người dùng sở hữu.
- Ngày sinh, giới tính và quốc gia theo thông tin thật.
- Mật khẩu mạnh, trình quản lý mật khẩu và phương thức 2FA.
- Tên pháp lý của doanh nghiệp/thương hiệu, danh mục, bio, website, email, địa chỉ, giờ hoạt động.
- Logo, ảnh bìa, tuyên bố quyền sở hữu thương hiệu và nội dung mẫu.

**Gate P0:** dữ liệu đúng chủ thể; không có yêu cầu tạo persona giả hoặc nhiều tài khoản.

## Pha 1 — Tạo tài khoản cá nhân

1. Người dùng tự mở trang đăng ký Facebook.
2. Người dùng tự nhập tên, email/số điện thoại, mật khẩu, ngày sinh và giới tính.
3. Người dùng tự xử lý CAPTCHA/checkpoint và xác nhận email hoặc số điện thoại.
4. Agent chỉ được hướng dẫn hoặc điều hướng tới trường cần điền; không đọc/lưu bí mật.

**Gate P1:** đăng nhập thành công; email/điện thoại đã xác nhận; không có checkpoint tồn đọng.

## Pha 2 — Bảo mật và hồ sơ

1. Bật 2FA; lưu recovery code trong trình quản lý bí mật của người dùng, không phải Obsidian.
2. Kiểm tra phiên đăng nhập, email/số điện thoại khôi phục và cảnh báo đăng nhập.
3. Điền ảnh đại diện, bio, nơi ở hoặc thông tin công khai theo lựa chọn thật của người dùng.
4. Review quyền riêng tư, tagging, tìm kiếm bằng email/số điện thoại và audience mặc định.
5. Không tạo hàng loạt bài đăng/tương tác để “làm ấm” tài khoản.

**Gate P2:** bảo mật hoàn chỉnh; người dùng duyệt ảnh, bio và mức công khai.

## Pha 3 — Tạo Page hợp lệ

Facebook hướng dẫn Page dành cho doanh nghiệp, thương hiệu, tổ chức và nhân vật công chúng. Người tạo phải có quyền đại diện phù hợp. Xem [tạo Page](https://www.facebook.com/help/104002523024878) và [quản lý Page](https://www.facebook.com/help/135275340210354).

1. Người dùng mở `facebook.com/pages/create` từ tài khoản thật.
2. Nhập tên Page, danh mục và bio; người dùng duyệt trước khi nhấn Create.
3. Thêm logo, ảnh bìa, username, action button, thông tin liên hệ và website.
4. Kết nối Instagram/WhatsApp chỉ khi tài khoản thuộc cùng chủ thể và người dùng xác nhận.
5. Cấp Page access/task access theo nguyên tắc quyền tối thiểu; hạn chế `full control`.

**Gate P3:** Page ID đã ghi nhận; chủ sở hữu và quyền truy cập đã kiểm tra; không có bí mật trong vault.

## Pha 4 — Meta Business Suite trước API

Dùng Meta Business Suite để kiểm tra quy trình thật trước khi tự động hóa:

- Tạo draft, duyệt nội dung, lên lịch và quản lý Content.
- Xử lý Inbox/bình luận có người giám sát.
- Xem Insights và xác lập baseline.
- Phân quyền theo task thay vì chia sẻ thông tin đăng nhập.

Các hành động cần xác nhận ngay trước khi thực hiện:

- Publish hoặc gửi tin ra ngoài.
- Xóa nội dung, ban người dùng, thay quyền Page.
- Kết nối tài khoản, thêm thanh toán, tạo chiến dịch quảng cáo.
- Thay đổi tên, username, danh mục hoặc thông tin pháp lý của Page.

**Gate P4:** một draft và một lịch xuất bản thử được người dùng duyệt; quyền task hoạt động đúng.

## Pha 5 — Meta App và Pages API

Theo [Pages API Overview](https://developers.facebook.com/docs/pages-api/overview), Pages API quản lý cài đặt/nội dung Page bằng Graph API endpoints. Hầu hết endpoints cần Page access token; quyền và feature có thể cần App Review; mọi request chịu rate limit.

Luồng chuẩn:

1. Tạo Meta App đúng use case và ghi nhận App ID; App Secret chỉ ở secret store.
2. Cấu hình Facebook Login hoặc Facebook Login for Business.
3. Người dùng cấp quyền tối thiểu cho Page mình sở hữu/quản lý.
4. Lấy User Access Token qua OAuth; gọi `/me/accounts` để nhận Page ID, Page access token và task.
5. Kiểm tra task cần thiết: `CREATE_CONTENT`, `ANALYZE`, `MODERATE`, `MESSAGING`, `ADVERTISE`, `MANAGE` tùy use case.
6. Với luồng publish cơ bản, tài liệu Get Started hiện liệt kê `pages_manage_metadata`, `pages_manage_posts`, `pages_manage_read_engagement`, `pages_show_list`; phải kiểm tra lại reference/changelog trước triển khai.
7. Chỉ chuyển App sang Live/Advanced Access sau khi App Review và kiểm thử Development Mode đạt.
8. Theo dõi rate-limit headers, expiry và lỗi quyền; không retry vô hạn.

> [!warning] Test Users
> Trang chính thức hiện thông báo tạm ngừng khả năng tạo test user mới. Test user hiện có chỉ dùng để kiểm thử app, không được chuyển thành người dùng thật và không được tương tác với người dùng thật ngoài phạm vi role/test cho phép. Xem [Meta Test Users](https://developers.facebook.com/docs/development/build-and-test/test-users).

**Gate P5:** read-only API call thành công; token không xuất hiện trong log/vault; scope/task khớp use case; version API được ghim rõ.

## Pha 6 — Tự động hóa tăng dần

Thứ tự mở quyền:

1. Đọc Page và Insights.
2. Nhận Webhooks vào staging.
3. Tạo draft nội bộ; người dùng publish thủ công.
4. Publish qua API với nội dung đã duyệt và idempotency key nội bộ.
5. Phản hồi bình luận/tin nhắn theo rule rõ ràng, rate limit và escalation.
6. Chỉ sau lịch sử ổn định mới cân nhắc moderation hoặc quảng cáo.

Mỗi action ghi: `actor`, `page_id`, `action`, `object_id`, `approval`, `timestamp`, `result`, `error_code`; không ghi raw token hay nội dung riêng tư không cần thiết.

## Ma trận chấp thuận

| Hành động | Agent có thể chuẩn bị | Ai xác nhận | Tự động thực hiện |
|---|---|---|---|
| Điền thông tin signup không nhạy cảm | Có | Người dùng | Không |
| Mật khẩu, OTP, CAPTCHA, checkpoint | Không | Người dùng | Không |
| Cập nhật bio/ảnh hồ sơ | Có | Người dùng | Sau xác nhận từng thay đổi |
| Tạo Page | Có | Người dùng | Không ở lần đầu |
| Tạo draft Page | Có | Người dùng/biên tập | Có |
| Publish bài | Có | Chủ Page | Chỉ sau policy phê duyệt |
| Trả lời tin nhắn/bình luận | Có | Rule + escalation | Có trong phạm vi duyệt |
| Xóa/ban/thay quyền | Có thể đề xuất | Chủ Page | Không mặc định |
| Ads/thanh toán | Có thể chuẩn bị | Chủ tài khoản | Không mặc định |

## Phân vai hệ 7 agent

- **Codex:** captain, schema, acceptance gate, safety và final review.
- **Antigravity:** deputy, chia pha, theo dõi gate và hợp nhất bằng chứng.
- **OpenClaw:** gateway, webhook, lịch chạy, retry, cảnh báo và vận hành dài hạn.
- **Hermes:** review quyền/token, phản biện nội dung và kiểm tra compliance.
- **Goose:** workflow từng bước, checkpoint và rollback.
- **Open Interpreter:** thao tác máy có giám sát; dừng tại mật khẩu/OTP/CAPTCHA/publish.
- **Aider:** code client Pages API, validation, test, logging và idempotency.

## Điều kiện dừng khẩn cấp

Dừng toàn bộ khi có checkpoint, cảnh báo đăng nhập, yêu cầu giấy tờ, quyền bị thu hồi, token xuất hiện trong log, lỗi rate limit lặp lại, Page ownership không rõ, nội dung chưa được duyệt hoặc yêu cầu tạo tương tác giả.

## Checklist trước nhiệm vụ đầu tiên

- [ ] Xác nhận đây là tài khoản duy nhất của người dùng.
- [ ] Chuẩn bị email/số điện thoại thật nhưng không gửi bí mật vào chat.
- [ ] Chuẩn bị thông tin Page và tài sản thương hiệu.
- [ ] Chọn hành động nào human-only, browser-assisted và API-first.
- [ ] Chốt approval matrix cho publish, messaging, moderation và ads.
- [ ] Chọn secret store cho App Secret/token.
- [ ] Chốt phiên bản Graph API sau khi kiểm tra changelog.
- [ ] Cấu hình audit log không chứa token/cookie/session.

## Liên kết nội bộ

- [[Facebook Developers — Bản đồ tài liệu]]
- [[Meta-Developer-Platform-Guide]]
- [[fb-graph-api-learning]]
- [[fb-graph-api-quick-ref]]
- [[fb-graph-api-v25-reference]]
- [[agent-integration-framework]]
