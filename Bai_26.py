# Bài 26: Đọc một chữ cái; kiểm tra nguyên âm (a,e,i,o,u), y là có thể là nguyên âm hoặc phụ âm.
ch = input("Nhập một chữ cái: ").lower()
if ch in ('a','e','i','o','u'):
    print(ch, "là nguyên âm.")
elif ch == 'y':
    print(ch, "có thể là nguyên âm hoặc phụ âm.")
else:
    print(ch, "là phụ âm.")
