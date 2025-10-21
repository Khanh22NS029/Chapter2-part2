# Bài 12: Tìm tất cả số chia hết cho 7 nhưng không phải bội của 5 trong đoạn [2000,3200].
res = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        res.append(str(i))
print(",".join(res))
