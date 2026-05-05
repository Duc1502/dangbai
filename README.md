# Đức - Quản Lý Web 🌐

Công cụ quản lý các trang web cá nhân: kiểm tra dữ liệu, đăng bài, theo dõi metrics.

## Setup

### 1. Clone/Tạo Project
```bash
cd Duc-Quan-ly-web
```

### 2. Setup Environment
```bash
# Copy file mẫu
cp .env.example .env

# Edit .env với thông tin website của bạn
nano .env  # hoặc mở bằng editor yêu thích
```

### 3. Cài Đặt Dependencies (nếu cần)
```bash
# Python
pip install requests beautifulsoup4

# Optional: Nếu cần automated browser
# pip install selenium
```

## Cấu Trúc

```
Duc-Quan-ly-web/
├── .claude/
│   └── CLAUDE.md           ← Hướng dẫn cho Claude Code
├── src/
│   ├── check_website_data.py       ← Check dữ liệu website
│   ├── post_article.py             ← Đăng bài
│   └── website_manager.py          ← Quản lý danh sách
├── data/
│   ├── websites.json               ← Danh sách website
│   ├── articles.csv                ← Bài viết cần đăng
│   └── checklist.json              ← Checklist kiểm tra
├── output/
│   ├── reports/                    ← Report dữ liệu
│   └── logs/                       ← Logs hoạt động
├── .env                    ← Config (GHI: Không commit!)
├── .env.example           ← Mẫu config
├── .gitignore
└── README.md
```

## Sử Dụng

### 1. Kiểm Tra Dữ Liệu Website
```bash
python src/check_website_data.py
```
- Check metadata, headings, links
- Xuất report ra `output/reports/`

### 2. Đăng Bài
```bash
python src/post_article.py --file data/articles.csv
```
- Đọc danh sách bài từ CSV
- Đăng lên các website

### 3. Quản Lý Website
```bash
python src/website_manager.py --list
```
- Xem danh sách website
- Thêm/xóa website

## File Config (.env)

```
WEBSITE_1_URL=https://your-site.com
WEBSITE_1_USERNAME=admin
WEBSITE_1_PASSWORD=your_password
```

⚠️ **Bảo Mật:** Không commit `.env` - chỉ commit `.env.example`

## File Data

### websites.json
```json
{
  "websites": [
    {
      "name": "Site 1",
      "url": "https://site1.com",
      "type": "wordpress",
      "status": "active"
    }
  ]
}
```

### articles.csv
```
Title,Content,Website,PublishDate
Bài 1,Nội dung...,site1.com,2026-05-05
Bài 2,Nội dung...,site2.com,2026-05-06
```

## Logs & Reports

- Logs: `output/logs/` - Ghi lại tất cả hoạt động
- Reports: `output/reports/` - Kết quả kiểm tra dữ liệu

## Tips

1. **Kiểm tra lần đầu:** Chạy script với `--dry-run` để xem kết quả trước
2. **Backup:** Lưu trữ backup dữ liệu website thường xuyên
3. **Schedule:** Dùng cron job để chạy script tự động hàng ngày

```bash
# Ví dụ: Chạy check mỗi sáng 8h
0 8 * * * cd ~/Duc-Quan-ly-web && python src/check_website_data.py
```

## Help

Hỏi Claude Code để:
- Thêm script mới
- Debug issues
- Tối ưu hóa code
- Thêm features

---

**Project:** Đức - Quản Lý Web 🌐  
**Created:** 2026-05-05  
**Status:** Active
