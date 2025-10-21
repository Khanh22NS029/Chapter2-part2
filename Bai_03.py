# Bài 3: Viết một chương trình kiểm tra một chuỗi có trong chuỗi khác.
# Yêu cầu: Nhập vào một chuỗi st. Nhập vào chuỗi cần tìm st_search.
# Nếu có thì in ra màn hình "Đã tìm thấy chuỗi cần tìm, tại vị trí: ...".
# Ngược lại in "Không tìm thấy".

st = input("Nhập vào chuỗi: ")
st_search = input("Nhập chuỗi cần tìm: ")

if st_search in st:
    print("Đã tìm thấy chuỗi cần tìm, tại vị trí:", st.find(st_search))
else:
    print("Không tìm thấy")
