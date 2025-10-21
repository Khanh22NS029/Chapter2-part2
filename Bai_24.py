# Bài 24: Hàm nhận 2 chuỗi, in chuỗi có độ dài lớn hơn; nếu bằng thì in cả hai.
def printValue(s1, s2):
    if len(s1) > len(s2):
        print("Chuỗi dài hơn:", s1)
    elif len(s2) > len(s1):
        print("Chuỗi dài hơn:", s2)
    else:
        print(s1)
        print(s2)

if __name__ == '__main__':
    st1 = input("Nhập chuỗi thứ nhất: ")
    st2 = input("Nhập chuỗi thứ hai: ")
    printValue(st1, st2)
