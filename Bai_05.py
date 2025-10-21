# Bài 5: Tính sum = 1/2 + 2/3 + 3/4 + ... + n/(n+1) với n>0.
n = int(input("Nhập n (nguyên > 0): "))
_sum = 0.0
for i in range(1, n+1):
    _sum += float(i) / (i + 1)
print("Kết quả:", _sum)
