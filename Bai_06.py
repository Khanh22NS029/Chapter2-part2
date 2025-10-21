# Bài 6: Đếm số ký tự hoa và ký tự thường trong một câu nhập vào.
s = input("Nhập câu: ")
sum_upper = 0
sum_lower = 0
for c in s:
    if c.isupper():
        sum_upper += 1
    elif c.islower():
        sum_lower += 1
print("Chữ hoa:", sum_upper)
print("Chữ thường:", sum_lower)
