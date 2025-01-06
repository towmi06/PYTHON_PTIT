class hcn:
    def __init__(self, dai, rong,mau):
        self.dai = dai
        self.rong  = rong
        self.mau = mau

    def tinh(self):
        c = (self.dai + self.rong) * 2
        s = self.dai * self.rong
        return f'{c} {s}'
    
    def __str__(self):
        if self.dai > 0 and self.rong > 0:
            return f'{self.tinh()} {self.mau.capitalize()}'
        else:
            return 'INVALID'
a= input().split()
r = hcn(int(a[0]), int(a[1]), a[2])
print(r)