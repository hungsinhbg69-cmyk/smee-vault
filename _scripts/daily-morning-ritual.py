#!/usr/bin/env python3
"""
Daily Morning Ritual - Create a morning routine note for Obsidian daily log.
Generates a structured daily plan to kickstart the day productively.
"""

import os
import sys
from datetime import datetime, timedelta

# Config
VAULT_ROOT = r"C:\Users\Hung\Desktop\Smee Obsidian\Smee"
DAILY_FOLDER = os.path.join(VAULT_ROOT, "02-Daily")

def get_date_strings():
    """Get formatted date strings for Vietnamese locale."""
    today = datetime.now()
    
    # Date formats
    today_iso = today.strftime("%Y-%m-%d")
    
    # Vietnamese weekday names
    vn_weekdays = [
        "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", 
        "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"
    ]
    weekday_name = vn_weekdays[today.weekday()]
    
    # Vietnamese month names
    vn_months = [
        "tháng 1", "tháng 2", "tháng 3", "tháng 4", "tháng 5", "tháng 6",
        "tháng 7", "tháng 8", "tháng 9", "tháng 10", "tháng 11", "tháng 12"
    ]
    
    yesterday = today - timedelta(days=1)
    yesterday_iso = yesterday.strftime("%Y-%m-%d")
    
    return {
        "today": today_iso,
        "date_formatted": f"{today.day} {vn_months[today.month-1]} {today.year}",
        "weekday": weekday_name,
        "yesterday": yesterday_iso,
        "time_morning": str(datetime.now().replace(hour=8, minute=30, second=0)),
    }

def create_daily_note(data):
    """Create a daily morning ritual note."""
    
    yesterday_link = f"[[{data['yesterday']}]]" if os.path.exists(
        os.path.join(DAILY_FOLDER, f"{data['yesterday']}.md")
    ) else "_None_"
    
    today_file = os.path.join(DAILY_FOLDER, f"{data['today']}.md")
    
    # Check if already exists (avoid duplicates)
    if os.path.exists(today_file):
        print(f"Daily note for {data['today']} already exists. Skipping.")
        return False
    
    template = f"""---
title: "🌅 Morning Ritual — {data['today']}"
slug: "morning-ritual-{data['today']}"
category: daily-morning-ritual
tags: [daily, morning-ritual, intention]
status: active
type: daily-plan
created: {data['today']}
last_updated: {{date}}
mood: 
energy_level: 1-5
focus_today: 
---

# 🌅 {data['weekday']}, {data['date_formatted']} — Chào Ngày Mới!

<!-- Khởi động ngày mới cùng Obsidian & Smee -->

## 🧘 Morning Intention (3 phút)
> "Hôm nay em sẽ tập trung vào..."

- [ ] **Nhắm mắt, hít thở sâu 3 lần**
- [ ] **Viết 1 câu intention cho hôm nay:** _"_________________________________________"_
- [ ] **Cảm ơn 3 điều nhỏ bé trong đời**

## 🎯 Today's Big 3 (Prioritas tối đa 3 việc)
1. [ ] ___________________ *(năng lượng cao nhất)*
2. [ ] ___________________ *(quan trọng nhất)*
3. [ ] ___________________ *(gấp nhất)*

## 🔋 Energy & Mood Check-in
- **Năng lượng sáng:** ⭐(1-5, chọn 1): __
- **Mood hôm nay:** 😊/😐/😔/😤 (khoanh tròn)
- **Yếu tố ảnh hưởng chính:** ___________________

## 📋 Daily Flow Template *(tham khảo)*
```tasks
not done
due after {data['yesterday']}
sort by due
group by priority
```

### Morning (6:00 - 12:00)
- [ ] Review Big 3 priorities
- [ ] Làm việc sâu (deep work) #1 vào ca tốt nhất của bạn
- [ ] Kiểm tra email/calls quan trọng *(giới hạn 30 phút)*

### Afternoon (13:00 - 17:00)
- [ ] Làm việc sâu (deep work) #2 / Meetings
- [ ] Quản lý tác vụ nhỏ, admin tasks
- [ ] Review tiến độ Big 3 — điều chỉnh nếu cần

### Evening (18:00+)
- [ ] **Evening Review:** hoàn thành những việc gì?
- [ ] Chuẩn bị hôm sau: lên Top 3 priorities
- [ ] Disconnect & recharge ⭐

## 📝 Quick Capture *(notes, ideas, insights)*
- 
- 

## 💬 Gratitude Log *(3 điều biết ơn hôm nay)*
1. 
2. 
3. 

## 🔗 Yesterday's Links Link kết từ ngày trước:
- {yesterday_link}

---
*🌱 Morning Ritual tạo bởi Smee Agent — Hãy yêu thương bản thân trong hành trình phát triển!*
"""

    with open(today_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✅ Created: {today_file}")
    return True

def main():
    """Main entry point."""
    data = get_date_strings()
    created = create_daily_note(data)
    
    if created:
        print(f"🌅 Daily Morning Ritual for {data['today']} ( {data['weekday']} )")
        print(f"   Yesterday's note link: {data['yesterday']}")
    else:
        print(f"⏭️  Skipped duplicate for {data['today']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
