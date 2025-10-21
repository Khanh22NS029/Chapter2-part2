# Bài 1: Viết một chương trình nhập vào một số nguyên dương.
# Nếu nó là số chẵn thì in ra chuỗi “Đây là số chẵn”,
# ngược lại thì in ra chuỗi “Đây là số lẻ”.

# Nhập vào một số nguyên dương
number = int(input("Nhập vào một số nguyên dương: "))

# Kiểm tra số chẵn hay lẻ
if number % 2 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")
