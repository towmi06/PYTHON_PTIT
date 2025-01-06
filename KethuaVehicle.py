class Vehicle:
    def __init__(self, ma, ten, hang, mau, gia):
        self.ma = ma
        self.ten = ten
        self.hang = hang
        self.mau = mau
        self.gia = gia

class Moto(Vehicle):
    def __init__(self, ma, ten, hang, mau, td, gia):
        super().__init__(ma, ten, hang, mau, gia)
        self.td = td

    def __str__(self):
        return f"{self.ma} {self.ten} {self.hang} {self.mau} {self.td} {self.gia}"

class Oto(Vehicle):
    def __init__(self, ma, ten, hang, mau, mluc, gia):
        super().__init__(ma, ten, hang, mau, gia)
        self.mluc = mluc

    def __str__(self):
        return f"{self.ma} {self.ten} {self.hang} {self.mau} {self.mluc} {self.gia}"

if __name__ == '__main__':
    n = int(input())
    oto_list = []
    moto_list = []

    for _ in range(n):
        ma = input().strip()
        ten = input().strip()
        hang = input().strip()
        mau = input().strip()
        if ma.startswith("XM"):
            td = int(input().strip())
            gia = int(input().strip())
            moto_list.append(Moto(ma, ten, hang, mau, td, gia))
        elif ma.startswith("OTO"):
            mluc = int(input().strip())
            gia = int(input().strip())
            oto_list.append(Oto(ma, ten, hang, mau, mluc, gia))

    hang_can_tim = input().strip()

    print(f"DANH SACH XE HANG {hang_can_tim} :")

    for oto in oto_list:
        if oto.hang == hang_can_tim:
            print(oto)

    for moto in moto_list:
        if moto.hang == hang_can_tim:
            print(moto)
