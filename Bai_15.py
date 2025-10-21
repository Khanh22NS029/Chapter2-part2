# Bài 15: Nhập một chuỗi số phân tách bằng dấu phẩy, in danh sách và tuple.
chuoi = input("Nhập các giá trị phân tách bằng dấu phẩy: ")
kieu_ds = chuoi.split(",")
kieu_tuple = tuple(kieu_ds)
print(kieu_ds)
print(kieu_tuple)
