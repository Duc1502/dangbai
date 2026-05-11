# HƯỚNG DẪN CÀI ĐẶT - ĐĂNG BÀI TỰ ĐỘNG

Đây là hướng dẫn chi tiết để cài đặt và chạy hệ thống đăng bài tự động trên PC của bạn.

## YÊU CẦU CÓ SẴN

1. **Python 3.8+** - Tải từ https://www.python.org/downloads/
2. **OpenAI API Key** - Từ https://platform.openai.com/
3. **WordPress Admin Credentials** - Username + App Password cho các website

## BƯỚC 1: TẢI VÀ GIẢI NÉN FILE

1. Tải file project từ GitHub hoặc USB
2. Giải nén vào một thư mục (vd: C:\DangBai\)
3. Mở PowerShell/Command Prompt

## BƯỚC 2: CÀI ĐẶT PYTHON LIBRARIES

Mở PowerShell và chạy:

\\\powershell
cd "C:\DangBai"
python -m pip install -r requirements.txt
\\\

Đợi cho đến khi tất cả libraries được cài đặt.

## BƯỚC 3: CẤU HÌNH .env FILE

1. Mở file .env bằng Notepad
2. Thay các giá trị:

\\\
# Website URLs
WEBSITE_1_URL=https://techupdatedaily.com/
WEBSITE_1_ADMIN_URL=https://techupdatedaily.com/wp-login.php

WEBSITE_2_URL=https://discoveringaiworld.com/
WEBSITE_2_ADMIN_URL=https://discoveringaiworld.com/wp-login.php

# WordPress Credentials
WEBSITE_1_USERNAME=admin
WEBSITE_1_APP_PASSWORD=GKfb xxPi D1As e6Sk T7bK 8wLN

WEBSITE_2_USERNAME=admin
WEBSITE_2_APP_PASSWORD=ydwt 0B1a Pl74 9aUi BRRS 7Eiq

# API Keys
OPENAI_API_KEY=sk_...PASTE_YOUR_KEY_HERE...

# Other
LOG_LEVEL=INFO
OUTPUT_FORMAT=json
\\\

⚠️ **QUAN TRỌNG**: Thay sk_... bằng OpenAI API key thực của bạn

3. Lưu file

## BƯỚC 4: CHẠY WEB INTERFACE

Mở PowerShell tại thư mục project và chạy:

\\\powershell
python app.py
\\\

Output sẽ hiển thị:

\\\
============================================================
  DANG BAI WEB INTERFACE
============================================================

Truy cập: http://localhost:5000
Nhấn Ctrl+C để dừng server
\\\

Mở trình duyệt → http://localhost:5000

## CÁCH DÙNG

### 1. Gợi ý Tiêu Đề
- Click vào icon ✨ bên cạnh ô "Tiêu Đề Bài Viết"
- Nhập từ khóa (vd: "AI", "ChatGPT", "Security")
- Click "Gợi ý Tiêu Đề" → Chọn 1 trong 5 tiêu đề được gợi ý

### 2. Điền Thông Tin
- **Website**: Chọn website muốn đăng
- **Tiêu đề**: Tiêu đề bài viết
- **Category**: Chọn 1 hoặc nhiều category
- **Publish**: Chọn "Lưu Nháp" hoặc "Đăng Ngay"

### 3. Đăng Bài
- Click "Đăng Bài"
- Chờ hệ thống:
  - Tạo nội dung (1500-2000 từ)
  - Tạo ảnh featured
  - Upload ảnh lên WordPress
  - Đăng bài (hoặc lưu nháp)

## CHẠY LÂUDÀI (24/7)

Nếu muốn web interface chạy liên tục:

**Cách 1: Batch File (Đơn giản)**
1. Tạo file un.bat trong thư mục project:
\\\atch
@echo off
cd /d "%~dp0"
python app.py
pause
\\\

2. Double-click un.bat để chạy

**Cách 2: Windows Task Scheduler (24/7)**
1. Mở Task Scheduler
2. Create Basic Task
3. Trigger: At startup (or your desired time)
4. Action: Run \python.exe\ với argument: \C:\\DangBai\\app.py\

## TROUBLESHOOTING

### Lỗi: "Python not found"
→ Python chưa được cài hoặc chưa add vào PATH
→ Cài lại Python và chọn "Add Python to PATH"

### Lỗi: "OPENAI_API_KEY not configured"
→ Chưa set OPENAI_API_KEY trong .env
→ Lấy key từ https://platform.openai.com/ → Settings → API keys

### Lỗi: "Connection refused localhost:5000"
→ Flask server chưa chạy
→ Chạy \python app.py\ lại

### Lỗi: "WordPress credentials invalid"
→ Kiểm tra username + app password trong .env
→ Đảm bảo app password được tạo từ WordPress admin

## CẦN HỖ TRỢ?

Liên hệ: geo@seongon.com

---
**Version**: 1.0  
**Last Updated**: 2026-05-11
