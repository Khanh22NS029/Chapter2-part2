# Bài 8: Loại bỏ các ký tự không phải chữ cái hoặc số trong một chuỗi.
st1 = "!()-[]{};:'\"\\,<>./?@#$%^&*_~ "
my_str = input("Nhập chuỗi: ")
st2 = ""
for ch in my_str:
    if ch.isalnum() or ch.isspace():
        st2 += ch
print("Kết quả:", st2)
