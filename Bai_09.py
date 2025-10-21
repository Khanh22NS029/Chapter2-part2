# Bài 9: Tách từ thành danh sách và sắp xếp theo alphabet.
my_str = input("Nhập chuỗi: ")
ds_tu = my_str.split()
ds_tu.sort()
print("Các từ đã tách và sắp xếp theo alphabet:")
for tu in ds_tu:
    print(tu)
