# Bài 42: Tính giai thừa của một số cho trước, in kết quả.
def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

n = int(input("Nhập n: "))
print("Giai thừa:", fact(n))
