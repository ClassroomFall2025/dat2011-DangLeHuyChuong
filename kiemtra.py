import re
def kiem_tra_email(email):
    """Kiểm tra định dạng email hợp lệ"""
    mau_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(mau_email, email)

def kiem_tra_sdt(sdt):
    """Kiểm tra định dạng số điện thoại Việt Nam (10 số, bắt đầu bằng 0)"""
    mau_sdt = r'^(0[0-9]{9})$'
    return re.match(mau_sdt, sdt)

def nhap_thong_tin_sinh_vien():
    sinh_vien = {
        "Họ tên": input("Nhập họ tên: "),
        "Email": input("Nhập email: "),
        "Số điện thoại": input("Nhập số điện thoại: "),
        "CMND": input("Nhập số CMND: ")
    }
    return sinh_vien

def kiem_tra_thong_tin(sinh_vien):
    if not kiem_tra_email(sinh_vien["Email"]):
        print("Email sai (ví dụ hợp lệ: ten@gmail.com)")
    else:
        print("Email đúng")

    if not kiem_tra_sdt(sinh_vien["Số điện thoại"]):
        print("Số điện thoại sai(phải có 10 chữ số và bắt đầu bằng 0)")
    else:
        print("Số điện thoại đúng!")

    print("\n--- THÔNG TIN SINH VIÊN ---")
    for key, value in sinh_vien.items():
        print(f"{key}: {value}")
