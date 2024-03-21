# Nhập điểm các môn
diem_toan = float(input("Nhập điểm Toán: "))
diem_van = float(input("Nhập điểm Văn: "))
diem_anh = float(input("Nhập điểm Anh: "))

# Kiểm tra điểm hợp lệ
if 0 <= diem_toan <= 10 and 0 <= diem_van <= 10 and 0 <= diem_anh <= 10:
    # Tính điểm trung bình
    diem_tb = (diem_toan + diem_van + diem_anh) / 3
    
    # Xét điều kiện để đánh giá học sinh
    if diem_tb >= 8 and diem_toan >= 8 and diem_van >= 8 and diem_anh >= 8:
        print("Học sinh giỏi")
    elif diem_tb >= 6.5 and diem_toan >= 6.5 and diem_van >= 6.5 and diem_anh >= 6.5:
        print("Học sinh khá")
    elif diem_tb >= 5 and diem_toan >= 5 and diem_van >= 5 and diem_anh >= 5:
        print("Học sinh trung bình")
    elif diem_tb >= 3.5 and diem_toan >= 3.5 and diem_van >= 3.5 and diem_anh >= 3.5:
        print("Học sinh yếu")
    else:
        print("Học sinh kém")
else:
    print("Điểm không hợp lệ, hãy nhập điểm trong khoảng từ 0 đến 10")

