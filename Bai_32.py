# Bài 32: Mã hóa/giải mã Caesar với số dịch chuyển do người dùng nhập.
def caesar(text, shift, mode='enc'):
    if mode == 'dec':
        shift = -shift
    out = []
    for ch in text:
        if ch.isupper():
            out.append(chr((ord(ch)-65+shift)%26 + 65))
        elif ch.islower():
            out.append(chr((ord(ch)-97+shift)%26 + 97))
        else:
            out.append(ch)
    return ''.join(out)

mode = input("Chọn 'enc' để mã hóa hoặc 'dec' để giải mã: ").strip().lower()
shift = int(input("Nhập số dịch chuyển (số nguyên): "))
text = input("Nhập chuỗi: ")
print("Kết quả:", caesar(text, shift, mode))
