import pandas as pd
import gdown
import os
from bs4 import BeautifulSoup

# -----------------------------------------------------------------------------
files = ['./ggdrive.htm', './ggdrive.html']  # Danh sách file HTML
download_folder = './downloads_html'
os.makedirs(download_folder, exist_ok=True)
log_file = 'logs_html.txt'
with open(log_file, 'w', encoding='utf-8') as log:
    log.write("Kết quả tải file:\n")

def extract_drive_id(link):
    if 'id=' in link:
        return link.split('id=')[1].split('&')[0]
    elif 'file/d/' in link:
        return link.split('file/d/')[1].split('/')[0]
    elif 'uc?export=download&id=' in link:
        return link.split('id=')[1].split('&')[0]
    else:
        return None

def sanitize_filename(name):
    # Loại bỏ ký tự không hợp lệ cho tên file Windows
    invalid = '<>:"/\\|?*'
    for c in invalid:
        name = name.replace(c, '_')
    return name.strip()

def process_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'drive.google.com' in href:
            file_id = extract_drive_id(href)
            if file_id:
                # Lấy tên file từ nội dung thẻ a, nếu không có thì dùng file_id
                file_name = a.text.strip()
                if not file_name or file_name.startswith('http'):
                    file_name = f"{file_id}.file"
                file_name = sanitize_filename(file_name)
                links.append((file_name, file_id))
    return links

for file_path in files:
    if file_path.endswith('.htm') or file_path.endswith('.html'):
        links = process_html(file_path)
        for file_name, file_id in links:
            download_url = f"https://drive.google.com/uc?id={file_id}"
            output_path = os.path.join(download_folder, file_name)
            if os.path.exists(output_path):
                print(f"[✔] Đã tồn tại, bỏ qua: {file_name}")
                with open(log_file, 'a', encoding='utf-8') as log:
                    log.write(f"[✔] Đã tồn tại: {file_name}\n")
                continue
            try:
                print(f" → Đang tải: {file_name}")
                gdown.download(download_url, output_path, quiet=False)
                with open(log_file, 'a', encoding='utf-8') as log:
                    log.write(f"[✔] Tải thành công: {file_name}\n")
            except Exception as e:
                print(f"[X] Lỗi khi tải {file_name}: {e}")
                with open(log_file, 'a', encoding='utf-8') as log:
                    log.write(f"[X] Tải thất bại: {file_name} — {e}\n")
# ------------------------------------------------------------------------------