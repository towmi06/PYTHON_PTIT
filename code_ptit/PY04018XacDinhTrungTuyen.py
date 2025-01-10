d =[0.0,2.0,1.5,1.0,0.0]

class giaovien:
    cnt = 0
    def __init__ (self, ten, ma, tin ,cm):
        giaovien.cnt +=1
        self.id = f'GV{giaovien.cnt:02d}'
        self.ten = ten 
        self.ut = int(ma[-1])
        self.mon = ma[0]
        self.tin = tin
        self.cm = cm
        self.tong = (self.tin)*2 +self.cm + d[self.ut]

    def xeploai(self):
        return f'{self.tong:.1f} TRUNG TUYEN' if self.tong >=18.0 else f'{self.tong:.1f} LOAI'
    
    def chuyenmon(self):
        return 'TOAN' if self.mon  == 'A' else 'LY' if self.mon =='B' else 'HOA'
    def __str__(self):
        return f'{self.id} {self.ten} {self.chuyenmon()} {self.xeploai()}'

a = []
for _ in range(int(input())):
    a.append(giaovien(input(), input(), float(input()), float(input())))
a.sort(key = lambda x: -x.tong)
print(*a, sep = '\n')

