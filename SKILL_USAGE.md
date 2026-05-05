# Hướng Dùng Skill /dang-bai

## Cách sử dụng nhanh nhất

### Từ Claude Code UI
Nếu skill đã được đăng ký, bạn có thể gõ:
```
/dang-bai
```

### Từ Terminal/Command Line
Nếu chưa thấy skill trong UI, chạy trực tiếp:
```bash
python src/dang_bai_skill.py
```

## Các bước sẽ hỏi

1. **Chọn website:**
   ```
   Chon website de dang bai:
     1. Tech Update Daily
     2. Discovering AI World
   Ban chon (1/2): _
   ```

2. **Nhập tiêu đề bài viết:**
   ```
   Tieu de bai viet: _
   ```

3. **Chọn category (tùy chọn, mặc định: News):**
   ```
   Category (mac dinh: News): _
   ```

4. **Chọn đăng ngay hay lưu nháp:**
   ```
   Publish ngay hay luu nap (ngay/nap, mac dinh: nap): _
   ```
   - `ngay` = Đăng bài ngay lập tức
   - `nap` = Lưu nháp (mặc định)

## Kết quả tự động

Sau khi hoàn thành, script sẽ tự động:
✅ Tạo nội dung HTML bằng Groq AI (1500-2000 từ)
✅ Tạo ảnh AI bằng Stability AI  
✅ Upload ảnh lên WordPress
✅ Tạo Table of Contents tự động
✅ Thêm dấu gạch vàng trước mỗi h2
✅ Đăng bài (hoặc lưu nháp)

## Thông tin kỹ thuật

- **Handler script:** `src/dang_bai_skill.py`
- **Main logic:** `src/post_article.py`
- **Dependencies:** requests (đã install)
- **API Keys:** Lưu trong `.env`

Xem `.claude/skills/dang-bai.md` để biết thêm chi tiết.
