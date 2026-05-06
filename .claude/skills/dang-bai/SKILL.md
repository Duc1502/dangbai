---
name: dang-bai
version: 1.0.0
description: |
  Đăng bài viết tự động lên WordPress với AI content generation.
  Tạo nội dung HTML, ảnh featured, upload WordPress và tạo Table of Contents.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# /dang-bai — Đăng Bài Tự Động

Đăng bài viết tự động lên một trong hai website (Tech Update Daily hoặc Discovering AI World).

## User-invocable

Khi user gõ `/dang-bai`, chạy skill này.

## Usage

```
/dang-bai
```

## Quy trình

Script sẽ hỏi bạn:

1. **Website nào?**
   - 1 = Tech Update Daily (techupdatedaily.com)
   - 2 = Discovering AI World (discoveringaiworld.com)

2. **Tiêu đề bài viết** (bắt buộc)

3. **Category** (tùy chọn, mặc định: News)

4. **Đăng ngay hay lưu nháp?**
   - `ngay` = Đăng bài ngay lập tức
   - `nap` = Lưu nháp (mặc định)

## Tính năng tự động

- ✅ Tạo nội dung HTML bằng Groq AI (1500-2000 từ)
- ✅ Tạo ảnh featured bằng Stability AI
- ✅ Upload ảnh lên WordPress Media
- ✅ Tạo Table of Contents tự động
- ✅ Thêm dấu gạch vàng (#FFAD00) trước h2
- ✅ Thêm ảnh embedded trước h2 thứ 3
- ✅ Đăng bài hoặc lưu nháp

## Setup

Script chính: `skills/dang-bai/main.py`

Yêu cầu:
- Python 3.x
- `.env` file với:
  - GROQ_API_KEY
  - STABILITY_API_KEY
  - WordPress credentials (WEBSITE_1_APP_PASSWORD, WEBSITE_2_APP_PASSWORD)

## Ví dụ

```
/dang-bai

Chon website de dang bai:
  1. Tech Update Daily              (https://techupdatedaily.com)
  2. Discovering AI World           (https://discoveringaiworld.com)

Ban chon (1/2): 1

Tieu de bai viet: AI Trends 2026

Category (mac dinh: News): Technology

Publish ngay hay luu nap (ngay/nap, mac dinh: nap): nap

[Script sẽ tạo bài và hiển thị URL...]
```

## Lưu ý

- Bài viết mặc định lưu **draft** (nháp), edit trên WordPress rồi publish
- Nếu Stability AI hết credit, bài vẫn được tạo nhưng không có ảnh
- Xem KNOWN_ISSUES.md nếu gặp lỗi
