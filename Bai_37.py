# Bài 37: Đọc các từ cho tới dòng trống, in các từ đã nhập sau khi loại bỏ trùng, giữ thứ tự.
print("Nhập các từ (mỗi từ 1 dòng). Nhấn Enter trên dòng trống để kết thúc:")
seen = set()
result = []
while True:
    s = input().strip()
    if s == "":
        break
    if s not in seen:
        seen.add(s)
        result.append(s)
for w in result:
    print(w)
