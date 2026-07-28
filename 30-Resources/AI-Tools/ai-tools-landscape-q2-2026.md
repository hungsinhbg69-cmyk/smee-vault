---
title: "Bản đồ công cụ AI Q2/2026"
slug: "ai-tools-landscape-q2-2026"
category: resource
tags: [vault-maintenance]
status: "draft"
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---

---

# Bản đồ công cụ AI Q2/2026

> Tổng hợp và phân tích các công cụ AI nổi bật trong quý 2 năm 2026, tập trung vào marketing stack của Hùng.

## Tóm tắt điều hành (Executive Summary)

Quý 2/2026: Các công cụ AI đã chuyển từ "thử nghiệm" → "sẵn sàng cho sản xuất". Xu hướng chính:
1. **Đa phương thức là mặc định** — văn bản/hình ảnh/video/audio trong cùng một mô hình
2. **Vòng lặp tác nhân (Agent loops)** — công cụ không chỉ tạo sinh nội dung, mà tự động thực thi quy trình làm việc
3. **AI trên thiết bị/cục bộ** — ưu tiên quyền riêng tư, chạy ngoại tuyến (hệ sinh thái Ollama phát triển mạnh)
4. **AI chuyên ngành (Vertical AI)** — các công cụ chuyên sâu cho từng lĩnh vực (luật pháp, y tế, bất động sản) thay vì các mô hình tổng quát

## Lớp Mô hình — Các LLM cốt lõi

### 1. OpenAI GPT-4o / GPT-5 (xem thử GPT-5)
- **Giá:** $8/tháng (Plus), $200/tháng (Pro)
- **Điểm mạnh:** Hỗ trợ đa phương thức từ gốc, tích hợp Sora 2 (tạo video), hệ sinh thái plugin
- **Ứng dụng marketing:** Tạo nội dung, phân tích tài liệu, nghiên cứu khách hàng
- **Điểm yếu:** Giới hạn tốc độ trên gói miễn phí, thiên về dữ liệu thị trường Mỹ
- **Đối với Hùng:** ChatGPT + GPT-5 là công cụ cốt lõi cho việc lên ý tưởng nội dung và phân tích tài liệu

### 2. Xa cổ động Claude (Opus/ Sonnet)
- **Giá:** $17/tháng+, Opus cao hơn nhiều
- **Điểm mạnh:** Độ chính xác lập trình cao nhất, logic suy luận tốt, Claude Cowork (tự động hóa trên máy tính để bàn)
- **Ứng dụng marketing:** Tạo mã nguồn (kỹ năng OpenClaw), phân tích dữ liệu, đầu ra có cấu trúc
- **Điểm yếu:** Giá cao so với các lựa chọn thay thế khác
- **Đối với Hùng:** Claude Sonnet > GPT-4o cho các tác vụ lập trình. Claude 4 Opus đáng giá nếu ngân sách cho phép

### 3. Google Song tử (Pro/Utra + Deep Research)
- **Giá:** $7.99/tháng+, tính năng Deep Research trả phí
- **Điểm mạnh:** Cửa sổ ngữ cảnh lớn, nghiên cứu tự động Deep Research, tạo ảnh Nano Banana, Tổng quan âm thanh (Audio Overview)
- **Ứng dụng marketing:** Tổng hợp nghiên cứu, phân tích thị trường, tái sử dụng nội dung (tóm tắt dạng âm thanh)
- **Điểm yếu:** Bị khóa trong hệ sinh thái Google products
- **Đối với Hùng:** Gemini Deep Research = đối thủ cạnh tranh cho NotebookLM. Dùng để nghiên cứu các thị trường ngách

