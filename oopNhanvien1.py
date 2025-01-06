from math import*
from functools import cmp_to_key
from datetime import*
class Nhanvien:
    cnt = 0
    def __init__(self, ten,gt, ns, dc,mst,ngayKi):
        Nhanvien.cnt +=1
        self.ma = f'{Nhanvien.cnt:05d}'
        self.ten = ten
        self.gt = gt
        self.ns = ns
        self.dc = dc
        self.mst = mst
        self.ngayKi = ngayKi

    def chuanHoa(self):
        ch_ns = datetime.strptime(self.ns, '%d/%m/%Y')
        ch_nk = datetime.strptime(self.ngayKi, '%d/%m/%Y')

        self.ns = ch_ns.strftime('%d/%m/%Y')
        self.ngayKi = ch_nk.strftime('%d/%m/%Y')
    def get_ns(self):
        return self.ns
    def get_ma(self):
        return self.ma
    def __str__(self):
        return f'{self.ma} {self.ten} {self.gt} {self.ns} {self.dc} {self.mst} {self.ngayKi}'

#cach dung cmp de sort ngay
def comp(a, b):
    # So sánh ngày sinh tăng dần
    if a.get_ns() != b.get_ns():
        return -1 if a.get_ns() < b.get_ns() else 1
    # Nếu ngày sinh bằng nhau, so sánh mã tăng dần
    return -1 if a.get_ma() < b.get_ma() else 1
'''
    ns1 = a.get_ns
    ns2 = b.get_ns
    a1 = list(map(int,ns1.split('/')))
    a2 = list(map(int, ns2.split('/')))
    for i in range(-1, -4, -1):
        if a1[i] != a2[i]:
            return -1 if a1[i] < a2[i] else 1
    ma1, ma2 = a.get_ma(), b.get_ma()
    return 1 if ma1 < ma2 else -1
'''

if  __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range (n):
        nv = Nhanvien(input(), input(), input(), input(),input(), input())
        nv.chuanHoa()
        a.append(nv)

    #sap xep ngay sinh tu gia -> ter , bang thi theo ma
    a.sort(key=lambda x: datetime.strptime(x.ns, '%d/%m/%Y'))
    #a.sort(key = cmp_to_key(comp))
    for x in a:
        print(x)
