# Bài 40: Với tuple (1..10), in nửa phần tử đầu trên 1 dòng và nửa còn lại trên dòng khác.
t = (1,2,3,4,5,6,7,8,9,10)
mid = len(t)//2
print(t[:mid])
print(t[mid:])
