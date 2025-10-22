source_file = "ASM_GD2.py"
target_file = "ASM_GD2.txt"
with open(source_file, "r", encoding="utf-8") as f_src:
    noi_dung = f_src.read()
with open(target_file, "w", encoding="utf-8") as f_dst:
    f_dst.write(noi_dung)
print(f"Đã sao chép nội dung từ {source_file} sang {target_file}")

from nhanvien import NhanVien, TiepThi, TruongPhong
ds = []
def nhap_danh_sach_nv():
    print("Nhập danh sách nhân viên: ")
    while True:
        loai = input("Nhập loại nhân viên (1: Nhân viên, 2: Tiếp thị, 3: Trưởng phòng, 0: Thoát): ")
        if loai == '0':
            break
        ma_nv = input("Mã nhân viên: ")
        ten_nv = input("Tên nhân viên: ")
        luong_cb = float(input("Lương cơ bản: "))
        if loai == '1':
            nv = NhanVien(ma_nv, ten_nv, luong_cb)
        elif loai == '2':
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Hoa hồng (%): ")) / 100
            nv = TiepThi(ma_nv, ten_nv, luong_cb, doanh_so, hoa_hong)
        elif loai == '3':
            luong_trach_nhiem = float(input("Lương trách nhiệm: "))
            nv = TruongPhong(ma_nv, ten_nv, luong_cb, luong_trach_nhiem)
        else:
            print("Loại nhân viên không hợp lệ!")
            continue
        ds.append(nv)
        print("Đã thêm nhân viên.")
print(">> Chức năng 1: Nhập danh sách nhân viên và lưu vào file")

def doc_file_nv():
    print(">> Chức năng 2: Đọc thông tin nhân viên từ file và xuất ra màn hình")
    
def tim_kiem_nv():
    ma_nv = input("Nhập mã nhân viên cần tìm: ")
    for nv in ds:
        if nv.get_ma_nv() == ma_nv:
            print(nv)
            return
    print("Không tìm thấy nhân viên với mã đã cho.")
print(">> Chức năng 3: Tìm và hiển thị nhân viên theo mã")

def xoa_nv_theo_ma():
    print(">> Chức năng 4: Xóa nhân viên theo mã và cập nhật file dữ liệu")
    
def cap_nhat_nv():
    print(">> Chức năng 5: Cập nhật thông tin nhân viên")
    
def tim_nhan_vien_theo_khoang_luong():
    min_luong = float(input("Nhập mức lương tối thiểu: "))
    max_luong = float(input("Nhập mức lương tối đa: "))
    found = [nv for nv in ds if min_luong <= nv.get_thu_nhap() <= max_luong]
    if found:
        for nv in found:
            print(nv)
    else:
        print("Không có nhân viên nào trong khoảng lương đã cho.")
print(">> Chức năng 6: Tìm nhân viên theo khoảng lương")
def sap_xep_nv_theo_ten():
    ds.sort(key=lambda nv: nv.get_ten_nv())
    print("Danh sách nhân viên sau khi sắp xếp theo tên:")
    for nv in ds:
        print(nv)
print(">> Chức năng 7: Sắp xếp nhân viên theo họ tên")
def sap_xep_nv_theo_thu_nhap():
    ds.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
    print("Danh sách nhân viên sau khi sắp xếp theo thu nhập giảm dần:")
    for nv in ds:
        print(nv)
print(">> Chức năng 8: Sắp xếp nhân viên theo thu nhập")
def xuat_5_nv_thu_nhap_cao_nhat():
    top5 = sorted(ds, key=lambda nv: nv.get_thu_nhap(), reverse=True)
    print("5 nhân viên có thu nhập cao nhất:")
    for nv in top5[:5]:
        print(nv)
print(">> Chức năng 9: Xuất 5 nhân viên có thu nhập cao nhất")
def thoat():
    print("Thoát chương trình.")