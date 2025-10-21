# Bài 30: Kiểm tra năm nhuận.
year = int(input("Nhập năm: "))
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print(year, "là năm nhuận.")
else:
    print(year, "không phải là năm nhuận.")