### 4. Các mô hình mã nguồn mở cục bộ (Hệ sinh thái Ollama)
- **Mô hình:** Qwen 3, Llama 4, Mixtral, các biến thể Gemma
- **Giá:** Miễn phí (cục bộ), chi phí suy luận ≈ $0
- **Điểm mạnh:** Quyền riêng tư, không giới hạn tốc độ, có thể tùy chỉnh và tinh chỉnh
- **Ứng dụng marketing:** Các hoạt động tác nhân hàng ngày (OpenClaw chạy trên Ollama)
- **Đối với Hùng:** Cấu hình hiện tại `mixi/fredrezones55-qwen36-aggressive-stable:latest` là lựa chọn vững chắc. Cân nhắc chuyển sang Qwen 3 Turbo khi có sẵn

## Tạo video AI — Kho báu vàng cho marketing

### 5. Google Veo 3
- **Giá:** Gói miễn phí, trả phí $19.99/tháng+
- **Điểm mạnh:** Chất lượng điện ảnh, chuyển động máy ảnh mượt mà, chuyển động tự nhiên, âm thanh đồng bộ
- **Ứng dụng marketing:** Quảng cáo sản phẩm, teaser mạng xã hội, hình ảnh thương hiệu, các cảnh theo cảm xúc
- **Đối với Hùng:** Veo 3 > Sora 2 cho video sản phẩm thực tế. Tích hợp với Synthesia

### 6. OpenAI Sora 2
- **Điểm mạnh:** Câu chuyện có cốt truyện, đoạn phim điện ảnh
- **Ứng dụng marketing:** Kể chuyện thương hiệu, video chiến dịch
- **Điểm yếu:** Ít kiểm soát hơn đối với các cảnh cụ thể so với Veo

### 7. Higgsfield AI
- **Giá:** $9/tháng (không có gói miễn phí)
- **Điểm mạnh:** Tất cả trong một (hình ảnh + video), thử nghiệm đa mô hình, nội dung thịnh hành cộng đồng
- **Ứng dụng marketing:** Lặp lại ý tưởng sáng tạo, kiểm tra A/B nhanh các sáng tạo quảng cáo
- **Đối với Hùng:** Tốt nhất cho việc kiểm tra sáng tạo nhanh. Tạo ảnh không giới hạn + quy trình pipeline video

### 8. Synthesia
- **Giá:** Gói miễn phí, $18/tháng+
- **Điểm mạnh:** Avatars AI (người dẫn chương trình ảo), Video Agents (tương tác), tích hợp Veo 3 + Sora 2
- **Ứng dụng marketing:** Video đào tạo, giải thích sản phẩm, nội dung đa ngôn ngữ, demo tương tác
- **Đối với Hùng:** Video Agents = bước ngoặt cho các tour tham quan bất động sản

## Âm thanh và giọng nói AI

### 9. ElevenLabs
- **Giá:** $5-$99/tháng
- **Điểm mạnh:** Giọng nói thực tế nhất, sao chép giọng nói, Voice Agents (bot hội thoại), đa ngôn ngữ
- **Ứng dụng marketing:** Đọc sách podcast, lồng tiếng YouTube, bot hỗ trợ khách hàng, lồng tiếng quảng cáo
- **Đối với Hùng:** Voice Agents cho Facebook Messenger/Telegram trả lời tự động. Sao chép giọng thương hiệu

### 10. Google Google
- **Giá:** Miễn phí bên trong Gemini
- **Điểm mạnh:** Tóm tắt phong cách podcast từ tài liệu
- **Ứng dụng marketing:** Tái sử dụng nội dung, học nhanh khi di chuyển

## Nghiên cứu và Quản lý tri thức

### 11. NotebookLM (Google)
- **Giá:** Miễn phí, $8.99/tháng+
- **Điểm mạnh:** Hỏi đáp tài liệu, tóm tắt âm thanh, tạo cơ sở kiến thức
- **Ứng dụng marketing:** Tổng hợp nghiên cứu thị trường, phân tích đối thủ, lên kế hoạch nội dung
- **Đối với Hùng:** Tải báo cáo thị trường Bac Giang → nhận thông tin tức thì. Tóm tắt âm thanh cho quãng đường di chuyển

