# Bài 38: Đọc số nguyên cho tới dòng trống, sau đó in các số: tất cả số âm, sau đó số không, sau đó số dương.
print("Nhập các số nguyên (mỗi số 1 dòng). Nhấn Enter trên dòng trống để kết thúc:")
neg, zero, pos = [], [], []
while True:
    s = input().strip()
    if s == "":
        break
    try:
        v = int(s)
    except:
        print("Giá trị không hợp lệ, bỏ qua.")
        continue
    if v < 0:
        neg.append(v)
    elif v == 0:
        zero.append(v)
    else:
        pos.append(v)

out = neg + zero + pos
for v in out:
    print(v)
