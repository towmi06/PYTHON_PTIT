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
    moto_list, oto_list = [], []

    for _ in range(n):
        ma = input()
        if ma[:2] == 'XM':  # Xe máy
            moto_list.append(Moto(ma, input(), input(), input(), int(input()), int(input())))
        elif ma[:3] == 'OTO':  # Ô tô
            oto_list.append(Oto(ma, input(), input(), input(), int(input()), int(input())))

    a= input()

    if oto_list:
        print("DANH SACH OTO :")
        for oto in oto_list:
            if oto.ten == a:
                print(oto)

    if moto_list:
        print("DANH SACH XE MAY :")
        for moto in moto_list:
            if moto.ten == a:
                print(moto)