### 12 Song Tử nghiên cứu sâu
- **Giá:** Tính năng trả phí bên trong Gemini
- **Điểm mạnh:** Nghiên cứu đa bước tự động, báo cáo tương tác, vết dấu lý luận (reasoning traces)
- **Ứng dụng marketing:** Phân tích cạnh tranh, phát hiện xu hướng, nghiên cứu thị trường ngách
- **Đối với Hùng:** Thay thế quy trình nghiên cứu thủ công. Cung cấp URL → nhận báo cáo có cấu trúc

## Xây dựng ứng dụng không cần code (No-Code App Building)

### 13. Lovable
- **Giá:** Gói miễn phí, $25/tháng+
- **Điểm mạnh:** Từ lệnh đến ứng dụng, không cần lập trình, widget tương tác
- **Ứng dụng marketing:** Trang đích, MVPs, công cụ nội bộ, biểu mẫu thu thập lead
- **Đối với Hùng:** Trang đích chiến dịch nhanh chóng mà không cần nhà phát triển

## Trình chiếu và Tạo tài liệu

### 14. Gamma
- **Giá:** Gói miễn phí, $9-$90/tháng
- **Điểm mạnh:** Ghi chú thành bài thuyết trình, thiết kế sạch sẽ, hình ảnh AI, xuất PPTX
- **Ứng dụng marketing:** Đề xuất khách hàng, slide thuyết trình, tài liệu đào tạo
- **Đối với Hùng:** Biến ghi chú nghiên cứu → bài thuyết trình chuyên nghiệp cho khách hàng chỉ trong vài phút

## Họp hành và Tự động hóa quy trình làm việc

### 15. Fathom
- **Giá:** Miễn phí (vĩnh viễn), $15/tháng+
- **Điểm mạnh:** Tích hợp Zoom/Teams, ghi âm tự động, trích xuất mục tiêu hành động, đồng bộ CRM
- **Ứng dụng marketing:** Ghi chú cuộc họp khách hàng, đồng bộ nhóm, theo dõi hành động
- **Đối với Hùng:** Ghi lại cuộc gọi khách hàng → tóm tắt tự động + nhiệm vụ theo sau

## Công cụ dành riêng cho Tác nhân (OpenClaw Context)

### 16. OpenClaw Gateway
- **Hiện tại:** v2026.6.5
- **Vai trò:** Điều phối tác nhân AI, công việc cron, hệ thống bộ nhớ, định tuyến đa kênh
- **Đối với Hùng:** Hạ tầng cốt lõi — mọi thứ chạy qua đây

### 17. Obsidian + Smart Connections MCP
- **Vai trò:** Não bộ thứ hai, tìm kiếm ngữ nghĩa, tự động hóa kho lưu trữ
- **Hiện tại:** 139 ghi chú, 8386 khối, vector 384-dim (bge-micro-v2)
- **Đối với Hùng:** Cơ sở tri thức cho tất cả nghiên cứu và truy xuất tác nhân

### 18. Kỹ năng Multi-Search Engine
- **Vai trò:** 6 công cụ tìm kiếm (4 toàn cầu + 2 Trung Quốc), không cần API key
- **Đối với Hùng:** Nghiên cứu thị trường xuyên suốt các khu vực, giám sát đối thủ cạnh tranh

## Bảng so sánh giá — Chi phí hàng tháng cho stack

| Phân loại | Công cụ | Miễn phí | Trả phí | ROI Marketing |
|----------|------|------|------|---------------|
| LLM cốt lõi | ChatGPT Plus | Hạn chế | $8/tháng | Cao |
| LLM cốt lõi | Claude Pro | Hạn chế | $17/tháng | Trung bình (lập trình) |
| Nghiên cứu | NotebookLM | ✅ | $8.99/tháng | Trung bình |
| Video | Veo 3 | ✅ | $19.99/tháng | Cao (quảng cáo) |
| Video | Higgsfield | ❌ | $9/tháng | Cao (kiểm tra sáng tạo) |
| Giọng nói | ElevenLabs | ✅ | $5-$99/tháng | Trung bình-Cao |
| Không cần code | Lovable | ✅ | $25/tháng | Thấp-Trung bình |
| Trình chiếu | Gamma | ✅ | $9+/tháng | Trung bình |
| Họp hành | Fathom | ✅ | Gói miễn phí | Trung bình |

