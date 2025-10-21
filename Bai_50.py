# Bài 50: Tạo mật khẩu ngẫu nhiên độ dài ngẫu nhiên 7..10 ký tự, ký tự ASCII 33..126.
import random
import string

def make_password():
    length = random.randint(7, 10)
    pwd = ''.join(chr(random.randint(33,126)) for _ in range(length))
    return pwd

if __name__ == '__main__':
    print("Mật khẩu ngẫu nhiên:", make_password())
