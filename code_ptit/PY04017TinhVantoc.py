class tsinh:
    def __init__(self, ten, donVi, thoiGian) :
        a = [i[0] for i in ten.split()]
        b = [i[0] for i in donVi.split()]
        self.id = ''.join(b) + ''.join(a)
        self.ten = ten
        self.donVi = donVi
        c = thoiGian.split(':')
        self.vanToc = 120 / (int(c[0]) - 6 + int(c[1]) / 60)

    def __str__(self) :
        return f"{self.id} {self.ten} {self.donVi} {round(self.vanToc)} Km/h"
        

n = int(input())
a=[]
for _ in range(n):
    a.append(tsinh(input(), input(), input()))
    
a = sorted(a, key = lambda x: -x.vanToc)
print(*a, sep = '\n')


