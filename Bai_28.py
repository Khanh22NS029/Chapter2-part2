# Bài 28: Nhập tên tháng, hiển thị số ngày (tháng 2 là 28 hoặc 29).
month = input("Nhập tên tháng (việt/eng): ").strip().lower()
thang_31 = {'1','3','5','7','8','10','12','january','march','may','july','august','october','december'}
thang_30 = {'4','6','9','11','april','june','september','november'}
if month in ('2','february','tháng 2','thang 2'):
    print("Tháng 2 có 28 hoặc 29 ngày.")
elif month in thang_31:
    print("Tháng này có 31 ngày.")
elif month in thang_30:
    print("Tháng này có 30 ngày.")
else:
    print("Không nhận diện được tháng.")
