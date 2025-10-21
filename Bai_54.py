# Bài 54: Định dạng danh sách từ tiếng Anh với dấu phẩy và 'and' trước từ cuối cùng.
def format_list(words):
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return words[0] + " and " + words[1]
    return ", ".join(words[:-1]) + " and " + words[-1]

if __name__ == '__main__':
    s = input("Nhập các từ, cách nhau bằng dấu phẩy: ")
    words = [w.strip() for w in s.split(",") if w.strip()!='']
    print(format_list(words))
