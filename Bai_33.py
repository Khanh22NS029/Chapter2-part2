# Bài 33: Kiểm tra một chuỗi có phải palindrome không.
s = input("Nhập chuỗi: ").strip()
# Loại bỏ khoảng trắng để kiểm tra
s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
if s2 == s2[::-1]:
    print("Là palindrome.")
else:
    print("Không phải palindrome.")
