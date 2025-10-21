# Bài 13: Nhập nhiều dòng, chuyển các dòng thành chữ in hoa rồi in.
print("Nhập các dòng (nhấn Enter trên dòng trống để kết thúc):")
lines = []
while True:
    s = input()
    if s == "":
        break
    lines.append(s.upper())

for sentence in lines:
    print(sentence)
