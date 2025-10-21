# Bài 22: Tạo danh sách bình phương 1..20 và in 5 phần tử đầu và 5 phần tử cuối.
def Tao_In_DS():
    ds = [i**2 for i in range(1,21)]
    print("5 phần tử đầu:", ds[:5])
    print("5 phần tử cuối:", ds[-5:])

Tao_In_DS()
