class sinhvien:
    def __init__(self, msv, ten, lop,diemcc):
        self.msv = msv
        self.ten = ten 
        self.lop = lop
        self.diemcc = diemcc
    
    def diem(self):
        c = self.diemcc
        cc = c.count('x')
        mm = c.count('m')
        vv = c.count('v')
        d = 10 - mm*1 - vv*2
        return '0 KDDK' if d <= 0 else d
    
    def __str__(self):
        diemcc = self.diem()
        return f'{self.msv} {self.ten} {self.lop} {diemcc}'
    
if __name__ == '__main__':
    n = int(input())
    listsv=[]
    for _ in range (n):
        msv,ten,lop = input().strip(),input().strip(),input().strip()
        listsv.append(sinhvien(msv,ten,lop,''))
    for _ in range(n):
        cc = input().strip().split()
        for sv in listsv:
            if sv.msv == cc[0]:
                sv.diemcc = cc[1]
    for sv in listsv:
        print(sv)
