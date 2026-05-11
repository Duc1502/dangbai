# HƯỚNG DẪN NHANH - START NGAY

## Lần đầu tiên (5 phút)

1. **Cài Python** (nếu chưa có)
   - Tải từ: https://www.python.org/downloads/
   - Chọn "Add Python to PATH" khi cài

2. **Cài dependencies**
   - Mở PowerShell trong thư mục dự án
   - Chạy: \python -m pip install -r requirements.txt\

3. **Cấu hình .env**
   - Mở file .env bằng Notepad
   - Thay OPENAI_API_KEY=sk_... bằng API key thực của bạn
   - Lưu file

4. **Chạy lần đầu**
   - Double-click file \un.bat\
   - Hoặc chạy: \python app.py\
   - Mở browser → http://localhost:5000

## Lần tiếp theo (1 click)

- Double-click \un.bat\ → Xong!

## API Key từ đâu?

1. Vào https://platform.openai.com/
2. Click "API keys" 
3. Click "+ Create new secret key"
4. Copy key → Paste vào .env

---

📖 **Xem chi tiết**: SETUP_GUIDE.md
