d = {'A': 100, 'B': 500, 'C': 200}

class TienDien:
    cnt = 0

    def __init__(self, ten, loai, dau, cuoi):
        TienDien.cnt += 1
        self.ma = f'KH{TienDien.cnt:02d}'
        self.ten = ' '.join(ten.strip().split())  
        self.loai = loai.strip()
        self.dien = cuoi - dau  

    def tinh_tien(self):
        dinh_muc = d[self.loai]
        tien_dinh_muc = min(self.dien, dinh_muc) * 450  # Tiền trong định mức
        tien_vuot = max(0, (self.dien - dinh_muc)) * 1000  # Tiền vượt định mức
        thue_vat = tien_vuot // 20  # Thuế VAT
        tong_tien = tien_dinh_muc + tien_vuot + thue_vat  # Tổng tiền phải trả
        return tien_dinh_muc, tien_vuot, thue_vat, tong_tien

    def __str__(self):
        tien_dinh_muc, tien_vuot, thue_vat, tong_tien = self.tinh_tien()
        return f'{self.ma} {self.ten.title()} {tien_dinh_muc} {tien_vuot} {thue_vat} {tong_tien}'

if __name__ == '__main__':
    n = int(input())  
    a = []

    for _ in range(n):
        ten = input().strip() 
        loai, dau, cuoi = input().split()  
        a.append(TienDien(ten, loai, int(dau), int(cuoi)))

    # Sắp xếp danh sách theo tổng số tiền phải trả giảm dần
    a.sort(key=lambda x: -x.tinh_tien()[3])
    print(*a, sep='\n')
