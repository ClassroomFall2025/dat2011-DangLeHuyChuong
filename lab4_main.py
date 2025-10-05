import lab4_module

san_luong = int(input("Nhập số m3 nước đã sử dụng: "))
tien = lab4_module.tinh_tien_nuoc(san_luong)
print(f"Số tiền nước phải trả: {tien} VND")



import lab4_module   
so_dx = int(input("Nhập số bánh đậu xanh: "))
so_tc = int(input("Nhập số bánh thập cẩm: "))
so_deo = int(input("Nhập số bánh dẻo: "))

ket_qua = lab4_module.tinh_nguyen_lieu(so_dx, so_tc, so_deo)

print("Nguyên liệu cần thiết:")
print("Đường:", ket_qua["sugar"], "kg")
print("Đậu:", ket_qua["bean"], "kg")



import lab4_module
my_list = list(map(int, input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ").split()))
ket_qua = lab4_module.loc_so_chan(my_list)
print("Các số chẵn là:", ket_qua)
