# HƯỚNG DẪN NHANH - START NGAY

## Lần đầu tiên (10 phút)

### Bước 1: Cài Python (nếu chưa có)
- Tải từ: https://www.python.org/downloads/
- **QUAN TRỌNG**: Chọn "Add Python to PATH" khi cài
- Click Install

### Bước 2: Cài thư viện
- Right-click file `install_dependencies.bat` → Run as administrator
- Chờ cửa sổ CMD đóng lại (tự động)

### Bước 3: Cấu hình API Keys
Mở file `.env` bằng Notepad và điền:

```
# Bắt buộc
GROQ_API_KEY=your_groq_key_here
STABILITY_API_KEY=your_stability_key_here

# WordPress
WEBSITE_1_USERNAME=admin
WEBSITE_1_APP_PASSWORD=your_app_password_here
WEBSITE_2_USERNAME=admin
WEBSITE_2_APP_PASSWORD=your_app_password_here
```

- Nhấn Ctrl+S để lưu

### Bước 4: Chạy ứng dụng
- Double-click file `run.bat`
- Mở trình duyệt → http://localhost:5000
- Xong! Bắt đầu dùng

## Lần tiếp theo (1 click)

- Double-click `run.bat` → Chạy ngay!

---

## Cần API Key?

### Groq API (Miễn phí)
1. Vào: https://console.groq.com/
2. Đăng nhập hoặc tạo account
3. Copy API Key → Paste vào `.env`

### Stability AI (Miễn phí ~$10/tháng)
1. Vào: https://stability.ai/
2. Đăng nhập hoặc tạo account
3. Lấy API Key → Paste vào `.env`

### WordPress App Password
1. Vào WordPress Admin → Settings → Application Passwords
2. Tạo app password mới
3. Copy → Paste vào `.env`

---

Xem chi tiết: SETUP_GUIDE.md
