# Đức - Quản Lý Web

## Vai Trò
Quản trị web cho các web cá nhân

## Mô Tả
Project để quản lý các trang web cá nhân, kiểm tra dữ liệu, đăng bài lên các website.

## Công Việc Chính
1. **Kiểm tra dữ liệu website** - Check SEO, content, links
2. **Đăng bài lên website** - Upload article, update content
3. **Quản lý danh sách website** - Track các site đang quản lý
4. **Report dữ liệu** - Tổng hợp metrics, thống kê

## Cấu Trúc Thư Mục
- `src/` - Script chính (check data, post article)
- `skills/` - Các chức năng tự động (dang-bai, ...)
- `data/` - Dữ liệu website (JSON, CSV)
- `output/` - Kết quả check, report
- `websites.json` - Danh sách website quản lý

## Setup
```bash
# Vào folder
cd Duc-Quan-ly-web

# Setup environment
cp .env.example .env
# Edit .env với:
# - Website URLs
# - Admin credentials
# - API keys

# Run scripts
python src/check_website_data.py
python src/post_article.py
```

## Technologies
- Python 3.x (requests, BeautifulSoup4, Selenium - optional)
- JSON/CSV cho data
- Bash scripts

## Skill: Đăng Bài Tự Động

Đăng bài lên website tự động với AI content generation:

```bash
# Chạy từ thư mục gốc
python skills/dang-bai/main.py

# Hoặc vào thư mục skill
cd skills/dang-bai
python main.py
```

Skill sẽ hỏi:
1. Website nào? (1. Tech Update Daily, 2. Discovering AI World)
2. Tiêu đề bài viết?
3. Category (tùy chọn, mặc định: News)
4. Đăng ngay hay lưu nháp? (ngay/nap, mặc định: nap)

Sau đó tự động:
- Tạo nội dung HTML với Groq AI (1500-2000 từ)
- Tạo ảnh featured với Stability AI
- Upload ảnh lên WordPress
- Tạo Table of Contents tự động
- Thêm dấu gạch vàng (#FFAD00) trước h2
- Đăng bài hoặc lưu nháp

Xem chi tiết: `SKILL_USAGE.md`

## Tips cho Claude Code
- Tập trung vào: Kiểm tra data website, đăng bài, quản lý danh sách
- Không cần: Database phức tạp (dùng JSON/CSV đủ)
- Code style: Python simple, easy to run, no external dependencies nếu có thể
- Hỗ trợ tiếng Việt trong comments
