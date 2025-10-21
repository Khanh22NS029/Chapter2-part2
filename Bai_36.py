# Bài 36: Đọc số nguyên đến khi nhập 0, lưu vào danh sách, in ra theo thứ tự tăng dần (không gồm 0).
nums = []
while True:
    inp = input("Nhập số nguyên (nhập 0 để dừng): ")
    try:
        v = int(inp)
    except:
        print("Giá trị không hợp lệ.")
        continue
    if v == 0:
        break
    nums.append(v)
nums.sort()
for v in nums:
    print(v)
