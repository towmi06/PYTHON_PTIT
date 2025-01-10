class Mua:
    cnt = 0

    def __init__(self, ten, gio, luong):
        Mua.cnt += 1
        self.ma = f'T{Mua.cnt:02d}'
        self.ten = ten
        self.gio = gio
        self.luong = luong

    def tb(self):
        return self.luong / self.gio

    def __str__(self):
        return f'{self.ma} {self.ten} {self.tb():.2f}'


if __name__ == '__main__':
    n = int(input())
    a = {}
    for _ in range(n):
        ten = input().strip()
        bd = list(map(int, input().split(':')))
        kt = list(map(int, input().split(':')))
        luong = int(input())
        
        # Tính số giờ làm
        gio = (kt[0] - bd[0]) + (kt[1] - bd[1]) / 60
        if gio < 0: # Nếu giờ kết thúc < giờ bắt đầu thì cộng thêm 24
            gio += 24

        if ten not in a:
            a[ten] = [gio, luong]
        else:
            a[ten][0] += gio
            a[ten][1] += luong

    for key, value in a.items():
        print(Mua(key, value[0], value[1]))
