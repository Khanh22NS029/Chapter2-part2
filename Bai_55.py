# Bài 55: (Cơ bản) Nén và giải nén file bằng zipfile (ví dụ đơn giản).
import zipfile
import os

def compress(files, out_name):
    with zipfile.ZipFile(out_name, 'w') as z:
        for f in files:
            if os.path.isfile(f):
                z.write(f)
    print("Đã tạo:", out_name)

def decompress(zip_path, extract_to='.'):
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(extract_to)
    print("Đã giải nén vào:", extract_to)

if __name__ == '__main__':
    print("Ví dụ: gọi compress(['file1.txt'], 'out.zip') hoặc decompress('out.zip')")
