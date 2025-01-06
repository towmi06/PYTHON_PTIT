import sys
class SinhVien:
    def __init__(self,ma, ten, lop,email):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.email = email

    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.email}'

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range (n):
        sv  = SinhVien(input(), input(), input(), input())
        a.append(sv)
# sắp xếp theo lớp tăng dần (thứ tự từ điển).
 #Nếu 2 sinh viên có cùng lớp thì sắp xếp theo mã tăng dần (thứ tự từ điển)
    a.sort(key = lambda x:  (x.ma, x.ten))
    for i in a:
        print (i)