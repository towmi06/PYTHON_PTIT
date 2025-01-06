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
    def __init__(self,ma,ten,ns,dc,khoa,luong):
        super().__init__(ma,ten,ns,dc)
        self.khoa = khoa
        self.luong = luong
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
            g = GiaoVien(ma,input(), input(), input(), input(),int(input()))
            gv.append(g)

    sv.sort(key = lambda h: (-h.gpa, h.ma))
    gv.sort(key= lambda k: (-k.luong, k.ma))

    print ('DANH SACH GIAO VIEN :')
    for x in gv:
       print(x)

    print('DANH SACH SINH VIEN :')
    for x in sv:
        print(x)