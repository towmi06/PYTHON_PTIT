
class Staff:
    cnt =0
    def __init__(self, ten, th, lt):
        Staff.cnt +=1
        self.ma = f'TS0{Staff.cnt:01d}'
        self.ten = ten
        self.th = th
        self.lt = lt
        self.get_diem()

    def get_diem(self):
        if self.th > 10:
            self.th = self.th/ 10
        if self.lt > 10:
            self.lt = self.lt/10
        return (self.lt + self.th)/2

    def xeploai(self):
        x = self.get_diem()
        if x> 9.5: return 'XUAT SAC'
        elif 8 <= x <= 9.5: return 'DAT'
        elif 5 <= x < 8: return 'CAN NHAC'
        else: return 'TRUOT'

    def __str__(self):
        return f'{self.ma} {self.ten} {self.get_diem():.02f} {self.xeploai()}'

if __name__ =='__main__':
    n = int(input())
    a = []
    for _ in range(n):
        nv = Staff(input(),  float(input()), float(input()))
        a.append(nv)
    a.sort(key = lambda x: -x.get_diem())
    for i in a:
        print(i)
