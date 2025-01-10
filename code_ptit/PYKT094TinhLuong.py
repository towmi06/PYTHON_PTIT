class Nhanvien:
    def __init__ (self, ma,ten, phong, lcb, cong):
        self.ma = ma
        self.ten = ten 
        self.phong = phong
        self.lcb = lcb 
        self.cong = cong
        self.loai = ma[0]
        self.nam = int(ma[1:3])
    def luong(self):
        l,n = self.loai,  self.nam
        hso = 0
        if l =='A':
            if 1 <= n <= 3: hso = 10
            elif 4 <= n <= 8: hso = 12
            elif 9 <= n <= 15: hso = 14
            elif n>=16: hso = 20
        elif l == 'B':
            if 1 <= n <= 3: hso = 10
            elif 4 <= n <= 8: hso = 11
            elif 9 <= n <= 15: hso = 13
            elif n>=16: hso = 16
        elif l == 'C':
            if 1 <= n <= 3: hso = 9
            elif 4 <= n <= 8: hso = 10
            elif 9 <= n <= 15: hso = 12
            elif n>=16: hso = 14
        elif l =='D':
            if 1 <= n <= 3: hso = 8
            elif 4 <= n <= 8: hso = 9
            elif 9 <= n <= 15: hso = 11
            elif n>=16: hso = 13
        return hso * self.lcb * self.cong
    def __str__(self):
        return f'{self.ma} {self.ten} {self.phong} {self.luong()}000'

if __name__ =='__main__':
    phong,nv =[],[]
    for _ in range(int(input())):
        m = input().split()
        phong.append((m[0],m[1:]))
    for _ in range(int(input())):
        ma, ten , lcb, cong = input().strip(), input().strip(), int(input()), int(input())
        for i in range(len(phong)):
            if phong[i][0] == ma[-2:]:
                nv.append(Nhanvien(ma, ten, ' '.join(phong[i][1]), lcb, cong))
    print(*nv, sep ='\n')


