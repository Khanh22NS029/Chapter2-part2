# Bài 31: Mã hóa Caesar chuyển mỗi chữ cái sang phải 3 vị trí; giữ nguyên ký tự khác.
def caesar_encrypt(text, shift=3):
    res = []
    for ch in text:
        if ch.isupper():
            res.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif ch.islower():
            res.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            res.append(ch)
    return ''.join(res)

msg = input("Nhập tin nhắn: ")
print("Tin nhắn đã mã hóa:", caesar_encrypt(msg, 3))
