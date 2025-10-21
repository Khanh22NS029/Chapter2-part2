# Bài 43: Hàm in chuỗi có độ dài lớn hơn hoặc in cả hai nếu bằng.
def longer(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)

if __name__ == '__main__':
    a = input("Chuỗi 1: ")
    b = input("Chuỗi 2: ")
    longer(a,b)
