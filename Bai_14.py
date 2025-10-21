# Bài 14: Tìm tất cả các số trong [100,300] sao cho mọi chữ số đều là số chẵn.
values = []
for i in range(100, 301):
    s = str(i)
    if all((int(ch) % 2 == 0) for ch in s):
        values.append(s)
print(",".join(values))
