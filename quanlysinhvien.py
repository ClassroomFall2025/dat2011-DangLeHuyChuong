from sinhvienpoly import SinhVienIT, SinhVienBiz

danh_sach = []

def nhap_sinh_vien():
    print("NHẬP THÔNG TIN SINH VIÊN")
    loai = input("Nhập loại sinh viên (IT/Biz): ").strip().lower()
    ho_ten = input("Họ tên: ")

    if loai == "it":
        diem_java = float(input("Điểm Java: "))
        diem_html = float(input("Điểm HTML: "))
        diem_css = float(input("Điểm CSS: "))
        sv = SinhVienIT(ho_ten, diem_java, diem_html, diem_css)
    elif loai == "biz":
        diem_marketing = float(input("Điểm Marketing: "))
        diem_sales = float(input("Điểm Sales: "))
        sv = SinhVienBiz(ho_ten, diem_marketing, diem_sales)
    else:
        print("Loại sinh viên không hợp lệ!")
        return

    danh_sach.append(sv)
    print("Đã thêm sinh viên thành công!\n")


def xuat_danh_sach():
    print("\nDANH SÁCH SINH VIÊN")
    if not danh_sach:
        print("Danh sách rỗng!")
    for sv in danh_sach:
        sv.xuat()
        print("-" * 30)


def xuat_sv_gioi():
    print("\nDANH SÁCH SINH VIÊN GIỎI")
    ds_gioi = [sv for sv in danh_sach if sv.get_hoc_luc() == "Giỏi"]
    if not ds_gioi:
        print("Không có sinh viên giỏi nào.")
    for sv in ds_gioi:
        sv.xuat()
        print("-" * 30)


def sap_xep_theo_diem():
    print("\nSẮP XẾP DANH SÁCH THEO ĐIỂM GIẢM DẦN")
    danh_sach.sort(key=lambda sv: sv.get_diem(), reverse=True)
    xuat_danh_sach()
