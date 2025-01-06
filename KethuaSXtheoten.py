from datetime import datetime

class Person:
    def __init__(self, ten, ns, dc):
        self.ten = ten
        self.ns = ns
        self.dc = dc
        self.chuanhoa()
    def chuanhoa(self):
        # Chuẩn hóa ngày sinh
        ngaysinh = datetime.strptime(self.ns, '%d/%m/%Y')
        self.ns = datetime.strftime(ngaysinh, '%d/%m/%Y')
        # Chuẩn hóa tên
        name_parts = self.ten.strip().split()
        self.ten = ' '.join(x.title() for x in name_parts)
        self.ten_cuoi = name_parts[-1]
        self.ten_dau = ' '.join(name_parts[:-1])

    def __str__(self):
        return f"{self.ten} {self.ns} {self.dc}"

class Student(Person):
    cnt = 0
    def __init__(self, ten, ns, dc, lop, gpa):
        super().__init__(ten, ns, dc)
        Student.cnt += 1
        self.ma = f'{Student.cnt:04d}'
        self.lop = lop
        self.gpa = gpa
        self.chuanhoa()

    def __str__(self):
        return f'{self.ma} {self.ten} {self.ns} {self.dc} {self.lop} {self.gpa:.2f}'


if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        sv = Student(input(), input(), input(), input(), float(input()))
        a.append(sv)
# Sap xep theo ten tang dan, sau do den ho 
# a.sort(key=lambda x: tuple(x.ten.split()[-1:] + x.ten.split()[:-1]))
    a.sort(key=lambda x: (x.ten_cuoi, x.ten_dau))
    for sv in a:
        print(sv)
