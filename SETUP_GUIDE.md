# HƯỚNG DẪN CÀI ĐẶT - ĐĂNG BÀI TỰ ĐỘNG

Hệ thống tự động tạo nội dung và đăng bài lên WordPress với AI.

## YÊU CẦU CÓ SẴN

1. **Python 3.8+** - Tải từ https://www.python.org/downloads/
2. **Groq API Key** (miễn phí) - Từ https://console.groq.com/
3. **Stability AI API Key** (~$10/tháng) - Từ https://stability.ai/
4. **WordPress App Password** - Từ mỗi website's wp-admin

## BƯỚC 1: TẢI VÀ GIẢI NÉN FILE

1. Clone từ GitHub: `git clone https://github.com/Duc1502/dangbai.git`
2. Hoặc tải file project và giải nén vào thư mục (vd: C:\DangBai\)
3. Mở Command Prompt / PowerShell

## BƯỚC 2: CÀI ĐẶT PYTHON LIBRARIES

Chạy file batch (đơn giản nhất):
```
install_dependencies.bat
```

Hoặc dùng Command Prompt:
```
cd C:\DangBai
python -m pip install -r requirements.txt
```

Đợi cho đến khi tất cả libraries được cài đặt.

## BƯỚC 3: CẤU HÌNH .env FILE

1. Mở file `.env` bằng Notepad
2. Điền các API keys và WordPress credentials:

```env
# Website URLs
WEBSITE_1_URL=https://techupdatedaily.com/
WEBSITE_2_URL=https://discoveringaiworld.com/

# WordPress Credentials (App Password, không phải password thường)
WEBSITE_1_USERNAME=admin
WEBSITE_1_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx

WEBSITE_2_USERNAME=admin
WEBSITE_2_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx

# API Keys (BẮTBUỘC)
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
STABILITY_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Cấu hình khác
LOG_LEVEL=INFO
```

3. Nhấn Ctrl+S để lưu

### Lấy API Keys:

**Groq API (Miễn phí)**
- Vào https://console.groq.com/
- Đăng nhập → Settings → API Keys
- Copy key → Paste vào .env

**Stability AI API (~$10 credit/tháng)**
- Vào https://stability.ai/
- Đăng nhập → Dashboard → API Keys
- Copy key → Paste vào .env

**WordPress App Password**
- Vào WordPress Admin → Settings → Application Passwords
- Tạo app password mới (không phải password đăng nhập)
- Copy → Paste vào .env

## BƯỚC 4: CHẠY WEB INTERFACE

**Cách đơn giản nhất:** Double-click `run.bat`

**Hoặc dùng Command Prompt:**
```
python app.py
```

Sẽ thấy:
```
============================================================
  DANG BAI WEB INTERFACE
============================================================

Truy cập: http://localhost:5000
Nhấn Ctrl+C để dừng server
```

Mở trình duyệt → http://localhost:5000

## CÁCH DÙNG

### 1. Gợi ý Tiêu Đề (Tùy chọn)
- Click icon ✨ bên ô "Tiêu Đề Bài Viết"
- Nhập từ khóa (vd: "AI", "ChatGPT")
- Click "Gợi ý Tiêu Đề" → Chọn 1 tiêu đề

### 2. Điền Thông Tin
- **Website**: Chọn website muốn đăng
- **Tiêu đề**: Tiêu đề bài viết
- **Category**: 
  - Chọn 1 category → tự tạo nếu không tồn tại
  - Chọn 2+ categories → chỉ tìm (không tạo mới)
- **Ảnh Featured** (tùy chọn):
  - Không upload → Stability AI tự tạo
  - Upload → dùng ảnh của bạn
- **Publish**: Lưu Nháp hoặc Đăng Ngay

### 3. Đăng Bài
- Click "Đăng Bài"
- Hệ thống sẽ:
  1. Tạo nội dung (1500-2000 từ tiếng Anh)
  2. Tạo/upload ảnh featured
  3. Upload ảnh vào WordPress
  4. Rải các ảnh trong bài
  5. Đăng bài hoặc lưu nháp

### 4. Khi Stability AI Hết Credit
- Khi API hết credit → modal hiển thị
- Upload ảnh của bạn
- Click "Tiếp Tục Với Ảnh Này"
- Bài vẫn được đăng với ảnh của bạn

## CHẠY LIÊN TỤC (24/7)

Nếu muốn web chạy khi khởi động Windows:

**Windows Task Scheduler:**
1. Mở Task Scheduler
2. Create Basic Task
3. Name: "DangBai Auto Posting"
4. Trigger: At startup
5. Action: 
   - Program: `python.exe`
   - Arguments: `C:\DangBai\app.py`
6. Click OK

## FEATURE

✅ Tạo nội dung AI với Groq (1500-2000 từ)
✅ Tạo ảnh với Stability AI
✅ Upload ảnh lên WordPress
✅ Chọn 1 hoặc nhiều categories
✅ Upload nhiều ảnh (ảnh đầu làm thumbnail)
✅ Lưu nháp hoặc đăng ngay
✅ Gợi ý tiêu đề AI
✅ Web interface đơn giản
✅ Fallback upload ảnh khi API hết credit

## TROUBLESHOOTING

### Lỗi: "Python not found"
→ Cài Python từ https://www.python.org/downloads/
→ QUAN TRỌNG: Chọn "Add Python to PATH"

### Lỗi: "GROQ_API_KEY not configured"
→ Lấy key từ https://console.groq.com/ → API Keys
→ Paste vào .env

### Lỗi: "STABILITY_API_KEY not configured"
→ Lấy key từ https://stability.ai/ → API Keys
→ Paste vào .env
→ Nếu hết credit, upload ảnh thay vì tạo

### Lỗi: "Connection refused localhost:5000"
→ Flask server chưa chạy
→ Chạy `python app.py` lại

### Lỗi: "WordPress credentials invalid"
→ Dùng **App Password**, không phải password đăng nhập
→ Lấy từ WordPress Admin → Settings → Application Passwords

### Lỗi: "Category not found"
→ Nếu chọn 2+ categories, phải tồn tại trong WordPress
→ Tạo category trong WordPress trước, hoặc chọn 1 category

## CẦN HỖ TRỢ?

Liên hệ: geo@seongon.com

---
**Version**: 2.0  
**Features**: Content AI (Groq), Image Generation (Stability AI), Multiple Images, Category Smart Selection  
**Last Updated**: 2026-05-11
