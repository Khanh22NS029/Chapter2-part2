# Bài 7: Kiểm tra số Armstrong bậc N.
num = int(input("Nhập số nguyên dương: "))
level = int(input("Bậc (N): "))
temp = num
_sum = 0
while temp > 0:
    digit = temp % 10
    _sum += digit ** level
    temp //= 10

if num == _sum:
    print(f"{num} là số Armstrong bậc {level}")
else:
    print(f"{num} không phải Armstrong bậc {level}")
