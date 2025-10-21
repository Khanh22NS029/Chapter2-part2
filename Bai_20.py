# Bài 20: Tính giai thừa của một số nhập vào.
def giaithua(x):
    if x == 0:
        return 1
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

x = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", x, "là:", giaithua(x))
