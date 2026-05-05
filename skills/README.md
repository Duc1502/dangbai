# Skills - Các Chức Năng Tự Động

Thư mục này chứa tất cả các skills (chức năng tự động) cho project.

## Cấu Trúc

```
skills/
├── README.md (file này)
├── dang-bai/
│   ├── main.py (skill handler)
│   └── README.md (hướng dẫn sử dụng)
├── [skill-name]/
│   ├── main.py
│   └── README.md
└── ...
```

## Chạy Skills

**Cách 1: Từ thư mục gốc**
```bash
python skills/dang-bai/main.py
```

**Cách 2: Vào thư mục skill và chạy**
```bash
cd skills/dang-bai
python main.py
```

## Danh Sách Skills

### 1. dang-bai
Đăng bài viết tự động lên WordPress

- **Thư mục:** `skills/dang-bai/`
- **Chạy:** `python skills/dang-bai/main.py`
- **Chức năng:** Tạo nội dung AI → Upload ảnh → Đăng WordPress

Xem chi tiết: `skills/dang-bai/README.md`

---

## Thêm Skill Mới

Để thêm skill mới, tạo folder mới với cấu trúc:

```bash
mkdir skills/[skill-name]
```

Các file bắt buộc:
- `main.py` - Skill handler (point entry)
- `README.md` - Hướng dẫn sử dụng

Ví dụ:
```bash
mkdir skills/check-seo
# Tạo skills/check-seo/main.py
# Tạo skills/check-seo/README.md
```

## Ghi Chú

- Tất cả skills nên có `main.py` làm entry point
- Mỗi skill nên có `README.md` hướng dẫn
- Skills có thể gọi các script trong `src/` nếu cần
- Credentials/API keys lấy từ `.env`
