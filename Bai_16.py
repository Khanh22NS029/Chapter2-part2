# Bài 16: Tạo dictionary có n phần tử, khóa 1..n, giá trị là bình phương khóa.
n = int(input("Nhập n: "))
d = {}
for i in range(1, n+1):
    d[i] = i*i
print(d)
