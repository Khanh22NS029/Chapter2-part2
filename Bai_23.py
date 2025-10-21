# Bài 23: Định nghĩa hàm Check_chan(n) kiểm tra số chẵn trong file Kiem_tra.py
# (Ở đây chỉ minh họa nội dung; lưu dưới tên Bai_23.py)
def Check_chan(x):
    if x % 2 == 0:
        print(x, "là số chẵn")
    else:
        print(x, "là số lẻ")

if __name__ == '__main__':
    n = int(input("Nhập vào một số để kiểm tra: "))
    Check_chan(n)
