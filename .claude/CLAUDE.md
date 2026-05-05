# Đức - Quản Lý Web

## Mô Tả
Project để quản lý các trang web cá nhân, kiểm tra dữ liệu, đăng bài lên các website.

## Công Việc Chính
1. **Kiểm tra dữ liệu website** - Check SEO, content, links
2. **Đăng bài lên website** - Upload article, update content
3. **Quản lý danh sách website** - Track các site đang quản lý
4. **Report dữ liệu** - Tổng hợp metrics, thống kê

## Cấu Trúc Thư Mục
- `src/` - Script chính (check data, post article)
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

## Tips cho Claude Code
- Tập trung vào: Kiểm tra data website, đăng bài, quản lý danh sách
- Không cần: Database phức tạp (dùng JSON/CSV đủ)
- Code style: Python simple, easy to run, no external dependencies nếu có thể
- Hỗ trợ tiếng Việt trong comments
