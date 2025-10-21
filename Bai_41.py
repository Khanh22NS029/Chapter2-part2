# Bài 41: Tạo tuple chứa các số chẵn từ tuple ban đầu.
t = (1,2,3,4,5,6,7,8,9,10)
evens = tuple(x for x in t if x%2==0)
print(evens)
