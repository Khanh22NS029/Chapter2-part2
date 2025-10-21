# Bài 51: Kiểm tra mật khẩu có tốt không (ít nhất 8 ký tự, có hoa, thường, số).
def good_password(pw):
    if len(pw) < 8:
        return False
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    return has_upper and has_lower and has_digit

if __name__ == '__main__':
    pw = input("Nhập mật khẩu: ")
    print("Mật khẩu tốt?" , good_password(pw))
