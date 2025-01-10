from datetime import datetime

d=[0,25, 34, 50, 80]
class Hd:
    cnt = 0  
    def __init__(self, ten, phong, nhan, tra, dv):
        Hd.cnt += 1
        self.ma = f'KH{Hd.cnt:02d}'
        self.ten = ten.strip()
        self.phong = phong.strip()
        self.tang = int(self.phong[0])  # Tầng là chữ số đầu tiên của số phòng
        self.nhan = datetime.strptime(nhan.strip(), '%d/%m/%Y') 
        self.tra = datetime.strptime(tra.strip(), '%d/%m/%Y')  
        self.dv = dv 
        self.ngay = (self.tra - self.nhan).days +  1# Số ngày ở
    
    def tien(self):
        return d[self.tang] * self.ngay + self.dv
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.phong} {self.ngay} {round(self.tien())}'


a = []
for _ in range(int(input())):  

    a.append(Hd( input(), input(), input().strip(), input().strip(), int(input())))
    
a.sort(key=lambda x: -x.tien())
    
print(*a, sep='\n')
