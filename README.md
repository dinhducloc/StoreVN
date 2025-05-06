# CÔNG CỤ TẢI XUỐNG NHANH TỪ GOOGLE DRIVE
Script Python này giúp tải file từ Google Drive dựa trên thông tin trong các file CSV.
---
---
## Yêu Cầu

- Python 3.x trở lên
- Các thư viện Python: pandas, gdown

## Cài Đặt

```bash
pip install pandas gdown
```
s
## Chuẩn Bị
Chuẩn bị file CSV [ ggdrive.csv ] với các cột và Đặt các file CSV vào cùng thư mục với script:
   - Cột B: Tên file (A, B [Tên file], C...)
   - Cột C: Link Google Drive (A, B, C [Link Google Drive])
   - Đổi nội dung từ sau chữ /edit= thành htmlview rồi Ctrl + S để lưu (Nếu cần tải theo tệp .htm và .html)
## Cách Sử Dụng
1. Chạy script:
```bash
python local.py (tải bằng tệp .csv)
```
---
```bash
python website.py (tải bằng tệp .html hoặc .htm)
```
2. Script sẽ:
   - Tự động tạo thư mục `downloads`
   - Đọc từng file CSV
   - Tải các file từ Google Drive và lưu vào thư mục `downloads`
   - Hiển thị tiến trình tải
---
## Lưu Ý
- Đảm bảo các link Google Drive được chia sẻ công khai
- Kiểm tra đủ dung lượng ổ đĩa trước khi tải
- Kiểm tra kết nối internet ổn định
---
