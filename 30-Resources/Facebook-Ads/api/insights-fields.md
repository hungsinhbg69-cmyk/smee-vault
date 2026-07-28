---
title: "Tham khảo các trường của Facebook Insights API"
slug: "fb-api-insights-fields-reference"
category: resource
tags: [vault-maintenance, facebook-ads]
status: "draft"
type: reference
created: 2026-06-15
last_updated: 2026-06-24
---


# Các trường Insights của API (Báo cáo + Chỉ số)

## Meta Graph API - Điểm cuối Insights

### Điểm cuối cơ bản
`
Lấy /act_{AD_ACCOT_D}/insights
Lấy /{CAMPAIGN_ID}/insights
Lấy /{ADST_ID}/insights
Gỡ bỏ /{D_ID}/insights
`

### Các tham số bắt buộc
- level: campaign | adset | ad | criteria (bắt buộc)
- fields: các trường chỉ số phân cách bằng dấu phẩy (bắt buộc)

### Các tham số tùy chọn
### Tham số tùy chọn
- since / until: khoảng thời gian tùy chỉnh (ISO 8601)
- filtering: mảng JSON các điều kiện lọc
- breakdowns: mảng các chiều phân tích
- sort: trường để sắp xếp
- limit: số kết quả mỗi trang

## Các trường Insights chính

### Các trường chi phí
| Trường | Mô tả | Giá trị ví dụ |
|---|---|---|
| spend | Chi phí quảng cáo tính bằng đơn vị tiền tệ nhỏ nhất (xu) | 5000 = .00 |
| cpm | Chi phí cho mỗi 1.000 lượt hiển thị | 8.50 |
| ecpm | CPM hiệu quả (bao gồm tất cả vị trí hiển thị) | 9.20 |
| chi phí_per_ttal_ action | Chi phí trung bình cho mọi hành động | 3.50 |

### Các trường nhấp chuột
| Trường | Mô tả | Giá trị ví dụ |
|---|---|---|
| clicks | Tổng số lượt nhấp (tất cả loại) | 1500 |
| link_clicks | Lượt nhấp vào liên kết | 800 |
| unique_clicks | Người nhấp duy nhất | 650 |
| ctr | Tỷ lệ nhấp (lượt nhấp/lượt hiển thị) | 0.025 |
| nhấn_qua_rate | CTR cho liên kết cụ thể | 0.015 |
| _ bấy_nhiêu_ bấy_nhiêu: | CPC cho lượt nhấp vào liên kết | 0.63 |
| cost_per_unique_click | Cost per unique clicker | 0.77 |

### Các trường chuyển đổi
| Trường | Mô tả | Giá trị ví dụ |
|---|---|---|
| actions | Mảng các sự kiện chuyển đổi theo loại | Xem phần phân tích bên dưới |
| kiểu_p/ hành động | CPA cho mỗi loại sự kiện | Xem phần phân tích bên dưới |
| purchases | Số lượng chuyển đổi mua hàng | 25 |
| purchase_roas | Tỷ suất lợi nhuận trên chi phí quảng cáo (mua hàng) | 3.85 |
| results | Tổng kết quả tối ưu hóa | 150 |
| _per_reult | Chi phí trung bình cho mỗi kết quả tối ưu hóa | 2.00 |

### Định dạng phân tích trường actions
`json
"actions": [
  "Xà" theo kiểu "ppurchase", "giá trị" : "25"
  ["ase_type": "add_ to_cart", "giá trị": "80"
  "Xâm nhập" : "link_ click", "giá trị" : "800"
  ["a"ase_type": "tiểu thức ", giá trị" : "45"}
]
`

### Định dạng phân tích trường cost_per_action_type
`json
"kiểu hành động giá trị:
  {"action_type": "purchase", "cost_per_action": "2.00"},
  "Xin lỗi" là "lên xe"
  {"action_type": "link_click", "cost_per_action": "0.01"}
]
`

### Các trường Phạm vi tiếp cận & Tần suất
| Trường | Mô tả | Giá trị ví dụ |
|---|---|---|
| impressions | Tổng số lượt hiển thị quảng cáo | 50000 |
| reach | Số người duy nhất được tiếp cận | 35000 |
| frequency | Số lần hiển thị trung bình mỗi người | 1.43 |
| unique_impressions | Lượt hiển thị duy nhất (đã loại trùng) | 42000 |
| unique_reach | Phạm vi tiếp cận duy nhất (đã loại trùng) | 35000 |

### Các trường Video
| Trường | Mô tả | Giá trị ví dụ |
|---|---|---|
| Xem giây_động | Thời gian xem trung bình | 8.5 |
| videos_3sec_watches | 3-second video views | 12000 |
| videos_10sec_watches | 10-second video views | 4500 |
| _Xem ảnh động đầy đủ | Lượt xem hoàn chỉnh video | 1200 |
| video_avg_time_watched | Average watch time (formatted) | "8.5s" |

