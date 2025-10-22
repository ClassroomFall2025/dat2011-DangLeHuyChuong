import statistics
def doc_du_lieu(ten_file):
    """Đọc file và trả về danh sách các số nguyên."""
    with open(ten_file, "r") as f:
        du_lieu = f.read().split()
    return list(map(int, du_lieu))

def tinh_thong_ke(du_lieu):
    """Tính trung bình và độ lệch chuẩn của dữ liệu."""
    trung_binh = statistics.mean(du_lieu)
    do_lech_chuan = statistics.stdev(du_lieu)
    return trung_binh, do_lech_chuan


def doc_du_lieu_iterator(ten_file):
    """Dùng iterator để đọc từng phần tử (cho dữ liệu lớn)."""
    with open(ten_file, "r") as f:
        for so in f.read().split():
            yield int(so)
