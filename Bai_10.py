# Bài 10: Nhập các số từ bàn phím, khi nhập "done" dừng, in giá trị trung bình.
total = 0.0
count = 0
while True:
    inp = input("Enter a number (hoặc 'done' để kết thúc): ")
    if inp.lower() == "done":
        break
    try:
        value = float(inp)
    except:
        print("Giá trị không hợp lệ, thử lại.")
        continue
    total += value
    count += 1

if count == 0:
    print("Không có giá trị để tính.")
else:
    average = total / count
    print("Average is:", average)
