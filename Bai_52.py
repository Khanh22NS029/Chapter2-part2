# Bài 52: Kiểm tra số hoàn hảo; in tất cả số hoàn hảo từ 1 đến 10000.
def is_perfect(n):
    if n <= 1:
        return False
    s = 1
    i = 2
    while i*i <= n:
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
        i += 1
    return s == n

perfects = [i for i in range(1, 10001) if is_perfect(i)]
print("Các số hoàn hảo trong 1..10000:", perfects)
