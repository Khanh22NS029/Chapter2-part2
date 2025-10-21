# Bài 27: Xác định tên hình dạng dựa trên số cạnh (3..10).
n = int(input("Nhập số cạnh (3-10): "))
mapping = {
    3: "Tam giác",
    4: "Tứ giác",
    5: "Ngũ giác",
    6: "Lục giác",
    7: "Thất giác",
    8: "Bát giác",
    9: "Cửu giác",
    10: "Thập giác"
}
print(mapping.get(n, "Lỗi: chương trình chỉ hỗ trợ 3 đến 10 cạnh."))
