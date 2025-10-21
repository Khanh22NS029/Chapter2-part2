# Bài 39: Với n cho trước, tạo dictionary chứa (i, i*i) với i từ 1 đến n và in.
n = int(input("Nhập n: "))
d = {i: i*i for i in range(1, n+1)}
print(d)
