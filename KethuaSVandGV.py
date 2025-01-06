from datetime import*

class Person:
    def __init__(self, ma, ten , ns, dc):
        self.ma = ma
        self.ten = ten
        self.ns = ns
        self.dc = dc
        self.chuanhoa()

    def chuanhoa(self):
        ngaysinh = datetime.strptime(self.ns, '%d/%m/%Y')
        self.ns = datetime.strftime(ngaysinh, '%d/%m/%Y')
        name = self.ten.strip().split()
        self.ten = ' '.join(x.title() for x in name)

    def __str__(self):
        return f'{self.ma} {self.ten} {self.ns} {self.dc}'
class Student(Person):
    def __init__(self, ma, ten, ns, dc, lop, gpa):
        super().__init__(ma,ten,ns,dc)
        self.lop = lop
        self.gpa = gpa

    def __str__(self):
        return f'{self.ma} {self.ten} {self.ns} {self.dc} {self.lop} {self.gpa:.2f}'

class GiaoVien(Person):
    def __init__(self,ma,ten,ns,dc,khoa,luong,lql):
        super().__init__(ma,ten,ns,dc)
        self.khoa = khoa
        self.luong = luong
        self.lql = lql
    def __str__(self):
        return f'{self.ma} {self.ten} {self.ns} {self.dc} {self.khoa} {self.luong}'

if __name__ == '__main__':
    n = int(input())
    sv = []
    gv=[]
    for _ in range (n):
        ma = input()
        if ma[:2] == 'SV':
            s = Student(ma, input(),input(),input(), input(),float(input()))
            sv.append(s)
        if ma[:2] == 'GV':
            g = GiaoVien(ma,input(), input(), input(), input(),int(input()),input())
            gv.append(g)

    q = input()
    print (f'DANH SACH GIAO VIEN CO DIA CHI TAI {q} :')
    for x in gv:
        if x.dc == q:
            print(x)
    print(f'DANH SACH SINH VIEN CO DIA CHI TAI {q} :')
    for x in sv:
        if x.dc == q:
            print(x)