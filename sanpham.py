class SanPham:
    def __init__(self, ten="", gia=0, giam_gia=0):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia

    @property
    def ten(self):
        """Getter cho tên sản phẩm"""
        return self.__ten

    @ten.setter
    def ten(self, value):
        """Setter cho tên sản phẩm"""
        self.__ten = value

    @property
    def gia(self):
        """Getter cho giá sản phẩm"""
        return self.__gia

    @gia.setter
    def gia(self, value):
        """Setter cho giá sản phẩm"""
        if value < 0:
            print("Giá không thể là số âm. Gán giá trị bằng 0.")
            self.__gia = 0
        else:
            self.__gia = value

    @property
    def giam_gia(self):
        """Getter cho giảm giá"""
        return self.__giam_gia

    @giam_gia.setter
    def giam_gia(self, value):
        """Setter cho giảm giá"""
        self.__giam_gia = value
        
    def nhap(self):
        self.ten = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập đơn giá: "))
        self.giam_gia = float(input("Nhập số tiền giảm giá: "))

    def tinh_thue_nhap_khau(self):
        return self.gia * 0.1

    def xuat_thong_tin(self):
        print("Tên sản phẩm:", self.ten)
        print("Đơn giá:", self.gia)
        print("Giảm giá:", self.giam_gia)
        print("Thuế nhập khẩu:", self.tinh_thue_nhap_khau())