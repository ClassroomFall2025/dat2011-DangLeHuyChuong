def tinh_tien_nuoc(san_luong):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if san_luong <= 10:
        tien = san_luong * gia_ban_nuoc[0]
    elif san_luong <= 20:
        tien = 10 * gia_ban_nuoc[0] + (san_luong - 10) * gia_ban_nuoc[1]
    elif san_luong <= 30:
        tien = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (san_luong - 20) * gia_ban_nuoc[2]
    else:
        tien = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (san_luong - 30) * gia_ban_nuoc[3]
    return tien


def tinh_nguyen_lieu(so_banh_dau_xanh, so_banh_thap_cam, so_banh_deo):
    sugar = so_banh_dau_xanh * 0.04 + so_banh_thap_cam * 0.06 + so_banh_deo * 0.05
    bean = so_banh_dau_xanh * 0.07 + so_banh_thap_cam * 0.0 + so_banh_deo * 0.02
    return {"sugar": sugar, "bean": bean}



def loc_so_chan(my_list):
    return list(filter(lambda x: x % 2 == 0, my_list))