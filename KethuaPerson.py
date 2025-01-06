from datetime import*
class Person:
    def __init__(self, ten, ns, dc):
        self.ten = ten
        self.ns = ns
        self.dc = dc

class Student(Person):
    cnt =0
    def __init__(self, ten, ns, dc, lop, gpa):
        super().__init__(ten, ns, dc)
        Student.cnt +=1
        self.msv = f'{Student.cnt:04d}'
        self.lop = lop
        self.gpa = gpa

    def chuanhoaDate(self):
        NgaySinh = datetime.strptime(self.ns,'%d/%m/%Y')
        self.ns = datetime.strftime(NgaySinh,'%d/%m/%Y')
    def __str__(self):
        self.chuanhoaDate()
        return f'{self.msv} {self.ten.title()} {self.ns} {self.dc} {self.lop} {self.gpa:.2f}'

if __name__ == '__main__':
    n = int(input())
    a = []

    for _ in range (n):
        sv = Student(input(),input(),input(),input(),float(input()))
        a.append(sv)
    for i in a:
        print(i)


