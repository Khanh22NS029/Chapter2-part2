# Bài 25: Tạo tu_dien.py với các hàm thao tác từ điển (ở đây lưu chung).
def tao_TD(Max):
    d = {}
    for i in range(1, Max+1):
        d[i] = i**2
    return d

def Print_Item(TD):
    for k, v in TD.items():
        print(k, v)

def Print_key(TD):
    for k in TD.keys():
        print(k)

def Print_value(TD):
    for v in TD.values():
        print(v)

if __name__ == '__main__':
    maxv = int(input("Nhập Max: "))
    TD = tao_TD(maxv)
    print("Các phần tử của từ điển:")
    Print_Item(TD)
    print("Khoá của từ điển:")
    Print_key(TD)
    print("Giá trị của từ điển:")
    Print_value(TD)