### Các trường Tương tác
| Trường | Mô tả | Giá trị ví dụ |
|---|---|---|
| Gửi_gấp_resuts | Số lượng tương tác bài đăng | 450 |
| page_likes | Lượt thích trang đã tăng thêm | 12 |
| _ Nhóm_ kích hoạt_động_rút | Phạm vi tiếp cận được tối ưu cho mục tiêu | 30000 |

## Các chiều phân tích (Breakdown Dimensions)

### Các chiều phân tích khả dụng
| Chiều | Mô tả |
|---|---|
| platform | Facebook so với Instagram và Audience Network |
| device | Máy tính để bàn, Di động hay Máy tính bảng |
| age | Nhóm tuổi |
| gender | Nam, Nữ hoặc Tất cả |
| country | Theo mã quốc gia |
| region | Theo khu vực/tỉnh bang |
| city | Theo thành phố |
| placement | Feed, Stories, Reels và v.v. |
| impression_device | Loại thiết bị tại thời điểm hiển thị |
| publisher_platform | Nơi quảng cáo được hiển thị |
| _Sự phân loại tạo | Hình ảnh, Video hay Carousel |

### Ví dụ với các chiều phân tích
`
Lấy /cc_{ID*TIẾNG THÔI*? *SPED=KNEED=OOH, CLOOO:
`

## Các tùy chọn Đặt trước ngày (Date Preset)
| Tùy chọn | Mô tả |
|---|---|
| today | Ngày hiện tại (UTC) |
| yesterday | Ngày hôm qua (UTC) |
| last_7d | 7 ngày gần nhất bao gồm ngày hôm nay |
| last_14d | 14 ngày gần nhất bao gồm ngày hôm nay |
| last_30d | 30 ngày gần nhất bao gồm ngày hôm nay |
| this_month | Tháng hiện tại cho đến nay |
| last_month | Tháng đầy đủ trước đó |
| last_3m | 3 tháng gần nhất |
| this_quarter | Quý hiện tại |
| last_quarter | Quý đầy đủ trước đó |
| lifetime | Tất cả thời gian |
| custom | Sử dụng các tham số since/until |

## Các toán tử Lọc
| Toán tử | Mô tả | Ví dụ |
|---|---|---|
| = | Bằng | "Freveive" "Op" ":"eq", giá trị ": "Cunguests" |
| != | Không bằng | "field": "Status" ","op"": "neq", giá trị ": "EEETEEEEEEEEEEEE""" "} |
| > | Lớn hơn | "Floafield" :"Ep" "Op""" "gt""" ", giá trị" "a 1000"" |
| < | Nhỏ hơn | "field": "Frequaency" "Op": "lt", giá trị ":"3.0" |
| >= | Lớn hơn hoặc bằng | "field": "purchasses" "Op"" "gte" ", giá trị" "50" |
| <= | Nhỏ hơn hoặc bằng | "field": "cpm" "op"" "lte" ", giá trị" "10". |
| IN | Trong danh sách | "Franve" "Op" "in" ", giá trị" ["CONVES" ",SALES"] |

## Các truy vấn API phổ biến

### Lấy hiệu suất của tất cả các tập quảng cáo (7 ngày qua)
`
Lấy /cc_{IDTập hợp =adset&fields=adset_ name, less, inpressions,link_ctr, cpcc, actions,purchase_roas&date_preset=7d
`

### Lấy 5 quảng cáo hiệu quả nhất theo ROAS
`
Lấy /cc_{ID*TIẾNG C_EPHHHHHHHHHHHHHHHHHHHHHHHHH: = [creative_creative_cate_cate_cate]&fields=ad_ name, staset=th_30d&ort=-purchase_roas = 5
`

### Tìm các tập quảng cáo đang ở giai đoạn học tập
`
Lấy /cc_{ID[Tiếng địa phương] [tiếng vỗ]
`

### Phân tích theo vị trí hiển thị (tìm vị trí hiệu quả nhất)
`
Lấy /cc_{ID*Tám ảnh? *SPCpccpdowns=[ment]&fields=adset= biệt hiệu : biệt lập, đình chỉ, hành động, cpcccc, ctr& Breakdowns=[các chỉ định]&date_preset=st_14d
`

## Giới hạn tốc độ API
- Tiêu chuẩn: ~200 yêu cầu mỗi ứng dụng cho mỗi người dùng mỗi giờ
- Đột xuất: Lên đến 50 yêu cầu/giây (những đợt ngắn)
- Kiểm tra X-Marketing-App-Event-Header để xem số lượng còn lại
- Triển khai cơ chế giảm tốc độ theo hàm mũ đối với phản hồi 429

---
*Đã tạo: 2026-06-15 | Tham khảo: tài liệu Graph API v25.0*