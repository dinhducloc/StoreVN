import pandas as pd
import gdown
import os
# -----------------------------------------------------------------------------
# Danh sách file CSV
files = ['./ggdrive.csv']
# -----------------------------------------------------------------------------
# Thư mục tải về
download_folder = './downloads_local'
os.makedirs(download_folder, exist_ok=True)
# -----------------------------------------------------------------------------
# File log
log_file = 'logs_local.txt'
with open(log_file, 'w', encoding='utf-8') as log:
    log.write("Kết quả tải file:\n")
# ------------------------------------------------------------------------------
# Hàm trích xuất ID từ link Google Drive
def extract_drive_id(link):
    if 'id=' in link:
        return link.split('id=')[1].split('&')[0]
    elif 'file/d/' in link:
        return link.split('file/d/')[1].split('/')[0]
    elif 'uc?export=download&id=' in link:
        return link.split('id=')[1].split('&')[0]
    else:
        return None
# ------------------------------------------------------------------------------
# Duyệt qua từng file CSV
for file_path in files:
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Không thể đọc {file_path}: {e}")
        continue
    # --------------------------------------------------------------------------
    for index, row in df.iterrows():
        # Xác định tên file và link
        file_name = str(row['B']) if 'B' in df.columns else str(row[1])
        drive_link = str(row['C']) if 'C' in df.columns else str(row[2])
        # ----------------------------------------------------------------------
        # Trích xuất ID
        file_id = extract_drive_id(drive_link)
        if not file_id:
            print(f"[!] Không thể phân tích link: {drive_link}")
            with open(log_file, 'a', encoding='utf-8') as log:
                log.write(f"[X] Lỗi link: {drive_link}\n")
            continue
        # ----------------------------------------------------------------------
        # Tạo đường dẫn và kiểm tra trùng lặp
        download_url = f"https://drive.google.com/uc?id={file_id}"
        output_path = os.path.join(download_folder, file_name)

        if os.path.exists(output_path):
            print(f"[✔] Đã tồn tại, bỏ qua: {file_name}")
            with open(log_file, 'a', encoding='utf-8') as log:
                log.write(f"[✔] Đã tồn tại: {file_name}\n")
            continue
# ------------------------------------------------------------------------------
        # Tải file
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