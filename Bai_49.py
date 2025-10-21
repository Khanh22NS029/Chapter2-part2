# Bài 49: Kiểm tra số nguyên tố, trả về True/False.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    n = int(input("Nhập số nguyên: "))
    print("Is prime?", is_prime(n))
