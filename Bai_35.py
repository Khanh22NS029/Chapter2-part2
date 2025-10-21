# Bài 35: Tạo danh sách các số lẻ từ chuỗi số người dùng nhập (phân tách bằng dấu phẩy).
s = input("Nhập các số, phân tách bằng dấu phẩy: ")
nums = [int(x.strip()) for x in s.split(",") if x.strip()!='']
odds = [str(x) for x in nums if x % 2 != 0]
print(",".join(odds))
