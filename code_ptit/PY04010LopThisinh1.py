from datetime import datetime

class sinhvien :
    def __init__(self, ten, ns, m1, m2, m3):
        self.ten = ten 
        self.ns = ns
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.tongdiem = self.m1 + self.m2 + self.m3 
        self.chuanhoangay()
    def  chuanhoangay(self):
        ngay = datetime.strptime(self.ns,'%d/%m/%Y')
        self.ns = ngay.strftime('%d/%m/%Y')
    def __str__(self):

        return f'{self.ten.title()} {self.ns} {self.tongdiem:.1f}'
    
if __name__ == '__main__':
    sv = sinhvien(input().strip(), input().strip(),float(input()), float(input()), float(input()))
    print(sv)

