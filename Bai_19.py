# Bài 19: Hiển thị 10 từ có tần suất xuất hiện nhiều nhất trong file romeo.txt
# (File romeo.txt cần có sẵn trong thư mục làm việc nếu muốn chạy)
from collections import Counter
try:
    with open("romeo.txt", encoding="utf-8") as f:
        words = []
        for line in f:
            words.extend(line.split())
    c = Counter(words)
    for word, cnt in c.most_common(10):
        print(word, cnt)
except FileNotFoundError:
    print("Không tìm thấy file romeo.txt trong thư mục hiện tại.")
