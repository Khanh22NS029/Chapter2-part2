# Bài 29: Phân loại tam giác theo độ dài ba cạnh.
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))

# Kiểm tra điều kiện tam giác
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Không phải tam giác hợp lệ.")
else:
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or b == c or a == c:
        print("Tam giác cân.")
    else:
        print("Tam giác thường.")
