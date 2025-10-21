# Bài 53: Trả về danh sách chứa mọi danh sách con (subsets) của một danh sách.
def all_subsets(lst):
    res = [[]]
    for item in lst:
        res += [curr + [item] for curr in res]
    return res

if __name__ == '__main__':
    s = input("Nhập các phần tử, cách nhau bằng dấu phẩy: ")
    lst = [x.strip() for x in s.split(",") if x.strip()!='']
    print(all_subsets(lst))
