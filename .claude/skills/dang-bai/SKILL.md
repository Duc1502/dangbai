# /dang-bai

Đăng bài tự động lên website với AI content generation.

## Chức Năng
Hỏi user về:
1. Website nào (Tech Update Daily hoặc Discovering AI World)
2. Tiêu đề bài viết
3. Category (mặc định: News)
4. Publish ngay hay lưu nháp (mặc định: nháp)

Sau đó tự động:
- Tạo nội dung HTML với Groq AI (1500-2000 từ)
- Tạo ảnh featured với Stability AI
- Upload ảnh lên WordPress
- Tạo Table of Contents tự động
- Thêm dấu gạch vàng (#FFAD00) trước h2
- Đăng bài hoặc lưu nháp

## Cách Sử Dụng
```bash
/dang-bai
```

## Cấu Trúc File
- `main.py` - Skill handler, hỏi user thông tin
- `post_article.py` - Script thực tế đăng bài
- `logs/` - Lịch sử chạy