**Stack tối thiểu khả thi cho Hùng:** ChatGPT Plus ($8) + Veo 3 miễn phí + Higgsfield ($9) + ElevenLabs starter ($5) = **$22/tháng** cho các công cụ AI marketing cốt lõi.

## Các công cụ thị trường Việt Nam

### Công cụ AI địa phương (Tập trung vào Việt Nam)
- **VUI.AI** — AI hội thoại tiếng Việt, bot hỗ trợ khách hàng
- **VNLP** — Bộ công cụ xử lý ngôn ngữ tự nhiên tiếng Việt cho phân tích văn bản
- **SpeechPro VN** — Chuyển giọng nói thành văn bản tiếng Việt
- **AI Content VN** — Tạo nội dung tiếng Việt (SEO, mạng xã hội)

### Công cụ nền tảng địa phương/Facebook
- **Meta Business Suite** — Miễn phí, quản lý FB/IG nguyên sinh
- **Canva AI** — Thiết kế + tạo ảnh AI (có gói miễn phí)
- **CapCut** — Chỉnh sửa video + tính năng AI (miễn phí)
- **Zalo AI Chatbot** — Bot nền tảng nhắn tin tiếng Việt

## Bản đồ tích hợp — Stack 2026 Q2 của Hùng

```
[Hoạch định nội dung] → NotebookLM (nghiên cứu) → ChatGPT/Claude (soạn thảo) → Gamma (trình chiếu)
       ↓
[Sản xuất sáng tạo] → Higgsfield (tạo ảnh) → Veo 3 (video) → ElevenLabs (lồng tiếng)
       ↓
[Phân phối] → OpenClaw (lên lịch + tự động hóa) → Facebook Pages (Graph API)
       ↓
[Tương tác] → Voice Agent ElevenLabs (trả lời tự động) → Fathom (ghi chú cuộc họp)
       ↓
[Phân tích] → Gemini Deep Research (xu hướng thị trường) → Obsidian (cơ sở tri thức)
```

## Các xu hướng chính Q3 2026 (Xem trước)

1. **Trình duyệt AI-native** — Duyệt web với tác nhân AI được xây dựng sẵn (không chỉ là tiện ích mở rộng)
2. **Avatars video thời gian thực** — Phát trực tiếp với người dẫn chương trình AI (Synthesia Video Agents đang mở rộng)
3. **Tìm kiếm đa phương thức** — Tìm kiếm bằng hình ảnh/âm thanh/video, không chỉ văn bản
4. **Nhân bản AI cá nhân** — AI của bạn biết phong cách, sở thích và mẫu hành vi ra quyết định của bạn
5. **Chip Edge AI** — Các LLM trên thiết bị cục bộ cho điện thoại/laptop (không cần đám mây)
6. **Tuân thủ quy định AI** — Thực thi EU AI Act bắt đầu giữa năm 2026

## Nguồn và Xác minh

- Chính: "12 Best AI Tools for 2026" của Synthesia (Tháng 6/2026) — đã xác minh URL trực tiếp
- Phụ: Thư mục FutureTools.io (Matt Wolfe)
- Dữ liệu mô hình: Trang giá chính thức, tài liệu OpenAI/Anthropic/Google
- Hệ sinh thái địa phương: Đăng ký mô hình Ollama, chợ plugin Obsidian
- **Lần cuối xác minh:** 2026-06-17

---

*Tạo: 2026-06-17 | Cập nhật: 2026-06-17 | Lần xem lại tiếp theo: 2026-09-17 (Cập nhật Q3)*
