class HDon:
    cnt = 0
    def __init__(self, ten, cso):
        HDon.cnt += 1
        self.ma = f'KH{HDon.cnt:02d}' 
        self.ten = ten
        self.cso = cso

    def tien(self):
        x = self.cso
        s = 0
        if 0 <= x <= 50:
            s = x * 100
            s+= s*0.02
            return round(s)
        elif 50<x<= 100: 
            s = x*150
            s += s*0.03
            return round(s)
        elif x > 100:
            s = x*200
            s += s*0.05
            return round(s)
    def __str__(self):
        return f'{self.ma} {self.ten} {self.tien()}'

if __name__ == '__main__':
    n = int(input())
    hoadon = []
    for _ in range(n):
        ten = input().strip()
        cu,moi = int(input()),int(input())
        cso = moi - cu
        hoadon.append(HDon(ten, cso))

    hoadon.sort(key=lambda x: x.tien(), reverse=True)
    print(*hoadon, sep='\n')
