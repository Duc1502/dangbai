# Skill: Đăng Bài Tự Động

Đăng bài viết tự động lên WordPress với AI content generation.

## Chạy Skill

```bash
# Từ thư mục gốc của project
python skills/dang-bai/main.py

# Hoặc từ thư mục skill
cd skills/dang-bai
python main.py
```

## Tương Tác

Script sẽ hỏi bạn:

1. **Chọn website:**
   - 1 = Tech Update Daily
   - 2 = Discovering AI World

2. **Tiêu đề bài viết** (bắt buộc)

3. **Category** (tùy chọn, mặc định: News)

4. **Đăng ngay hay lưu nháp?**
   - `ngay` = Đăng bài ngay lập tức
   - `nap` = Lưu nháp (mặc định)

## Tính Năng Tự Động

- ✅ Tạo nội dung HTML với Groq AI (1500-2000 từ)
- ✅ Tạo ảnh featured với Stability AI
- ✅ Upload ảnh lên WordPress
- ✅ Tạo Table of Contents tự động
- ✅ Thêm dấu gạch vàng trước h2
- ✅ Thêm ảnh embedded trước h2 thứ 3
- ✅ Đăng bài hoặc lưu nháp

## Yêu Cầu

- Python 3.x
- `.env` file với credentials và API keys
- `src/post_article.py` (main logic)

## Ghi Chú

- Bài mặc định lưu **draft** (nháp)
- Bạn có thể chỉnh sửa trên WordPress rồi publish
- Xem `KNOWN_ISSUES.md` nếu gặp lỗi
