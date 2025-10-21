# Bài 2: Viết một chương trình kiểm tra một chuỗi nhập vào từ bàn phím:
# - Nếu chuỗi toàn chữ hoa → in ra “Chuỗi hoa”
# - Nếu chuỗi toàn chữ thường → in ra “Chuỗi thường”
# - Nếu chuỗi chứa cả chữ hoa và chữ thường → in ra “Chuỗi chứa ký tự hoa và ký tự thường”

# Nhập chuỗi từ bàn phím
st = input("Nhập vào một chuỗi: ")

# Kiểm tra loại chuỗi
if st.isupper():
    print("Đây là chuỗi hoa")
elif st.islower():
    print("Đây là chuỗi thường")
else:
    print("Chuỗi chứa cả ký tự hoa và ký tự thường")
