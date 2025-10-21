# Bài 11: Nhập các số lưu vào danh sách, khi nhập "done" dừng, in trung bình và danh sách.
numlist = []
while True:
    inp = input("Enter a number (hoặc 'done' để kết thúc): ")
    if inp.lower() == "done":
        break
    try:
        value = float(inp)
    except:
        print("Giá trị không hợp lệ, thử lại.")
        continue
    numlist.append(value)

if len(numlist) == 0:
    print("Không có giá trị.")
else:
    average = sum(numlist) / len(numlist)
    print("Giá trị trung bình:", average)
    print("Danh sách:", numlist)
