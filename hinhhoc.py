class ChuNhat:
    
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) *2 
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def xuat(self):
        print("Chiều dài: ", self.chieu_dai)
        print("Chiều rộng: ", self.chieu_rong)
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")
    
class Vuong(ChuNhat):
    
    def __init__(self, canh):
        super(Vuong, self).__init__(canh, canh)
        self.canh = canh
        
    def xuat(self):
        print(f"Cạnh: {self.canh}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")
