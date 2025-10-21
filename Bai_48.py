# Bài 48: Hàm có 3 tham số trả về giá trị trung bình của chúng.
def avg(a,b,c):
    return (a+b+c)/3.0

if __name__ == '__main__':
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print("Trung bình:", avg(a,b,c))
